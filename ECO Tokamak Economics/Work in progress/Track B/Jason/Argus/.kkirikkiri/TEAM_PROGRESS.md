# 진행 상황

## trust-builder
- [시작] Phase A: Trust Scaffolding (SECURITY.md, CHANGELOG.md, CODE_OF_CONDUCT.md)
- 시작 시각: 2026-03-06

## infra-hardener
- [시작] Phase B+C+D: Dockerfile 경화, Cargo.toml, CI, 버전 통일
- 시작 시각: 2026-03-06
- [완료] Phase B: Dockerfile 경화
  - B-1: rust:latest → rust:1.85-bookworm
  - B-2: non-root user (argus:argus) 추가
  - B-3: HEALTHCHECK 추가
  - B-4: sentinel_alerts_backup.jsonl COPY 제거
  - B-5: runtime deps에 curl 추가
- [완료] Phase C: Cargo.toml + CI
  - C-1: readme, homepage, documentation 필드 추가
  - C-2: ci.yml에 cargo-audit job 추가
- [완료] Phase D: 버전/이름 통일
  - D-1: Docker Hub 실제 이미지명 확인 → `tokamak/argus-demo` (docker-publish.yml)
  - README, deployment.md: `tokamak-network/argus:v0.1.3` → `tokamak/argus-demo:latest` 수정
  - ECR 관련 명령어(deployment.md)는 사용자 커스텀이므로 유지

## translator
- [시작] Phase E: 영어 번역 (ROADMAP.md, competitive-analysis.md)
- 시작 시각: 2026-03-06
- [완료] E-1: docs/ROADMAP.md 영문 번역 완료
  - 159줄 한국어 → 161줄 영문 (100% 번역, 내용 축소 없음)
  - Phase 0/1/2/AI-0/AI-1/3 + 전략 전환 테이블 전체 포함
  - 정직한 자기진단 톤 유지 (Critical/High/Medium 심각도, Bus Factor=1, ethrex ~0%)
- [완료] E-2: docs/competitive-analysis.md 영문 번역 완료
  - 198줄 한국어 → 197줄 영문 (100% 번역, 내용 축소 없음)
  - 9열 비교표 + 각주 10개 + 6개 약점 + 포지셔닝 전략 전체 포함
  - 정직한 자기비판 톤 유지 ("Zero production detection record", "Bus Factor = 1", "ethrex market share ~0%")
  - 앵커 링크 영문화: #1-ethrex-종속--tam-문제 → #1-ethrex-dependency--tam-problem
