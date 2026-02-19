- **Repo**: [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)

Refer [[Deploy TON-Staking-v2  on Mainnet ]] 

[[Deploy TON-Staking-v2  on Mainnet ]] 

### Expected Used Gas 

- [https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=653462001#gid=653462001](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=653462001#gid=653462001)
- gasUsed : 2,686,198
- 0.0189 ETH (7Gwei 기준)
- 10 TON

# Submit an agenda

proposer: 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6 

```javascript

function1 : upgradeTo (DAO)
function2 : upgradeTo2 (DAO)
function3 : setImplementation2 (DAO)
function4 : setSelectorImplementations2 (DAO)

function5 : SeigManager.upgradeTo (0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4 )

function6 : SeigManager.setImplementation2 (0xce18C6F84F10881eA47A43AF7311A29bb116F628, 1, true)

function7 : SeigManager.setSelectorImplementations2 ( ['0x764a7856','0x1e1f0b60','0x5015cb2b','0x2c1e0156','0x54798b55','0xd732785e','0x8456cb59','0x3f4ba83a'], 0xce18C6F84F10881eA47A43AF7311A29bb116F628 )

function8 : DepositManager.setImplementation2 (0x74bC3031b9369e6b898e82784106257D4D37Eac5, 2, true)

function9 : DepositManager.setSelectorImplementations2 ( ['0xcc48b947','0xdd283f97','0x1c9283a3','0x9f382d11','0xcf8f9110','0x16b5d5bd','0x90107afe','0xda95ebf7' ], 0x74bC3031b9369e6b898e82784106257D4D37Eac5)

function10 : DAO.setCandidateAddOnFactory (0xFA8ce5caF456115E72B96E5074769b8f66AA5861)

function11 : DAO.setLayer2Manager (0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D)

function12 : SeigManager.setLayer2Manager (0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D)

function13 : SeigManager.setL1BridgeRegistry (0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4)

function14 : DepositManager.setAddresses (0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4, 0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D)


function15 : setCooldownTime (DAO) (3일 : 259200)

```

Create Agenda tx :  [https://etherscan.io/tx/0x6586038041b73be4311dec3d8e1fbd011b8dfef1bc98014e3db51a5a81ced779](https://etherscan.io/tx/0x6586038041b73be4311dec3d8e1fbd011b8dfef1bc98014e3db51a5a81ced779)

## DAO Agenda 페이지에서 아젠다 확인

-  [https://dao.tokamak.network/#/agenda](https://dao.tokamak.network/#/agenda)
- Agenda #14 : [https://dao.tokamak.network/#/agenda/14](https://dao.tokamak.network/#/agenda/14)

## 톤 유통량 집계 페이지 에 아젠다 burn 금액 반영

- [https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004)
- J열 ( Burned: TON (Team+DAO) ) 열에 10 TON 적고, 우측에 해당 트랜잭션 넣어두기 

## 사용한 TON, ETH 

입금 tx

- TON
  - [https://etherscan.io/tx/0x9a5eec4578b5646b54f7f7fa8a6b823c4d545960abde1d7577638ee9f886d7b9](https://etherscan.io/tx/0x9a5eec4578b5646b54f7f7fa8a6b823c4d545960abde1d7577638ee9f886d7b9)
- ETH
  - [https://etherscan.io/tx/0xf4e95a5df039e62d885eac8603cf4cc57fa4d1ff94442d3aa7a6ec084a2f1725](https://etherscan.io/tx/0xf4e95a5df039e62d885eac8603cf4cc57fa4d1ff94442d3aa7a6ec084a2f1725)

반환 tx

- ETH
  - [https://etherscan.io/tx/0xdcea70d05d7bddc83c2e067f55de4f69a1fb6e9a1dd765ca62b90734ec2411fe](https://etherscan.io/tx/0xdcea70d05d7bddc83c2e067f55de4f69a1fb6e9a1dd765ca62b90734ec2411fe)

반환 금액 :   0**.**0486 ETH

[[DAO Agenda Description]]

# Addresses  

```javascript
SeigManagerProxy : 0x0b55a0f463b6defb81c6063973763951712d0e5f
DepositManagerProxy : 0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e
DAOAgendaManager: 0xcD4421d082752f363E1687544a09d5112cD4f484
DAOCommitteeProxy: 0xDD9f0cCc044B0781289Ee318e5971b0139602C26


TON: 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5
WTON: 0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2


"L1BridgeRegistryProxy"   0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4 
"CandidateAddOnFactoryProxy"   0xFA8ce5caF456115E72B96E5074769b8f66AA5861 
"Layer2ManagerProxy"   0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D 
"DAOCommitteeProxy2"   0x9e7f54efF4A4D35097e0Acb6994A723F1a28368c  
"DAOCommitteeOwner"   0xcb9859Dc0fBECa68eFFf2bce289150513fdF7D92  
"DAOCommittee_V1"   0x9050Af1638f379A018737880aD946CdDA9101A25  
"SeigManagerV1_2"   0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4 
"SeigManagerV1_3"   0xce18C6F84F10881eA47A43AF7311A29bb116F628
```

- DAOCommitteeProxy 

```javascript
DAOCommitteeProxy 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
old implementation: 0xdF2eCda32970DB7dB3428FC12Bc1697098418815  (DAOCommittee_V1) 
_implementation: (DAOCommitteeProxy2)
proxyImplementation[0]:    (DAOCommittee_V1)
proxyImplementation[1]:    (DAOCommitteeOwner)
```

- SeigManagerProxy

```javascript
SeigManagerProxy   0x0b55a0f463b6defb81c6063973763951712d0e5f
implementation(0):  0x8813C76858C2fc048B14Bd4c75F2Daee43c79958 (SeigManagerV1_2) 
implementation(1):  0x0000000000000000000000000000000000000000
implementation(2):  

```

- DepositManagerProxy

```javascript
DepositManagerProxy   0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e
implementation(0):  0x76C01207959DF1242C2824B4445CdE48eb55D2f1 (DepositManager
)
implementation(1):  0xAB9231f3081B5C3C27d34Ed4CEFc1280f89ff687 (DepositManager_setWithdrawalDelay) 
implementation(2):   0x0000000000000000000000000000000000000000

```

#  Agenda Contents Detail

1. DAOCommitteeProxy의 upgradeTo함수를 이용해 DAOCommitteeProxy2 주소를 호출합니다.
  1. daoCommitteeProxy.upgradeTo(**DAOCommitteeProxy2Addr**)
1. DAOCommitteeProxy2의 upgradeTo2함수를 이용해 DAOCommittee_V1 주소로 호출합니다. (함수는 DAOCommitteeProxy2에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.upgradeTo2(**DAOCommittee_V1Addr**)
1. DAOCommitteeProxy2의 setImplementation2함수를 호출합니다. (함수는 DAOCommitteeProxy2에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.setImplementation2(**daoCommitteeOwnerAddr**,1,true)
1. DAOCommitteeProxy2의 setSelectorImplementations2함수를 호출합니다. (함수는 DAOCommitteeProxy2에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.setSelectorImplementations2(functions,**daoCommitteeOwnerAddr**)
1. SeigManagerProxy의 upgradeTo함수를 호출합니다.
  1. seigManagerProxy.upgradeTo(**seigManagerV1_2Addr**)
1. SeigManagerProxy의 setImplementation2함수를 호출합니다
  1. seigManagerProxy.setImplementation2(**seigManagerV1_3Addr**,1,true)
1. SeigManagerProxy의 setSelectorImplementations2함수를 호출합니다
  1. seigManagerProxy.setSelectorImplementations2(functionBytecodes,**seigManagerV1_3Addr**)
1. DepositManagerProxy의 setImplementation2함수를 호출합니다.
  1. depositManagerProxy.setImplementation2(**depositManagerV1_1Addr**,2,true)
1. DepositManagerProxy의 setSelectorImplementations2함수를 호출합니다.
  1. depositManagerProxy.setSelectorImplementations2(functionBytecodes,**depositManagerV1_1Addr**)
1. DAOCommitteeOwner의 setCandidateAddOnFactory함수를 호출합니다. (함수는 DAOCommitteeOwner에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.setCandidateAddOnFactory(**candidateAddOnFactoryProxyAddr**)
1. DAOCommitteeOwner의 setLayer2Manager함수를 호출합니다. (함수는 DAOCommitteeOwner에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.setLayer2Manager(**Layer2ManagerProxy**)
1. SeigManagerV1_2의 setLayer2Manager함수를 호출합니다. (함수는 SeigManagerV1_2의 함수를 사용하지만 호출 주소는 SeigManagerProxy 입니다.)
  1. seigManagerProxy.setLayer2Manager(**Layer2ManagerProxy**)
1. SeigManagerV1_2의 setL1BridgeRegistry함수를 호출합니다. (함수는 SeigManagerV1_2의 함수를 사용하지만 호출 주소는 SeigManagerProxy 입니다.)
  1. seigManagerProxy.setL1BridgeRegistry(**L1BridgeRegistryProxy**)
1. depositManagerV1_1의 setAddresses함수를 호출합니다. (함수는 depositManagerV1_1의 함수를 사용하지만 호출 주소는 depositManagerProxy 입니다.)
  1. depositManagerProxy.setAddresses(**L1BridgeRegistryProxy,Layer2ManagerProxy**)
1. DAOCommitteeOwner의 setCooldownTime함수를 호출합니다. (함수는 DAOCommitteeOwner에 있는 함수를 사용하지만 호출 주소는 DAOCommitteeProxy 입니다.)
  1. daoCommitteeProxy.setCooldownTime(3일)