# Sentinel Architecture — Design Decisions

**Date**: 2026-03-01
**Branch**: `feat/tokamak-autopsy`
**Scope**: H-1 (Pre-Filter), H-2 (Deep Analysis), H-3 (Block Processing Integration), H-4 (Alert System), H-5 (Dashboard), H-6 (CLI, Mempool, Pipeline, Auto-Pause)

---

## Core Constraint

ethrex is a full node. Any analysis added to the block processing hot path must not degrade synchronization performance or risk consensus divergence. This constraint drives every design decision below.

---

## 1. Two-Stage Pipeline (PreFilter → DeepAnalyzer)

**Analogy**: Airport security screening. Everyone passes through the metal detector (PreFilter); only those who trigger an alarm get a full pat-down (DeepAnalyzer).

```
Block (200 TXs)
  │
  ├─ PreFilter: receipt-based, ~10-50μs/TX  ← scans ALL TXs
  │   └─ 197 benign → discard
  │   └─ 3 suspicious → forward to DeepAnalyzer
  │
  └─ DeepAnalyzer: opcode replay, ~10-100ms/TX  ← suspicious only
      └─ AttackClassifier + FundFlowTracer
      └─ SentinelAlert generation
```

### Why not a single stage?

Opcode replay re-executes the transaction from scratch. Replaying all 200 TXs in a block would double block processing time. Receipts already exist as execution output — scanning them costs nearly zero.

### Why receipts for the pre-filter?

Receipts contain logs (events), `gas_used`, and `succeeded` status. Flash loan event signatures, ERC-20 Transfer counts, and gas patterns can be extracted without opcode-level tracing. False positives are filtered by the DeepAnalyzer.

---

## 2. BlockObserver Trait Placement

### Dependency graph

```
ethrex-blockchain  ──depends──>  ethrex-vm, ethrex-storage
tokamak-debugger   ──depends──>  ethrex-blockchain, ethrex-vm, ethrex-storage
```

tokamak-debugger depends on ethrex-blockchain, not the reverse. If blockchain directly referenced `SentinelService`, it would create a **circular dependency**.

### Solution: Dependency Inversion Principle (DIP)

Define the `BlockObserver` trait in ethrex-blockchain (the interface). Implement it (`SentinelService`) in tokamak-debugger (the concrete). blockchain only knows `dyn BlockObserver`.

```rust
// ethrex-blockchain — interface only
pub trait BlockObserver: Send + Sync {
    fn on_block_committed(&self, block: Block, receipts: Vec<Receipt>);
}

// tokamak-debugger — implementation
impl BlockObserver for SentinelService { ... }
```

No feature gates needed in blockchain. The `block_observer` field defaults to `None` — zero overhead when sentinel is not configured.

---

## 3. Background Worker Thread + mpsc Channel

**Analogy**: Restaurant kitchen. The waiter (block processing thread) hangs the order ticket (`send`) and immediately serves the next customer. The cook (worker thread) processes orders at their own pace.

```rust
// Block processing hot path — non-blocking
fn on_block_committed(&self, block: Block, receipts: Vec<Receipt>) {
    let _ = sender.send(SentinelMessage::BlockCommitted { ... });
    // Returns immediately — analysis happens on the worker
}
```

### Why std::sync::mpsc instead of async?

LEVM's `Database` trait is synchronous. `replay_tx_from_store` calls LEVM directly. Using `block_on()` inside a tokio async context panics (learned from the autopsy `reqwest::blocking` experience). A dedicated OS thread is the safest choice.

### Why `Mutex<mpsc::Sender>`?

`mpsc::Sender` is `Send` but NOT `Sync`. The `BlockObserver: Send + Sync` bound requires wrapping with `Mutex`. Lock contention is effectively zero — `send()` takes microseconds.

---

## 4. Autopsy Infrastructure Reuse

E-4's `AttackClassifier`, `FundFlowTracer`, and `DetectedPattern` are reused directly.

