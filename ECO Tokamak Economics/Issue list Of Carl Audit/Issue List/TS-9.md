TS-9 - Divide by zero

ID Type Severity Location Status

TS-9

Mathematica

l Operation

Minor

contracts/stake/managers/SeigManagerV1_3.sol#L289

contracts/stake/managers/SeigManagerV1_3.sol#L309

contracts/stake/managers/SeigManagerV1_3.sol#L328

contracts/stake/managers/SeigManagerV1_3.sol#L589

contracts/stake/managers/SeigManagerV1_3.sol#L617

contracts/stake/managers/SeigManagerV1_3.sol#L655

Pending

**Description**

언급된 코드는 잠재적으로 0으로 나눌 수 있습니다. 이 경우 EVM Panic (code=0x12)가 발생하며 컨트랙트

디버깅에 어려움이 있습니다.

**Recommendation**

제수(Divisor)가 0인 경우에 대한 예외 처리를 추가하십시오.

## Feedback

- 코드에서 사용되고 있는 tos 는 아래 함수의 리턴값으로 0이 나올 수 없습니다. 
  - SEIG_START_MAINNET , INITIAL_TOTAL_SUPPLY_MAINNET, _seigPerBlock 값이 변경되지 않을것이기 때문입니다. 
  - [SEIG_START_MAINNET](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F12)  : 10837698
  - [INITIAL_TOTAL_SUPPLY_MAINNET](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F5): 50000000000000000000000000000000000
  - [seigStartBlock](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F51) : 0
  - [initialTotalSupply](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F30): 0
  - [_seigPerBlock](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F50) : 3920000000000000000000000000

```solidity
function _totalSupplyOfTon(uint256 blockNumber) internal view returns (uint256 tos) {
        uint256 startBlock = (seigStartBlock == 0 ? SEIG_START_MAINNET : seigStartBlock);
        uint256 initial = (
            initialTotalSupply == 0 ? INITIAL_TOTAL_SUPPLY_MAINNET : initialTotalSupply
        );
        uint256 burntAmount = (burntAmountAtDAO == 0 ? BURNT_AMOUNT_MAINNET : burntAmountAtDAO);

        tos =
            initial +
            (_seigPerBlock * (blockNumber - startBlock)) -
            (ITON(_ton).balanceOf(address(1)) * (10 ** 9)) -
            burntAmount;
    }
}
```

- tos가 0이 아닐것이 확실하므로, 아래 함수들의 코드에서 잠재적으로 0으로 나누어지는 일은 없습니다. 
  - contracts/stake/managers/SeigManagerV1_3.sol#L289
```javascript
stakedSeig = rdiv(rmul(maxSeig, prevTotalSupply), tos);
```
  - contracts/stake/managers/SeigManagerV1_3.sol#L309
```javascript
l2TotalSeigs = rdiv(rmul(maxSeig, totalLayer2TVL * 1e9), tos);
```
  - contracts/stake/managers/SeigManagerV1_3.sol#L328
```javascript
 if (l2TotalSeigs != 0) tempL2RewardPerUint += ((l2TotalSeigs * 1e18) / totalLayer2TVL);
```
  - contracts/stake/managers/SeigManagerV1_3.sol#L589
```solidity
 uint256 stakedSeig = rdiv(
            rmul(
                maxSeig,
                // total staked amount
                prevTotalSupply
            ),
            tos
        );
```
  - contracts/stake/managers/SeigManagerV1_3.sol#L617
if (totalLayer2TVL != 0) l2TotalSeigs = rdiv(rmul(maxSeig, totalLayer2TVL * 1e9), tos);
- totalLayer2TVL 가 0이라면 l2TotalSeigs 가 0이 되기 때문에 아래 라인은 실행되지 않을것입니다. 
  - contracts/stake/managers/SeigManagerV1_3.sol#L655
```solidity
if (l2TotalSeigs != 0) l2RewardPerUint += ((l2TotalSeigs * 1e18) / totalLayer2TVL);
```