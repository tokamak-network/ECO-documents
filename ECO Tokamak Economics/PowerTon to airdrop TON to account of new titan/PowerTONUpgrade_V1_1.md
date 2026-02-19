**파워톤 distribute 함수 실행시 파워톤이 가지고 있는 톤을  L2 의 L2DividendPoolStos 컨트랙으로 보낸다.** 

## Repo  : 

- Upgrade L1 PowerTon 
[https://github.com/tokamak-network/ton-staking-v2/blob/distribute-l2-powerTon/contracts/stake/powerton/PowerTONUpgrade_V1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/distribute-l2-powerTon/contracts/stake/powerton/PowerTONUpgrade_V1_1.sol)

# Contract Name 

PowerTONUpgrade_V1_1 

# Storage 

```javascript
address public l1CrossDomainMessage;
address public l1Bridge;
address public ton;

address public l2PowerTon;
address public l2Ton;

uint32 public depositMinGasLimit;
uint32 public sendMsgMinGasLimit;
```

# Events 

```javascript
event DistributedToL2(address l1Token, address l2Token, uint256 amount);
```

# Function 

## distribute() 

(1) 파워톤의 wton을 ton으로 스왑하고, 

(2) L1 bridge를 통해 L1PowerTon으로 톤을 보내고, 

(3) L1PowerTon에서 distribute하는 함수를 실행한다. 

```solidity
function distribute() external {
        _distributeToL2();
    }
```