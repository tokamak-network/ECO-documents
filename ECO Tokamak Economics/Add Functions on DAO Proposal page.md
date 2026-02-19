# Type A 

## L1BridgeRegistry  

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/abi/L1BridgeRegistryV1_1.json) 
- L1BridgeRegistryProxy [0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#writeProxyContract)

### **addRegistrant(address registrant)  **

- Description : Add a registrant.
An account with registrant permission in the L1BridgeRegistry contract can register RollupConfig, which holds unique information about Layer2. Registering RollupConfig means ensuring that there are no issues in Layer2.
Only the registered RollupConfig can be registered as CandidateAddOn. Only after being registered as CandidateAddOn can the sequencer(seigniorageReceiver) receive seigniorage.
- Param1 : address registrant 
  - Address of registrant to register
  - placeholder : 0x0000000000000000000000000000000000000000

### setSeigniorageCommittee**(address _seigniorageCommittee)  **

- Description : Add a seigniorageCommittee.
Simple Staking V2 designed an economy that issues TON seigniorage to CandidateAddOn's OperatorManager. The layer 2 operator(OperatorManager.manager() , Set to RollupConfig's unsafeBlockSigner() when registering) can claim the seigniorage stored in the OperatorManager contract. Just in case, we must have a function to stop issuing TON seigniorage to OperatorManager. A SeigniorageCommittee account was created in the L1BridgeRegistry contract. The SeigniorageCommittee can perform the function of suspending issuance of seigniorage or canceling suspension of issuance for a sequencer in a specific CandidateAddOn.
- Param1 : address _seigniorageCommittee 
  - Address to set to _seigniorageCommittee
  - placeholder : 0x0000000000000000000000000000000000000000

### [**registerRollupConfigByManager**](https://github.com/tokamak-network/ton-staking-v2/blob/b7e1d493b34dbefddf92e3f28ec00e003a1df884/contracts/layer2/L1BridgeRegistryV1_1.sol#L220-L225)**(address rollupConfig, uint8 _type, address _l2TON, string calldata _name)  **

- Description : Registers a specific rollupConfig by the manager. 
Only the registered RollupConfig can be registered as CandidateAddOn. Only after being registered as CandidateAddOn can the sequencer(seigniorageReceiver) receive seigniorage.
- Param1 : address rollupConfig 
  - the rollupConfig address
  - placeholder : 0x0000000000000000000000000000000000000000
- Param2 : uint8 _type
  - 1: optimism rollup legacy version, 2: Thanos in Tokamak Rollup Hub
  - placeholder : 2
- Param3 : address _l2TON
  - TON address in Layer2
  - placeholder : 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000
- Param4 : string _name
  - Name of Layer2
  - placeholder : Tokamak Layer2 

### [**registerRollupConfigByManager**](https://github.com/tokamak-network/ton-staking-v2/blob/b7e1d493b34dbefddf92e3f28ec00e003a1df884/contracts/layer2/L1BridgeRegistryV1_1.sol#L230)**(address rollupConfig, uint8 _type, address _l2TON)  **

- Description : Registers a specific rollupConfig by the manager. 
Only the registered RollupConfig can be registered as CandidateAddOn. Only after being registered as CandidateAddOn can the sequencer(seigniorageReceiver) receive seigniorage.
- Param1 : address rollupConfig 
  - the rollupConfig address
  - placeholder : 0x0000000000000000000000000000000000000000
- Param2 : uint8 _type
  - 1: optimism rollup legacy version, 2: Thanos in Tokamak Rollup Hub
  - placeholder : 2
- Param3 : address _l2TON
  - TON address in Layer2
  - placeholder : 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000

### [**rejectCandidateAddOn**](https://github.com/tokamak-network/ton-staking-v2/blob/b7e1d493b34dbefddf92e3f28ec00e003a1df884/contracts/layer2/L1BridgeRegistryV1_1.sol#L182-L188)**(address rollupConfig)**

- Description : Stop issuing seigniorage to the layer 2 sequencer of a specific rollupConfig. 
- Param1 : address rollupConfig 
  - rollupConfig contract address
  - placeholder : 0x0000000000000000000000000000000000000000

### [restoreCandidateAddOn](https://github.com/tokamak-network/ton-staking-v2/blob/b7e1d493b34dbefddf92e3f28ec00e003a1df884/contracts/layer2/L1BridgeRegistryV1_1.sol#L200-L208)( address rollupConfig, bool rejectedL2Deposit )

- Description : Cancel stopping seigniorage to the layer 2 sequencer of a specific rollupConfig.
- Param1 : address rollupConfig 
  - rollupConfig contract address
  - placeholder : 0x0000000000000000000000000000000000000000
- Param2 : bool rejectedL2Deposit 
  - if it is true, allow the withdrawDepositL2 function.
  - placeholder : true

