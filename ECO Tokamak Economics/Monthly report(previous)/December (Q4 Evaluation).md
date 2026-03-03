## Motivation: <u>Why do we develop in this project?</u>

The Tokamak Network has announced plans to launch a layer 2 (L2) protocol based on Optimism in the second quarter of 2023. However, the current infrastructure, including Simple Staking, is not suitable for the L2 environment. Additionally, with competitors such as Arbitrum, Optimism, and Boba Network already in the market, merely creating a layer 2 platform may not be enough to attract users.

To overcome these challenges, Tokamak Layer2 Economics team will provide infrastructure for the Tokamak Network’s L2 environment. So, our team’s plan is to convert the current TON ecosystem to layer2 friendly such as Staking & DAO. 

## Goals: <u>What do we want to achieve with this project?</u>

L2 Economics team aims to implement TON Staking & DAO v2 and achieve the following goals:

- Foster organic growth of the Tokamak Network
- Enhance the user experience of the Tokamak Network
- Reinforce the security of the Tokamak Network
- Alleviate the capital inefficiency of staked TON
- To support both v1 & v2 update TON seigniorage distribution model

## Original Plan

### Simple staking patch

- **Motivation**
  - To solve vulnerability and improve usability of staking related service
- **Goals**
  - contract upgrade & test
  - implement subgraph for new staking contracts
  - connect subgraph with front-end
  - front-end update(staking & dao)
  - fix staking mobile version & open it to public

### Staking V2 & FW

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - Research about how to implement FW based on current contract
    - If it is possible it reduce a lot of migration resource
  - Implement contract based on new model
  - make storyboard
  - implement subgraph
  - If model is fixed until November, V2 & FW service will be open at Q1, 2024

### Renewal price dashboard

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to new DAO model
- Goals
  - Research how to make it (3rd party or in-house)
  - adopt our model to service

## Actual Developments in Q4, 2023

- In this quarter L2 Economics team will be working on 7 types of task

**Red: Original plan, ****Blue: Additional task**

### Simple staking patch (100%)

- **Motivation**
  - To solve vulnerability and improve usability of staking related service
- **Goals**
  - front-end update(staking & dao)
  - fix staking mobile version & open it to public
  - re-open wallet tab
  - Fix DAO with new contracts & subgraph
