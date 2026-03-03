## 1. 개요

본 문서는 Tokamak Network의 DAO 거버넌스 모델을 정의한다. Tokamak Network Economics Whitepaper V2에서 제시한 검증 경제학(Verification Economics)과 TON Staking V3 모델을 기반으로, 분산화된 의사결정 구조를 구축한다. 이를 위한 핵심 설계 원칙으로 다음을 적용한다:

- TON과 vTON의 역할 분리를 통해 경제적 기능과 거버넌스 기능 간의 충돌을 방지한다.
- 투표권 집중을 구조적으로 제한하여 소수에 의한 거버넌스 장악을 방지한다.
- Security Council을 통해 긴급 상황에 신속히 대응하되, 권한 남용을 방지한다.

## 2. TOKEN (vTON)

### 2.1 vTON 정의

vTON은 Tokamak Network의 거버넌스 토큰이다. TON은 경제적 유틸리티(가스, 담보, 브릿지)를 담당하고, vTON은 투표권으로 활용된다. 두 토큰의 역할 분리를 통해 경제적 기능과 거버넌스 기능 간의 충돌을 방지한다.

### 2.2 vTON Distribution

vTON은 시뇨리지를 받는 주체에게 시뇨리지 비율에 따라 분배된다. 시뇨리지는 L2 Operator, Validator, DAO Treasury 세 주체가 받으며, vTON은 L2 Operator와 Validator 두 주체에게 분배된다.

| 수령 주체 | 시뇨리지 (TON) | vTON |
| --- | --- | --- |
| L2 Operator (시퀀서) | ✓ | ✓ |
| Validator | ✓ | ✓ |
| DAO Treasury | ✓ | ✗ |

DAO Treasury는 시뇨리지를 수령하지만 vTON은 받지 않는다. Treasury의 주요 용도는 생태계 그랜트, 운영 비용, 유동성 공급, 비상 대응 등 경제적 지출이며, 이는 TON으로 충당된다. vTON은 투표권인데, Treasury가 이를 보유하면 "그 투표권을 누가 대신 행사할 것인가?"를 또 투표로 정해야 하는 불필요한 복잡성이 생긴다. Treasury는 자금을 보관하고 운용하는 역할이지 스스로 의사결정을 내리는 주체가 아니므로, vTON을 배제하는 것이 적절하다.

### 2.3 발행 방식

무한 발행 방식을 채택한다. 다만 DAO가 시뇨리지 대비 vTON 발행 비율을 조정할 수 있으며, 이 비율은 최소 0에서 최대 1까지 설정 가능하다. 0으로 지정하면 시뇨리지에 따른 vTON의 추가 발행은 일어나지 않는다.

| 파라미터 | 초기값 | 범위 | 설명 |
| --- | --- | --- | --- |
| vTON 발행 비율 | 1 | 0 ~ 1 | 시뇨리지 대비 vTON 발행 비율 |

### 2.4 Tradeable

vTON은 거래가 가능하다. vTON 보유자는 직접 delegate에게 위임하는 대신, 투표권을 필요로 하는 다른 참여자에게 vTON을 판매할 수 있다. 이를 통해 거버넌스 참여에 관심이 없는 보유자도 경제적 가치를 실현할 수 있고, 적극적인 거버넌스 참여를 원하는 주체는 시장에서 투표권을 확보할 수 있다.

### 2.5 Not-burnable

vTON은 투표 시 소각되지 않는다. 투표는 토큰을 소비하는 행위가 아니라 보유량에 따른 권한 행사다. 투표할 때마다 vTON이 소각되면 보유자는 중요한 안건에만 투표하게 되어 일상적인 거버넌스 참여가 저해된다.

## 3. VOTING MECHANISM

### 3.1 Delegation

