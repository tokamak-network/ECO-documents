Test the updateSeigniorage after 1000.1 TON deposit of operator on Talken layer

repo : [https://github.com/tokamak-network/ton-staking-v2/tree/test.talken.update_seigniorage](https://github.com/tokamak-network/ton-staking-v2/tree/test.talken.update_seigniorage)

# Test 1

1. talken accounts : talken 레이어에 deposit 한 계정 리스트를 취합한다.
1. prev balances : 계정리스트의 현재 스테이킹 금액을 모두 조회한다.
1. updateSeigniorageLayer : **오퍼레이터가** 1001톤 스테이킹한뒤, 업데이트 시뇨리지 실행한다.
1. 계정리스트의 스테이킹 금액을 모두 조회한다. 
1. 이전 스테이킹 금액과 새로 집계된 스테이킹 금액을 비교하여,  추가된 시뇨리지 양을 집계한다. 

**code** 

 [https://github.com/tokamak-network/ton-staking-v2/blob/test.talken.update_seigniorage/scripts/talken/0.gathering.talken.users.js](https://github.com/tokamak-network/ton-staking-v2/blob/test.talken.update_seigniorage/scripts/talken/0.gathering.talken.users.js)

**run** 

`npx hardhat run ./scripts/talken/0.gathering.talken.users.js`

**result**  

```javascript
talken accounts :  [
  '0x86f2d556c21ca350dce7988f08d4b5c61cc25144',
  '0x6e40960315ce2906577042c78e03006da3f55226',
  '0x85d8d5eb9f6d1c9dd61ff39ee99f68c77d6f7780',
  '0xd040baeb020692d62a0ec7811fb6be9b96f9844e',
  '0x2b8fa2d118ff2e512ba76f6a8c19dea4e75df05a',
  '0x61009474455ee644bce02d729d4d29df2f3bda00',
  '0xbe3ee1401be4bd18eb75ab528b88ffc1df8c6007',
  '0x30448930a038fec80f8534fa54a24ad0f5393dd4',
  '0xceb2196addf345f68d1f536ddaa49fe54bcbddad'
]
prev balances :  [
  {
    account: '0x86f2d556c21ca350dce7988f08d4b5c61cc25144',
    balance: '2000000000000000000000000000000'
  },
  {
    account: '0x6e40960315ce2906577042c78e03006da3f55226',
    balance: '6000000000000000000000000000'
  },
  {
    account: '0x85d8d5eb9f6d1c9dd61ff39ee99f68c77d6f7780',
    balance: '3000000000000000000000000000'
  },
  {
    account: '0xd040baeb020692d62a0ec7811fb6be9b96f9844e',
    balance: '5000000000000000000000000000'
  },
  {
    account: '0x2b8fa2d118ff2e512ba76f6a8c19dea4e75df05a',
    balance: '1000000000000000000000000000'
  },
  {
    account: '0x61009474455ee644bce02d729d4d29df2f3bda00',
    balance: '1000000000000000000000000000'
  },
  {
    account: '0xbe3ee1401be4bd18eb75ab528b88ffc1df8c6007',
    balance: '174000000000000000000000000000'
  },
  {
    account: '0x30448930a038fec80f8534fa54a24ad0f5393dd4',
    balance: '420920000000000000000000000000'
  },
  {
    account: '0xceb2196addf345f68d1f536ddaa49fe54bcbddad',
    balance: '5000000000000000000000000000'
  }
]
--- updateSeigniorageLayer  0x36101b31e74c5E8f9a9cec378407Bbb776287761
-----
after balances :  [
  {
    account: '0x86f2d556c21ca350dce7988f08d4b5c61cc25144',
    balance: '4516475350347622416978960096000'
  },
  {
    account: '0x6e40960315ce2906577042c78e03006da3f55226',
    balance: '13549426051042867250936880288'
  },
  {
    account: '0x85d8d5eb9f6d1c9dd61ff39ee99f68c77d6f7780',
    balance: '6774713025521433625468440144'
  },
  {
    account: '0xd040baeb020692d62a0ec7811fb6be9b96f9844e',
    balance: '11291188375869056042447400240'
  },
  {
    account: '0x2b8fa2d118ff2e512ba76f6a8c19dea4e75df05a',
    balance: '2258237675173811208489480048'
  },
  {
    account: '0x61009474455ee644bce02d729d4d29df2f3bda00',
    balance: '2258237675173811208489480048'
  },
  {
    account: '0xbe3ee1401be4bd18eb75ab528b88ffc1df8c6007',
    balance: '392933355480243150277169528352'
  },
  {
    account: '0x30448930a038fec80f8534fa54a24ad0f5393dd4',
    balance: '950537402234160613877391941804'
  },
  {
    account: '0xceb2196addf345f68d1f536ddaa49fe54bcbddad',
    balance: '11291188375869056042447400240'
  }
]
-----
addSeigs :  [
  {
    account: '0x86f2d556c21ca350dce7988f08d4b5c61cc25144',
    seigs: '2516475350347622416978960096000'
  },
  {
    account: '0x6e40960315ce2906577042c78e03006da3f55226',
    seigs: '7549426051042867250936880288'
  },
  {
    account: '0x85d8d5eb9f6d1c9dd61ff39ee99f68c77d6f7780',
    seigs: '3774713025521433625468440144'
  },
  {
    account: '0xd040baeb020692d62a0ec7811fb6be9b96f9844e',
    seigs: '6291188375869056042447400240'
  },
  {
    account: '0x2b8fa2d118ff2e512ba76f6a8c19dea4e75df05a',
    seigs: '1258237675173811208489480048'
  },
  {
    account: '0x61009474455ee644bce02d729d4d29df2f3bda00',
    seigs: '1258237675173811208489480048'
  },
  {
    account: '0xbe3ee1401be4bd18eb75ab528b88ffc1df8c6007',
    seigs: '218933355480243150277169528352'
  },
  {
    account: '0x30448930a038fec80f8534fa54a24ad0f5393dd4',
    seigs: '529617402234160613877391941804'
  },
  {
    account: '0xceb2196addf345f68d1f536ddaa49fe54bcbddad',
    seigs: '6291188375869056042447400240'
  }
]

```

# Test2 

1. dev tester : 0xceb2196addf345f68d1f536ddaa49fe54bcbddad 
1. talken accounts : talken 레이어에 deposit 한 계정 리스트를 취합한다. ( dev tester포함되어 있음.) 
1. prev balances : 계정리스트의 현재 스테이킹 금액을 모두 조회한다.
1. dev tester 가 2000TON 을  deposit 한다. 
1. updateSeigniorageLayer : **dev tester**가 오퍼레이터에게 1001톤 스테이킹한뒤, 업데이트 시뇨리지 실행한다.
  1. [https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#writeProxyContract](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#writeProxyContract) depositManager 의 deposit ( layer address, to address , wton deposit amount) 함수를 사용하여 대신 deposit 해줄 수 있다. 사용하기전에 WTON.approve(depositManager, amount) 를 실행해야 한다. 
1. 계정리스트의 스테이킹 금액을 모두 조회한다. 
1. 이전 스테이킹 금액과 새로 집계된 스테이킹 금액을 비교하여,  추가된 시뇨리지 양을 집계한다. 

**code** 

 [https://github.com/tokamak-network/ton-staking-v2/blob/test.talken.update_seigniorage/scripts/talken/0.gathering.talken.users.js](https://github.com/tokamak-network/ton-staking-v2/blob/test.talken.update_seigniorage/scripts/talken/0.gathering.talken.users.js)

**run** 

`npx hardhat run ./scripts/talken/1.gathering.talken.users.js`

**result 1 **  

tester 가 2000 WTON deposit 하고, 1001TON을 오퍼레이터에게 deposit하면, 

업데이트 시뇨리지 후, 받는 시뇨리지는 1624.810837822243208473060056070 WTON 입니다. 

**result 2**  

- tester 가 1500 WTON deposit 하고, 1001TON을 오퍼레이터에게 deposit하면,  업데이트 시뇨리지 후, 받는 시뇨리지는 1338,805424185951218078820976220 WTON 입니다. 
- tester 가 1300 WTON deposit 하고, 1001TON을 오퍼레이터에게 deposit하면,  업데이트 시뇨리지 후, 받는 시뇨리지는 1208.117721529181319997961722455 WTON 입니다. 
- tester 가 1050 WTON deposit 하고, 1001TON을 오퍼레이터에게 deposit하면,  업데이트 시뇨리지 후, 받는 시뇨리지는 1029.002718652192675695158782015 WTON 입니다. 