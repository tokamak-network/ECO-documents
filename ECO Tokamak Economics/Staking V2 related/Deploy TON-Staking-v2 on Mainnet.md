- 

# Deploy TON staking V2 Contracts 

### Expected Used Gas 

[https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=1111221829#gid=1111221829](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=1111221829#gid=1111221829)

- 예상 배포 가스비 :   38,868,869 gas , 0.194344345 ETH  ( gasPrice: 5gwei 기준)
- ETH transfer (kevin→harvey) : [https://etherscan.io/tx/0x7a5b56a6ddcc8324c894397f233bffcd98d1e6fe161221d4ce5e81f3c39d12e3](https://etherscan.io/tx/0x7a5b56a6ddcc8324c894397f233bffcd98d1e6fe161221d4ce5e81f3c39d12e3) 
  - from : 0x340C44089bc45F86060922d2d89eFee9e0CDF5c7 
- ETH transfer (harvey→zena) :  [https://etherscan.io/tx/0x7c685b488a1d1d9c6129ad03d53587c8079a29e63134af4bdc2b42ff9a0d6c52](https://etherscan.io/tx/0x7c685b488a1d1d9c6129ad03d53587c8079a29e63134af4bdc2b42ff9a0d6c52)
- ETH transfer (zena→kevin) : [https://etherscan.io/tx/0xf6004d374ad624f7fdd19feeef6f3241e4013dea7dfb2c05cdc67f01010698f2](https://etherscan.io/tx/0xf6004d374ad624f7fdd19feeef6f3241e4013dea7dfb2c05cdc67f01010698f2)
  - to:   0x340C44089bc45F86060922d2d89eFee9e0CDF5c7

## [Harvey] deploy MultisigWallet 

- Repo : [GitHub - tokamak-network/tokamak-multisig-wallet at simpleVersion](https://github.com/tokamak-network/tokamak-multisig-wallet/tree/simpleVersion)
- deploy 실행 계정  : 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- 필요한 데이터
  - 멀티시그월렛의 오너 계정 3개 
  - Owners :
    - 0x77b9D55e98126CD457D8F914647e634613D2A7fc
    - 0x9de8cAc67B6514837c31F367aC18a457d8f34c3D
    - 0xa4ABB4Bb512Fc1fecF5556ADDa9B8a4C96dc3790
- 실행 명령어 
  - npx hardhat run scripts/deploy.js --network mainnet
  - npx hardhat verify --constructor-args arguments.js 0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95 --network mainnet
- tx
  - [https://etherscan.io/tx/0xf97c035481c4498afaefd0de3cb1584029b23d309d604da17308578af6f78af1](https://etherscan.io/tx/0xf97c035481c4498afaefd0de3cb1584029b23d309d604da17308578af6f78af1)
- 실행결과 확인 
  - [https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#code](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#code)
  - MultisigWallet Contract : **0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95**
    - getOwners : [link](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract) 
[[0x77b9D55e98126CD457D8F914647e634613D2A7fc]

[0x9de8cAc67B6514837c31F367aC18a457d8f34c3D]

[0xa4ABB4Bb512Fc1fecF5556ADDa9B8a4C96dc3790]]
    - isOwner : [link](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract)  (배포 주소 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6는 false나오는 것 확인)
    - owners : [link](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract) 
- MultiSigWalletCreate Contract 2,286,247

## [Kevin] change DAO’s owner to MultisigWallet 

멀티시그 월렛에게 다오의 오너 권한을 부여한다. 

- 실행 계정  :  0xB4983DA083A5118C903910DB4f5a480B1D9f3687 (DAO의 Owner계정)
- 실행 방법
  - [https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeContract#F2](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeContract#F2)
  - grantRole
    - role : 0x0000000000000000000000000000000000000000000000000000000000000000
    - account : 0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95
- tx
  - [https://etherscan.io/tx/0x9e85908ae5d27fd1bf9d118a33d69efa657af3bd73adc1ecb9fe0c397ed22944](https://etherscan.io/tx/0x9e85908ae5d27fd1bf9d118a33d69efa657af3bd73adc1ecb9fe0c397ed22944)
- 실행결과 확인 
  - [https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11)
  - hasRole
    - role : 0x0000000000000000000000000000000000000000000000000000000000000000
    - account : 0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95
  - result 
    - true (나와야하는 값, 확인완료)

## [Kevin] MultiSigWallet. submitTransaction  

다오의 EOA 오너의 권한을 삭제하는 안건을 제출한다. 

- 실행 계정  :  0x9de8cAc67B6514837c31F367aC18a457d8f34c3D (MultiSigWallet의 Owner 계정)
- 실행 방법
  - 배포된 MultiSigWallet의 [etherscan](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F5)  
  - submitTransaction [link](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F5)
    - _to : 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 (DAOCommitteeProxy)
    - _value : 0 (no send ETH)
    - _data : 0xd547741f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b4983da083a5118c903910db4f5a480b1d9f3687 (d547741f = revokeRole함수 selector, b4983da083a5118c903910db4f5a480b1d9f3687 = revoke할 주소)
- tx
  - [https://etherscan.io/tx/0x8e3d688d38ffa888c1aba559f50f2e0eeed1ac6dc702934c1fd563493c0ed7f6](https://etherscan.io/tx/0x8e3d688d38ffa888c1aba559f50f2e0eeed1ac6dc702934c1fd563493c0ed7f6)
- 실행결과 확인 
  - MultiSigWallet의 etherscan page의 Read Contract의 3. getTransactionCount값 확인
  - [https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F3](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F3)
  - result
    - 1 (나와야하는 값, 확인완료)

## [Kevin] MultiSigWallet. confirmTransaction  

다오의 EOA 오너의 권한을 삭제하는 안건을 승인한다. 

- 실행 계정  :   0x77b9D55e98126CD457D8F914647e634613D2A7fc (submitTransaction을 실행한 계정과 다른 owner 계정)
- 실행 방법
  - 배포된 MultiSigWallet의 [etherscan](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F2) 
  - [confirmTransaction](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F2) 
    - _txIndex : 0
- tx : [https://etherscan.io/tx/0x2d06c547f2e7e163a4dd88466c7f5abb211bd0c66b517015e8a2b1bc58b40fa2](https://etherscan.io/tx/0x2d06c547f2e7e163a4dd88466c7f5abb211bd0c66b517015e8a2b1bc58b40fa2)
- 실행결과 확인 
  - MultiSigWallet의 etherscan page의 Read Contract의 4. isConfirmed 값 확인
  - [https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F4](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F4)
    - uint256 : 0
    - address : 0x77b9D55e98126CD457D8F914647e634613D2A7fc
  - result
    - true (나와야하는 값, 확인완료)

## [Kevin] MultiSigWallet. executeTransaction  

다오의 EOA 오너의 권한을 삭제하는 안건을 실행한다.  

- 실행 계정  :  (Owner로 설정한 계정들 중 아무 계정이나 실행가능)
- 실행 방법
  - 배포된 MultiSigWallet의 [etherscan](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F3) (배포 후 수정)
  - [executeTransaction](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#writeContract#F3)
    - _txIndex : 0
- tx
  - [https://etherscan.io/tx/0xba6c643ad25fb1e04b1790928cb2dafaa1bada240bcded22b2aece08b3db09d0](https://etherscan.io/tx/0xba6c643ad25fb1e04b1790928cb2dafaa1bada240bcded22b2aece08b3db09d0)
- 실행결과 확인
  -  MultiSigWallet의 etherscan page의 Read Contract의 2. getTransaction 값 확인
  - [https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F2](https://etherscan.io/address/0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95#readContract#F2)
    - uint256 : 0
  - result
    - executed : true (나와야하는 값)
  - [https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11)
    - role : 0x0000000000000000000000000000000000000000000000000000000000000000
    - account : 0xB4983DA083A5118C903910DB4f5a480B1D9f3687
  - result
    - false
- DAO CooldownTime = 72시간 (changeMember 실행 후 다시 실행할 수 있는데 까지 걸리는 시간 [후보자 각각 시간이 다름])

## [Zena] deploy TON Staking 

- **Repo**: [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)

배포후, 아젠다 생성전에 생성한 컨트랙의 오너를 모두 DAO로 바꾼다. 

`npx hardhat deploy --network mainnet `

- deployer:  **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F**
- check to set values [code](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/deploy-staking-v2.5-mainnet/0.deploy.ts) 

```javascript
 === ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    seigniorageCommittee: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26'
  },
  Layer2Manager: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' },
  OperatorManagerFactory: { owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26' }
}
 
```

- the deployment transactions  

```javascript

 
deployer 0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F
deploying "L1BridgeRegistryV1_1" (tx: 0x9510b0b6021e50706771ed43143f8ee5fede24e73148827c6c630819fc8e7ae4)...: deployed at 0x259Ac335EB42d345A61bE48104eC0Ec20b283F14 with 2405573 gas
deploying "L1BridgeRegistryProxy" (tx: 0xebdf3ff64f0db31be4c08a083be9f942b23cd00b3b634f982dfd41272f76b243)...: deployed at 0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4 with 1979058 gas
deploying "OperatorManagerV1_1" (tx: 0x1e67f8b4760742acf58ba220ff988fafb2f4c3c9359ce318d48dbc75eff40c61)...: deployed at 0xB5F3b31dFB4DCe9a2FA12dE50A97250d60823750 with 1247734 gas
deploying "OperatorManagerFactory" (tx: 0x3737cb1cada96576fe46786608a4daf448f95fed7a43e4ef9dfe54e81de1e76c)...: deployed at 0xAf86b21edDdC78ea27E23A7F2151d60d4e069450 with 1086529 gas
deploying "CandidateAddOnV1_1" (tx: 0x38cb0e701c23e397ed8fdc0f6fa5b4aa4516be04522bfd168b9b6b28be265c70)...: deployed at 0x73Bfd5cAEC63307784C7B6d2555F18ec24D96E2e with 1801036 gas
deploying "CandidateAddOnFactory" (tx: 0x5c4044e871d677ee662c518fb14902a05f3a55ef6bc3217d705ac47d4e190b0f)...: deployed at 0x557E24b5CbFbDA3e5aC1bD01F38EcDe865791Bc5 with 2681314 gas
deploying "CandidateAddOnFactoryProxy" (tx: 0xbe9d8e180fe4d324b6b8cacc2f7857731744489a6076744a38ae1553d3f850af)...: deployed at 0xFA8ce5caF456115E72B96E5074769b8f66AA5861 with 1489240 gas
deploying "Layer2ManagerV1_1" (tx: 0x3b2e2e24328eb72dc89714645fd628664a71ca381ecdd11e127acdd1a449b163)...: deployed at 0x2EB7f500125f11544392B83B87cDEb9456f3509f with 2677767 gas
deploying "Layer2ManagerProxy" (tx: 0x9cce9532345917fda587ca449b460b54a0156a21a79a352480026c0e44ffa2ca)...: deployed at 0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D with 1577795 gas
deploying "SeigManagerV1_2" (tx: 0xbf1ad3e583ae4e59ea5863eabc1dfa8878f2d455c2b6d3cc01517dadc4358f3d)...: deployed at 0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4 with 5322969 gas
deploying "SeigManagerV1_3" (tx: 0x469b2dda84c4694113c2ca8ed721e33524c872e3de268ac3ac0cb9fd277fb3b3)...: deployed at 0xce18C6F84F10881eA47A43AF7311A29bb116F628 with 3482067 gas
deploying "DepositManagerV1_1" (tx: 0x092c57a96eb7f8ad39c27544f4fcdb6582046d932c2ce938bc933affb5618de8)...: deployed at 0x74bC3031b9369e6b898e82784106257D4D37Eac5 with 1853596 gas
deploying "DAOCommitteeProxy2" (tx: 0xc6e5baea2c74c223c566a478dcfd9241f2a48918daa2ce623a9dbb201ba7af1c)...: deployed at 0x9e7f54efF4A4D35097e0Acb6994A723F1a28368c with 1381834 gas
deploying "DAOCommitteeOwner" (tx: 0x6f375e4993f0d28a893ef17ef6319aab231cb47d06ffc43e7cd702b8a8c199a1)...: deployed at 0xcb9859Dc0fBECa68eFFf2bce289150513fdF7D92 with 1983810 gas
deploying "DAOCommittee_V1" (tx: 0x5d3f35a22b27c90e0860780f97b385e205e5f41175cc4ba59a2245c53daecb32)...: deployed at 0x9050Af1638f379A018737880aD946CdDA9101A25 with 4744974 gas

```

# Deployed Addresses 

```javascript
"L1BridgeRegistryV1_1"    0x259Ac335EB42d345A61bE48104eC0Ec20b283F14 
"L1BridgeRegistryProxy"   0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4 
"OperatorManagerV1_1"   0xB5F3b31dFB4DCe9a2FA12dE50A97250d60823750 
"OperatorManagerFactory"   0xAf86b21edDdC78ea27E23A7F2151d60d4e069450 
"CandidateAddOnV1_1"  0x73Bfd5cAEC63307784C7B6d2555F18ec24D96E2e
"CandidateAddOnFactory"  0x557E24b5CbFbDA3e5aC1bD01F38EcDe865791Bc5 
"CandidateAddOnFactoryProxy"   0xFA8ce5caF456115E72B96E5074769b8f66AA5861 
"Layer2ManagerV1_1"   0x2EB7f500125f11544392B83B87cDEb9456f3509f 
"Layer2ManagerProxy"   0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D 
"SeigManagerV1_2"   0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4 
"SeigManagerV1_3"   0xce18C6F84F10881eA47A43AF7311A29bb116F628
"DepositManagerV1_1"   0x74bC3031b9369e6b898e82784106257D4D37Eac5  
"DAOCommitteeProxy2"   0x9e7f54efF4A4D35097e0Acb6994A723F1a28368c  
"DAOCommitteeOwner"   0xcb9859Dc0fBECa68eFFf2bce289150513fdF7D92  
"DAOCommittee_V1"   0x9050Af1638f379A018737880aD946CdDA9101A25  
```

#  Owner of  Contracts 

```json
MultisigWallet :   
- owners 
    0x77b9D55e98126CD457D8F914647e634613D2A7fc, 0x9de8cAc67B6514837c31F367aC18a457d8f34c3D, 0xa4ABB4Bb512Fc1fecF5556ADDa9B8a4C96dc3790

DAOCommitteeProxy : (MultiSigWallet) **0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95**

DAOAgendaManager:(DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
DepositManagerProxy:(DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
SeigManagerProxy: (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
Layer2RegistryProxy: (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
CoinageFactory: (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
CandidateFactoryProxy: (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
 
L1BridgeRegistryProxy (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
CandidateAddOnFactoryProxy (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
Layer2ManagerProxy  (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
OperatorManagerFactory (DAOCommitteeProxy) 0xDD9f0cCc044B0781289Ee318e5971b0139602C26

seigniorageCommittee Of L1BridgeRegistryProxy :  0xDD9f0cCc044B0781289Ee318e5971b0139602C26

```

# Addresses  

```javascript

MultisigWallet  **0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95**

DAOCommitteeProxy 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
DAOAgendaManager 0xcD4421d082752f363E1687544a09d5112cD4f484
DepositManagerProxy 0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e
SeigManagerProxy 0x0b55a0f463b6defb81c6063973763951712d0e5f
Layer2RegistryProxy 0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b
CoinageFactory 0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43
CandidateFactoryProxy 0x9fc7100a16407ee24a79c834a56e6eca555a5d7c 

L1BridgeRegistryProxy  0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4
CandidateAddOnFactoryProxy 0xFA8ce5caF456115E72B96E5074769b8f66AA5861
Layer2ManagerProxy  0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D
OperatorManagerFactory 0xAf86b21edDdC78ea27E23A7F2151d60d4e069450


TON: 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5
WTON: 0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2

```