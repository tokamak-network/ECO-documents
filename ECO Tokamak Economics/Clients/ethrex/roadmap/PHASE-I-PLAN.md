# Phase I: Sentinel Production Deployment — Implementation Plan

> Autopsy Lab + Sentinel을 연구 프로토타입에서 배포 가능한 서비스로 전환.

## 현재 상태 (Baseline)

| 영역 | 상태 | 근거 |
|------|------|------|
| 핵심 분석 엔진 | ✅ 완성 | 310+10 tests, 100k steps < 5s |
| CLI 플래그 | ✅ 완성 | 6개 `--sentinel.*` 옵션 정의됨 |
| init_sentinel() | ✅ 완성 | TOML 로드 → CLI 오버라이드 → AlertDispatcher 조립 |
| init_blockchain_with_sentinel() | ✅ 완성 | BlockObserver + PauseController 연결 |
| sentinel_status/resume RPC | ✅ 완성 | JSON-RPC via authrpc |
| Dashboard HTTP/WS 서버 | ❌ 없음 | sentinel_dashboard_demo.rs에만 존재 |
| init_l1() 연결 | ❌ 없음 | `None` 하드코딩 (line 656) |
| 메인넷 검증 | ❌ scaffold | 10개 테스트 전부 `#[ignore]` + `Vec::new()` |
| 운영 문서 | ❌ 없음 | 아키텍처 문서만 존재 |


## Task 목록

### I-1. init_l1() Sentinel 연결 (소)

**목표**: `--sentinel.enabled` 플래그가 켜졌을 때 Sentinel이 실제로 작동하는 상태.

**변경 파일**: `cmd/ethrex/initializers.rs`

**작업 내용**:
1. `init_l1()` 함수에서 `#[cfg(feature = "sentinel")]` 분기 추가
2. `init_sentinel()` 호출 → `SentinelComponents` 생성
3. `init_blockchain()` 대신 `init_blockchain_with_sentinel()` 호출
4. `pause_controller`를 `init_rpc_api()`에 전달 (현재 `None` → `sentinel.pause_controller`)
5. Mempool observer도 연결 (MempoolObserver trait)

**현재 코드** (line 600-656):
```rust
let blockchain = init_blockchain(store.clone(), BlockchainOptions { ... });
// ...
init_rpc_api(&opts, ..., None) // ← pause_controller is None
```

**목표 코드** (의사코드):
```rust
#[cfg(feature = "sentinel")]
let (blockchain, pause_controller) = {
    let sentinel = init_sentinel(&opts, store.clone());
    let pc = sentinel.pause_controller.clone();
    let bc = init_blockchain_with_sentinel(store.clone(), opts, sentinel);
    (bc, pc)
};
#[cfg(not(feature = "sentinel"))]
let (blockchain, pause_controller) = (init_blockchain(store.clone(), opts), None);
// ...
init_rpc_api(&opts, ..., pause_controller)
```

**테스트**:
- `cargo build --features sentinel` 빌드 성공 확인
- `cargo build` (sentinel 없이) 기존 동작 유지 확인
- `--sentinel.enabled` 플래그로 시작 시 "Sentinel initialized and ready" 로그 출력 확인

**예상 변경량**: ~30줄

---

### I-2. Dashboard HTTP/WS 서버 (대)

**목표**: `sentinel_dashboard_demo.rs`의 서버 로직을 ethrex-rpc에 통합. Dashboard가 실제 Sentinel에 연결 가능.

**배경**: `sentinel_dashboard_demo.rs`에 3개 endpoint가 이미 구현되어 있음:
- `GET /sentinel/metrics` — JSON metrics
- `GET /sentinel/history` — 페이지네이션 alert history
- `GET /sentinel/ws` — WebSocket 실시간 feed

이 로직을 demo에서 ethrex-rpc의 Axum 라우터로 이동.

**변경 파일**:
1. `crates/networking/rpc/rpc.rs` — Axum 라우터에 3개 REST/WS 라우트 추가
2. `crates/networking/rpc/sentinel/` — 새 모듈 (metrics, history, ws 핸들러)
3. `crates/networking/rpc/lib.rs` — sentinel 모듈 등록
4. `crates/networking/rpc/Cargo.toml` — sentinel feature dep 추가
5. `cmd/ethrex/initializers.rs` — SentinelMetrics + WsAlertBroadcaster + AlertHistory를 RpcApiContext에 전달

**설계 결정**:

| 결정 | 선택 | 근거 |
|------|------|------|
| 라우팅 방식 | Axum REST 라우트 (JSON-RPC 아님) | Dashboard는 REST/WS 기대. JSON-RPC는 부적합 |
| 배치 위치 | 기존 HTTP 서버 (8545)에 `/sentinel/*` 추가 | 별도 포트 불필요, 운영 복잡성 감소 |
| Feature gate | `#[cfg(feature = "sentinel")]` | sentinel 미사용 시 zero cost |
| State 전달 | `RpcApiContext`에 `Option<SentinelState>` 추가 | 기존 DI 패턴 활용 |