```
E-4 (Autopsy Lab)          H-2 (Sentinel Deep Analysis)
─────────────────          ──────────────────────────────
RemoteVmDatabase           StoreVmDatabase (local Store)
    ↓                          ↓
OpcodeRecorder             OpcodeRecorder (identical)
    ↓                          ↓
AttackClassifier           AttackClassifier (identical)
FundFlowTracer             FundFlowTracer (identical)
    ↓                          ↓
AutopsyReport              SentinelAlert (different output format)
```

### The only difference is the data source

Autopsy fetches state from an external archive RPC. Sentinel reads from the node's own Store. The analysis logic is 100% identical.

### `#[cfg(feature = "autopsy")]` gating

Sentinel can run with only the `sentinel` feature (without `autopsy`). In this mode, only the PreFilter operates and deep analysis is skipped. This excludes heavy dependencies like `reqwest` (HTTP client) from sentinel-only builds.

---

## 5. Store-Based Replay vs Remote RPC

```rust
// Autopsy (E-4) — depends on external archive node
let db = RemoteVmDatabase::new(rpc_url, block_number);

// Sentinel (H-2) — reads directly from local Store
let db = StoreVmDatabase::new(store.clone(), parent_header);
```

Why Sentinel uses the local Store:

| Factor | Remote RPC | Local Store |
|--------|-----------|-------------|
| Latency | ~ms per call | ~μs per read |
| Availability | External node may fail | Always available (just stored) |
| Consistency | May lag or differ | Block was just committed |
| Dependencies | reqwest, network | None |

---

## 6. Block Clone Timing

```rust
// Clone BEFORE store_block — block is consumed by store_block()
let observer_data = self.block_observer.as_ref()
    .map(|_| (block.clone(), res.receipts.clone()));

let result = self.store_block(block, ...);  // block consumed here

// Notify observer ONLY after successful store
if result.is_ok() {
    if let Some((block_clone, receipts)) = observer_data {
        observer.on_block_committed(block_clone, receipts);
    }
}
```

### Why clone before store?

`store_block()` consumes `Block` by value (`fn store_block(self, block: Block, ...)`). The clone cannot be deferred to after the store call.

### Why skip clone when no observer?

The `.map(|_| ...)` pattern skips cloning entirely when `block_observer` is `None`. Zero overhead when sentinel is not configured.

---

## 7. Graceful Shutdown via Drop

```rust
impl Drop for SentinelService {
    fn drop(&mut self) {
        self.shutdown();              // Send Shutdown message
        if let Some(h) = handle.take() {
            let _ = h.join();         // Wait for worker to finish
        }
    }
}
```

The worker thread holds a `Store` reference. If the process exits while the worker is mid-analysis, in-flight data is lost. Graceful shutdown ensures the worker finishes its current block before terminating.

---

## 8. E2E Validation

The live reentrancy E2E test (`examples/reentrancy_demo.rs`) validates the full 6-phase pipeline with real bytecode execution:

```
Phase 1: Deploy & Execute  → LEVM executes attacker/victim contracts
Phase 2: Verify Attack      → call depth >= 3, SSTORE count >= 2
Phase 3: Classify            → AttackClassifier detects Reentrancy (conf >= 0.7)
Phase 4: Fund Flow           → FundFlowTracer traces ETH transfers
Phase 5: Sentinel Pipeline   → real receipt → PreFilter → SentinelService → alert
Phase 6: Alert Validation    → alert content + metrics verification
```

Key insight: stealthy attacks bypass PreFilter entirely. The `prefilter_alert_mode` flag ensures alerts are still emitted when deep analysis is unavailable (no Store for replay).

---

## 9. MempoolObserver Trait (H-6b)

**Analogy**: Customs inspection at the port. Instead of only checking cargo after it's been unloaded (block committed), officers also inspect shipping manifests at arrival (mempool insertion) — before the goods touch the warehouse.

### Why pre-execution monitoring?

