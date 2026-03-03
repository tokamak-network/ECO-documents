## 1. Developments in April

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
    - Simple Staking burger menu UI [Update](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1712560888651799?thread_ts=1712311420.136489&cid=C0416F1TNE5)
    - update simple staking UX/UI([commit](https://github.com/tokamak-network/simple-staking-v2/commit/71eb3fc99d17e8c8026ed8ba1f35bd7dd0ca93a8))
  - **DAO**: 
    - reflect feedback to DAO([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/33eb747855cbb44e5e0e2ba8ab52de1d4cef80b7))
    - DAO page Mainnet reopen UI ([update](/c0143a8ecbfe477c81c505573b6870f1))
    - worked on [user guide ](https://docs.tokamak.network/)[** **](https://docs.tokamak.network/)
    - reopen DAO
  - **Price Dashboard**
    - no progress
  - **Migrate DAO to react**
    - implement challenge button in DAO([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/4223d61549f5ae0cea8440979de5dc6d0d496673)) 
    - Migrate DAO to react(Propose tab) ([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/946a1f05bdd98fb0fa2bd087503df75c16894d00))

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the thanos-sepolia-test
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **Progress**
  - develop to provide seigniorage to the Layer 2 sequencer ([doc](/f4cf189b490c4d1198a044119333d4e3), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/))
  - develop and test to give seigniorage to the Layer 2 sequencer and 'Add L2 Withdraw for staked TON' function ([doc](/f4cf189b490c4d1198a044119333d4e3), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage))
  - verify staking v2 update [seigniorage logic](https://docs.google.com/spreadsheets/d/1khbkDRD_ATWYKdmOfOJBUngxtAMp-JRDDMvFrF-AFbk/edit#gid=0)
  - made the contract interface documentation for service ([notion](/45bcb8cbd5064df192a93c199b07f464), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/))
  - developed the deployment scripts ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/))

### Tokamak DAO V2 

- **Motivation**
  - Provide better UX/UI about the price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (model) Finalize Tokamak DAO Policy/ Guidelines
- **Progress**
  - There has been no progress this month

## 2. Goals in May

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - finalize DAO migration(in PC version)

### Staking V2 

- **Motivation**
  - To provide seigniorage to L2 Sequencer
  - Upgrade existing simple staking service to support registration and display of L2 reference chain (Titan, Thanos) information
- **Goals** 
  - (contract) develop the L2RegisterDAO for seigniorage 
  - (contract) do audit the contracts to provide seigniorage to the L2 sequencer
  - (contract) create Titan and Thanos Candidate on the simple staking contracts of the thanos-sepolia-test.
  - (Model + UI) Simple Staking V2 withdraw modal UX/UI Update

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI for price dashboard and use it for new DAO model
  - Using Tally for managing the new DAO.
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 

## 3. Others

- 

## 4. Comments from Tokamak Network

- Resource 관리에 대한 부분