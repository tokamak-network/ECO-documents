The amount of seigniorage issued must be subtracted from the total issuance used in calculating seigniorage distribution.

시뇨리지 분배 계산시 사용되는 총 발행량에서 발급된 시뇨리지 금액을 빼고, 스테이킹된 비율을 계산해야 한다.  

시뇨리지 계산  : [https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/stake/managers/SeigManagerV1_3.sol#L548-L556](https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/stake/managers/SeigManagerV1_3.sol#L548-L556)

```shell
// 1. increase total supply of {tot} by maximum seigniorages * staked rate
//    staked rate = total staked amount / total supply of (W)TON
uint256 prevTotalSupply = _tot.totalSupply();

uint256 span = block.number - _lastSeigBlock;
if (_unpausedBlock > _lastSeigBlock) span -= (_unpausedBlock - _pausedBlock);

// maximum seigniorages
uint256 maxSeig = span * _seigPerBlock;

// total supply of (W)TON , https://github.com/tokamak-network/TON-total-supply
uint256 tos = _totalSupplyOfTon(block.number);

**// maximum seigniorages * staked rate
****uint256 stakedSeig = FullMath.rdiv(
  FullMath.rmul(
      maxSeig,
      // total staked amount
      prevTotalSupply
  ),
  tos
);**
```

- tos: 총 톤 공급량 [https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/stake/managers/SeigManagerV1_3.sol#L687-L699](https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/stake/managers/SeigManagerV1_3.sol#L687-L699)
  - 총공급량의 계산은 블록당 발행되는 시뇨리지를 기준으로 계산되었다. 
  - 현재 블록에서의 총공급량은 현재까지 발행된 시뇨리지까지를 포함하여 계산된다. 

```shell
function _totalSupplyOfTon(uint256 blockNumber) internal view returns (uint256 tos) {
    uint256 startBlock = (seigStartBlock == 0 ? SEIG_START_MAINNET : seigStartBlock);
    uint256 initial = (
        initialTotalSupply == 0 ? INITIAL_TOTAL_SUPPLY_MAINNET : initialTotalSupply
    );
    uint256 burntAmount = (burntAmountAtDAO == 0 ? BURNT_AMOUNT_MAINNET : burntAmountAtDAO);
    uint256 OneAddressBalance = ITON(_ton).balanceOf(address(1));
    tos =
        initial +
        (_seigPerBlock * (blockNumber - startBlock)) -
        ( OneAddressBalance * GWEI_UNIT) -
        burntAmount;
}

```

- stakedSeig :  먼저 스테이커에게 나눠주는 시뇨리지중에 스테이킹비율에 따른 시뇨리지를 계산할때, 
  - 비율은 total staked amount/ tos 로 계산하였는데, 이 tos안에 분배해야 하는 시뇨리지 부분도 포함된것이 적절하지 않다는 의견입니다. 
  - 따라서, 비율을  **total staked amount/ ****(tos - 지금분배해야하는시뇨리지양) **과 같이 비율을 정할때, 지금 발행되는시뇨리지는 아직 분배가 되지 않은 양이므로, 그 안에는 스테이커가 받아야 할 양도 포함되어 있는데, 아직 받지 않았으므로, 해당 금액을 제하고 비율을 정해야 정확하다는 의견 

## 결론

위 기능이 모든 스테이커에게 공통으로 적용된 점.

위 내용으로 인해, 스테이커가 받을수도 잇었던 물량이 다오에게 갔을것이라는 점을 공유하고 인지했습니다.

그런데, 위 내용을 수정하게 된다면,

유통량이 늘어나게 되고(실제 발급량을 의미하는 것이아니고, 시장에 풀릴수있는 물량이 늘어나게 된다는 의미) 이는 토카막 생태계에는 더 좋은 영향을 주게 되지는 않는다는 점을 고려했을때 코드 수정은 하지 않기로 했습니다.

만약 위의 내용으로 스테이커가 손해를 보았다는 생각으로 불합리하다는 의견이 있다면,

다오 아젠다를 통해 시뇨리지를 더 가져갈수있는 안건을 내는것이 더 좋은 방향인 것 같다고 의견이 모아졌습니다. 