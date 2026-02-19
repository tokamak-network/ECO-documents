[[DAO+TONStakingV2 Audit Report(KR)]]

[[DAO & TON Staking V2 Audit Report(EN)]]

# Scope

### Repo (Branch)

- [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request)
- the latest commit hash:  **01e198130b178757dd194bd8726a1ab678fca167**

### Contract scope  

- DAOCommitteeProxy2.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol)
- DAOCommittee_V1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol) 
- DAOCommitteeOwner.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol)
- SeigManagerV1_3.sol : [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol) 
- DepositManagerV1_1.sol: [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol)
- L1BridgeRegistryV1_1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol)
- Layer2ManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol)
- OperatorManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol)
- CandidateAddOnV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol)

# Hammer

## **감사 기간**

- 2025년 2월 5일 ~ 2025년 3월 13일

## **발견된 이슈**

Audit 과정에서 총 9건의 이슈가 발견되었으며, 심각도에 따라 다음과 같이 분류되었습니다

- **CRITICAL**: 2건 (해결됨)
- **HIGH**: 1건 (해결됨)
- **MEDIUM**: 0건
- **LOW**: 6건 (해결됨)

## **주요 개선 사항**

## **CRITICAL 이슈**

1. **DAO 권한 탈취 취약점 (주요 업그레이드 사항) - Omniscia의 DAO-11M과 겹침**
  - 문제: **`retireMember`** 및 **`changeMember`** 메소드를 악용하여 DAO 위원회의 과반수를 장악할 수 있는 취약점이 발견되었습니다.
  - 개선사항: **`retireMember`** 메소드 호출 시 해당 사용자를 블랙리스트에 추가하여 재가입을 방지하도록 수정하였습니다.
1. **Layer2 TVL 조작 취약점**
  - 문제: 악의적인 컨트랙트를 통해 다른 Layer2의 TVL 값을 도용하여 시뇨리지 분배 시스템을 조작할 수 있는 문제가 있었습니다.
  - 개선사항: Layer2 등록 시 operator와 layer2 주소 간 매핑을 생성하고, TVL 확인 시 해당 매핑을 참조하도록 변경하였습니다.

## **HIGH 이슈**

1. **시뇨리지 분배 오류**
  - 문제: Layer2의 TVL 변동에 따라 **`initialDebt`** 값이 업데이트되지 않아 잘못된 보상이 할당되는 문제가 있었습니다.
  - 개선사항: TVL 변동 시 **`initialDebt`**를 업데이트하는 로직을 추가하여 문제를 해결하였습니다.

## **LOW 이슈**

1. **컨트랙트를 배포하는 과정에 불필요한 검증 코드 제거**
  - 문제: 컨트랙트 배포는 실패할 수 없음에도 불구하고, 배포 이후 컨트랙트의 주소가 **`address(0)`**인지 검증하는 코드들이 포함되어 있음. 이는 불필요한 검증으로 제거해야 함.
  - 개선사항: 불필요한 검증 코드를 제거하여 문제를 해결함.
1. **OperatorManagerV1_1 컨트랙트의 depositByCandidateAddOn / claimByCandidateAddOn 메소드 개선**
  - 문제: **`OperatorManagerV1_1`** 컨트랙트의 **`depositByCandidateAddon`**과 **`claimByCandidateAddon`** 메소드는 필요한 동작에 비해 불필요한 코드가 많아 간소화가 필요함.
  - 개선사항: 코드 간소화 및 최적화를 통해 문제를 해결함.
1. **OperatorManagerV1_1 컨트랙트의 _claim 메소드에서 불필요한 변수 할당 제거**
  - 문제: **`OperatorManagerV1_1`** 컨트랙트의 **`_claim`** 메소드에서 **`address(this)`**를 메모리 변수에 할당하여 사용하고 있음. 이는 불필요한 변수 할당으로 가스 소모를 초래함.
  - 개선사항: 불필요한 코드를 제거하여 가스 효율성을 높였습니다.
