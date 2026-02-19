- Sepolia simple staking web   
  - old version: [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/)
  - upgraded version (v2.5): [Simple Staking - Tokamak](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking)

[Simple Staking - Tokamak](https://simple-staking-v2-one.vercel.app/staking)

Repo :  [https://github.com/tokamak-network/ton-staking-v2/tree/deploy-4th-sepolia](https://github.com/tokamak-network/ton-staking-v2/tree/deploy-4th-sepolia)

- Sepolia ERC20 
c4f0547b-d7c5-406f-8763-2978e8de89a1 
- Sepolia Simple Staking Contracts 
  - 0ef21581-cb54-4875-b2c9-19593dbc8325 
  - b4f734dd-4f19-4e75-b2ca-f815934ee317 
- Thanos-Sepolia Network 
  - 3e04fb22-aad4-4e89-91ae-4c4df0ced626 
- sepolia tokamak bridge 
[https://tokamak-bridge-pool.vercel.app/](https://tokamak-bridge-pool.vercel.app/)

# Web 

[https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking)

# Initialize the storage  using DAO Agenda 

sepolia 리허설때만 하는 작업임. 메인넷에서는 할 필요가 없다. 

- 아젠다 등록하기 

`npx hardhat run scripts/layer2-sepolia/5.agenda_initialize_storage.js --network sepolia`

- dao 멤버들이 투표하기 : 컨트랙에서 직접 실행 
- 아젠다 실행하기 : 컨트랙에서 직접 실행 
- 초기화 상태 확인하기 
  - `5.agenda_initialize_storage.js` 파일에서 
await proposeAgenda_rejectCandidateAddOn() 라인을 주석으로 막고 실행 

`npx hardhat run scripts/layer2-sepolia/5.agenda_initialize_storage.js --network sepolia`

```javascript

const main = async () => {
    // await proposeAgenda_rejectCandidateAddOn()
    await view()
}

==== view =====
deployer  0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
layer2Manager 0x0000000000000000000000000000000000000000
l1BridgeRegistry 0x0000000000000000000000000000000000000000
layer2StartBlock BigNumber { value: "0" }
l2RewardPerUint BigNumber { value: "0" }
totalLayer2TVL BigNumber { value: "0" }
```
  - 웹페이지에서 L2 타이탄 초기화 되었는지 확인하기 
[https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking)

L2가 안없어지는 부분은 기능보강을 하기로 한다.  해당 데이타를 서브그래프에서 가져왔다면,

L1BridgeRegistryProxy 컨트랙에서 emit RejectedCandidateAddOn(rollupConfig) 이벤트가 발생되면, 그 데이타를 기반으로 기존 L2에서 빼야 하는 로직이 추가되었어야 할것 같아요.

[https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1738920126855819?thread_ts=1738917650.677639&cid=C07JU6K4KDY](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1738920126855819?thread_ts=1738917650.677639&cid=C07JU6K4KDY)

# deploy contracts 

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
    manager: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    registrant: ''
  },
  Layer2Manager: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  OperatorManagerFactory: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  Titan: {
    proxyOwner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    manager: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  }
}
0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
deploying "L1BridgeRegistryV1_1" (tx: 0x978496afeecd0a00c8066fca88c5261260bbc0dc8e889d637faa48abc22400cc)...: deployed at 0xbBb386Ef8Fa6908258b3f0277C58bf79df568cAb with 2523958 gas
deploying "L1BridgeRegistryProxy" (tx: 0x68cac5068e83698470fdd8dd3d7cf05eeb402379263bb7952ef425da83e2f261)...: deployed at 0x35822B4be688B06E58479Ed289E928cB25Cb3c68 with 1864283 gas
deploying "OperatorManagerV1_1" (tx: 0x2e5ed78fdcf162877247cfb4f9384f7dfbdd4330d97d07ecfbcecd33f652c4cb)...: deployed at 0xeE04A9Afb05C5366aA8015669A73c82eb4830D33 with 1557395 gas
deploying "OperatorManagerFactory" (tx: 0x07cc03eee860cf852f22bafd8f120b86891133aa945922856bc441078c62c794)...: deployed at 0xB00E2f069f9167079398C46BeC31985a3dF2fabd with 1079274 gas
deploying "CandidateAddOnV1_1" (tx: 0x3959a1731277e79cac676652a240c23eed3b7a1a31c405bdf2bb8dd66848f766)...: deployed at 0x82736FaA37035FCb88773451f6e3961a391AFCe3 with 2099110 gas
deploying "CandidateAddOnFactory" (tx: 0x3667ff94408b962ff7efd9114c669eaeeadf404b53149bd56811f77c4d6f01b4)...: deployed at 0x0325371ED5f95cDeB615ca5A0911dF3FaC24C7A2 with 2622515 gas
deploying "CandidateAddOnFactoryProxy" (tx: 0xe65b77e6793a713d80fd79c529495b8d4e6698fde05e5d6db7bfa2e377b6fe80)...: deployed at 0x4e13CfdCf03A5bB11d55f2537108860d44F3C098 with 1418724 gas
deploying "Layer2ManagerV1_1" (tx: 0xb13689773b00aa2e5a75230bd774028d566a2f70867b8903d73ab4ad7d4721a6)...: deployed at 0x027Dd0FC59c82D09392F99B56F615A6D86c735a7 with 2657338 gas
deploying "Layer2ManagerProxy" (tx: 0x99edd4d5f5959b749e838409229a8bc7c69c9c39e158a109795383af8ac72801)...: deployed at 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5 with 1491085 gas
deploying "SeigManagerV1_3" (tx: 0x4dd0b6939aab012f30a4358c17aae22f345570f462d1dadf5d04c699ca00f92a)...: deployed at 0x1ae2b8a23384e4D76290eF9AE30Edf574D82d991 with 4035692 gas
deploying "DepositManagerV1_1" (tx: 0x308f49c20a234fd15453f81d0670aa82e110a533f3f5cca8b9798a70476384ab)...: deployed at 0xa9d1AaE84f4fF55d72B5f2D71fFAFe99a3F9BdE2 with 1655743 gas
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
   
   
 "L1BridgeRegistryV1_1" at 0xbBb386Ef8Fa6908258b3f0277C58bf79df568cAb
 "L1BridgeRegistryProxy" at 0x35822B4be688B06E58479Ed289E928cB25Cb3c68
 "OperatorManagerV1_1" at 0xeE04A9Afb05C5366aA8015669A73c82eb4830D33
 "OperatorManagerFactory" at 0xB00E2f069f9167079398C46BeC31985a3dF2fabd
 "CandidateAddOnV1_1" at 0x82736FaA37035FCb88773451f6e3961a391AFCe3
 "CandidateAddOnFactory" at 0x0325371ED5f95cDeB615ca5A0911dF3FaC24C7A2
 **"CandidateAddOnFactoryProxy" at 0x4e13CfdCf03A5bB11d55f2537108860d44F3C098**
 "Layer2ManagerV1_1" at 0x027Dd0FC59c82D09392F99B56F615A6D86c735a7
 "Layer2ManagerProxy" at 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5
 "SeigManagerV1_3" at 0x1ae2b8a23384e4D76290eF9AE30Edf574D82d991
 "DepositManagerV1_1" at 0xa9d1AaE84f4fF55d72B5f2D71fFAFe99a3F9BdE2
```

# Propose an agenda for upgrading staking v2.5 

`npx hardhat run scripts/layer2-sepolia/6.agenda_stake_v25.js --network sepolia`

-  

```json

const main = async () => {

    // await upgradeContracts_v25()
    // await executeAgenda(agendaId)

    await views()
}

```

- 아젠다 실행전 views

```json

==== views =====
depositManagerV1_1.l1BridgeRegistry 0x3268e4D8276c58A806E83B3B080Cf29514A837cf
depositManagerV1_1.layer2Manager 0xab303E7CBFd19C998268e19d830770e215AbDF7F
seigManager.layer2Manager 0x0000000000000000000000000000000000000000
seigManager.l1BridgeRegistry 0x0000000000000000000000000000000000000000
seigManager.layer2StartBlock BigNumber { value: "0" }
seigManager.l2RewardPerUint BigNumber { value: "0" }
seigManager.totalLayer2TVL BigNumber { value: "0" }
```

- 아젠다 제출  
`npx hardhat run scripts/layer2-sepolia/6.agenda_stake_v25.js --network sepolia`

```json
const main = async () => {

    await upgradeContracts_v25()
    // await executeAgenda(agendaId)

    // await views()
}
```

  - tx : [https://sepolia.etherscan.io/tx/0x9595ee540762ca8374229d29250f1d776d62471cab388ef53fea07942c640b05](https://sepolia.etherscan.io/tx/0x9595ee540762ca8374229d29250f1d776d62471cab388ef53fea07942c640b05)
- 투표
  - tx : [https://sepolia.etherscan.io/tx/0x3ad5d5db4040b75e1bd1d4ca0ab3baf06b33be58d049796f6daf68876e9bdffa](https://sepolia.etherscan.io/tx/0x3ad5d5db4040b75e1bd1d4ca0ab3baf06b33be58d049796f6daf68876e9bdffa)
  - tx: [https://sepolia.etherscan.io/tx/0x26eec274a1ec461e7e66d640e7e4ca243be10a32f1c4987d68d082db3255767f](https://sepolia.etherscan.io/tx/0x26eec274a1ec461e7e66d640e7e4ca243be10a32f1c4987d68d082db3255767f)
- 아젠다 실행 
  - tx : [https://sepolia.etherscan.io/tx/0x11628970deacd1f203c23e1fba54f41f277e2e10502783ab87cd7ff1160cc6e2](https://sepolia.etherscan.io/tx/0x11628970deacd1f203c23e1fba54f41f277e2e10502783ab87cd7ff1160cc6e2)
- 아젠다 실행후 view : 수정사항 확인됨 
```javascript
==== views =====
daoCommitteeAddV1_1.layer2Manager 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5
daoCommitteeAddV1_1.candidateAddOnFactory 0x0325371ED5f95cDeB615ca5A0911dF3FaC24C7A2
depositManagerV1_1.l1BridgeRegistry 0x35822B4be688B06E58479Ed289E928cB25Cb3c68
depositManagerV1_1.layer2Manager 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5
seigManager.layer2Manager 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5
seigManager.l1BridgeRegistry 0x35822B4be688B06E58479Ed289E928cB25Cb3c68
seigManager.layer2StartBlock BigNumber { value: "0" }
seigManager.l2RewardPerUint BigNumber { value: "0" }
seigManager.totalLayer2TVL BigNumber { value: "0" }
```

 

# Propose an agenda for grating registrant for TRH 

registrant : [0xfca535c88660e261f3bd82c81640366dbbb3517a](https://etherscan.io/address/0xfca535c88660e261f3bd82c81640366dbbb3517a)

[https://tokamak-network.slack.com/archives/C06UKCF86TE/p1738926211105799?thread_ts=1738903618.878159&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1738926211105799?thread_ts=1738903618.878159&cid=C06UKCF86TE)

`npx hardhat run scripts/layer2-sepolia/7.agenda_registrant.js --network sepolia`

-  

```json

const main = async () => {

    // await upgradeContracts_v25()
    // await executeAgenda(agendaId)

    await views()
}

```

- 아젠다 실행전 views

```json

==== views =====
l1BridgeRegistryV1_1.isRegistrant  0xfca535c88660e261f3bd82c81640366dbbb3517a   false
```

- 아젠다 제출  
`npx hardhat run scripts/layer2-sepolia/6.agenda_stake_v25.js --network sepolia`

```json
const main = async () => {

    await upgradeContracts_v25()
    // await executeAgenda(agendaId)

    // await views()
}
```

agendaId BigNumber { value: "33" }
```json

==== registranst =====
deployer  0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
L1BridgeRegistryProxy.addRegistrant
make an agenda
Propose an agenda receipt  {
  to: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
  from: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2',
  contractAddress: null,
  transactionIndex: 22,
  gasUsed: BigNumber { value: "386360" },
  logsBloom: '0x000000000000000000000000000000010000000000000000000000000000000200000000000000000000000000000000800000000000000000002000002400000000000000000000004000080000000000000000000400000010000000000000001000000000000000000000000000000000000000000000000000100c0000000000000000000000000080000000000000000200000000000000000001000020020000000000000000000000000000000000080800000000000000000000000000000002000000000000000000000000000000400000000000800000000040000010000000000000000000000000000000000800000000000000000000000000',
  blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
  transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
  logs: [
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 34,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a'
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 35,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a'
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000000',
      logIndex: 36,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a'
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 37,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a'
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000012c00000000000000000000000000000000000000000000000000000000000002580000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000035822b4be688b06e58479ed289e928cb25cb3c68',
      logIndex: 38,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a'
    }
  ],
  blockNumber: 7658785,
  confirmations: 1,
  cumulativeGasUsed: BigNumber { value: "2291372" },
  effectiveGasPrice: BigNumber { value: "61182145036" },
  status: 1,
  type: 2,
  byzantium: true,
  events: [
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 34,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'Approval',
      eventSignature: 'Approval(address,address,uint256)',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 35,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'Transfer',
      eventSignature: 'Transfer(address,address,uint256)',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000000',
      logIndex: 36,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'Approval',
      eventSignature: 'Approval(address,address,uint256)',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000056bc75e2d63100000',
      logIndex: 37,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'Transfer',
      eventSignature: 'Transfer(address,address,uint256)',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 22,
      blockNumber: 7658785,
      transactionHash: '0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc',
      address: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000012c00000000000000000000000000000000000000000000000000000000000002580000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000035822b4be688b06e58479ed289e928cb25cb3c68',
      logIndex: 38,
      blockHash: '0x07a4cc6feb17b78f63b35a79653f1c18c9e4ac74ee43d0b5dea09e94eab90f3a',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    }
  ]
}
agendaId BigNumber { value: "33" }
executionInfo : [
  [ '0x35822B4be688B06E58479Ed289E928cB25Cb3c68' ],
  [
    '0xbbfcfc1e000000000000000000000000fca535c88660e261f3bd82c81640366dbbb3517a'
  ],
  true,
  BigNumber { value: "0" },
  target: [ '0x35822B4be688B06E58479Ed289E928cB25Cb3c68' ],
  functionBytecode: [
    '0xbbfcfc1e000000000000000000000000fca535c88660e261f3bd82c81640366dbbb3517a'
  ],
  atomicExecute: true,
  executeStartFrom: BigNumber { value: "0" }
]
```

  - tx :  [https://sepolia.etherscan.io/tx/0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc#eventlog](https://sepolia.etherscan.io/tx/0x1699115fbef709cec4d05bc00788c8f0a31a2c75c6118503b8397041b551d4dc#eventlog)
- 투표
  - tx :  [https://sepolia.etherscan.io/tx/0x23dfc60a55332648c3dd4e97594b6bdaa695521cf2c87d6b13eeaba099b1b954](https://sepolia.etherscan.io/tx/0x23dfc60a55332648c3dd4e97594b6bdaa695521cf2c87d6b13eeaba099b1b954)
  - tx:  [https://sepolia.etherscan.io/tx/0x02d07861d08e08fae51f4a7172db5809fcef764d39d12077d0f4d875a31b15e4](https://sepolia.etherscan.io/tx/0x02d07861d08e08fae51f4a7172db5809fcef764d39d12077d0f4d875a31b15e4)
- 아젠다 실행 

```json

