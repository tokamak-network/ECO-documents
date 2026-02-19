Tokamak Network의 vTON 거버넌스 토큰 설계를 위한 8개 프로젝트의 거버넌스 구조를 비교 분석한 결과, **MakerDAO와 Lido가 가장 혁신적인 거버넌스 모델**을 운영하고 있으며, 지속적 토큰 발행 모델은 Uniswap, Optimism, ENS가 연 2% 인플레이션 메커니즘을 채택하고 있다. 특히 MakerDAO의 SubDAO 토큰 파밍과 Lido의 Dual Governance는 vTON 설계에 직접적인 참고가 될 수 있는 **지속 발행과 거버넌스 참여를 연계**하는 모델을 제시한다.

## **1. 토큰 설계 비교**

8개 프로젝트 모두 **1 토큰 = 1 투표**의 단순 가중치 방식을 기본으로 채택했으나, 토큰 발행 메커니즘과 인플레이션 정책에서 상당한 차이가 존재한다.

| **프로젝트** | **총 공급량** | **발행 방식** | **전송 가능** | **인플레이션** | **veToken** |
| --- | --- | --- | --- | --- | --- |
| **Arbitrum** | 100억 ARB | 에어드랍 (11.62%) | ✅ | 연 최대 2% (DAO 승인) | ❌ |
| **Optimism** | ~43억 OP | 에어드랍 (19%) | ✅ | 기본 연 2% | ❌ |
| **Uniswap** | 10억 UNI | 에어드랍 + 유동성 마이닝 | ✅ | 연 2% 영구 (2024년~) | ❌ |
| **Aave** | 1,600만 AAVE | 토큰 마이그레이션 | ✅ | 없음 (고정) | ❌ |
| **MakerDAO** | ~97.7만 MKR → 234억 SKY | 프로토콜 운영 | ✅ | 있음 (SubDAO용) | ⚠️ 유사 |
| **Lido** | 10억 LDO | 사전 채굴 | ✅ | 없음 (고정) | ❌ |
| **Compound** | 1,000만 COMP | 유동성 마이닝 | ✅ | 없음 (고정) | ❌ |
| **ENS** | 1억 ENS | 에어드랍 (25%) | ✅ | 연 최대 2% 가능 | ❌ |

**지속적 토큰 발행 모델 상세:**