거버넌스 제안은 기술적 복잡성, 경제적 영향, 보안 고려사항 등 다양한 전문 지식을 요구한다. 모든 vTON 보유자가 각 안건을 충분히 검토할 시간과 전문성을 갖추기는 현실적으로 어렵다. Delegation은 이 문제를 해결한다. 보유자는 자신의 투표권을 신뢰할 수 있는 전문가에게 위임하고, delegate는 위임받은 투표권을 바탕으로 안건을 분석하고 의사결정에 참여한다.

### **3.2 Delegate 등록**

Delegate가 되려면 다음 정보를 공개적으로 등록해야 한다:

| 항목 | 설명 |
| --- | --- |
| Name | 커뮤니티 내 식별 및 인지도 구축 |
| About me | 배경과 전문성 공유를 통한 신뢰 형성 |
| Why I want to be a delegate | 투표 철학과 목표 공개로 위임자의 선택 지원 |
| Address or ENS | 온체인 투표 실행을 위한 지갑 연결 |

이 요건은 시빌 공격을 억제한다. 익명 지갑 여러 개를 만드는 것은 쉽지만, 각각의 delegate로서 커뮤니티의 신뢰를 얻어 위임을 받는 것은 어렵기 때문이다.

### **3.3 Delegation 방식**

vTON 보유자는 직접 투표할 수 없으며, 반드시 delegate에게 위임해야 한다. 위임하지 않은 vTON은 투표권으로 행사되지 않는다.

본인이 직접 투표권을 행사하려면 delegate로 등록해야 하며, 이 경우에도 동일한 등록 요건이 적용된다. Operator와 Validator도 시뇨리지로 받은 vTON을 delegate에게 위임해야 한다. 자신이 delegate로 등록하여 본인에게 위임할 수도 있고, 다른 delegate에게 위임할 수도 있다.

위임은 언제든 철회(undelegate)하고 다른 delegate에게 재위임할 수 있다.

### 3.4 투표권 산정

vTON을 delegate에게 위임하면 해당 시점이 온체인에 기록된다. 위임된 vTON은 7일 후 투표권으로 활성화되며, 대기 중인 투표권을 Pending Voting Power라 한다. 이 기간은 DAO 투표를 통해 조정할 수 있다.

| 파라미터 | 초기값 | 설명 |
| --- | --- | --- |
| 활성화 대기 기간 | 7일 | 위임 후 투표권 활성화까지 필요한 기간 |

Pending Voting Power의 상태 전이는 다음과 같다:

```
위임 실행 (Day 0)
      │
      ▼
Pending Voting Power (Day 0~6): 투표권 없음, Undelegate 불가
      │
      ▼
Active Voting Power (Day 7~): 투표권 행사 가능, Undelegate 가능
```

이 설계는 스냅샷 직전 대량 매집 공격을 방어한다. 일반적인 스냅샷 방식은 제안 생성 시점의 보유량만 확인하므로, 공격자가 스냅샷 직전에 토큰을 매집하고 투표 후 매도하는 것이 가능하다. Pending Voting Power는 위임 시점 기준 7일 대기를 요구하여 단기 매집을 통한 투표권 확보를 원천 차단한다. 해당 설정값은 DAO 투표를 통해 변경할 수 있다.

### 3.5 Proposal Creation

제안을 생성하려면 전체 vTON 발행량의 0.25% 이상을 보유해야 한다. 이는 스팸 제안을 방지하면서도 충분한 지분을 가진 주체만 제안할 수 있도록 한다. 실제로 이 수준의 vTON을 보유한 주체는 대부분 delegate이므로, 일반적으로 delegate가 제안을 생성하게 된다.

| 파라미터 | 초기값 | 설명 |
| --- | --- | --- |
| 제안 생성 기준 | 0.25% | 제안 생성에 필요한 최소 vTON 보유량 (전체 발행량 대비) |

해당 설정값은 DAO 투표를 통해 변경할 수 있다.

### 3.6 Voting Period

RFC (7일+) → Snapshot 투표 (5일) → 검토 기간 (3일) → 온체인 투표 (7일) → Timelock (7일) → 실행의 단계를 거친다.