**SentinelState 구조**:
```rust
pub struct SentinelState {
    pub metrics: Arc<SentinelMetrics>,
    pub broadcaster: Arc<WsAlertBroadcaster>,
    pub history: AlertHistory,
}
```

**Endpoint 스펙**:

1. `GET /sentinel/metrics`
   - Response: `SentinelMetrics::snapshot()` → JSON
   - No auth required (read-only)

2. `GET /sentinel/history?page=1&page_size=20&priority=High&block_from=100&block_to=200`
   - Response: `AlertHistory::query()` → `AlertQueryResult` JSON
   - Query params → `AlertQueryParams` 변환
   - No auth required (read-only)

3. `GET /sentinel/ws` → WebSocket upgrade
   - `WsAlertBroadcaster::subscribe()` → per-client mpsc → WS frames
   - JSON text messages with `suspicion_reasons` 포맷 변환 (externally-tagged → `{type, details}`)
   - No auth required (read-only feed)

**테스트**:
- 3개 endpoint 핸들러 유닛 테스트
- WS upgrade + message 수신 통합 테스트
- sentinel feature 없이 빌드 시 라우트 미등록 확인

**예상 변경량**: ~400줄 (핸들러 200 + 라우팅 50 + state 전달 50 + 테스트 100)

---

### I-3. Dashboard 환경변수 기반 endpoint 설정 (소)

**목표**: `sentinel.astro`의 하드코딩 `localhost:3001` → 환경변수 기반 동적 설정.

**변경 파일**:
1. `dashboard/src/pages/sentinel.astro` — 환경변수 읽기
2. `dashboard/astro.config.mjs` — env 설정 (필요시)

**현재 코드**:
```astro
<SentinelMetricsPanel apiBase="http://localhost:3001/sentinel/metrics" />
<AlertFeed wsUrl="ws://localhost:3001/sentinel/ws" />
<AlertHistoryTable apiBase="http://localhost:3001/sentinel/history" />
```

**목표 코드**:
```astro
---
const sentinelApi = import.meta.env.PUBLIC_SENTINEL_API || 'http://localhost:8545';
const sentinelWs  = import.meta.env.PUBLIC_SENTINEL_WS  || sentinelApi.replace('http', 'ws');
---
<SentinelMetricsPanel apiBase={`${sentinelApi}/sentinel/metrics`} />
<AlertFeed wsUrl={`${sentinelWs}/sentinel/ws`} />
<AlertHistoryTable apiBase={`${sentinelApi}/sentinel/history`} />
```

**테스트**:
- 환경변수 미설정 시 기본값 `localhost:8545` 사용 확인
- `PUBLIC_SENTINEL_API=https://sentinel.example.com` 설정 시 올바른 URL 생성 확인
- `npm run build` 성공 확인

**예상 변경량**: ~15줄

---

### I-4. 메인넷 실전 검증 (중)

**목표**: `mainnet_validation.rs`의 10개 scaffold 테스트를 실제 archive node로 검증 가능하게 구현.

**현재 문제**: `analyze_tx()` 함수가 `Vec::new()` 반환 (line 60). TX를 가져오지만 실제 replay를 하지 않음.

**변경 파일**:
1. `crates/tokamak-debugger/src/tests/mainnet_validation.rs` — `analyze_tx()` 완전 구현
2. `crates/tokamak-debugger/src/autopsy/mod.rs` — 필요시 public API 노출

**작업 내용**:

1. `analyze_tx()` 구현 완성:
   ```rust
   fn analyze_tx(tx_hash_hex: &str) -> Vec<AttackPattern> {
       let url = rpc_url();
       let tx_hash = parse_tx_hash(tx_hash_hex);
       let client = EthRpcClient::new(&url, 0);
       let tx = client.eth_get_transaction_by_hash(tx_hash).unwrap();
       let block_number = tx.block_number.expect("must be mined");

       // 1. Build remote database at block_number - 1
       let db = RemoteVmDatabase::from_rpc(&url, block_number - 1).unwrap();

       // 2. Reconstruct TX environment
       // 3. Execute TX with OpcodeRecorder
       // 4. Build trace → AttackClassifier::classify()
       // 5. Return detected patterns
   }
   ```

2. TX 환경 재구성:
   - `eth_getBlockByNumber` → block header (gas_limit, timestamp, basefee 등)
   - `eth_getTransactionByHash` → TX details (from, to, value, data, gas)
   - Environment 구성 → LEVM `VM::new()` 호출

3. 각 테스트에 assertion 추가:
   ```rust
   fn validate_dao_hack_reentrancy() {
       let patterns = analyze_tx("0x0ec3f...");
       assert!(!patterns.is_empty(), "DAO hack must detect patterns");
       assert!(patterns.iter().any(|p| matches!(p, AttackPattern::Reentrancy { .. })));
   }
   ```