**Uniswap**은 4년 초기 배포 완료 후 **2024년 9월부터 연 2% 영구 인플레이션**이 시작되었으며, 신규 발행 토큰은 거버넌스 트레저리로 배분된다. [Exponential DeFi](https://exponential.fi/assets/uniswap-ethereum/47e10d3a-7a65-4b89-b582-8eff4237f708) 2025년 12월 제안된 UNIfication에서는 프로토콜 수수료 활성화 시 **토큰 소각 메커니즘** 도입이 논의 중 [Uniswapfoundation](https://vote.uniswapfoundation.org/proposals/93)이어서, 인플레이션과 디플레이션의 균형 모델로 진화하고 있다.

**MakerDAO**는 Endgame 구조조정으로 **SKY 토큰** (1 MKR = 24,000 SKY)을 도입하며, [BlockApps Inc.](https://blockapps.net/blog/understanding-the-makerdao-governance-process-for-stablecoins-insights-and-mechanisms/)[The Block](https://www.theblock.co/post/313235/makerdao-mkr-sky-dai-stablecoin-usds) **연간 6억 SKY**가 [The Block](https://www.theblock.co/post/313235/makerdao-mkr-sky-dai-stablecoin-usds) SubDAO 인큐베이션, AVC 자금, 워크포스 인센티브로 지속 발행된다. 특히 **Sagittarius Lockstake Engine**은 SKY를 락업하고 거버넌스에 참여하면 USDS/SubDAO 토큰 파밍 리워드를 획득하는 구조로, [Reflexivityresearch](https://www.reflexivityresearch.com/free-reports/makerdao-overview) vTON의 시뇨리지 기반 모델과 가장 유사한 형태다.

**Optimism**과 **Arbitrum**은 둘 다 연 최대 2% 인플레이션 권한을 DAO에 부여했지만, 실제 발행에는 거버넌스 승인이 필요하다. Optimism의 경우 **인플레이션율 변경은 Token House 제안 + Citizens' House 거부권**의 양원제 견제를 받는다. [Lemma](https://www.lemma.solutions/insights/the-governance-of-optimism)

**주요 인사이트:** 8개 프로젝트 중 **veToken 모델을 완전히 채택한 곳은 없다**. MakerDAO의 Sagittarius Engine이 유일하게 락업 기반 보상을 제공하지만, 투표권 가중치 부여보다는 추가 수익 파밍에 초점을 맞춘다. [Phemex](https://phemex.com/blogs/what-is-vetokenomics-an-analysis-on-the-vetoken-model) 이는 DeFi 거버넌스에서 유동성 유지의 중요성을 보여준다. **지속 발행 모델**을 채택한 프로젝트들(Uniswap, Optimism, MakerDAO)은 공통적으로 **신규 발행 토큰이 트레저리 또는 커뮤니티 프로그램으로 유입**되어, 기존 보유자의 거버넌스 권한 희석과 신규 참여자의 진입 사이 균형을 추구한다.

---

## **2. 투표 메커니즘 비교**

투표 방식은 **On-chain과 Off-chain(Snapshot)의 혼합 모델**이 표준으로 자리잡았으며, 정족수와 통과 기준에서 프로젝트별 철학 차이가 드러난다.

| **프로젝트** | **투표 방식** | **위임** | **정족수** | **통과 조건** | **투표 기간** |
| --- | --- | --- | --- | --- | --- |
| **Arbitrum** | 혼합 (Snapshot + Tally) | ✅ | 4.5% (Constitutional) / 3% (Treasury) | 단순 과반 | 14-16일 |
| **Optimism** | On-chain (Agora) + Snapshot | ✅ 부분위임 가능 | 30% | 51-76% (유형별) | 7일 |
| **Uniswap** | 혼합 (Snapshot + Governor Bravo) | ✅ | 4% (40M UNI) | 단순 과반 | 7일 (On-chain) |
| **Aave** | 혼합 (Snapshot + On-chain) | ✅ 제안권/투표권 분리 | 2-6.5% | 과반 + Vote Differential | 3-10일 |
| **MakerDAO** | On-chain (Continuous Approval) | ✅ Aligned Delegates | 없음 (상대적 다수) | 이전 제안 초과 | 지속적 (30일 만료) |
| **Lido** | 혼합 (Snapshot + Aragon) | ✅ | 5% | 단순 과반 | 7일 (Snapshot) / 72시간 (On-chain) |
| **Compound** | On-chain (Governor Bravo) | ✅ | 4% (400K COMP) | 단순 과반 | 3일 |
| **ENS** | 혼합 (Snapshot + Tally) | ✅ 필수 (Multi-Delegate 지원) | 1% | 50% / 66.7% (헌법) | 5-7일 |

**위임 시스템의 혁신:**

**Aave**는 **제안권(Proposition Power)과 투표권(Voting Power)을 별도로 위임**할 수 있어, 전문성에 따른 역할 분담이 가능하다. [Aave](https://docs.aave.com/developers/v/2.0/protocol-governance/governance) **Optimism**의 GovernorV6는 **부분 위임(Partial Delegation)**을 지원해 여러 대리인에게 투표권을 나눠 위임할 수 있다. **ENS**는 **Multi-Delegate Manager**로 이를 더욱 발전시켜 분할 위임을 공식화했으며, [ENS](https://ens.domains/blog/post/multi-delegate-manager) 투표 전 위임이 필수다. [Ens](https://docs.ens.domains/dao/governance/process/)

**MakerDAO의 Continuous Approval Voting**은 독특한 방식으로, 새 제안이 현재 상태(마지막 통과된 제안)보다 더 많은 투표를 받아야만 통과된다. 투표는 시스템에 지속적으로 남아 있어 **거버넌스 공격 방어**에 효과적이다. [Makerdao](https://community-development.makerdao.com/en/learn/governance/how-voting-works/)

**주요 인사이트:** 정족수 기준은 **ENS 1%부터 Optimism 30%까지** 30배 차이가 난다. [Medium](https://dexenetwork.medium.com/how-do-top-10-daos-manage-treasury-and-governance-4abbac6a5d83) 낮은 정족수(Arbitrum 3-4.5%, ENS 1%)는 의사결정 효율성을 높이지만, 소수 대형 홀더의 영향력이 커진다. Optimism의 30% 높은 정족수는 더 강한 정당성을 확보하지만 투표 불성립 위험이 있다. [GitHub](https://github.com/ethereum-optimism/OPerating-manual/blob/main/manual.md) **헌법적 변경에 대한 상향된 통과 기준**(ENS 66.7%, Optimism 76%)은 핵심 원칙 보호를 위한 장치로 참고할 만하다.

---

## **3. 제안 프로세스 비교**

제안 생성의 진입장벽과 실행까지의 소요 시간에서 프로젝트별 탈중앙화 수준과 보안-효율 트레이드오프가 드러난다.

| **프로젝트** | **제안 자격 (최소 토큰)** | **제안 유형** | **Timelock** | **총 소요 시간** |
| --- | --- | --- | --- | --- |
| **Arbitrum** | 100만 ARB (0.01%) | Constitutional / Non-Constitutional | 3-8일 | 27-37일 |
| **Optimism** | 0.1% OP | Protocol / Fund / Inflation / Director | 1주 (거부권 기간) | 3-4주 |
| **Uniswap** | 250만 UNI (0.25%) | 공식 분류 없음 | 2-30일 | 16일+ |
| **Aave** | 0.5-1.25% (~8-20만 AAVE) | Short Executor / Long Executor | 1-7일 | 8-20일 |
| **MakerDAO** | 명시적 threshold 없음 | 5개 Scope 기반 | 16-30시간 (GSM) | 1-2주 |
| **Lido** | 없음 (Easy Track은 승인된 주소만) | 일반 / Easy Track / 긴급 | 3-45일 (Dual Gov) | 2-7주+ |
| **Compound** | 2.5만 COMP (0.25%) | 공식 분류 없음 | 2일 | 7일 |
| **ENS** | 10만 ENS (0.1%) | Executable / Social / Constitutional | 2일 | 2-3주 |

**제안 유형 분류의 다양성:**

**Arbitrum**은 **Constitutional AIP**(헌법 수정, 소프트웨어 업데이트)와 **Non-Constitutional AIP**(트레저리 지출)로 구분하며, 각각 다른 정족수와 타임락을 적용한다. [Arbitrum](https://docs.arbitrum.foundation/concepts/dao-vote)[Arbitrum](https://docs.arbitrum.foundation/dao-constitution) **Optimism**은 **Protocol Upgrade, Governance Fund, Inflation Adjustment, Director Removal** 등으로 세분화하고, 유형별로 51-76%의 차등화된 통과 기준을 적용한다.

**Aave**는 **Short Executor**(일반 파라미터 변경, 1일 타임락)와 **Long Executor**(거버넌스 핵심 변경, 7일 타임락)로 구분해 **리스크에 비례한 심의 시간**을 확보한다. [Aave](https://aave.com/help/governance/proposals) **MakerDAO**는 Endgame으로 **Governance, Support, Protocol, Stability, Accessibility** 5개 Scope 기반 분류 체계를 도입했다.

- *Compound CAP (Autonomous Proposal)**은 혁신적 접근으로, 단 **100 COMP만 잠금**하면 제안을 생성할 수 있고, 25,000 COMP 위임을 받으면 정식 제안으로 전환된다. 이는 진입장벽을 크게 낮추면서도 커뮤니티 지지를 확인하는 메커니즘이다.

**주요 인사이트:** 제안 자격 요건은 **MakerDAO의 0%부터 Aave의 1.25%까지** 큰 차이가 있다. Compound의 CAP 방식은 저렴한 비용으로 제안을 시작하되 커뮤니티 위임으로 정당성을 확보하는 **점진적 진입 모델**로, vTON에서 신규 발행 토큰 보유자의 거버넌스 참여를 촉진하는 데 참고할 수 있다. **Timelock 기간**은 보안과 민첩성의 트레이드오프로, Compound의 2일 최소 기간부터 Lido Dual Governance의 45일 최대 기간까지 다양하다.

---

## **4. 거버넌스 범위 비교**

DAO가 통제하는 영역과 제외되는 영역을 명확히 구분함으로써 거버넌스의 경계가 정의된다.

| **프로젝트** | **주요 투표 대상** | **투표 제외 대상** | **Treasury 규모** |
| --- | --- | --- | --- |
| **Arbitrum** | 프로토콜 업그레이드, Treasury, 헌법 수정, Security Council 선출 | 법적 제재 위반, Orbit 체인 자체 거버넌스 | ~35억 ARB + 14,223 ETH |
| **Optimism** | 프로토콜 업그레이드, Governance Fund, 인플레이션 조정, RetroPGF | Foundation 운영 일부, 법적 준수 | 초기 25% + 시퀀서 수익 |
| **Uniswap** | 수수료 스위치, 풀 설정, 컨트랙트 업그레이드, 토큰 리스트 | 팀 개발 결정, 감사/보안 | ~~4.3억 UNI (~~$2.3B) |
| **Aave** | 리스크 파라미터, 자산 온보딩, GHO 파라미터, 체인 배포 | 일상 리스크 조정 (Steward), 긴급 보안 (Guardian) | ~$260-280M |
| **MakerDAO** | 담보 관리, DSR, Stability Fees, Debt Ceiling, SubDAO | Oracle 직접 조작, 개별 Vault, Atlas 불변 원칙 | DAI TVL ~$45억 + RWA $12.5억+ |
| **Lido** | 수수료 설정, 노드 오퍼레이터, 오라클, 컨트랙트 업그레이드 | Easy Track 루틴 운영 (반대 없을 시) | 프로토콜 수수료 (10% 중 5%) |
| **Compound** | 이자율 모델, 담보 비율, 시장 추가/제거, COMP 분배율 | 긴급 일시정지 (Pause Guardian) | ~$172M |
| **ENS** | 프로토콜 파라미터, 워킹그룹 예산, Endowment, 등록 수수료 | 이름 소유권 침해, 차별적 수수료, 새 TLD 생성 | .eth 수수료 + Endowment 16,000 ETH |

**Treasury 관리 방식의 다양성:**

**Aave**와 **ENS**는 **Karpatkey**를 외부 자산 관리자로 선임해 전문적인 트레저리 운용을 한다. ENS는 2023년 **Endowment(기부금)** 개념을 도입해 16,000 ETH를 DeFi 수익 창출에 투입, 장기 지속가능성을 확보한다. [ENS Endowment](https://basics.ensdao.org/endowment)[Medium](https://medium.com/@SHIFT_DeFi/dao-treasuries-are-billions-really-billions-9c21f49a46a0)

**MakerDAO**는 **RWA(Real World Assets) 투자**의 선구자로, 미국 국채 등에 $12.5억 이상을 투자해 프로토콜 수익을 다각화했다. Arbitrum은 **STEP(Stable Treasury Endowment Program)**으로 토큰화된 미국 국채에 35M ARB를 투자한다.

**Optimism**의 **RetroPGF(소급적 공공재 펀딩)**는 독특한 재분배 메커니즘으로, 시퀀서 수익이 기본적으로 공공재 펀딩에 배분되며, Token House가 이 배분 비율을 변경할 수 있다. [Optimism](https://www.optimism.io/blog/the-future-of-optimism-governance)

**주요 인사이트:** **헌법 또는 불변 원칙**을 명시한 프로젝트(ENS Constitution, MakerDAO Atlas)는 DAO가 절대 변경하면 안 되는 핵심 가치를 보호한다. ENS는 "이름 소유권 침해 금지", "차별적 수수료 금지" 등을 명문화했다. [Ens](https://docs.ens.domains/dao/constitution/) 이러한 **거버넌스 경계 설정**은 vTON 설계 시 무엇을 DAO 권한으로 하고 무엇을 불변으로 할지 결정하는 데 중요한 참고가 된다.

---

## **5. 견제 메커니즘 비교**

모든 프로젝트가 거버넌스 공격과 악의적 제안에 대비한 안전장치를 갖추고 있으나, 그 구현 방식에서 철학적 차이가 있다.

| **프로젝트** | **Security Council/Guardian** | **구성** | **거부권** | **긴급 조치** |
| --- | --- | --- | --- | --- |
| **Arbitrum** | Security Council | 12명 멀티시그 (2코호트, 반기 선거) | 제안 취소 가능 | 9/12로 즉시 업그레이드 |
| **Optimism** | Security Council (2024년~) | 커뮤니티 선출 | Citizens' House 거부권 (30%) | Maintenance Upgrade |
| **Uniswap** | Guardian (제한적) + Foundation | Uniswap Foundation | 제안 취소 (임계값 미달 시) | 공식 프로세스 없음 |
| **Aave** | Protocol Emergency + Governance Guardian | 5/9 멀티시그 × 2 | 악성 코드 제안 취소 | Freeze/Pause 즉시 실행 |
| **MakerDAO** | GSM + ESM + Constitutional Conservers | GSM: 16-30시간 지연, ESM: MKR 예치 | GSM 기간 내 새 투표로 취소 | Out-of-schedule Executive |
| **Lido** | Dual Governance + Tiebreaker Committee | stETH 홀더 + 3개 서브위원회 | stETH 1-10% 에스크로 시 | GateSeal (11일 중지) |
| **Compound** | Pause Guardian + Community Multi-Sig | 멀티시그 | 모든 제안 취소 가능 | 특정 기능 일시정지 |
| **ENS** | Security Council | 4/8 Safe 멀티시그 (2년 후 자동 소멸) | 악의적 제안 취소 전용 | 제한된 권한 |

**혁신적 견제 메커니즘:**

**Lido의 Dual Governance**는 2025년 6월 통과된 세계 최초의 **동적 타임락 거버넌스**다. stETH 홀더가 LDO 거버넌스 결정에 거부권을 행사할 수 있다: [Ainvest](https://www.ainvest.com/news/lido-finance-proposes-dual-governance-giving-steth-holders-veto-power-2505/)[The Block](https://www.theblock.co/post/360212/lido-dao-votes-to-enable-dual-governance-giving-stakers-veto-power)

- **1% stETH 에스크로**: 타임락 5-45일로 연장 (Veto Signaling) [Lido](https://lido.fi/governance)[The Block](https://www.theblock.co/post/360212/lido-dao-votes-to-enable-dual-governance-giving-stakers-veto-power)
- **10% stETH 에스크로**: **Rage Quit** 발동 - 반대 스테이커 전원 출금 완료까지 모든 거버넌스 중단 [Lido](https://lido.fi/governance)[The Block](https://www.theblock.co/post/360212/lido-dao-votes-to-enable-dual-governance-giving-stakers-veto-power)

**Optimism의 양원제 견제**는 Token House와 Citizens' House가 상호 거부권을 보유한다. [Lemma](https://www.lemma.solutions/insights/the-governance-of-optimism) Token House의 프로토콜 업그레이드나 인플레이션 조정 제안에 대해 Citizens' House가 30% 거부권을 행사할 수 있다. [GitHub](https://github.com/ethereum-optimism/OPerating-manual/blob/main/manual.md)[Lemma](https://lemma.solutions/the-governance-of-optimism/)

**ENS Security Council**의 독특한 점은 **2년 시한부 설계**다. `renounceTimelockRoleByExpiration()` 함수로 2년 후 취소 권한이 영구 비활성화되어, 장기적으로 완전한 탈중앙화를 지향한다. [Ensdao](https://basics.ensdao.org/security-council)

- *MakerDAO의 Emergency Shutdown Module(ESM)**은 최후의 수단으로, 충분한 MKR/SKY를 예치하면 전체 시스템을 긴급 중단하고 담보를 동결 가격으로 상환할 수 있다.

**주요 인사이트:** **Lido의 Dual Governance**는 토큰 보유자(LDO)와 프로토콜 사용자(stETH)의 이해관계를 분리하고 사용자에게 거부권을 부여한 혁신적 모델이다. [CoinMarketCap](https://coinmarketcap.com/cmc-ai/lido-dao/what-is/) vTON 설계 시 **시뇨리지로 새로 발행된 토큰 보유자**와 **기존 스테이커/사용자** 간 이해 충돌을 관리하는 데 이 모델이 직접적인 참고가 될 수 있다. 또한 ENS의 시한부 Security Council은 **점진적 탈중앙화 로드맵**을 위한 좋은 예시다.

---

## **6. 거버넌스 구조 비교**

조직 구조와 Foundation의 역할에서 프로젝트의 성숙도와 탈중앙화 철학이 드러난다.

| **프로젝트** | **구조** | **위원회/워킹그룹** | **SubDAO** | **Foundation 관계** |
| --- | --- | --- | --- | --- |
| **Arbitrum** | 단원제 (Dual Governor) | Security Council, Data Availability Committee | 그랜트 프로그램 (STIP, STEP) | Arbitrum Foundation (케이맨) - 예산 승인 |
| **Optimism** | **양원제** (Token + Citizens' House) | Grants Council, Developer Advisory Board, Security Council | RetroPGF 라운드 | Optimism Foundation - 시퀀서 수익 관리 |
| **Uniswap** | 단원제 | 공식 위원회 없음 | 없음 | Uniswap Foundation + DUNA (Wyoming) |
| **Aave** | 단원제 (Dual Executor) | Service Providers (Gauntlet, BGD Labs), Stewards | Grants DAO | Aave Labs - 인터페이스/브랜드 |
| **MakerDAO** | 다층 구조 | AVCs, Scope Advisory Councils, Alignment Conservers | **FacilitatorDAO, AllocatorDAO, MiniDAO** | 완전 탈중앙화 (Foundation 해산) |
| **Lido** | 단원제 + Dual Governance 레이어 | LEGO, Treasury, Growth 등 다수 위원회 | 없음 | Foundation 없음 - DAO 직접 관리 |
| **Compound** | 단원제 | Gauntlet (외부), Growth Program | 없음 | Compound Labs - 개발 담당 |
| **ENS** | 단원제 | 3개 워킹그룹 (Meta-Gov, Ecosystem, Public Goods) | 없음 | ENS Foundation (케이맨) - 법적 실체 |

**양원제와 다층 구조의 실험:**

**Optimism**은 유일한 **완전 양원제** 거버넌스로, Token House(토큰 가중 투표)와 Citizens' House(1인 1투표 Soulbound NFT)가 상호 견제한다. [Mirror](https://optimism.mirror.xyz/PLrAQgE1EGRo7GRrFoztplFChnUZda4DFGW3dkQayxY)[Optimism](https://www.optimism.io/blog/the-future-of-optimism-governance) Token House는 경제적 이해관계자를, Citizens' House는 개인 인간 이해관계자를 대표해 **금권정치(Plutocracy) 위험을 완화**한다. [Optimism](https://www.optimism.io/blog/the-future-of-optimism-governance)[Optimism](https://community.optimism.io/citizens-house/citizen-house-overview)

**MakerDAO**의 Endgame은 가장 복잡한 **다층 구조**를 도입했다:

- **MKR/SKY 보유자**: Maker Core 거버넌스
- **SubDAO 토큰 보유자**: 각 SubDAO 자체 거버넌스
- **FacilitatorDAO** (2개): 거버넌스 관리 [Reflexivityresearch](https://www.reflexivityresearch.com/free-reports/makerdao-overview)
- **AllocatorDAO** (Spark 등): DAI 생성 및 DeFi 배분 [Reflexivityresearch](https://www.reflexivityresearch.com/free-reports/makerdao-overview)
- **MiniDAO**: 소규모 혁신 프로젝트

SubDAO는 자체 토큰을 보유하며 **초기 공급량 26억 토큰** 중 20억이 10년간 yield farming으로 배분된다. [Makerdao](https://endgame.makerdao.com/tokenomics/subdao-tokenomics)

**법적 구조의 혁신:**

**Uniswap DUNA**는 2025년 8월 채택된 Wyoming의 **Decentralized Unincorporated Nonprofit Association**으로, DAO에 법적 실체를 부여해 계약 체결, 세금 준수, 법적 방어가 가능하게 했다. $16.5M UNI가 법적 방어 예산으로 할당됐다.

**주요 인사이트:** **MakerDAO의 SubDAO 구조**는 혁신과 리스크를 분리하는 모듈형 거버넌스의 좋은 예시다. 각 SubDAO가 자체 토큰을 발행하고 독자 거버넌스를 운영하면서 Core DAO와 연결되는 구조는, vTON이 **시뇨리지 기반 지속 발행 모델**에서 신규 토큰의 거버넌스 참여 경로를 설계할 때 참고할 수 있다. Optimism의 양원제는 **비금권적 투표권**(Citizens' House)을 도입해 장기적 이해관계와 단기 경제적 이해의 균형을 추구한다.

---

## **vTON 설계를 위한 종합 시사점**

### **지속적 토큰 발행 모델 참고사항**

vTON의 시뇨리지 비례 지속 발행 구조와 관련하여:

| **모델 유형** | **적용 프로젝트** | **특징** | **vTON 적용 가능성** |
| --- | --- | --- | --- |
| **연 2% 고정 인플레이션** | Uniswap, Optimism | 트레저리로 배분, 수동 보유자 희석 | 인플레이션율 상한 설정 참고 |
| **조건부 인플레이션** | Arbitrum, ENS | DAO 승인 시에만 발행 | 발행 거버넌스 절차 참고 |
| **SubDAO 토큰 파밍** | MakerDAO | 락업 + 거버넌스 참여 = 신규 토큰 보상 | **직접적 참고 모델** |
| **바이백/소각 균형** | Uniswap (제안 중), MakerDAO | 프로토콜 수익으로 토큰 소각 | 인플레이션 상쇄 메커니즘 |

MakerDAO의 Sagittarius Lockstake Engine은 vTON과 가장 유사한 구조로, **SKY 락업 → 거버넌스 참여 → 추가 토큰 파밍**의 선순환을 만든다. 시뇨리지로 지속 발행되는 vTON도 유사하게 **거버넌스 참여를 토큰 획득의 전제 조건**으로 설정할 수 있다.

### **핵심 설계 권장사항**

**토큰 설계**: veToken보다는 **위임 기반 + 락업 보상** 혼합 모델 권장. MakerDAO의 Delayed Upgrade Penalty(마이그레이션 지연 시 분기별 1% 패널티)처럼 **시간에 따른 인센티브 조정** 고려.

**투표 메커니즘**: Aave의 **제안권/투표권 분리 위임** + ENS의 **Multi-Delegate Manager**로 분할 위임 지원. 정족수는 **2-5%** 범위가 효율성과 정당성의 균형점.

**제안 프로세스**: Compound CAP 방식의 **점진적 진입 모델**(소액 잠금으로 시작 → 커뮤니티 위임 시 정식화). 제안 유형별 차등 타임락(Aave Short/Long Executor 참고).

**견제 메커니즘**: Lido Dual Governance의 **동적 타임락 + 사용자 거부권** 모델을 적극 검토. 신규 발행 토큰 보유자와 기존 스테이커 간 이해 충돌 관리에 효과적.

**거버넌스 구조**: 초기에는 단원제로 시작하되, **ENS 스타일 시한부 Security Council**로 점진적 탈중앙화 로드맵 설정. 장기적으로 Optimism 양원제나 MakerDAO SubDAO 구조로 진화 가능성 열어둠.

---

## **결론**

8개 프로젝트 분석 결과, DAO 거버넌스는 **단순한 1 토큰 = 1 투표에서 복잡한 다층 구조로 진화**하고 있다. 지속적 토큰 발행 모델에서 가장 혁신적인 접근은 **MakerDAO의 Sagittarius Engine**으로, 락업과 거버넌스 참여를 신규 토큰 획득과 연계한다. **Lido의 Dual Governance**는 프로토콜 사용자에게 거부권을 부여해 토큰 보유자와 사용자 간 이해관계를 정렬하는 모범 사례다.

vTON 설계 시 핵심은 **시뇨리지 발행 토큰이 자동으로 거버넌스 참여를 유도하는 메커니즘** 구축이다. 단순 보유만으로 투표권을 부여하기보다, MakerDAO처럼 **락업 + 거버넌스 활동 = 추가 보상**의 구조나, Lido처럼 **프로토콜 사용자의 견제권 부여**를 통해 장기적 가치 정렬을 추구하는 것이 바람직하다.