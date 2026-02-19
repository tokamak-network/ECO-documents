# TON Staking V2 Upgrade and Audit Announcement

# Background

The Tokamak Network Foundation proposes the TON Staking V2 upgrade to enhance the TON economy. This upgrade allows for the creation of DAO candidates using Layer2 of TRH(Tokamak Rollup Hub), enabling  TRH Layer2’s operators to receive seigniorage based on the amount of TON locked in the bridge (or portal). This aligns with the roadmap set forth in the Tokamak Layer2 Economic Whitepaper to support the development of the Tokamak ecosystem. More details on this can be found in the TON Staking V2 Seigniorage Issuance Mechanism [section 2.2.2 of the Tokamak Whitepaper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2).

# Purpose of the upgrade contracts

Modify and add contracts for the following purposes:

1. Upgrade the DAO contract to provide additional functionality to create DAO candidates using TRH(Tokamak Rollup Hub)’s Layer2.
1. Modify the TON seigniorage distribution logic to match seigniorage mecahnism of Whitepaper V2, allowing L2 operators to receive seigniorage based on their L2 TVL (based on the amount of TON locked in the bridge or portal).

# Purpose of auditing

In order to ensure the functionality and security of the upgraded and added contracts, we will run TON Staking V2 and DAO Contract Audit. Through the contract audit, we have tried to secure the overall security and integrity of the TON Staking and DAO service, and have done our best to eliminate contract vulnerabilities by considering malicious activities in advance.

# Content and scope of auditing

## **Description of changes**

- Description of staking v2.5: [description](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/docs/en/ton-staking-v2.md)
- Description of DAO upgrade: [description](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md)

## Contract scope  

- Repo (Branch): [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request)
  - The latest commit hash:  **01e198130b178757dd194bd8726a1ab678fca167**
- DAOCommitteeProxy2.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol)
- DAOCommittee_V1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol) 
- DAOCommitteeOwner.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol)
- SeigManagerV1_3.sol : [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol) 
- DepositManagerV1_1.sol: [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol)
- L1BridgeRegistryV1_1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol)
- Layer2ManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol)
- OperatorManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol)
- CandidateAddOnV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol)

## The auditors

- Certik  [https://www.certik.com/](https://www.certik.com/)
- BlackCow 
- Carl Park @4000d 
- Omniscia   [https://omniscia.io/](https://omniscia.io/)

# Deploying the TON Staking V2 & DAO V2 Contracts

- L1BridgeRegistryV1_1 [0x259Ac335EB42d345A61bE48104eC0Ec20b283F14](https://etherscan.io/tx/0x9510b0b6021e50706771ed43143f8ee5fede24e73148827c6c630819fc8e7ae4)
- L1BridgeRegistryProxy [0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4](https://etherscan.io/tx/0xebdf3ff64f0db31be4c08a083be9f942b23cd00b3b634f982dfd41272f76b243)
- OperatorManagerV1_1 [0xB5F3b31dFB4DCe9a2FA12dE50A97250d60823750](https://etherscan.io/tx/0x1e67f8b4760742acf58ba220ff988fafb2f4c3c9359ce318d48dbc75eff40c61)
- OperatorManagerFactory [0xAf86b21edDdC78ea27E23A7F2151d60d4e069450](https://etherscan.io/tx/0x3737cb1cada96576fe46786608a4daf448f95fed7a43e4ef9dfe54e81de1e76c)
- CandidateAddOnV1_1 [0x73Bfd5cAEC63307784C7B6d2555F18ec24D96E2e](https://etherscan.io/tx/0x38cb0e701c23e397ed8fdc0f6fa5b4aa4516be04522bfd168b9b6b28be265c70)
- CandidateAddOnFactory [0x557E24b5CbFbDA3e5aC1bD01F38EcDe865791Bc5](https://etherscan.io/tx/0x5c4044e871d677ee662c518fb14902a05f3a55ef6bc3217d705ac47d4e190b0f)
- CandidateAddOnFactoryProxy [0xFA8ce5caF456115E72B96E5074769b8f66AA5861](https://etherscan.io/tx/0xbe9d8e180fe4d324b6b8cacc2f7857731744489a6076744a38ae1553d3f850af)
- Layer2ManagerV1_1 [0x2EB7f500125f11544392B83B87cDEb9456f3509f](https://etherscan.io/tx/0x3b2e2e24328eb72dc89714645fd628664a71ca381ecdd11e127acdd1a449b163)
- Layer2ManagerProxy [0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D](https://etherscan.io/tx/0x9cce9532345917fda587ca449b460b54a0156a21a79a352480026c0e44ffa2ca)
- SeigManagerV1_2 [0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4](https://etherscan.io/tx/0xbf1ad3e583ae4e59ea5863eabc1dfa8878f2d455c2b6d3cc01517dadc4358f3d)
- SeigManagerV1_3 [0xce18C6F84F10881eA47A43AF7311A29bb116F628](https://etherscan.io/tx/0x469b2dda84c4694113c2ca8ed721e33524c872e3de268ac3ac0cb9fd277fb3b3)
- DepositManagerV1_1 [0x74bC3031b9369e6b898e82784106257D4D37Eac5](https://etherscan.io/tx/0x092c57a96eb7f8ad39c27544f4fcdb6582046d932c2ce938bc933affb5618de8)
- DAOCommitteeProxy2 [0x9e7f54efF4A4D35097e0Acb6994A723F1a28368c](https://etherscan.io/tx/0xc6e5baea2c74c223c566a478dcfd9241f2a48918daa2ce623a9dbb201ba7af1c)
- DAOCommitteeOwner [0xcb9859Dc0fBECa68eFFf2bce289150513fdF7D92](https://etherscan.io/tx/0x6f375e4993f0d28a893ef17ef6319aab231cb47d06ffc43e7cd702b8a8c199a1)
- DAOCommittee_V1 [0x9050Af1638f379A018737880aD946CdDA9101A25](https://etherscan.io/tx/0x5d3f35a22b27c90e0860780f97b385e205e5f41175cc4ba59a2245c53daecb32)

# Deploying the MultisigWallet Contract

- MultisigWallet [0xe3f72e959834d0a72afb2ea79f5ec2b4243d2d95](https://etherscan.io/tx/0xf97c035481c4498afaefd0de3cb1584029b23d309d604da17308578af6f78af1)