| 단계 | 기간 | 목적 | 활동 |
| --- | --- | --- | --- |
| RFC | 최소 7일 | 커뮤니티 의견 수렴 | 초안 작성, 피드백 반영 |
| Snapshot 투표 | 5일 | 온체인 진행 여부 결정 | 오프체인 찬반 투표 |
| 검토 기간 | 3일 | 스냅샷 준비, 위임 조정 | 제안 확정 |
| 온체인 투표 | 7일 | 최종 실행 승인 | Yes/No/Abstain 투표 |
| Timelock | 7일 | 비상 대응, 보안 검토 | Security Council 검토 |

### **3.7 Quorum**

투표가 유효하려면 전체 위임된 vTON의 최소 정족수가 투표에 참여해야 한다. 쿼럼을 충족하지 못하면 제안은 자동으로 부결된다.

| 파라미터 | 초기값 | 설명 |
| --- | --- | --- |
| Quorum | 4% | 투표에 참여해야 하는 최소 vTON 비율 (전체 위임된 vTON 대비) |

해당 설정값은 DAO 투표를 통해 변경할 수 있다.

### **3.8 Pass Rate**

정족수를 충족한 상태에서 찬성이 가결 기준을 넘으면 제안이 통과된다. 기권은 정족수 계산에는 포함되지만 가결 여부 판정에는 포함되지 않는다.

| 파라미터 | 초기값 | 설명 |
| --- | --- | --- |
| Pass Rate | 과반수 | 정족수 충족 시 제안 통과에 필요한 찬성 비율 |

해당 설정값은 DAO 투표를 통해 변경할 수 있다.

### 3.9 Proposal Lifecycle

제안은 다음 상태를 순차적으로 거친다:

| 상태 | 설명 |
| --- | --- |
| Pending | 투표 시작 대기 중 |
| Active | 투표 진행 중 |
| Succeeded | 가결됨 (찬성 > 반대 + 정족수 충족) |
| Queued | Timelock 대기 중 |
| Executed | 실행 완료 |
| Defeated | 부결됨 (정족수 미달 또는 반대 ≥ 찬성) |
| Canceled | 제안자 또는 Security Council에 의해 취소됨 |
| Expired | Grace Period 내 execute() 미호출 시 발생 |

**상태 전이**

| 흐름 | 전이 | 조건 |
| --- | --- | --- |
| 정상 | Pending → Active → Succeeded → Queued → Executed | - |
| 부결 | Active → Defeated | 정족수 미달 또는 반대 ≥ 찬성 |
| 만료 | Queued → Expired | Grace Period 내 execute() 미호출 |
| 취소 | Pending/Active/Succeeded/Queued → Canceled | 제안자 또는 Security Council |

**기간 설정**

해당 설정값은 DAO 투표를 통해 변경할 수 있다.

| 파라미터 | 초기값 | 설명 |
| --- | --- | --- |
| Voting Delay | 1일 | 제안 생성 후 투표 시작까지 대기 기간 |
| Voting Period | 7일 | 투표 진행 기간 |
| Timelock Delay | 7일 | queue() 호출 후 실행까지 최소 대기 기간 |
| Grace Period | 14일 | Timelock Delay 이후 실행 가능 기간 |

**Timelock Delay**

가결된 제안이 즉시 실행되는 것을 방지한다. 이 기간 동안 커뮤니티는 제안을 최종 검토하고, Security Council은 악의적 제안을 취소할 수 있다. 또한 사용자는 불리한 변경에 대비해 자산을 이동할 시간을 확보한다.

**Grace Period**

실행 가능 기간의 상한선이다. Timelock Delay 종료 후 14일 내에 execute()가 호출되지 않으면 제안은 Expired 상태로 전환된다.

**취소 권한**

