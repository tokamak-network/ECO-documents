# Basic Info

- Project codename : ECO
- requester name: Harvey
- requester Github id: zzooppii
- Review branch link: [GitHub - tokamak-network/ton-staking-v2 at daoSnapshot-codeReview](https://github.com/tokamak-network/ton-staking-v2/tree/daoSnapshot-codeReview)
- commit hash : c3020fba1af25ce44a4c58103b449d31797db857
- Review Duration : 4 days (business days) (5 days[extended]) (2025-06-02~2025-06-10)
- Review completion deadline : 2025-06-09 (It has been extended for one more day. 2025-06-10)
- Explanation of the Upgraded : [link](/203d96a400a3805e92dcc97c46aa2eeb)

# Audit Scope 

- [https://github.com/tokamak-network/ton-staking-v2/blob/daoSnapshot-codeReview/contracts/dao/DAOCommittee_V2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/daoSnapshot-codeReview/contracts/dao/DAOCommittee_V2.sol)
- [https://github.com/tokamak-network/ton-staking-v2/blob/daoSnapshot-codeReview/contracts/dao/StorageStateCommitteeV3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/daoSnapshot-codeReview/contracts/dao/StorageStateCommitteeV3.sol)
- Functions that have changed
  - onApprove
  - currentAgendaStatus
  - _decodeAgendaData
  - _createAgenda
- Added storage
  - mapping(uint256 => string) public agendaMemo

# How to Test

## Install

```solidity
git clone https://github.com/tokamak-network/ton-staking-v2.git

cd ton-staking-v2

git checkout DAOSnapshot

npm install
```

## Set ENV

```solidity
cp .env.sample .env


//Please copy the contents below and paste them into .env.
ETHERSCAN_API_KEY=
COINMARKETCAP_API_KEY=

ETH_NODE_URI_localhost=http://127.0.0.1:8545/
ETH_NODE_URI_MAINNET=https://mainnet.infura.io/v3/{your key}
ETH_NODE_URI_goerli=https://goerli.infura.io/v3/{your key}
ETH_NODE_URI_sepolia=https://sepolia.infura.io/v3/{your key}
ETH_NODE_URI_TITAN_GOERLI=https://rpc.titan-goerli.tokamak.network
ETH_NODE_URI_THANOS_SEPOLIA=https://rpc.thanos-sepolia-test.tokamak.network



#======= private key =========
PRIVATE_KEY=
DEPLOYER_PRIVATE_KEY=

```

### Check Point

1. ETHERSCAN_API_KEY can be obtained from the following [link](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics).
1. COINMARKETCAP_API_KEY can be obtained from the following [link](https://coinmarketcap.com/api/).
1. The value of {your key} is [infura](https://www.infura.io/), [**Alchemy**](https://www.alchemy.com/)**, **etc.
1. PRIVATE_KEY and DEPLOYER_PRIVATE_KEY are the privateKey of your personal account, and it is okay to use the same value.

## On Sepolia

```solidity
//blockNumber: 8323710
npx hardhat test test/agenda/29.currentAgendaViewTest-sepolia.js

//hardhat Setting
forking: {
  url: `${process.env.ETH_NODE_URI_sepolia}`,
  blockNumber: 8323710
},
```

## On Mainnet

```solidity
//blockNumber:22355050
npx hardhat test test/agenda/30.currentAgendaViewTest-mainnet.js


//hardhat Setting
forking: {
	url: `${process.env.ETH_NODE_URI_MAINNET}`,
	blockNumber:22355050
},
```

## Reference video for testing

[Link](https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view)

# Deploy & CreateAgenda the Contract

## On Sepolia

```solidity
//Deployed Contract
DAOCommittee_V2 0xF955b73431ba9B411E41A13Bf29787BCD087FA6E

//Create Agenda
tx : https://sepolia.etherscan.io/tx/0x8ce7ab0412fc6c9a5f7dcde6b56c212b52e5714ede0ea6f6e41a79c3a13485b1

//Execute Agenda
tx : https://sepolia.etherscan.io/tx/0x59fc5d95f9bb71590bd41a4d2442e94d34d05199188d3e31978a89480e7ddac6
```

# Feedback

Suhyeon
Goerli related settings should be removed

log
```javascript
·------------------------|----------------------------|-------------|-----------------------------·
|  Solc version: 0.5.12  ·  Optimizer enabled: false  ·  Runs: 200  ·  Block limit: 30000000 gas  │
·························|····························|·············|······························
|  Methods               ·               21 gwei/gas                ·       2624.94 usd/eth       │
··············|··········|··············|·············|·············|···············|··············
|  Contract   ·  Method  ·  Min         ·  Max        ·  Avg        ·  # calls      ·  usd (avg)  │
··············|··········|··············|·············|·············|···············|··············
|  Deployments           ·                                          ·  % of limit   ·             │
·························|··············|·············|·············|···············|··············
|  DAOCommittee_V2       ·           -  ·          -  ·    4959174  ·       16.5 %  ·     273.37  │
·------------------------|--------------|-------------|-------------|---------------|-------------·


  27 passing (3s)
  64 failing

  1) currentAgendaStatus Test on Sepolia
       Setting TON-related Contract
         TON Admin Test:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="balanceOf(address)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  2) currentAgendaStatus Test on Sepolia
       Set Contract
         pauseProxy check:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="pauseProxy()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  3) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check implementation:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="implementation()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  4) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check proxyImplementation(0) = DAOCommittee_V1:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  5) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check proxyImplementation(1) = DAOCommitteeOwner:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  6) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check CandidateAddOnFactory Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="candidateAddOnFactory()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  7) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check Layer2Manager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="layer2Manager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  8) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check daoCommitteeOwner cooldownTime:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="cooldownTime()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  9) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check ton Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="ton()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  10) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check daoVault Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="daoVault()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  11) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check agendaManager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="agendaManager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  12) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check candidateFactory Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="candidateFactory()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  13) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check layer2Registry Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="layer2Registry()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  14) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check seigManager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="seigManager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  15) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check maxMember:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="maxMember()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  16) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check quorum:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="quorum()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  17) currentAgendaStatus Test on Sepolia
       Check the executed agenda
         Check wton:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="wton()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  18) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         upgradeTo2 Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  19) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         increase block time and check votable:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="numAgendas()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  20) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  21) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  22) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  23) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         execute agenda:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  24) currentAgendaStatus Test on Sepolia
       Deploy And UpgradeTo2 newDAOLogic
         Ensure the agenda is properly executed proxyImplementation(0) = DAOCommittee_V2:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  25) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         1. Return for an Agenda that has not been created:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="numAgendas()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  26) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  27) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  28) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         2. Returns a status called NoticeTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  29) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  30) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         3. Returns (NO CONSENSUS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  31) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  32) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         4. Returns (pending, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  33) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  34) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         5. Returns (ACCEPT, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  35) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  36) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         6. Returns (ACCEPT, WAITING_EXEC):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  37) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         execute agenda (anyone):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  38) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         7. Returns (ACCEPT, EXECUTED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  39) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  40) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  41) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  42) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         8. Returns (NO CONSENSUS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  43) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  44) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         9. Returns (pending, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  45) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  46) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         10. Returns (DISMISS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  47) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  48) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         11. Returns (DISMISS, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  49) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  50) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  51) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  52) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  53) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  54) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         12. Returns (REJECT, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  55) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  56) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         13. Returns (REJECT, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  57) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  58) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  59) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  60) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  61) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  62) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         14. Returns (PENDING, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  63) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  64) currentAgendaStatus Test on Sepolia
       currentAgendaVeiw Test
         15. Returns (NO CONSENSUS, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)



```

hardhat.config.ts (Sepolia)
```solidity
// import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import '@typechain/hardhat'
import '@nomiclabs/hardhat-ethers'
import "@nomicfoundation/hardhat-chai-matchers";
// import "hardhat-deploy/src/type-extensions";
// import "@nomiclabs/hardhat-ethers";

import "hardhat-gas-reporter";
import dotenv from "dotenv" ;
import { HardhatUserConfig } from "hardhat/types";
import "hardhat-deploy";
dotenv.config();
import { task, types } from 'hardhat/config'
import "./tasks";

const config: HardhatUserConfig = {
  namedAccounts: {
    deployer: 0,
    addr1: 1,
    addr2: 2,
    SeigManager: {
      default: 3,
      mainnet: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      goerli: '0x446ece59ef429B774Ff116432bbB123f1915D9E3',
      hardhat: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      local: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      sepolia: '0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7'
    },
    DepositManager: {
      default: 4,
      mainnet: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      goerli: '0x0ad659558851f6ba8a8094614303F56d42f8f39A',
      hardhat: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      local: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      sepolia: '0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F'
    },
    L2Registry: {
      default: 5,
      mainnet: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      goerli: '0x6817e1c04748eae68EBFF13216280Df1ec15ba86',
      hardhat: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      local: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      sepolia: '0xA0a9576b437E52114aDA8b0BC4149F2F5c604581'
    },
    CoinageFactory: {
      default: 6,
      mainnet: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      goerli: '0x09207BdB146E41dadad015aB3d835f66498b0A0c',
      hardhat: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      local: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      sepolia: '0x93258413Ef2998572AB4B269b5DCb963dD35D440'
    },
    TON: {
      default: 7,
      mainnet: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      goerli: '0x68c1F9620aeC7F2913430aD6daC1bb16D8444F00',
      hardhat: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      local: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      sepolia: '0xa30fe40285b8f5c0457dbc3b7c8a280373c40044'
    },
    WTON: {
      default: 8,
      mainnet: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      goerli: '0xe86fCf5213C785AcF9a8BFfEeDEfA9a2199f7Da6',
      hardhat: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      local: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      sepolia: '0x79e0d92670106c85e9067b56b8f674340dca0bbd'
    },
    TOS: {
      default: 9,
      mainnet: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      goerli: '0x67F3bE272b1913602B191B3A68F7C238A2D81Bb9',
      hardhat: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      local: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      sepolia: '0xff3ef745d9878afe5934ff0b130868afddbc58e8'
    },
    DAOCommitteeProxy: {
      default: 10,
      mainnet: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      goerli: '0x3C5ffEe61A384B384ed38c0983429dcDb49843F6',
      hardhat: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      local: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      sepolia: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386'
    },
    CandidateFactory: {
      default: 11,
      mainnet: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      goerli: '0xd1c4fE0Ac211F8A41817c26D1801fd549D56E31e',
      hardhat: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      local: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      sepolia: '0x04e3C2B720FB8896A7f9Ea59DdcA85fD45189C7f'
    },
    DAOAgendaManager: {
      default: 12,
      mainnet: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      goerli: '0x0e1583da47cf641305eDD1e4C6dB6DD18e138a21',
      hardhat: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      local: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      sepolia: '0x1444f7a8bC26a3c9001a13271D56d6fF36B44f08'
    },
    AutoCoinageSnapshot2: {
      default: 13,
      mainnet: '0x85Ca9f611C363065252EA9462c90743922767b55',
      goerli: '',
      hardhat: '0x85Ca9f611C363065252EA9462c90743922767b55',
      local: '0x85Ca9f611C363065252EA9462c90743922767b55',
      sepolia: ''
    },
    DaoCommitteeAdminAddress: {
      default: 14,
      mainnet: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      goerli: '',
      hardhat: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      local: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    powerTonAddress: {
      default: 15,
      mainnet: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      goerli: '',
      hardhat: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      local: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      sepolia: '0xbe16830EeD019227892938Ae13C54Ec218772f48'
    },
    daoVaultAddress: {
      default: 16,
      mainnet: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      goerli: '',
      hardhat: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      local: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      sepolia: '0xB9F6c9E75418D7E5a536ADe08f0218196BB3eBa4'
    },
    level19Address: {
      default: 17,
      mainnet: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      goerli: '',
      hardhat: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      local: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      sepolia: ''
    },
    level19Admin: {
      default: 18,
      mainnet: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      goerli: '',
      hardhat: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      local: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      sepolia: ''
    },
    tokamakAddress: {
      default: 19,
      mainnet: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      goerli: '',
      hardhat: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      local: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      sepolia: ''
    },
    tokamakAdmin: {
      default: 20,
      mainnet: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      goerli: '',
      hardhat: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      local: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      sepolia: ''
    },
    powerTonAdminAddress: {
      default: 21,
      mainnet: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      goerli: '',
      hardhat: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      local: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    SeigManagerProxy: {
      default: 22,
      mainnet: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      goerli: '',
      hardhat: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      local: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      sepolia: '0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7'
    },
    DepositManagerProxy: {
      default: 23,
      mainnet: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      goerli: '',
      hardhat: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      local: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      sepolia: '0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F'
    },
    Layer2RegistryProxy: {
      default: 23,
      mainnet: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      goerli: '',
      hardhat: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      local: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      sepolia: '0xA0a9576b437E52114aDA8b0BC4149F2F5c604581'
    },
    // tonAdminAddress: {
    //   default: 10,
    //   mainnet: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    //   goerli: '',
    //   hardhat: '',
    // },
    l1MessengerAddress: {
      default: 22,
      mainnet: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      goerli: '0x2878373BA3Be0Ef2a93Ba5b3F7210D76cb222e63',
      hardhat: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      local: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      sepolia: '0xc123047238e8f4bFB7Ad849cA4364b721B5ABD8A'
    },
    l1BridgeAddress: {
      default: 23,
      mainnet: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      goerli: '0x7377F3D0F64d7a54Cf367193eb74a052ff8578FD',
      hardhat: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      local: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      sepolia: '0x1F032B938125f9bE411801fb127785430E7b3971'
    },
    l1AddressManagerAddress: {
      default: 24,
      mainnet: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      goerli: '0xEFa07e4263D511fC3a7476772e2392efFb1BDb92',
      hardhat: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      local: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      sepolia: '0x79a53E72e9CcfAe63B0fB9A4edb66C7563d74Dc3'
    },
    l2TokenFactoryAddress: {
      default: 25,
      mainnet: '',
      goerli: '',
      hardhat: '',
      local: '',
      sepolia: ''
    },
    l2TonAddress: {
      default: 26,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa',
      hardhat: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      local: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      sepolia: '0x7c6b91d9be155a6db01f749217d76ff02a7227f2'
    },
    swapProxy: {
      default: 27,
      mainnet: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      goerli: '',
      hardhat: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      local: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      sepolia: '0x690f994b82f001059e24d79292c3c476854b767a'
    },
    DAOCommitteeOwner : {
      default: 28,
      mainnet: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      goerli: '',
      hardhat: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      local: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    titanL1StandardBridge : {
      default: 29,
      mainnet: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      goerli: '',
      hardhat: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      local: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      sepolia: '0x1F032B938125f9bE411801fb127785430E7b3971'
    },
    titanL1CrossDomainMessenger : {
      default: 30,
      mainnet: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      goerli: '',
      hardhat: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      local: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      sepolia: '0xc123047238e8f4bFB7Ad849cA4364b721B5ABD8A'
    },
    titanL1ERC721Bridge: {
      default: 31,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanL2OutputOracle: {
      default: 32,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanOptimismPortal: {
      default: 33,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanOptimismMintableERC20Factory: {
      default: 34,
      mainnet: '0x4200000000000000000000000000000000000012',
      goerli: '',
      hardhat: '0x4200000000000000000000000000000000000012',
      local: '0x4200000000000000000000000000000000000012',
      sepolia: '0x4200000000000000000000000000000000000012'
    },
    thanosL1StandardBridge : {
      default: 35,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E',
      local: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E',
      sepolia: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E'
    },
    thanosL1CrossDomainMessenger : {
      default: 36,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x8ca593C92446104B4DA968786735dbd503886ed7',
      local: '0x8ca593C92446104B4DA968786735dbd503886ed7',
      sepolia: '0x8ca593C92446104B4DA968786735dbd503886ed7'
    },
    thanosL1ERC721Bridge: {
      default: 37,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x29677290236F7950B96a30383D76AD363C08f51A',
      local: '0x29677290236F7950B96a30383D76AD363C08f51A',
      sepolia: '0x29677290236F7950B96a30383D76AD363C08f51A'
    },
    thanosL2OutputOracle: {
      default: 38,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0xfa565a84075091044FC891e3f73E26A014A4fd8c',
      local: '0xfa565a84075091044FC891e3f73E26A014A4fd8c',
      sepolia: '0xfa565a84075091044FC891e3f73E26A014A4fd8c'
    },
    thanosOptimismPortal: {
      default: 39,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x54A01163474FCD8a781455f09Ff0910e7e31B772',
      local: '0x54A01163474FCD8a781455f09Ff0910e7e31B772',
      sepolia: '0x54A01163474FCD8a781455f09Ff0910e7e31B772'
    },
    thanosOptimismMintableERC20Factory: {
      default: 40,
      mainnet: '0x4200000000000000000000000000000000000012',
      goerli: '0x4200000000000000000000000000000000000012',
      hardhat: '0x4200000000000000000000000000000000000012',
      local: '0x4200000000000000000000000000000000000012',
      sepolia: '0x1b624b7037C7d958Fb3fe22B12307E5295530C27'
    },
    thanosSystemConfig: {
      default: 41,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '0x0000000000000000000000000000000000000000',
      hardhat: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387',
      local: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387',
      sepolia: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387'
    },
    titanL2TON: {
      default: 42,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '',
      hardhat: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      local: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      sepolia: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2'
    },
    thanosL2TON: {
      default: 42,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '',
      hardhat: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000',
      local: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000',
      sepolia: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000'
    },
    daoMember1: {
      default: 43,
      mainnet: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      goerli: '',
      hardhat: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      local: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      sepolia: '0xD4335A175c36c0922F6A368b83f9F6671bf07606'
    },
    daoMember2: {
      default: 44,
      mainnet: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      goerli: '',
      hardhat: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      local: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      sepolia: '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea'
    },
    daoMember3: {
      default: 45,
      mainnet: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      goerli: '',
      hardhat: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      local: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    }
  },
  networks: {
    hardhat: {
      forking: {
        // url: `${process.env.ETH_NODE_URI_MAINNET}`,
        // blockNumber: 21077756
        url: `${process.env.ETH_NODE_URI_sepolia}`,
        // npx hardhat test test/layer2/units/3.Layer2Manager.sepolia.test.ts
        // blockNumber: 5859537,
        // blockNumber: 6042730
        // npx hardhat test test/layer2/units/3.Layer2Manager.sepolia.test.ts
        // blockNumber: 6042730
        // npx hardhat test test/layer2/sepolia_test/0.registerLayer2Candidate.ts
        // blockNumber: 5860655,
        // npx hardhat test test/layer2/sepolia_test/2.withdrawAndDepositL2.ts
        // blockNumber: 5870490,
        // npx hardhat test test/layer2/sepolia_test/1.updateSeigs.ts
        // blockNumber: 5874556,
        // npx hardhat test test/layer2/sepolia_test/3.updateSeigsAndClaim.ts
        // blockNumber: 5892966,
        // blockNumber: 6676283,
        // url: `${process.env.ETH_NODE_URI_MAINNET}`,
        // blockNumber: 18811511
        // blockNumber:
        // test registerCandidateAddOn
        // blockNumber: 6797943
        // blockNumber: 22081265
        // blockNumber:22355050
        blockNumber: 8323710
      },
      // allowUnlimitedContractSize: false,
      deploy: ['deploy-staking-v2.5-mainnet'],
      // deploy: ['deploy-staking-all-sepolia'],
    },
    local: {
      url: `${process.env.ETH_NODE_URI_localhost}`,
      timeout: 800000,
      accounts: [`${process.env.PRIVATE_KEY}`],
      // deploy: ['deploy-migration']
    },
    mainnet: {
      url: `${process.env.ETH_NODE_URI_MAINNET}`,
      accounts: [`${process.env.DEPLOYER_PRIVATE_KEY}`],
      gasPrice: 1000000000,
      // deploy: ['deploy']
      deploy: ['deploy-staking-v2.5-mainnet'],
    },
    goerli: {
      url: `${process.env.ETH_NODE_URI_goerli}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 5,
      // deploy: ['deploy-seig-manager-v1']
    },
    titan: {
      url: `${process.env.ETH_NODE_URI_TITAN}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 55004,
      // gasPrice: 1000000,
      // deploy: ['deploy_l2_proxy']
    },
    titangoerli: {
      url: `${process.env.ETH_NODE_URI_TITAN_GOERLI}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 5050,
      gasPrice: 250000,
      // deploy: ['deploy_l2_proxy']
    },
    sepolia: {
      url: `${process.env.ETH_NODE_URI_sepolia}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      // deploy: ['deploy_l2_proxy']
      deploy: ['deploy-layer2']
    },
  },
  deterministicDeployment: (network: string) => {
    // Skip on hardhat's local network.
    if (network === "31337") {
      return undefined;
    } else {
      return {
        factory: "0x4e59b44847b379578588920ca78fbf26c0b4956c",
        deployer: "0x3fab184622dc19b6109349b94811493bf2a45362",
        funding: "10000000000000000",
        signedTx: "0x00",
      }
    }
  },
  etherscan: {
    apiKey: {
      mainnet: `${process.env.ETHERSCAN_API_KEY}`,
      goerli: `${process.env.ETHERSCAN_API_KEY}`,
      sepolia: `${process.env.ETHERSCAN_API_KEY}`,
      titan: "verify",
      titangoerli: "verify"
    } ,
    customChains: [
      {
        network: "titan",
        chainId: 55004,
        urls: {
          apiURL: "https://explorer.titan.tokamak.network//api",
          browserURL: "https://explorer.titan.tokamak.network/"
        }
      },
      {
        network: "titangoerli",
        chainId: 5050,
        urls: {
          apiURL: "https://explorer.titan-goerli.tokamak.network/api",
          browserURL: "https://explorer.titan-goerli.tokamak.network/"
        }
      }
    ]
  },
  gasReporter: {
    enabled: true,
    currency: 'USD',
    gasPrice: 21,
    coinmarketcap: `${process.env.COINMARKETCAP_API_KEY}`
  },
  mocha: {
    timeout: 100000000
  },
  solidity: {
    compilers: [
      {
        version: "0.5.12",
      },
      {
        version: "0.8.19",
        settings: {
          // evmVersion: "cancun",
          viaIR: true,
          optimizer: {
            enabled: true,
            runs: 200,
            // details: {
            //   yul: true,
            // },
          },
          metadata: {
            // do not include the metadata hash, since this is machine dependent
            // and we want all generated code to be deterministic
            // https://docs.soliditylang.org/en/v0.8.12/metadata.html
            bytecodeHash: 'none',
          },
        },
      },
    ],
  },
};

export default config;
```

hardhat.config.ts (Mainnet)
```solidity
// import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import '@typechain/hardhat'
import '@nomiclabs/hardhat-ethers'
import "@nomicfoundation/hardhat-chai-matchers";
// import "hardhat-deploy/src/type-extensions";
// import "@nomiclabs/hardhat-ethers";

import "hardhat-gas-reporter";
import dotenv from "dotenv" ;
import { HardhatUserConfig } from "hardhat/types";
import "hardhat-deploy";
dotenv.config();
import { task, types } from 'hardhat/config'
import "./tasks";

const config: HardhatUserConfig = {
  namedAccounts: {
    deployer: 0,
    addr1: 1,
    addr2: 2,
    SeigManager: {
      default: 3,
      mainnet: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      goerli: '0x446ece59ef429B774Ff116432bbB123f1915D9E3',
      hardhat: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      local: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      sepolia: '0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7'
    },
    DepositManager: {
      default: 4,
      mainnet: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      goerli: '0x0ad659558851f6ba8a8094614303F56d42f8f39A',
      hardhat: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      local: '0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E',
      sepolia: '0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F'
    },
    L2Registry: {
      default: 5,
      mainnet: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      goerli: '0x6817e1c04748eae68EBFF13216280Df1ec15ba86',
      hardhat: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      local: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      sepolia: '0xA0a9576b437E52114aDA8b0BC4149F2F5c604581'
    },
    CoinageFactory: {
      default: 6,
      mainnet: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      goerli: '0x09207BdB146E41dadad015aB3d835f66498b0A0c',
      hardhat: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      local: '0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43',
      sepolia: '0x93258413Ef2998572AB4B269b5DCb963dD35D440'
    },
    TON: {
      default: 7,
      mainnet: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      goerli: '0x68c1F9620aeC7F2913430aD6daC1bb16D8444F00',
      hardhat: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      local: '0x2be5e8c109e2197D077D13A82dAead6a9b3433C5',
      sepolia: '0xa30fe40285b8f5c0457dbc3b7c8a280373c40044'
    },
    WTON: {
      default: 8,
      mainnet: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      goerli: '0xe86fCf5213C785AcF9a8BFfEeDEfA9a2199f7Da6',
      hardhat: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      local: '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
      sepolia: '0x79e0d92670106c85e9067b56b8f674340dca0bbd'
    },
    TOS: {
      default: 9,
      mainnet: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      goerli: '0x67F3bE272b1913602B191B3A68F7C238A2D81Bb9',
      hardhat: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      local: '0x409c4D8cd5d2924b9bc5509230d16a61289c8153',
      sepolia: '0xff3ef745d9878afe5934ff0b130868afddbc58e8'
    },
    DAOCommitteeProxy: {
      default: 10,
      mainnet: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      goerli: '0x3C5ffEe61A384B384ed38c0983429dcDb49843F6',
      hardhat: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      local: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
      sepolia: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386'
    },
    CandidateFactory: {
      default: 11,
      mainnet: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      goerli: '0xd1c4fE0Ac211F8A41817c26D1801fd549D56E31e',
      hardhat: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      local: '0x9fc7100a16407ee24a79c834a56e6eca555a5d7c',
      sepolia: '0x04e3C2B720FB8896A7f9Ea59DdcA85fD45189C7f'
    },
    DAOAgendaManager: {
      default: 12,
      mainnet: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      goerli: '0x0e1583da47cf641305eDD1e4C6dB6DD18e138a21',
      hardhat: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      local: '0xcD4421d082752f363E1687544a09d5112cD4f484',
      sepolia: '0x1444f7a8bC26a3c9001a13271D56d6fF36B44f08'
    },
    AutoCoinageSnapshot2: {
      default: 13,
      mainnet: '0x85Ca9f611C363065252EA9462c90743922767b55',
      goerli: '',
      hardhat: '0x85Ca9f611C363065252EA9462c90743922767b55',
      local: '0x85Ca9f611C363065252EA9462c90743922767b55',
      sepolia: ''
    },
    DaoCommitteeAdminAddress: {
      default: 14,
      mainnet: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      goerli: '',
      hardhat: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      local: '0xb4983da083a5118c903910db4f5a480b1d9f3687',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    powerTonAddress: {
      default: 15,
      mainnet: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      goerli: '',
      hardhat: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      local: '0x970298189050aBd4dc4F119ccae14ee145ad9371',
      sepolia: '0xbe16830EeD019227892938Ae13C54Ec218772f48'
    },
    daoVaultAddress: {
      default: 16,
      mainnet: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      goerli: '',
      hardhat: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      local: '0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303',
      sepolia: '0xB9F6c9E75418D7E5a536ADe08f0218196BB3eBa4'
    },
    level19Address: {
      default: 17,
      mainnet: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      goerli: '',
      hardhat: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      local: '0x42ccf0769e87cb2952634f607df1c7d62e0bbc52',
      sepolia: ''
    },
    level19Admin: {
      default: 18,
      mainnet: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      goerli: '',
      hardhat: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      local: '0xd1820b18be7f6429f1f44104e4e15d16fb199a43',
      sepolia: ''
    },
    tokamakAddress: {
      default: 19,
      mainnet: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      goerli: '',
      hardhat: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      local: '0x576c7a48fcef1c70db632bb1504d9a5c0d0190d3',
      sepolia: ''
    },
    tokamakAdmin: {
      default: 20,
      mainnet: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      goerli: '',
      hardhat: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      local: '0xEA8e2eC08dCf4971bdcdfFFe21439995378B44F3',
      sepolia: ''
    },
    powerTonAdminAddress: {
      default: 21,
      mainnet: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      goerli: '',
      hardhat: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      local: '0x15280a52e79fd4ab35f4b9acbb376dcd72b44fd1',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    SeigManagerProxy: {
      default: 22,
      mainnet: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      goerli: '',
      hardhat: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      local: '0x0b55a0f463b6defb81c6063973763951712d0e5f',
      sepolia: '0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7'
    },
    DepositManagerProxy: {
      default: 23,
      mainnet: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      goerli: '',
      hardhat: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      local: '0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e',
      sepolia: '0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F'
    },
    Layer2RegistryProxy: {
      default: 23,
      mainnet: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      goerli: '',
      hardhat: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      local: '0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b',
      sepolia: '0xA0a9576b437E52114aDA8b0BC4149F2F5c604581'
    },
    // tonAdminAddress: {
    //   default: 10,
    //   mainnet: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    //   goerli: '',
    //   hardhat: '',
    // },
    l1MessengerAddress: {
      default: 22,
      mainnet: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      goerli: '0x2878373BA3Be0Ef2a93Ba5b3F7210D76cb222e63',
      hardhat: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      local: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      sepolia: '0xc123047238e8f4bFB7Ad849cA4364b721B5ABD8A'
    },
    l1BridgeAddress: {
      default: 23,
      mainnet: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      goerli: '0x7377F3D0F64d7a54Cf367193eb74a052ff8578FD',
      hardhat: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      local: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      sepolia: '0x1F032B938125f9bE411801fb127785430E7b3971'
    },
    l1AddressManagerAddress: {
      default: 24,
      mainnet: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      goerli: '0xEFa07e4263D511fC3a7476772e2392efFb1BDb92',
      hardhat: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      local: '0xeDf6C92fA72Fa6015B15C9821ada145a16c85571',
      sepolia: '0x79a53E72e9CcfAe63B0fB9A4edb66C7563d74Dc3'
    },
    l2TokenFactoryAddress: {
      default: 25,
      mainnet: '',
      goerli: '',
      hardhat: '',
      local: '',
      sepolia: ''
    },
    l2TonAddress: {
      default: 26,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa',
      hardhat: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      local: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      sepolia: '0x7c6b91d9be155a6db01f749217d76ff02a7227f2'
    },
    swapProxy: {
      default: 27,
      mainnet: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      goerli: '',
      hardhat: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      local: '0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d',
      sepolia: '0x690f994b82f001059e24d79292c3c476854b767a'
    },
    DAOCommitteeOwner : {
      default: 28,
      mainnet: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      goerli: '',
      hardhat: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      local: '0xe070ffd0e25801392108076ed5291fa9524c3f44',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    },
    titanL1StandardBridge : {
      default: 29,
      mainnet: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      goerli: '',
      hardhat: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      local: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
      sepolia: '0x1F032B938125f9bE411801fb127785430E7b3971'
    },
    titanL1CrossDomainMessenger : {
      default: 30,
      mainnet: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      goerli: '',
      hardhat: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      local: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
      sepolia: '0xc123047238e8f4bFB7Ad849cA4364b721B5ABD8A'
    },
    titanL1ERC721Bridge: {
      default: 31,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanL2OutputOracle: {
      default: 32,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanOptimismPortal: {
      default: 33,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x0000000000000000000000000000000000000000',
      local: '0x0000000000000000000000000000000000000000',
      sepolia: '0x0000000000000000000000000000000000000000'
    },
    titanOptimismMintableERC20Factory: {
      default: 34,
      mainnet: '0x4200000000000000000000000000000000000012',
      goerli: '',
      hardhat: '0x4200000000000000000000000000000000000012',
      local: '0x4200000000000000000000000000000000000012',
      sepolia: '0x4200000000000000000000000000000000000012'
    },
    thanosL1StandardBridge : {
      default: 35,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E',
      local: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E',
      sepolia: '0x5D2Ed95c0230Bd53E336f12fA9123847768B2B3E'
    },
    thanosL1CrossDomainMessenger : {
      default: 36,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x8ca593C92446104B4DA968786735dbd503886ed7',
      local: '0x8ca593C92446104B4DA968786735dbd503886ed7',
      sepolia: '0x8ca593C92446104B4DA968786735dbd503886ed7'
    },
    thanosL1ERC721Bridge: {
      default: 37,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x29677290236F7950B96a30383D76AD363C08f51A',
      local: '0x29677290236F7950B96a30383D76AD363C08f51A',
      sepolia: '0x29677290236F7950B96a30383D76AD363C08f51A'
    },
    thanosL2OutputOracle: {
      default: 38,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0xfa565a84075091044FC891e3f73E26A014A4fd8c',
      local: '0xfa565a84075091044FC891e3f73E26A014A4fd8c',
      sepolia: '0xfa565a84075091044FC891e3f73E26A014A4fd8c'
    },
    thanosOptimismPortal: {
      default: 39,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '',
      hardhat: '0x54A01163474FCD8a781455f09Ff0910e7e31B772',
      local: '0x54A01163474FCD8a781455f09Ff0910e7e31B772',
      sepolia: '0x54A01163474FCD8a781455f09Ff0910e7e31B772'
    },
    thanosOptimismMintableERC20Factory: {
      default: 40,
      mainnet: '0x4200000000000000000000000000000000000012',
      goerli: '0x4200000000000000000000000000000000000012',
      hardhat: '0x4200000000000000000000000000000000000012',
      local: '0x4200000000000000000000000000000000000012',
      sepolia: '0x1b624b7037C7d958Fb3fe22B12307E5295530C27'
    },
    thanosSystemConfig: {
      default: 41,
      mainnet: '0x0000000000000000000000000000000000000000',
      goerli: '0x0000000000000000000000000000000000000000',
      hardhat: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387',
      local: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387',
      sepolia: '0xf8FCFDbdb7C4E734D035A5681Fd1fe08ec85e387'
    },
    titanL2TON: {
      default: 42,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '',
      hardhat: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      local: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      sepolia: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2'
    },
    thanosL2TON: {
      default: 42,
      mainnet: '0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2',
      goerli: '',
      hardhat: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000',
      local: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000',
      sepolia: '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000'
    },
    daoMember1: {
      default: 43,
      mainnet: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      goerli: '',
      hardhat: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      local: '0x0f42d1c40b95df7a1478639918fc358b4af5298d',
      sepolia: '0xD4335A175c36c0922F6A368b83f9F6671bf07606'
    },
    daoMember2: {
      default: 44,
      mainnet: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      goerli: '',
      hardhat: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      local: '0xf3b17fdb808c7d0df9acd24da34700ce069007df',
      sepolia: '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea'
    },
    daoMember3: {
      default: 45,
      mainnet: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      goerli: '',
      hardhat: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      local: '0x06d34f65869ec94b3ba8c0e08bceb532f65005e2',
      sepolia: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
    }
  },
  networks: {
    hardhat: {
      forking: {
        url: `${process.env.ETH_NODE_URI_MAINNET}`,
        // blockNumber: 21077756
        // url: `${process.env.ETH_NODE_URI_sepolia}`,
        // npx hardhat test test/layer2/units/3.Layer2Manager.sepolia.test.ts
        // blockNumber: 5859537,
        // blockNumber: 6042730
        // npx hardhat test test/layer2/units/3.Layer2Manager.sepolia.test.ts
        // blockNumber: 6042730
        // npx hardhat test test/layer2/sepolia_test/0.registerLayer2Candidate.ts
        // blockNumber: 5860655,
        // npx hardhat test test/layer2/sepolia_test/2.withdrawAndDepositL2.ts
        // blockNumber: 5870490,
        // npx hardhat test test/layer2/sepolia_test/1.updateSeigs.ts
        // blockNumber: 5874556,
        // npx hardhat test test/layer2/sepolia_test/3.updateSeigsAndClaim.ts
        // blockNumber: 5892966,
        // blockNumber: 6676283,
        // url: `${process.env.ETH_NODE_URI_MAINNET}`,
        // blockNumber: 18811511
        // blockNumber:
        // test registerCandidateAddOn
        // blockNumber: 6797943
        // blockNumber: 22081265
        blockNumber:22355050
        // blockNumber: 8323710
      },
      // allowUnlimitedContractSize: false,
      deploy: ['deploy-staking-v2.5-mainnet'],
      // deploy: ['deploy-staking-all-sepolia'],
    },
    local: {
      url: `${process.env.ETH_NODE_URI_localhost}`,
      timeout: 800000,
      accounts: [`${process.env.PRIVATE_KEY}`],
      // deploy: ['deploy-migration']
    },
    mainnet: {
      url: `${process.env.ETH_NODE_URI_MAINNET}`,
      accounts: [`${process.env.DEPLOYER_PRIVATE_KEY}`],
      gasPrice: 1000000000,
      // deploy: ['deploy']
      deploy: ['deploy-staking-v2.5-mainnet'],
    },
    goerli: {
      url: `${process.env.ETH_NODE_URI_goerli}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 5,
      // deploy: ['deploy-seig-manager-v1']
    },
    titan: {
      url: `${process.env.ETH_NODE_URI_TITAN}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 55004,
      // gasPrice: 1000000,
      // deploy: ['deploy_l2_proxy']
    },
    titangoerli: {
      url: `${process.env.ETH_NODE_URI_TITAN_GOERLI}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      chainId: 5050,
      gasPrice: 250000,
      // deploy: ['deploy_l2_proxy']
    },
    sepolia: {
      url: `${process.env.ETH_NODE_URI_sepolia}`,
      accounts: [`${process.env.PRIVATE_KEY}`],
      // deploy: ['deploy_l2_proxy']
      deploy: ['deploy-layer2']
    },
  },
  deterministicDeployment: (network: string) => {
    // Skip on hardhat's local network.
    if (network === "31337") {
      return undefined;
    } else {
      return {
        factory: "0x4e59b44847b379578588920ca78fbf26c0b4956c",
        deployer: "0x3fab184622dc19b6109349b94811493bf2a45362",
        funding: "10000000000000000",
        signedTx: "0x00",
      }
    }
  },
  etherscan: {
    apiKey: {
      mainnet: `${process.env.ETHERSCAN_API_KEY}`,
      goerli: `${process.env.ETHERSCAN_API_KEY}`,
      sepolia: `${process.env.ETHERSCAN_API_KEY}`,
      titan: "verify",
      titangoerli: "verify"
    } ,
    customChains: [
      {
        network: "titan",
        chainId: 55004,
        urls: {
          apiURL: "https://explorer.titan.tokamak.network//api",
          browserURL: "https://explorer.titan.tokamak.network/"
        }
      },
      {
        network: "titangoerli",
        chainId: 5050,
        urls: {
          apiURL: "https://explorer.titan-goerli.tokamak.network/api",
          browserURL: "https://explorer.titan-goerli.tokamak.network/"
        }
      }
    ]
  },
  gasReporter: {
    enabled: true,
    currency: 'USD',
    gasPrice: 21,
    coinmarketcap: `${process.env.COINMARKETCAP_API_KEY}`
  },
  mocha: {
    timeout: 100000000
  },
  solidity: {
    compilers: [
      {
        version: "0.5.12",
      },
      {
        version: "0.8.19",
        settings: {
          // evmVersion: "cancun",
          viaIR: true,
          optimizer: {
            enabled: true,
            runs: 200,
            // details: {
            //   yul: true,
            // },
          },
          metadata: {
            // do not include the metadata hash, since this is machine dependent
            // and we want all generated code to be deterministic
            // https://docs.soliditylang.org/en/v0.8.12/metadata.html
            bytecodeHash: 'none',
          },
        },
      },
    ],
  },
};

export default config;

```

error log for mainnet test
```javascript

  31 passing (5s)
  64 failing

  1) currentAgendaStatus Test on Mainnet
       Setting TON-related Contract
         TON Admin Test:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="balanceOf(address)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  2) currentAgendaStatus Test on Mainnet
       Set Contract
         pauseProxy check:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="pauseProxy()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  3) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check implementation:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="implementation()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  4) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check proxyImplementation(0) = DAOCommittee_V1:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  5) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check proxyImplementation(1) = DAOCommitteeOwner:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  6) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check CandidateAddOnFactory Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="candidateAddOnFactory()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  7) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check Layer2Manager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="layer2Manager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  8) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check daoCommitteeOwner cooldownTime:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="cooldownTime()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  9) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check ton Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="ton()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  10) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check daoVault Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="daoVault()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  11) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check agendaManager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="agendaManager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  12) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check candidateFactory Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="candidateFactory()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  13) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check layer2Registry Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="layer2Registry()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  14) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check seigManager Addr:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="seigManager()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  15) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check maxMember:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="maxMember()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  16) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check quorum:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="quorum()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  17) currentAgendaStatus Test on Mainnet
       Check the Storage
         Check wton:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="wton()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  18) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         upgradeTo2 Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  19) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         increase block time and check votable:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="numAgendas()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  20) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  21) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  22) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  23) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         execute agenda:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  24) currentAgendaStatus Test on Mainnet
       Deploy And CreateAgenda newDAOLogic
         Ensure the agenda is properly executed proxyImplementation(0) = DAOCommittee_V2:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="proxyImplementation(uint256)", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  25) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         1. Return for an Agenda that has not been created:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="numAgendas()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  26) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  27) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  28) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         2. Returns a status called NoticeTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  29) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  30) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         3. Returns (NO CONSENSUS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  31) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  32) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         4. Returns (pending, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  33) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  34) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         5. Returns (ACCEPT, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  35) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  36) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         6. Returns (ACCEPT, WAITING_EXEC):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  37) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         execute agenda (anyone):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  38) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         7. Returns (ACCEPT, EXECUTED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  39) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  40) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  41) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  42) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         8. Returns (NO CONSENSUS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  43) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  44) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         9. Returns (pending, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  45) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  46) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         10. Returns (DISMISS, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  47) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  48) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         11. Returns (DISMISS, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  49) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  50) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  51) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  52) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  53) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  54) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         12. Returns (REJECT, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  55) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  56) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         13. Returns (REJECT, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  57) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         Create new Agenda:
     Error: call revert exception [ See: https://links.ethers.org/v5-errors-CALL_EXCEPTION ] (method="minimumNoticePeriodSeconds()", data="0x", errorArgs=null, errorName=null, errorSignature=null, reason=null, code=CALL_EXCEPTION, version=abi/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Interface.decodeFunctionResult (node_modules/@ethersproject/abi/src.ts/interface.ts:427:23)
      at Contract.<anonymous> (node_modules/@ethersproject/contracts/src.ts/index.ts:400:44)
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  58) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check the agenda Memo:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  59) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         increase block time and check votable:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  60) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member1:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  61) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         castVote member3:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  62) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         14. Returns (PENDING, VOTING):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  63) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         check vote result/status & increase can ExecuteTime:
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)

  64) currentAgendaStatus Test on Mainnet
       currentAgendaVeiw Test
         15. Returns (NO CONSENSUS, ENDED):
     Error: invalid BigNumber value (argument="value", value=undefined, code=INVALID_ARGUMENT, version=bignumber/5.7.0)
      at Logger.makeError (node_modules/@ethersproject/logger/src.ts/index.ts:269:28)
      at Logger.throwError (node_modules/@ethersproject/logger/src.ts/index.ts:281:20)
      at Logger.throwArgumentError (node_modules/@ethersproject/logger/src.ts/index.ts:285:21)
      at Function.BigNumber.from (node_modules/@ethersproject/bignumber/src.ts/bignumber.ts:289:23)
      at NumberCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/number.ts:25:27)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/abi/src.ts/coders/array.ts:71:19
      at Array.forEach (<anonymous>)
      at pack (node_modules/@ethersproject/abi/src.ts/coders/array.ts:54:12)
      at TupleCoder.encode (node_modules/@ethersproject/abi/src.ts/coders/tuple.ts:54:20)
      at AbiCoder.encode (node_modules/@ethersproject/abi/src.ts/abi-coder.ts:111:15)
      at Interface._encodeParams (node_modules/@ethersproject/abi/src.ts/interface.ts:323:31)
      at Interface.encodeFunctionData (node_modules/@ethersproject/abi/src.ts/interface.ts:378:18)
      at /home/jazz/git/ton-staking-v2/node_modules/@ethersproject/contracts/src.ts/index.ts:228:37
      at step (node_modules/@ethersproject/contracts/lib/index.js:48:23)
      at Object.next (node_modules/@ethersproject/contracts/lib/index.js:29:53)
      at fulfilled (node_modules/@ethersproject/contracts/lib/index.js:20:58)




