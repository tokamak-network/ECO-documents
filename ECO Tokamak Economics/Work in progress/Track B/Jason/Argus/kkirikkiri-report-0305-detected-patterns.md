# detected_patterns Bug Fix Report

## Summary

**Problem**: All 82 mainnet alerts had empty `detected_patterns: []`. The AttackClassifier failed to match any flash loan patterns despite successful deep RPC replay.

**Root Cause**: Classifier strategy logic issues (not data capture). Three independent problems in `src/autopsy/classifier.rs`.

**Result**: 752 tests passed, 0 failed, clippy clean, fmt clean.

## Root Cause Analysis

### Phase 0 Diagnosis (diagnostician)

**Data capture (recorder.rs) is correct.** All 6 fields (call_value, log_topics, log_data, stack_top, storage_writes, call_input_selector) are properly captured. The problem was purely in classifier matching conditions.

| Strategy | Failure Reason | Severity |
|----------|---------------|----------|
| Strategy 1 (ETH value) | Balancer uses ERC-20 tokens, not ETH. `call_value = None` always. | Structural (by design) |
| Strategy 2 (ERC-20 LOG3) | `borrow_amount` hardcoded to `U256::zero()`, weakening confidence scoring | High |
| Strategy 3 (Callback depth) | 60% threshold too strict. Balancer vault setup/teardown at depth 1 dilutes ratio to ~50% | High |

## Changes Made

### File: `src/autopsy/classifier.rs` (classifier-dev)

**1. Strategy 2 -- borrow_amount extraction from log_data**
- Previously: `borrow_amount: U256::zero()` and `repay_amount: U256::zero()`
- Now: Extracts uint256 from `log_data` (first 32 bytes, big-endian)
- Pattern: `s.log_data.as_ref().filter(|d| d.len() >= 32).map(|d| U256::from_big_endian(&d[..32]))`
- Added `amount` field to `Erc20Transfer` struct

**2. Strategy 3 -- callback depth threshold relaxed**
- Changed: `deep_ratio < 0.6` to `deep_ratio < 0.4`
- Rationale: Real Balancer TXs have ~50% deep steps due to vault setup/teardown at depth 1

**3. Confidence scoring -- ERC-20 token + provider bonus**
- Added new tier: `has_token && has_provider && inner_sstores > 0` -> confidence 0.85
- Fills gap between 0.9 (has_amount) and 0.8 (has_provider only)

### File: `src/tests/classifier_diagnostic.rs` (diagnostician, new)
- 7 diagnostic tests validating Strategy 2 and Strategy 3 behavior

### File: `src/tests/classifier_validation_tests.rs` (tester, new)
- 10 validation tests: 4 positive detection + 3 false-positive rejection + 3 edge cases

### File: `src/tests/mod.rs`
- Registered both new test modules with `#[cfg(feature = "autopsy")]`

## Verification

```
cargo test --all-features     -> 752 passed, 0 failed, 25 ignored
cargo clippy --all-features   -> 0 warnings
cargo fmt --check             -> clean
```

## Unchanged Files (Confirmed Not Needed)

- `src/recorder.rs` -- Data capture logic is correct (6/6 fields verified)
- `src/sentinel/rpc_replay.rs` -- RPC replay works correctly
- `src/sentinel/rpc_service.rs` -- build_deep_alert pipeline is correct

## Team

| Member | Role | Deliverable |
|--------|------|------------|
| diagnostician | Phase 0 diagnosis + Phase 1 verification | Root cause analysis, 7 diagnostic tests |
| classifier-dev | Phase 2 classifier fix | 3 code changes in classifier.rs |
| tester | Phase 3 validation | 10 validation tests |
| lead | Coordination + integration | This report, final verification |
