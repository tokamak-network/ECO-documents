[[Contract 분석]]

## **Fault Proofs의 주요 특징**

1. **기능 및 목적**:
  - 사용자가 OP Stack 체인의 상태에 대한 제안(State Proposal)을 제출하고 이를 검증하거나 도전할 수 있도록 함.
  - L2에서 L1로의 메시지 전송 및 인출을 신뢰할 수 있는 제3자 없이 수행 가능.
  - 모듈형 설계를 통해 다양한 증명 메커니즘을 통합 가능.
1. **보안 강화**:
  - Optimism Security Council이 Guardian 역할을 수행하여 Fault Proof 게임 실패 시 백업 역할을 제공.
  - Guardian은 잘못된 제안을 차단하거나 시스템을 PermissionedDisputeGame(제한된 역할 기반 시스템)으로 전환 가능.

## **Permissionless Proposals 및 Challenges**

1. **Permissionless Proposals**:
  - "State Proposals"는 OP Stack 체인의 상태에 대한 주장으로, Ethereum 상의 **`DisputeGameFactory`** 계약을 통해 제출됨.
  - Fault Proofs 업그레이드 이후, 누구나 이러한 제안을 제출 가능.
1. **Permissionless Challenges**:
  - 잘못된 제안을 방지하기 위해 모든 사용자가 도전할 수 있음.
  - 약 1주일의 도전 기간 동안 잘못된 제안에 대해 이의를 제기 가능.
  - 사용자는 **`op-challenger`** 도구를 사용하여 분쟁 과정에 참여 가능.

## **모듈형 설계 및 다중 레이어 보안**

- Fault Proof 시스템은 다중 증명 시스템(Multi-Proof System)을 지원하도록 설계됨.
- 초기 Cannon 증명 시스템 외에도 추가적인 증명 메커니즘 통합 가능.
- 주요 보안 조치:
  - 오프체인 모니터링 시스템(**`op-dispute-mon`**)으로 모든 제안된 루트를 감시.
  - "Airgap Window"라는 추가 지연 기간 동안 Guardian이 루트를 거부할 수 있음.
  - **`DelayedWETH`** 계약을 통해 보증금을 보유하고, 게임 결과가 잘못될 경우 이를 재조정.
1. **분쟁 해결 단계**:
  - 최악의 경우 게임 깊이는 최대 73단계이며, 여러 클레임과 반박 클레임이 결합될 수 있음.
1. **Guardian 역할**:
  - Guardian은 인출 일시 중지, 게임 블랙리스트 지정, Permissioned 시스템 전환 등의 권한을 가짐.
1. **운영 비용**:
  - FP 시스템 운영에는 초기 보증금(예: OP Mainnet 기준 시간당 0.08 ETH)이 필요하며, 약 7일간의 분쟁 기간 동안 약 14 ETH가 소요될 수 있음.
1. **보증금 크기**:
  - 게임 내 반박 클레임 비용과 스팸 방지를 고려하여 보증금 크기가 결정됨.

Fault Dispute Game (FDG)는 Optimism의 Fault Proof 시스템 내에서 루트 클레임의 유효성을 검증하는 분쟁 게임 메커니즘입니다. FDG는 L2 상태 전환의 실행 추적 및 출력 루트를 이진 분할(bisect)하여 단일 명령어 단계 수준까지 좁혀가는 과정을 통해 클레임의 진위를 판별합니다. 

## **개요**

- FDG는 L2 블록 상태 전환과 관련된 클레임을 검증하는 게임으로, 잘못된 클레임을 반박하기 위해 플레이어들이 상호작용합니다.
- 각 클레임은 L2의 전체 상태 기록 중 특정 범위를 좁혀가며, 최종적으로 단일 상태 전환에서 분쟁의 원인을 판별합니다.
- 게임은 시간 제한 내에 해결되며, 반박된 클레임과 반박되지 않은 클레임을 기반으로 승자가 결정됩니다.

## **핵심 정의**

1. **Virtual Machine (VM)**:
  - VM은 상태 전환 함수(State Transition Function, STF)를 사용해 *pre-state*에서 *post-state*로 전환합니다.
  - 데이터 무결성을 검증하기 위해 증명(proof)을 포함할 수 있습니다.
1. **PreimageOracle**:
  - VM이 외부 데이터를 읽기 위해 사용하는 데이터 저장소로, 필요한 데이터를 사전에 로드해야 합니다.
1. **Execution Trace**:
  - VM 상태의 연속적인 시퀀스로, 각 상태 전환이 고유하게 정의됩니다.