1. **SeigManagerV1_3 컨트랙트의 _increaseTot 메소드에서 불필요한 스토리지 변경 코드 제거**
  - 문제: **`_increaseTot`** 메소드에서 **`false`**를 반환하면 트랜잭션이 revert되는데도, 반환 직전에 스토리지를 변경하는 코드가 존재함. 이는 불필요하므로 제거해야 함.
  - 개선사항: 불필요한 코드를 제거하여 가스 효율성을 높였습니다.
1. **Layer2ManagerV1_1 컨트랙트의 _availableRegister 메소드에서 불필요한 코드 제거**
  - 문제: **`_availableRegister`** 메소드는 전달된 **`rollupConfig`**의 유효성을 검증하는 데 사용되지만, Bridge 및 Optimism Portal 잔고 확인 등 필요 없는 기능을 포함하고 있음.
  - 개선사항: **`rollupConfig`** 타입 확인만으로 유효성을 검증할 수 있으므로, 불필요한 코드를 제거하여 가스 효율성을 높였습니다.
1. **SeigManagerV1_3 컨트랙트의 _increaseTot 메소드에서 Layer2 시뇨리지를 분배하는 코드 최적화**
  - 문제: Layer2 시뇨리지를 분배하는 코드가 여러 위치에 분산되어 있으며, 연산 및 변수 할당이 비효율적으로 이루어지고 있음. 최적화가 필요함.
  - 개선사항: 최적화된 코드를 Pull Request로 제출하여 문제를 해결함. (지나님께 요청)

# Carl

## **감사 기간**

- 2025년 2월 3일 ~ 2025년 3월 5일

## **발견된 이슈**

Audit 과정에서 총 21건의 이슈가 발견되었으며, 심각도에 따라 다음과 같이 분류되었습니다.

## **주요 감사 결과 및 개선 사항**

## **A. Critical (치명적)**

1. **Storage Layout Conflict (TS-1) (주요 사항) - CertiK의 CON-02와 같이**
  - **문제**: 기존 DAOCommitteeProxy 컨트랙트와 신규 DAOCommitteeProxy2 컨트랙트 간의 저장소 레이아웃 충돌 발생.
  - **개선사항**: 저장소 레이아웃을 재구성하여 충돌을 방지함.
1. **Centralized Execution of Agenda (TS-2) (주요 사항) - CertiK의 CON-01과 같이**
  - **문제**: DEFAULT_ADMIN_ROLE 계정이 투표 결과와 무관하게 아젠다 상태를 변경할 수 있는 권한 보유.
  - **개선사항**: DEFAULT_ADMIN_ROLE을 개인계정에서 멀티시그 월렛으로 변경하고, setAgendaStatus 함수의 사용을 제한함.

## **B. Medium (중간)**

1. **Duplicate Proxy Pausing Mechanism (TS-3)**
  - **문제**: DAOCommitteeProxy2에서 불필요한 프록시 정지 기능 중복 구현.
  - **개선사항**: 중복된 pauseProxy 상태 변수를 제거하고 기존 변수와 통합.
1. **Multiple Init Possible (TS-4)**
  - **문제**: CandidateAddOnV1_1 컨트랙트에서 initialize 함수가 여러 번 호출 가능.
  - **개선사항**: 초기화 상태를 확인하는 로직을 추가하여 함수를 한번만 호출 가능.
1. **Implementation Function Conflict (TS-6)**
  - **문제**: SeigManagerV1_3과 SeigManagerV1_2 간 동일 함수 중복 구현.
  - **개선사항**: 중복된 함수를 하나의 로직 컨트랙트로 통합.
1. **Infinite Length of Array in Memory (TS-22)**
  - **문제**: 메모리에 할당되는 배열 길이가 무한대로 설정되어서 out-of-gas 에러가 발생할 가능성이 있습니다.
  - **개선사항**: 메모리를 사용하는 pauseBlocks 지역 변수 삭제.

## **C. Minor (경미)**

1. **Cannot disable functions once set (TS-8)**
  - 문제: **`setSelectorImplementations2`** 함수는 등록된 함수를 비활성화할 수 있는 옵션이 부족합니다. 컨트랙트 업그레이드 시 기존에 등록된 함수들을 제거하거나 비활성화해야 할 필요가 있을 수 있음에도 불구하고, 이를 위한 효율적인 메커니즘이 제공되지 않아 가스 소비가 증가할 가능성이 있습니다.
  - 개선사항: unsetSelectorImplementations2 함수를 추가하여서 등록된 함수를 비활성화할 수 있는 옵션을 추가하였습니다.

