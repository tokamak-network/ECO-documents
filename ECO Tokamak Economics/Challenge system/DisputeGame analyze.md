## **1. DisputeGameFactory, FaultDisputeGame 핵심 구조 분석**

**1) DisputeGameFactory.sol**

### 역할

- **DisputeGameFactory**는 새로운 분쟁(Dispute) 게임을 생성하는 컨트랙트입니다.
- L1(이더리움 메인넷)에 배포되어, L2 상태에 대한 이의제기(Dispute)가 발생할 때마다 새로운 DisputeGame(분쟁 게임) 컨트랙트를 만듭니다.

### 함수

- **create(gameType, rootClaim, extraData, ...):**
  - 새로운 DisputeGame(분쟁 게임) 컨트랙트를 생성합니다.
  - gameType: 분쟁 게임의 종류(예: FaultDisputeGame, 0)
  - rootClaim: 검증하고자 하는 L2 상태의 루트 값
  - extraData: `_l2BlockNumber` 값을 ABI 인코딩한 `bytes` 값이어야 합니다.
    - `_l2BlockNumber`** **(uint64) **:이 분쟁 게임이 검증하려는 L2 블록의 번호입니다. 즉, 이 게임이 어떤 L2 상태에 대한 클레임을 다루는지 명시합니다.**
      - **테스트 목적**: 유효한 `uint64` 범위 내의 아무 숫자나 넣을 수 있습니다.
- **getGame(gameId): **특정 게임 인스턴스의 주소를 반환합니다.

### 

---

**2) FaultDisputeGame.sol**

### 역할

- **FaultDisputeGame**은 L2 상태의 진위 여부를 검증하는 실제 분쟁 게임 로직을 담당합니다.
- L1에 배포되어, Proposer와 Challenger(이의제기자)가 증거를 제출하며 게임을 진행합니다.

### 주요 함수

- **initialize(rootClaim, ...):**
  - 게임 인스턴스 초기화, 검증할 L2 상태(rootClaim) 등 세팅
- **attack/defend/step:**
  - Proposer와 Challenger가 번갈아가며 증거를 제출(공격/방어/단계별 진행)
- **resolve():**
  - 게임 종료 및 승자 결정, 보상/패널티 처리

## **2. **DisputeGame에 대한 **L1, L2, 오프체인에서의 역할 및 상호작용**

### **1) L1 (이더리움 메인넷)**

- **DisputeGameFactory, FaultDisputeGame 등 핵심 컨트랙트가 배포됨**
- L2에서 제출된 상태(rootClaim)에 대해, 이의제기가 들어오면 DisputeGameFactory가 새로운 FaultDisputeGame 인스턴스를 생성
- 모든 분쟁 게임의 진행(증거 제출, 승패 판정, 보상/패널티 등)이 L1에서 처리됨
- **보안의 최종 책임을 가짐** (L2 상태의 진위는 L1에서 최종 결정)

### **2) L2 (Optimism Rollup)**

- L2에서는 스마트컨트랙트가 아니라, 주로 오프체인 소프트웨어가 상태 계산 및 모니터링을 담당

### **3) 오프체인(Off-chain)**

- **Rollup Node, Proposer, Verifier 등 소프트웨어가 동작**
- Proposer: L2 트랜잭션을 모아 상태(rootClaim) 생성, L1에 제출
- Verifier: L2 상태를 검증, 이상 발견 시 L1에 이의제기
- 분쟁 게임이 시작되면, 오프체인에서 증거를 계산/준비하여 L1의 FaultDisputeGame에 제출