- **Progress**
  - open mobile version with restricted functions
  - design withdraw mobile alert modal ([link](https://zpl.io/XYQjN6j)) - 100%
  - fix restaking error([commit](https://github.com/tokamak-network/simple-staking-v2/commit/4391a6be52699db9a699d6d436375093ebbec1b7)) - 100%
  - staking simulator modeling([link](https://docs.google.com/spreadsheets/d/1Gjo9Wfk3yuiLoAcOVdBJ_bgYc_2UqsUXocGwH7sHuz4/edit#gid=0)) - 100%
  - fix staking simulation calculator([commit](https://github.com/tokamak-network/simple-staking-v2/commit/8b14e46531a0c47e3942364d677d3665ecf01d65)) - 90%
  - change the total supply of SeigManager's increaseTot() function ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/dev_fix_total_supply)) - 100%
  - Simulator Modal Design Update [Link](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1699867427763399?thread_ts=1699850898.319979&cid=C0416F1TNE5) - 100%

### Check-up supply (100%)

- **Motivation**
  - Identify real total & circulation supply of TON
- **Goals**
  - Identify actual total & circulate supply of TON
- **Progress**
  - Finished updating the raw data spreadsheet ([spreadsheet](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit#gid=681869004))
  - Finished making scripts for calculating relevant information for TON supply and circulating supply ([git](https://github.com/tokamak-network/TON-total-supply))

### Renewal price dashboard (95%)

- **Motivation**
  - Provide better UX/UI and explanation of each part about price dashboard 
- **Goals**
  - Implement dashboard based on new design
- **Progress**
  - Price dashboard design([link](https://www.figma.com/file/mWxAX7DaXChDTCVKpRZWT6/Price-Dashboard?node-id=310%3A296&mode=dev))
  - Ton supply dashboard([link](https://docs.google.com/presentation/d/1jUfS2q3poHaNrjTxNam8LnzR9_o-4NatNi-hQQeOoP4/edit#slide=id.g2a1d246af18_0_61))
  - Implement dashboard([git](https://github.com/tokamak-network/pricedashboard-v2), [link](https://pricedashboard-v2.vercel.app/)) 

### Dune dashboard (90%)

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to new DAO model
- **Goals**
  - Identify dashboard metrics 
  - Writing Dune queries
- **Progress**
  - Calculating data for Dune ([doc](https://docs.google.com/presentation/d/1DfXNf_YPuHa3msE6KehIxlujaVgINasV2UBbzrOVWqc/edit#slide=id.p)) - 30%
  - Tokenomics Dashboard ([link](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard))
  - TON Staking Dashboard ([link](https://dune.com/tokamak-network/tokamak-network-staking-dashboard))

### Set up test net & re-open DAO (70%)

- **Motivation**
  - set up testnet site on sepolia and test service for re-open DAO
- **Goals**
  - Setup DAO & staking on sepolia
  - re-open DAO
- **Progress**
  - Setup staking service on sepolia
  - Setup DAO service on sepolia
  - Setup staking-api server on sepolia
  - Setup subgraph on sepolia
  - test DAO for re-open
  - Upgrade DAO contract to prevent TON held by DaoVault from being transferred elsewhere
  - DAO vulnerability fix

### Staking V2 & FW (15%)

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - Research about how to implement FW based on current contract
    - If it is possible it reduce a lot of migration resource
  - Implement contract based on new model
- **Progress**
  - worked on FW model and [sWTON sync to Titan specs](https://docs.google.com/presentation/d/1ZVpp7Kc4_G2c0q2QqDvelHRV_iqBFf6NNNngXR0oRjg/edit#slide=id.g26037f5b433_1_11)
  - [Staking Storyboard 0.1](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?type=design&node-id=1075-28485&mode=design&t=BLkiKjM9B9VtpEhI-4) (50%)

### Tokamak DAO V2 (10%)

- **Motivation**
  - To improve DAO governance based on L2 environment
- **Goals**
  - Check limitation and scope of improvement
- **Progress**
  - seminar about limitation and scope of improvement([slide](https://docs.google.com/presentation/d/16x5zJGbjZL84SU_doiPhe-xw_cGMDJbCH9hSe4Efipc/edit#slide=id.g29d3390e064_0_63))
  - Policy guidelines([doc](https://docs.google.com/document/d/1rRV7SY7yp10adgymcVlZpD4VvuS9xr1Mk7A32jpqoHs/edit#heading=h.6zco28we142u))

## Member change

| Q2 | Jason | Suah | Praveen | Zena | Harvey | Justin | Ale | Ryan | Monica |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q3 | Jason | Suah | Praveen | Zena | Harvey |  |  |  |  |
| Q4 | Jason | Suah | Praveen | Zena | Harvey | Ryan | Monica |  |  |
| Q1, 2024 | Jason | Suah | Praveen | Suheyon | Zena | Harvey | Justin | Ethan | Monica |

## Budget Usage in Q4

|  | Income (TONs) | Outcome (TONs) | Total |
| --- | --- | --- | --- |
| Initial endowment | 20,300 | 18,900 (incentive) |  |
| Q1 Budget | 24,000 | 23,000 (incentive) |  |
| Q2 Budget | 24,000 + 3283 | 26,783(incentive) |  |
| Q3 Budget | 6000 | 6000(incentive) |  |
| Q4 Budget | 7500(L2) |  |  |
| BOE |  | 1,136 |  |
| Total | **85,038** | **75,819** | **9,264(L1+L2)** |

## Q4 2023: What did we do?

## output link: 

[L2 Economics Reporting](https://docs.google.com/spreadsheets/d/1dTV7H5ipGQWVrBd58S98_2mFtKcHfHqZ9g2BuvZcjxI/edit#gid=1575782868)

## Details

### Research: Suah, Praveen, Ethan

**Motivation**

- Define a path for TON Governance
- Research the two-step withdrawal flow in new optimism bedrock and understand the changes needed in our FW bridge

**Goals**

- Write the Governance Article series, and discuss the possible paths for progressive decentralization of TON Governance
- Finish Slides for Design possibilities of Tokamak DAO

**Progress**

October

- Analysis Simple Staking Patch Contracts ([doc](https://docs.google.com/presentation/d/1GTxvcRntM9rf62QaVIFxyAlMXCyqSoqJlx8keP5ZCPM/edit))
- Platform Research For Tokenomics Dashboard ([doc](https://docs.google.com/presentation/d/1hnTLbqJDKW957_WQ0CQB9WijAyXWSvXGHKY3Hzf4wQU/edit#slide=id.g292259f6bcf_0_25))
- Published Governance in Curve and Uniswap Article ([Medium](https://medium.com/onther-tech/cross-chain-governance-part-ii-3c2cf95aa1c4))
- Seminar - Tokenomics Dashboard ([Link](https://docs.google.com/presentation/d/1wN-yg2ePAV_G6LJg_oi3_cvtgERM96PhRb-35CZFVOg/edit?usp=sharing))

November

- Research: All about Tokamak Network Token ([doc](https://docs.google.com/presentation/d/12vr7GLyDUjTuxw3mhuJMrlNDoZfx6jdQEVfKE4kxo7A/edit))
- Set up for Dune dashboard ([link](https://dune.com/tokamak-network) / [link](https://dune.com/projects/Tokamak-Network)) (e.g Dune spell, projects, data etc.)
- Seminar - Tokamak DAO Limitations and Scope of Improvement ([Link](https://docs.google.com/presentation/d/16x5zJGbjZL84SU_doiPhe-xw_cGMDJbCH9hSe4Efipc/edit?usp=sharing))
- Liquidity Measure (C1,C2,C3) Calculation ([Doc](https://docs.google.com/document/d/1IZrdh38hXWfuRGX-_fuhTCutU9YZlIZIF8KRuMcjJIQ/edit))

December

- Dune Tokenomics/Staking dashboard first draft ([link1](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard) / [link2](https://dune.com/tokamak-network/tokamak-network-staking-dashboard))
- Price Dashboard Storyboard ([Slides](https://docs.google.com/presentation/d/1jUfS2q3poHaNrjTxNam8LnzR9_o-4NatNi-hQQeOoP4/edit?usp=sharing))
- Policy Guidelines for DAO (WIP,40%) - ([doc](https://docs.google.com/document/d/1rRV7SY7yp10adgymcVlZpD4VvuS9xr1Mk7A32jpqoHs/edit?usp=sharing))
- TON total supply data collection ([github](https://github.com/tokamak-network/TON-total-supply))

### Contract: Zena, Harvey, Justin

**Motivation**

- Fix and maintain existing contract vulnerabilities
- Checking TON supply statistics

**Goals**

- Fix simple staking vulnerability
- Fix DAOContract vulnerability
- DAOVault bans the use of TON
-  Added view function to check ton supply amount

**Progress**

**October**

- Urgent simple staking vulnerability correction work ([doc](/999debb51cf94f3b993077890542e27e))
  - contract upgrade([doc](/ff9089ba2f2f4aaf82ae920605ec877e), [commit](https://github.com/tokamak-network/ton-staking-v2/tree/audit_v1)) 
  - make test script([commit](https://github.com/tokamak-network/ton-staking-v2/tree/migration_mainnet_zena)) 
  - internal audit ([doc](/a2a8c81f77a0405ea20abcf0f5398979#1dcacadf5eef4de9a5b003cb02e51be2), [commit1](https://github.com/tokamak-network/ton-staking-v2/commits/audit_v1), [commit2](https://github.com/tokamak-network/ton-staking-v2/commits/audit_v1_harvey), [commit3](https://github.com/tokamak-network/ton-staking-v2/commits/audit_v1_justin)) 
  - migration test([commits](https://github.com/tokamak-network/ton-staking-v2/commit/0885afb3e1b44f5e01d9c637c2c228fd250dfeb4), [transactions](https://goerli.etherscan.io/tx/0xbd047ce4db69ae5da065ff6b36be6c566095cf5a6b7ec3a4595d02c044a73fa1)) 
  - migration simulation on mainnet([simulation3](/ad11bf335ae545a9a2b85cccd6ba20e1), [simulation4](/ec9296afe8614380a432bb67f06fd04e), [commit](https://github.com/tokamak-network/ton-staking-v2/commits/migration_mainnet_2_zena))
  - contract deploy & migration([doc](/39f2dbfda73f45a3a24b66c21f557233), [commit](https://github.com/tokamak-network/ton-staking-v2/commits/deploy_mainnet)) 
  - make the script for deposit test ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/migration_scripts))
  - test the changed simple Staking (doc)
  - make the check script (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/migration_scripts))
  - develop & test the migration script (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/migration_mainnet_2_zena))

**November**

- Develop the DAO Contract
  - Upgrade DAO contract to prevent TON held by DaoVault from being transferred elsewhere ([doc](/94e44d7876234c2da9fe303cb0770585), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/daoVault_agenda_check), [commits2](https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit))
  - request audit about Upgrade DAO Contract ([doc](/70a79bed70f645f5946e06e17e70ef8e))
- Working with TON supply    
  - change the total supply of SeigManager's increaseTot() function ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/dev_fix_total_supply)) 
- deploy contracts on Test-net  
  - deploy ton, wton, powerTON, simple staking patch contracts  on holesky (doc1, doc2, doc3 )

**December**

- apply the upgraded DAO Contract
  - update audit feedback about DAO ([doc](/70a79bed70f645f5946e06e17e70ef8e), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit))
  - deploy the DAOCommitteeDAOVault (doc)
  - deploy the DAOCommitteeOwner (doc)
- fix the DAO Contract vulnerability
  - fix the DAOLogic ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/))
- deploy contracts on Test-net  
  - deploy ton, wton, powerTON, simple staking patch contracts  on sepolia (doc1, doc2, doc3)
- develop contracts for L2 
  - develop/test the staked ton register  from L1 to L2:  L1StakedTONToL2 (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/register-stakedTon-to-l2) , doc1, doc2, doc3, doc4 , [commits](https://github.com/tokamak-network/ton-staking-v2/commits/register-stakedTon-index-snapshot/))
  - develop the powerton's ton distribute to l2  ([doc](/f02391b9f5824526af8bf1f5765e2d78), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/distribute-l2-powerTon/) )
- Working with TON supply statistics  
  - summary of 1.3 seigniorage distribution method ( [doc](/37755af987954a73925c23a8da7a2c73) ) 
  - Factor review of total staked amount (including segs) [doc](/a79c766c980a48a1b87c4c3591b54e58)
  - upgrade seigManager ( relate to totalSupplyOfTon, uncomittedStakeOf, CommitLog1 event ) :[doc](/d2f1088d60fa48d6b197ec945e10896f), [goerli deploy](/ed8b81faec894492963868892118157e), [mainnet deploy](/264958871b704fb39c22d61f69a2d95e)
  - check the VestingSchedule (doc)
  - DAO Pause cleanup (doc)

### Service: Jason

**Motivation**

- Connect new contracts and services

**Goals**

- adopt new contract to our service
- implement additional components

**Progress**

**Oct**

- patching simple staking([commit](https://github.com/tokamak-network/simple-staking-v2/commit/ea302c87f037919e646a3899ad062764a8a5fde3))
- re-open staking service([link](https://simple.staking.tokamak.network/))
- implement subgraph for staking([commit](https://github.com/tokamak-network/staking-v1-subgraph/commit/273b4edda310e49f05b5e11c6539fb9b6a2d616a))

**Nov**

- open simple staking mobile version ([commit](https://github.com/tokamak-network/simple-staking-v2/commit/cee0e5af456a4839760f59c523c3961b67b23675))

**Dec**

- set dao to sepolia([link](https://sepolia.dao.tokamak.network/))
- set sepolia dao server([link](https://api-dev.tokamak.network/))
- implement new price dashboard

### Design: Monica

**Motivation**

- The current simple staking service is based on the old plasma evm L2 structure and we need to update it based on Titan on demand and Titan L2 service.

**Goals**

- design update UX/UI to upgrade the current simple staking page

**Progress**

October 

- updated storyboard for simple staking page that supports L2 registry + FW ([figma](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?type=design&node-id=1075-28485&mode=design&t=s8DBFRi370XVKZlx-4))

November

- updated storyboard for simple staking page that supports L2 registry + FW ([figma](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?type=design&node-id=1075-28485&mode=design&t=s8DBFRi370XVKZlx-4))

December

- no work done → will ask for support from Praveen in 2024 Q1

## Contribution to the Tokamak ecosystem

---

### 1. Governance

- The current governance model is designed when we don’t operate our L2. So we need a new governance model considering L2 environment. L2 economics team’s modeling team is researching it and it is one of the contribution points to the Tokamak ecosystem.

### 2. Re-check token distribution

- Because of Upbit, Token distribution is a very important part of Tokamak network. In this quarter l2 economics team checked again about token distribution and got the exact value of it.

### 3. Is our project fit for the grant program of Tokamak Network?

- I think L2 economics project is fit for the grant program. Staking service is our most successful service and it can derive many services from it. And services that we try to implement are necessary things for our ecosystem.

---

## Strengths and Weaknesses Analysis

---

### Strengths

- Did additional things than the original plan
  - In the Q3 report, our team set the three types of goals. But we did 7 types of tasks and finalized 3 types of tasks and 1 task is almost finalized 

### Weaknesses

- Project delay due to lack of resource
  - Though we did many more things than expected, we cannot proceed much things with our original plan. Because of testnet issue.

---

## Challenges Faced

---

**Project progress is affected by testnet**

- Due to the end of the service of Goerli, we have to reset testnet service to Sepolia. Because it takes time to open the test net, it is not possible to develop functions related to l2.

---

## Lessons Learned

---

| Team | Lessons |
| --- | --- |
| Modelling | In developing Tokamak's next-gen DAO, we discovered areas that needed improvement. One critical aspect was ensuring the accurate dissemination of our tokenomics data, achieved by utilizing the Dune Dashboard and updating our supply dashboard. We realized that for a DAO to gain community trust, transparent disclosure of tokenomics information is vital for its acceptance |
| Contract | This quarter, we performed contract upgrade and migration due to a zero-day vulnerability in Simple Staking.
Once again, I thought that we should conduct a more thorough inspection during contract development.
Accordingly, we introduced a procedure in which each individual must perform an internal audit involving the entire contract team after developing a contract.
In the future, we plan to conduct more thorough contract testing and internal auditing in contract development. |
| Service | When we try to re-open DAO. It's been a long time since it was developed, so it took a long time to figure out the existing code. |
| Design | We need L2 registry research to finish the storyboard. Especially, it would be good to look into Optimism’s superchain. |

---

## Q4 Roadmap

## Goals in Q1, 2024

### Staking V2 & FW

- **Motivation**
  - Open FW for TON on the new network 
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
    - Work with design team to create a storyboard:** ~ End of March**

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - Finalize renewal dashboard based on Dune
  - Finalize price dashboard
  - Finalize DAO mechanics (Policy Guideline/Rule Book, Overall Process Diagram)

### Setup services on test net & re-open DAO

- **Motivation**
  - Check that all functions are working correctly for DAO to reopen
- **Goals**
  - Check contract values and audit frontend
  - re-open DAO service

### Porting DAO to react

- **Motivation**
  - Before end of service of current hosting environment we have to porting current DAO to react
- **Goals**
  - implement react version of DAO
  - test it
  - open react version of DAO to public

## Detail task per each team

### Research

**Motivation**

- Offer next-generation DAO for Tokamak Network
- Improve the L2 registry to effectively communicate with the community
- Provide good FW service

**Goals**

- Finalize DAO mechanics (Policy Guideline/Rule Book, Overall Process Diagram)
- Finalize Dune dashboard
- Research and finalize FW logic model 
- Research L2 registry (like Optimism Superchain)
- Finalize [price dashboard](https://pricedashboard-v2.vercel.app/)

### Contract

**Motivation**

- Power TON should be claimed on L2 (New Titan Test-net) rather than L1 .
- L2 (New Titan Test-net) should support fast withdrawals. For this, we need to be able to use the staked ton of Simple Staking.

**Goals**

- develop contract to register the staking TON as L2 (New Titan)
- modify PowerTon contract to divide ton at New Titan
- develop simple staking upgrade logic to support fast withdraw at New Titan Test-net
- DAO vulnerability correction audit in progress
- mainnet DAO open support

### Service

**Motivation**

- Offer better environment for DAO user

**Goals**

- re-open DAO service
- finalize convert DAO to react

### Plan & Design

**Motivation**

- Current simple staking service is based on old plasma evm L2 structure and we need to update it based on Titan on demand and Titan L2 service.

**Goals**

- design update UX/UI to upgrade current simple staking page

## Budget Request

|  | request | approved | get |
| --- | --- | --- | --- |
| endowment | 20,300 |  |  |
| Q1 | 24,000 |  |  |
| Q2 | **24,000 + 3283** |  |  |
| Q3 | 8,000 |  |  |
| Q4 | 15,000 | 15,000 | 7,500 |
| Q1, 2024 | 27,000 |  |  |

- **Reason for change:** 
  - Previously, I set grants per person as 1,000 TON per month. because we don’t have too many things to do. but in this quarter(Q4, 2023) and next quarter(Q1, 2024) it seems much things to do. So, I set the grant per person as 1,500 TON per month.

## Changes

- Suhyeon will join for modeling FW.

## Comments from Tokamak Network

[[2024 Q1, Budget report_L2 Economics]]