## **D. Informational (정보성)**

다수의 정보성 이슈가 발견되었으며, 주요 내용은 다음과 같습니다:

1. **Multiple SLOAD (getSelectorImplementation2) (TS-7)**
  - 문제: 동일한 상태 변수를 여러 번 읽어 불필요한 가스 소비 발생
  - 개선사항: 상태 변수를 로컬 변수에 저장하여 가스 소비를 줄임
1. **No event emitted (TS-10)**
  - 문제: 주요 상태 변수 변경 시 이벤트가 발생하지 않음
  - 개선사항: 이벤트를 정의하고 발생시켜 상태 변경을 추적 가능하게 개선
1. **Unnecessary public function (TS-11)**
  - 문제: 내부에서 사용되지 않는 함수가 **`public`**으로 선언됨
  - 개선사항: **`external`**로 변경하여 가스 소비를 최적화
1. **Unused internal functions (TS-12)**
  - 문제: 선언된 내부 함수가 호출되지 않음.
  - 개선사항: 사용하지 않는 함수를 제거하여 배포 시 가스 소비 절감
1. **Duplicate code (StorageStateCommittee) (TS-14)**
  - 문제: 동일한 enum 타입이 중복 정의됨
  - 개선사항: 중복된 정의를 제거하여 코드 관리 포인트 감소 및 가독성 향상
1. **Validate user input (CandidateAddOnV1_1.initialize) (TS-15)**
  - 문제: Address 타입 파라미터 검증 부족으로 Zero address 저장 가능성 존재
  - 개선사항: 입력값 검증 로직 추가로 데이터 안정성 확보
1. **Validate user input (address) (TS-16)**
  - 문제: Address 타입 파라미터 검증 부족으로 Zero address 저장 가능성 존재
  - 개선사항: 입력값 검증 로직 추가로 데이터 안정성 확보
1. **Duplicate code (unstakedSeig) (TS-17)**
  - 문제: 동일 연산을 반복적으로 수행하여 가스 소비 증가
  - 개선사항: 연산 결과를 로컬 변수에 저장하여 중복 연산 제거
1. **Event emitted before state change (TS-18)**
  - 문제: 상태 변경 이전에 이벤트를 발생시켜 패턴 미준수
  - 개선사항: 상태 변경 후 이벤트를 발생시켜 Checks-Effects-Interactions 패턴 준수
1. **Duplicate code in modifier (nonRejected) (TS-19)**
  - 문제: Modifier 내부에서 동일 기능을 반복 수행함
  - 개선사항: Internal 함수로 대체하여 가스 소비 감소 및 코드 간소화
1. **Typo (TOON) (TS-20)**
  - 문제: 변수 이름에 오타 존재(TOON → TON)
  - 개선사항: 변수 이름을 올바르게 수정하여 명확성 향상
1. **Use reason string instead of predefined error (onlySeigniorageCommittee) (TS-21)**
  - 문제: **`require`**문에 String literal 사용으로 가스 소비 증가
  - 개선사항: Custom error를 사용하여 가스 최적화
1. **Unused variable (_isSenderOperator) (TS-23)**
  - 문제: 사용되지 않는 변수가 존재함
  - 개선사항: 불필요한 변수를 삭제하여 코드 간소화 및 배포 비용 절감
1. **Duplicate code (isPauseL2Seigniorage(msg.sender)) (TS-24)**
  - 문제: 동일 조건이 반복적으로 사용되어 가스 소비 증가
  - 개선사항: 조건을 로컬 변수로 할당하거나 코드 순서를 조정해 최적화

# CertiK

## **감사 기간**

- 2025년 1월 31일 ~ 2025년 4월 1일

## **발견된 이슈**