Block-level detection (H-1~H-3) only fires after a transaction is executed and committed. By then, the attack has already succeeded. Mempool monitoring catches suspicious transactions before execution, enabling:

1. Earlier alerting (seconds before block inclusion)
2. Potential front-running defense (future: drop or deprioritize flagged TXs)
3. Detection of transactions that never get mined (reverted in mempool)

### Trait placement: same DIP pattern

```
ethrex-blockchain        ──defines──>  MempoolObserver trait
tokamak-debugger         ──implements──> MempoolPreFilter: MempoolObserver
```

```rust
// ethrex-blockchain — interface only (same pattern as BlockObserver)
pub trait MempoolObserver: Send + Sync {
    fn on_transaction_added(&self, tx: &Transaction, sender: Address, tx_hash: H256);
}
```

Hooks in `add_transaction_to_pool()` and `add_blob_transaction_to_pool()` call the observer after successful pool insertion.

### Calldata-only heuristics

No receipts, logs, or state are available — only TX-level data (calldata, value, gas limit, target address). Five heuristics extract signal:

| Heuristic | Signal | Score |
|-----------|--------|-------|
| Flash loan selector | Known 4-byte selectors (Aave, Balancer, Compound) | 0.4 |
| High-value DeFi | ETH value > threshold to known DeFi contract | 0.3 |
| High-gas known contract | Gas limit > threshold targeting known contract | 0.2 |
| Suspicious creation | Contract creation with init code > 10 KB | 0.25 |
| Multicall pattern | `multicall(bytes[])` selector to known router | 0.3 |

### Limitations

Signature-based detection is inherently bypassable. A custom contract with non-standard selectors will evade all 5 heuristics. MempoolPreFilter is a **fast early warning**, not a security guarantee. The adaptive pipeline (H-6c) provides the real defense after execution.

---

## 10. Adaptive Analysis Pipeline (H-6c)

**Analogy**: Medical triage. Instead of running the same battery of tests on every patient (fixed DeepAnalyzer), triage nurses evaluate each patient and order specific follow-up tests based on initial symptoms. Some patients are discharged early (Dismiss); others get additional specialist consults (AddSteps).

### Why replace the fixed DeepAnalyzer?

The H-2 `DeepAnalyzer` runs all classifiers unconditionally: replay → classify → trace funds. This wastes work on benign-looking TXs that pass the pre-filter threshold but aren't actually malicious. The adaptive pipeline:

1. Can early-exit (Dismiss) at any step — e.g., a TX with zero CALL opcodes skips reentrancy analysis
2. Can inject follow-up steps dynamically — e.g., detecting delegation chains triggers a deeper access control check
3. Produces a numerical `FeatureVector` for statistical anomaly scoring alongside pattern matching

### AnalysisStep trait

```rust
pub trait AnalysisStep: Send {
    fn name(&self) -> &'static str;
    fn execute(
        &self,
        ctx: &mut AnalysisContext,
        store: &Store,
        block: &Block,
        suspicion: &SuspiciousTx,
        config: &AnalysisConfig,
    ) -> Result<StepResult, SentinelError>;
}

pub enum StepResult {
    Continue,                          // proceed to next step
    Dismiss,                           // TX is benign, stop
    AddSteps(Vec<Box<dyn AnalysisStep>>), // inject follow-up steps
}
```

### Six pipeline steps

| Step | Purpose | Can Dismiss? | Can AddSteps? |
|------|---------|:------------:|:-------------:|
| 1. TraceAnalyzer | Replay TX, populate `replay_result` | No | No |
| 2. FeatureExtractor | Extract 16-field FeatureVector from trace | No | No |
| 3. FlashLoanDetector | Check flash loan indicators | Yes (if none) | No |
| 4. ReentrancyDetector | Check recursive CALL depth patterns | Yes (if none) | Yes (deeper analysis) |
| 5. PatternMatcher† | Run AttackClassifier + FundFlowTracer | No | No |
| 6. AnomalyScorer | z-score anomaly detection + confidence scoring | No | No |