## **3. 전체 흐름 요약 (시퀀스 다이어그램)**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/5b5ca3a3-0115-41fc-a1fa-b41bd43dd86a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZL4TKN6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGEN6fzraABC8EL2FtUnwYcsBtkN%2Bo0Nk26zFHGbQrTkAiEA9PFU7qMkxjGQjmWxpLbq4Es6%2BUA62JDKelIYYR2CzT4q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNE1kFHAkDycanAQ4ircA%2BTf2dNgMiwrZCZeExYmvdOpy4VZuUzFAvnDqkJMrGj7AVEcDkw1ncml0RHtiVPJKT%2BFstBn0ryCLALdQlAftNTagavLvQJ1I0xOMTa3BoIjwxogrkjWNe%2F8%2Fv9XlkpVfgBWUFICZ7Gly%2Bt%2Frn3riTjei7sD%2F1weNYZsRi60XAYdctHV3WjjXIRqorVHY%2FL2%2B%2F4rHr1DM2r%2FRSRFX7%2B%2B992V10UY9ipF1whkcMyKDovIY%2FTcp2vFAYCFD2mu3n61XgFoWVB%2B5Bjg%2BErBhL6IrmEdH5bcBCkUxeySgqar3hkEQ2DpzYFHZU5F78oHRhYE9aHWQQ5XvGgxILljK3sFxh90iSaQkGCcPIJCpP6iPHcXCv08A2qbvwnvRXd3Tc%2B9fyQ4R9yTYRtz5T%2FXo707AdPF0jLyB0r0WPVa4VeIe7BXaCoq%2FNRbRVvFRKnso88YRtjlc6yBz6jz69KIglLeUsmNsLo%2FiqMGM4kVYlyfW6X%2BueGwloKQbtigGmdO2PLOKSUa3zPGXAGFDSESZV%2BvHWC290NNp9fNowBiEQGBMk9H3i4VRAlyiy6DEXJ9S8yHZ8BAikrSFHRNHM0AkX9rddHso5VthMWkKsvxODnb%2By%2Bu%2FYbNL0v8oTt0b7SQMJDv2cwGOqUBBWZit3sytfli4lGwenG%2BTUeCwZKd%2F6oDtqLwoWL4Uo9ARWR8Weertqgn%2FsobuJ1W41vO0qA90MXliKwcCVvsK7hA7DrdYb3Zrzgs9E3yQqlUoEtxIQlO5e%2BB31icjdxyCk7iIYECihzpxqq0Dd%2BHMMaFptrQMEwkQiZwm3Am8wkUvmdTMD%2FswUtYz6Zaj59XZ1oD5dvsdZ%2FcP4t0oGUMHyZ0Nx4L&X-Amz-Signature=a2f132d1a3465888a573a81ee97c1e85db647a4376d7e804f2a2c760f2d162c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## **4. 실제 테스트 on Sepolia **