Your solidity settings have viaIR enabled, which is not fully supported yet. You can still use Hardhat, but some features, like stack traces, might not work correctly.

Learn more at https://hardhat.org/solc-viair
```

Overall Feedback
    - The test codes work well
    - The testing process is not seamless. The guidance should be revised to allow testing without requiring additional oversight from the developer. In the current description, it was nearly impossible to finish the test without communication to Harvey.

Mehdi
Testing Sepolia
Testing failed with two types of errors:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/770f11f6-4c96-41bb-bd38-fb07c6ce256d/Capture_decran_2025-06-06_a_12.09.18.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXAHXLTD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQDDVR45CEq5vsPIr7uuVrWD9ez18xXNEElrHHXMkeaAIgUoELgQkLlf6IECG0MBU%2BScwz9iFLsr1%2BIS8E05KBRsMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDECHc7G1hq2yYhJ%2F5ircA2AtALlJyRu2KenM5ZP3O96hWhafTQyj1dtG2esTl5GNBnQbpNm7opuwR8avHXVuLdNjpCiJwHgffb8jf78qkTzaNU3PtI7M1fuNBtkRrzmiYsuXc7uAyzyR7WKTDkrmviOLQPuvmLp8gaPJ7BJgRz1R84K8PuHAOe41gAFp5JqAPasFopeF1fMX6VuRbzXbvSEaNXZPmROgfT9aMMzuCDwyHROK8UyYlPm3C5asCzwPtgnMKT0v2r6PErBPN6qVCM4SGEUe%2B%2FHp4BaIl7OYgSQnFdp6Ga%2FxInwIheY%2Fv0EHOj%2FvQtIUIfsuVideCCrLX1NGCVbk40yG7JDb6y2dq5MSDuUT1s%2FQ7vUJ5PdCRvYoP4iR46lU%2B8QNBhQf%2BRhETTFGbxqnjNxdckpGfnTE7FGXxTSlBY7DWAKeBiEEAC%2FMXN21GkIwt85ccyGFbaBDd5ycfLm5A0CgJCja6UjEivAUzh65B0Lc0v6KmBUBOTZSiWpoE1t75hq3Jm8gpfgZuJ7ERzwfIWcSp1W1LYpUkEgG97x4V6pdLd6cbEUKs6KzF5gSTW0WP4ZL2zBPNJZ5nZTuy0zlUu%2BN49VQrGVakiHOc22DcJC9RhnNvAJl2R12kBlcG%2BAjt32Ng1BJMPuY28wGOqUBPPHxymZk3B%2FryAyCPNFpqgtZfqRC78ZGqHIGKCX1gFsTlAKLOpdjOGk%2FlEiqrKn60CtWQWNPaKLZtESn6ZN255b%2Fv%2BNj1BoAieYDeirtCN4FjxK0bfboTDGahVY83wwyYLgRyRIktLXSB9GkpDjAFql46M0Kb7wmL9EKu8Jyq00JAXDzdj99xchwh23xHOg0TkA%2F7VSrhwkI1QZiVLY88Xj061lI&X-Amz-Signature=9dadb1f8d406936c72262bed087e331d0dc338d7ef69b8a043a924d97f15c2fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/95d46ec2-1286-4002-842e-ecf4323b7849/Capture_decran_2025-06-06_a_12.13.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXAHXLTD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQDDVR45CEq5vsPIr7uuVrWD9ez18xXNEElrHHXMkeaAIgUoELgQkLlf6IECG0MBU%2BScwz9iFLsr1%2BIS8E05KBRsMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDECHc7G1hq2yYhJ%2F5ircA2AtALlJyRu2KenM5ZP3O96hWhafTQyj1dtG2esTl5GNBnQbpNm7opuwR8avHXVuLdNjpCiJwHgffb8jf78qkTzaNU3PtI7M1fuNBtkRrzmiYsuXc7uAyzyR7WKTDkrmviOLQPuvmLp8gaPJ7BJgRz1R84K8PuHAOe41gAFp5JqAPasFopeF1fMX6VuRbzXbvSEaNXZPmROgfT9aMMzuCDwyHROK8UyYlPm3C5asCzwPtgnMKT0v2r6PErBPN6qVCM4SGEUe%2B%2FHp4BaIl7OYgSQnFdp6Ga%2FxInwIheY%2Fv0EHOj%2FvQtIUIfsuVideCCrLX1NGCVbk40yG7JDb6y2dq5MSDuUT1s%2FQ7vUJ5PdCRvYoP4iR46lU%2B8QNBhQf%2BRhETTFGbxqnjNxdckpGfnTE7FGXxTSlBY7DWAKeBiEEAC%2FMXN21GkIwt85ccyGFbaBDd5ycfLm5A0CgJCja6UjEivAUzh65B0Lc0v6KmBUBOTZSiWpoE1t75hq3Jm8gpfgZuJ7ERzwfIWcSp1W1LYpUkEgG97x4V6pdLd6cbEUKs6KzF5gSTW0WP4ZL2zBPNJZ5nZTuy0zlUu%2BN49VQrGVakiHOc22DcJC9RhnNvAJl2R12kBlcG%2BAjt32Ng1BJMPuY28wGOqUBPPHxymZk3B%2FryAyCPNFpqgtZfqRC78ZGqHIGKCX1gFsTlAKLOpdjOGk%2FlEiqrKn60CtWQWNPaKLZtESn6ZN255b%2Fv%2BNj1BoAieYDeirtCN4FjxK0bfboTDGahVY83wwyYLgRyRIktLXSB9GkpDjAFql46M0Kb7wmL9EKu8Jyq00JAXDzdj99xchwh23xHOg0TkA%2F7VSrhwkI1QZiVLY88Xj061lI&X-Amz-Signature=f38b14bc56518b1e08e11116d4fba4095e08c3e3745b4b4f78393756b0a2ab99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

    - Answer @Mehdi 
      - Can you Change the hardhat.config.ts?
      - If you continue to receive this error after looking at the record in the link below, it would be a good idea to call and resolve it together.
      - [https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view](https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view)

@Harvey I was updating the hardhat.config.sepolia.ts file instead of hardhat.config.ts. Now it works. Thanks

Testing Mainnet
Testing successfull

DAOCommitteeV2.sol
    - onApprove ⇒ OK
    - currentAgendaStatus ⇒ OK
    - _decodeAgendaData ⇒ OK
    - _createAgenda ⇒ OK

StorageStateCommitteeV3.sol
    - storage mapping ⇒ OK

George
Sepolia
Same Error invalid BigNumber

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2841571e-0079-4b17-8bbb-eef74b4de1da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXU4OPGC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv8pW3PzWAvBciL296WzuMtIvzygRptjm52xZ%2F7OnxaAIhANgGSvGHIDeWLRQN0kBPw9%2F4wS9e67tIcavSArPfc5D1Kv8DCHoQABoMNjM3NDIzMTgzODA1IgwImpMLreE8294Wcb4q3AM%2Fqxht2%2FdQyL0LsyVV0X98HdBzE%2FkvxPHIM%2BPPzxiM5qQAYgZN3gKoEV%2BqDz7JhylutqHixyt50FykPBfQmST%2BlEMQYPHVmM6JcCumVAJiSaFtfssiLoqNeMvXhKcZd%2FWQr1t5HxmIMt3jW2aL3rA8Di10%2Bf%2FtG9DZ%2FcOKcVWue4WbenKW6I1ThJ5QaG52Ohnxb8v%2Fh2RWYkOIiBtJ0eU9KJ67OpwqC9jn4fq%2BK6aWreDUGi2gnxRf5yjCUo7RiahhxDn4%2FDXjj%2FN2P9jrrTMhFcJQTjL22X8Q1kLIPStMtvbQ3UgVOHig34E1xpdXwgEHV65TUBXkpR0Vb8qdKBhXWrFcRlu%2F5Mz9IL7okBBAnIYttp%2FhyJOxWmmg9AS9Pdf%2ByZycpjmpA5hoUiD7UcjjwKHSxE1DBUuSG3936Fi11DKKEz4aY81IjE%2BURgmy%2FRzrNEfszR5P6k1E6lAGdZD%2BMYDmqXNMmgZBmzbGBCyKXJtHHeoRyRYegtWyN%2B%2F7O889opDBDK8fOMI3GT6Md07R1MUmSNISE6d4P%2FkSyOfEglCEYm6bnIJJTqOrg9r9QO33g4Q3gMMzQufaQMeKTioeRwS2auwYDmO5bHlXWhbTLiJt5UiuaYLOkRZXDTDwmNvMBjqkAbXVls%2FUoaBbv73oP6Hd5nzoBIhHkEsdXpy1Egqq7flY2DQ%2FsudMZ0WAru3fG6mK68AqHaGU9AHAkc%2FBUABTfcrP%2FXO7yuY35FmiTpuov7%2FdajjlIa5Usn5DRa8WJ1AncKtPuyaJ3Bmz7n8PYwBS67Zt2ws0YrjjpFizRhSED3wUlqkCZuvFjrF6q4O0424hdi9JTW%2BQ3YRi4ztAZ%2FJZ7mreRaZI&X-Amz-Signature=dd2add1108f1305ad90a7b126c0152dce4c5970c74ff5efa941c7611bf567d1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

    - Answer @Unknown 
      - Can you Change the hardhat.config.ts?
      - If you continue to receive this error after looking at the record in the link below, it would be a good idea to call and resolve it together.
      - [https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view](https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view)

Mainnet
works fine.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0310a9ba-e2f2-4dea-8bc6-924ff87bbdbe/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZWC26LO%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B6yWXGYgiC8CAZr9NSUvz0hUnt1opnpBH1d7AgLSu8gIhAJ652H6RJ6qOjXXu2DMQ20%2FwVK%2B3vh%2F6f%2F6kAreGEvffKv8DCHoQABoMNjM3NDIzMTgzODA1IgyiqaXJYe7NcnXMt8Qq3APYGYP25EyGeMlhO%2FkVE%2FIq1wA8%2Bwt0GmjdNVnwrH%2FWa4cg7uoUymuRgXesvyyN3knSpDOPGgdYyML%2Bn3%2BzLfPx8YUpMrZTxPnbt527QmuQi1xQ%2FNF5sXXvexrf3DAwSR6kn1ibwrnlOqecVDAgWmX%2BwJvfu5%2BUdtVQrGHwgVMUQ8s2nluF%2Be6%2FhEVbKbUY72SKvMCgXG1P6EqxZDZilszkWSMFc1HSBJA%2Bsgr%2Bi6rcS4%2FMrU7a%2Fw%2FB2X5DISZFUjxYPNrw3ZUka1iLC1W1KHbdOGNIUN65f%2BzVWfPnU2MeTQ%2FhV%2FBHfMXTflQt%2BD2wE2zsO%2B0HA8TyWpLixWDhSygXULpbe8QAvTihzZ7%2FzRkWXDJj2eeWsBDER15pmV9noKfh3l6W2Y5hjNUd8D4%2FNOOb5lkQ%2BUFpHrb31x0Vxlay5TQ3CwIIek6oBpTP2%2Bat%2FNwgs2up%2BLuE1S7Wvd4zyqicKnsjDiaPfc6OT0WHNobUEkLbLyD%2BoJH0VJtisVW45iTQEoXNZIwY32kAES22JQhsb3iCMNfwbGTGWGk7y2%2BLbqlOqwGcOQXNwSKTJSlFQjPZ%2B9%2BUe4m%2Fq%2FlR50jGOkFQlHBS4dYvD5wT5mi3yAN6WiQwOyWl2j7ChCm21DDwmNvMBjqkASz2VVgi2AbkYH8NkELJEYURa%2BoIh%2BaTbLDLV9mkQeBplr%2BSGdU55mvLPNJWv11zk0t9X7Tiz2LT9M5d2TjBIFlPXGl6D3bj1qtMpyAyD%2B%2FulI8nZOgmh1zR6JBqgFLKwIRP7%2FrOSh2kG%2BMMIJf7iaFum4xixsCxk%2BuQwlmM%2FkvJePTufhMaDac1X3zefDTpkQbiNDBnpt8h4YfCpdSBPRjCB1Tn&X-Amz-Signature=bedced8a2422dff624e06f7cde6e7b4b387e2b00f47e8fe5ccba927fe5bc9b87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Justin
**No security vulnerabilities identified** - There are no breaking changes, the memo is simply stored as a string mapping

Hammer
  - It would be better to change the inspection logic of onApprove as below and hard code the calldata of claimERC20Bytes into the contract as signature + TON Address and compare them!
```solidity
for (uint256 i; i < agendaData.target.length; i++) {
    if (agendaData.target[i] == address(daoVault)) {
        bytes memory abc = agendaData.functionBytecode[i];
        bytes memory selector1 = abc.slice(0, 4);

        if (selector1.equal(claimTONBytes)) revert ClaimTONError();
        if (selector1.equal(claimWTONBytes)) revert ClaimWTONError();
        if (selector1.equal(claimERC20Bytes)) {
            bytes memory tonaddr = _toBytes(ton);
            bytes memory ercaddr = abc.slice(16, 20);
            bool check3 = ercaddr.equal(tonaddr);
            require(!check3, "claimERC20 ton dont use");
        }
    }
}
```

    - A : The order of the if statement has been changed.
If the signature + TON Address values are fixed, the contract bytecode values of Sepolia and Mainnet will be different.
This requires separate management of the contracts for Sepolia and Mainnet, so we decided not to apply it.
    - Commit : [https://github.com/tokamak-network/ton-staking-v2/commit/c478ade707eaffc64408ea6e9b4cec39c7cdbccc](https://github.com/tokamak-network/ton-staking-v2/commit/c478ade707eaffc64408ea6e9b4cec39c7cdbccc)
  - You should change currentAgendaStatus to not additionally validate values that have already been validated in the upper conditional statement.
    - Commit : [https://github.com/tokamak-network/ton-staking-v2/commit/1dd8df15a622c221be9619977f21620b74f870fa](https://github.com/tokamak-network/ton-staking-v2/commit/1dd8df15a622c221be9619977f21620b74f870fa)