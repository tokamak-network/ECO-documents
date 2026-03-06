#!/usr/bin/env python3
"""
T6: Claude API EVM Trace Analysis Accuracy Test

Usage:
  ANTHROPIC_API_KEY=sk-ant-... python3 t6_api_test.py --fixtures-dir ./fixtures/

Reads AgentContext JSON fixtures, sends to Claude (Haiku then Sonnet),
measures accuracy and collects token/cost data for T7.
"""

import json
import os
import sys
import time
import glob
import argparse
from pathlib import Path

try:
    import httpx
except ImportError:
    print("httpx not installed. Trying requests...")
    import requests as httpx

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
HAIKU_MODEL = "claude-haiku-4-5-20251001"
SONNET_MODEL = "claude-sonnet-4-6-20250514"
ESCALATION_THRESHOLD = 0.6
MAX_TOKENS = 4000

SYSTEM_PROMPT = """You are an expert EVM (Ethereum Virtual Machine) security analyst. Your job is to analyze structured transaction execution traces and determine whether a transaction is an attack or benign activity.

You will receive an AgentContext JSON containing:
- tx_hash, block_number, from, to: Transaction metadata
- value_wei, gas_used, succeeded: Execution result
- revert_count: Number of internal reverts (high = suspicious)
- suspicious_score: Pre-filter suspicion score (0.0-1.0)
- suspicion_reasons: Why the pre-filter flagged this TX
- call_graph: Internal call tree with depth, caller, target, value, call_type
- storage_mutations: Storage slot changes (in_callback=true is a reentrancy signal)
- erc20_transfers: ERC-20 Transfer events
- eth_transfers: ETH value transfers
- log_events: Non-Transfer events (Swap, Sync, Approval, etc.)
- delegatecalls: DELEGATECALL operations (proxy pattern indicator)
- contract_creations: CREATE/CREATE2 operations

## Attack Patterns to Look For

1. **Reentrancy**: External call at depth N followed by state modification at depth > N. Key signals: CALL with ETH value -> re-entry to same contract -> SSTORE during callback (in_callback=true).

2. **Flash Loan Attack**: Token transfer from pool -> callback execution at high depth -> manipulation -> repayment. Key signals: ERC-20 transfer pool->attacker early, attacker->pool late, >60% steps at elevated depth.

3. **Price Manipulation**: Oracle price read (STATICCALL) -> swap activity -> second oracle read with different price. Key signals: Two STATICCALLs to same address with transfers between them.

4. **Access Control Bypass**: DELEGATECALL to unauthorized implementation -> SSTORE to critical slot (slot 0 = proxy implementation). Key signals: DELEGATECALL without CALLER check, storage mutation in delegated context.

5. **Front-Running / Sandwich**: Multiple transactions in same block targeting same pool. (Note: single-TX context only -- limited detection.)

## Important Rules

- Base your judgment ONLY on the data provided in AgentContext. Do not hallucinate addresses, amounts, or events that are not in the input.
- Every piece of evidence you cite must reference actual data from the AgentContext (addresses, amounts, slots, depths).
- If unsure, lean toward conservative judgment (lower confidence, not false positive).
- A high suspicious_score alone is not proof of attack -- analyze the actual trace data.
- Normal DeFi operations (swaps, liquidity adds, governance votes) can look suspicious but are benign."""

TOOL_DEFINITION = {
    "name": "analyze_evm_trace",
    "description": "Analyze an EVM transaction trace and return a structured security verdict",
    "input_schema": {
        "type": "object",
        "properties": {
            "is_attack": {
                "type": "boolean",
                "description": "Whether this transaction is an attack"
            },
            "confidence": {
                "type": "number",
                "description": "Confidence level 0.0-1.0"
            },
            "attack_type": {
                "type": "string",
                "description": "Attack type. One of: reentrancy, flash_loan, price_manipulation, access_control, front_running, sandwich, none"
            },
            "reasoning": {
                "type": "string",
                "description": "Detailed reasoning for the verdict"
            },
            "evidence": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Key evidence items from the trace. Each must reference actual data from the AgentContext."
            },
            "false_positive_reason": {
                "type": "string",
                "description": "If is_attack=false, explain why this is not an attack despite suspicious signals"
            }
        },
        "required": ["is_attack", "confidence", "attack_type", "reasoning", "evidence"]
    }
}


