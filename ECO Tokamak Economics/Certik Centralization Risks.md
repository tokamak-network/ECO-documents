## Contract Addresses on Mainnet 

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
```

## Owner of  Contracts 

```json
MultisigWallet :   
- owners : 0x77b9D55e98126CD457D8F914647e634613D2A7fc, 0x9de8cAc67B6514837c31F367aC18a457d8f34c3D, 0xa4ABB4Bb512Fc1fecF5556ADDa9B8a4C96dc3790

DAOCommitteeProxy : (MultiSigWallet) 0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95

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

- In the contract `CandidateAddOnV1_1` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE :  DAOCommitteeProxy contract.  
  - CandidateAddOnFactoryProxy is isAdmin
    - [https://etherscan.io/address/0xFA8ce5caF456115E72B96E5074769b8f66AA5861#readContract#F11](https://etherscan.io/address/0xFA8ce5caF456115E72B96E5074769b8f66AA5861#readContract#F11)
    - input : 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
    - result : true
  - CandidateAddOnFactoryProxy setAddress
    - [https://etherscan.io/tx/0xfc9ee401cc6f5997140e2ecd48a822ef1e7d75da51046dc9425d3c53e7e58132](https://etherscan.io/tx/0xfc9ee401cc6f5997140e2ecd48a822ef1e7d75da51046dc9425d3c53e7e58132)
  - so DEFAULT_ADMIN_ROLE of CandidateAddOnV1_1 is DAOCommitteeProxy.
- In the contract `DAOCommittee_V1`  & `DAOCommitteeOwner` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE : DAOCommitteeProxy contract & MultiSigWallet Contract
  - DAOCommitteeProxy
    - grantRole to MultSigWallet : [https://etherscan.io/tx/0x9e85908ae5d27fd1bf9d118a33d69efa657af3bd73adc1ecb9fe0c397ed22944](https://etherscan.io/tx/0x9e85908ae5d27fd1bf9d118a33d69efa657af3bd73adc1ecb9fe0c397ed22944)
    - revokeRole to EOA : [https://etherscan.io/tx/0xba6c643ad25fb1e04b1790928cb2dafaa1bada240bcded22b2aece08b3db09d0](https://etherscan.io/tx/0xba6c643ad25fb1e04b1790928cb2dafaa1bada240bcded22b2aece08b3db09d0)
    - How to Check
      - [https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F11)
      - hasRole
        - role : 0x0000000000000000000000000000000000000000000000000000000000000000
        - account : [0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95](https://etherscan.io/address/0xE3F72E959834d0A72aFb2ea79F5ec2b4243d2d95) (MultiSigWallet)
        - result : true
      - hasRole
        - role : 0x0000000000000000000000000000000000000000000000000000000000000000
        - account : 0xB4983DA083A5118C903910DB4f5a480B1D9f3687 (EOA)
        - result : false
- In the contract `L1BridgeRegistryV1_1` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE :  DAOCommitteeProxy contract.  
  - How to Check
    - [https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F14](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F14)
    - isAdmin
      - account : 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
      - result : true
- In the contract `L1BridgeRegistryV1_1` the role `MANAGER_ROLE` 
  - MANAGER_ROLE : DAOCommitteeProxy contract.  
  - How to Check
    - [https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F15](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F15)
    - isManager
      - account : 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
      - result : true
- In the contract `L1BridgeRegistryV1_1` the role `REGISTRANT_ROLE`
  - There is no address with REGISTRANT_ROLE.
  - The authority to set REGISTRANT_ROLE belongs to MANAGER_ROLE.
  - MANAGER_ROLE authority belongs to DAO.
    - [L1BridgeRegistryProxy.isManager](https://etherscan.io/address/0x39d43281a4a5e922ab0dcf89825d73273d8c5ba4#readContract#F15)(0xDD9f0cCc044B0781289Ee318e5971b0139602C26) returns true.
- In the contract `L1BridgeRegistryV1_1` the role `seigniorageCommittee`
  - seigniorageCommittee : DAOCommitteeProxy contract.  
  - How to Check
    - [https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F26](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4#readContract#F26)
    - result : [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)
- In the contract `Layer2ManagerV1_1` the role `DEFAULT_ADMIN_ROLE` 
  - seigniorageCommittee : DAOCommitteeProxy contract.  
  - How to Check
    - [https://etherscan.io/address/0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D#readContract](https://etherscan.io/address/0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D#readContract)
    - isAdmin
      - account : 0xDD9f0cCc044B0781289Ee318e5971b0139602C26
      - result : true
- In the contract `Layer2ManagerV1_1` the role `_l1bridgeregistry` 
  - onlyL1BridgeRegistry is L1BridgeRegistry Contract. 
    - [Layer2ManagerProxy.l1BridgeRegistry()](https://etherscan.io/address/0xd6bf6b2b7553c8064ba763ad6989829060fdfc1d#readContract#F12) is [0x0b55a0f463b6DEFb81c6063973763951712D0E5F](https://etherscan.io/address/0x0b55a0f463b6DEFb81c6063973763951712D0E5F)  (SeigManagerProxy Contract).
  - L1BridgeRegistryProxy’s DEFAULT_ADMIN_ROLE is DAOCommittee contract.  
    - [L1BridgeRegistryProxy.isAdmin](https://etherscan.io/address/0x39d43281a4a5e922ab0dcf89825d73273d8c5ba4#readContract#F14)(0xDD9f0cCc044B0781289Ee318e5971b0139602C26) return true
- In the contract `Layer2ManagerV1_1` the role `seigManager`
  - `seigManager` is SeigManagerProxy Contract.
    - [Layer2ManagerProxy.seigManager() ](https://etherscan.io/address/0xd6bf6b2b7553c8064ba763ad6989829060fdfc1d#readContract#F20)is [0x0b55a0f463b6DEFb81c6063973763951712D0E5F](https://etherscan.io/address/0x0b55a0f463b6DEFb81c6063973763951712D0E5F)  (SeigManagerProxy Contract).
- In the contract `OperatorManagerV1_1` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE : DAOCommitteeProxy contract.   
    - [OperatorManagerFactory.owner](https://etherscan.io/address/0xaf86b21edddc78ea27e23a7f2151d60d4e069450#readContract#F5)() is [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26) 
- In the contract `OperatorManagerV1_1` the role `_candidateaddon`
  - Deleted  the modifier onlyCandidateAddOn, and deleted the related functions. 
- In the contract `OperatorManagerV1_1` the role `_ownerormanager` 
  - owner : DAOCommitteeProxy contract.   
    - [OperatorManagerFactory.owner](https://etherscan.io/address/0xaf86b21edddc78ea27e23a7f2151d60d4e069450#readContract#F5)() is [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26) 
  - manager is the account receiving L2 sequencer seigniorage, This address is an account managed by the L2 operator and L2 must manage this account well.
- In the contract `DepositManagerV1_1` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE : DAOCommitteeProxy contract.   
  - [DepositManagerProxy.isAdmin](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#readContract#F10)(0xDD9f0cCc044B0781289Ee318e5971b0139602C26) returns true
- In the contract `SeigManagerV1_3` the role `DEFAULT_ADMIN_ROLE`
  - DEFAULT_ADMIN_ROLE : DAOCommitteeProxy contract.   
  - [SeigManagerProxy.isAdmin](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readContract#F23) (0xDD9f0cCc044B0781289Ee318e5971b0139602C26)   returns true 

[[[Issue] Centralization Risks]]