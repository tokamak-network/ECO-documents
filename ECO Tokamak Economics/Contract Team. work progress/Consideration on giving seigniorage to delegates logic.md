# 시뇨리지 발행 설정 옵션 

1. 오퍼레이터는 commissionRate 을 설정하여, 발생되는 시뇨리지 중 일부를 오퍼레이터가 받을 수 있다.
  1.  isCommissionRateNegative_ == false && commissionRate == RAY 인 경우, 
    1.  오퍼레이터가 별도로 가져가는 시뇨리지는 없다. 
  1. isCommissionRateNegative_ == false && commissionRate > RAY 인 경우, 
    1. 해당 레이어에 발행되는 시뇨리지의 commissionRate 만큼의 시뇨리지양을 오퍼레이터가 가져간다. 
1.  오퍼레이터는 commissionRate 을 설정하여, **오퍼레이터가 스테이킹해서 발생하는 시뇨리지 중 commissionRate 만큼의 시뇨리지를  해당 레이어에 스테이킹하고 있는 스테이커(delegator)에게 나눠준다. **
  1. 현재 코드  [link](https://github.com/tokamak-network/ton-staking-v2/blob/c1f9d40570c59de18868bd735e41e9c46ea496bb/contracts/stake/managers/SeigManager.sol#L604-L671)
```javascript
function _calcSeigsDistribution(
    address layer2,
    RefactorCoinageSnapshotI coinage,
    uint256 prevTotalSupply,
    uint256 seigs,
    bool isCommissionRateNegative_,
    address operator
  ) internal returns (
    uint256 **nextTotalSupply**,
    uint256 operatorSeigs
  ) {
    if (block.number >= delayedCommissionBlock[layer2] && delayedCommissionBlock[layer2] != 0) {
      _commissionRates[layer2] = delayedCommissionRate[layer2];
      _isCommissionRateNegative[layer2] = delayedCommissionRateNegative[layer2];
      delayedCommissionBlock[layer2] = 0;
    }

    uint256 commissionRate = _commissionRates[msg.sender];

    **nextTotalSupply = prevTotalSupply + seigs;**

    // short circuit if there is no commission rate
    if (commissionRate == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    **// if commission rate is possitive
    if (!isCommissionRateNegative_) {
      operatorSeigs = rmul(seigs, commissionRate); // additional seig for operator
      nextTotalSupply = nextTotalSupply - operatorSeigs;
      return (nextTotalSupply, operatorSeigs);
    }**

    // short circuit if there is no previous total deposit (meanning, there is no deposit)
    if (prevTotalSupply == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    // See negative commission distribution formular here: TBD
    uint256 operatorBalance = coinage.balanceOf(operator);

    // short circuit if there is no operator deposit
    if (operatorBalance == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    uint256 operatorRate = rdiv(operatorBalance, prevTotalSupply);

    // ɑ: insufficient seig for operator
    operatorSeigs = rmul(
      rmul(seigs, operatorRate), // seigs for operator
      commissionRate
    );

    // β:
    uint256 **delegatorSeigs** = operatorRate == RAY
      ? operatorSeigs
      : rdiv(operatorSeigs, RAY - operatorRate);

    // 𝜸:
    **operatorSeigs** = operatorRate == RAY
      ? operatorSeigs
      : **operatorSeigs** + rmul(delegatorSeigs, operatorRate);

   ** nextTotalSupply = nextTotalSupply + delegatorSeigs;**

    return (nextTotalSupply, operatorSeigs);
  }
```
  1. 수정 요청 :  수정해야 한다고 생각한 이유 
_calcSeigsDistribution 함수의 파라미터중  uint256 prevTotalSupply, uint256 seigs 을 이용하여, 해당 레이어의 시뇨리지실행후의 총 잔액 nextTotalSupply 이 결정됩니다.   

prev total = 1000 , next total = 1100 

seig 100 , 

operator Rate 70%, delegator rate 30% 

커미션 10% 

operatorSeigs = rmul(
      rmul(seigs, operatorRate), // seigs for operator
      commissionRate
    ); 

Operator seig = seig * operator Rate  * 커미션 = 100 * 0.7* 0.1 = 7 

**delegator Seigs = 7 / 30% = 7* 10/3 = 70/3 =  23.33 **

**operatorSeigs** = operatorRate == RAY
      ? operatorSeigs
      : **operatorSeigs** + **rmul(delegatorSeigs, operatorRate)**;


**operatorSeigs = **7** + 23.33* 0.7 =   23.33 **

**nextTotalSupply = nextTotalSupply + delegatorSeigs;**

⇒ 검토결과 **operatorSeigs 와 delegatorSeigs 는 항상 값이 같게 나옴. 문제없음. **

  