def call_claude(api_key: str, model: str, context_json: str, use_cache: bool = True) -> dict:
    """Send AgentContext to Claude and get structured verdict via tool_use."""
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    if use_cache:
        headers["anthropic-beta"] = "prompt-caching-2024-07-31"

    system_content = [
        {
            "type": "text",
            "text": SYSTEM_PROMPT,
        }
    ]

    if use_cache:
        system_content[0]["cache_control"] = {"type": "ephemeral"}

    body = {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "system": system_content,
        "tools": [TOOL_DEFINITION],
        "tool_choice": {"type": "tool", "name": "analyze_evm_trace"},
        "messages": [
            {
                "role": "user",
                "content": f"Analyze this EVM transaction trace:\n\n{context_json}"
            }
        ]
    }

    start = time.time()

    if hasattr(httpx, 'Client'):
        # httpx
        with httpx.Client(timeout=60.0) as client:
            resp = client.post(ANTHROPIC_API_URL, headers=headers, json=body)
            resp.raise_for_status()
            data = resp.json()
    else:
        # requests
        resp = httpx.post(ANTHROPIC_API_URL, headers=headers, json=body, timeout=60)
        resp.raise_for_status()
        data = resp.json()

    latency_ms = int((time.time() - start) * 1000)

    # Extract tool_use response
    verdict = None
    for block in data.get("content", []):
        if block.get("type") == "tool_use" and block.get("name") == "analyze_evm_trace":
            verdict = block["input"]
            break

    usage = data.get("usage", {})

    return {
        "verdict": verdict,
        "usage": {
            "input_tokens": usage.get("input_tokens", 0),
            "output_tokens": usage.get("output_tokens", 0),
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
            "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
        },
        "model": model,
        "latency_ms": latency_ms,
    }


def load_fixtures(fixtures_dir: str) -> list[dict]:
    """Load fixture JSONs. Each file should have 'context' and 'expected' keys."""
    fixtures = []
    for path in sorted(glob.glob(os.path.join(fixtures_dir, "*.json"))):
        with open(path) as f:
            data = json.load(f)
        data["_filename"] = os.path.basename(path)
        fixtures.append(data)
    return fixtures


def evaluate(verdict: dict, expected: dict) -> bool:
    """Check if verdict matches expected classification."""
    if verdict is None:
        return False
    return verdict.get("is_attack", False) == expected.get("is_attack", False)


def calculate_cost(usage: dict, model: str) -> float:
    """Calculate cost in USD based on token usage and model."""
    if "haiku" in model:
        input_price = 1.0 / 1_000_000   # $1/MTok
        output_price = 5.0 / 1_000_000   # $5/MTok
        cache_write_price = 1.25 / 1_000_000  # 25% surcharge
        cache_read_price = 0.1 / 1_000_000    # 90% discount
    else:
        input_price = 3.0 / 1_000_000   # $3/MTok
        output_price = 15.0 / 1_000_000  # $15/MTok
        cache_write_price = 3.75 / 1_000_000
        cache_read_price = 0.3 / 1_000_000

    cost = (
        usage["input_tokens"] * input_price
        + usage["output_tokens"] * output_price
        + usage.get("cache_creation_input_tokens", 0) * cache_write_price
        + usage.get("cache_read_input_tokens", 0) * cache_read_price
    )
    return cost


