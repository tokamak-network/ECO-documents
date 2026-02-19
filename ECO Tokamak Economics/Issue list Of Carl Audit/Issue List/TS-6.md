TS-6 - Implementation function conflict (SeigManagerV1_3,

SeigManagerV1_2)

ID Type Severity Location Status

TS-6

Volatile

Code

Medium

contracts/stake/managers/SeigManagerV1_2.sol#L429

contracts/stake/managers/SeigManagerV1_2.sol#L510

contracts/stake/managers/SeigManagerV1_2.sol#L564

contracts/stake/managers/SeigManagerV1_2.sol#L568

contracts/stake/managers/SeigManagerV1_2.sol#L606

contracts/stake/managers/SeigManagerV1_2.sol#L614

contracts/stake/managers/SeigManagerV1_2.sol#L628

contracts/stake/managers/SeigManagerV1_3.sol#L224

contracts/stake/managers/SeigManagerV1_3.sol#L347

contracts/stake/managers/SeigManagerV1_3.sol#L380

contracts/stake/managers/SeigManagerV1_3.sol#L384

contracts/stake/managers/SeigManagerV1_3.sol#L388

contracts/stake/managers/SeigManagerV1_3.sol#L397

contracts/stake/managers/SeigManagerV1_3.sol#L697

Pendi

ng

**Description**

SeigManagerV1_3 컨트랙트는 SeigManagerProxy 컨트랙트의 로직 컨트랙트 중 하나로

SeigManagerV1_2 컨트랙트와 함께 사용됩니다. SeigManagerProxy 컨트랙트는 일부 함수들에 대해서

만 SeigManagerV1_3 컨트랙트를 로직 컨트랙트로 사용하기 때문에, 다른 로직 컨트랙트에서 구현할 필요가

없습니다.

특히 동일한 함수를 다르게 구현할 경우 컨트랙트 배포 시 가스 소비가 늘어날 뿐만 아니라 코드의 가독성을 떨어

뜨리며 실제 구현 컨트랙트를 찾기 힘들어 프록시 컨트랙트 관리에 어려움이 있습니다.

**Recommendation**

중복 구현된 external 함수는 하나의 로직 컨트랙트에서만 구현하십시오. 만약 인터페이스를 맞추기 위해서 함수

를 삭제할 수 없다면 revert("implemented in SeigManagerV1_3") 와 같은 방식으로 함수가 실행되지 않

음을 컨트랙트 소스 코드에 명시할 수 있습니다.

## Feedback

- SeigManagerProxy 의 프록시 설명에 따라 프록시에서는 함수별 로직을 관리하고, 함수에 정해진 로직이 없다면 인덱스0번의 로직을 사용합니다. 

 

- [SeigManagerV1_2](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readContract#F21) 는 현재 상용서비스에서 사용중인 로직이므로, [SeigManagerV1_2 코드 변경은](https://etherscan.io/address/0x8813C76858C2fc048B14Bd4c75F2Daee43c79958#code) 불가합니다. 
- SeigManagerV1_3 는 SeigManagerV1_2 에서 수정해야 할 함수나 추가해야 하는 함수로 구성하였습니다. 
  - contracts/stake/managers/SeigManagerV1_3.sol#L224  updateSeigniorage()
    - 코드 변경됨 
  - contracts/stake/managers/SeigManagerV1_3.sol#L347 getOperatorAmount(address layer2) 
    - external 로 코드 변경되어 SeigManagerV1_3 에 추가함. 
  - contracts/stake/managers/SeigManagerV1_3.sol#L380 unallocatedSeigniorage() 
    - 코드 변경됨  
  - contracts/stake/managers/SeigManagerV1_3.sol#L384 unallocatedSeigniorageAt(uint256 snapshotId)
    - stakeOfAllLayersAt 함수가 변경됨에 따라,  stakeOfAllLayersAt 함수를 사용하고 있어서 같이 배포함. 
  - contracts/stake/managers/SeigManagerV1_3.sol#L388 stakeOfAllLayers()
    - 코드 변경됨 
  - contracts/stake/managers/SeigManagerV1_3.sol#L397 stakeOfAllLayersAt(uint256 snapshotId)
    - 코드 변경됨 
  - contracts/stake/managers/SeigManagerV1_3.sol#L697 totalSupplyOfTon()
    - 변경된 다른 함수에서 사용해서, 같이 배포함.  
-  다오를 통한 seigManagerProxy 업그레이드 
  ([8.dao-staking-v2.5.deployments.sepolia.test.ts: L572:L609](https://github.com/tokamak-network/ton-staking-v2/blob/e0bc94c28817c76c0e63a4de6a56231f96a6fda7/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L572-L610)) 을 보시면,  다오를 통해 seigManagerProxy 를 업그레이드 할때,  추가 및 변경된 함수를 SeigManagerV1_3 로직으로 지정하여 배포할 것입니다. 

```typescript
// =========================================
//  upgrade SeigManager setTargetSetSelectorImplementations2
targets.push(seigManagerProxy.address)

const selector1 = encodeFunctionSignature("setLayer2StartBlock(uint256)");
const selector2 = encodeFunctionSignature("setLayer2Manager(address)");
const selector3 = encodeFunctionSignature("setL1BridgeRegistry(address)");
const selector4 = encodeFunctionSignature("updateSeigniorage()");
const selector5 = encodeFunctionSignature("updateSeigniorageOperator()");
const selector6 = encodeFunctionSignature("updateSeigniorageLayer(address)");
const selector7 = encodeFunctionSignature("allowIssuanceLayer2Seigs(address)");
const selector8 = encodeFunctionSignature("totalLayer2TVL()");
const selector9 = encodeFunctionSignature("layer2RewardInfo(address)");
const selector10 = encodeFunctionSignature("l1BridgeRegistry()");
const selector11 = encodeFunctionSignature("layer2Manager()");
const selector12 = encodeFunctionSignature("layer2StartBlock()");
const selector13 = encodeFunctionSignature("l2RewardPerUint()");
const selector14 = encodeFunctionSignature("unSettledReward(address)");
const selector15 = encodeFunctionSignature("estimatedDistribute(uint256,address,bool)");
const selector16 = encodeFunctionSignature("excludeFromSeigniorage(address)");
 const selector17 = encodeFunctionSignature("unallocatedSeigniorage()");
const selector18 = encodeFunctionSignature("unallocatedSeigniorageAt(uint256)");
const selector19 = encodeFunctionSignature("stakeOfAllLayers()");
const selector20 = encodeFunctionSignature("stakeOfAllLayersAt(uint256)");

let functionBytecodes = [
    selector1, selector2, selector3, selector4, selector5,
    selector6, selector7, selector8, selector9, selector10,
    selector11, selector12, selector13, selector14, selector15,
    selector16,selector17, selector18, selector19, selector20
];

callDtata = seigManagerProxy.interface.encodeFunctionData("**setSelectorImplementations2**",
    [
        functionBytecodes,
        seigManagerV1_3.address
    ])
params.push(callDtata)

```

[ton-staking-v2/docs/developer-guide/contracts/SeigManagerProxy.md at SMV-02 · tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2/blob/SMV-02/docs/developer-guide/contracts/SeigManagerProxy.md#seigmanagerproxy)