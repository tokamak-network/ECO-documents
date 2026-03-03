## 1. Developments in July

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO service re-open
  - Price dashboard maintenance
- **Progress**
  - **Staking:** 
    - no progress
  - **DAO**: 
    - no progress
  - **Price Dashboard**
    - no progress
  - **Migrate DAO to react**
    - no progress

**Design**

  - Service ([Simple Staking, ](https://zpl.io/bJo96r3)[TITAN](https://zpl.io/6N9EB3m), [DAO](https://zpl.io/30XKZnW)) menu 'more' reorganized.
  - Tokamak network [Brand kit](https://tokamak.notion.site/Tokamak-Network-Brand-Kit-6b0c1badd78446f98b60cdd0e4b30456)

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the Sepolia
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **Progress**
**Contract**

  - Request the code review & feedback [#16](https://github.com/tokamak-network/ton-staking-v2/issues/16) ([#17](https://github.com/tokamak-network/ton-staking-v2/issues/17), [#18](https://github.com/tokamak-network/ton-staking-v2/issues/18), [#19](https://github.com/tokamak-network/ton-staking-v2/issues/19), [#20](https://github.com/tokamak-network/ton-staking-v2/issues/20), [#21](https://github.com/tokamak-network/ton-staking-v2/issues/21), [#22](https://github.com/tokamak-network/ton-staking-v2/issues/22), [#23](https://github.com/tokamak-network/ton-staking-v2/issues/23), [#25](https://github.com/tokamak-network/ton-staking-v2/issues/25) ) 
  - Add explorer function to Operator Contract [#24](https://github.com/tokamak-network/ton-staking-v2/issues/24#issuecomment-2216697884)
  - code review the Layer2Candidate about updateSeigniorage  ([issue28](https://github.com/tokamak-network/ton-staking-v2/issues/28), [question1](https://github.com/tokamak-network/ton-staking-v2/issues/29), [question2](https://github.com/tokamak-network/ton-staking-v2/issues/30), [question3](https://github.com/tokamak-network/ton-staking-v2/issues/31))
  - Answering the question for Staking V2 UI Implementation: doc  
  - Update contract interface for usage on the web service: doc

**Service**

  - implement withdraw tab in mobile([commit](https://github.com/tokamak-network/simple-staking-v2/commit/8ace8921782bd30b24ceb223e688f8ff07dd14bc))
  - implement withdraw modal([commit](https://github.com/tokamak-network/simple-staking-v2/commit/86ce3aa4b2a9b419f607f19dfb55505b55e55492))
  - update subgraph for layer2Candidate & withdrawAndDeposit([commit](https://github.com/tokamak-network/staking-v1-subgraph/commit/ddbf70279e0394c8366e7afbab9de5b18cef683f))

### Tokamak DAO V2 

- **Motivation**
  - Provide better UX/UI about the price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (model) Finalize Tokamak DAO Policy/ Guidelines
- **Progress**
  - DAO Governance Lifecycle - [Slides](https://docs.google.com/presentation/d/1WKX2bD96Qe7JNRFq_npK4eI0yPoiGXn4_pitd-2F6t8/edit?usp=sharing)
  -  Explore a token using SWTON that can be used in Tally [#27](https://github.com/tokamak-network/ton-staking-v2/issues/27) (Analysis of tally, Design a contract )  
  - Develop the tokamak tally contracts [#1](https://github.com/tokamak-network/ton-staking-tally-contract/issues/1) 
  - Test the tokamak tally basic functionality [#3](https://github.com/tokamak-network/ton-staking-tally-contract/issues/3)
  - [Titan Wrapped Staked TON presentation](https://docs.google.com/presentation/d/1y1XPOOr5DD1CXl_PpzLoFzmTwWsi22tEPLoWZQbkD30/edit#slide=id.gcb9a0b074_1_0)

## 2. Goals in August

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - finalize DAO migration(in PC version)

### Staking V2 

- **Motivation**
  - Robust code through gas optimization and internal auditing of the contract that provides seigniorage to the L2 Sequencer.
  - Upgrade existing simple staking service to support registration and display of L2 reference chain (Titan, Thanos) information
- **Goals** 
  - Pause the Titan-sepolia and Thanos-sepolia-test layers, re-deploy code reviewed contracts, and then register titan-sepolia and thanos-sepolia again.
  - internal QA

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI for the price dashboard and use it for the new DAO model
  - Using Tally for managing the new DAO.
  - Define the Governance Process for New DAO
- **Goals**
  - Testing the basic functionality of the Tokamak tally contracts
  - Production of various scenario scripts for Tokamak tally contracts 
  - Request a code review for the Tokamak tally contracts
  - Finalize rulebook for Tokamak DAO Governance
  - Setup associated tools for Governance (Forum, Snapshot etc)

## 3. Others

- 

## 4. Comments from Tokamak Network

- 