def main():
    parser = argparse.ArgumentParser(description="T6: Claude API EVM Trace Accuracy Test")
    parser.add_argument("--fixtures-dir", required=True, help="Directory containing fixture JSON files")
    parser.add_argument("--no-cache", action="store_true", help="Disable prompt caching")
    parser.add_argument("--haiku-only", action="store_true", help="Skip Sonnet escalation")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    fixtures = load_fixtures(args.fixtures_dir)
    if not fixtures:
        print(f"ERROR: No fixture files found in {args.fixtures_dir}")
        sys.exit(1)

    print(f"Loaded {len(fixtures)} fixtures from {args.fixtures_dir}")
    print(f"Prompt caching: {'disabled' if args.no_cache else 'enabled'}")
    print(f"Escalation: {'disabled (haiku only)' if args.haiku_only else 'enabled (threshold={ESCALATION_THRESHOLD})'}")
    print("=" * 70)

    results = []
    total_cost = 0.0

    for i, fixture in enumerate(fixtures):
        filename = fixture.get("_filename", f"fixture_{i}")
        expected = fixture.get("expected", {})
        context = fixture.get("context", fixture)
        context_json = json.dumps(context, indent=2)

        print(f"\n[{i+1}/{len(fixtures)}] {filename}")
        print(f"  Expected: is_attack={expected.get('is_attack', '?')}, type={expected.get('attack_type', '?')}")

        # Step 1: Haiku screening
        try:
            haiku_result = call_claude(
                api_key, HAIKU_MODEL, context_json, use_cache=not args.no_cache
            )
        except Exception as e:
            print(f"  Haiku ERROR: {e}")
            results.append({"filename": filename, "correct": False, "error": str(e)})
            continue

        haiku_verdict = haiku_result["verdict"]
        haiku_cost = calculate_cost(haiku_result["usage"], HAIKU_MODEL)
        total_cost += haiku_cost

        if haiku_verdict is None:
            print(f"  Haiku: No verdict returned")
            results.append({"filename": filename, "correct": False, "error": "no verdict"})
            continue

        haiku_confidence = haiku_verdict.get("confidence", 0)
        haiku_is_attack = haiku_verdict.get("is_attack", False)

        print(f"  Haiku: is_attack={haiku_is_attack}, confidence={haiku_confidence:.2f}, "
              f"type={haiku_verdict.get('attack_type', 'none')}")
        print(f"  Haiku cost: ${haiku_cost:.6f} | tokens: "
              f"in={haiku_result['usage']['input_tokens']}, out={haiku_result['usage']['output_tokens']}, "
              f"cache_write={haiku_result['usage'].get('cache_creation_input_tokens', 0)}, "
              f"cache_read={haiku_result['usage'].get('cache_read_input_tokens', 0)}")
        print(f"  Haiku latency: {haiku_result['latency_ms']}ms")

        final_verdict = haiku_verdict
        final_model = HAIKU_MODEL
        escalated = False

        # Step 2: Escalate to Sonnet if confidence >= threshold and not haiku-only
        if not args.haiku_only and haiku_confidence >= ESCALATION_THRESHOLD:
            print(f"  -> Escalating to Sonnet (confidence {haiku_confidence:.2f} >= {ESCALATION_THRESHOLD})")
            try:
                sonnet_result = call_claude(
                    api_key, SONNET_MODEL, context_json, use_cache=not args.no_cache
                )
                sonnet_verdict = sonnet_result["verdict"]
                sonnet_cost = calculate_cost(sonnet_result["usage"], SONNET_MODEL)
                total_cost += sonnet_cost

                if sonnet_verdict:
                    final_verdict = sonnet_verdict
                    final_model = SONNET_MODEL
                    escalated = True

                    print(f"  Sonnet: is_attack={sonnet_verdict.get('is_attack')}, "
                          f"confidence={sonnet_verdict.get('confidence', 0):.2f}, "
                          f"type={sonnet_verdict.get('attack_type', 'none')}")
                    print(f"  Sonnet cost: ${sonnet_cost:.6f} | tokens: "
                          f"in={sonnet_result['usage']['input_tokens']}, out={sonnet_result['usage']['output_tokens']}")
                    print(f"  Sonnet latency: {sonnet_result['latency_ms']}ms")
            except Exception as e:
                print(f"  Sonnet ERROR: {e} (using Haiku verdict)")

        correct = evaluate(final_verdict, expected)
        print(f"  RESULT: {'CORRECT' if correct else 'WRONG'} (model: {final_model})")
        if not correct:
            print(f"  Reasoning: {final_verdict.get('reasoning', 'N/A')[:200]}")

        results.append({
            "filename": filename,
            "correct": correct,
            "escalated": escalated,
            "final_model": final_model,
            "haiku_verdict": haiku_verdict,
            "final_verdict": final_verdict,
            "haiku_usage": haiku_result["usage"],
            "haiku_cost": haiku_cost,
            "haiku_latency_ms": haiku_result["latency_ms"],
        })

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    correct_count = sum(1 for r in results if r.get("correct", False))
    total_count = len(results)
    accuracy = correct_count / total_count if total_count > 0 else 0

    attacks_correct = sum(1 for r, f in zip(results, fixtures)
                         if r.get("correct") and f.get("expected", {}).get("is_attack"))
    attacks_total = sum(1 for f in fixtures if f.get("expected", {}).get("is_attack"))

    normals_correct = sum(1 for r, f in zip(results, fixtures)
                          if r.get("correct") and not f.get("expected", {}).get("is_attack"))
    normals_total = sum(1 for f in fixtures if not f.get("expected", {}).get("is_attack"))

    escalated_count = sum(1 for r in results if r.get("escalated", False))

    print(f"Accuracy: {correct_count}/{total_count} = {accuracy:.1%}")
    print(f"  Attacks: {attacks_correct}/{attacks_total}")
    print(f"  Normal:  {normals_correct}/{normals_total}")
    print(f"Escalation rate: {escalated_count}/{total_count} = {escalated_count/total_count:.1%}" if total_count else "N/A")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"PoC threshold: {'PASS' if accuracy >= 0.8 else 'FAIL'} (need >= 80%)")

    # Save detailed results
    output_path = os.path.join(os.path.dirname(args.fixtures_dir.rstrip("/")), "t6_results.json")
    with open(output_path, "w") as f:
        json.dump({
            "accuracy": accuracy,
            "correct": correct_count,
            "total": total_count,
            "attacks_correct": attacks_correct,
            "attacks_total": attacks_total,
            "normals_correct": normals_correct,
            "normals_total": normals_total,
            "escalation_rate": escalated_count / total_count if total_count else 0,
            "total_cost_usd": total_cost,
            "results": results,
        }, f, indent=2, default=str)

    print(f"\nDetailed results saved to: {output_path}")

    return 0 if accuracy >= 0.8 else 1


if __name__ == "__main__":
    sys.exit(main())