- DisputeGame create
  - tx : [https://sepolia.etherscan.io/tx/0x8ce341276d3a9f8e6d91100bf27e134afc998da7df78dec019ac77229ae0b69c](https://sepolia.etherscan.io/tx/0x8ce341276d3a9f8e6d91100bf27e134afc998da7df78dec019ac77229ae0b69c) (rootClaim으로 아무값이나 넣어서 attack을 당함)
- created Disputegame Contract : [0x9e929b2e5f0409f2ba219556e71b2ab1fdaa945a](https://sepolia.etherscan.io/address/0x9e929b2e5f0409f2ba219556e71b2ab1fdaa945a)
- How to create values that go into create
  - [https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L133-L145](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L133-L145)
```solidity
/// @notice Creates a new DisputeGame proxy contract.
/// @param _gameType The type of the DisputeGame - used to decide the proxy implementation.
/// @param _rootClaim The root claim of the DisputeGame.
/// @param _extraData Any extra data that should be provided to the created dispute game.
/// @return proxy_ The address of the created DisputeGame proxy.
function create(
    GameType _gameType,
    Claim _rootClaim,
    bytes calldata _extraData
)
    external
    payable
    returns (IDisputeGame proxy_)
```
  - rootClaim 값 계산 : L2Block의 정보를 이용해서 계산 (출처 :  [https://specs.optimism.io/protocol/proposals.html](https://specs.optimism.io/protocol/proposals.html))
```solidity
const bytes32zero = "0x0000000000000000000000000000000000000000000000000000000000000000"
const outputRoot = ethers.solidityPackedKeccak256(
    ["bytes32", "bytes32", "bytes32", "bytes32"],
    [
      bytes32zero,
      blockInfo.stateRoot,
      blockInfo.withdrawalsRoot,
      blockInfo.hash
    ]
);
```
  - extraData값 계산 : extraData는 rootClaim을 만드는 l2block의 Number로 계산됩니다.
```solidity
const extraData = ethers.AbiCoder.defaultAbiCoder().encode(
   ["uint64"],
   [latestBlockNumber]
);
```
- 예전에는 L2OutputOracle.sol이 존재해서 여기서 rootClaim값을 받아올 수 있었지만 현재는 더이상 L2OutputOracle.sol이 지원되지 않아서 rootClaim값을 얻기위해서는 block의 stateRoot, withdrawalsRoot, hash값을 알아야합니다.
- L2block에 대한 stateRoot, hash값은 optimism-etherscan에서 찾을 수 있지만 withdrawalsRoot는 제공하지 않음, 공식적인 Optmism-sepolia Node에 호출했을때는 whiteList 검사를 하여서 호출을 못하게 해놓았음
- withdrawalsRoot값을 얻기 위해서는 node를 실제로 실행하여서 해당 블록의 값을 가지고 올 수 있습니다.
- Optimism-Sepolia Node를 로컬에서 연동해서 테스트 진행하였음.
- 테스트 결과
  - 실제 rootClaim값
![](images/49e4b4b38b48.png)
  - block데이터공식을 이용해서 rootClaim을 만듬
![](images/a9a67d7c6b61.png)
- 남은 테스트를 하기 위한 문제점
  1. M4에서는 Optimism에서 제공하는 Docker실행이 제대로 되지않아서 intel환경에서 Docker를 실행해야함
  1. 현재 Node 연결해서 rootClaim값을 만드는 테스트까지는 성공하였음
  1. 그러나 Node 용량 부족으로 현재 sync에러가 나서 추가 테스트를 위해서 용량을 추가할 수 있는 기기를 구입함 (**용량을 추가해야 테스트가 가능함**)
![](images/d9b0dfa67d9e.png)

## **5. 실제 Sepolia에 TON으로 변경된 DisputeGame 개발전 Contract값 및 함수들 확인**

1. 어떻게 DisputeGameFactory에서 DisputeGame주소를 세팅하고 초기 Bond 가격을 세팅하는가?
  1. setImplementation ([https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L266-L269](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L266-L269))
```solidity
 function setImplementation(GameType _gameType, IDisputeGame _impl) external onlyOwner {
    gameImpls[_gameType] = _impl;
    emit ImplementationSet(address(_impl), _gameType);
}

```
  1. setInitBond ([https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L275-L278](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L275-L278))
```solidity
function setInitBond(GameType _gameType, uint256 _initBond) external onlyOwner {
    initBonds[_gameType] = _initBond;
    emit InitBondUpdated(_gameType, _initBond);
}
```
1. 어떻게 DisputeGameFactory에서 DisputeGame Contract를 만들때 값들을 세팅하는가?
  1. DisputeGame Contract에 미리 세팅해놓고 clone함수를 이용해서 해당 Contract를 배포하여서 세팅값을 따로 진행하지 않아도 세팅이 되도록 하였음([https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L170](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol#L170))
```solidity
proxy_ = IDisputeGame(address(impl).clone(abi.encodePacked(msg.sender, _rootClaim, parentHash, _extraData)));

```
  1. constructor에서 세팅된 고정값들 
    1. GAME_TYPE
```solidity
function gameType() public view returns (GameType gameType_) {
    gameType_ = GAME_TYPE;
}
```
    1. ABSOLUTE_PRESTATE
```solidity
/// @notice Returns the absolute prestate of the instruction trace.
function absolutePrestate() external view returns (Claim absolutePrestate_) {
    absolutePrestate_ = ABSOLUTE_PRESTATE;
}
```
    1. MAX_GAME_DEPTH
```solidity
/// @notice Returns the max game depth.
function maxGameDepth() external view returns (uint256 maxGameDepth_) {
    maxGameDepth_ = MAX_GAME_DEPTH;
}
```
    1. SPLIT_DEPTH
```solidity
/// @notice Returns the split depth.
function splitDepth() external view returns (uint256 splitDepth_) {
    splitDepth_ = SPLIT_DEPTH;
}
```
    1. CLOCK_EXTENSION
```solidity
/// @notice Returns the clock extension constant.
function clockExtension() external view returns (Duration clockExtension_) {
  clockExtension_ = CLOCK_EXTENSION;
}
```
    1. MAX_CLOCK_DURATION
```solidity
/// @notice Returns the max clock duration.
function maxClockDuration() external view returns (Duration maxClockDuration_) {
    maxClockDuration_ = MAX_CLOCK_DURATION;
}
```
    1. VM
```solidity
/// @notice Returns the address of the VM.
function vm() external view returns (IBigStepper vm_) {
    vm_ = VM;
}
```
    1. WETH
```solidity
/// @notice Returns the WETH contract for holding ETH.
function weth() external view returns (IDelayedWETH weth_) {
    weth_ = WETH;
}
```
    1. ANCHOR_STATE_REGISTRY
```solidity
/// @notice Returns the anchor state registry contract.
function anchorStateRegistry() external view returns (IAnchorStateRegistry registry_) {
    registry_ = ANCHOR_STATE_REGISTRY;
}
```
    1. L2_CHAIN_ID
```solidity
/// @notice Returns the chain ID of the L2 network this contract argues about.
function l2ChainId() external view returns (uint256 l2ChainId_) {
    l2ChainId_ = L2_CHAIN_ID;
}
```
  1. 실제 Sepolia에 세팅된 값
    1. GAME_TYPE = 0
    1. ABSOLUTE_PRESTATE = 0x03eb07101fbdeaf3f04d9fb76526362c1eea2824e4c6e970bdb19675b72e4fc8
    1. MAX_GAME_DEPTH = 73
    1. SPLIT_DEPTH = 30
    1. CLOCK_EXTENSION = 10800
    1. MAX_CLOCK_DURATION = 302400
    1. VM = [0xA1B54D89e305bcd322Ba0C9C094093173C0d6b3a](https://sepolia.etherscan.io/address/0xA1B54D89e305bcd322Ba0C9C094093173C0d6b3a)
    1. WETH = [0xf8D7B42e1aD39F0e321CF8bf913E0E4CD1C1F571](https://sepolia.etherscan.io/address/0xf8D7B42e1aD39F0e321CF8bf913E0E4CD1C1F571)
    1. ANCHOR_STATE_REGISTRY = [0xa1Cec548926eb5d69aa3B7B57d371EdBdD03e64b](https://sepolia.etherscan.io/address/0xa1Cec548926eb5d69aa3B7B57d371EdBdD03e64b)
    1. L2_CHAIN_ID = 11155420
  1. abi.encodePacked된 값들 가져오는 방법
    1. msg.sender
```solidity
/// @notice Getter for the creator of the dispute game.
/// @dev `clones-with-immutable-args` argument #1
/// @return creator_ The creator of the dispute game.
function gameCreator() public pure returns (address creator_) {
    creator_ = _getArgAddress(0x00);
}
```
    1. _rootClaim
```solidity
/// @notice Getter for the root claim.
/// @dev `clones-with-immutable-args` argument #2
/// @return rootClaim_ The root claim of the DisputeGame.
function rootClaim() public pure returns (Claim rootClaim_) {
    rootClaim_ = Claim.wrap(_getArgBytes32(0x14));
}
```
    1. parentHash
```solidity
/// @notice Getter for the parent hash of the L1 block when the dispute game was created.
/// @dev `clones-with-immutable-args` argument #3
/// @return l1Head_ The parent hash of the L1 block when the dispute game was created.
function l1Head() public pure returns (Hash l1Head_) {
    l1Head_ = Hash.wrap(_getArgBytes32(0x34));
}
```
    1. _extraData
```solidity
/// @notice Getter for the extra data.
/// @dev `clones-with-immutable-args` argument #4
/// @return extraData_ Any extra data supplied to the dispute game contract by the creator.
function extraData() public pure returns (bytes memory extraData_) {
    // The extra data starts at the second word within the cwia calldata and
    // is 32 bytes long.
    extraData_ = _getArgBytes(0x54, 0x20);
}
```
  1. clone함수는 대표적으로 Solady와 OpenZeppelin에서 제공
    1. Solady의 장점
      1. 더 최적화된 바이트코드 (가스비 절약)
      1. 더 작은 런타임코드 (메모리 사용량 감소)
    1. OpenZeppelin의 장점
      1. 안정성 : 수많은 프로젝트에서 사용이 되어서 안정적인 것이 확인됨
      1. 사용편의함 : 복잡한 설정이 불편하고 사용방법에 대한 문서가 제공됨
  1. Optimism은 가스 효율성을 위해서 Solady Clone방법을 사용하는 것으로 보입니다.
    1. 실제 create로 DisputeGameContract가 생성된 tx ([https://sepolia.etherscan.io/tx/0x8ce341276d3a9f8e6d91100bf27e134afc998da7df78dec019ac77229ae0b69c](https://sepolia.etherscan.io/tx/0x8ce341276d3a9f8e6d91100bf27e134afc998da7df78dec019ac77229ae0b69c))
1. 어떻게 Attack이나 Defend를 진행할때 필요한 추가 Bond값을 계산하는가?
  1. getRequiredBond ([https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L909-L950](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L909-L950))
```solidity
function getRequiredBond(Position _position) public view returns (uint256 requiredBond_) {
    uint256 depth = uint256(_position.depth());
    if (depth > MAX_GAME_DEPTH) revert GameDepthExceeded();

    // Values taken from Big Bonds v1.5 (TM) spec.
    uint256 assumedBaseFee = 200 gwei;
    uint256 baseGasCharged = 400_000;
    uint256 highGasCharged = 300_000_000;

    // Goal here is to compute the fixed multiplier that will be applied to the base gas
    // charged to get the required gas amount for the given depth. We apply this multiplier
    // some `n` times where `n` is the depth of the position. We are looking for some number
    // that, when multiplied by itself `MAX_GAME_DEPTH` times and then multiplied by the base
    // gas charged, will give us the maximum gas that we want to charge.
    // We want to solve for (highGasCharged/baseGasCharged) ** (1/MAX_GAME_DEPTH).
    // We know that a ** (b/c) is equal to e ** (ln(a) * (b/c)).
    // We can compute e ** (ln(a) * (b/c)) quite easily with FixedPointMathLib.

    // Set up a, b, and c.
    uint256 a = highGasCharged / baseGasCharged;
    uint256 b = FixedPointMathLib.WAD;
    uint256 c = MAX_GAME_DEPTH * FixedPointMathLib.WAD;

    // Compute ln(a).
    // slither-disable-next-line divide-before-multiply
    uint256 lnA = uint256(FixedPointMathLib.lnWad(int256(a * FixedPointMathLib.WAD)));

    // Computes (b / c) with full precision using WAD = 1e18.
    uint256 bOverC = FixedPointMathLib.divWad(b, c);

    // Compute e ** (ln(a) * (b/c))
    // sMulWad can be used here since WAD = 1e18 maintains the same precision.
    uint256 numerator = FixedPointMathLib.mulWad(lnA, bOverC);
    int256 base = FixedPointMathLib.expWad(int256(numerator));

    // Compute the required gas amount.
    int256 rawGas = FixedPointMathLib.powWad(base, int256(depth * FixedPointMathLib.WAD));
    uint256 requiredGas = FixedPointMathLib.mulWad(baseGasCharged, uint256(rawGas));

    // Compute the required bond.
    requiredBond_ = assumedBaseFee * requiredGas;
}
```
  1. 게임의 깊이에 따라 가스 비용을 증가시키기 위해서 배율(Multiplier)를 구한뒤 maxGas를 계산합니다. (게임의 깊이가 깊어질수록 계산 복잡도가 증가해서 가스 비용도 이에 맞게 증가하도록 설계되어있음)
    1. Multiplier 공식
![](images/f2695f2e9751.png)
    1. 식 변환 가능 (이 식을 활용해서 multiplier 계산)
![](images/dee0537ccfa5.png)
    1. 최종 계산식
![](images/3606d3d04d40.png)
  1. 우리는 어떻게 할 것인가? 
    1. TON으로 변경함 → 어떻게?
    1. 해당 공식을 그대로 사용 (현재는 이렇게 진행)
1. DisputeGame 전체과정 이해
  1. 전체 함수들의 역할
| **단계** | **목적** | **결과** |
| --- | --- | --- |
| Create | rootClaim 제출 | 검토할 블록 범위 설정 |
| Attack/Defend | 이분법 진행 | 점진적 범위 축소 |
| Step | 최종 검증 | 단일 명령어 확인 |
| Resolve | 승부 결정 | 본드 분배 |
  1. 시나리오 설정
    - **Alice** (Proposer): L2 상태를 제출하는 정직한 사용자
      - Alice는 블록 1005번을 잘못 계산하여서 해당 값 때문에 L2상태가 다르자 Create를 생성함
    - **Bob** (Challenger): Alice의 제출이 틀렸다고 생각하는 사용자
    - **Charlie** (Observer): 게임을 지켜보는 제3자
    - **L2 블록 범위**: 1000~1008 (총 8개 블록)

**1. 게임 생성 (Create) (Alice)**

  1. **첫 번째 도전 (ATTACK) (Bob)**
    - Bob이 자신의 노드로 블록 1000~1008을 재계산해보니 Alice가 제출한 결과와 값이 다름! → Bob의 Attack
```solidity
// Bob이 FaultDisputeGame.attack() 호출
attack(
    parentIndex: 0,                 // rootClaim 공격
    claim: 0xCCC...DDD             // "중간 지점(블록 1004)의 상태"
) payable { value: 0.088 ether }   // 본드 10% 증가

// Bob의 주장: "블록 1004까지는 상태가 0xCCC...DDD인데, 
//             Alice의 최종 결과 0xAAA...BBB는 틀렸다!"
```
    - 게임상태
```solidity
First Attack! 
├─ Alice Claim: 블록 1000~1008 → 0xAAA...BBB
├─ Bob Attack: 블록 1000~1004 → 0xCCC...DDD
├─ 이분법 시작: [1000~1004] vs [1005~1008]
└─ Bob 본드: 0.088 ETH
```
  1. **새로운 Attack  (Alice)**
    - Alice는 Bob의 1004번까지의 블록 계산은 맞다고 생각하지만 1005~1008번에 틀린 것이 있다고 생각
```solidity
// Alice가 Bob의 클레임에 대해 새로운 attack!
attack(
    parentIndex: 1,                 // Bob의 클레임 공격
    claim: 0x555...666             // "1006 블록까지의 상태"
) payable { value: 0.097 ether }
```
    - 게임상태
```solidity
Attack! 
├─ 범위가 더 좁혀짐: 블록 1005~1008
├─ Alice: 0x555...666
└─ Alice 본드: 0.097 ETH

Before:
Root(Alice): 1000~1008 → 0xAAA...BBB
├─ Bob Attack: 1000~1004 → 0xCCC...DDD

After Alice's Strategic Move:
Root(Alice): 1000~1008 → 0xAAA...BBB  
├─ Bob: 1000~1004 → 0xCCC...DDD
│   └─ Alice Attack: 1005~1008 범위로 이동!
```
  1. **Alice의 Attack에 대한 Defend (Bob)**
    - Bob은 Alice가 1000~1004에는 문제 없다는것을 인정하고 1005~1008번에 찾자는 의도를 알고 1006번에 대한 claim으로 공격함
```solidity
defend(
    parentIndex: 2,
    claim: 0x777...888             // "내가 생각하는 1006 상태"
) payable { value: 0.097 ether }
```
    - 게임 상태
```solidity
현재 게임 상태:
├─ 1000~1004: Bob이 맞음 (Alice 동의)
└─ 1005~1008: Alice vs Bob 대결 중
    ├─ 1005~1006: Alice(0x555...666) vs Bob(0x777...888)
    └─ 1007~1008: 아직 미정
```
  1. **Alice의 재공격**
    - 둘의 값이 다르니 1005번부터 확인
```solidity
attack(
    parentIndex: 3,                 // Bob의 defend 공격
    claim: 0x333...444             // "1005 블록 상태"
) payable { value: 0.107 ether }   // 본드 계속 증가

// Alice의 주장:
// "그럼 1005 블록 하나만 보자. 내 계산으론 0x333...444야!"
```
    - 게임 상태
```solidity
단일 블록 도달! 
├─ 블록 1005: Alice(0x333...444) 주장
└─ 나머지: 아직 미정
```
  1. **Bob의 반박**
    - Bob의 1005번 값 제출
```solidity
defend(
    parentIndex: 4,                 // Alice의 1005 블록 주장
    claim: 0x999...AAA             // "진짜 1005 블록 상태"
) payable { value: 0.107 ether }

// Bob의 주장:
// "1005 블록 상태는 0x999...AAA가 정답이야!"
```
    - 게임상태
```solidity
블록 내부 진입! 
├─ 블록 1005: Alice(0x333...444) vs Bob(0x999...AAA)
└─ 이제 트랜잭션 레벨로 들어감
```
  1. **Alice의 Attack (이제 트랜잭션 레벨로 들어가서 확인)**
    - Alice의 1005번 블록의 첫번째 트랜잭션 상태 제출
```solidity
attack(
    parentIndex: 5,                 // Bob의 1005 블록 defend
    claim: 0xBBB...CCC             // "1005 블록의 트랜잭션 1 상태"
) payable { value: 0.118 ether }

// Alice의 주장:
// "1005 블록의 트랜잭션 1까지는 0xBBB...CCC야!"
```
  1. **Bob의 defend**
    - Bob의 1005번 블록의 첫번째 트랜잭션 상태 제출
```solidity
defend(
    parentIndex: 6,                 // Alice의 트랜잭션 1 주장
    claim: 0xDDD...EEE             // "진짜 트랜잭션 1 상태"
) payable { value: 0.118 ether }

// Bob의 주장:
// "트랜잭션 1 상태는 0xDDD...EEE가 맞아!"
```
    - 게임상태
```solidity
트랜잭션 내부! ⚡
├─ 블록 1005, 트랜잭션 1: Alice vs Bob
└─ 곧 MIPS 명령어 레벨 도달
```
  1. **최종 STEP 검증**
    - **Bob의 함수 호출**
```solidity
// 게임이 MAX_GAME_DEPTH (73레벨)에 도달
// Bob이 최종 검증 실행

step(
    claimIndex: 7,                  // 마지막 클레임 인덱스
    isAttack: true,                 // 공격 형태
    stateData: "0x4A6F686E...",    // 이전 MIPS 상태
    proof: "0x7B2274797065..."      // 메모리 증명
)

// 내부적으로 MIPS.sol 실행:
// 1005 블록, 트랜잭션 1, 명령어 #247 실행
```
    - **MIPS.sol의 판정**
```solidity
// MIPS 가상머신에서 실제 명령어 실행
// 예: "LOAD R1, 0x1000"

function step(bytes stateData, bytes proof, bytes32 context) 
    returns (bytes32) {
    
    // 실제 MIPS 명령어 실행
    bool validStep = VM.step(_stateData, _proof, uuid.raw()) == postState.claim.raw();
    
    return keccak256(newState); // 0xDDD...EEE 반환
}
```
    - 결과 비교
```solidity
MIPS.sol 실행 결과: 0xDDD...EEE
Alice의 주장: 0xBBB...CCC  ❌ (틀림!)
Bob의 주장: 0xDDD...EEE   ✅ (정답!)

→ Bob 승리 확정! 🏆
```
  1. **게임 종료**
    - 게임종료 함수 호출
```solidity
// 아무나 호출 가능 게임 종료
resolve()

// 내부 로직:
// - step()에서 Alice가 반박당함
// - Alice의 claimData[6].counteredBy = Bob
// - 루트까지 거슬러 올라가서 Bob 승리 확정
```
    - 크레딧 청구
```solidity
// Bob이 승리 보상 청구
claimCredit(Bob.address)

// Bob 획득 본드:
// 0.08 + 0.097 + 0.097 + 0.107 + 0.107 + 0.118 + 0.118 = 약 0.724 ETH
// (gas비 제외하고 약 0.6 ETH 순수익)
```

## Sepolia 테스트

[[TONDisputeGameFactory, TONDisputeGame Contract 배포 및 테스트 (Sepolia)]]