[[Tokamak Tally’s DAO (on sepolia) ]] 

```javascript
- TokamakVoteERC20: [0xE9394DAE067eF993Bb79d98917799CfA48BC83F0] 
- TokamakTimelockController: [0x079cC994fA06C916bA74a5714B6f7672Bd6F7567] 
- TokamakGovernor: [0x163de77dFe2eF689253d66D8B3fEB32eAdcb9DD3] 
```

- [https://sepolia.staking.tokamak.network/home](https://sepolia.staking.tokamak.network/home)
- Sepolia Simple Staking Contracts 
  - 80279cc6-a6d0-442a-9744-1b5837796677 
```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
"Layer2RegistryProxy" : 0xA0a9576b437E52114aDA8b0BC4149F2F5c604581 
DAOVault : 0xB9F6c9E75418D7E5a536ADe08f0218196BB3eBa4

DAOCommitteeProxy : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386
```

> [!tip]
> 💡 Suppose you specify TokamakTimelockController as the owner of DepositManager and SeigManager (Pre-work 2). In this case, it is very convenient to use the interface when changing the settings of DepositManager and SeigManager by creating an agenda with Tally. (Can be used like P1, P2) DepositManager and SeigManager support multiple owners, which makes this interface possible.

> [!tip]
> 💡 In the case of DAOVault, since the owner is one account.  we can add logic to DAO (Pre-work 3) and execute the function of DAOVault through DAO. (Example P4)

## Pre-work 

### Pre-work 1 

- Changed the min delay of the timelock controller to 300 (1 hour). [tx](https://sepolia.etherscan.io/tx/0x91957a54883361bad22963a16eba7e26e2582e429566e10f90a0592965ebea0f#eventlog) 
- Changed the set values of Governor 
  - votingDelay: 300 ( 1 hour )
  - votingPeriod: 300 ( 1 hour )
  - lateQuorumVoteExtension: 150 ( 30 mins ) (previously it was one day, but changed to 30 minutes. When the quorum is reached during voting, the voting deadline is extended by lateQuorumVoteExtension.)

### Pre-work 2 

- Add Owner TokamakTimelockController in DepositManager [tx](https://sepolia.etherscan.io/tx/0x17fb3753f41423f9f21c82ea083ba87bd7d5fddcd43670468bb863ae33960e6c)  
- Add Owner TokamakTimelockController in SeigManager 

### Pre-work 3

- DAO v1  
  - add storages ( timelockController, securityCouncil) 
  - add logics : DAOCommittee_SecurityCouncil_address = "0xDB86F93e01ba0424aEECfA2C1D87680a5614d8d2”
    - [executeTransactions](https://github.com/tokamak-network/ton-staking-v2/blob/bae4ce783774487ca6d61d558723e4d7090a7f2e/contracts/dao/DAOCommittee_SecurityCouncil.sol#L64)
    - [executeTransaction](https://github.com/tokamak-network/ton-staking-v2/blob/bae4ce783774487ca6d61d558723e4d7090a7f2e/contracts/dao/DAOCommittee_SecurityCouncil.sol#L87C14-L87C32)
  - [commits](https://github.com/tokamak-network/ton-staking-v2/commit/bae4ce783774487ca6d61d558723e4d7090a7f2e) 

## Proposal 

### (Executed) P1. DepositManagerProxy.**setGlobalWithdrawalDelay (**globalWithdrawalDelay**)**

### (Executed) P2. SeigManagerProxy.**setMinimumAmount**(minimumAmount_)

### P3. SeigManagerProxy’s **setPowerTONSeigRate, setDaoSeigRate, setPseigRate**

### (Executed) P4. DAOVault.claimERC20 

### P5. TON.addMinter

### P6. WTON.addMinter

### (Script Test - Done) P7. Security Council cancel or stop a successful proposal