## 1. Developments in August

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO service re-open
  - Price dashboard maintenance
- **Achievement**
  - **Staking:** 
    - no progress
  - **DAO**: 
    - Additional DAO changes ([issue34](https://github.com/tokamak-network/ton-staking-v2/issues/34#issue-2463316829))
    - DAO vulnerability: setExecutedCount method issue (doc, [issue](https://github.com/tokamak-network/tokamak-dao-contracts/issues/7))
    - Resolve “Staking vulnerability: withdraw delay issue” ([#33](https://github.com/tokamak-network/ton-staking-v2/issues/33)) and executed the related [agenda #11](https://dao.tokamak.network/#/agenda/11)
  - **Price Dashboard**
    - Staked amount related issue.
  - **Migrate DAO to react**
    - no progress
  - **Design**
    - Transfer of [TITAN](https://www.figma.com/design/U59zRP315qgNaiebTcedDk/L2-Mainnet?node-id=0-1&t=tFoQ7zItaeh7DHj2-11) & [Tokamak Network](https://www.figma.com/design/9QZfHwoowVz7hahu1SK7gG/Tokamak-Network?node-id=0-1&t=oUtf3n66lOmcWiEv-11) design environment.

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the Sepolia
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **Achievement**
**Contract**

  - make the codeReivew document about DAOContract([link](https://hackmd.io/@iqEXmofyQeyUFZRbg94Aiw/By9hcceqR), [github](https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/doc/kr/dao-upgraded.md))
  - Refactor the ton-staking-v2 to staking-v2.5 ([#35](https://github.com/tokamak-network/ton-staking-v2/issues/35)) 
  - (staking-v2.5) Modification of contract interface guide: doc
  - (staking-v2.5) Edit the contract description document: [en](https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/docs/en/ton-staking-v2.md), [kr](https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/docs/kr/ton-staking-v2.md)
  - Fix stakeOfAllLayers() + stakeOfAllLayersAt() function ([#36](https://github.com/tokamak-network/ton-staking-v2/issues/36))
  - Updated DAO changes according to StakeV2.5 ([#34](https://github.com/tokamak-network/ton-staking-v2/issues/34#issuecomment-2301019338))

**Service**

  - implement & test functions in mobile([commit](https://github.com/tokamak-network/simple-staking-v2/commit/d2e42ab2cefb365e092ac7618b31de5c89e19920))
  - implement withdraw to l2 table([commit](https://github.com/tokamak-network/simple-staking-v2/commit/82b41b525f53f113ead209dab10aa05b91781da1)) 
  - update subgraph([commit](https://github.com/tokamak-network/staking-v1-subgraph/commit/d6b396c9abd64ee1dcdb73524b72ca0b00b4717f))
  - request QA & check result ([doc](/3b0769cfad7b4d6fba2ffedf30ee3281))
- **Progress(compared with Q3 goals)**
  - deploy contracts on mainnet
    - new contract deployed
    - test remained
  - Update white paper
    - will be proceed
  - publish it to testnet & mainnet(pc/mobile)
    - internal QA was finished(based on old contract)
    - can be published on testnet within a few weeks

### Tokamak DAO V2 

- **Motivation**
  - Provide better UX/UI about the price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (model) Finalize Tokamak DAO Policy/ Guidelines
- **Achievement**
  - Internal Seminar: Security Council Formation([Slides](https://docs.google.com/presentation/d/1fYO5f1nx-PYW_T_dwA5TPXeOiYZX0RFOYmgrJvGXm74/edit?usp=sharing))
  - Uniswap Cross chain Governance Contract Flow (Notes)
  - Develop the several scenario scripts about the tokamak tally ([#4](https://github.com/tokamak-network/ton-staking-tally-contract/issues/4), [#5](https://github.com/tokamak-network/ton-staking-tally-contract/issues/5#issuecomment-2268626253), [#6](https://github.com/tokamak-network/ton-staking-tally-contract/issues/6))
  - Tokamak DAO v2 (Proposal Flow, Tools, Security Council) Seminar ([Slides](https://docs.google.com/presentation/d/1vcK6ybg6qmC0Jfhfwwhwi61WJ23EEL3YasXZAYZ_qls/edit?usp=sharing))
- **Progress(compared with Q3 goals)**
  - Seminar on DAO Proposal
    - done
  - Document defining integration of Staked WTON with Tally
    - integration of WTON with Tally contract is done
    - documentation will proceed
  - Finalize policy guidelines of DAO
    - progress is about 60%
    - need to finalize the voting pattern/sturcture, and security council membership
  - Seminar on using Tally to interact with Arbitrum DAO
  - Build an MVP on Sepolia with proposed structure and guidelines

## 2. Goals in September

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - finalize DAO migration(in PC version)
- **Design**
  - Reconfiguration of [TITAN](https://www.figma.com/design/U59zRP315qgNaiebTcedDk/L2-Mainnet?node-id=0-1&t=tFoQ7zItaeh7DHj2-11) & [Tokamak Network](https://www.figma.com/design/9QZfHwoowVz7hahu1SK7gG/Tokamak-Network?node-id=0-1&t=oUtf3n66lOmcWiEv-11) design environment.

### Staking V2 

- **Motivation**
  - Robust code through gas optimization and internal auditing of the contract that provides seigniorage to the L2 Sequencer.
  - Upgrade existing simple staking service to support registration and display of L2 reference chain (Titan, Thanos) information
- **Goals** 
  - test the sepolia simple staking contracts (ton-staking-v2.5) 
  - test the Updated DAO changes according to StakeV2.5
  - test front-end part according to stake v2.5

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI for the price dashboard and use it for the new DAO model
  - Using Tally for managing the new DAO.
  - Define the Governance Process for New DAO
- **Goals**
  - Modify TokamakGovernor to use voting weight as a quadratic voting ([#7](https://github.com/tokamak-network/ton-staking-tally-contract/issues/7))
  - develop the tokamak tally contracts and security council contracts 
  - Finalize the Policy on voting pattern/structure , security council
  - Cross Chain Governance Transaction flow
  - Write governance proposal examples for different scenarios

## 3. Others

- 

## 4. Comments from Tokamak Network

- 