†Steps 5 (PatternMatcher) and an additional FundFlowAnalyzer are only present with the `autopsy` feature.

### Bounded dynamic step queue

`StepResult::AddSteps` allows steps to inject follow-up analysis. To prevent unbounded queue growth (DoS vector), the queue is capped:

```rust
const MAX_DYNAMIC_STEPS: usize = 64;

// Queue extension bounded:
StepResult::AddSteps(new_steps) => {
    let remaining = MAX_DYNAMIC_STEPS.saturating_sub(dynamic_queue.len());
    dynamic_queue.extend(new_steps.into_iter().take(remaining));
}
```

Both the queue size and execution count are bounded to `MAX_DYNAMIC_STEPS`.

### FeatureVector design

All 16 fields use `f64` (not `u32`/`u64`) for direct compatibility with the anomaly model's z-score math (subtraction, division). Avoids repeated `as f64` casts in the scoring loop.

```rust
pub struct FeatureVector {
    pub total_steps: f64,      pub unique_addresses: f64,
    pub max_call_depth: f64,   pub sstore_count: f64,
    pub sload_count: f64,      pub call_count: f64,
    pub delegatecall_count: f64, pub staticcall_count: f64,
    pub create_count: f64,     pub selfdestruct_count: f64,
    pub log_event_count: f64,  pub revert_count: f64,
    pub gas_ratio: f64,        pub value_transferred: f64,
    pub reentrancy_depth: f64, pub storage_write_ratio: f64,
}
```

### Confidence scoring

Combined confidence from multiple signal sources:

| Mode | Weights |
|------|---------|
| With autopsy | pattern × 0.4 + anomaly × 0.3 + prefilter × 0.2 + fund_flow × 0.1 = 1.0 |
| Without autopsy | anomaly × 0.6 + prefilter × 0.4 = 1.0 |

The final `suspicion_score` stored in `SentinelAlert` is `max(prefilter_heuristic, pipeline_confidence)` — ensuring downstream handlers (AutoPauseHandler) use the best available signal.

---

## 11. PauseController Concurrency Model (H-6d)

**Analogy**: Emergency stop button on a factory conveyor belt. A single red button (AtomicBool) halts the belt instantly. Workers see it from afar (fast path: one glance). The timer relay auto-restarts after 5 minutes unless manually overridden.

### Why auto-pause?

Sentinel detects attacks, but without `PauseController`, it can only log alerts. Auto-pause enables the node to halt block ingestion when a Critical alert is confirmed, preventing further damage until an operator investigates. This is the "circuit breaker" pattern for blockchain nodes.

### Threading model

```
Block processing hot path:
  add_block() → check_pause() → wait_if_paused()
                                     │
                                ┌────┴────┐
                                │ paused?  │ ← AtomicBool::load(Acquire)  ~1ns
                                └────┬────┘
                                  false → return immediately (fast path)
                                  true  → Mutex::lock → Condvar::wait_timeout
                                                         ↓
                                          resume() or timeout → continue
```

### Fast path: zero overhead when not paused

```rust
pub fn wait_if_paused(&self) {
    if !self.paused.load(Ordering::Acquire) {
        return;  // Single atomic load — <1ns on x86_64
    }
    // Slow path: block on Condvar until resume() or timeout
    let mut guard = match self.lock.lock() { ... };
    while self.paused.load(Ordering::Acquire) {
        guard = match self.condvar.wait_timeout(guard, timeout) { ... };
    }
}
```

### Fail-open on lock poisoning

If any thread panics while holding the Mutex, the lock becomes "poisoned". A naive `.expect()` would crash ALL block processing threads permanently. Instead, PauseController **fails open**:

```rust
let mut guard = match self.lock.lock() {
    Ok(g) => g,
    Err(_poisoned) => {
        eprintln!("[SENTINEL] PauseController lock poisoned — treating as unpaused");
        self.paused.store(false, Ordering::Release);
        return;  // Continue processing blocks
    }
};
```

