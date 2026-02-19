## DisputeGameFactory

## 1.DisputeGameFactory의 역할

**`DisputeGameFactory`**는 새로운 **DisputeGame**(논쟁 게임)을 생성하는 스마트 컨트랙트입니다. 이 팩토리는 다음과 같은 작업을 수행합니다:

1. 새로운 **DisputeGame**을 생성.
1. 초기 루트 클레임(**`rootClaim`**)을 설정.
1. 논쟁의 유형(**`GameType`**)과 초기 데이터를 정의.

팩토리는 클론 팩토리(**`clones-with-immutable-args`**)를 사용하여 사전에 배포된 **`DisputeGame`** 구현을 복제(clone)하고, 이를 초기화합니다. ([https://github.com/vectorized/solady/blob/main/src/utils/LibClone.sol#L129](https://github.com/vectorized/solady/blob/main/src/utils/LibClone.sol#L129) 의 clone함수 이용) 

## **2. 게임 생성 과정**

1. **팩토리 호출**
  - 사용자가 **`DisputeGameFactory`**의 `create`함수를 호출하여 새로운 논쟁 게임을 생성합니다.
  - 입력값:
    - **`GameType`**: 논쟁의 유형 (CANNON, PERMISSIONED_CANNON 등 [https://github.com/code-423n4/2024-07-optimism/blob/main/packages/contracts-bedrock/src/dispute/lib/Types.sol](https://github.com/code-423n4/2024-07-optimism/blob/main/packages/contracts-bedrock/src/dispute/lib/Types.sol)).
    - **`rootClaim`**: 논쟁의 시작점이 되는 루트 클레임.
    - 기타 초기화 데이터 (예: 보증금, 시간 제한 등).
  - `clone` 함수 assembly 해석 ([https://github.com/vectorized/solady/blob/main/src/utils/LibClone.sol#L425-L499](https://github.com/vectorized/solady/blob/main/src/utils/LibClone.sol#L425-L499))
    1. **메모리 준비 및 args 복사**

```javascript
// args = abi.encodePacked(msg.sender, _rootClaim, parentHash, _extraData) 
let m := mload(0x40)
let n := mload(args)
pop(staticcall(gas(), 4, add(args, 0x20), n, add(m, 0x43), n))
```

    - 현재 "프리 메모리 포인터"를 가져옵니다. 이는 새로운 데이터를 저장할 메모리 위치를 나타냅니다.
    - **`args`**에 저장된 데이터의 길이를 가져옵니다. 이는 immutable arguments의 크기입니다.
    - **`identity precompile`**(주소 **`0x04`**)을 호출하여 immutable arguments를 복사합니다.
      - **`gas()`**: 현재 가용 가스를 전달.
      - **`add(args, 0x20)`**: **`args`**의 실제 데이터 시작 위치.
      - **`n`**: 복사할 데이터 길이.
      - **`add(m, 0x43)`**: 복사된 데이터를 저장할 메모리 위치.
    1. **런타임 바이트코드 구성**

```javascript
mstore(add(m, 0x23), 0x5af43d82803e903d91602b57fd5bf3)
mstore(add(m, 0x14), implementation)
mstore(m, add(0xfe61002d3d81600a3d39f3363d3d373d3d3d363d73, shl(136, n)))
```

    - 런타임 바이트코드의 마지막 부분을 메모리에 저장합니다. 이는 클론 컨트랙트가 구현체(implementation)로 delegatecall을 수행하도록 설정합니다.
    - 클론이 참조할 구현체(implementation) 주소를 저장합니다.
    - 런타임 바이트코드의 시작 부분을 저장합니다.
      - **`add(...)`**: 런타임 코드에 immutable arguments 길이를 추가.
      - **`shl(136, n)`**: immutable arguments의 길이를 런타임 코드에 반영하기 위해 왼쪽으로 시프트.
    1. Clone 컨트랙트 생성

```javascript
instance := create(value, add(m, add(0x0b, lt(n, 0xffd3))), add(n, 0x37))
```

    - EVM의 **`CREATE`** 명령어를 사용해 클론 컨트랙트를 배포합니다.
      - **`value`**: 생성 시 전송할 ETH 양.
      - **`add(m, add(0x0b, lt(n, 0xffd3)))`**: 런타임 코드 시작 위치. immutable arguments가 너무 크면 오프셋을 조정.
      - **`add(n, 0x37)`**: 런타임 코드 전체 길이 (immutable arguments 포함).
    1. 에러 처리

```javascript
if iszero(instance) {
    mstore(0x00, 0x30116425) // `DeploymentFailed()` 에러 메시지.
    revert(0x1c, 0x04)
}
```

    - 클론 생성이 실패하면 에러 메시지를 저장하고 트랜잭션을 revert합니다.
1. **초기화**
  - 팩토리는 새로 생성된 **`DisputeGame`**에 대해 **`initialize()`** 함수를 호출하여 초기 상태를 설정합니다.
  - 여기서 루트 클레임(**`rootClaim`**)과 기타 초기 데이터를 저장합니다.
  - **`initialize()`** 함수에서의 **assembly 해석**
    - 값이 예상 크기(**`0x7A`**, 즉 122 bytes)가 아닌 경우, 게임 초기화를 중단하고 오류를 반환합니다.
    - **0x04 bytes**: 함수 선택자 (function selector)
    - **0x14 bytes**: 게임 생성자의 주소 (creator address)
    - **0x20 bytes**: 루트 클레임 값 (root claim)
    - **0x20 bytes**: L1 헤드 값 (L1 head)
    - **0x20 bytes**: 추가 데이터 (extraData)
    - **0x02 bytes**: CWIA 관련 데이터
    - 총합: 4+20+32+32+32+2=122 bytes (**`0x7A`**)

```javascript
assembly {
    if iszero(eq(calldatasize(), 0x7A)) {
        // Store the selector for `BadExtraData()` & revert
        mstore(0x00, 0x9824bdab) // 오류 식별자를 메모리에 저장
        revert(0x1C, 0x04)       // 저장된 오류를 반환
    }
}
```
1. **이벤트 발생**
  - 팩토리는 **`DisputeGameCreated`** 이벤트를 발생시켜 새로운 게임이 생성되었음을 알립니다.

## FaultDisputeGame

## **1. 초기화 및 설정 관련 함수**

- **`initialize()`**
  - 게임을 초기화합니다.
  - 루트 클레임(root claim)을 설정하고, 보증금을 예치하며, 게임의 시작 상태를 정의합니다.
  - 이미 초기화된 경우 오류를 반환합니다.
- **`constructor()`**
  - 컨트랙트를 배포할 때 호출되며, 게임의 주요 파라미터(예: 최대 깊이, 분할 깊이, VM 주소 등)를 설정합니다.

## **2. 공격 및 방어 관련 함수**

- **`attack(Claim _disputed, uint256 _parentIndex, Claim _claim)`**
  - 특정 클레임에 대해 공격을 수행합니다.
  - 새로운 클레임을 추가하고, 공격자의 보증금을 예치합니다.
- **`defend(Claim _disputed, uint256 _parentIndex, Claim _claim)`**
  - 특정 클레임에 대해 방어를 수행합니다.
  - 새로운 클레임을 추가하고, 방어자의 보증금을 예치합니다.
- **`move(Claim _disputed, uint256 _challengeIndex, Claim _claim, bool _isAttack)`**
  - 공격 또는 방어 동작을 수행하는 공통 함수입니다.
  - 클레임의 위치와 깊이를 계산하고 유효성을 검증합니다.
- **`step(uint256 _claimIndex, bool _isAttack, bytes calldata _stateData, bytes calldata _proof)`**
  - 단일 명령어 실행 단계를 검증하여 상태 전환이 예상된 결과와 일치하는지 확인합니다.
  - 공격 또는 방어의 유효성을 평가합니다.

## **3. 분쟁 해결 관련 함수**

- **`resolve()`**
  - 전체 게임의 상태를 해소하며 최종 승자를 결정합니다.
  - 모든 하위 게임(subgame)이 해결된 경우에만 호출 가능합니다.
- **`resolveClaim(uint256 _claimIndex, uint256 _numToResolve)`**
  - 특정 클레임에 대한 하위 게임을 해결합니다.
  - 시간이 만료되었거나 반박되지 않은 경우 해당 클레임을 암묵적으로 유효하다고 간주합니다.

## **4. 데이터 관리 및 조회 함수**

- **`addLocalData(uint256 _ident, uint256 _execLeafIdx, uint256 _partOffset)`**
  - 로컬 데이터를 추가하여 실행 컨텍스트를 설정합니다.
  - L1 헤드 해시(L1 Head Hash), 시작 출력 루트(Start Output Root) 등과 같은 데이터를 로드합니다.
- **`claimDataLen()`**
  - 현재까지 생성된 클레임 데이터의 길이를 반환합니다.
- **`getRequiredBond(Position _position)`**
  - 특정 위치에서 필요한 보증금 금액을 반환합니다.
-  **`rootClaim()`** 
```javascript
function rootClaim() public pure returns (Claim rootClaim_) {
    rootClaim_ = Claim.wrap(_getArgBytes32(0x14));
}
```

  - 함수가 게임 생성 시 전달된 데이터를 기반으로 루트 클레임 값을 반환합니다:
  - **`_getArgBytes32(0x14)`**는 게임 생성 시 전달된 데이터(**`calldata`**)에서 특정 위치(**`0x14`**)에 저장된 값을 읽습니다.
  - 이 값은 Merkle 루트 또는 해시 값이며, 논쟁 중인 전체 상태 전환을 요약한 데이터입니다.

## **5. 기타 유틸리티 함수**

- **`challengeRootL2Block(Types.OutputRootProof calldata _outputRootProof, bytes calldata _headerRLP)`**
  - 루트 L2 블록 번호를 검증하여 잘못된 경우 이를 반박합니다.
- **`getChallengerDuration(uint256 _claimIndex)`**
  - 특정 클레임에 대해 도전자가 사용할 수 있는 남은 시간을 반환합니다.
- **`claimCredit(address _recipient)`**
  - 승리한 참가자가 보증금을 회수할 수 있도록 합니다.

## **6. move 함수 자세히**

```javascript
function move(Claim _disputed, uint256 _challengeIndex, Claim _claim, bool _isAttack) public payable virtual
```

- **`move`** 함수는 공격 또는 방어 동작을 수행합니다.
  - **`_disputed`**: 논쟁 중인 클레임(부모 클레임).
  - **`_challengeIndex`**: 논쟁 중인 클레임의 인덱스.
  - **`_claim`**: 새로 추가될 클레임.
  - **`_isAttack`**: 공격 여부를 나타내는 플래그 (**`true`** = 공격, **`false`** = 방어).

```javascript
if (status != GameStatus.IN_PROGRESS) revert GameNotInProgress();
```

- 게임 상태가 **`IN_PROGRESS`**(진행 중)가 아니면 트랜잭션을 중단합니다. 게임이 종료되었거나 초기화되지 않은 경우 실행되지 않습니다.

```javascript
ClaimData memory parent = claimData[_challengeIndex];
```

- 논쟁 중인 부모 클레임 데이터를 가져옵니다.
  - **`claimData`** 배열에서 **`_challengeIndex`** 위치에 있는 데이터를 읽습니다.

```javascript
if (Claim.unwrap(parent.claim) != Claim.unwrap(_disputed)) revert InvalidDisputedClaimIndex();
```

- 제공된 **`_disputed`** 클레임이 실제로 부모 클레임과 일치하는지 확인합니다.
  - 일치하지 않으면 오류를 반환합니다(**`InvalidDisputedClaimIndex`**).

```javascript
Position parentPos = parent.position;
Position nextPosition = parentPos.move(_isAttack);

//LibPosition
function move(Position _position, bool _isAttack) internal pure returns (Position move_) {
    assembly {
        move_ := shl(1, or(iszero(_isAttack), _position))
    }
}
```

- **`parent.position`**: 부모 클레임의 위치를 가져옵니다.
- **`parentPos.move(_isAttack)`**: 공격 또는 방어에 따라 다음 위치(**`nextPosition`**)를 계산합니다.
  - **`_isAttack`** 값이 **`true`**이면 **왼쪽 자식 노드**로 이동(공격).
  - **`_isAttack`** 값이 **`false`**이면 **오른쪽 자식 노드**로 이동(방어).
    - **`_isAttack == true`**: 2×n (왼쪽 자식으로 이동).
    - **`_isAttack == false`**: 2×n+1 (오른쪽 자식으로 이동).

```javascript
uint256 nextPositionDepth = nextPosition.depth();
```

- 다음 위치(**`nextPosition`**)의 깊이를 계산합니다. 깊이는 게임 트리에서 노드의 레벨을 나타냅니다.

```javascript
if ((_challengeIndex == 0 || nextPositionDepth == SPLIT_DEPTH + 2) && !_isAttack) {
    revert CannotDefendRootClaim();
}
```

- 루트 클레임에 대해 방어를 시도하거나, 특정 깊이 이상에서 방어를 시도하면 오류를 반환합니다(**`CannotDefendRootClaim`**).

```javascript
if (l2BlockNumberChallenged && _challengeIndex == 0) revert L2BlockNumberChallenged();
```

- 루트 L2 블록 번호가 이미 도전받은 경우, 추가적인 동작을 금지합니다.

```javascript
if (nextPositionDepth > MAX_GAME_DEPTH) revert GameDepthExceeded();
```

- 다음 위치가 게임 트리의 최대 깊이(**`MAX_GAME_DEPTH`**)를 초과하면 오류를 반환합니다(**`GameDepthExceeded`**).

```javascript
if (nextPositionDepth == SPLIT_DEPTH + 1) {
    _verifyExecBisectionRoot(_claim, _challengeIndex, parentPos, _isAttack);
}
```

- 분할 깊이(**`SPLIT_DEPTH + 1`**)에 도달하면 실행 분할 루트를 검증합니다.
  - **`_verifyExecBisectionRoot`**: 실행 분할 서브게임의 루트 클레임 무결성을 확인하는 함수입니다.

```javascript
if (getRequiredBond(nextPosition) != msg.value) revert IncorrectBondAmount();
```

- 제출된 보증금(**`msg.value`**)이 해당 위치에서 요구되는 보증금과 일치하지 않으면 오류를 반환합니다(**`IncorrectBondAmount`**).

```javascript
Duration nextDuration = getChallengerDuration(_challengeIndex);
```

- 다음 단계에서 사용될 시간 제한(clock duration)을 계산합니다.

```javascript
if (nextDuration.raw() == MAX_CLOCK_DURATION.raw()) revert ClockTimeExceeded();
```

- 시간이 초과되었는지 확인하고, 초과된 경우 오류를 반환합니다(**`ClockTimeExceeded`**).

```javascript
if (nextDuration.raw() > MAX_CLOCK_DURATION.raw() - CLOCK_EXTENSION.raw()) {
    uint64 extensionPeriod = nextPositionDepth == SPLIT_DEPTH - 1 ? CLOCK_EXTENSION.raw() * 2 : CLOCK_EXTENSION.raw();
    nextDuration = Duration.wrap(MAX_CLOCK_DURATION.raw() - extensionPeriod);
}
```

- 남은 시간이 부족하면 추가 시간을 부여합니다(**`CLOCK_EXTENSION`**).
- 특정 조건에서는 시간을 두 배로 연장할 수 있습니다.

```javascript
Clock nextClock = LibClock.wrap(nextDuration, Timestamp.wrap(uint64(block.timestamp)));
```

- 새로운 시간 제한(clock)을 생성하여 현재 타임스탬프와 함께 저장합니다.

```javascript
Hash claimHash = _claim.hashClaimPos(nextPosition, _challengeIndex);
if (claims[claimHash]) revert ClaimAlreadyExists();
claims[claimHash] = true;
```

- 새로운 클레임의 고유 해시 값을 생성하고, 기존에 동일한 해시 값이 존재하는지 확인합니다.
- 중복된 경우 오류를 반환합니다(**`ClaimAlreadyExists`**).

```javascript
claimData.push(
    ClaimData({
        parentIndex: uint32(_challengeIndex),
        counteredBy: address(0),
        claimant: msg.sender,
        bond: uint128(msg.value),
        claim: _claim,
        position: nextPosition,
        clock: nextClock
    })
);
```

- 새로운 클레임 데이터를 생성하여 **`claimData`** 배열에 추가합니다.
- 부모 인덱스, 제출자 주소, 보증금, 클레임 값 등을 포함합니다.

```javascript
subgames[_challengeIndex].push(claimData.length - 1);
```

- 부모 클레임의 서브게임 목록에 새로 생성된 클레임의 인덱스를 추가합니다.

```javascript
WETH.deposit{ value: msg.value }();
```

- 제출된 보증금을 WETH 컨트랙트에 예치합니다.

```javascript
emit Move(_challengeIndex, _claim, msg.sender);
```

- 새로운 이동(move)이 발생했음을 알리는 이벤트를 발생시킵니다.

## **분쟁 해결 과정**

## **1. 클레임 및 서브게임 구조**

- 분쟁은 루트 클레임(root claim)에서 시작되며, 각 클레임은 자신만의 서브게임을 가집니다.
- 서브게임은 트리 형태로 구성되며, 각 클레임은 자식 클레임(공격 또는 방어)으로 이어집니다.
- 게임의 최대 깊이(**`MAX_GAME_DEPTH`**)에 도달하면 더 이상 분할되지 않고, 최종적으로 해당 상태가 검증됩니다[5](https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html)[6](https://github.com/ethereum-optimism/specs/blob/main/specs/fault-proof/stage-one/fault-dispute-game.md).

## **2. 분쟁 진행**

1. **초기화 및 클레임 제출**
  - 루트 클레임이 제출되면, 도전자(Challenger)는 이를 공격하거나 방어할 수 있습니다.
  - 각 공격 또는 방어는 새로운 클레임을 생성하며, 이는 서브게임으로 이어집니다.
1. **상태 이분법(Bisection)**
  - 논쟁 중인 L2 상태 전환을 이분법적으로 나누어 점진적으로 좁혀갑니다.
  - 각 단계에서 도전자와 방어자는 서로 공격 및 방어를 통해 상대방의 주장을 반박합니다
1. **최대 깊이 도달**
  - 게임이 최대 깊이에 도달하면, 논쟁 중인 상태 전환이 단일 명령어 수준으로 축소됩니다.
  - 이 시점에서 **`MIPS.sol`** 컨트랙트를 호출하여 단일 명령어를 실행하고 결과를 검증합니다

## **3. 분쟁 해결**

1. **서브게임 해소 (****`resolveClaim`****)**
  - 각 서브게임은 하위 서브게임들이 모두 해결된 후에만 해소될 수 있습니다.
  - 서브게임의 시간이 만료되었거나 반박되지 않은 경우, 해당 클레임은 암묵적으로 유효하다고 간주됩니다.
  - 보증금(bond)은 승자에게 지급됩니다
1. **최종 게임 해소 (****`resolve`****)**
  - 모든 서브게임이 해결되면 루트 클레임에 대해 최종 결정을 내립니다.
  - 루트 클레임이 반박되지 않으면 방어자가 승리하며, 반대로 반박에 성공하면 도전자가 승리합니다.
  - 결과는 **`Anchor State Registry`**에 보고되어 L2 상태가 업데이트됩니다

## **핵심 요소**

- **MIPS.sol과의 상호작용**:
최대 깊이에 도달한 상태에서 단일 명령어를 실행하여 논쟁 중인 상태 전환을 검증합니다. 이 과정에서 이전 상태(Pre-image)와 이후 상태(Post-image)를 비교하여 결과를 결정합니다
- **시간 제한**:
각 서브게임에는 제한 시간이 설정되며, 시간이 만료되면 해당 클레임은 암묵적으로 유효하거나 무효로 간주됩니다
- **보증금 분배**:
각 참여자는 클레임 제출 시 보증금을 예치하며, 최종 승자는 상대방의 보증금을 획득합니다

## 공격, 방어 매커니즘

## **1. 루트 클레임 시작**

- 게임은 루트 클레임(root claim)으로 시작됩니다. 이 클레임은 L2 상태 전환의 출력 루트를 나타내며, 수비자(Defender)가 이를 방어합니다.
- 도전자(Challenger)는 루트 클레임이 잘못되었다고 주장하며, 이를 반박하기 위해 공격을 시작합니다.

## **2. 이진 분할(Bisection)**

- FDG는 루트 클레임을 검증하기 위해 **이진 분할(bisection)** 방식을 사용합니다.
- 전체 실행 추적(Execution Trace)을 여러 구간으로 나누고, 각 구간의 상태 전환에 대해 새로운 클레임을 제시합니다.
- 도전자는 특정 구간에서 오류가 발생했다고 주장하며 공격(Attack)을 수행하고, 수비자는 해당 구간이 올바르다고 주장하며 방어(Defend)합니다.

## **예시:**

1. 실행 추적 [A→B→C→D]가 있다고 가정합니다.
1. 도전자는 [A→D] 전체가 잘못되었다고 주장하며 공격.
1. 시스템은 이를 절반으로 나누어 [A→B]와 [B→D]로 구간을 나눕니다.
1. 도전자는 특정 구간(예: [B→D])이 잘못되었다고 주장하며 다시 공격.

이 과정을 반복하여 점차 좁혀갑니다.

## **3. 최소 단위로 좁혀감**

- 이진 분할 과정을 통해 실행 추적은 점점 더 작은 구간으로 나뉘며, 최종적으로 단일 상태 전환 단계로 좁혀집니다.
- 최종 단계에서는 특정 명령어 수준에서 상태 전환이 올바른지 여부를 확인합니다.

## **최종 단계:**

- 특정 상태 전환 S1→S2가 주어졌을 때:
  - 도전자는 이 전환이 잘못되었음을 증명해야 합니다.
  - 수비자는 이 전환이 올바르다는 것을 증명해야 합니다.
- 이때, 가상 머신(FPVM)이 해당 상태 전환을 실행하여 결과를 검증합니다.

## **4. 결론 도출**

- 최종적으로 단일 상태 전환 단계에서 VM(Virtual Machine)이 상태 전환의 유효성을 결정합니다.
- 두 가지 결과 중 하나로 결론이 납니다:
  1. **루트 클레임 유효**: 모든 공격이 반박되었으며, 수비자가 승리.
  1. **루트 클레임 무효**: 특정 상태 전환에서 오류가 발견되어 도전자가 승리.

## **공격과 방어의 역할**

## **공격(Attack):**

- 도전자는 기존 클레임에 대해 새로운 하위 클레임(Subclaim)을 제시하며 오류를 주장합니다.
- 공격의 목표는 특정 구간이나 상태 전환에서 잘못된 부분을 식별하는 것입니다.

## **방어(Defend):**

- 수비자는 도전자의 주장을 반박하며 기존 클레임을 지지합니다.
- 방어의 목표는 모든 하위 클레임이 올바르게 계산되었음을 증명하는 것입니다.

## **a. 이분법적 논쟁 진행**

- 게임은 논쟁 중인 상태 전환을 점진적으로 좁혀가며, 최종적으로 단일 명령어 수준까지 축소합니다.
- 각 단계에서:
  - 왼쪽 자식 노드(방어)는 부모 클레임의 **전반부**를 나타냅니다.
  - 오른쪽 자식 노드(공격)는 부모 클레임의 **후반부**를 나타냅니다.
- 이동 방향을 고정함으로써, 각 클레임이 논쟁 중인 범위 내에서 정확히 어디에 위치하는지 명확하게 정의할 수 있습니다.

## **b. 효율적인 상태 추적**

- 이동 방향이 정해져 있으면 트리 내에서 각 노드의 위치와 해당 범위를 쉽게 계산할 수 있습니다.
  - 예: 부모 노드가 [100] 범위를 나타낸다면,
    - 왼쪽 자식(방어)은 ,
    - 오른쪽 자식(공격)은 [100]을 나타냅니다.
- 이를 통해 트리 탐색 및 상태 검증이 체계적이고 효율적으로 이루어집니다.

## **c. 공격과 방어 역할 구분**

- 공격자는 항상 기존 클레임에 반대하며 새로운 문제를 제기해야 하므로, 부모 범위의 후반부로 이동하여 해당 부분에 문제가 있다고 주장합니다.
- 방어자는 기존 클레임을 지지하며 이를 보호해야 하므로, 부모 범위의 전반부로 이동하여 해당 부분이 옳다고 주장합니다.
- 이러한 역할 구분은 게임 논리를 명확히 하고, 분쟁 해결 과정을 체계적으로 관리할 수 있게 합니다.

## **d. 최종 상태 검증**

- 게임 트리가 최대 깊이에 도달하면 단일 상태 전환(단일 명령어 실행)에 도달합니다.
- 이 시점에서 특정 위치의 상태가 예상된 결과와 일치하는지 검증합니다.
- 이동 방향이 정해져 있어야 이러한 최종 상태 검증이 정확히 이루어질 수 있습니다.

## **FDG에서 결론에 도달하는 핵심 원리**

1. **점진적 축소**:
  - 이진 분할 과정을 통해 논쟁 범위를 점차 축소하여 단일 명령어 수준까지 좁힙니다.
1. **결정론적 검증**:
  - 최종 단계에서는 VM(FPVM)이 결정론적으로 상태 전환을 실행하여 결과를 검증합니다.
  - VM은 항상 동일한 입력에 대해 동일한 출력을 생성하므로, 최종 결과는 명확히 판별됩니다.
1. **시간 제한**:
  - 게임 시계(Game Clock)를 통해 각 참여자가 일정 시간 내에 움직이지 않으면 해당 클레임은 자동으로 만료됩니다.
  - 이는 게임의 종료를 보장하고 지연을 방지합니다.
1. **인센티브 구조**:
  - 잘못된 주장을 한 참여자는 보증금을 잃고, 정직한 참여자는 보상을 받습니다.
  - 이를 통해 정직한 행동을 유도하고 부정직한 행동을 억제합니다.