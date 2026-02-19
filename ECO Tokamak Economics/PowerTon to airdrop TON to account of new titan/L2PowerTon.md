Contract calling L2DividendPoolForStos's distribute function to dividend the deposited token from L1. 

- If there is no universal stos balance in L2, the airdrop should not be executed.
- When airdropping native TON, use **`0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000`** in the erc20 address parameter.

## Repo  : 

[https://github.com/tokamak-network/l2-project-launch/tree/NT_4_L2PowerTon](https://github.com/tokamak-network/l2-project-launch/tree/NT_4_L2PowerTon)

[https://github.com/tokamak-network/ton-staking-v2/tree/NT_4_L2PowerTon](https://github.com/tokamak-network/ton-staking-v2/tree/NT_4_L2PowerTon)

테스트를 하려고 보니, ton-staking-v2 레포에서 해야 한다. 그래서 코드를 ton-staking-v2 옮겨왔고, 테스트는 l2-project-launch 의 에어드랍 볼트가 배포되어야 테스트가 가능하다. 테스트는 에어드랍 볼트 배포 후 진행한다. 

# Contract Name 

- L2PowerTon  

# Storage 

```javascript
address public l2DividendPoolForStos;
address public universalStos;

address constant NativeTonAddress = address(0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000);
```

# Events 

```javascript
 event Distributed(address indexed token, uint256 amount);
```

# ABI 

[https://github.com/tokamak-network/l2-project-launch/blob/NT_4_L2PowerTon/artifacts/contracts/L2/powerton/L2PowerTon.sol/L2PowerTon.json](https://github.com/tokamak-network/l2-project-launch/blob/NT_4_L2PowerTon/artifacts/contracts/L2/powerton/L2PowerTon.sol/L2PowerTon.json)

# Function 

## distribute(address token)

/// distribute the token that this contract is holding
/// @param token token address to dividend. 

```solidity
 function distribute(address token) public
```

[https://github.com/tokamak-network/l2-project-launch/blob/63b9e51919c5140a1b89b0212d9787c5e2075eac/contracts/L2/powerton/L2PowerTon.sol#L55-L77](https://github.com/tokamak-network/l2-project-launch/blob/63b9e51919c5140a1b89b0212d9787c5e2075eac/contracts/L2/powerton/L2PowerTon.sol#L55-L77)

문의 1.  L1에서 distribute(**`0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000`**) 을 호출할것인데 , 실행조건이 맞지 않는 경우, 예를 들어, 잔액이 부족한 경우, 또는 IUniversalStos(universalStos).totalSupply() 가 0 인경우(stos 가 없는경우) 에는 revert되도록 해야 하는지 또는 트랜잭션이 실행되도록 해야 하는지 여부 

# Test 

1. L1에서 stos 를 L2로 등록한다. L2의 universal stos를 통해 stos 잔액을 조회할 수 있다. 
1. simple stake 서비스에서 업데이트 시뇨리지를 실행한다. 파워톤에 시뇨리지가 쌓인다. 
1. L1 powerton에서 distribute를 실행한다.  
  1.  L2DividendPoolForStos를 통해 에어드랍받은 금액을 클래임 할 수 있다. 
1. L2 powerton에 금액을 보내고, distribute를 실행하면, L2DividendPoolForStos를 통해 에어드랍받을 수 있다. 