==== executeAgenda =====  BigNumber { value: "33" }
block.timestamp 1738936776
Agenda Before executeing  [
  BigNumber { value: "1738935780" },
  BigNumber { value: "1738936080" },
  BigNumber { value: "600" },
  BigNumber { value: "1738936116" },
  BigNumber { value: "1738936716" },
  BigNumber { value: "1739541516" },
  BigNumber { value: "0" },
  BigNumber { value: "2" },
  BigNumber { value: "0" },
  BigNumber { value: "0" },
  3,
  1,
  [
    '0xD4335A175c36c0922F6A368b83f9F6671bf07606',
    '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea',
    '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  ],
  false,
  createdTimestamp: BigNumber { value: "1738935780" },
  noticeEndTimestamp: BigNumber { value: "1738936080" },
  votingPeriodInSeconds: BigNumber { value: "600" },
  votingStartedTimestamp: BigNumber { value: "1738936116" },
  votingEndTimestamp: BigNumber { value: "1738936716" },
  executableLimitTimestamp: BigNumber { value: "1739541516" },
  executedTimestamp: BigNumber { value: "0" },
  countingYes: BigNumber { value: "2" },
  countingNo: BigNumber { value: "0" },
  countingAbstain: BigNumber { value: "0" },
  status: 3,
  result: 1,
  voters: [
    '0xD4335A175c36c0922F6A368b83f9F6671bf07606',
    '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea',
    '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  ],
  executed: false
]
receipt {
  to: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
  from: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2',
  contractAddress: null,
  transactionIndex: 149,
  gasUsed: BigNumber { value: "158761" },
  logsBloom: '0x00000004000000000000020000000081000000000000008000000000000000020000000000000000000000000000000000400000000000000400000000000000000400000000000004000000000000000000000002080000000000000000000000100000000000000000000000000000000000000010000000008000040000000000000000000000000080000000000000000000002000000000000001000000000000000000000000000000000000000080080800000000009000000000000000000000000000000000000000000000000000400000000100000000000000100000000000200000000000000000000000000000000000000000800000000002',
  blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321',
  transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
  logs: [
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0x1444f7a8bC26a3c9001a13271D56d6fF36B44f08',
      topics: [Array],
      data: '0x00000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000004',
      logIndex: 203,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321'
    },
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0x35822B4be688B06E58479Ed289E928cB25Cb3c68',
      topics: [Array],
      data: '0x',
      logIndex: 204,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321'
    },
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000035822b4be688b06e58479ed289e928cb25cb3c68',
      logIndex: 205,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321'
    }
  ],
  blockNumber: 7658868,
  confirmations: 1,
  cumulativeGasUsed: BigNumber { value: "13542059" },
  effectiveGasPrice: BigNumber { value: "45587045621" },
  status: 1,
  type: 2,
  byzantium: true,
  events: [
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0x1444f7a8bC26a3c9001a13271D56d6fF36B44f08',
      topics: [Array],
      data: '0x00000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000004',
      logIndex: 203,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0x35822B4be688B06E58479Ed289E928cB25Cb3c68',
      topics: [Array],
      data: '0x',
      logIndex: 204,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'RoleGranted',
      eventSignature: 'RoleGranted(bytes32,address,address)',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    },
    {
      transactionIndex: 149,
      blockNumber: 7658868,
      transactionHash: '0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac',
      address: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
      topics: [Array],
      data: '0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000035822b4be688b06e58479ed289e928cb25cb3c68',
      logIndex: 205,
      blockHash: '0x61dcc388ed7db554513ce15fcbb5f41f69e28f6d31fcdec64d426af4b7ed4321',
      args: [Array],
      decode: [Function (anonymous)],
      event: 'AgendaExecuted',
      eventSignature: 'AgendaExecuted(uint256,address[])',
      removeListener: [Function (anonymous)],
      getBlock: [Function (anonymous)],
      getTransaction: [Function (anonymous)],
      getTransactionReceipt: [Function (anonymous)]
    }
  ]
}
Aagenda Aefore executeing  [
  BigNumber { value: "1738935780" },
  BigNumber { value: "1738936080" },
  BigNumber { value: "600" },
  BigNumber { value: "1738936116" },
  BigNumber { value: "1738936716" },
  BigNumber { value: "1739541516" },
  BigNumber { value: "1738936812" },
  BigNumber { value: "2" },
  BigNumber { value: "0" },
  BigNumber { value: "0" },
  4,
  1,
  [
    '0xD4335A175c36c0922F6A368b83f9F6671bf07606',
    '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea',
    '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  ],
  true,
  createdTimestamp: BigNumber { value: "1738935780" },
  noticeEndTimestamp: BigNumber { value: "1738936080" },
  votingPeriodInSeconds: BigNumber { value: "600" },
  votingStartedTimestamp: BigNumber { value: "1738936116" },
  votingEndTimestamp: BigNumber { value: "1738936716" },
  executableLimitTimestamp: BigNumber { value: "1739541516" },
  executedTimestamp: BigNumber { value: "1738936812" },
  countingYes: BigNumber { value: "2" },
  countingNo: BigNumber { value: "0" },
  countingAbstain: BigNumber { value: "0" },
  status: 4,
  result: 1,
  voters: [
    '0xD4335A175c36c0922F6A368b83f9F6671bf07606',
    '0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea',
    '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
  ],
  executed: true
]
```

  - tx :  [https://sepolia.etherscan.io/tx/0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac](https://sepolia.etherscan.io/tx/0xbd12daf3a1b0a75b8e177f5cdcff0bb02f60e2eb1004eb6e43a31a35f8f0edac)
- 아젠다 실행후 view : 수정사항 확인됨  [https://sepolia.etherscan.io/address/0x35822b4be688b06e58479ed289e928cb25cb3c68#readContract#F13](https://sepolia.etherscan.io/address/0x35822b4be688b06e58479ed289e928cb25cb3c68#readContract#F13)
```javascript

==== views =====
l1BridgeRegistryV1_1.isRegistrant  0xfca535c88660e261f3bd82c81640366dbbb3517a   true
```

# Register Thanos-sepolia on sepolia

## Propose an agenda for  register RollupConfig (Thanos-sepolia) 

By DAO 

## Register registerCandidateAddOn (Thanos-sepolia) 

- [approve](https://sepolia.etherscan.io/address/0xa30fe40285b8f5c0457dbc3b7c8a280373c40044#writeContract#F2) 1000.1 TON (1000100000000000000000) to 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5
  - tx : [https://sepolia.etherscan.io/tx/0xb8d7b1e12ecd507b7a57c4388f2f3355419939c425b8843c09204cfd2ab94d3e](https://sepolia.etherscan.io/tx/0xb8d7b1e12ecd507b7a57c4388f2f3355419939c425b8843c09204cfd2ab94d3e)

"Layer2ManagerProxy" at 0x53faC2e379cBfFd4C32D2b6FBBA83De102DDA2E5

[registerCandidateAddOn](https://sepolia.etherscan.io/address/0x53fac2e379cbffd4c32d2b6fbba83de102dda2e5#writeProxyContract#F5) 

```solidity
 function registerCandidateAddOn(
        address rollupConfig,
        uint256 amount,
        bool flagTon,
        string calldata memo
    )
    
- rollupConfig : 0x6eF61974A3CDa7BbD0a4DD0A613f56d211c8AfDC
- amount : 1000100000000000000000
- flagTon : true   
- memo: 'Thanos Sepolia'


```

tx: [https://sepolia.etherscan.io/tx/0x131a16b4037274d52897ed8a33b366e14f1344d69ae70086bf27773765710f70](https://sepolia.etherscan.io/tx/0x131a16b4037274d52897ed8a33b366e14f1344d69ae70086bf27773765710f70)

  - OperatorManagerProxy 
    - [manager](https://sepolia.etherscan.io/address/0x8d5400c38f4f8145f88783efd28776cac3e3fcd8#readProxyContract) :  [0x0Fd5632f3b52458C31A2C3eE1F4b447001872Be9](https://sepolia.etherscan.io/address/0x0Fd5632f3b52458C31A2C3eE1F4b447001872Be9) 
      - [RollupConfig.unsafeBlockSigner](https://sepolia.etherscan.io/address/0x6ef61974a3cda7bbd0a4dd0a613f56d211c8afdc#readProxyContract#F35) 가 자동으로 매니저로 지정됩니다. 현재 thanos sepolia 에서 가져온 값이므로, 아마 theo님께 위 매니저를 제이슨님으로 [수정해달라고 ](https://sepolia.etherscan.io/address/0x8d5400c38f4f8145f88783efd28776cac3e3fcd8#writeProxyContract#F12)하셔서 매니저권한 받으셔야 할것 같습니다. 
  - [CandidateAddOnProxy](https://sepolia.etherscan.io/address/0xdbd15bd93feb9689071f9c4e4edee8dc1c06de42#code)  : 0xDBD15bD93FEb9689071f9c4e4eDee8dc1C06dE42 
    - 이 컨트랙이 생성된 Candidate 입니다. 
  - [ConinageProxy](https://sepolia.etherscan.io/address/0xdb3ca0dd8ecca3220f4b1e360aede6ac5c4a8688#code)  : 0xdb3ca0dd8ecca3220f4b1e360aede6ac5c4a8688
    - 생성된 코인에이지(시뇨리지 관리) 컨트랙입니다.

# Web 

 [Simple Staking - Tokamak](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking)

### Simple Staking Web 

 [https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/staking) 에 자동으로 등록된 것 확인하기 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c7331f5-2617-43bc-99fe-6aaab5686acd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-08-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.35.29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSZMFR3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFLb8wMQhjD1XUnFSYhGu4LI4LkhbtzsSH8HLwlXtb8zAiBsMtspi1RMIfty5tBwdEpat7k15%2BOatrR61VQHAMND2ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRiVF4LEr93kJ%2Bl%2BPKtwD5Gg%2FEiWeNuH0IL2pMlcRLSsJchRV3TswF6nvKiXwebjbctcGn1hSBGoCx9iUUTjtDLiAfe04tD2WmMiUliQj60Q80FZn2Kk92Dqy6yHo2IDamyGmhv4PVrQbMEuk2jH8m73ijaTA272xwJrib2m48nr1Iz8c4mTOeqRbGA%2BYsVViVg2%2F6jk2ydo0MUVEJbMkXcHde5aBGGBXNUQIMlr7BWNAxCuwubQ3tV9zLRtffeeSC01s8f3dIXkpj8aVNy1ITZQn%2B2AQNNOD%2B5cL4RCrxya6UYFt3Mw3u%2FCuX%2FYQFkkOKMre%2BJvgUB%2B3HkshtCmp4aj%2F9yiydVp76XbjHAPd46jFWhUkgKf9G59SfD9Er67OQboqOOEie6wSgAGJZg42wYdK0RFEj%2BqBeCP4snzdHx2yIp9zcudvjE08F0Ud36C5YLpTwVL262Cv77Clb5YcMAO11sQGe%2BI%2FWGlGBGWVvDch8vF3VOY%2B1XKO5DfqnxrUKyQT7TLO6cMyMzPV%2BvXhtmQYZTy7fxNjXLGSMA%2BsgAhY3K0cjOnDjdiJMPL91wm5Xhiyy7dc%2FwCzmOIvhwrjirA31bMCEhP8mwzYmQvP2VuM22q%2Fw%2F2B8DCHbZR077SzY7jBerZW317UbJcw3e7ZzAY6pgFDLbih2M008BBsPFcj3o5Hg98Rgs6ZmibVO1jmCsSmOEAR0POxww2hzb2XwduZUldSA5U53AICheEWI8uzuaQ6ZF5AuVt6RN%2F92nDq7WfnBxnzKfCoB0%2F9JushQBxGDdEC1UBi8YRJ%2F8Q2jUUb3tci%2BlR9jG91jj1Slx9m%2BYEPg5fBDK0EsqMm%2B7tt4s3FvBeYhBas8eJ1BBbautBIGcWpFPDsXYwz&X-Amz-Signature=35e97b8bd7720424b29e38515c864c99b46e9c1dc3165ce89f2992f48dcd1b69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Addresses on sepolia 

```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386


TON : 0xa30fe40285b8f5c0457dbc3b7c8a280373c40044
WTON : 0x79e0d92670106c85e9067b56b8f674340dca0bbd
```

#  