**Rationale**: For a blockchain node, availability (continuing to process blocks) is more important than pause enforcement. A poisoned lock means something already went wrong — halting the entire chain would make it worse.

### Auto-resume via Condvar::wait_timeout

```rust
// No background timer thread needed — Condvar::wait_timeout is the timer
Condvar::wait_timeout(guard, Duration::from_secs(auto_resume_secs))
```

If the timeout expires without `resume()` being called, the controller auto-unpauses. Default: 300 seconds (5 minutes). Configurable via TOML.

### RPC authentication boundary

```
Public HTTP RPC          → sentinel_status (read-only: is paused? stats?)
Authenticated authrpc    → sentinel_resume (mutating: unpause the chain)
```

`sentinel_resume` is authrpc-only because it controls block processing — exposing it on public HTTP would allow anyone to unpause a legitimately paused chain.

---

## 12. AutoPauseHandler Circuit Breaker (H-6d)

`AutoPauseHandler` implements the `AlertHandler` trait, connecting the alert pipeline to the `PauseController`.

```rust
impl AlertHandler for AutoPauseHandler {
    fn on_alert(&self, alert: SentinelAlert) {
        if alert.alert_priority >= self.priority_threshold
            && alert.suspicion_score >= self.confidence_threshold
        {
            self.controller.pause();
        }
    }
}
```

### Dual-threshold gate

Both conditions must be met:

1. `alert_priority >= threshold` — e.g., only Critical alerts
2. `suspicion_score >= confidence` — e.g., score >= 0.8

This prevents false-positive pauses from high-priority but low-confidence alerts (e.g., a flash loan that looks suspicious but has low anomaly score).

---

## 13. TOML Configuration (H-6a)

### Why TOML?

The sentinel has 30+ tunable parameters across 6 sub-systems. CLI flags alone become unwieldy. TOML provides hierarchical configuration with defaults:

```toml
[sentinel]
suspicion_threshold = 0.5
min_gas_used = 500000

[analysis]
max_steps = 1000000

[alert]
jsonl_path = "/var/log/sentinel/alerts.jsonl"

[dedup]
window_blocks = 10

[rate_limit]
max_alerts_per_minute = 60

[auto_pause]
enabled = false
confidence_threshold = 0.8
priority_threshold = "Critical"
auto_resume_secs = 300
```

### CLI override precedence

```
TOML config file  →  CLI --sentinel.* flags  →  defaults
                      (overrides TOML)
```

`merge_cli_overrides()` applies CLI values only for flags explicitly provided. Unset flags inherit from the TOML file, which in turn inherits from `Default::default()`.

### Validation

`SentinelFullConfig::validate()` checks all thresholds at startup:
- Float thresholds in [0.0, 1.0]
- Counts > 0
- Auto-resume duration > 0 when auto-pause enabled

---

## Design Summary (Updated)

| Decision | Rationale |
|----------|-----------|
| Two-stage pipeline | 99% of TXs filtered at stage 1, saving replay cost |
| BlockObserver trait in blockchain | Avoids circular dependency (DIP) |
| MempoolObserver trait in blockchain | Same DIP pattern, pre-execution monitoring |
| Dedicated OS thread | Compatible with LEVM sync traits, prevents async deadlock |
| Autopsy reuse | Proven classifiers reused, no code duplication |
| Local Store replay | No external dependency, μs latency |
| Clone before store | Block is consumed by `store_block()` — unavoidable |
| Feature flag separation | sentinel-only builds exclude reqwest and other heavy deps |
| Mutex around mpsc::Sender | mpsc::Sender is Send but not Sync; Mutex satisfies Observer bounds |
| AnalysisStep trait pipeline | Dynamic step composition with early exit and follow-up injection |
| Bounded dynamic step queue | MAX_DYNAMIC_STEPS=64 prevents DoS from step injection |
| FeatureVector all-f64 | Direct z-score math compatibility, avoids repeated casts |
| Combined confidence score | max(prefilter, pipeline) for best downstream signal |
| PauseController fast path | Single AtomicBool load on hot path — <1ns when not paused |
| Fail-open lock poisoning | Availability over pause enforcement — never crash block processing |
| Condvar::wait_timeout | Auto-resume without background timer thread |
| sentinel_resume authrpc-only | Control-plane mutation requires authentication |
| TOML + CLI override | 30+ params need hierarchical config, not just CLI flags |

