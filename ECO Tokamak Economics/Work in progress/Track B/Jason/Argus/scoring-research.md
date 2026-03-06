# Argus Scoring System Research — 경쟁사 및 학술 분석

> 2026-03-05 작성. ECS Sentinel 운영 중 Balancer Vault 오탐 폭증 → Alchemy 비용 급증 계기로 스코어링 개선 리서치.

## 현재 문제

Argus의 가산(additive) 스코어링이 정상 DeFi 활동을 Critical로 분류:

```
flash_loan(0.3) + erc20_transfers(0.2) + known_contract(0.2) + unusual_gas(0.3) = 1.0 → Critical
```

Balancer Vault 아비트라지가 매 블록마다 deep RPC replay를 트리거 → Alchemy 아카이브 노드 비용 폭증.

---

## 1. 경쟁사 스코어링 방식

### Forta Network (소스코드 확인)

**Anomaly Score 계산:**
```python
anomaly_score = alert_count / scan_count  # 24시간 기준
# 예: 5 alerts / 1,000,000 TXs = 0.000005
```

**Attack Detector 조합 알고리즘:**
```python
# 공격 4단계: Funding → Preparation → Exploitation → Money Laundering
scores_by_stage = alerts.groupby('stage').min()  # 단계별 최소값
combined = scores_by_stage.prod()                 # 단계 간 곱셈

# 임계값
CRITICAL = 1e-7   # ATTACK-DETECTOR-3
LOW      = 1e-4   # ATTACK-DETECTOR-4

# 추가 조건: 최소 3개 서로 다른 봇이 발화해야 함 (MIN_ALERTS_COUNT = 3)
```

**오탐 억제 5단계:**
1. 컨트랙트 주소 → 공격자 분류 불가 (EOA만 해당)
2. Etherscan 라벨 존재 시 억제 ("Uniswap: Router", "Binance 14" 등)
3. MEV 봇 탐지 봇이 아비트라지/샌드위치/청산 봇 식별 → 억제
4. TX count > 500인 EOA → 억제
5. Positive reputation 봇 3단계 별도 운영

**FORTRESS (pre-execution, 롤업 미들웨어):**
- 신경망 기반, <60ms latency
- 자체 보고: >99% recall, <0.0002% FP rate
- 독립 검증 없음 (proprietary)

### Hexagate (Chainalysis)

- 사전 시뮬레이션(GateSigner): TX 서명 전 downstream 효과 시뮬레이션
- 행동 컨텍스트: "누가, 과거 행동과 얼마나 다른가" 평가
- Invariant 모니터링: `Initialized`, `RoleGranted`, `RemovedOwner` 이벤트 감시
- 실적: Venus Protocol $13M 구출 (공격 18시간 전 탐지)

### Hypernative

- Guardian: 시뮬레이션 → 실시간 risk score → approve/deny/manual review 3단계 판정
- ML + 휴리스틱 + 시뮬레이션 + 그래프 분석 결합
- 자체 보고: 99.5% 탐지, 0.001% FP (독립 검증 없음)
- 200+ risk type 커버

### OpenZeppelin Defender (2026.07 종료 예정)

- 점수 없음, boolean 규칙 매칭 (match/no-match)
- TX 속성 필터: value, gasPrice, gasUsed, to, from, status
- 강점은 자동 대응 (Relayer + Autotask), 탐지 정확도가 아님

---

## 2. 프로덕션 보안 시스템의 스코어링 비교

### Splunk RBA (Risk-Based Alerting)

```
risk_score = (impact * confidence) / 100  # 개별 시그널
total_risk = SUM(risk_scores)              # 엔티티별 누적
alert if total_risk > threshold            # 보통 100-200
```

Risk Modifiers (가산):
- 외부 노출 자산: +20
- 관리자 계정: +30
- 업무 외 시간: +10

결과: 전통 알림 대비 **80-90% FP 감소**.

### IBM QRadar

```
Magnitude = weighted_mean(Severity, Relevance, Credibility)
```

핵심: **Relevance = 0이면 심각도 무관하게 무시.** Windows 공격이 Linux 서버에 → 무관 → 스킵.
→ Argus 적용: 재진입 패턴이 ETH 0인 컨트랙트에 → 무관 → 스킵.

### FICO Falcon (신용카드 사기 탐지)

