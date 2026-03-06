# 팀 작업 계획

- 팀명: kkirikkiri-dev-0306
- 목표: Argus Public Release Readiness — 두 리뷰(Devil 8.20, OSS Review) 반영, 6개 Phase 실행
- 생성 시각: 2026-03-06

## 리뷰 소스
- `docs/devil-review-public-readiness.md` — Devil 점수 8.20 (Code 8.95, Public Readiness 7.70)
- `docs/open-source-readiness-review.md` — Claude+Codex 리뷰

## 팀 구성
| 이름 | 역할 | 모델 | 담당 업무 |
|------|------|------|----------|
| lead | 팀장 | Opus | 계획/배분/검증/통합 |
| trust-builder | Trust 담당 | Opus | Phase A (SECURITY.md, CHANGELOG.md, CODE_OF_CONDUCT.md) + Phase F (GitHub templates) |
| infra-hardener | Infra 담당 | Opus | Phase B (Dockerfile) + Phase C (Cargo.toml, CI) + Phase D (버전 통일) |
| translator | 번역 담당 | Opus | Phase E (ROADMAP.md, competitive-analysis.md 영어 번역) |

## 태스크 목록

### Phase A: Trust Scaffolding
- [ ] A-1: SECURITY.md 생성 → trust-builder
- [ ] A-2: CHANGELOG.md 생성 (v0.1.0→v0.1.3, git log 기반) → trust-builder
- [ ] A-3: CODE_OF_CONDUCT.md 생성 (Contributor Covenant) → trust-builder

### Phase B: Dockerfile 경화
- [ ] B-1: rust:latest → rust:1.85-bookworm 고정 → infra-hardener
- [ ] B-2: non-root USER 추가 → infra-hardener
- [ ] B-3: HEALTHCHECK 추가 → infra-hardener
- [ ] B-4: sentinel_alerts_backup.jsonl COPY 제거 → infra-hardener
- [ ] B-5: curl 추가 (healthcheck용) → infra-hardener

### Phase C: Cargo.toml + CI
- [ ] C-1: Cargo.toml에 readme, homepage, documentation 추가 → infra-hardener
- [ ] C-2: ci.yml에 cargo-audit 스텝 추가 → infra-hardener

### Phase D: 버전/이름 통일
- [ ] D-1: Docker Hub 실제 이미지명 확인 후 README/docs 통일 → infra-hardener
- [ ] D-2: Cargo.toml version 업데이트 (필요시) → infra-hardener

### Phase E: 영어 번역
- [ ] E-1: docs/ROADMAP.md 영문 번역 → translator
- [ ] E-2: docs/competitive-analysis.md 영문 번역 → translator

### Phase F: GitHub 템플릿
- [ ] F-1: .github/ISSUE_TEMPLATE/bug_report.md → trust-builder
- [ ] F-2: .github/ISSUE_TEMPLATE/feature_request.md → trust-builder
- [ ] F-3: .github/PULL_REQUEST_TEMPLATE.md → trust-builder
- [ ] F-4: .github/dependabot.yml → trust-builder

## 주요 결정사항

1. **Cargo.toml version은 0.1.0 유지** — git 태그가 v0.1.0만 존재하므로 함부로 올리지 않음
2. **Docker 이미지명은 `tokamak/argus-demo:latest`로 통일** — docker-publish.yml에서 실제 이미지명 `tokamak/argus-demo` 확인됨 (infra-hardener가 소스 확인 후 수정)
3. **CHANGELOG 날짜**: v0.1.0 (2026-02-28), v0.1.1 (2026-03-04), v0.1.2 (2026-03-04), v0.1.3 (2026-03-05)
4. **보안 연락처**: security@tokamak.network
5. **Task #2 (GitHub templates)는 Task #1 완료 후 진행** — trust-builder가 순차 실행
6. **번역은 원문 대체** — 한국어 원본을 영어로 완전 대체, /docs/ko/ 별도 보관 안 함

## 태스크 배분 완료 (2026-03-06)
- trust-builder: Task #1, #2 (순차)
- infra-hardener: Task #3
- translator: Task #4

## 검증 결과

### Task #3 (infra-hardener) — PASS
검증 시각: 2026-03-06

| 항목 | 결과 | 비고 |
|------|------|------|
| B-1: rust:1.85-bookworm 고정 | PASS | Dockerfile line 1 |
| B-2: non-root USER | PASS | groupadd/useradd + USER argus (lines 26-30) |
| B-3: HEALTHCHECK | PASS | curl + /health (lines 37-38) |
| B-4: sentinel_alerts_backup.jsonl 제거 | PASS | 해당 라인 없음 |
| B-5: curl 추가 | PASS | runtime deps에 curl 포함 (line 18) |
| C-1: Cargo.toml readme/homepage/documentation | PASS | lines 10-12 |
| C-2: cargo-audit CI | PASS | ci.yml audit job (lines 53-60) |
| D-1: Docker 이미지명 통일 | PASS | README + deployment.md 모두 `tokamak/argus-demo:latest` |
| D-2: version 유지 | PASS | 0.1.0 유지 |

특이사항: infra-hardener가 docker-publish.yml에서 실제 이미지명 `tokamak/argus-demo`를 확인하여 내 초기 지시(`tokamak-network/argus:latest`)보다 정확한 이름으로 수정. 올바른 판단.

### Task #4 (translator) — PASS (1건 수정 후)
검증 시각: 2026-03-06

| 항목 | 결과 | 비고 |
|------|------|------|
| E-1: ROADMAP.md 영문 번역 | PASS | 161줄, Phase 0~3 + AI-0/AI-1 + 전략 전환 테이블 전부 포함 |
| E-2: competitive-analysis.md 영문 번역 | PASS | 198줄, 9열 비교표 + 각주 10개 + 약점 6개 + 포지셔닝 전략 |
| 한국어 잔여 | PASS | 없음 — 전체 영문 |
| 자기비판 톤 유지 | PASS | "Zero production detection record", "Bus Factor = 1", "ethrex ~0%" 전부 보존 |
| 기술 용어 정확성 | PASS | Sentinel, PreFilter, ethrex LEVM, Reth ExEx 등 일관 |
| Docker 이미지명 통일 | FIXED | 원문에 있던 `tokamak/argus` → lead가 `tokamak/argus-demo`로 수정 (2곳) |