---

## File Map (Updated)

| File | Purpose | Lines |
|------|---------|-------|
| `sentinel/mod.rs` | Module declarations | 18 |
| `sentinel/types.rs` | Config, SuspiciousTx, AlertPriority, SentinelAlert, SentinelError, MempoolAlert | 261 |
| `sentinel/pre_filter.rs` | 7 receipt-based heuristics, known address DB | 396 |
| `sentinel/replay.rs` | replay_tx_from_store, load_block_header | 149 |
| `sentinel/analyzer.rs` | DeepAnalyzer orchestration (legacy, kept for compat) | 175 |
| `sentinel/service.rs` | SentinelService background worker, AlertHandler, BlockObserver/MempoolObserver impl | 268 |
| `sentinel/alert.rs` | AlertDispatcher, JsonlFileAlertHandler, StdoutAlertHandler, dedup, rate limiting | 554 |
| `sentinel/webhook.rs` | WebhookAlertHandler (HTTP POST + exponential backoff) | 114 |
| `sentinel/history.rs` | AlertHistory JSONL query engine (pagination, filtering, sorting) | 596 |
| `sentinel/metrics.rs` | SentinelMetrics (Prometheus text exposition, 14 atomic counters) | 639 |
| `sentinel/ws_broadcaster.rs` | WsAlertBroadcaster (WebSocket live feed) | 265 |
| `sentinel/config.rs` | SentinelFullConfig TOML loader, CLI merge, validation | 496 |
| `sentinel/mempool_filter.rs` | MempoolPreFilter (5 calldata heuristics) | 553 |
| `sentinel/pipeline.rs` | AnalysisStep trait, 6 pipeline steps, FeatureVector, ConfidenceScorer | 1,190 |
| `sentinel/ml_model.rs` | StatisticalAnomalyDetector (z-score + sigmoid) | 233 |
| `sentinel/auto_pause.rs` | AutoPauseHandler circuit breaker | 139 |
| `sentinel/tests.rs` | 310 tests (H-1~H-6 full coverage) | 2,735 |
| `blockchain/blockchain.rs` | BlockObserver, MempoolObserver, PauseController (+5 tests) | +424 |
| `networking/rpc/rpc.rs` | sentinel_status (public), sentinel_resume (authrpc) | +58 |

---

## Known Limitations (Updated)

1. **Single worker thread**: One worker processes blocks sequentially. If deep analysis is slow, blocks queue up. Acceptable for current throughput requirements.
2. **PreFilter blind spot**: The 7 receipt-based heuristics miss stealthy attacks (1 wei, ~82k gas, successful, no ERC-20 transfers). The adaptive pipeline (H-6c) with anomaly scoring partially addresses this for post-execution analysis.
3. **MempoolPreFilter blind spot**: Signature-based calldata detection bypassed by custom contract interfaces. Not a security guarantee — fast early warning only.
4. **Anomaly model calibration**: `StatisticalAnomalyDetector::default()` uses conservative placeholder values (high stddev = low sensitivity). Production deployment requires calibration against mainnet data (blocks 18M-19M recommended).
5. **Unbounded mpsc channel**: `mpsc::channel()` between block processing and sentinel worker is unbounded. Under sustained block bursts, memory could grow. AlertRateLimiter provides downstream backpressure but doesn't back-pressure the channel itself.
6. **PauseController false positives**: A false-positive Critical alert pauses block processing for up to 5 minutes (auto-resume default). During this window, the node falls behind peers. Dual-threshold gating (priority AND confidence) mitigates but cannot eliminate this risk.