- 400+ 속성, <1ms, 1-999 점수
- **개체별 행동 baseline** (카드홀더별 정상 패턴)
- 정상 패턴 대비 편차가 점수
- Kalman filter 기반 프로파일 지속 업데이트

### CVSS v3.1 (취약점 심각도)

```
ISCBase = 1 - [(1-ImpactConf) * (1-ImpactInteg) * (1-ImpactAvail)]  # 독립 차원: 곱셈
BaseScore = Impact + Exploitability                                    # 순차 단계: 덧셈
TemporalScore = BaseScore * ExploitMaturity * RemediationLevel         # 시간 조정: 곱셈
```

패턴: **독립 차원은 곱셈, 보완적 단계는 덧셈, 조정 계수는 곱셈.**

---

## 3. 학술 연구 핵심 결과

### 블록체인 공격 탐지

| 접근법 | 논문 | 성능 | 비고 |
|--------|------|------|------|
| Cash flow graph + GNN | DeFiGuard (IEEE TIFS 2024) | MLP 대비 우수 | 4개 노드 특성: type, frequency, diversity, profit |
| Cash flow tree | DeFiRanger (IEEE TDSC 2023) | P=0.996, TPR=0.962 | 432 실제 공격 탐지, 5개 zero-day |
| 컨트랙트 바이트코드 분석 | SMARTCAT (USENIX Security 2025) | R=91.6%, P=~100% | 배포 블록에서 탐지, 25초 이내 |
| LLM 기반 가격 조작 | DeFiScope (ASE 2025) | R=80%, P=96%, FP=0 | DeFiRanger(51.6%) 대비 큰 향상 |
| Opcode bigram | 여러 논문 | 96%+ P/R (재진입) | Shannon 엔트로피 기반 |
| Transformer 재구성 오류 | BlockScan (2024) | ETH+Solana 양쪽 고성능 | BERT-style, MLM 학습 |
| 앙상블 스태킹 | Arafat et al. (PeerJ CS 2025) | 98%+ F1 | RF+XGBoost+NN, SMOTEENN |

### MEV vs 공격 구분 — 핵심 특성

| 특성 | 아비트라지 (정상) | 공격 |
|------|-------------------|------|
| 자금 흐름 | **대칭** (차입→스왑→상환) | **비대칭** (차입→익스플로잇→신규 주소) |
| 컨트랙트 나이 | 오래됨 (반복 사용) | **24시간 이내 배포** |
| 이익 규모 | 얇은 마진 (0.01-1%) | **이상 고수익** |
| 상호작용 대상 | 알려진 DEX/프로토콜 | 미확인 컨트랙트 포함 |
| TX 패턴 | 반복적, 예측 가능 | 일회성, 이례적 |

### 정보 이론적 접근

**Opcode bigram 엔트로피:**
```
H(X) = -SUM(p(x_i) * log2(p(x_i)))
anomaly = |H(current) - H(baseline)| / H(baseline)
```
- 재진입: 낮은 엔트로피 (반복적 CALL/SSTORE)
- 난독화 공격: 비정상적 높은 엔트로피

---

## 4. Base Rate Fallacy — 가장 중요한 문제

Axelsson(2000) 계산:

```
조건: 1,000,000 이벤트/일, 공격 2건/일
탐지율 100%, 오탐률 0.001% (10만 건당 1건)

P(공격|알림) = (1.0 * 0.000002) / (0.000002 + 0.00001 * 0.999998)
            = 16.7%

→ 알림 6건 중 5건이 오탐
```

**P(공격|알림) >= 50%이려면 FP rate < P(공격) = 2*10⁻⁶ 필요.**

프로덕션 해결법:
1. **다단계 필터링** — 각 단계가 base rate를 올림
2. **시간 축적** — 단일 이벤트로 알림 X, 엔티티별 누적 필요
3. **개체별 baseline** — 전체 평균이 아닌 컨트랙트별 정상 패턴
4. **비용 민감 임계값** — `FP비용 * FP율 + FN비용 * FN율` 최소화

---

## 5. 스코어링 방식 비교