| 주체 | 취소 가능 상태 | 비고 |
| --- | --- | --- |
| 제안자 | Pending, Active | 본인 제안만 취소 가능 |
| Security Council | Pending, Active, Succeeded, Queued | 긴급 상황 대응 |

## 4. SECURITY COUNCIL

Security Council은 거버넌스 프로세스를 우회하여 긴급 조치를 취할 수 있다. 해킹이나 치명적 버그 발견 시 7일 이상의 투표 기간을 기다릴 수 없기 때문이다.

### **4.1 구성원 수와 실행 임계값**

주요 L2 프로토콜의 Security Council은 일반적으로 8명 이상으로 구성된다. Arbitrum은 12명(9/12 임계값), Optimism은 13명(10/13 임계값)을 운영하고 있으며, L2Beat는 Stage 1 요건으로 최소 8명 이상, 75% 초과 임계값을 권고한다.

Tokamak Network의 초기 Security Council은 3명으로 구성한다. 재단 1명과 외부 파트너 2명으로 이루어지며, 외부가 과반을 차지하므로 재단이 단독으로 결정할 수 없다. 이는 프로젝트 초기 규모에 적합한 최소 구성이며, 네트워크 성장에 따라 업계 표준 수준으로 점진적으로 확대할 계획이다.

| 구분 | 초기 구성 |
| --- | --- |
| 총 구성원 | 3명 |
| 재단 | 1명 |
| 외부 파트너 | 2명 |
| 실행 임계값 | 2/3 (67%) |

### **4.2 권한**

Security Council은 다음 권한을 갖는다.

| 권한 | 설명 |
| --- | --- |
| 악의적 제안 취소 | Timelock 대기 중인 제안을 거부할 수 있다 |
| 긴급 업그레이드 | 보안 취약점 발견 시 즉시 컨트랙트를 업그레이드할 수 있다 |
| 프로토콜 일시정지 | 긴급 상황 시 프로토콜 기능을 중단할 수 있다 |

이 권한들은 일반 거버넌스 프로세스를 우회하여 즉시 실행된다. 단, 모든 긴급 조치는 사후에 커뮤니티에 공개되어야 한다.

### **4.3 외부 파트너**

초기 외부 파트너는 재단이 지명한다. 이후 DAO가 성장하면 DAO 투표를 통해 선출하는 방식으로 전환한다. 외부 파트너의 자격 요건은 추후 DAO 거버넌스를 통해 정의한다.**
**

### **4.4 임기**

초기 Security Council 구성원은 별도의 임기가 없다. 다만 DAO 거버넌스를 통해 임기를 설정할 수 있다.


### 4.5 해임 절차

Security Council 구성원의 변경(해임 및 선출)은 DAO 투표를 통해 결정된다. 단, Security Council 관련 제안에 대해서는 Security Council이 거부권을 행사할 수 없으며, 재단이 DAO 투표 결과에 따라 집행한다.

## 5. DAO 파라미터

다음은 DAO 투표를 통해 조정할 수 있는 파라미터들이다.

| 카테고리 | 파라미터 | 초기값 | 범위/설명 | 관련 섹션 |
| --- | --- | --- | --- | --- |
| 토큰 발행 | vTON 발행 비율 | 1 | 0 ~ 1 | 2.3 |
| 위임 | 위임 상한 | 20% | 전체 발행량 대비 | 3.4 |
| 위임 | 위임 자동 만료 | 제한 없음 | 일 단위 | 3.4 |
| 투표권 | 위임 기간 요건 | 7일 | 스냅샷 기준 | 3.5 |
| 제안 | 제안 생성 비용 | 100 TON | 소각 | 3.6 |
| 투표 | Quorum | 4% | 전체 위임된 vTON 대비 | 3.8 |
| 투표 | Pass Rate | 과반수 | 찬성/(찬성+반대) | 3.9 |
| Security Council | 구성원 수 | 3명 | - | 4.1 |
| Security Council | 실행 임계값 | 2/3 (67%) | - | 4.1 |
| Security Council | 임기 | 제한 없음 | 일/년 단위 | 4.4 |

