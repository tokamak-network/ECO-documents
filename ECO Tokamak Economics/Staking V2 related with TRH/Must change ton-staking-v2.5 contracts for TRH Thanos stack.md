## (1) DepositManagerV1_1.sol 

### will be modified withdrawAndDepositL2 

If l2Type = 2, use IL1Bridge(l1Bridge).bridgeNativeTokenTo instead of IL1Bridge(l1Bridge).depositERC20To.

```
 ~~function bridgeERC20To(
        address _localToken,
        address _remoteToken,
        address _to,
        uint256 _amount,
        uint32 _minGasLimit,
        bytes calldata _extraData
    )
        public~~

function bridgeNativeTokenTo(
        address _to,
        uint256 _amount,
        uint32 _l2Gas,
        bytes calldata _data
  )
        public
```

## (2) How to get the address that receives the seigniorage in on-chain?

Currently, we gave seigniorage to the owner of SystemConfig ( SystemConfig.owner() ) .

In Thanos stack, SystemConfig.owner() = 0x000000000000000000000000000000000000dEaD, so this cannot be used.

When an operator changes, it should be possible to query the operator on-chain.

### (3) 너무 느린 조회함수(전체 레이어의 총 스테이크량, 특정 계정의 총 스테이크량 ) 발생 가능성 있음.  

- 증상
  - SeigManager.**stakeOf(address account) **특정계정이 스테이크 한 톤 물량 
  - 특정 계정이 전체 레이어에 스테이크한 톤을 조회할때, 모든 레이어를 For문으로 조회합니다. 따라서 레이어가 너무 많은 경우, 조회 함수가 동작이 너무 느려질 수 있다. 
- 원인
  - TRH의 On-Demand L2 사용자가 늘어나서 레이어2가 계속해서 늘어날수 있습니다.
  - Layer2Registry.register(address layer2) 함수의 계속적인 호출로, 레이어가 늘어날 수 있다. → 악의 적인 공격 
- 결과
  - 시뇨리지 로직에는 문제가 되지 않는다. 
  - 레이어가 너무 많이 생겨나면 위의 스테이킹 조회함수를 사용할 수 없을 수 있다. → 이때는 Off 체인에서 모든 레이어의 스테이크양을  조회해서, 총 스테이킹 물량을 확인해야 한다. 
- 이 부분을 개선해야 한다면
  - 레이어의 최대 개수 정해서, 최대 개수 이상 레이어가 생성되지 않게 해야 하는지  →  서비스의 제한이 될 수도 있다. 서비스 제한이 된다면, 개수 제한 보다는 총 스테이크 량을 오프체인에서 조회하게 하는 편이 나을것 같다. 
 
 

 

### (4) 문서 내용 변경 

- type = 2  를 optimism bedrock (with native TON) 으로 명시했는데, 이부분을 Tokamak Rollup Hub Thanos stack 으로 변경해야 함. 
- L2의 시뇨리지 받는 주소를 SystemConfig.operator() 로 조회한다고 명시해야 함. 
- 