## Layer2Manager 

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/abi/Layer2ManagerV1_1.json)
- Layer2ManagerProxy [0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D](https://etherscan.io/address/0xd6bf6b2b7553c8064ba763ad6989829060fdfc1d#writeProxyContract) 

### [setMinimumInitialDepositAmount](https://github.com/tokamak-network/ton-staking-v2/blob/2211f6ed60c9f657b3feb2c7d1c2f092504ca1bc/contracts/layer2/Layer2ManagerV1_1.sol#L160-L170)(uint256 _minimumInitialDepositAmount)

- Description : Set the minimum TON deposit amount required when creating a CandidateAddOn.
Due to calculating swton, it is recommended to set DepositManager's minimum deposit + 0.1 TON
- Param1 : uint256 _minimumInitialDepositAmount
  - the minimum initial deposit amount
  - placeholder :  1000100000000000000000

## DAOCommittee_V1

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/abi/DAOCommittee_V1.json)
- DAOCommitteeProxy [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)

### [createCandidateOwner](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommittee_V1.sol#L187-L190)(string calldata _memo, address _operatorAddress)

- Description : The DAO Owner registers a Candidate for the Operator on his behalf.
- Param1 : string calldata _memo
  - Here is a memo briefly explaining the candidate.
  - placeholder : “Candidate Memo”
- Param2 : address _operatorAddress
  - Operator address that will operate the Candidate.
  - placeholder : 0x0000000000000000000000000000000000000000

### [registerLayer2CandidateByOwner](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommittee_V1.sol#L267-L271)(address _operator, address _layer2, string memory _memo)

- Description : This is a function used when a user creates a Layer2 Contract (not the Candidate Contract we provide) and links it to the TONStaking system, and then registers the contract as a Candidate.
- Param1 : address _operator
  - This is the operator address of the Layer2 Contract.
  - placeholder : 0x0000000000000000000000000000000000000000
- Param2 : address _layer2
  - This is the Layer2Contract address to be registered as a Candidate.
  - placeholder : 0x0000000000000000000000000000000000000000
- Param3 : string memory _memo
  - Here is a memo briefly explaining the candidate.
  - placeholder : “Layer2Candidate Memo”

## CandidateAddOnFactoryProxy

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/abi/CandidateAddOnFactoryProxy.json)
- CandidateAddOnFactoryProxy   : [0xFA8ce5caF456115E72B96E5074769b8f66AA5861](https://etherscan.io/address/0xFA8ce5caF456115E72B96E5074769b8f66AA5861)

### [upgradeTo](https://github.com/tokamak-network/ton-staking-v2/blob/3457b3d4ce278d03286325f8d47cbfa9bf568a63/contracts/proxy/Proxy.sol#L33-L43)(address impl)

- Description : A function that modifies the logic of a proxy.
- Param1 : address impl
  - New logic address
  - placeholder : 0x0000000000000000000000000000000000000000

# Type B 

## DAOCommitteeOwner

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/abi/DAOCommitteeOwner.json)
- DAOCommitteeProxy [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)

### [setCooldownTime](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommitteeOwner.sol#L181-L183)(uint256 _cooltime)

- Description : The time it takes to execute changeMember in the DAO and then execute it again.
- Param1 : uint256 _cooltime
  - The value of cooldownTime.
  - placeholder : 259200

### [setCandidateAddOnFactory](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommitteeOwner.sol#L193-L195)(address _candidateAddOnFactory)

- Description : Sets the address of the CandidateAddOnFactoryProxy.
- Param1 : address _candidateAddOnFactory
  - Sets the address of the CandidateAddOnFactoryProxy.
  - placeholder : 0x0000000000000000000000000000000000000000

### [setLayer2Manager](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommitteeOwner.sol#L206-L208)(address _layer2Manager)

- Description : Sets the address of the Layer2ManagerProxy.
- Param1 : address _layer2Manager
  - Sets the address of the Layer2ManagerProxy.
  - placeholder : 0x0000000000000000000000000000000000000000

### [setBurntAmountAtDAO](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommitteeOwner.sol#L384-L386)(uint256 _burnAmount)

- Description : Sets the burntAmountAtDAO value of SeigManager.
- Param1 : uint256 _burnAmount
  - Sets the burntAmountAtDAO value of SeigManager.
  - placeholder : 0

### [daoExecuteTransaction](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/contracts/dao/DAOCommitteeOwner.sol#L396-L399)(address _to,bytes memory _data)

- Description : Executes a function that onlyOwner can execute immediately.
- Param1 : address _to
  - The address of where the function will be executed.
  - placeholder : 0x0000000000000000000000000000000000000000
- Param2 : bytes memory _data
  - A bytes value that encodes the function to be executed and the input values.
  - placeholder : 0x00

## L1BridgeRegistry  

- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/abi/L1BridgeRegistryV1_1.json) 
- L1BridgeRegistryProxy [0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#writeProxyContract)

### [setAddresses](https://github.com/tokamak-network/ton-staking-v2/blob/b7e1d493b34dbefddf92e3f28ec00e003a1df884/contracts/layer2/L1BridgeRegistryV1_1.sol#L125-L135) (address layerManager, address seigManager, address ton) 

- Description : Set layerManager, seigManager, and ton addresses.
- Param1 : address layerManager
  - the layerManager contract address 
  - placeholder :  0x0000000000000000000000000000000000000000
- Param2 : address seigManager
  - the seigManager contract address
  - placeholder : 0x0000000000000000000000000000000000000000
- Param3 : address ton
  - the ton contract address 
  - placeholder :  0x0000000000000000000000000000000000000000