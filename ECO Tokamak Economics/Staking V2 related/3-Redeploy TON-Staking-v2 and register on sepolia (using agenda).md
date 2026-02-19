- Sepolia simple staking web 

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/)

[Simple Staking - Tokamak](https://simple-staking-v2-one.vercel.app/staking)

Repo :  [https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5](https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5)

- Sepolia ERC20 
c4f0547b-d7c5-406f-8763-2978e8de89a1 
- Sepolia Simple Staking Contracts 
  - 0ef21581-cb54-4875-b2c9-19593dbc8325 
  - b4f734dd-4f19-4e75-b2ca-f815934ee317 
- Titan-Sepolia Network 
  - ec715fc8-07cc-4b69-90ce-98192930fa55 
- Thanos-Sepolia Network 
  - 95ab153a-e004-4baa-9d61-92492eb81176 
- sepolia tokamak bridge 
[https://tokamak-bridge-pool.vercel.app/](https://tokamak-bridge-pool.vercel.app/)

# Web 

[https://simple-staking-v2-one.vercel.app/staking](https://simple-staking-v2-one.vercel.app/staking)

# Initialize the storage  

sepolia 리허설때만 하는 작업임. 메인넷에서는 할 필요가 없다. 

` npx hardhat run scripts/layer2-sepolia/4.initialize_storage.js --network sepolia `

```javascript
deployer : 0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2

==== rejectCandidates =====
seigniorageCommittee 0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
totalLayer2TVL BigNumber { value: "100000000126054660158101999998000111" }
totalLayer2TVL BigNumber { value: "0" }

==== initialze =====
layer2Manager 0x0000000000000000000000000000000000000000
l1BridgeRegistry 0x0000000000000000000000000000000000000000
layer2StartBlock BigNumber { value: "0" }
l2RewardPerUint BigNumber { value: "0" }
totalLayer2TVL BigNumber { value: "0" }
```

# deploy contracts 

Candidate 이름이 Titan 인지 확인하고 실행해야 한다. 

아젠다 생성전에 생성한 컨트랙의 오너를 모두 DAO로 바꿨다. 

`npx hardhat deploy --network sepolia `

```javascript
 
Nothing to compile
No need to generate any newer typings.
deploy hre.network.config.chainId undefined
deploy hre.network.name sepolia
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }

=== ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    manager: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386'
  },
  Layer2Manager: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  OperatorManagerFactory: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  Titan: {
    MultiProposerableTransactionExecutor: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  }
}

 === Titan Candidate ===
name:  Titan
addresses:  {
  l1CrossDomainMessenger: '0xc123047238e8f4bFB7Ad849cA4364b721B5ABD8A',
  l1ERC721Bridge: '0x0000000000000000000000000000000000000000',
  l1StandardBridge: '0x1F032B938125f9bE411801fb127785430E7b3971',
  l2OutputOracle: '0x0000000000000000000000000000000000000000',
  optimismPortal: '0x0000000000000000000000000000000000000000',
  optimismMintableERC20Factory: '0x0000000000000000000000000000000000000000'
}
0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
deploying "L1BridgeRegistryV1_1" (tx: 0x56b56850027453e762fdf45e30571820a116a3533e66d8362ad1827d793a15f6)...: deployed at 0x893E828CEc5D1b83c75f1E7e0f9cAC2b22E79ac2 with 2523958 gas
deploying "L1BridgeRegistryProxy" (tx: 0x140dea0efa74688ad4347b911cdfc8d73e2e087506b748d6934c78ca7fc438ac)...: deployed at 0x3268e4D8276c58A806E83B3B080Cf29514A837cf with 1864283 gas
deploying "OperatorManagerV1_1" (tx: 0xfa8b93b89365aaa632782ed8a8e894009b002848067c990bca7cfab6cad3db99)...: deployed at 0xC41aaE1962822B2067Eda22302C473E4f424Ab11 with 1555619 gas
deploying "OperatorManagerFactory" (tx: 0x48104ccaabc651ff09edf62b11fd4549ae8a7f48bcf1525eff1ae40c74c03a5f)...: deployed at 0x91dCe71eB9D258E47B26E454DdBEd9f225278C2F with 1079274 gas
deploying "CandidateAddOnV1_1" (tx: 0x29d6cda2e48fbfeb5268af2d4b0494dafb7e1fbc854c202dc287dad704ddf394)...: deployed at 0x4CBc76898B547abEb3c7f23517F26a40687773c8 with 2099110 gas
deploying "CandidateAddOnFactory" (tx: 0x55f00c006c925819ce06d387cbfc45ab48fd23825e31f08975920a6cf06d5edc)...: deployed at 0x27D0d6fc7C687146806526e4C60E3DaCF5743814 with 2622515 gas
deploying "CandidateAddOnFactoryProxy" (tx: 0xacc4f4734bb60513b517153049475ac876875092db87c735377c25ad367d423d)...: deployed at 0x31BE6c47233A65fA60877c087634DB582082E4da with 1418724 gas
deploying "Layer2ManagerV1_1" (tx: 0x87565b4592d25ff0568f86c9aaff543dfc43796aabdc6e2a332cbfd204921629)...: deployed at 0x415AB5482f2d0e6D64D15AeD800176c521A927d0 with 2657338 gas
deploying "Layer2ManagerProxy" (tx: 0xc19c669cb387aa4dee49d635c66af323a5ced98cbf1fe6e136126ce263c69716)...: deployed at 0xab303E7CBFd19C998268e19d830770e215AbDF7F with 1491085 gas
deploying "SeigManagerV1_3" (tx: 0x066cf7a746525d55e2a2ef90493d894dc7b52674915c948bec6161239bab53c5)...: deployed at 0xB0A131FCc74F40b9Fb0379C4AEa7b97617305C31 with 4035692 gas
deploying "DepositManagerV1_1" (tx: 0x7904a0c972c1083f8266b628cac9cca165bd139df38370a959960dab873cf447)...: deployed at 0x18D0F9bC41a82A540e166C949a4A5C02036dffcA with 1655731 gas
deploying "DAOCommitteeProxy2" (tx: 0x88053630b067f56454d51ec21284f375e48041c607adda70366db3b2c932ee6c)...: deployed at 0xbFDE9Bf0eb9f4D2ae12dD17Cb770c3289dC4fd42 with 1282977 gas
deploying "DAOCommitteeOwner" (tx: 0x93070229dc43c4a0945d4f632ee956eea91b5cdb3a1d4ae9c1ce02fe6c60ac49)...: deployed at 0x84868ca4DD708cC035bcE0578054aa62c663e309 with 2471593 gas
deploying "DAOCommittee_V1" (tx: 0x86d8387f1c3a6bd1d6a57296da2f3d376e6e69fba8f3fffef8938989b842d3a0)...: deployed at 0x1E44122E3230957309B29636938e223705C0Da35 with 4453991 gas
deploying "LegacySystemConfig" (tx: 0x1d660300d6f0399d99b4ebc44cccb1ba3f660c0858cca53d6d23c41a8e65e39c)...: deployed at 0x501C74df1aDEb8024738D880B01306a92d6e722d with 558553 gas
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xA2101482b28E3D99ff6ced517bA41EFf4971a386
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
```

# Deployed Addresses 

```javascript
 "L1BridgeRegistryV1_1" 0x893E828CEc5D1b83c75f1E7e0f9cAC2b22E79ac2  
 "L1BridgeRegistryProxy"  0x3268e4D8276c58A806E83B3B080Cf29514A837cf  
 "OperatorManagerV1_1"  0xC41aaE1962822B2067Eda22302C473E4f424Ab11  
 "OperatorManagerFactory"  0x91dCe71eB9D258E47B26E454DdBEd9f225278C2F  
 "CandidateAddOnV1_1"   0x4CBc76898B547abEb3c7f23517F26a40687773c8  
 "CandidateAddOnFactory"   0x27D0d6fc7C687146806526e4C60E3DaCF5743814  
 "CandidateAddOnFactoryProxy"  0x31BE6c47233A65fA60877c087634DB582082E4da  
 "Layer2ManagerV1_1"  0x415AB5482f2d0e6D64D15AeD800176c521A927d0  
 "Layer2ManagerProxy"  0xab303E7CBFd19C998268e19d830770e215AbDF7F  
 "SeigManagerV1_3"  0xB0A131FCc74F40b9Fb0379C4AEa7b97617305C31  
 "DepositManagerV1_1"  0x18D0F9bC41a82A540e166C949a4A5C02036dffcA  
 "DAOCommitteeProxy2" 0xbFDE9Bf0eb9f4D2ae12dD17Cb770c3289dC4fd42  
 "DAOCommitteeOwner"  0x84868ca4DD708cC035bcE0578054aa62c663e309  
 "DAOCommittee_V1"  0x1E44122E3230957309B29636938e223705C0Da35 
 "LegacySystemConfig"  0x501C74df1aDEb8024738D880B01306a92d6e722d  
```

- Create agenda(total 14 functions) gasLimit : 3,545,145
- execute Agenda gasLimit : 1,306,687
## Expected Used Gas 

[https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0)

# Submit an agenda

```javascript
tx : https://sepolia.etherscan.io/tx/0xd7e84b1e00628219de08ddee400e528f36f9192cf0e9f41a3575f5fae4232301
```

[[DAO Agenda Description]]

# Addresses 

- DAO 

```javascript
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386

old implementation: 0xDC7e4c6cAe2123758f17D17572c6f6e820D2b431

DAOCommitteeAddV1_1 : ~~0x5AA500FA01b230EF2121c51e60c1bb1DFb1967eB

~~npx hardhat run scripts/3.deploy_DAOCommitteeAddV1_1.js --network sepolia
DAOCommitteeAddV1_1: 0x7a22429CcDbDdB13ff52d1598290186a5562b49B~~
~~
upgrade To : 0x7a22429CcDbDdB13ff52d1598290186a5562b49B

createCanddiateAddOn memo, manager address
```

- 2024.10.01 현재 상태 

```javascript
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386

impl : 0x399A7Aa3BF8da93319494CdFC495Ab20541eC1D4. DAOCommitteeProxy2

DAOCommitteeProxy2
implementation : 0x399A7Aa3BF8da93319494CdFC495Ab20541eC1D4

implementation2(0) : 0xaDf24e3885D4c8DB092514dF364b09f314F1e794 DAOCommittee_V1
implementation2(1) : 0x63f116823B6Ed37271B0204A51e8ea4Eaa09c9a6 DAOCommitteeOwner
```

for sepolia 

```javascript
 
"Layer2RegistryProxy" : 0xA0a9576b437E52114aDA8b0BC4149F2F5c604581

SeigManagerProxy : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
- SeigManager : 0xe05d62c21f4bba610F411A6F9BddF63cffb43B63
- SeigManagerV1_1 : 
- SeigManagerV1_2 : 0x32Fa7147C4d82c821518B54196de680CA03BfA30 


--SeigManagerV1_3reset: 0xa996664C21f77C6C6e477150d3AfB5F41a508457

impl(0) :  0x32Fa7147C4d82c821518B54196de680CA03BfA30
impl(1):  ~~0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3 ~~
           **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**
impl: (2) : 0
SeigManagerV1_3Logic : ~~0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3
~~              **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**

```

- DepositManager

```javascript
DepositManagerProxy : 0x90ffcc7f168dcedbef1cb6c6eb00ca73f922956f
impl(0) :  0x2d361b25395907a897f62e87A57b362264F36d7a 
impl(1): 0x82039558f14C900fC42c155281f7A4E765962b18 (not verified) 
impl(2):  DepositManager_setWithdrawalDelay : 0x7E459BC07736f735E3E758fbB740c385FB4d466B
impl(3): ~~0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211~~  **0x14b288C49C3aCc125CF88AADe631B52Fa4C2e679 **DepositManagerV1_1
```

           

# Web 

[https://simple-staking-v2-one.vercel.app/staking](https://simple-staking-v2-one.vercel.app/staking)

### Simple Staking Web 

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/) 에 자동으로 등록된 것 확인하기 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c7331f5-2617-43bc-99fe-6aaab5686acd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-08-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.35.29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JW3WH6T%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDglf7gJk6RsycgF%2F7iPUMMCMdG3EsEhpsbQCoCIeUyFAIhAPb1N0PzArWfxkaZtB3f1WlWdMDpjaMA8dUYOZ4LrMq8Kv8DCHQQABoMNjM3NDIzMTgzODA1IgzO0hgvZNOafDA5Eowq3ANpfnafISD2aajdUlQPc%2BimBpAJ1vKCsXJoAzicKosLX0ubQWebvOXccOnb3Is7bcPtMPNwLE8pBC4TtLUf0nKQZfKDl39SovAZvh35TTqZ2MH06xs6SYlqOF6L3A1iqv0D6Qdmm0vnr%2FVYjpAuNlqL2%2BIbqKU3kM4gxNrz1T6eQ9DjDMgDCBlB9zUX3ROPNCvKZJe8nCKPXard2OKx%2FlMl06aAwX%2BWXUy6ILCi0qCxYogse%2F%2FKXvCxyy5LhmMEd2LANu5zOaDHZmnmIAtl2QwkTFohTTHJR09QK4QvUIDN66BwEIkl%2Bn14qQXpXmpRWpjFSNB%2FUNoHpHfIvn0e5qf70E7UzUBICNkFyJgDaR%2Bl%2FPK9wgs6xOvVhcHolqFVIFrPaRoHjpqAfai1DaKsNF%2BFe9Zj1Pcz6WvuY1fSYkCiZYlLSTVS7bHc0JKjMv%2F6hF%2BpeE5hkSGuzMAWGE4iOjHvVA%2BMWA2slMagpCsJCnRHSvGWjGSq8Iv12i2XeWjjRNvWO%2Bfof8gDMVaJ%2F5PtPI5ZGU3jj4lt2xIbX85B0%2FwTX5efz28XexJL2T5scFmDPYL8WJScg3RaQQaDwkJsCnWaktV4%2B9Em4yP71bUVENH41agYWokZZPBUxq6nuDDC7tnMBjqkAcneYkkGl1L6vB7BVnxEordLZtzLA1HeJToOC5vkv4HdB8Mc9kgIEwBzqITnLBbprlm%2FkapuOZ%2BowTvXRZ6fFsoWshR0qs1b3FSkR2Oq8Up5wY%2FWBoiCymi0bCUOKgbMlTEC73K5nVIbHVhcGcxji4gvl6vsS4PJ4%2BFmTgx%2ByEOAAFH3bmY3azh6zgHxEaUezIn%2BTldOOki15EttnEqagwMnic5Q&X-Amz-Signature=7aab28b7edd9fbf66f19f32eb9ce958f450309a84fac0e654c5aa2296ac2ffdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Addresses on sepolia 

```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F

TON : 0xa30fe40285b8f5c0457dbc3b7c8a280373c40044
WTON : 0x79e0d92670106c85e9067b56b8f674340dca0bbd
```

```javascript

```

#  