4. 불가능한 테스트 표시:
   - Mango Markets (Solana) → 삭제 또는 `#[ignore]` 유지 + 사유 명시
   - Ronin Bridge (private key compromise) → 패턴 미검출 예상 표시

**주의사항**:
- `RemoteVmDatabase`는 preceding TX 실행이 필요할 수 있음 (block 내 TX 순서)
- Archive node rate limit 대비 `RpcConfig { timeout: 30, max_retries: 5 }` 사용
- CI에서는 `#[ignore]` 유지 (archive node 없음) — 로컬에서만 수동 실행

**테스트 실행 방법**:
```bash
ARCHIVE_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/KEY \
  cargo test -p tokamak-debugger --features autopsy -- mainnet_validation --ignored
```

**목표**: 10개 중 최소 6개 올바른 패턴 검출 (DAO, Euler, Curve, Cream, bZx, Parity)

**예상 변경량**: ~200줄

---

### I-5. 운영자 배포 가이드 (중)

**목표**: 오퍼레이터가 Sentinel을 설정하고 실행할 수 있는 문서.

**출력 파일**: `docs/tokamak/SENTINEL-OPERATOR-GUIDE.md`

**내용 구조**:

```markdown
# Sentinel Operator Guide

## Quick Start
- 빌드: cargo build --features sentinel
- 실행: ethrex --sentinel.enabled --sentinel.alert-file alerts.jsonl
- Dashboard: PUBLIC_SENTINEL_API=http://HOST:8545 npm run dev

## Configuration
- TOML 설정 파일 예시 (sentinel.toml)
- CLI 플래그 설명 (6개)
- CLI가 TOML을 오버라이드하는 우선순위

## Alert Handlers
- JSONL file (기본)
- Stdout (컨테이너)
- Webhook (Slack/Discord)
- Auto-pause (circuit breaker)

## Dashboard
- 환경변수 설정
- Metrics 패널 설명
- Alert feed 설명
- History 테이블 필터링

## Monitoring
- Prometheus 메트릭 목록 (14개)
- Grafana 대시보드 예시 쿼리
- 핵심 알림 규칙

## Troubleshooting
- False positive 감소 방법 (threshold 조정)
- Auto-pause 복구 방법
- Archive node 연결 문제
```

**민감도**: PUBLIC (repo에 커밋 가능)

**예상 변경량**: ~300줄

---

## 의존성 그래프

```
I-1 (init_l1 연결)
 ├──→ I-2 (HTTP/WS 서버) ← I-1의 SentinelComponents가 있어야 State 전달 가능
 │     └──→ I-3 (Dashboard 환경변수) ← I-2의 endpoint가 있어야 URL 결정
 └──→ I-4 (메인넷 검증) ← 독립적이지만 I-1 이후가 자연스러움

I-5 (운영 문서) ← I-1~I-3 완료 후 최종 작성
```

**추천 실행 순서**:
1. **I-1** (소, ~30줄) → 빠르게 완료, 나머지의 전제조건
2. **I-4** (중, ~200줄) → I-1과 독립적이므로 병렬 가능
3. **I-2** (대, ~400줄) → 핵심 작업
4. **I-3** (소, ~15줄) → I-2 완료 직후
5. **I-5** (중, ~300줄) → 모든 구현 완료 후


## 리스크

| 리스크 | 심각도 | 대응 |
|--------|--------|------|
| RPC server에 REST 라우트 추가 시 기존 JSON-RPC와 충돌 | LOW | `/sentinel/*` prefix로 네임스페이스 분리, 기존 핸들러 영향 없음 |
| WsAlertBroadcaster in-process mpsc → 실제 WS 변환 시 메모리 | LOW | subscriber cleanup on broadcast + bounded channel |
| mainnet_validation에서 preceding TX 미실행 시 상태 불일치 | MEDIUM | 단순한 TX부터 시작 (DAO hack은 block 내 첫 TX), 복잡한 건 skip |
| sentinel feature 빌드 시간 증가 | LOW | feature gate로 비활성 시 zero cost |
| Archive node rate limit (Alchemy 25 RPS free tier) | MEDIUM | RpcConfig timeout 30s + max_retries 5 + 테스트 간 sleep |


## 완료 기준

| Task | Done 기준 |
|------|-----------|
| I-1 | `cargo build --features sentinel` 성공 + `--sentinel.enabled`로 시작 시 로그 출력 + 기존 빌드 미영향 |
| I-2 | Dashboard가 ethrex 노드의 `/sentinel/*` 엔드포인트에 연결되어 metrics/history/ws 동작 |
| I-3 | `PUBLIC_SENTINEL_API` 환경변수로 URL 변경 가능 + `npm run build` 성공 |
| I-4 | 10개 mainnet TX 중 6개 이상 올바른 패턴 검출 (archive RPC 필요) |
| I-5 | 오퍼레이터가 문서만 보고 sentinel 시작 + dashboard 연결 가능 |

**전체 완료 기준**: I-1~I-5 모두 통과 시 Sentinel은 **MVP 프로덕션 레벨**.
