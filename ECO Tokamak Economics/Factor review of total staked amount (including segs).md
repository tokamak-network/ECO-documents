[https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit#gid=681869004](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit#gid=681869004)

Seignorage start (Seignorage contract deployment at block **10837698**) ([etherscan](https://etherscan.io/txs?a=0x710936500aC59e8551331871Cbad3D33d5e0D909&f=5#:~:text=0x4750dd10e22f993cea3052dfc9872ad4d25efa68cb21938ad429dd59b912b8b5))

- > seignorage minting logic (3.92 WTON per block): [github](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L714-L756)
- > seignorage per block (3.92 WTON, 10^27 decimal): [constructor argument (seig per block)](https://etherscan.io/address/0x710936500ac59e8551331871cbad3d33d5e0d909#code:~:text=Constructor%20Arguments%20(ABI%2DEncoded%20and%20is%20the%20last%20bytes%20of%20the%20Contract%20Creation%20Code%20above))
- > first seignorage txn (block 10839649, 7,647.920000000000000000000003146 WTON minted): [etherscan](https://etherscan.io/tx/0x7c02b858b11c9a18973b013d986bc738709569071b5f940fc81048bb009bbc62)
- -->> (check) first seignorage minted = seignorage per block x (first seignorage block # - seignorage start block #) = 3.92 x (10839649-10837698) = 7,647.92 WTON

## Check Event 

(1) **CommitLog1**  [code](https://github.com/tokamak-network/plasma-evm-contracts/blob/c3ac1a98c7b8ac03496c9f4e523bd3f5990b6a62/contracts/stake/managers/SeigManager.sol#L653-L659) 

- Event log : [link](https://etherscan.io/tx/0x7c02b858b11c9a18973b013d986bc738709569071b5f940fc81048bb009bbc62#eventlog) 

```javascript
CommitLog1 (uint256 totalStakedAmount, uint256 totalSupplyOfWTON, uint256 prevTotalSupply, uint256 nextTotalSupply)View Source

Topics
0 0x41a79a497d1457df24c25ab99f22349ae9aef4468429f0a781216e8dcf80c628

totalStakedAmount : // 시뇨리지 발행 반영된, 총 스테이킹 금액 **(팩터 계산) tot.totalSupply**
**15857587692752419690502400003146**
totalSupplyOfWTON :
50000000000000000000000000000000000
prevTotalSupply :            // 시뇨리지 발행전, 스테이킹 되어 있는 금액 
12797245225060000000000000000000
nextTotalSupply :            // 시뇨리지 발행후, 시뇨리지가 추가된 스테이킹 금액 (맞음)
**15857587692752419690502400000000** 
```

<u>** 위의 totalStakedAmount 금액과 nextTotalSupply 금액의 차이 확인</u> 

(2) FactorSet 팩터 변경   [code](https://github.com/tokamak-network/plasma-evm-contracts/blob/c3ac1a98c7b8ac03496c9f4e523bd3f5990b6a62/contracts/stake/tokens/AutoRefactorCoinage.sol#L182-L194)

Event Log : [link](https://etherscan.io/tx/0x7c02b858b11c9a18973b013d986bc738709569071b5f940fc81048bb009bbc62#eventlog)

```javascript
FactorSet (uint256 previous, uint256 current, uint256 shiftCount)View Source

****Topics****
• **0** 0x47eb304b27f9efb047a046029f8a279a7cc8fccc6786f1e2f65939639584fbdc

previous :
1000000000000000000000000000
current :
**1239140722387623954213875945 ****=> 소수점이 생겼을때, 내림으로 하지 않고 올림으로 계산됨 **
shiftCount :
0
```

 

-  팩터 계산 확인  [link](https://github.com/tokamak-network/plasma-evm-contracts/blob/c3ac1a98c7b8ac03496c9f4e523bd3f5990b6a62/contracts/stake/managers/SeigManager.sol#L599-L600) 

```javascript
source: prevTotalSupply  12797245225060000000000000000000
target: nextTotalSupply  15857587692752419690502400000000
oldFactor:  1000000000000000000000000000

function _calcNewFactor(uint256 source, uint256 target, uint256 oldFactor)
return rdiv(rmul(target, oldFactor), source);
=15857587692752419690502400000000 * 1000000000000000000000000000 / 12797245225060000000000000000000
=**1239140722387623954213875944.7541310550540577  => 소수점이 생김.  **
-> **1239140722387623954213875944** : factor 
```

** 팩터 계산시 소수점이 생기는데, 반올림으로 처리하여 발생되는 수치임. 그러나 ray 27로 계산하고, 추후 wei 18 로 바꾸기 때문에 해당 오차로 인한 실제적인 추가 발행은 존재하지 않는다고 판단하고 개발한것 같음