| 방식 | 공식 | 장점 | 단점 | 적합한 용도 |
|------|------|------|------|-------------|
| **가산** | `Σ(impact × confidence)` | 직관적, 디버깅 쉬움 | 조건부 의존성 무시 | 시간 축적 알림 (Splunk) |
| **곱셈** | `Π(factor_i)` | 독립 확률에 최적 | 보정 실패 시 전체 오염 | 독립 차원 조합 (CVSS) |
| **Log-odds Bayesian** | `sigmoid(log_prior + Σlog_LR_i)` | 수학적 건전, 확률 출력 | 학습 데이터 필요 | 다수 독립 특성 분류 |
| **하이브리드** | 단계별 다른 방식 | 각 단계에 최적 | 복잡도 | **프로덕션 시스템 전부** |

---

## 6. Argus 권장 아키텍처

```
Stage 1: Pre-Filter (가산 + relevance gate)
  signal_score = impact * confidence
  total = SUM(signal_scores)
  adjusted = total * relevance_factor     ← QRadar 패턴
  relevance_factor:
    - KnownContract → 0.3 (화이트리스트가 아닌 감점)
    - 미확인 컨트랙트 → 1.0
    - ETH 0 컨트랙트 → 0.1
  최소 2개 독립 시그널 필요 (Forta MIN_ALERTS_COUNT 패턴)

Stage 2: Deep Analyzer (특성 기반)
  opcode bigram 엔트로피
  cash flow 대칭성 (대칭 = 아비트라지, 비대칭 = 공격 의심)
  컨트랙트 나이 (24h 이내 배포 = 의심↑)
  이익 규모 이상치

Stage 3: AI Agent (LLM 판정)
  AgentContext → LLM → AgentVerdict
  Log-odds 기반 confidence 출력
  Hallucination Guard로 증거 검증

FP 억제 레이어:
  - MEV 봇 패턴 인식 → 억제
  - TX count > 500 EOA → 의심↓ (Forta 패턴)
  - Known DeFi 프로토콜 → relevance 조정
  - 컨트랙트 배포 후 24h 이내 아닌 경우 → 의심↓
```

### 즉시 적용 가능한 3가지

1. **`KnownContractInteraction`을 relevance gate로 전환** — 의심도 증가 → relevance=0.3 감점
2. **flash loan 단독 deep analysis 진입 차단** — 최소 2개 독립 시그널 필요
3. **자금 흐름 대칭성 체크 추가** — 차입→상환 대칭 = 아비트라지, 비대칭 = 공격

---

## 참고 자료

### 경쟁사
- [Forta Attack Detector Bot](https://docs.forta.network/en/latest/attack-detector-bot/)
- [Forta starter-kits GitHub](https://github.com/forta-network/starter-kits/tree/main/alert-combiner-py)
- [Forta bot-alert-rate GitHub](https://github.com/forta-network/bot-alert-rate)
- [Forta Attack Detector 2.0 Blog](https://www.forta.org/blog/attack-detector-2)
- [Hexagate Product](https://www.chainalysis.com/product/hexagate/)
- [Hexagate Venus Protocol Case Study](https://www.chainalysis.com/blog/hexagate-and-community-stops-a-hack-on-venus-protocol/)
- [Hypernative Guardian](https://www.hypernative.io/products/hypernative-guardian)

### 프로덕션 보안 시스템
- [Splunk RBA Risk Score Calculation](https://github.com/splunk/security_content/wiki/6.1-%E2%80%90-How-are-risk-score-calculated-for-RBA)
- [QRadar Offense Prioritization](https://www.ibm.com/docs/en/qsip/7.5?topic=management-offense-prioritization)
- [CVSS v3.1 Equations](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator/v31/equations)
- [FICO Falcon Fraud Manager](https://www.fico.com/en/products/fico-falcon-fraud-manager)
- [Axelsson Base Rate Fallacy (2000)](https://people.scs.carleton.ca/~soma/id-2007w/readings/axelsson-base-rate.pdf)

### 학술 논문
- DeFiGuard: [arXiv 2406.11157](https://arxiv.org/abs/2406.11157) (IEEE TIFS 2024)
- DeFiRanger: [arXiv 2104.15068](https://arxiv.org/abs/2104.15068) (IEEE TDSC 2023)
- SMARTCAT: [USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-bosi)
- DeFiScope: [arXiv 2502.11521](https://arxiv.org/abs/2502.11521) (ASE 2025)
- BlockScan: [arXiv 2410.04039](https://arxiv.org/abs/2410.04039)
- Ensemble Stacking: [PeerJ CS 2025](https://peerj.com/articles/cs-2630/)