1. **Claims**:
  - 출력 루트 또는 특정 명령어 단계에서 VM 상태를 나타내는 해시 값입니다.
  - FDG는 초기화 시 L2 블록 번호에 해당하는 출력 루트로 시작하며, 분쟁 게임은 이 루트를 중심으로 진행됩니다.
1. **Anchor State**:
  - 유효하다고 간주되는 이전 출력 루트로, FDG는 이를 기준으로 실행됩니다.
1. **Directed Acyclic Graph (DAG)**:
  - 클레임 간 관계를 나타내는 그래프로, 노드는 클레임을, 엣지는 공격(Attack) 또는 방어(Defend) 움직임을 나타냅니다.
1. **Game Tree**:
  - 이진 트리 구조로, 각 노드는 특정 클레임의 위치를 나타냅니다.
  - 트리는 **`SPLIT_DEPTH`**와 **`MAX_GAME_DEPTH`**로 나뉘며, 깊이에 따라 출력 루트 또는 실행 추적에 대한 클레임으로 구분됩니다.

## **게임 메커니즘**

1. **참여자 (Actors)**:
  - 두 종류의 플레이어가 존재: **Challengers(도전자)**와 **Defenders(수비자)**.
  - 도전자는 루트 클레임을 반박하려 하고, 수비자는 이를 방어합니다.
1. **움직임 (Moves)**:
  - 공격(Attack): 기존 클레임에 반대하는 새로운 클레임을 추가.
  - 방어(Defend): 기존 클레임을 지지하며 반박 시도를 막음.
1. **L2 Block Number Challenge**:
  - 도전자가 출력 루트와 관련된 L2 블록 번호의 무결성을 검증하는 특별한 행동입니다.
1. **Step**:
  - **`MAX_GAME_DEPTH`**에서 VM의 상태 전환(STF)을 통해 클레임의 유효성을 직접 확인합니다.
  - 공격 스텝은 잘못된 상태 전환을 증명하고, 방어 스텝은 잘못된 공격을 반박합니다.
1. **PreimageOracle 상호작용**:
  - 특정 단계에서 필요한 데이터를 Oracle에 미리 로드해야 하며, 대규모 데이터는 스트리밍 방식으로 제출 가능합니다.
1. **게임 시계 (Game Clock)**:
  - 체스 시계와 유사하게 각 팀이 움직이는 데 소요되는 시간을 추적하며 지연을 방지합니다.
  - 제한 시간을 초과하면 해당 클레임은 만료됩니다.

## **게임 해결 및 최종화**

1. **해결 (Resolution)**:
  - 모든 하위 게임(Subgame)이 해결되면 최상위 루트 클레임이 유효한지 여부가 결정됩니다.
  - 하위 게임은 DAG 구조를 따라 아래에서 위로 순차적으로 해결됩니다.
1. **최종화 (Finalization)**:
  - 유효한 루트 클레임은 Anchor State Registry에 보고되어 새 앵커 상태로 업데이트됩니다.
  - 업데이트는 FDG 계약이 생성되었음을 확인하고, 기존 앵커보다 최신 상태여야 합니다.

## **예시로 보는 루트 클레임**

## **초기 데이터**

1. 초기 상태 (S0):
Account A: 100 ETH
Account B: 50 ETH
1. 최종 상태 (Sn):
Account A: 100 ETH
Account B: 50 ETH

## **Merkle 트리 생성**

1. 각 트랜잭션과 중간 상태를 리프 노드로 추가:
```javascript
Tx1 -> Hash1
Tx2 -> Hash2
...
TxN -> HashN
```
1. 리프 노드들을 반복적으로 해싱하여 Merkle 루트를 생성:
```javascript
      Root (Merkle Root)
       /         \
   HashA         HashB
   /  \          /  \
 H1    H2      H3    H4

```
1. 최종적으로 생성된 Merkle 루트를 **`rootClaim`** 값으로 설정:
```javascript
rootClaim = Root (Merkle Root)
```

## **Solidity 코드에서 루트 클레임**

Solidity 코드에서는 **`rootClaim()`** 함수가 게임 생성 시 전달된 데이터를 기반으로 루트 클레임 값을 반환합니다:

```javascript
function rootClaim() public pure returns (Claim rootClaim_) {
    rootClaim_ = Claim.wrap(_getArgBytes32(0x14));
}
```

- **`_getArgBytes32(0x14)`**는 게임 생성 시 전달된 데이터(**`calldata`**)에서 특정 위치(**`0x14`**)에 저장된 값을 읽습니다.
- 이 값은 Merkle 루트 또는 해시 값이며, 논쟁 중인 전체 상태 전환을 요약한 데이터입니다.