## 부록: DAO 거버넌스 공격 사례 분석

본 부록은 블록체인 생태계에서 발생한 주요 DAO 거버넌스 공격 및 문제 사례를 체계적으로 정리한다. 각 사례는 Tokamak Network vTON DAO 설계의 방어 메커니즘 근거로 활용된다.

**사례 총괄표**

| # | 프로토콜 | 연도 | 공격 유형 | 피해 | 핵심 경위 |
| --- | --- | --- | --- | --- | --- |
| 1 | Beanstalk | 2022 | Flash Loan | $182M | $1B 대출로 67% 확보, 단일 블록 내 제안-투표-실행-탈취 |
| 2 | Aragon | 2023 | Treasury 탈취 | $155M | 시총 < Treasury 차익 노림. 45일간 47% 축적 후 청산 강제 |
| 3 | Radiant | 2024 | 다중서명 탈취 | $50M | 11명 중 3명 서명 필요. 악성 PDF로 정확히 3명 장악 |
| 4 | Compound | 2024 | 투표권 집중 | $24M | 단일 주체가 쿼럼의 81%(325K COMP) 축적, 자기 볼트에 자금 할당 제안 통과 |
| 5 | Balancer | 2022 | 배출 조작 | $1.8M | veBAL 35% 확보 후 저볼륨 풀로 과도한 토큰 배출 유도 |
| 6 | Build Finance | 2022 | 적대적 탈취 | $470K | 알림 시스템 무력화 후 제안 제출, 0표 반대로 통과 |
| 7 | Uniswap | 2020-24 | 위임 집중 | - | 4년간 지니계수 0.881→0.943, 참여자 88% 감소 |
| 8 | Optimism | 2024 | 이해충돌 | - | Delegate가 자신의 컨설팅 고객 지지, 관계 미공개 |
| 9 | Arbitrum | 2024-25 | 인센티브 실패 | - | 소급 규칙 변경으로 활성 delegate 49명→21명 |
| 10 | Aave | 2024 | 타이밍 조작 | - | 크리스마스 연휴에 브랜드 소유권 제안 강행 |

**1. Beanstalk Flash Loan 공격 (2022)**

2022년 4월 17일, Beanstalk에서 역대 가장 정교한 거버넌스 공격이 발생했다. 공격자는 악의적 제안 2개(BIP-18, BIP-19)를 제출하고 24시간 긴급 제안 기간을 기다렸다. 그리고 단일 트랜잭션 안에서 모든 것을 실행했다. Aave, Uniswap, SushiSwap에서 $1B 이상을 Flash Loan으로 차입한 뒤, 토큰을 Beanstalk "Silo"에 예치하여 거버넌스 토큰을 생성했다. 이로써 67% 투표권을 확보하여 긴급 실행에 필요한 초다수 요건을 충족했다. 악의적 제안을 통과시키고 즉시 실행하여 $182M을 탈취한 뒤 Flash Loan을 상환했다. 전 과정이 단일 블록 안에서 완료되었다. 핵심 취약점은 `emergencyCommit` 함수가 투표와 실행을 동일 블록에서 허용했다는 점이다. 또한 투표권 계산에 스냅샷이 적용되지 않아 방금 획득한 토큰으로도 즉시 투표할 수 있었다.

**교훈**: 투표권은 제안 생성 시점의 스냅샷 기준으로 계산해야 한다. 투표와 실행은 반드시 분리되어야 하며, 신규 토큰에 대한 투표권 유예 기간이 필요하다.

**2. Aragon "RFV Raiders" 공격 (2023)**

