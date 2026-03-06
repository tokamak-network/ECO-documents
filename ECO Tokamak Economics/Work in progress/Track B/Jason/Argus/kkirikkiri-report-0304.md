# kkirikkiri-dev-0304 Integration Report

**Date**: 2026-03-04
**Team**: kkirikkiri-dev-0304
**Objective**: Argus Sentinel Dashboard Phase 1 — axum JSON handlers, CORS, Stitch UI design, frontend .env setup, and tests

---

## Summary

All 7 tasks completed successfully. Backend API endpoints, CORS middleware, frontend configuration, UI design, and all tests are verified and passing.

- **Rust tests**: 407 passed, 0 failed, 18 ignored
- **Frontend tests**: 97 passed, 0 failed (5 test files)
- **Clippy**: Clean (zero warnings with `-D warnings`)
- **Fmt**: Clean

---

## Deliverables

### 1. Backend: `src/sentinel/http_metrics.rs`

**New endpoints added to existing axum Router:**

| Endpoint | Method | Response | Tests |
|----------|--------|----------|-------|
| `GET /sentinel/metrics` | JSON | `{ blocks_scanned, txs_scanned, txs_flagged, alerts_emitted }` | 2 |
| `GET /sentinel/history` | JSON | `{ alerts, total, page, page_size }` | 7 |

**Preserved endpoints (unchanged behavior):**

| Endpoint | Method | Response |
|----------|--------|----------|
| `GET /metrics` | Prometheus text | Prometheus exposition format |
| `GET /health` | JSON | `{ status, blocks_scanned, txs_scanned, alerts_emitted, uptime_secs }` |

**CORS**: `CorsLayer::permissive()` applied to all routes (2 tests: header + preflight).

**Architecture changes:**
- `AppState` extended with `AlertHistory` and `Arc<WsAlertBroadcaster>`
- `start_metrics_server` signature updated: `alert_file: Option<PathBuf>`, `broadcaster: Option<Arc<WsAlertBroadcaster>>`
- `HistoryQuery` struct for query parameter deserialization
- `remap_suspicion_reasons` function: converts Rust externally-tagged enum to `{ type, details }` format

**`/sentinel/history` query parameters:**

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `page_size` | int | 20 | Items per page |
| `priority` | string | - | Min priority filter: medium, high, critical |
| `block_from` | u64 | - | Block range start (inclusive) |
| `block_to` | u64 | - | Block range end (inclusive) |
| `pattern_type` | string | - | Attack pattern filter |

**Response field mapping (Rust → HTTP JSON):**
- `AlertQueryResult.total_count` → `total`
- `SuspicionReason` externally-tagged → `{ type: string, details?: object }`

**Total backend tests**: 14 (3 existing + 11 new)

### 2. Frontend: `dashboard/`

**Files created:**
- `dashboard/.env` — `PUBLIC_SENTINEL_API=http://localhost:9090`, `PUBLIC_SENTINEL_WS=ws://localhost:9090`

**Type alignment verified:**
- `SuspicionReason`: `{ type: string, details?: Record<string, unknown> }` — matches backend remap
- `AlertQueryResult.total: number` — matches backend `"total"` field
- `AlertQueryParams.priority` — matches backend `HistoryQuery.priority` query param
- `SentinelMetricsSnapshot`: 4 fields match backend `/sentinel/metrics` response exactly

**Components verified:**
- `AlertHistoryTable.tsx`: Uses `data.total`, sends `priority` in query string
- `AlertCard.tsx`: Uses `reason.type` for suspicion reason display
- `SentinelMetricsPanel.tsx`: Reads 4 metric fields, computes flagged rate
- `AlertFeed.tsx`: WebSocket reconnect with exponential backoff, `AlertCard` rendering

**Frontend test suite**: 97 tests across 5 files (types, formats, data, components, sentinel)

### 3. Stitch UI Design

**Project**: Argus Sentinel Dashboard
- **Project ID**: `1151486258435224978`
- **URL**: https://stitch.google.com/projects/1151486258435224978

