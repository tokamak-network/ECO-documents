- **Repo**: [https://github.com/tokamak-network/ton-staking-v2/tree/deploy-ton-staking-v2.5](https://github.com/tokamak-network/ton-staking-v2/tree/deploy-ton-staking-v2.5) 

# Deploy contracts 

- Candidate 이름 확인 :  Titan DAO 
- 아젠다 생성전에 생성한 컨트랙의 오너를 모두 DAO로 바꾼다. 

`npx hardhat deploy --network mainnet `

- deployer:  **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F**
- check to set values 

```javascript
 === ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26'
  },
  Layer2Manager: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' },
  OperatorManagerFactory: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' },
  Titan: {
    proxyOwner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0x340C44089bc45F86060922d2d89eFee9e0CDF5c7'
  }
}

 === Titan Candidate ===
name:  Titan DAO
addresses:  {
  l1CrossDomainMessenger: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
  l1ERC721Bridge: '0x0000000000000000000000000000000000000000',
  l1StandardBridge: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
  l2OutputOracle: '0x0000000000000000000000000000000000000000',
  optimismPortal: '0x0000000000000000000000000000000000000000',
  optimismMintableERC20Factory: '0x0000000000000000000000000000000000000000'
}
```

- the deployment transactions  

```javascript

=== ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26'
  },
  Layer2Manager: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' },
  OperatorManagerFactory: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' },
  Titan: {
    proxyOwner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0x340C44089bc45F86060922d2d89eFee9e0CDF5c7'
  }
}

 === Titan Candidate ===
name:  Titan DAO
addresses:  {
  l1CrossDomainMessenger: '0xfd76ef26315Ea36136dC40Aeafb5D276d37944AE',
  l1ERC721Bridge: '0x0000000000000000000000000000000000000000',
  l1StandardBridge: '0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD',
  l2OutputOracle: '0x0000000000000000000000000000000000000000',
  optimismPortal: '0x0000000000000000000000000000000000000000',
  optimismMintableERC20Factory: '0x0000000000000000000000000000000000000000'
}
deployer 0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F
deploying "L1BridgeRegistryV1_1" (tx: 0x80c3fd40ae3852bd0248b5f3b06d346015bcc2e6a738dba2b1b140489590091c)...: deployed at 0x70aFe7e41e7F7406BCC446f652e2f94ae5b76282 with 2523958 gas
deploying "L1BridgeRegistryProxy" (tx: 0x2332fa1562d35c4bca2f1a769529feee55bcdf5b72686a8861dc51e58ea0e8d4)...: deployed at 0x17Fa32DFf4c26cf0AC65Ff6700B57a4826513Fa0 with 1864283 gas
deploying "OperatorManagerV1_1" (tx: 0xd375ad64ffb8b3d442685328b4a2a1b4d84edff511befe56a696d3184c1b4371)...: deployed at 0x8522234116A0E5fAb2AC469d9d7Ad8381DE0BEE9 with 1555619 gas
deploying "OperatorManagerFactory" (tx: 0xe8ffb7a51a63f1f064a8b391d174d198b086ae188e110421b760f5c371345004)...: deployed at 0x79f3DfCC532b3876eE7f2e02C7A92Ca7F7a7a307 with 1079274 gas
deploying "CandidateAddOnV1_1" (tx: 0x4933d35b30b69fa2f20ca442489ac3d3c0edbe394618fc2e82a88e9711157c5b)...: deployed at 0x324b3C030A76c85AaC0B4B85bDc560D0df32f58B with 2099110 gas
deploying "CandidateAddOnFactory" (tx: 0xdb3b3522627cbe8dba521607860ce5d5944899bcd944ee5ed7265cc21b104e17)...: deployed at 0xBda1647ED13483BA68957874BAFB2E5A6E508900 with 2622515 gas
deploying "CandidateAddOnFactoryProxy" (tx: 0x29f1aa3659c02bede113719e5ea6be830c85c82baeb0255df4e9ee8f249edc06)...: deployed at 0x61a80Dcf8269f18Ed9bb6C563035651A1756B263 with 1418724 gas
deploying "Layer2ManagerV1_1" (tx: 0xfeb23e66d0eb0ba767fa00e4f1972fa9985a04bbd54947512fe003a99e88d60a)...: deployed at 0x2A25b0Cf9969b292e7fBa9c4429e371D1F4DCE08 with 2657338 gas
deploying "Layer2ManagerProxy" (tx: 0xdea979a20152b295afe3e055529b4de7c398cc6e125e2a48340472c2c09eedf7)...: deployed at 0xC534047FFD60c151E818C4Ac5A51fFbC234A3F77 with 1491085 gas
deploying "SeigManagerV1_3" (tx: 0x57164250eb0156a88fa0c7a4d47336200e8d697907fddb423037972c41a9ef8b)...: deployed at 0xBC71FB7373Fe0dD9Fc003D7850D710d5aAd98750 with 4035692 gas
deploying "DepositManagerV1_1" (tx: 0xa4e9adfb2d98b3aff9404595840f4f7906a0979df28bf67b62da77883b33042a)...: deployed at 0x769E782b60e80A395096aA9eb42A910A2b25DD52 with 1655731 gas
deploying "DAOCommitteeProxy2" (tx: 0xe889729eec738c64243f128f3085df236870d855fcda0115dc1da098037bb0fd)...: deployed at 0xD6175F575F4d32392508Ee2FBbDec9a2E8B3c01a with 1282977 gas
deploying "DAOCommitteeOwner" (tx: 0xbbf0e0af8e78b73011e48b329d7fe4b8ff0c1a4105b3e2e81594c6cc4a976539)...: deployed at 0x5991Aebb5271522d33C457bf6DF26d83c0dAa221 with 2471593 gas
deploying "DAOCommittee_V1" (tx: 0xb21af84262468ac0eaf54c040d0c6d32ed5a5ce60533ec81e4a53c98727038c7)...: deployed at 0xcC88dFa531512f24A8a5CbCB88F7B6731807EEFe with 4453991 gas
deploying "LegacySystemConfig" (tx: 0x34d87efb9db2b81777950119eef11ef163b3c86813929d56879a08f626dea3bb)...: deployed at 0xBa962e2150fAd0Da33462e9891138b6a0fEaCA65 with 569610 gas
deploying "LegacySystemConfigProxy" (tx: 0x3bd5b2aab3740a858979403f2a75afa59a5a37dc8ef39e9ccc0121182096d5cf)...: deployed at 0xB8439E3939647746821dE85b0d3A50460147b292 with 619611 gas
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
[Titan RollupConfig] legacySystemConfig.proxyOwner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
[Titan RollupConfig] legacySystemConfig.owner():  0x340C44089bc45F86060922d2d89eFee9e0CDF5c7
```

# Deployed Addresses 

```javascript
"L1BridgeRegistryV1_1"  0x70aFe7e41e7F7406BCC446f652e2f94ae5b76282 
"L1BridgeRegistryProxy" 0x17Fa32DFf4c26cf0AC65Ff6700B57a4826513Fa0 
"OperatorManagerV1_1" 0x8522234116A0E5fAb2AC469d9d7Ad8381DE0BEE9 
"OperatorManagerFactory" 0x79f3DfCC532b3876eE7f2e02C7A92Ca7F7a7a307 
"CandidateAddOnV1_1"  0x324b3C030A76c85AaC0B4B85bDc560D0df32f58B 
"CandidateAddOnFactory"  0xBda1647ED13483BA68957874BAFB2E5A6E508900 
"CandidateAddOnFactoryProxy"  0x61a80Dcf8269f18Ed9bb6C563035651A1756B263 
"Layer2ManagerV1_1"  0x2A25b0Cf9969b292e7fBa9c4429e371D1F4DCE08 
"Layer2ManagerProxy" 0xC534047FFD60c151E818C4Ac5A51fFbC234A3F77 
"SeigManagerV1_3"  0xBC71FB7373Fe0dD9Fc003D7850D710d5aAd98750 
"DepositManagerV1_1"  0x769E782b60e80A395096aA9eb42A910A2b25DD52 
"DAOCommitteeProxy2" 0xD6175F575F4d32392508Ee2FBbDec9a2E8B3c01a 
"DAOCommitteeOwner"  0x5991Aebb5271522d33C457bf6DF26d83c0dAa221 
"DAOCommittee_V1"  0xcC88dFa531512f24A8a5CbCB88F7B6731807EEFe 
"LegacySystemConfig"  0xBa962e2150fAd0Da33462e9891138b6a0fEaCA65 
"LegacySystemConfigProxy"  0xB8439E3939647746821dE85b0d3A50460147b292
```

받음: 0.56 ETH 

잔액: 0**.**222419661207069 ETH 

보냄: [https://etherscan.io/tx/0x4cdd97665ad1dbccf31c1d7a119140804af4618e09b9af9758f4b0b5f9be7e70](https://etherscan.io/tx/0x4cdd97665ad1dbccf31c1d7a119140804af4618e09b9af9758f4b0b5f9be7e70)

## Expected Used Gas 

[https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0)

# Submit an agenda

proposer: **0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea**

```javascript

function1 : upgradeTo (DAO)
function2 : upgradeTo2 (DAO)
function3 : setImplementation2 (DAO)
function4 : setSelectorImplementations2 (DAO)
function5 : setImplementation2 (SeigManager)
function6 : setSelectorImplementations2 (SeigManager)
function7 : setImplementation2 (DepositManager)
function8 : setSelectorImplementations2 (DepositManager)
function9 : setCandidateAddOnFactory (DAO)
function10 : setLayer2Manager (DAO)
function11 : setLayer2Manager (SeigManager)
function12 : setL1BridgeRegistry (SeigManager)
function13 : setAddresses (DepositManager)
function14 : registerRollupConfigByManager (L1BridgeRegistry)

tx : 0x61a58533689b3753e2203dcd9abd8a7b42462e63c1cf04833bb4a6910d2dcccf
```

Create Agenda tx : [https://etherscan.io/tx/0x61a58533689b3753e2203dcd9abd8a7b42462e63c1cf04833bb4a6910d2dcccf](https://etherscan.io/tx/0x61a58533689b3753e2203dcd9abd8a7b42462e63c1cf04833bb4a6910d2dcccf)

반환 : [https://etherscan.io/tx/0x0b3b9ee0fa7f41a6970f2c1e7251de2c1204ddc74c69cbca222f396e7fbb7887](https://etherscan.io/tx/0x0b3b9ee0fa7f41a6970f2c1e7251de2c1204ddc74c69cbca222f396e7fbb7887)

반환 금액 : 0**.**189521033145823 ETH

[[DAO Agenda Description]]

# Addresses  

```javascript
SeigManagerProxy : 0x0b55a0f463b6defb81c6063973763951712d0e5f
DepositManagerProxy : 0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e
DAOAgendaManager: 0xcD4421d082752f363E1687544a09d5112cD4f484
DAOCommitteeProxy: 0xDD9f0cCc044B0781289Ee318e5971b0139602C26


TON: 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5
WTON: 0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2

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

#  