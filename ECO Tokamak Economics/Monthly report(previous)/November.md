## 1. Developments in November

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO maintenance
  - Price dashboard maintenance
- **Achievement**
  - **Staking:** 
    - no progress
  - **DAO**: 
    - 
  - **Price Dashboard**
    - 
  - **Design**
    - Integrated GNB, Footer Design for New L2 On-Denad(TRH) Service Addition. (Notion)
    - Tokamak Network v2 storyboard planning support. ([Figma](https://www.figma.com/design/7u09jK09RXmdi9umRSQZoy/Tokamak-Network-Landing-Page?node-id=730-14&t=YSmvuLr9rTHdItbt-4))
  - **Storyboard**
    - Tokamak network landing page minor update ([docs](/d84d1bbf22014b198c973d10c56e5db8), [slide](https://docs.google.com/presentation/d/1JVWJVXCjFOzsr2Le1J1gEprIHMJTpYz7yKllnINoSls/edit#slide=id.g2f91639884e_1_0))

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page 
  - (contract) internal audit, deployment staking v2.5 contracts on mainnet, propose an agenda for upgrading staking v2.5
  - (design) Finalize storyboard and design for staking V2
- **Achievement**
**Service**

  - Simple Staking v2.5 UX/UI [usability improvement](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=82-240&node-type=frame&t=f9uGdunUtUUaONH2-11)

**Design**

  - Simple Staking v2.5 UX/UI [usability improvement](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=82-240&node-type=frame&t=f9uGdunUtUUaONH2-11)

**Contract**

  - Deploy TON staking V2.5 contract + upgrade DAO to support preliminary security council features
    - [issue #59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    - [DAO Agenda #13](https://dao.tokamak.network/#/agenda/13): End the notice on Nov 15, 2024, 18:35**,  waiting to vote **
- **Progress(compared with Q3 goals)**
  - Staking V2.5 will not open.

### Tokamak DAO V2 

- **Motivation**
  - To improve DAO and communication with external parties
- **Goals**
  - Determine a voting style suitable for DAOv2
  - Research and identify how cross-chain governance can be implemented in DAOv2
- **Achievement**
  - Summary of functions related to voting tokens doc
  - Research The Security Council Management Contract of ArbitrumFoundation(doc) 
  - L2 DAO Research & Decided the Policy (doc)
  - L2 DAO Test (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2-DAO-Test/))
  - Develop the functions of DAO for only the security council and the TokamakTimelock  ([issue#60](https://github.com/tokamak-network/ton-staking-v2/issues/60), [commit](https://github.com/tokamak-network/ton-staking-v2/commit/bae4ce783774487ca6d61d558723e4d7090a7f2e))
- **Progress(compared with Q3 goals)**
  - DAO v2 Policy DOC initial draft completed ([Link](/135d96a400a3808ebad2ea61e879db8b))

## 2. Goals in December

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - **Service** - Set DAO infra on Holesky
  - **Storyboard** - Finalize Tokamak network landing page minor update
  - **Design** **- **Simple staking UX/UI usability improvement
- **Achievement**
  - **Staking:** 
    - 
  - **DAO**: 
    - 
  - **Price Dashboard**
    - 
  - **Design**
    - Tokamak Network v2 storyboard planning support.
    - Tokamak Network v2 website renewal Design.
  - **Storyboard**
    - 

### Staking V2 

- **Motivation**
  - To give incentives to the L2 sequencer & improve UX / UI
- **Goals** 
**Model**

  -  assist with closing down the service → make community posting for closing down and ensure the community that the service will be serviced by third party member

**Service**

  - Finalize Staking V2.5 UI
  - Implement mobile version
  - Prepare closing down the service

**Contract**

  - Create etherscan/my crypto wallet guide  
  - Register ‘Titan DAO’ on simple staking service After executing [the DAO Agenda #13](https://dao.tokamak.network/#/agenda/13)

### Tokamak DAO V2

- **Motivation**
  - Test and validate the proposal flow using the policy doc 
  - Security Council validation
- **Goals**
  - Release the completed version of the Policy doc
  - (On Sepolia) Develop the test scripts to check the security council's functions [issue#8](https://github.com/tokamak-network/ton-staking-tally-contract/issues/8)  
  - (On Sepolia) Modify the functions or delete the existing functions on DAO v1 to migrate to tally 
    - Check if there are any problems with the existing DAO code about Our Tally’s Contract(Tally’s TokamakTimelock Contract & Security Council Contract)
  - (On Sepolia) Test creating and executing proposals in Tally 
    - (L1) Changes to simple staking settings, TON, WTON minter permissions, DAO Vault token claim, contract upgrades, security council member changes, etc.
    - (L2) Test the L2 DAO (Thanos, Optimism)
  - make the document about deleting from existing DAOv1
    - delete the functions from DAOv1
    - make the document

## 3. Others

**Project ECO’s Frontend service closure & next phase plan:**

1. **Simple staking (simple.staking.tokamak.network)**
  1. Shutdown by -> Prepare hosting guide
  1. Create basic version for other developers to build on top of (no end date yet)
  1. Create etherscan/my crypto wallet guide by 2024.12
  1. Create contract development guide (no end date yet)
1. **DAO (dao.tokamak.network)**
  1. Shutdown by 2025 Q1 -> Open on Tally
  1. Create contract development guide (no end date yet)
1. **Price dashboard (price.tokamak.network)**
  1. Move it to tokamak.network by 2025
1. **Tokamak Network (tokamak.network)**
  1. Small update by 2024.12
  1. Full update by 2025

## 4. Comments from Tokamak Network

- 