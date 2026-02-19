**Author:** Bernard Lee, Suhyeon Lee

**Date:** January 28, 2026

**Environment:** Local Devnet (op-succinct) + Succinct Prover Network

**Mode:** Real ZK Mode (1000-block batch proving)

---

## 1. Test Objective

To evaluate the **scaling characteristics** of ZK validity proofs when proving larger block ranges:

1. How does proof generation cost scale with block count?
1. How does proof generation time scale with block count?
1. What configuration changes are required for larger batches?
1. Is batch proving more cost-efficient than single-block proving?

---

## 2. Test Environment

### 2.1 Network Configuration

| Component | Endpoint |
| --- | --- |
| L1 RPC | [http://127.0.0.1:50643](http://127.0.0.1:50643/) |
| L2 RPC | [http://127.0.0.1:50696](http://127.0.0.1:50696/) |
| L2 Node RPC | [http://127.0.0.1:50701](http://127.0.0.1:50701/) |
| L1 Beacon RPC | [http://127.0.0.1:50647](http://127.0.0.1:50647/) |
| L1 Chain ID | 3151908 |
| L2 Chain ID | 901 |

### 2.2 Deployed Contracts

| Contract | Address | Role |
| --- | --- | --- |
| DisputeGameFactory | `0x37d08c124B91e1663d83fb1b742677115959b726` | Game creation management |
| SP1 Verifier Gateway | `0x48266A1953D7e3a02603868528Fd51DCa1866614` | Routes proofs to correct verifier |
| SP1 Verifier (v5.0.0 Plonk) | `0x835089111509d7102bF2935f50905a89d5840AAD` | On-chain proof verification |
| Anchor State Registry | `0xfbECDA1A5CAf07b2a9E6042e6A41A85935a557cD` | L2 state anchoring |

### 2.3 Accounts

| Role | Address | Purpose |
| --- | --- | --- |
| Proposer/Owner | `0x589A698b7b7dA0Bec545177D3963A2741105C7C9` | Game creation, proof submission |
| Challenger | `0x90F79bf6EB2c4f870365E785982E1f101E93b906` | Challenge submission |
| Succinct Requester | `0x6d14e0f28cc49f11613e0092773101cce2cfb0ab` | Proof requests to Succinct Network |

### 2.4 Proposer Configuration

`MOCK_MODE=false
SP1_PROVER=network
PROPOSAL_INTERVAL_IN_BLOCKS=1000

# Proof Strategy
RANGE_PROOF_STRATEGY=auction
AGG_PROOF_STRATEGY=auction
AUCTION_TIMEOUT=600
MIN_AUCTION_PERIOD=300

# Resource Limits (Increased for batch proving)
RANGE_CYCLE_LIMIT=100000000000    # 100B cycles
RANGE_GAS_LIMIT=100000000000      # 100B PGUs
AGG_CYCLE_LIMIT=100000000000      # 100B cycles
AGG_GAS_LIMIT=30000000000         # 30B PGUs

# Pricing
MAX_PRICE_PER_PGU=450000000       # 0.45 PROVE per bPGU`

**Key Changes from 1-Block Test:**

- `PROPOSAL_INTERVAL_IN_BLOCKS`: 1 → 1000
- `RANGE_GAS_LIMIT`: 10B → 100B (10x increase required)
- `AGG_GAS_LIMIT`: 10B → 30B
- `MAX_PRICE_PER_PGU`: 150M → 450M (0.15 → 0.45 PROVE)

---

## 3. Two-Stage Proof Architecture

### Why Two Proofs?

OP Succinct uses a two-stage proof system for cost efficiency:

`┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Range Proof (Compressed)                          │
│  - Proves L2 state transition correctness                   │
│  - Large proof size (several MB)                            │
│  - Cannot be verified on-chain directly (too expensive)     │
│  - Fast to generate relative to complexity                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Aggregation Proof (Plonk)                         │
│  - Proves "the Compressed proof is valid"                   │
│  - Small proof size (hundreds of bytes)                     │
│  - Can be verified on-chain efficiently                     │
│  - SNARK-based, constant verification cost                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  On-chain Verification                                      │
│  - SP1VerifierGateway routes to correct verifier            │
│  - SP1Verifier (Plonk) verifies the proof                   │
│  - Game status updated to "Proven"                          │
└─────────────────────────────────────────────────────────────┘`

---

## 4. Test Procedure and Results

### 4.1 Game Creation

The proposer created a dispute game covering blocks 90650 to 91650 (1000 blocks):

`2026-01-22T20:12:48.489474Z  INFO [[Proving]]: Attempting to prove game 0x151f6aaf18bb88d011272edfb2f77736d15d26e2
2026-01-22T20:12:48.490142Z  INFO [[Proving]]: Proving over 1 ranges
2026-01-22T20:12:48.490334Z  INFO [[Proving]]: Generating Range Proof for blocks 90650 to 91650`

### 4.2 Challenge Execution

bash

`cast send 0x151f6aaf18bb88d011272edfb2f77736d15d26e2 "challenge()" \
  --value 0.001ether \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6`

### 4.3 Range Proof Request Log

`2026-01-22T20:14:39.925210Z  INFO [[Proving]]: Requesting proof:
2026-01-22T20:14:39.925250Z  INFO [[Proving]]: ├─ Strategy: Auction
2026-01-22T20:14:39.926686Z  INFO [[Proving]]: ├─ Proof mode: Compressed
2026-01-22T20:14:39.926716Z  INFO [[Proving]]: ├─ Circuit version: v5.0.0
2026-01-22T20:14:39.926723Z  INFO [[Proving]]: ├─ Timeout: 14400 seconds
2026-01-22T20:14:39.926732Z  INFO [[Proving]]: ├─ Base fee: 0.2000 $PROVE
2026-01-22T20:14:39.927940Z  INFO [[Proving]]: ├─ Max price per bPGU: 0.4500 $PROVE
2026-01-22T20:14:39.927989Z  INFO [[Proving]]: ├─ Cycle limit: 100000000000 cycles
2026-01-22T20:14:39.928998Z  INFO [[Proving]]: └─ Gas limit: 100000000000 PGUs`

### 4.4 Aggregation Proof Request Log

`2026-01-22T20:25:42.283638Z  INFO [[Proving]]: Requesting proof:
2026-01-22T20:25:42.283947Z  INFO [[Proving]]: ├─ Strategy: Auction
2026-01-22T20:25:42.283976Z  INFO [[Proving]]: ├─ Proof mode: Plonk
2026-01-22T20:25:42.283983Z  INFO [[Proving]]: ├─ Circuit version: v5.0.0
2026-01-22T20:25:42.283988Z  INFO [[Proving]]: ├─ Timeout: 14400 seconds
2026-01-22T20:25:42.283995Z  INFO [[Proving]]: ├─ Base fee: 0.3000 $PROVE
2026-01-22T20:25:42.284001Z  INFO [[Proving]]: ├─ Max price per bPGU: 0.4500 $PROVE
2026-01-22T20:25:42.284018Z  INFO [[Proving]]: ├─ Cycle limit: 100000000000 cycles
2026-01-22T20:25:42.284024Z  INFO [[Proving]]: └─ Gas limit: 30000000000 PGUs`

### 4.5 On-chain Submission Log

`2026-01-22T20:32:21.469833Z  INFO Game proven successfully 
  game_address=0x151f6aaf18bb88d011272edfb2f77736d15d26e2 
  l2_block_start=90650 
  l2_block_end=91650
  tx_hash=0xe10930e70839bec4582177795aa31dedcfc35589039ed08f6d7146d991bb1fbf
  duration_s=1172.927940209`

---

## 5. Proof Details from Succinct Explorer

### 5.1 Range Proof (Compressed)

| Item | Value |
| --- | --- |
| Request ID | `0x52ea844a6033c72447e6b50086ca243b6a8ae023d1d97597a9265f0226026fd3` |
| Explorer Link | [https://explorer.succinct.xyz/request/0x52ea844a6033c72447e6b50086ca243b6a8ae023d1d97597a9265f0226026fd3](https://explorer.succinct.xyz/request/0x52ea844a6033c72447e6b50086ca243b6a8ae023d1d97597a9265f0226026fd3) |
| Status | Fulfilled |
| Mode | Compressed |
| SP1 Version | v5.0.0 |
| Time Taken | **10m 40s** |
| Gas Limit | 100,000,000,000 PGUs |
| Gas Used | **11,852,253,092 PGUs** (~11.85B) |
| Base Fee | 0.2 PROVE |
| Price Per bPGU | 0.45 PROVE |
| **Total Fee** | **5.5335 PROVE** |
| Prover | `0x3d008bdb990e69c40afb6aa7161c91e82f0fa125` |

### 5.2 Aggregation Proof (Plonk)

| Item | Value |
| --- | --- |
| Request ID | `0xd84b56816780061ba17a03fb936bf54c4796f32b773fac4ba5779265e8f53f0f` |
| Explorer Link | [https://explorer.succinct.xyz/request/0xd84b56816780061ba17a03fb936bf54c4796f32b773fac4ba5779265e8f53f0f](https://explorer.succinct.xyz/request/0xd84b56816780061ba17a03fb936bf54c4796f32b773fac4ba5779265e8f53f0f) |
| Status | Fulfilled |
| Mode | Plonk |
| SP1 Version | v5.0.0 |
| Time Taken | **6m 7s** |
| Gas Limit | 30,000,000,000 PGUs |
| Gas Used | **1,529,006 PGUs** (~1.5M) |
| Base Fee | 0.3 PROVE |
| Price Per bPGU | 0.45 PROVE |
| **Total Fee** | **0.3007 PROVE** |
| Prover | `0x22f87c35b900b117c19cc4c9ca6a9f59fb38fa4d` |

---

## 6. Cost and Time Summary

### 6.1 Proof Generation Costs

| Stage | Time | Gas Used | Cost |
| --- | --- | --- | --- |
| Range Proof (Compressed) | 10m 40s | 11.85B PGUs | 5.5335 PROVE |
| Aggregation Proof (Plonk) | 6m 7s | 1.5M PGUs | 0.3007 PROVE |
| On-chain Submission | ~20s | - | Gas fees |
| **Total** | **~19m 33s** | - | **~5.83 PROVE** |

### 6.2 Comparison: 1-Block vs 1000-Block

| Metric | 1 Block | 1000 Blocks | Ratio |
| --- | --- | --- | --- |
| Block Count | 1 | 1000 | 1000x |
| **Range Proof** |  |  |  |
| └─ Gas Used | 1.68B PGUs | 11.85B PGUs | **~7x** |
| └─ Time | 6m 22s | 10m 40s | ~1.7x |
| └─ Cost | ~0.2 PROVE | 5.53 PROVE | ~27x |
| **Aggregation Proof** |  |  |  |
| └─ Gas Used | 1.5M PGUs | 1.5M PGUs | **~1x** |
| └─ Time | 6m 21s | 6m 7s | ~1x |
| └─ Cost | ~0.3 PROVE | ~0.3 PROVE | ~1x |
| **Total** |  |  |  |
| └─ Time | ~13 min | ~20 min | ~1.5x |
| └─ Cost | ~0.5 PROVE | ~5.83 PROVE | ~12x |
| **Cost per Block** | **0.5 PROVE** | **0.00583 PROVE** | **~86x cheaper** |

### 6.3 Comparison: Mock Mode vs Real ZK Mode

| Metric | Mock Mode | Real ZK Mode (1000 blocks) |
| --- | --- | --- |
| Total Duration | ~66 seconds | ~20 minutes |
| PROVE Cost | 0 | ~5.83 PROVE |
| On-chain Verification | Skipped | Actual verification |
| Proof Generation | Simulated | Succinct Network |

---

## 7. Troubleshooting Journey

### 7.1 Issue: Gas Limit Exceeded (First Attempt)

**Symptom:**

`Error: Program execution failed
Execution Failure Reason: The request's prover gas limit was exceeded
Request ID: 0x7c21552430f9f58d880a5042e135e6e2f2d0be341e040b1e824c8f78deffb454`

**Root Cause:** Initial `RANGE_GAS_LIMIT=10000000000` (10B) was insufficient for 1000 blocks.

**Solution:** Increased to `RANGE_GAS_LIMIT=100000000000` (100B PGUs).

### 7.2 Issue: Auction Not Filled

**Symptom:** Proof requests timing out without prover bids.

**Root Cause:** `MAX_PRICE_PER_PGU=150000000` (0.15 PROVE) was too low for larger workloads.

**Solution:** Increased to `MAX_PRICE_PER_PGU=450000000` (0.45 PROVE per bPGU).

---

## 8. Key Findings

### 8.1 Scaling Characteristics

The test demonstrates that OP Succinct's ZK validity proof system exhibits **favorable scaling properties**:

| Component | Scaling Behavior |
| --- | --- |
| Range Proof | Sublinear (~7x gas for 1000x blocks) |
| Aggregation Proof | Constant cost regardless of block count |
| Overall | Batch proving dramatically reduces per-block costs |

### 8.2 Cost Analysis

| Metric | Value | Notes |
| --- | --- | --- |
| Per-block proof cost (1 block) | 0.5 PROVE | High fixed cost overhead |
| Per-block proof cost (1000 blocks) | 0.00583 PROVE | 86x more efficient |
| Gas used (Range, 1000 blocks) | 11.85B PGUs | 11.85% of 100B limit |
| Gas used (Plonk) | 1.5M PGUs | Constant regardless of batch size |

### 8.3 Cost Model

Based on the test results, the approximate cost model is:

`Total Cost ≈ Fixed Cost + Variable Cost
           ≈ 0.3 PROVE (Plonk) + f(blocks) PROVE (Range)

Where f(blocks) scales sublinearly:
- f(1) ≈ 0.2 PROVE
- f(1000) ≈ 5.5 PROVE
- Ratio: 1000x blocks → ~27x cost`

### 8.4 Operational Considerations

1. **Auction Strategy**: More flexible than Reserved, works without pre-registration
1. **Timeout Settings**: 10-minute auction timeout provides sufficient time for prover bids
1. **Minimum Auction Period**: 5 minutes ensures competitive bidding
1. **Price Per bPGU**: Set to at least 0.45 PROVE for reliable prover participation on larger workloads

---

## 9. Conclusion

Successfully completed the **1000-block batch ZK validity proof** with real proof generation:

### Verified Items

- Dispute Game creation for large block ranges
- Range Proof (Compressed) generation for 1000 blocks via Succinct Network
- Aggregation Proof (Plonk) generation via Succinct Network
- On-chain proof verification with SP1Verifier
- Game state transition to "Proven"

### Key Metrics

| Metric | Value |
| --- | --- |
| Total Time | ~20 minutes |
| Total Cost | ~5.83 PROVE tokens |
| Blocks Proven | 1000 (L2 blocks 90650 → 91650) |
| Cost per Block | 0.00583 PROVE |
| Efficiency vs 1-Block | 86x cheaper per block |

### Configuration Recommendations for Batch Proving

| Parameter | 1 Block | 1000 Blocks | Recommendation |
| --- | --- | --- | --- |
| RANGE_GAS_LIMIT | 10B | 100B | Scale with block count |
| AGG_GAS_LIMIT | 10B | 30B | 30B is sufficient |
| MAX_PRICE_PER_PGU | 0.15 | 0.45 | Higher for larger batches |

### Production Implications

1. **Batch Size Optimization**: Larger batches are significantly more cost-efficient. Production deployments should maximize batch size within latency constraints.
1. **Resource Planning**: For 1000-block batches, allocate:
  - ~6 PROVE tokens per proof cycle
  - ~20 minutes proving time
  - 100B PGU gas limit for Range proofs
1. **Auction Pricing**: Set `MAX_PRICE_PER_PGU` to at least 0.45 PROVE for reliable prover participation on larger workloads.

---

## Appendix: Key Commands Reference

bash

`# Check game status
cast call <game_address> "status()(uint8)" --rpc-url <l1_rpc>
cast call <game_address> "gameOver()(bool)" --rpc-url <l1_rpc>

# Execute challenge
cast send <game_address> "challenge()" --value 0.001ether --rpc-url <l1_rpc> --private-key <pk>

# Check proof request status on Succinct Explorer
# https://explorer.succinct.xyz/request/<request_id>

# Monitor proposer logs
RUST_LOG=info ./target/release/proposer

# Verify on-chain transaction
cast tx <tx_hash> --rpc-url <l1_rpc>`