Aragon은 구조적 취약점을 안고 있었다. 시가총액은 약 $129M이었지만 Treasury에는 $177-200M이 쌓여 있었다. 토큰을 전량 매입한 뒤 Treasury를 청산하면 차익이 남는 구조였다. "RFV Raiders"라 불리는 공격자 그룹이 이를 간파했다. 약 45일간 Discord에 침투하여 커뮤니티 동향을 파악하면서 ANT 토큰을 시장에서 조용히 매집했다. 토큰 래핑을 통해 47% 이상의 투표권을 확보한 뒤 Treasury 전액 청산 제안을 준비했다. 결국 Aragon Association은 프로젝트 해산을 결정했고, 0.0025376 ETH/ANT 비율로 총 $155M을 상환했다. 사실상 공격자의 목표가 달성된 셈이다.

**교훈**: Treasury 규모가 시총을 초과하면 "합법적 약탈"의 표적이 된다. Treasury 인출 상한, 차등 쿼럼, 장기 축적 모니터링이 필수적이다.

**3. Radiant Capital 키 탈취 (2024)**

2024년 10월, Radiant Capital에서 $50M이 탈취되었다. 이 사건은 다중서명 설계의 근본적인 함정을 보여준다. Radiant는 11명의 서명자를 두었지만, 실행에 필요한 서명은 3개뿐이었다(3/11 = 27%). 공격자는 악성코드가 포함된 PDF 파일을 배포하여 정확히 3명의 서명자를 장악했다. 그것으로 충분했다. 다중서명 지갑의 통제권을 획득하여 $50M을 탈취했다. 11명이라는 숫자는 의미가 없었다. 3명만 뚫리면 끝이었기 때문이다. L2Beat는 이 사건 이후 Security Council의 최소 요건으로 "8명 이상의 서명자, 75% 이상의 임계값"을 권고하고 있다.

**교훈**: 다중서명의 보안은 서명자 수보다 임계값이 중요하다. 임계값은 최소 70-75% 이상이어야 의미 있는 보안을 제공한다. 3명만 장악하면 뚫리는 구조는 11명이 있어도 무의미하다.

**4. Compound "Golden Boys" 공격 (2024)**

2024년 7월, "Humpy"로 알려진 공격자가 Bybit 거래소에서 조직적으로 COMP 토큰을 인출하기 시작했다. 최종적으로 축적한 물량은 325,333 COMP로, Compound의 쿼럼 요건 400,000 COMP의 81%에 해당했다. Humpy는 두 차례 실패한 제안 끝에 Proposal 289를 제출했다. 제안 내용은 $24M 상당의 COMP를 자신이 통제하는 "goldCOMP" 볼트에 할당하는 것이었다. 주말 타이밍을 노려 delegate들의 대응이 어려운 시점에 투표를 진행했고, 최종 결과는 682,191 찬성 대 633,636 반대(51.84%)로 통과되었다. 커뮤니티의 긴급 조율로 Humpy와 협상이 이루어졌고, 자금 할당은 실행되었으나 향후 거버넌스 개선 논의가 촉발되었다.

**교훈**: 쿼럼은 "최소 참여 요건"일 뿐, 대량 보유자의 영향력을 제한하지 못한다. 단일 주체의 투표권 상한과 주말/휴일 블랙아웃 기간이 필요하다.

**5. Balancer veBAL 집중 공격 (2022)**

Compound 공격과 동일한 공격자 Humpy가 Balancer에서도 활동했다. 그는 전체 veBAL의 35%를 축적한 뒤 Gauge 투표를 조작했다. 자신이 통제하는 저볼륨 CREAM/WETH 풀로 BAL 토큰 배출을 유도한 것이다. 결과는 극단적이었다. 해당 풀은 6주간 $17,846의 프로토콜 수익만 발생시켰지만, 동일 기간 $1.8M의 BAL 배출을 받았다. 수익 대비 배출 비율이 약 100:1에 달했다. Balancer DAO는 이후 Gauge Framework V1을 도입하여 단일 풀 최대 배출 상한을 10-15%로 설정했고, Humpy와 "평화 협정"을 체결했다.

