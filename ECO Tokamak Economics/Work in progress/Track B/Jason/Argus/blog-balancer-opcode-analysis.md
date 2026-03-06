# Replaying the $128M Balancer V2 Exploit at Opcode Level

On November 3, 2025, an attacker drained $128M from Balancer V2 in under 30 minutes. By the time the community noticed, it was already over.

I built [Argus](https://github.com/tokamak-network/Argus), an open-source Ethereum runtime security tool, and ran this attack through its detection pipeline. This article walks through what the opcodes reveal — step by step — and why static analysis tools couldn't catch it.

---

## The Attack in 60 Seconds

A rounding error in Balancer's `_upscaleArray` function. One swap loses a negligible fraction. But 65 swaps inside a single `batchSwap` transaction compound the error into millions.

```
Stage 1: Push a token's balance down to 8-9 wei (maximize rounding)
Stage 2: Execute 65 small swaps at the boundary (extract precision loss)
Stage 3: Mint BPT (Balancer Pool Token — LP shares) at suppressed price → redeem at full value
```

Total time: ~30 minutes across 6 chains. $128M gone.

## Why This Needs Runtime Analysis

Static analysis (Slither, Mythril, Echidna) and runtime monitoring (Forta, Phalcon, Argus) solve different problems. Static tools catch code-level bugs before deployment. Runtime tools catch state-dependent exploits as they happen.

This vulnerability only manifests at runtime when:
- A specific pool has a specific token balance distribution
- 65+ swaps execute in a single transaction
- Rounding compounds across each operation

No amount of source code inspection reveals this. You need to watch the opcodes as they execute against live state.

## What the Opcodes Show

I replayed the attack transaction through Argus's EVM engine ([ethrex](https://github.com/lambdaclass/ethrex) LEVM — a minimal Rust EVM implementation). Here's what the pipeline produces.

### Step 1: Pre-Filter (~10-50μs)

Before any expensive analysis, Argus's pre-filter checks receipt-level heuristics:

```
Signal: UnusualGasPattern
  Gas used: ~2,847,392 (top 0.1% of all transactions)

Signal: MultipleErc20Transfers
  65 batchSwap operations → dozens of ERC-20 Transfer events
  Threshold: > 20 (configurable)

Pre-filter verdict: Score 0.65 → Promoted to Deep Analysis
```

This costs microseconds. 99.97% of transactions are eliminated here — only 0.03% make it to the expensive opcode replay. (That's a real number from [Argus's mainnet operation](https://github.com/tokamak-network/Argus/blob/main/docs/detection-report.md): 82 flags out of ~20M transactions in 11 hours.)

### Step 2: Deep Analyzer (opcode replay)

Now Argus replays the full transaction through the EVM and traces every opcode:

```
Total opcode steps:     ~850,000
CALL opcodes:           197
STATICCALL opcodes:     312
SSTORE opcodes:         89
Unique addresses:       14
```

197 `CALL`s in a single transaction. That's not a normal swap.

The classifier identifies two patterns:

**Pattern 1: Price Manipulation (82% confidence)**
- 65 sequential swap operations detected
- Token balance driven to < 10 wei (boundary value)
- Internal price deviation: -43.7% during execution

**Pattern 2: Flash Loan (71% confidence)**
- Large value movement with same-block profit extraction
- Net profit: ~$2.1M per cycle

```
Alert Priority: CRITICAL
Score: 0.92
```

### Step 3: Autopsy Report

After detection, Argus generates a forensic report with the full attack timeline:

```
ATTACK TIMELINE
  Step      0-   200: Contract deployment + initialization
  Step    200- 2,400: Stage 1 — Large BPT→token swaps (price suppression)
  Step  2,400-45,000: Stage 2 — 65 batchSwap operations (rounding extraction)
  Step 45,000-50,000: Stage 3 — BPT mint at suppressed price + redemption

FUND FLOW
  Attacker (0x506D...) → Attack Contract (0x54B5...)
    └── Balancer Vault (0xBA12...) → Attacker
        ├── 1,847 WETH ($4.2M)
        ├── 2,100,000 USDC
        └── 890,000 DAI
```

The 42-minute gap between attack and community awareness is where the $128M was lost.

## The Detection Gap is Real

Here's what I observed in the first 11 hours of running Argus on Ethereum mainnet:

| Metric | Value |
|--------|-------|
| Alerts raised | 82 in 11 hours |
| Pre-filter flag rate | 0.030% |
| Deep replay success | 100% (82/82) |
| Avg opcode steps per alert | 69,259 |
| Infrastructure cost | $7/month (AWS Fargate) |

All 82 alerts were MEV/arbitrage — no exploits during the observation window. But the pipeline that flagged those MEV transactions is the same one that would have caught Balancer. The signatures overlap: high gas, multiple token transfers, flash loan patterns.

**Honest caveat**: This is a retroactive analysis. Argus wasn't running when the Balancer exploit happened. I can't claim "we would have stopped it." What I can show is that the detection signals fire correctly when the transaction is replayed.

## Try It Yourself

```bash
git clone https://github.com/tokamak-network/Argus.git
cd Argus
cargo run --example sentinel_realtime_demo
```

No RPC key needed — the demo runs against a local EVM. You'll see the same pipeline: pre-filter → deep analysis → alert → auto-pause.

To run against live Ethereum:

```bash
# With Docker
docker run -d \
  -e ARGUS_RPC_URL="https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY" \
  -p 9090:9090 \
  tokamak/argus-demo:latest

# Or from source
cargo run --bin argus --features cli -- sentinel \
  --rpc https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY
```

## What Argus Is (and Isn't)

**Is**: An open-source, self-hosted runtime security tool for Ethereum. Opcode-level analysis. 767 tests. MIT/Apache-2.0 licensed.

**Isn't**: A production-hardened commercial product. It's early-stage, single-developer, and Ethereum-only. The anomaly detection is rule-based + statistical (not ML). See the [honest competitive analysis](https://github.com/tokamak-network/Argus/blob/main/docs/competitive-analysis.md) for a detailed comparison with Forta, Phalcon, Tenderly, and Hexagate.

**Why open-source matters**: Every commercial security tool is a black box. You can't verify what it detects or how. Argus is fully auditable — the detection logic is in [`src/sentinel/`](https://github.com/tokamak-network/Argus/tree/main/src/sentinel), the forensics in [`src/autopsy/`](https://github.com/tokamak-network/Argus/tree/main/src/autopsy).

---

*The $128M Balancer exploit took 30 minutes. The community noticed 42 minutes later. The detection pipeline that would have flagged it costs $7/month and is [open source](https://github.com/tokamak-network/Argus). If you're a security researcher, auditor, or node operator — [feedback welcome](https://github.com/tokamak-network/Argus/discussions).*

*Built by [Jason Hwang](https://github.com/nicewook) at [Tokamak Network](https://tokamak.network/).*

**References**:
- [Check Point Research — How an Attacker Drained $128M from Balancer](https://research.checkpoint.com/2025/how-an-attacker-drained-128m-from-balancer-through-rounding-error-exploitation/)
- [BlockSec — In-Depth Analysis: The Balancer V2 Exploit](https://blocksec.com/blog/in-depth-analysis-the-balancer-v2-exploit)
- [Halborn — Explained: The Balancer Hack](https://www.halborn.com/blog/post/explained-the-balancer-hack-november-2025)
- [Argus GitHub](https://github.com/tokamak-network/Argus) | [Detection Report](https://github.com/tokamak-network/Argus/blob/main/docs/detection-report.md) | [Competitive Analysis](https://github.com/tokamak-network/Argus/blob/main/docs/competitive-analysis.md)
