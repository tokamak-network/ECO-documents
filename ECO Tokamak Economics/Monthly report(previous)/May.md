## 1. Developments in May

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
    - migrate agenda page
  - **Server migration**
    - migrate server to private AWS account

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the Sepolia
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **Progress**
  - Hold a seminar on Layer2Candidate for audit ( doc)
  - Register  titan-sepolia, thanos-sepolia candidate on sepolia simple staking (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/deploy_sepolia_v2/)) 
  - test titan-sepolia candidate on sepolia simple staking (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/deploy_sepolia_v2/))
  - define the process for stopping seigniorage issuance to Layer2Candidate (doc) 
  - Audit about Layer2Candidate (doc)
  - upgrade DAO Contract for DAO Structure & Layer2Candidate (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/NewDAOStructure/))
  - test DAO Contract & Layer2Candidate (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/NewDAOStructure/))
  - Deploy & Setting change DAOStructure & function on sepolia ([doc](/3b3a8c856cf041f9bf1b8fae8e5f0510))
  - Simple Staking V2 [withdraw modal](https://zpl.io/WQK50r7) UX/UI Update

### Tokamak DAO V2 

- **Motivation**
  - Provide better UX/UI about the price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (model) Finalize Tokamak DAO Policy/ Guidelines
- **Progress**
  - There has been no progress this month

## 2. Goals in June

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
  - (model) finish tooltips and language part of the UIs
  - (contract)  Develop the function for stopping seigniorage issuance to Layer2Candidate
  - (contract) Gas optimization and refactoring contracts to provide seigniorage to the sequencer of Layer2Candidate 
  - (contract) Do audit the contracts to provide seigniorage to the L2 sequencer
  - (contract) Make the document about how to set on mainnet
  - (service) Implement Staking v2 page

** **

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI for the price dashboard and use it for the new DAO model
  - Using Tally for managing the new DAO.
- **Goals**
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.

## 3. Others

- operating cost of this month is about 317 $ (AWS)

## 4. Comments from Tokamak Network

- 