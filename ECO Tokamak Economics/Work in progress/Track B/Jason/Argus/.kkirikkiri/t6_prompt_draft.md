# T6 Prompt Design Draft

## System Prompt (cached)

```
You are an expert EVM (Ethereum Virtual Machine) security analyst. Your job is to analyze structured transaction execution traces and determine whether a transaction is an attack or benign activity.

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

1. **Reentrancy**: External call at depth N followed by state modification at depth > N. Key signals: CALL with ETH value → re-entry to same contract → SSTORE during callback (in_callback=true).

2. **Flash Loan Attack**: Token transfer from pool → callback execution at high depth → manipulation → repayment. Key signals: ERC-20 transfer pool→attacker early, attacker→pool late, >60% steps at elevated depth.

3. **Price Manipulation**: Oracle price read (STATICCALL) → swap activity → second oracle read with different price. Key signals: Two STATICCALLs to same address with transfers between them.

4. **Access Control Bypass**: DELEGATECALL to unauthorized implementation → SSTORE to critical slot (slot 0 = proxy implementation). Key signals: DELEGATECALL without CALLER check, storage mutation in delegated context.

5. **Front-Running / Sandwich**: Multiple transactions in same block targeting same pool. (Note: single-TX context only — limited detection.)

## Important Rules

- Base your judgment ONLY on the data provided in AgentContext. Do not hallucinate addresses, amounts, or events that are not in the input.
- Every piece of evidence you cite must reference actual data from the AgentContext (addresses, amounts, slots, depths).
- If unsure, lean toward conservative judgment (lower confidence, not false positive).
- A high suspicious_score alone is not proof of attack — analyze the actual trace data.
- Normal DeFi operations (swaps, liquidity adds, governance votes) can look suspicious but are benign.
```

## Tool Schema (for structured JSON output)

```json
{
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
        "description": "Attack type if is_attack=true. One of: reentrancy, flash_loan, price_manipulation, access_control, front_running, sandwich, or a custom description",
        "enum": ["reentrancy", "flash_loan", "price_manipulation", "access_control", "front_running", "sandwich", "none"]
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
```

## Test Strategy

1. Send each fixture (3 attacks + 10 normal) to Haiku with system prompt + tool_use
2. Parse tool_use response into AgentVerdict
3. For attacks: Haiku confidence >= 0.6 → escalate to Sonnet
4. Score: correct classification = 1, wrong = 0
5. Target: >= 80% accuracy (>= 11/13 correct)

## Escalation Flow Test

1. Haiku screens all 13 TXs
2. Haiku confidence >= is_suspicious_confidence_threshold (0.6) → Sonnet
3. Sonnet provides deep analysis
4. Final verdict = Sonnet verdict (if escalated) or Haiku verdict (if not)

## Cost Tracking

For each API call, record:
- Model used
- Input tokens (from usage.input_tokens)
- Output tokens (from usage.output_tokens)
- Cache creation tokens (from usage.cache_creation_input_tokens)
- Cache read tokens (from usage.cache_read_input_tokens)
- Calculate cost per request