**교훈**: 시뇨리지나 토큰 배출 기반 시스템에서는 배출 상한과 프로토콜 수익 연계 메커니즘이 필수적이다. veToken 집중 자체를 제한하는 장치도 고려해야 한다.

**6. Build Finance DAO 적대적 탈취 (2022)**

Build Finance 공격은 단순하면서도 치명적이었다. 공격자(ENS: Suho.eth)는 먼저 제안 알림 봇과 gitbook 문서를 비활성화했다. 커뮤니티가 새 제안을 인지할 수 없는 상황을 만든 것이다. 그 상태에서 거버넌스 탈취 제안을 제출했다. 아무도 제안의 존재를 몰랐기 때문에 반대표는 0표였고, 제안은 그대로 통과되었다. 전체 Treasury 약 $470,000가 탈취되었다. 공격자는 "규칙대로 행동했을 뿐"이라고 주장했고, 프로토콜은 사실상 종료되었다. Code is Law의 한계가 적나라하게 드러난 사례다.

**교훈**: Timelock, 최소 투표 참여 요건, 다중 알림 시스템은 선택이 아닌 필수다. 단일 실패점을 제거해야 한다.

**7. Uniswap 위임 집중화 (2020-2024)**

학술 연구에서 21,791명의 Uniswap 투표자와 68개 거버넌스 제안을 4년간 분석한 결과, 위임 제도의 의도치 않은 부작용이 드러났다. 위임 도입 전 투표권 분포의 지니계수는 0.881이었다. 4년 후 이 수치는 0.943으로 상승했다. 불평등이 6.6% 증가한 것이다. 제안당 평균 참여자 수는 503명에서 267명으로 88% 감소했다. 상위 1%가 전체 투표권의 47.5%를 장악했고, 기술 관련 제안에서는 집중도가 99.97%에 달해 사실상 독점 상태였다. "누군가 대신 해줄 것"이라는 심리적 효과가 작용한 것으로 분석된다. 위임 상한이 없었고, 비활성 delegate에 대한 조치도 없었으며, 대형 delegate로의 쏠림 현상이 심화되었다.

**교훈**: 위임은 참여율을 높이려는 의도와 달리 오히려 불평등과 무관심을 심화시킬 수 있다. 위임 상한, 활동 요건, 자동 만료 등의 보완책이 필요하다.

**8. Optimism Griff Green 이해충돌 (2024)**

Griff Green은 Optimism의 주요 Delegate였다. 동시에 Giveth 창립자이자 General Magic 공동창립자이기도 했다. 문제는 그랜트 심사 과정에서 드러났다. Green은 자신의 컨설팅 고객인 프로젝트들을 지지했다. 해당 컨설팅은 그랜트 금액의 7-50% 수수료를 수취하는 구조였다. 그러나 Green은 이 이해충돌 관계를 투표 전에 공개하지 않았다. 커뮤니티 논쟁 후 "marginal vote가 아니었으므로 실질적 피해 없음"이라는 판정이 내려졌다. 그러나 이 사건을 계기로 Optimism은 필수 이해충돌 공시 규정을 도입했고, Badgeholder Conflict of Interest Disclosure 제도를 시행하게 되었다.

**교훈**: Delegate의 이해충돌 공시는 선택이 아닌 의무여야 한다. 사전 공시 없는 투표는 무효 처리하는 등 강제 메커니즘이 필요하다.

**9. Arbitrum Delegate Incentive Program 실패 (2024-2025)**

Arbitrum DAO는 delegate 참여를 독려하기 위해 연간 $1.5M 규모의 인센티브 프로그램을 도입했다. 초기에는 활성 delegate가 증가하는 효과가 있었다. 문제는 버전 1.6/1.7 업데이트에서 발생했다. 소급 규칙 변경이 단행된 것이다. 진입 장벽이 10배 상향되었고(50K → 500K ARB), delegate 보상은 약 40% 삭감되었다. 반면 프로그램 관리자 보상은 25% 증가했다. 대규모 비활성 delegate는 방치되었고, 소규모 delegate에게 불리한 규칙이 적용되었다. 결과는 참담했다. 2024년 12월 49명이었던 활성 delegate 수는 2025년 2월 21명으로 57% 감소했다. 커뮤니티에서는 "후원 시스템"이라는 비판이 제기되었고, v1.5로 복귀하자는 제안이 논의 중이다.

