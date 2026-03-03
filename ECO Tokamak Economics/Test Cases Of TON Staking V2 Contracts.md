# Test Case 1. 

Staking V2 오딧 후 머지한 브랜치에서 테스트    [** **](https://github.com/tokamak-network/ton-staking-v2/issues/310)

- **Branch** :  **v2.5-audit-merge**  [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge)
- **checkout commit** : **c274c039ee355535f08bd8e8e6e438713ffc327f**
- (Test Case 1-1) test on sepolia (block number is 7933538)
```shell
npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts
```

**Work contents** 
```shell
zena@MacBook-Pro-2 ton-staking-v2 % npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts

  TON Staking V2.5
    # MockSystemConfigFactory
      ✓ set MockSystemConfigFactory
    # L1BridgeRegistry
      ✓ deploy
    # seigniorageCommittee
      ✓ setSeigniorageCommittee can not be executed by not an admin
      ✓ setSeigniorageCommittee can be executed by admin
    # OperatorManagerFactory
      ✓ deploy OperatorManagerV1_1
      ✓ deploy OperatorManagerFactory
    # CandidateAddOnV1_1
      ✓ deploy CandidateAddOnV1_1Imp
    # CandidateAddOnFactoryProxy
      ✓ deploy
    # Layer2Manager
      ✓ deploy
      ✓ addManager can be executed by admin
      ✓ OperatorManagerFactory.setAddresses
    # setAddresses
      ✓ setAddresses can not be executed by not an admin
      ✓ setAddresses can be executed by admin
    # setMinimumInitialDepositAmount
      ✓ setMinimumInitialDepositAmount can not be executed by not an admin
      ✓ setMinimumInitialDepositAmount can be executed by admin
      ✓ cannot set with same minimumInitialDepositAmount
    # LegacySystemConfig : Titan
      ✓ set Titan LegacySystemConfig
      ✓ registerSystemConfigByManager
    # MockSystemConfigFactory
      ✓ create mockSystemConfig
      ✓ registerSystemConfigByManager
    # LegacySystemConfig Test2
      ✓ set legacySystemConfigTest2
      ✓ registerRollupConfigByManager : Already registered l2Bridge addresses cannot be registered.
    # checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # _lastSeigBlock
lastSeigBlock 7880372
      ✓ _lastSeigBlock
    # ThanosSystemConfig : Thanos
      ✓ registerRollupConfigByManager
    # DAO.upgradeTo(DAOCommittee_V1) , SeigManagerV1_3
      ✓ deploy DAOCommitteeAddV1_1
      ✓ deploy DAOCommitteeOwner
      ✓ deploy DAOCommitteeOwner
      ✓ deploy seigManagerV1_2
      ✓ deploy SeigManagerV1_3
      ✓ deploy DepositManagerV1_1
      ✓ upgradeTo DAO
      ✓ DAO register function 2
      ✓ DAO register function 3
      ✓ DAO register function 3
      ✓ upgradeTo SeigManager
      ✓ SeigManager register function
      ✓ DepositManager register function
      ✓ setCandidateFactory to candidateAddOnFactory
      ✓ setLayer2Manager to layer2Manager
      ✓ setTargetSetLayer2Manager to layer2Manager
      ✓ setTargetSetL1BridgeRegistry to l2Register
    # registerCandidateAddOn : MockSystemConfig
      ✓ registerCandidateAddOn : MockSystemConfig
    # registerCandidateAddOn
      ✓ Fail if rollupConfig is an invalid address
      ✓ Failure in case of insufficient ton balance
      ✓ Failure when there is no prior approval of wton
      ✓ Fail if there is no content in memo
      ✓ registerCandidateAddOn : titanCandidateAddOn
      ✓ If the layer has already been created, it will fail.
      ✓ Layers that are not registered in the L1BridgeRegistry cannot be registered.
    # L1BridgeRegistry
      # setAddresses
        ✓ setAddresses : onlyOwner
        ✓ setAddresses : onlyOwner
    # SeigManagerV1_3
      ✓ SeigManagerV1_3 : setLayer2StartBlock
    # DepositManager : CandidateAddOn titanLayerAddress
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ deposit to titanLayerAddress using deposit(address,uint256)
      ✓ deposit to titanLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ The operator's staking amount must be greater than minimumAmount.
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (2) updateSeigniorage to titanLayerAddress
    # Layer2Manager ZeroAddress Test (1) deposit
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ evm_mine
    # register CandidateAddOn : thanosCandidateAddOn
      ✓ register CandidateAddOn : thanosCandidateAddOn
    # DepositManager : CandidateAddOn : thanosCandidateAddOn
      ✓ deposit to thanosLayerAddress using approveAndCall
      ✓ deposit to thanosLayerAddress using deposit(address,uint256)
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to thanosLayer
      ✓ deposit to thanosLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (2) updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (3) updateSeigniorage to thanosLayerAddress
thanosLayerAddress 0xd53419CA3c684d5A1728F072b76e5A4eE516E536
      ✓ requestWithdrawal to titanLayerAddress
      ✓ processRequest to titanLayerAddress will be fail when delay time didn't pass.
      ✓ processRequest to titanLayerAddress.
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : (3) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : (4) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # Layer2Manager ZeroAddress Test (2)
      ✓ evm_mine
      ✓ deposit to layer1 using approveAndCall
      ✓ evm_mine
      ✓ updateSeigniorage to layer1
      ✓ evm_mine
      ✓ updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # Reject titanCandidateAddOn test
      ✓ evm_mine
totalLayer2TVL BigNumber { value: "100900000011951976733301235248101059" }
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
      ✓ updateSeigniorage to layer1
totalLayer2TVL BigNumber { value: "100900000011951976733301235248101059" }
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ updateSeigniorage to layer1
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
    # Reject updating seigniorage from unknown sender
      ✓ updateSeigniorage
```
- (Test Case 1-2) test using DAO agenda on sepolia (block number is 7933538)
```shell
npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts
```

**Work contents** 
```shell
zena@MacBook-Pro-2 ton-staking-v2 % npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts

  Rehearsal of upgrading staking v2.5 on the sepola
    # Tester
      ✓ mint ton
    # Initialize of contracts
seigniorageCommittee 0x0000000000000000000000000000000000000000
[
  1,
  '0x8d5400c38f4F8145F88783efd28776cac3e3FCd8',
  status: 1,
  operatorManager: '0x8d5400c38f4F8145F88783efd28776cac3e3FCd8'
]
totalLayer2TVL reject ThanosSepolia BigNumber { value: "0" }
      ✓ Reject all layers of L1BridgeRegistry
      ✓ Initialize of seigManager
    # Contracts from deployments
deploy hre.network.config.chainId 31337
deploy hre.network.name hardhat
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
    proxyOwner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    manager: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
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
0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xA2101482b28E3D99ff6ced517bA41EFf4971a386
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
      ✓ deployments
    # Agenda
      ✓ Submit an agenda
      ✓ Pass the noticePeriod before voting
      ✓ Vote an agenda
      ✓ Pass the votingPeriod before executing
      ✓ Execute an agenda
      ✓ Check the storages
    # Titan checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # Thanos checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # registerCandidateAddOn
      ✓ Fail if systemConfig is an invalid address
      ✓ Failure in case of insufficient ton balance
      ✓ Failure when there is no prior approval of wton
      ✓ Fail if there is no content in memo
      ✓ registerCandidateAddOn : titanCandidateAddOn
      ✓ If the layer has already been created, it will fail.
      ✓ registerCandidateAddOn : thanosCandidateAddOn
    # DepositManager : Titan CandidateAddOn
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ deposit to titanLayerAddress using deposit(address,uint256)
      ✓ deposit to thanosLayerAddress using approveAndCall
      ✓ deposit to thanosLayerAddress using deposit(address,uint256)
      ✓ deposit to titanLayerAddress using deposit(address,address,uint256)
      ✓ deposit to thanosLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ The operator's staking amount must be greater than minimumAmount.
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (2) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  (3) updateSeigniorage to titanLayerAddress
      ✓ requestWithdrawal to thanosLayerAddress
      ✓ processRequest to thanosLayerAddress will be fail when delay time didn't pass.
      ✓ processRequest to thanosLayerAddress.
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ evm_mine
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ evm_mine
      ✓ processRequest to layer1.
    # withdrawAndDepositL2 : Thanos LayerCandidate
      ✓ deposit to Thanos using approveAndCall
      ✓ deposit to layer1 using approveAndCall
      ✓ evm_mine
      ✓ withdrawAndDepositL2 : Not supported in DAOCandidate layer.
      ✓ withdrawAndDepositL2 : Failure if the staking amount is insufficient
      ✓ When you run it, deposit money to L2 immediately without delay blocks.
    # reject CandidateAddOn : L1BridgeRegistry
      ✓ evm_mine
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # DepositManager : CandidateAddOn : thanosCandidateAddOn
      ✓ Layer2Contract:  updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract:  updateSeigniorage to thanosLayerAddress
    # restore CandidateAddOn : L1BridgeRegistry
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ restore CandidateAddOn (titanCandidateAddOn) : Only rejected layers can be restored.
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : (2) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : (3) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanCandidateAddOn
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ processRequest to layer1.
```
- (Test Case 1-3) test using DAO agenda on mainnet (block number is 22081265)
```shell
npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts
```

**Work contents** 
```shell
zena@MacBook-Pro-2 ton-staking-v2 % npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts

  Layer2Manager
    # Tester
      ✓ mint ton
    # Contracts from deployments
deploy hre.network.config.chainId 31337
deploy hre.network.name hardhat
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }

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
deployer 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
[Titan RollupConfig] legacySystemConfig.proxyOwner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
[Titan RollupConfig] legacySystemConfig.owner():  0x340C44089bc45F86060922d2d89eFee9e0CDF5c7
      ✓ deployments
    # Agenda
      ✓ Submit an agenda
      ✓ Pass the noticePeriod before voting
      ✓ Vote an agenda
      ✓ Pass the votingPeriod before executing
      ✓ Execute an agenda
      ✓ Check the storages
    # Titan checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # registerCandidateAddOn
      ✓ Fail if systemConfig is an invalid address
      ✓ Failure in case of insufficient ton balance
      ✓ Failure when there is no prior approval of wton
      ✓ Fail if there is no content in memo
      ✓ registerCandidateAddOn : titanCandidateAddOn
      ✓ If the layer has already been created, it will fail.
    # LegacySystemConfig : Titan SystemConfig
      ✓ proxy owner
      ✓ upgradeTo: proxy owner
      ✓ manager
      ✓ setAddresses: manager
    # DepositManager : CandidateAddOn
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ deposit to titanLayerAddress using deposit(address,uint256)
      ✓ deposit to titanLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ The operator's staking amount must be greater than minimumAmount.
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ requestWithdrawal to titanLayerAddress
      ✓ processRequest to titanLayerAddress will be fail when delay time didn't pass.
      ✓ processRequest to titanLayerAddress.
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ processRequest to layer1.
    # reject CandidateAddOn : L1BridgeRegistry
      ✓ evm_mine
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :   updateSeigniorage to titanLayerAddress
    # restore CandidateAddOn : L1BridgeRegistry
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ restore CandidateAddOn (titanCandidateAddOn) : Only rejected layers can be restored.
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ requestWithdrawal to titanLayerAddress
      ✓ evm_mine
      ✓ processRequest to titanLayerAddress will be fail when delay time didn't pass.
      ✓ evm_mine
      ✓ processRequest to titanLayerAddress.

```

# Test Case 2. 

오딧 머지 브랜치를 다오 아젠다 제출용 브랜치고 머지 후, 테스트  ([**Tokamak Network DAO agenda #14 proposal **](https://github.com/tokamak-network/ton-staking-v2/issues/310)**제출전)**

- **Branch** :  v2.5-audit-agenda  [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
- **checkout commit** : **cfb7bb9847c0f7496e99ec76cd0a702a6adaae58**
- (Test Case 2-1) test using DAO agenda on sepolia (block number is 7933538)
```shell
npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts
```

**Work contents** 
```shell
zena@MacBook-Pro-2 ton-staking-v2 % npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts

  Rehearsal of upgrading staking V2 on the sepola
    # Tester
      ✓ mint ton
    # Initialize of contracts
seigniorageCommittee 0x0000000000000000000000000000000000000000
[
  1,
  '0x8d5400c38f4F8145F88783efd28776cac3e3FCd8',
  status: 1,
  operatorManager: '0x8d5400c38f4F8145F88783efd28776cac3e3FCd8'
]
totalLayer2TVL reject ThanosSepolia BigNumber { value: "0" }
      ✓ Reject all layers of L1BridgeRegistry
      ✓ Initialize of seigManager
    # Contracts from deployments
deploy hre.network.config.chainId 31337
deploy hre.network.name hardhat
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }

=== ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    manager: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    seigniorageCommittee: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386'
  },
  Layer2Manager: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  OperatorManagerFactory: { owner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386' },
  Titan: {
    proxyOwner: '0xA2101482b28E3D99ff6ced517bA41EFf4971a386',
    manager: '0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2'
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
0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xA2101482b28E3D99ff6ced517bA41EFf4971a386
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
l1BridgeRegistryProxy.seigniorageCommittee():  0xA2101482b28E3D99ff6ced517bA41EFf4971a386
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
      ✓ deployments
    # Agenda
      ✓ Submit an agenda
      ✓ Pass the noticePeriod before voting
      ✓ Vote an agenda
      ✓ Pass the votingPeriod before executing
      ✓ Execute an agenda
      ✓ Check the storages
    # Titan checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # Thanos checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # registerCandidateAddOn
      ✓ Fail if systemConfig is an invalid address
      ✓ Failure in case of insufficient ton balance
      ✓ Failure when there is no prior approval of wton
      ✓ Fail if there is no content in memo
      ✓ registerCandidateAddOn : titanCandidateAddOn
      ✓ If the layer has already been created, it will fail.
      ✓ registerCandidateAddOn : thanosCandidateAddOn
    # DepositManager : Titan CandidateAddOn
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ deposit to titanLayerAddress using deposit(address,uint256)
      ✓ deposit to thanosLayerAddress using approveAndCall
      ✓ deposit to thanosLayerAddress using deposit(address,uint256)
      ✓ deposit to titanLayerAddress using deposit(address,address,uint256)
      ✓ deposit to thanosLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ The operator's staking amount must be greater than minimumAmount.
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer : (2) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  (3) updateSeigniorage to titanLayerAddress
      ✓ requestWithdrawal to thanosLayerAddress
      ✓ processRequest to thanosLayerAddress will be fail when delay time didn't pass.
      ✓ processRequest to thanosLayerAddress.
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ evm_mine
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ evm_mine
      ✓ processRequest to layer1.
    # withdrawAndDepositL2 : Thanos LayerCandidate
      ✓ deposit to Thanos using approveAndCall
      ✓ deposit to layer1 using approveAndCall
      ✓ evm_mine
      ✓ withdrawAndDepositL2 : Not supported in DAOCandidate layer.
      ✓ withdrawAndDepositL2 : Failure if the staking amount is insufficient
      ✓ When you run it, deposit money to L2 immediately without delay blocks.
    # reject CandidateAddOn : L1BridgeRegistry
      ✓ evm_mine
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # DepositManager : CandidateAddOn : thanosCandidateAddOn
      ✓ Layer2Contract:  updateSeigniorage to thanosLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract:  updateSeigniorage to thanosLayerAddress
    # restore CandidateAddOn : L1BridgeRegistry
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ restore CandidateAddOn (titanCandidateAddOn) : Only rejected layers can be restored.
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : (1) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : (2) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : (3) updateSeigniorage to titanLayerAddress
      ✓ evm_mine
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanCandidateAddOn
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ processRequest to layer1.
```
- (Test Case 2-2) test using DAO agenda on mainnet (block number is 22081265)
```shell
npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts
```

  - deploy-staking-v2.5-mainnet/0.seploy.ts 파일에서, 실제 상용에서 실행하지 않는 부분이 주석으로 되어 있는데, 이부분 주석을 풀고 실행해야 합니다. 
  - 환경설정 파일을 메인넷 환경파일로 복사하고 실행해야 합니다. 

**Work contents**  ( Test case 2-1 과 같은 테스트 케이스) 
```shell
zena@MacBook-Pro-2 ton-staking-v2 % npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts

  Layer2Manager
    # Tester
      ✓ mint ton
    # Contracts from deployments
deploy hre.network.config.chainId 31337
deploy hre.network.name hardhat
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }

=== ownerAddressInfo ===
{
  L1BridgeRegistry: {
    owner: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    manager: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26',
    seigniorageCommittee: '0xDD9f0cCc044B0781289Ee318e5971b0139602C26'
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
deployer 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
candidateAddOnFactoryProxy.isAdmin(deployer):  false
candidateAddOnFactoryProxy.isAdmin(DAOCommitteeProxy):  true
operatorManagerFactory.owner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
l1BridgeRegistryProxy.isAdmin(deployer):  false
l1BridgeRegistryProxy.isAdmin(DAOCommitteeProxy):  true
l1BridgeRegistryProxy.seigniorageCommittee():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
layer2ManagerProxy.isAdmin(deployer):  false
layer2ManagerProxy.isAdmin(DAOCommitteeProxy):  true
[Titan RollupConfig] legacySystemConfig.proxyOwner():  0xDD9f0cCc044B0781289Ee318e5971b0139602C26
[Titan RollupConfig] legacySystemConfig.owner():  0x340C44089bc45F86060922d2d89eFee9e0CDF5c7
      ✓ deployments
    # Agenda
      ✓ Submit an agenda
      ✓ Pass the noticePeriod before voting
      ✓ Vote an agenda
      ✓ Pass the votingPeriod before executing
      ✓ Execute an agenda

      1) Check the storages
    # Titan checkLayer2TVL
      ✓ If the rollupConfig or L1Bridge address does not exist, the result is returned as false.
      ✓ If the rollupConfig or L1Bridge address exist, the result is returned as false.
    # registerCandidateAddOn
      ✓ Fail if systemConfig is an invalid address
      ✓ Failure in case of insufficient ton balance
      ✓ Failure when there is no prior approval of wton
      ✓ Fail if there is no content in memo
      ✓ registerCandidateAddOn : titanCandidateAddOn
      ✓ If the layer has already been created, it will fail.
    # LegacySystemConfig : Titan SystemConfig
      ✓ proxy owner
      ✓ upgradeTo: proxy owner
      ✓ manager
      ✓ setAddresses: manager
    # DepositManager : CandidateAddOn
      ✓ deposit to titanLayerAddress using approveAndCall
      ✓ deposit to titanLayerAddress using deposit(address,uint256)
      ✓ deposit to titanLayerAddress using deposit(address,address,uint256)
      ✓ evm_mine
      ✓ The operator's staking amount must be greater than minimumAmount.
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :  updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ requestWithdrawal to titanLayerAddress
      ✓ processRequest to titanLayerAddress will be fail when delay time didn't pass.
      ✓ processRequest to titanLayerAddress.
    # DepositManager : DAOCandidate
      ✓ deposit to layer1 using approveAndCall
      ✓ deposit to layer2 using approveAndCall
      ✓ deposit to layer1 using deposit(address,uint256)
      ✓ deposit to tokamak using deposit(address,address,uint256)
      ✓ set layerContract
      ✓ query unallocatedSeigniorage
      ✓ updateSeigniorage to layer1
      ✓ requestWithdrawal to layer1
      ✓ processRequest to layer1 will be fail when delay time didn't pass.
      ✓ processRequest to layer1.
    # reject CandidateAddOn : L1BridgeRegistry
      ✓ evm_mine
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ reject CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ evm_mine
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage : updateSeigniorage to titanLayerAddress
      ✓ evm_mine
      ✓ Layer2Contract: updateSeigniorage :   updateSeigniorage to titanLayerAddress
    # restore CandidateAddOn : L1BridgeRegistry
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
      ✓ restore CandidateAddOn (titanCandidateAddOn) : Only rejected layers can be restored.
      ✓ restore CandidateAddOn (titanCandidateAddOn) can be executed by seigniorageCommittee
    # DepositManager : CandidateAddOn : titanCandidateAddOn
      ✓ seigManager: updateSeigniorageLayer : updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ seigManager: updateSeigniorageLayer :  updateSeigniorage to titanCandidateAddOn
      ✓ evm_mine
      ✓ requestWithdrawal to titanLayerAddress
      ✓ evm_mine
      ✓ processRequest to titanLayerAddress will be fail when delay time didn't pass.
      ✓ evm_mine
      ✓ processRequest to titanLayerAddress.
```

# Test Case 3. 

[**DAO Agenda #15 Proposal 제출전,**](https://github.com/tokamak-network/ton-staking-v2/issues/311)** **수정한 CandidateAddOnProxy 변경후, 문제가 없는지 테스트합니다. 

- **Branch** : deploy-candidateAndDAO
 [https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/test/layer2/units/13.patch.CandidateAddOnFactory.mainnet.test.ts](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/test/layer2/units/13.patch.CandidateAddOnFactory.mainnet.test.ts)
- **commit**: **0d00832da88ad62aa923775b193a574994a71651** [https://github.com/tokamak-network/ton-staking-v2/commit/0d00832da88ad62aa923775b193a574994a71651](https://github.com/tokamak-network/ton-staking-v2/commit/0d00832da88ad62aa923775b193a574994a71651)
- **Work contents**
  - Execution after mainnet fork
  - Agenda registration and pass approval
  - CandidateAddOn registration (test by registering MockSystemConfig)
  - Staking, unstaking, withdrawal, and update seigniorage of existing DAO Candidate
  - Staking, unstaking, withdrawal, and update seigniorage of CandidateAddOn
  - Reject CandidateAddOn L2 seigniorage

```shell
 npx hardhat test test/layer2/units/13.patch.CandidateAddOnFactory.mainnet.test.ts
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/543f9a4d-d802-40c1-8077-ab12a09bfeab/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-06-16_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.39.26.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLZ2R3WH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWCRt%2F1a2mcXtutLdpdiG%2BPAWuL6vqnlNCc0qCqCDOsAiAQRn76oX8rl561yQW%2Buwmo5ulFFjg6SKKXPHIvypofMSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM70kyIXs7lb0XQwIPKtwD2RH2w1YQJlvF8UIh3tYCcS0K%2FcvsNFl34QEJlBL5x5l6ePDvlcnbMdPIF6Q0kYRHSF9iFg01a3DfBCZT71TczYefpkDxr5UYfy6SsIB8cGBIipKrUZduj8wuVN69Iy7CuR3%2FJe1Hwns5Xt0nlDMIj0bXx9T7o6iAuZGY4mM7oC6%2FqPa%2Bo4Qk36rczxIX7x8tzN09%2Fggq7Ak90OA87UWgDCEvn9x5oCg2sqKVCMtEtkFFgkekcEd6yAk3izZw0K46AboyCPOSe43kK9TZvkevBPljcqdp%2Fsk0w2okVqCZGFOkl2DrbcWtlZdgeUU%2FHWdEHtRs8Ex3xb5ABLcs1kJBeYz%2BgzwUBLGDCG0ui%2Bdmvo5%2FuNYjIz5%2FagAsQU3tfVRVMEMiYGM%2FivEJuDguUDLAkuyn%2FY%2BPvgSHd6cXcYP6lR%2B1eBVqdauXyQFzdf%2Fjln0WSJUljivBeAUSeB%2BM4QFzuWpj8ut3ZuDXqUdHWY6lGolA5v5%2BBxx1GEd3z75MiycBtwBnVHhFPFrM2Tp2VvoYwiX2T1JNDBzWAWHKZJl4DHpODtpC1ilKbS6ByQ08H%2FcIhpAW0x4GhogQwnPaTR7DJQ8tu2XIy08rl2vifqXO8EsUURKXAoma2GrhwUww0ZrbzAY6pgF3jXSmqnv5v%2F5%2B66%2B3bJe%2BUMJCEeYtzDLXP7G9whVgG%2B2t1we4CxuuCuZpzdjzwUnhZ%2BxlhbufxHn0wy9RQpFy9jwvB7use%2FfI4wBdhhdmXjBm9nJGuktey3I5KGrNDsV%2FIRy4r2rg5UA6CVsdTu%2FIGw2dQ%2BCsCOgpczgTQz4WRO16jS5l%2FpAQ4E8hFvrfInOureXDrd6bCB3tf7YDA1HzZSqra5dz&X-Amz-Signature=13c84e524977914b514ea7330d1cbf84ad94e5b82bdb85d7cdbfea5c0653293c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f2b45081-aeb6-4dd6-93fb-b36b7f29ab32/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-06-16_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.39.40.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLZ2R3WH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWCRt%2F1a2mcXtutLdpdiG%2BPAWuL6vqnlNCc0qCqCDOsAiAQRn76oX8rl561yQW%2Buwmo5ulFFjg6SKKXPHIvypofMSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM70kyIXs7lb0XQwIPKtwD2RH2w1YQJlvF8UIh3tYCcS0K%2FcvsNFl34QEJlBL5x5l6ePDvlcnbMdPIF6Q0kYRHSF9iFg01a3DfBCZT71TczYefpkDxr5UYfy6SsIB8cGBIipKrUZduj8wuVN69Iy7CuR3%2FJe1Hwns5Xt0nlDMIj0bXx9T7o6iAuZGY4mM7oC6%2FqPa%2Bo4Qk36rczxIX7x8tzN09%2Fggq7Ak90OA87UWgDCEvn9x5oCg2sqKVCMtEtkFFgkekcEd6yAk3izZw0K46AboyCPOSe43kK9TZvkevBPljcqdp%2Fsk0w2okVqCZGFOkl2DrbcWtlZdgeUU%2FHWdEHtRs8Ex3xb5ABLcs1kJBeYz%2BgzwUBLGDCG0ui%2Bdmvo5%2FuNYjIz5%2FagAsQU3tfVRVMEMiYGM%2FivEJuDguUDLAkuyn%2FY%2BPvgSHd6cXcYP6lR%2B1eBVqdauXyQFzdf%2Fjln0WSJUljivBeAUSeB%2BM4QFzuWpj8ut3ZuDXqUdHWY6lGolA5v5%2BBxx1GEd3z75MiycBtwBnVHhFPFrM2Tp2VvoYwiX2T1JNDBzWAWHKZJl4DHpODtpC1ilKbS6ByQ08H%2FcIhpAW0x4GhogQwnPaTR7DJQ8tu2XIy08rl2vifqXO8EsUURKXAoma2GrhwUww0ZrbzAY6pgF3jXSmqnv5v%2F5%2B66%2B3bJe%2BUMJCEeYtzDLXP7G9whVgG%2B2t1we4CxuuCuZpzdjzwUnhZ%2BxlhbufxHn0wy9RQpFy9jwvB7use%2FfI4wBdhhdmXjBm9nJGuktey3I5KGrNDsV%2FIRy4r2rg5UA6CVsdTu%2FIGw2dQ%2BCsCOgpczgTQz4WRO16jS5l%2FpAQ4E8hFvrfInOureXDrd6bCB3tf7YDA1HzZSqra5dz&X-Amz-Signature=9a4d89d4fd8a95e41ccfd8c53967d1128424fb84f14c27f2df03643a13aca28b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1e5fd94c-54b7-4f3d-8d90-eb31d50773a4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-06-16_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.39.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLZ2R3WH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWCRt%2F1a2mcXtutLdpdiG%2BPAWuL6vqnlNCc0qCqCDOsAiAQRn76oX8rl561yQW%2Buwmo5ulFFjg6SKKXPHIvypofMSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM70kyIXs7lb0XQwIPKtwD2RH2w1YQJlvF8UIh3tYCcS0K%2FcvsNFl34QEJlBL5x5l6ePDvlcnbMdPIF6Q0kYRHSF9iFg01a3DfBCZT71TczYefpkDxr5UYfy6SsIB8cGBIipKrUZduj8wuVN69Iy7CuR3%2FJe1Hwns5Xt0nlDMIj0bXx9T7o6iAuZGY4mM7oC6%2FqPa%2Bo4Qk36rczxIX7x8tzN09%2Fggq7Ak90OA87UWgDCEvn9x5oCg2sqKVCMtEtkFFgkekcEd6yAk3izZw0K46AboyCPOSe43kK9TZvkevBPljcqdp%2Fsk0w2okVqCZGFOkl2DrbcWtlZdgeUU%2FHWdEHtRs8Ex3xb5ABLcs1kJBeYz%2BgzwUBLGDCG0ui%2Bdmvo5%2FuNYjIz5%2FagAsQU3tfVRVMEMiYGM%2FivEJuDguUDLAkuyn%2FY%2BPvgSHd6cXcYP6lR%2B1eBVqdauXyQFzdf%2Fjln0WSJUljivBeAUSeB%2BM4QFzuWpj8ut3ZuDXqUdHWY6lGolA5v5%2BBxx1GEd3z75MiycBtwBnVHhFPFrM2Tp2VvoYwiX2T1JNDBzWAWHKZJl4DHpODtpC1ilKbS6ByQ08H%2FcIhpAW0x4GhogQwnPaTR7DJQ8tu2XIy08rl2vifqXO8EsUURKXAoma2GrhwUww0ZrbzAY6pgF3jXSmqnv5v%2F5%2B66%2B3bJe%2BUMJCEeYtzDLXP7G9whVgG%2B2t1we4CxuuCuZpzdjzwUnhZ%2BxlhbufxHn0wy9RQpFy9jwvB7use%2FfI4wBdhhdmXjBm9nJGuktey3I5KGrNDsV%2FIRy4r2rg5UA6CVsdTu%2FIGw2dQ%2BCsCOgpczgTQz4WRO16jS5l%2FpAQ4E8hFvrfInOureXDrd6bCB3tf7YDA1HzZSqra5dz&X-Amz-Signature=21dcd163f47346381f69a08c61f1da3c1724701eae7034af6e3f04192c7bcead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)