- **총 발견 이슈:** 15건
- **이슈 등급별 분포:**
  - Critical(치명적): 0건
  - Major(중대): 1건 (해결)
  - Medium(보통): 3건 (해결)
  - Minor(경미): 6건 (4건 해결, 2건 인정)
  - Informational(정보성): 4건 (해결)
  - Centralization : 1건 (2/3 Multi-Sig)

## **주요 감사 결과 및 개선 사항**

## **A. Critical (치명적)**

- 없음

## **B. Major (중대)**

1. **CON-02: Potential Storage Collision (주요 사항)**
  - 문제: 업그레이드 시 상속 순서 변경으로 인한 저장소 레이아웃 충돌 및 데이터 손상 위험
  - 해결 내용: 상속 순서를 변경하지 않고 기존 레이아웃을 유지하여 문제 해결

## **C. Medium (중간)**

1. SMV-05: Unused Minted Tokens in layer2Manager Contract
  - 문제: layer2Manager에 불필요하게 토큰이 민팅되어 잠기는 문제
  - 해결 내용: 조건문 추가로 불필요한 민팅 방지
1. SMV-06: Incorrect Reward Allocation After Unpause
  - 문제: 보상 일시 중지 후 재개 시, 중지 기간에 대한 보상이 잘못 지급되는 문제
  - 해결 내용: initialDebt 값 처리 로직 수정
1. SMV-07: Inconsistent Reward Calculation for Layer2
  - 문제: 최초 호출 시 보상 계산이 일관되지 않은 문제
  - 해결 내용: initialDebt 처리 로직 일관성 확보

## **D. Minor (경미)**

1. CON-04: Third-Party Dependencies
  - 문제: 외부 컨트랙트 의존성으로 인한 잠재적 위험
  - 해결 내용: 코드 변경 없이, 외부 컨트랙트 등록 시 코드 해시 및 권한 검증 절차 강화(인정, 미수정)
1. DAC-02: Unused Modifier
  - 문제: 사용되지 않는 modifier 존재
  - 해결 내용: 미사용 modifier 삭제
1. DAC-03: Violation of Check-Effect-Interaction Pattern
  - 문제: 외부 호출 전 상태 변경 미이행(재진입 공격 위험)
  - 해결 내용: Checks-Effects-Interactions 패턴 적용
1. DAC-04: Ineffective onlyMemberContract Modifier
  - 문제: modifier의 검증이 불충분하여 향후 보안 위험
  - 해결 내용: 추가 입력 검증 로직 도입
1. DAO-01: Lack of Storage Gap in Upgradeable Contract
  - 문제: 업그레이드 시 저장소 레이아웃 변경 위험(확장성 저하)
  - 해결 내용: 기존 서비스와의 호환성 문제로 미적용(인정, 미수정)
1. DMV-01: minDepositGasLimit Is Not Used
  - 문제: setter 함수는 있으나 실제로 사용되지 않는 변수
  - 해결 내용: 미사용 setter 및 변수 삭제, 관련 로직 정비

## **E. Informational (정보성)**

1. COT-01: Functions With _ as Name Prefix Not private/internal
  - 문제: _로 시작하는 함수가 private/internal이 아님
  - 해결 내용: 함수 접근제어자(private/internal) 수정
1. DAC-05: Redundant Code Components
  - 문제: 중복된 require문 등 불필요 코드 존재
  - 해결 내용: 중복 코드 삭제 및 리팩토링
1. DAC-06: Unused Internal Function
  - 문제: 사용되지 않는 internal 함수 존재
  - 해결 내용: 미사용 함수 삭제
1. OMV-01: Typos
  - 문제: 변수명 오타 등 코드 가독성 저하
  - 해결 내용: 오타 수정

## F. Centralization 

1. **CON-01 : Centralization Risks**
  - 문제 : 개인 EOA가 해킹당했을때 해당 계정이 가지고 있는 권한이 너무 많을 수 있습니다.
  - 해결 내용 : 개인 EOA를 멀티시그월렛으로 변경하여서 개인 EOA가 해킹당해도 DAO에 피해를 주지 못합니다.

# Omniscia

## **감사 기간**

- 2025년 1월 31일 ~ 2025년 2월 26일

## **발견된 이슈**