**교훈**: Delegate 인센티브는 명확하고 예측 가능해야 한다. 소급 규칙 변경은 신뢰를 파괴한다. 진입 장벽과 보상 구조는 균형을 맞춰야 한다.

**10. Aave Labs 크리스마스 투표 논란 (2024)**

2024년 12월, Aave Labs가 "Aave" 브랜드 소유권 이전 제안을 제출했다. 포럼에서 5일만 논의한 뒤 Snapshot 투표로 강행했다. 제안 저자의 동의 없이 투표 단계로 이동한 것이다. 투표 기간은 12월 23일부터 26일까지였다. 크리스마스 연휴와 정확히 겹쳤다. 설상가상으로 창업자 Stani Kulechov가 투표 직전 $10-15M 상당의 AAVE를 매입했다. "적대적 인수 시도"라는 비판이 제기되었다. 결과적으로 제안은 부결되었다. 반대 55.29%, 기권 41.21%, 찬성 3.50%로, 기록적인 180만 AAVE가 투표에 참여했다. 커뮤니티의 반발이 그만큼 컸다는 의미다.

**교훈**: 주요 공휴일 전후 중요 제안을 금지하는 블랙아웃 기간, 저자 동의 요건, 최소 논의 기간 강제가 필요하다. 타이밍 조작은 참여율을 왜곡하고 거버넌스 정당성을 훼손한다.

**참고 문헌**

1. [*DeSpread Research, "The Compound Finance Governance Attack: A Recap and Its Implications" (2024)*](https://research.despread.io/compound-finance-governance-attack/)
1. [*Messari, "Governor Note: The veBAL Wars" (2022)*](https://messari.io/report/governor-note-the-vebal-wars)
1. [*Blockworks, "Arca Offers Their 2 Cents on Aragon DAO Attack Allegations" (2023)*](https://blockworks.co/news/arca-aragon-dao-attack-allegations)
1. [*The Block, "Build Finance DAO suffers 'hostile governance takeover'" (2022)*](https://www.theblock.co/post/134180/build-finance-dao-suffers-hostile-governance-takeover-loses-470000)
1. [*PANews, "A Study of Uniswap On-Chain Voting: Implications for Power, Apathy, and Evolution" (2024)*](https://www.panewslab.com/en/articles/7c66f3fa-b71d-4fa0-898d-243cf083e8a8)
1. [*DL News, "Griff Green's disclosure 'mistake' sparks heated debate among Optimism DAO" (2024)*](https://www.dlnews.com/articles/defi/green-offers-mea-culpa-to-optimism-dao-over-grants-disclosure/)
1. [*The Defiant, "Arbitrum DAO Votes on $1.5 Million Program to Reward Active Delegates" (2024)*](https://thedefiant.io/news/blockchains/arbitrum-dao-votes-on-usd1-5-million-program-to-reward-active-delegates)
1. [*Arbitrum Proposals, "Revert the Delegate Incentive Program (DIP) to Version 1.5" (2025)*](https://forum.arbitrum.foundation/t/proposal-revert-the-delegate-incentive-program-dip-to-version-1-5/29867)
1. [*DL News, "Aave Labs critics lose key DAO vote — for now" (2024)*](https://www.dlnews.com/articles/defi/aave-labs-critics-lose-key-dao-vote-for-now/)
1. [*Arbitrum Foundation, "Security Council: A conceptual overview" (2024)*](https://docs.arbitrum.foundation/concepts/security-council)
1. [*ENS Docs, "ENS DAO Security Council" (2024)*](https://docs.ens.domains/dao/security-council/)