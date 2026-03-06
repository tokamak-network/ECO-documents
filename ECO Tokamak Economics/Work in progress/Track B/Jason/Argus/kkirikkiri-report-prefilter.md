# PreFilter Scoring Improvement Report

- Team: kkirikkiri-dev-prefilter
- Date: 2026-03-05
- Branch: feature/phase2-deliverables

## Goal

Reduce false positives from normal DeFi activity (Balancer arbitrage, Aave flash loan arb) that was being classified as Critical by the additive scoring system.

**Before:**
```
flash_loan(0.4) + erc20_transfers(0.4) + known_contract(0.1) + gas(0.15) = 1.05 -> Critical
```

## 3 Improvements Implemented

### 1. KnownContractInteraction -> Relevance Gate (QRadar pattern)

- `KnownContractInteraction` score: 0.1 -> 0.0 (no longer contributes additively)
- When a known contract is involved, total score is multiplied by `relevance_factor = 0.3`
- Unknown contracts: `relevance_factor = 1.0` (no change)
- Rationale: interactions with verified contracts (Uniswap, Aave, Balancer) are overwhelmingly benign

### 2. Minimum 2 Independent Signals (Forta MIN_ALERTS_COUNT pattern)

- 6 signal categories counted: Flash(H1), Revert(H2), ERC20(H3), Gas(H5), SelfDestruct(H6), Oracle+DEX(H7)
- H4 (KnownContract) excluded from count (now a modifier, not a signal)
- If fewer than `min_independent_signals` (default: 2) unique categories fire, score is clamped to 0.0
- Replaces the previous flash-loan-alone guard with a generalized version

### 3. Cash Flow Symmetry Check (H8 - new heuristic)

- Applied only when a flash loan is detected
- Analyzes ERC20 Transfer logs: compares first-half destinations with second-half destinations
- Symmetric flow (borrow -> repay to same pool): `symmetry_factor = 0.5`
- Asymmetric flow (funds drained to new addresses): adds `AsymmetricCashFlow` reason (score: 0.2), `symmetry_factor = 1.0`
- Not applicable (no flash loan): `symmetry_factor = 1.0`

## New Score Formula

```
base_score = SUM(reason.score())   // H4 = 0.0
relevance  = if known_contract { 0.3 } else { 1.0 }
symmetry   = if symmetric_flow { 0.5 } else { 1.0 }
score      = (base_score * relevance * symmetry + whitelist_modifier).clamp(0.0, 1.0)
```

## Files Changed

| File | Changes |
|------|---------|
| `src/sentinel/types.rs` | AsymmetricCashFlow variant, KnownContract score 0.0, min_independent_signals field |
| `src/sentinel/pre_filter.rs` | check_cash_flow_symmetry(), count_independent_signals(), scan_tx score formula |
| `src/sentinel/config.rs` | PrefilterConfig.min_independent_signals, to_sentinel_config() |
| `src/sentinel/service.rs` | AsymmetricCashFlow match arm |
| `src/sentinel/rpc_service.rs` | AsymmetricCashFlow match arm, test config fix |
| `src/sentinel/tests/prefilter_tests.rs` | 37 tests updated + 4 new tests |
| `src/sentinel/tests/prefilter_benchmark.rs` | 27 benchmark cases, 2 new cases, diagnostic output |
| `src/sentinel/tests/exploit_smoke_tests.rs` | Threshold adjustment for known-contract dampening |

## Test Results

### Unit Tests (prefilter_tests.rs)
- 37 tests, all passing
- New tests: relevance_gate, min_two_independent_signals, cash_flow_symmetric_discount, cash_flow_asymmetric_adds_reason

### Benchmark (prefilter_benchmark.rs)

**Default config (threshold=0.5):**

| Metric | Value |
|--------|-------|
| True Positives | 6 |
| False Positives | **0** |
| True Negatives | 14 |
| False Negatives | 7 |
| Precision | **100%** |
| Recall | 46.2% |

**Production config (threshold=0.7):**

| Metric | Value |
|--------|-------|
| True Positives | 4 |
| False Positives | **0** |
| True Negatives | 14 |
| False Negatives | 9 |
| Precision | **100%** |
| Recall | 30.8% |

### FP -> TN Conversions (primary goal)
- `normal_balancer_arbitrage`: FP -> **TN**
- `normal_aave_flash_loan_arbitrage`: FP -> **TN**
- `normal_uniswap_flash_loan_arb`: FP -> **TN**

### Full Suite
- **763 passed, 0 failed, 27 ignored**
- Clippy: 0 warnings
- Formatting: clean

## Trade-offs

- **Recall decreased** from previous levels due to stricter scoring. This is intentional: the primary goal was eliminating false positives that triggered unnecessary Alchemy deep-replay calls (cost reduction).
- The `min_independent_signals` threshold is configurable via TOML config, allowing operators to tune the precision/recall balance.
- Edge-case attacks (single-signal, low-value) now fall below threshold. These are expected to be caught by the AI agent pipeline (Phase 2) rather than the pre-filter.

## Team

| Member | Tasks | Contribution |
|--------|-------|-------------|
| core-dev | #1, #2 | types.rs + pre_filter.rs core logic |
| support-dev | #3 | config.rs + service integration |
| tester | #4, #5 | Tests, benchmarks, collateral fixes |
| team-lead | #6 | Validation, formatting, report |