- **총 발견 이슈:** 21건
- **이슈 등급별 분포:**
  - Major(중대): 3건 (해결)
  - Medium(보통): 10건 (해결)
  - Minor(경미): 8건 (해결)

## A**. Major**

- **DAO-11M**
  - [https://github.com/tokamak-network/ton-staking-v2/issues/274](https://github.com/tokamak-network/ton-staking-v2/issues/274)
  - 문제 : DAOCommittee_V1::changeMember 및 DAOCommittee_V1::retireMember 함수는 빈도에 시간 제한을 두지 않으므로 단일 멤버가 충분한 ICandidate::totalStaked 평가가 있는 한 단일 트랜잭션에서 모든 기존 후보를 교체할 수 있습니다.
  - 해결 내용 : changeMember로 Member가 된 이후부터는 cooldownTime이 지난 후 changeMember가 가능하게 하였고, retireMember를 호출한 Member는 blackList에 등록되어서 더 이상 멤버가 될 수 없도록 하였습니다.
- SM3-07M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/155](https://github.com/tokamak-network/ton-staking-v2/issues/155)
- SM3-08M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/156](https://github.com/tokamak-network/ton-staking-v2/issues/156)
  - 문제 : 
  - 해결 내용 : Changed code to distribute seigniorage to layer2 even when non-layer2 user calls `updateSeigniorage`.

## **B. **Medium

- DAO-04S
  - [https://github.com/tokamak-network/ton-staking-v2/issues/260](https://github.com/tokamak-network/ton-staking-v2/issues/260)
  - 문제 : 연결된 명령문은 EIP-20 표준 전달 함수의 반환된 bool 값을 제대로 검증하지 않습니다. 표준에 따라 호출자는 false가 반환되지 않는다고 가정해서는 안 됩니다.
  - 해결 내용 : safeERC20으로 변경하여서 true, false값을 제대로 검증하도록 변경하였습니다.
- DAO-06M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/269](https://github.com/tokamak-network/ton-staking-v2/issues/269)
  - 문제 : DAOCommittee_V1::castVote 함수는 반대 투표만을 평가하기 때문에 abstain 단계에서 특정 의제의 정족수가 충족되었는지 여부를 잘못 평가합니다.
  - 해결 내용 : abstain 단계에서 전체 투표수와 남은 투표수 계산을 넣어서 계산을 진행하여서 잘못된 평가가 일어나지 않게 하였습니다.
- DAO-07M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/270](https://github.com/tokamak-network/ton-staking-v2/issues/270)
  - 문제 : Candidate::_getCoinageToken 구현에 따르면, 후보자가 사용하는 코인 토큰은 레이어 2 후보인지 여부에 따라 달라집니다. DAOCommittee_V1::operatorAmountCheck 함수는 이를 고려하지 않아 잘못되거나 실행 불가능한 코인 인스턴스를 생성합니다.
  - 해결 내용 : operatorCheck함수를 추가하고 해당 함수에서는 레이어2 후보의 여부에 따라서 다른 로직이 작동하도록 하였습니다.
- DAO-08M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/271](https://github.com/tokamak-network/ton-staking-v2/issues/271)
  - 문제 : DAOCommittee_V1::changeMember 함수를 사용하면 후보자가 기존 멤버를 각 멤버의 ICandidate::totalStaked 평가에서 단일 wei 차이로 교체할 수 있습니다. 우리는 이러한 특성이 불공평하고 조작되기 쉽다고 생각합니다.
  - 해결 내용 : 의도한 로직으로 문제되는 부분이 아니여서 수정하지 않았습니다.
- DAO-09M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/272](https://github.com/tokamak-network/ton-staking-v2/issues/272)
  - 문제 : TON 구현에서는 EIP-165 표준을 통해 지원을 신호하기 위해 DAOCommittee_V1::onApprove 함수가 호출되어야 하는 계약을 예상하지만 DAOCommittee_V1::supportsInterface 함수는 그러한 신호를 보내지 않습니다.
  - 해결 내용 : 사용되지 않는 supportsInterface함수를 삭제하였습니다.
- DAO-10M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/273](https://github.com/tokamak-network/ton-staking-v2/issues/273)
  - 문제 : DAOCommittee_V1::onApprove 함수는 모든 사용자가 시스템에서 의제를 생성할 수 있도록 허용하며, 여기에는 실행 불가능한 의제까지 포함될 수 있으므로 현재 안전하지 않습니다.
  - 해결 내용 : 안전을 위한 require문을 추가하였습니다.
- DAC-01M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/261](https://github.com/tokamak-network/ton-staking-v2/issues/261)
  - 문제 : DAOCommitteeOwner::decreaseMaxMember 함수 구현은 멤버 조회가 addressZero 주소로 평가되더라도 CandidateInfo 데이터 항목의 rewardPeriod를 재설정합니다. 불공평한 양의 보상이 0 주소에 빚을 졌기 때문에 우리는 이 특성을 유효하지 않다고 생각합니다.
  - 해결 내용 : addressZero주소일때는 해당 로직을 사용하지 않게 변경하였습니다.
- SM3-05M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/153](https://github.com/tokamak-network/ton-staking-v2/issues/153)
- SM3-06M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/154](https://github.com/tokamak-network/ton-staking-v2/issues/154)
- CAO-01M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/81](https://github.com/tokamak-network/ton-staking-v2/issues/81)
  - 문제 : initialize 함수는 다시 호출되는 것을 방지하지 않으므로 CandidateAddOnV1_1은 임의의 횟수만큼 다시 초기화될 수 있습니다.
  - 해결 내용 : 호출 후 재호출 방지

## **C. **Minor

- DAP-01M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/262](https://github.com/tokamak-network/ton-staking-v2/issues/262)
  - 문제 : DAOCommitteeProxy2:_setImplementation2 함수는 _alive 상태가 false로 설정되어 있어도 지정된 주소에 코드가 존재해야합니다.
  - 해결 내용 : false로 설정되어 있으면 지정된 주소에 대한 코드검사를 하지 않습니다.
- DAP-02M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/263](https://github.com/tokamak-network/ton-staking-v2/issues/263)
  - 문제 : DAOCommitteeProxy2::setSelectorImplementations2 함수는 사용하지 않을 특정 selector에 대해 비활성화가 불가능합니다.
  - 해결 내용 : unsetSelectorImplementations2함수를 추가하여서 특정 selector 비활성화 기능 추가
- DAO-03M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/266](https://github.com/tokamak-network/ton-staking-v2/issues/266)
  - 문제 : DAOCommittee_V1::byteToUnit256 함수는 오류 선택기를 건너뛰기 위해 이유 선언을 4바이트만큼 오프셋해야 하지만, 잘못된 방식으로 이를 수행합니다.
  - 해결 내용 : 사용하지 않는 함수여서 함수를 삭제하였습니다.
- DAO-04M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/267](https://github.com/tokamak-network/ton-staking-v2/issues/267)
  - 문제 : DAOCommittee_V1::createCandidate 함수는 관리 변형에 적용되는 여러 Modifier를 적용하지 않습니다.
  - 해결 내용 : Modifier 검사 추가
- DAO-05M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/268](https://github.com/tokamak-network/ton-staking-v2/issues/268)
  - 문제 : DAOCommittee_V1::onApprove 함수는 claimWTON 구현이 호출되는 것을 방지하여 WTON 인출을 금지하려고 시도하지만, claimERC20 함수는 WTON 인수로 잘못 호출될 수 있습니다.
  - 해결 내용 : DAOVault에서 TON출금을 금지하기위한 로직으로 WTON출금은 가능하기 때문에 문제가 아니여서 수정하지 않습니다.
- SM3-03M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/151](https://github.com/tokamak-network/ton-staking-v2/issues/151)
- SM3-04M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/152](https://github.com/tokamak-network/ton-staking-v2/issues/152)
- DMV-01M
  - [https://github.com/tokamak-network/ton-staking-v2/issues/114](https://github.com/tokamak-network/ton-staking-v2/issues/114)
  - 문제 : 참조된 바이트 메모리 페이로드는 '0x'로 정의되며, 이는 길이가 2인 페이로드와 그 안에 0과 x개의 문자를 포함하게 됩니다.
  - 해결 내용 : 0x가 아닌 empty bytes로 변경