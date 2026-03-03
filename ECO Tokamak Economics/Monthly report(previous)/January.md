## 1. Developments in January

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO service re-open
  - Price dashboard maintenance
- **Progress**
  - **DAO** - Implement and prepare to deploy DAO_Committe_V1([commit](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/), [doc](/7fb6a7ba69074bae99a9f60985db3509)) - 100%
  - **DAO -** QA([link](/96240df7f1df471292edcff8b6dda7c2))
    - reflect feedback([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/a7d2070c3729ed1c4a557451b469fc8a499904ca))
  - **Staking** - update expected seig formula
  - **Staking** - non-deposited operator issue
    - update staking UI related with non-deposited operator([storyboard](https://www.figma.com/files/project/184786887/Team-project?fuid=1185093972752859396), [UI](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1705915313813089?thread_ts=1705887413.313179&cid=C0416F1TNE5), [commits](https://github.com/tokamak-network/simple-staking-v2/commit/3d8e75f90f854ef7bd0457dba9e5f3c9900be52b)) - 100%
    - solve non-deposited operator issue([link](https://drive.google.com/file/d/1EPmJxjGrA8YzL2JiVcCN3JJBGBz6qHo7/view)) - 100%
  - **Price dashboard** - troubleshoot price.tokamak.network([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/1ef64fa412be97fc6cc86d0ced56c9ab4db415d6))

### Staking V2 & FW (25%)

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - Research and finalize FW logic model 
    - Core service improvement
      - Provide support to integrate Optimism Bedrock withdraw process to existing FW logic 
      - Finalize FW fee policies (based on time, amount, etc)
    - Vulnerability check + Optimization: 
      - Basic vulnerability checklist for L1↔L2 communication 
      - Vulnerability check for abusing FW
      - Operation efficiency check to reduce gas usage 
  - Work on L2 registry 
    - Research competitors (Optimism Superchain, Arbitrum Orbit, [Celestia](https://celestia.org/)) + Make a list of features we want to include: **~ End of January**
    - Determine overall UX for L2 registry + check in with core team (require verification + restriction for registration): **~ End of February **
    - Work with the design team to create a storyboard:** ~ End of March**
    - If it may reduce a lot of migration resource
- **Progress**
  - FW modeling([slides](https://docs.google.com/presentation/d/1LWuEAHuN8F6pNguYcS6l3317WAnbTLAE/edit#slide=id.p1)) - 80%
  - L2 Registry research([slides](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit#slide=id.g2b2a2873c15_0_0)) - 80%

### Tokamak DAO V2 (15%)

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - Finalize DAO mechanics (Policy Guideline/Rule Book, Overall Process Diagram)
- **Progress**
  - DAO Policy guidelines ([link](https://docs.google.com/document/d/1rRV7SY7yp10adgymcVlZpD4VvuS9xr1Mk7A32jpqoHs/edit?usp=sharing)) - 50%
  - DAO Stage Seminar([link](https://docs.google.com/presentation/d/1hEiqnHllf6CgVKgWoT-D1Qa-DD1KImKwsP-hjIN5G0o/edit#slide=id.g2ada51891fe_0_15)) - 100%
  - research contract about Tally use token on sepolia([commit](https://github.com/tokamak-network/tally-erc20/commits))

## 2. Goals in February

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - re-open DAO
  - update staking dashboard
  - deploy the DAOCommitte_V1 on mainnet

### Staking V2 & FW

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - Finalize FW model design
  - Seminar about research competitors
  - Determine overall UX for L2 registry and communicate with Core team

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to new DAO model
- **Goals**
  - write a draft policy framework for the DAO 
  - deploy tally DAO contract to test on sepolia

## 3. Others

- 

## 4. Comments from Tokamak Network