**Screens created (6):**
1. Main Dashboard (Metrics + Alert Feed)
2. Alert History Table (filters + pagination)
3. Dashboard Overview (combined view for screenshots)
4. Main Dashboard v2 (detailed color codes: #0d1117, #161b22)
5. Alert Detail View (suspicion score gauge, fund flows table)
6. Empty State / Landing Page (getting started guide)

**Design specs:**
- Theme: Dark slate (#0f172a background, #1e293b cards, #334155 borders)
- Color coding: Critical=#ef4444, High=#f97316, Medium=#eab308, Primary=#06b6d4
- Device: Desktop
- Font: Space Grotesk + monospace for hashes/numbers

---

## Integration Verification

### HTTP API Path (Full Stack)

```
Frontend (AlertHistoryTable)
  → GET /sentinel/history?priority=Critical&page=1&page_size=20
  → Backend (HistoryQuery → AlertQueryParams → AlertHistory::query)
  → Response: { alerts: [{..., suspicion_reasons: [{type: "FlashLoanSignature", details: {...}}]}], total: N, page: 1, page_size: 20 }
  → Frontend reads data.total, renders AlertCard with reason.type
```

**Verified**: All field names, types, and formats are consistent end-to-end for the HTTP API path.

### Metrics API Path

```
Frontend (SentinelMetricsPanel)
  → GET /sentinel/metrics
  → Response: { blocks_scanned: N, txs_scanned: N, txs_flagged: N, alerts_emitted: N }
  → Frontend renders 4 metric cards + computes flagged rate
```

**Verified**: 4 field names match exactly. Backend filters out 10 internal-only fields from MetricsSnapshot.

### WebSocket Path (Known Limitation)

```
Frontend (AlertFeed)
  → WebSocket connect to /sentinel/ws
  → Receives raw serde-serialized SentinelAlert JSON
  → AlertCard renders with reason.type
```

**Known gap**: `ws_broadcaster.rs` sends raw Rust serde externally-tagged format `{"FlashLoanSignature": {...}}`, but `AlertCard.tsx` reads `reason.type` expecting `{type: "FlashLoanSignature"}`. The WebSocket upgrade handler (`/sentinel/ws`) is not yet implemented in the axum Router — it is a future task. When implemented, the same `remap_suspicion_reasons` transformation should be applied to WebSocket messages.

### CORS

**Verified**: `CorsLayer::permissive()` applied. Tests confirm `access-control-allow-origin: *` on responses and `200 OK` on preflight OPTIONS requests.

---

## Issues Found and Resolved During Review

### Round 1: Backend Review

| # | Severity | Issue | Resolution |
|---|----------|-------|------------|
| 1 | CRITICAL | Backend returned `total_count`, frontend expected `total` | Backend handler manually maps `total_count` → `total` in JSON response |
| 2 | MEDIUM | `suspicion_reasons` sent as raw externally-tagged enum | Added `remap_suspicion_reasons` function in handler (pattern from `sentinel_dashboard_demo.rs`) |
| 3 | LOW | `/sentinel/metrics` returned all 14 MetricsSnapshot fields | Restricted to 4 dashboard-facing fields only |

### Round 2: Frontend Alignment

Frontend-dev initially adapted TS types to match backend's native format. After backend applied review fixes, TS types were reverted to original format which now matches the backend's remapped output. Final state is consistent.

---

## Known Limitations (Future Work)

1. **WebSocket suspicion_reasons format**: `ws_broadcaster.rs` sends raw externally-tagged format. When the WebSocket upgrade route is added, apply `remap_suspicion_reasons` to outgoing messages.

2. **No WebSocket route in axum Router**: The current Router has no `/sentinel/ws` endpoint. `WsAlertBroadcaster` is wired into `AppState` but not exposed via HTTP yet.

3. **`sort_order` query param**: Backend `HistoryQuery` does not include `sort_order` in the deserialized struct (hardcoded to `SortOrder::Newest`). Adding this is a minor enhancement.

4. **Alert file path**: `start_metrics_server` defaults to `sentinel_alerts.jsonl` if no path provided. The CLI `--alert-file` option passes this through.

---

## File Manifest

### Modified Files

| File | Changes |
|------|---------|
| `src/sentinel/http_metrics.rs` | Added `AppState`, `HistoryQuery`, `/sentinel/metrics` handler, `/sentinel/history` handler, `remap_suspicion_reasons`, CORS layer, 11 new tests |
| `src/sentinel/metrics.rs` | Added `Serialize` derive to `MetricsSnapshot` |

### New Files

| File | Purpose |
|------|---------|
| `dashboard/.env` | Frontend environment variables for backend connection |

### Unchanged Files (Verified Compatible)

| File | Status |
|------|--------|
| `dashboard/src/types/sentinel.ts` | Original types match backend's remapped output |
| `dashboard/src/components/AlertHistoryTable.tsx` | `data.total` and `priority` query param match backend |
| `dashboard/src/components/AlertCard.tsx` | `reason.type` matches backend's remapped format |
| `dashboard/src/components/SentinelMetricsPanel.tsx` | 4 field names match backend response |
| `dashboard/src/components/AlertFeed.tsx` | WebSocket reconnect logic unchanged |
| `dashboard/src/components/AlertPriorityBadge.tsx` | Priority display unchanged |
| `dashboard/src/__tests__/sentinel.test.tsx` | 21 tests passing |
| `src/sentinel/history.rs` | Alert history storage unchanged |
| `src/sentinel/ws_broadcaster.rs` | WebSocket broadcaster unchanged |
| `src/sentinel/types.rs` | SentinelAlert type unchanged |

---

## Quality Metrics

| Metric | Result |
|--------|--------|
| Rust tests | 407 passed, 0 failed, 18 ignored |
| Frontend tests | 97 passed, 0 failed |
| Clippy | Clean (`-D warnings`) |
| Fmt | Clean |
| PRD constraints | All respected (no pipeline changes, no new npm deps, no mutation, existing endpoints preserved) |
| Existing test regression | None |
| New backend tests | 11 |
| New frontend tests | 0 (existing 21 sentinel tests already covered the components) |
