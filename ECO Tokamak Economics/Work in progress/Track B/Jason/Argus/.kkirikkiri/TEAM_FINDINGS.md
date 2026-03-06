# 발견 사항 & 공유 자료

## 프로젝트 컨텍스트
- Rust 1.85+ (edition 2024), clippy warnings = errors
- Feature flags: `sentinel` (default), `autopsy` (default), `cli`, `ai_agent`
- 리포: https://github.com/tokamak-network/Argus
- 현재 브랜치: feature/batch-receipt-fetch
- License: MIT OR Apache-2.0

## 리뷰 참고 파일
- Devil review: docs/devil-review-public-readiness.md
- OSS review: docs/open-source-readiness-review.md

## 기존 파일 상태
- Dockerfile: rust:latest, no USER, no HEALTHCHECK, copies sentinel_alerts_backup.jsonl
- Cargo.toml: version 0.1.0, missing readme/homepage/documentation fields
- CI: .github/workflows/ci.yml (check/test/clippy/fmt, no cargo-audit)
- README Docker section: `tokamak-network/argus:v0.1.3`
- Docker Hub 실제: `tokamak/argus-demo` (확인 완료 — docker-publish.yml line 10에서 `IMAGE_NAME: tokamak/argus-demo`)
- README, deployment.md의 `tokamak-network/argus:v0.1.3` → `tokamak/argus-demo:latest`로 수정 완료
- SECURITY.md: 없음
- CHANGELOG.md: 없음
- CODE_OF_CONDUCT.md: 없음
- Issue/PR templates: 없음
- dependabot.yml: 없음

---

# DEAD_ENDS (시도했으나 실패한 접근)

(아직 없음)
