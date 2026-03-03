## Motivation: <u>Why do we develop in this project?</u>

The Tokamak Network has announced plans to launch a layer 2 (L2) protocol based on Optimism in the second quarter of 2023. However, the current infrastructure, including Simple Staking, is not suitable for the L2 environment. Additionally, with competitors such as Arbitrum, Optimism, and Boba Network already in the market, merely creating a layer 2 platform may not be enough to attract users.

To overcome these challenges, Tokamak Layer2 Economics team will provide infrastructure for the Tokamak Network’s L2 environment. So, our team’s plan is to convert the current TON ecosystem to layer2 friendly such as Staking & DAO. 

## Goals: <u>What do we want to achieve with this project?</u>

- L2 Economics team’s current ultimate goals are implement & publish to public TON Staking V2 and DAO V2. 
- After achieving those goals we can make the following contributions:
  - Foster organic growth of the Tokamak Network
  - Enhance the user experience of the Tokamak Network
  - Reinforce the security of the Tokamak Network
  - Alleviate the capital inefficiency of staked TON
  - To support both v1 & v2 update TON seigniorage distribution model

# Expected vs Actual outputs

## Service maintenance

### What it is?

- Service maintenance task is for the service that served by Tokamak Network.
- Although Tokamak Network does not want to operate service directly, some of the services must operate by Tokamak Network Foundation.
- So, L2 Economics team make a task for operate those of services such as Staking, DAO and Price Dashboard.
- The scope of this task is reflect feedback from community, update UX/UI and migration.

### Result of Q1 compare with original plan

- **Price dashboard & Dune dashboard**
  - **goal:** publish to public
  - **progress:** 100%(achieved)
  - **details:**
    - **(Original Plan)**** **Finalize dune dashboard
    - Update price dashboard for continuously price update
    - **(Original Plan)**** **Connect dune dashboard with price dashboard(make a link)
    - **(Original Plan)**** **Dune dashboard weekly update
- **Re-open DAO **
  - **goal**: re-open DAO to public
  - **progress**: 95%
    - Before DAO re-opening, some of the contracts need to deployed.
    - But, due to high gas fee, contracts deployment was delayed about 3 weeks.
    - Currently, we deployed contracts, And did internal test about it.
    - Remained task is update UX/UI based on feedback.
    - After that, we can re-open DAO in Apr.
  - **details:**
    - **(Original Plan) **Remove duplicated functions that makes user confused(ex. vote related function in election page)
    - **(Original Plan) **fix terms(voter → staker)
    - **(Original Plan) **set server on Sepolia & open testnet service on Sepolia
    - **(Original Plan) **Remove candidate who are not satisfied minimum deposit(in Sepolia)
    - **(Original Plan) **Remove next & prev button when there is no content after / before current one.
- **Staking V1**
  - **goal:** no task
  - **progress:** additional task
  - **details:**
    - **(Additional Output) **add wton staking(pc, mobile)
    - **(Additional Output) **change button disable condition.(pc, mobile)
    - **(Additional Output) **re-open wallet tab(with restricted functionality)
    - **(Additional Output) **update warning text, if candidate does not stake minimum collateral (pc, mobile)
    - **(Additional Output) **integrate staking function(operators tab, staking tab) in mobile
- **Migrate DAO(optional)**
  - **goal:** 100%
  - **progress:** 40%
    - Vercel, which is used for hosting our services, notice that node 16 will not supported. After support for node 16 is end, we cannot update services which is implemented with node 16. So, we have to prepare for that situation.
    - But, there is lots of urgent task than this, we have to work on this task when there is remained resources in service team.
    - In this quarter, there are many task in staking v1 than we thought. So we could not focus on migration.
  - **details:**
    - **(Original Plan) **finalize to publish agenda page.
    - **(Original Plan) **connect server data with agenda page & get agenda related data from server.
    - **(Original Plan) **finalize agenda detail page
    - **(Original Plan) **connect contract function in election page

## Staking V2

### What it is?

- Staking V2 is for the next generation staking service of Tokamak Network
- Because Staking V1 is implemented when there is no L2 in Tokamak Network, Its background and concepts are fit for Plasma EVM environment.
- But, mainnet of Tokamak Network is based on rollups. So, we have to change our staking service fit for rollup environment.
- Staking V2 aims to give seigniorage to L2 Sequencer.

### Result of Q1 compare with original plan

- **goal:** 70% - total progress
  - Modify PowerTon contract to divide ton at New Titan
  - Develop simple staking upgrade logic to support fast withdraw at New Titan Test-net
  - Seminar about explain contract function for front-end
- **progress**: 60%
  - Contract implementation was almost done
  - Develop upgrade staking logic to support FW is pending. Because we gonna implement FW  in another way.
  - FW model which is use staked TON as FW liquidity will be implemented in the future.
- **details:**
  - **(Original Plan)**** **develop and test to provide seigniorage to the Layer 2 sequencer
  - **(Original Plan)**** **seigniorage simulation based on white paper

## FW

### What it is?

- This task is for support Fast Withdrawal to Tokamak Network
- In this quarter, our team research about new FW model which is adopt bidding model.

### Result of Q1 compare with original plan

- **goal:** 70% - total progress
  - Research and finalize FW logic model 
    - Core service improvement
      - Provide support to integrate Optimism Bedrock withdraw process to existing FW logic 
      - Finalize FW fee policies (based on time, amount, etc)
    - Vulnerability check + Optimization: 
      - Basic vulnerability checklist for L1↔L2 communication 
      - Vulnerability check for abusing FW
      - Operation efficiency check to reduce gas usage 
- **progress**: 40%
  - In the original plan, we consider FW & Staking V2 as same task, because original model was designed to use staked TON as FW liquidity
  - But in this quarter, we suggested new model that adopt bidding logic in FW
  - We consider this model is fit for Ethereum Academic Grants, because it contains several subjects that Ethereum Academic Grants is interested in.
  - But in production level, this model require high gas fee. So, we discussed about alternative model
  - So, we used unexpected time for discuss practical model.
  - And this task will be moved to Tokamak Bridge team.
- **details:**
  - **(Original Plan)**** **Research and develop about FW model
  - **(Additional Output)**** **FW improvement proposal (seminar),
  - **(Additional Output)**** **Seminar about FW settlement
  - **(Additional Output)**** **Ethereum Academic Grant Submission
  - **(Original Plan)**** **Set contract implementation environment
  - **(Original Plan)**** **Start to develop FW contract

## L2 Registry

### What it is?

- L2 Registry is for the On-demand L2 of Tokamak Network.
- It will provide UX/UI about functionality deploy & register L2 on Tokamak Network service

### Result of Q1 compare with original plan

- **goal:** 
  - Research competitors (Optimism Superchain, Arbitrum Orbit, [Celestia](https://celestia.org/)) + Make a list of features we want to include: **~ End of January**
  - Determine overall UX for L2 registry + check in with core team (require verification + restriction for registration): **~ End of February **
  - Work with design team to create a storyboard:** ~ End of March**
- **progress: **
  - Currently, we are working on the storyboard task.
  - This task is being carried out without a delay.
  - It will be separated into other project.
- **details:**
  - **(Original Plan)**** **L2 On Demand Storyboard
  - **(Original Plan)**** **L2 On Demand Stage wise Deployment
  - **(Original Plan) **Research on Rollup competitors
  - **(Original Plan) **Demo related testing different deployment services(Caldera & Arbitrum Orbit)

## DAO V2

### What it is?

- DAO V2 is for the next generation DAO service of Tokamak Network
- Current DAO is not fit for L2 environment. So, we have to change current DAO to L2 friendly.

### Result of Q1 compare with original plan

- **goal:** 40% - total progress
  - Finalize DAO mechanics (Policy Guideline/Rule Book, Overall Process Diagram)
- **progress**: 20%
  - Originally, our goal is focus on DAO policy.
  - But in the middle of Q1, we consider Tally for DAO
  - So, our actual output have changed compared to original plan
- **details:**
  - **(Original Plan)** 50% progress in Policy Guideline/Rule Book
  - **(Additional Output)**** **Set Tally contract on Sepolia
  - **(Additional Output)**** **Test Tally contract on Sepolia

## Actual Developments in Q1, 2024 (with links)

- In this quarter L2 Economics team will be working on 5 types of task

## Service maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - **Re-open DAO → 100% (90% achieved)**
    - re-open DAO to public
    - DAO related user guide on gitbook
    - **Reason:** because of the high gas fee. We cannot deploy contract. So, re-open is delayed
  - **Price dashboard & Dune dashboard → 100%(done)**
    - publish new price dashboard & dune dashboard to public
- **Progress**
  - **Staking:** update  expected seig formular - 100%
  - **Staking:** non-depoisted operator issue
    - update staking UI related with non-deposited operator([storyboard](https://www.figma.com/files/project/184786887/Team-project?fuid=1185093972752859396), [UI](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1705915313813089?thread_ts=1705887413.313179&cid=C0416F1TNE5), [commits](https://github.com/tokamak-network/simple-staking-v2/commit/3d8e75f90f854ef7bd0457dba9e5f3c9900be52b)) - 100%
    - solve non-deposited operator issue([link](https://drive.google.com/file/d/1EPmJxjGrA8YzL2JiVcCN3JJBGBz6qHo7/view)) - 100%
  - **Staking**: re-open wallet page with restricted functionality([commit](https://github.com/tokamak-network/simple-staking-v2/commit/732d136f038750f8fc07a99d31186f6b2a555237)) - 100%
  - **Price Dashboard**
    - update link to dune dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/b7ba6ff75c36166f8048b7d8658f07c62b5cce4b)) - 100%
    - Dune Dashboard weekly update - 100%
    - Dune Dashboard mobile view update - 100%
  - **DAO**
    - modify DAO logic to strengthening DAO Committee qualifications through checking minimum collateral ([doc](/607fc9970b5f48d6ba7dd0fc21764809), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/)) - 100%
    - prepare deployment of DAOCommitte_V1, SeigManagerV1_2 on mainnet and reopen DAO  ([doc](/b77464f38a7a4174a4173e6c5ae8dd59), [commits1](https://github.com/tokamak-network/ton-staking-v2/commits/SeigManagerV1_2/) ) - 100%
    - prepare DAO re-open ([design](/ae0da156b2f346658aff622c60ef25bf), [front](https://github.com/tokamak-network/dao.tokamak.network/commit/5cf07ce49654abd55d1d151eed7580643ad450fa)) - 100%

### FW (40%)

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - new FW model
    - **result:** seminar about it **(done)**
  - Deploy & test contract in new testnet  
    - **result:** will be seminar about contract function explanation for implement front-end **(not finished)**
- **Progress**
  - **FW Modeling**
    - FW modeling: [mechanism design](/328d03ce7b30420cadc99ba6e5c73e02)
    - FW modeling and Game theory seminar
    - Current FW model analysis (WIP): [slides](https://docs.google.com/presentation/d/1bcXhBlm5uboiUvcbDIT9PhbN0RzFAVphtxFnnwKatPg/edit#slide=id.p)
    - Work on FW storyboard design with Monica
    - Submit Ethereum Academic Grant proposal
  - **Contract**
    - Building and testing FW development environment (tokamak-titan-canyon) ([doc](/1ea7e4c6b31a43f5aa74c0dba8dae620))
- **Reason for the progress**
  - In the original plan, we consider FW & Staking V2 as same task. But it is not same task because Staking V2 is not for the FW, but for staking for on-demand L2 environment.
  - And, there are few argument about development direction for the FW, so contract implementation is little bit delay

### Staking V2 (60%)

- **Motivation**
  - Upgrade existing simple staking service to support registration and display of L2 reference chain (Titan, Thanos) information
- **Goals**
  - Seminar about research competitors
  - Determine overall UX for L2 registry and communicate with Core team
- **Progress**
  - **Contract**
    - develop contracts that manages the L2 TVL to provide seigniorage, (20% , [contract design](/20b2ca5fe08e4986959d890fb2fb1d82), [L2Registry](/f7f2a0f242fa4171b45434810d6a32f4)**, **[Operator](/c3ef429695944ab5a67a8eb8b3df97c2), [OperatorFactory](/8e0abb3092ff4348997c87b07b0f8391), ** **[commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/)** **)
    - develop and test to provide seigniorage to the Layer 2 sequencer with method1 ([doc](/bc37d271e54a4a53a4ba28c4137dcd07), [modifySeigManager](/f4cf189b490c4d1198a044119333d4e3), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/) ) 
  - **L2 Registry & Simple staking page **
    -  [Seminar_L2 On Demand Competitors](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit?usp=sharing)
    - Rollup Deployment Demo: Caldera ([Slides](https://docs.google.com/presentation/d/1AlV80kW2UxmcYQ6Sz1wNws9H2xP_3FG0tTm8YkPTjBs/edit?usp=sharing))
    - L2 On Demand Storyboard :[ Initial version](https://www.figma.com/file/PUXcCtb9O0w5DMqc8cBNQ3/L2On-demand-Rollup-Storyboard?type=design&node-id=0-1&mode=design)
    - Seignorage simulation based on current white paper ([spreadsheet](https://docs.google.com/spreadsheets/d/1GKi5zEhSSRLz07PtHotioeUdZlyPGBxnipBu5h9Q1qw/edit#gid=0))
- **Explanation of the progress**
  - Contract implementation for the staking v2 is almost done.
  - Some of the team members are working on L2 Registry storyboard now.

### Tokamak DAO V2 (20%)

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - Finalize DAO mechanics (Policy Guideline/Rule Book, Overall Process Diagram)
    - **target overall progress:** 40%
    - **result:** seminar
- **Progress**
  - **Model**
    - DAO Policy guidelines ([link](https://docs.google.com/document/d/1rRV7SY7yp10adgymcVlZpD4VvuS9xr1Mk7A32jpqoHs/edit?usp=sharing)) - 50%
    - DAO Stage Seminar([link](https://docs.google.com/presentation/d/1hEiqnHllf6CgVKgWoT-D1Qa-DD1KImKwsP-hjIN5G0o/edit#slide=id.g2ada51891fe_0_15)) - 100%
  - **Contract**
    - research & deploy the Contract about Tally use Token on Sepolia ([doc](/17fb45703ea549adbd9c9b58513f64e7), [commits](https://github.com/tokamak-network/tally-erc20/commits/main/)) - 100%
- **Reason for the progress**
  - We judged another task is urgent than this task. So resource for this task is used for **System management**
  - And we are more focused on testing Tally than DAO policy guideline.

### Migrate DAO to react (40%)

- **Motivation**
  - Current package version will not be supported in Vercel. So before cannot update DAO, we have to migrate it.
- **Goals**
  - Porting DAO to react** (optional) → 100% (40% achieved)**
- **Progress**
  - Update election page([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/b9d4a5c53fdf96ec915b91d98bdc104427124ee4))
  - Agenda detail page([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/2e7396782dd4f428073bd37add699a237976c377))
- **Reason for the progress**
  - There are many things to do for service management task than original plan, so resource for migrate DAO 

## Member change

| Q2 | Jason | Suah | Praveen | Zena | Harvey | Justin | Ale | Ryan | Monica |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q3 | Jason | Suah | Praveen | Zena | Harvey |  |  |  |  |
| Q4 | Jason | Suah | Praveen | Zena | Harvey | Ryan | Monica |  |  |
| Q1, 2024 | Jason | Suah | Praveen | Suhyeon | Zena | Harvey | Justin | Ethan | Monica |
| Q2, 2024 | Jason | Suah | Praveen | Zena | Harvey | Ethan | Monica | Lucas |  |

- FW task will be implemented in P13, So Suhyeon will be participate in P13

## Budget Usage in Q2

|  | Income (TONs) | Outcome (TONs) | Total |
| --- | --- | --- | --- |
| Initial endowment | 20,300 | 18,900 (incentive) |  |
| Q1 Budget | 24,000 | 23,000 (incentive) |  |
| Q2 Budget | 24,000 + 3,283 | 26,783(incentive) |  |
| Q3 Budget | 6,000 | 6,000(incentive) |  |
| Q4 Budget | 15,000 | 14,500(incentive) |  |
| Q1 Budget | 13,000 |  |  |
| BOE |  | 1,136 |  |
| Total | 105,583 | 90,319 | **15,264(L1+L2)** |

## Q1 2024: What did we do?

## output link: 

[L2 Economics Reporting](https://docs.google.com/spreadsheets/d/1dTV7H5ipGQWVrBd58S98_2mFtKcHfHqZ9g2BuvZcjxI/edit#gid=1428995050)

## Details

### Model: Suah, Praveen, Suhyeon, Ethan

**Motivation**

- provide model support for other teammates to build the service

**Goals**

- determine DAO dev direction
- work on economics for staking 
- work on economics for FW

**Progress**

**January**

- updated TON supply sheet 
- worked on storyboard for simple staking and DAO
- L2 On-Demand Competitor Research ([Slides](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit?usp=sharing))
- Staking Page community feedback based storyboard update ([figma](https://www.figma.com/files/project/184786887/Team-project?fuid=1185093972752859396))
- [L2 Registry Research (25%)](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit?usp=sharing)
- Dune Update based on comment([Link](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard))
- FW modeling and analysis ([link](https://docs.google.com/presentation/d/1LWuEAHuN8F6pNguYcS6l3317WAnbTLAE/edit?usp=drive_link&ouid=112080929623748634135&rtpof=true&sd=true))
- Provided support launching new supply [dashboard](https://price.tokamak.network/#/)
- DAO[ Rule Book](https://docs.google.com/document/d/1rRV7SY7yp10adgymcVlZpD4VvuS9xr1Mk7A32jpqoHs/edit?usp=sharing)(50%)
- Apply Dune dashboard feedback([link](/d5be8b8e3e9a43cbb888fe74244e119f))

**February**

- simple staking UI [update](https://www.figma.com/file/mjiyy4ImRFKlH8rzEtXN0h/2024.1.22-Simple-Staking-Page-Update?type=design&node-id=0-1&mode=design&t=F6aHZpXE3HIERueh-0)  
- [Seminar_L2 On Demand Competitors](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit?usp=sharing)
- FW modeling: [mechanism design](/328d03ce7b30420cadc99ba6e5c73e02) 
- FW manuscript writing (draft) (30%)
- FW modeling and Game theory seminar ([slides](https://docs.google.com/presentation/d/1Xt5MJTSPVMflmgzx9vr4DmO8620wLbqC/edit?usp=drive_link&ouid=112080929623748634135&rtpof=true&sd=true))
- FW PoC: Optimism Bedrock env. setting (50%) 
- Demo:Caldera Deployment Service([Slides](https://docs.google.com/presentation/d/1AlV80kW2UxmcYQ6Sz1wNws9H2xP_3FG0tTm8YkPTjBs/edit?usp=sharing))
- FW analysis and improvement proposal ([slides](https://docs.google.com/presentation/d/1bcXhBlm5uboiUvcbDIT9PhbN0RzFAVphtxFnnwKatPg/edit#slide=id.p))
- Gave feedback for L2 On-Demand Rollup Storyboard([Link](https://drive.google.com/file/d/1w4h6P-I8uz1IiVSkiBCEOGN6Y1v5xr4F/view?usp=sharing)) 
- Seignorage simulation based on white paper ([spreadsheet](https://docs.google.com/spreadsheets/d/1GKi5zEhSSRLz07PtHotioeUdZlyPGBxnipBu5h9Q1qw/edit#gid=0))

**March**

- L2 settlement scheme ([slides](https://docs.google.com/presentation/d/1bcXhBlm5uboiUvcbDIT9PhbN0RzFAVphtxFnnwKatPg/edit#slide=id.g2bb7d141c9d_1_10)) 
- Ethereum Academic grant submission ([doc](https://drive.google.com/file/d/1ALoETYMU27szQHt_zHv9tPf3fdh6mP-h/view?usp=drive_link))
- L2 On Demand Storyboard v2 ([Slides](https://docs.google.com/presentation/d/1Ptv6xJVLbwwW8EraRIOyAwR-zljR1yzgsF186upjcAw/edit?usp=sharing)) (20%) 

### Contract: Zena, Harvey

**Motivation**

- To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2

**Goals**

- Staking service maintenance
- DAO service re-open
- Develop contracts to provide seigniorage to the Layer 2 sequencer  

**Progress**

**January**

- test the updateSeigniorage after 1000.1 TON deposit of operator on Talken layer( [doc](/7c8574f75cf34bb080def5d2d79c3603), [commits](https://github.com/tokamak-network/ton-staking-v2/commit/2aa0af191c312f27e5fc2957d018b26c037267e1#diff-eff1dca66cb32c9b6709469dd96275815b4b76d07c8ae71b9a1b0681fe215612) ) 
- research the Contract about Tally use Token on Sepolia ([commits](https://github.com/tokamak-network/tally-erc20/commits/main/))
- prepare Deploy the DAOCommitte_V1 (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/))
- develop L2PowerTon (contract calling L2DividendPoolForStos's distribute function to dividend the deposited token from L1) [doc](/b0e3e3f4e1e74af9bc0986840da0e548), [commits](https://github.com/tokamak-network/l2-project-launch/commits/NT_4_L2PowerTon/)   
- DAO test on Sepolia ([doc](/7fb6a7ba69074bae99a9f60985db3509))
- did audit of DAO (doc)  
- apply the feedback for audit ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/)) 
- summary of registering stakingTon to L2 ([doc](/3d53af8d83bb490085bafd18b3a15157))
- request the Audit for DAO fix logic (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/))
-  test the dao web on sepolia ([doc](/96240df7f1df471292edcff8b6dda7c2))

**February**

- modify simple stake to check operator's minimum collateral when stake. ( [doc](/607fc9970b5f48d6ba7dd0fc21764809), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/SeigManagerV1_2/) ) 
- modify DAO logic to strengthening DAO Committee qualifications through checking minimum collateral ([doc](/607fc9970b5f48d6ba7dd0fc21764809), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/))
- develop contracts that manages the L2 TVLto provide seigniorage, (20% ,[contract design](/20b2ca5fe08e4986959d890fb2fb1d82),[L2Registry](/f7f2a0f242fa4171b45434810d6a32f4)**,**[Operator](/c3ef429695944ab5a67a8eb8b3df97c2),[OperatorFactory](/8e0abb3092ff4348997c87b07b0f8391),[commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/))
- Building and testing FW development environment (tokamak-titan-canyon) ([doc](/1ea7e4c6b31a43f5aa74c0dba8dae620))
- deploy DAOCommitte_V1, SeigManagerV1_2 on mainnet and reopen DAO  ([doc](/b77464f38a7a4174a4173e6c5ae8dd59),[commits1](https://github.com/tokamak-network/ton-staking-v2/commits/SeigManagerV1_2/))
- research & deploy the Contract about Tally use Token on Sepolia ([doc](/17fb45703ea549adbd9c9b58513f64e7), [commits](https://github.com/tokamak-network/tally-erc20/commits/main/))

**March**

- develop Layer2Candidate, Layer2Manager to support simple staking services to on-demand L2 and Titan, Thanos  ([Layer2Manager](/bc37d271e54a4a53a4ba28c4137dcd07), [Layer2Candidate](/fb1c29d9bd7545e890becb9cd8196e9b), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/))
- make the Document about Summary of parts executed in DAO ([doc](/3844cf2b3d0e406d9a3f8be2aa42ed61))
- develop and test to provide seigniorage to the Layer 2 sequencer with method1 ([doc](/bc37d271e54a4a53a4ba28c4137dcd07), [modifySeigManager](/f4cf189b490c4d1198a044119333d4e3), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/) ) 
- develop the FWContract ([doc](/277d3430557941a1af858234f780e767), [commits](https://github.com/tokamak-network/tokamak-titan-canyon/commits/develop-FWContract/))

### Service: Jason

**Motivation**

- Offer better environment for DAO user
- Service management & update

**Goals**

- re-open DAO service
- Maintain services of Tokamak Network’

**Progress**

**January**

- update for no staking reward operator([commit](https://github.com/tokamak-network/simple-staking-v2/commit/3d8e75f90f854ef7bd0457dba9e5f3c9900be52b))
- update simple staking mobile & pc version([commit](https://github.com/tokamak-network/simple-staking-v2/commit/ddb98d482fa49e677400d77f81639676002cddd3))
- price dashboard update([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/1ef64fa412be97fc6cc86d0ced56c9ab4db415d6))
- reflect dao feedback([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/a7d2070c3729ed1c4a557451b469fc8a499904ca))
- implement price dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/344abde00dcb9da3511ccfb3da379c3b2b7b3e16))
- publish dashboard([link](https://price.tokamak.network/))

**February**

- set DAO on mainnet(not public) ([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/45beb3c96ef4bdf83112e5d85e5697e1e2916834))
- update staking([commit](https://github.com/tokamak-network/simple-staking-v2/commit/4df24355aaba640c5937b8c72bfeefb7ef5c6846))
- set wallet page in staking ([commit](https://github.com/tokamak-network/simple-staking-v2/commit/732d136f038750f8fc07a99d31186f6b2a555237))
- update for dao re-open([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/5cf07ce49654abd55d1d151eed7580643ad450fa))

**March**

- fix withdraw bug([commit](https://github.com/tokamak-network/simple-staking-v2/commit/ed6674ed6ff8220a1f3c5be89f499aadd6ff26a8))
- fix dao interface([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/09d9a32c482e90ce0b41c4376dad8903b3bbd1e5))
- migrate dao to react([commit](https://github.com/tokamak-network/simple-staking-v2/commit/ed6674ed6ff8220a1f3c5be89f499aadd6ff26a8))

### Design: Lucas, Monica

**Motivation**

- Current simple staking service is based on old plasma evm L2 structure and we need to update it based on Titan on demand and Titan L2 service.

**Goals**

- design update UX/UI to upgrade current simple staking page

**Progress**

**January**

- Simple staking UI update ([Desktop](/468f5805a332473d96412b5cc5bffc53))
- Simple staking page UI [update](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1705915313813089?thread_ts=1705887413.313179&cid=C0416F1TNE5) / [mobile](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1705979052885659?thread_ts=1705887413.313179&cid=C0416F1TNE5) / [Reflect additions](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1705983753655989?thread_ts=1705887413.313179&cid=C0416F1TNE5)

**February**

- Simple staking UI update ([Desktop](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1707267152171089?thread_ts=1707105885.396839&cid=C0416F1TNE5) & [Mobile](/468f5805a332473d96412b5cc5bffc53))
- Update storyboard(-)
- Thanos BI [design](https://docs.google.com/presentation/d/1-NLA9Uqg6zj_7S-BjndagivZ5V87fQuVKNzH15z48j0/edit#slide=id.gc29d83f0ba_0_710)
- simple staking footer copyright [updated](https://tokamak-network.slack.com/archives/C9Y5915B7/p1708939084296619?thread_ts=1708917169.256729&cid=C9Y5915B7)
- DAO page reopening design [update](/ae0da156b2f346658aff622c60ef25bf)

**March**

- Thanos BI [design](https://docs.google.com/presentation/d/1-NLA9Uqg6zj_7S-BjndagivZ5V87fQuVKNzH15z48j0/edit#slide=id.gc29d83f0ba_0_710)

## Contribution to the Tokamak ecosystem

---

### 1. FW Modeling

- Suhyeon submit his FW model to Ethereum Academic Grants program. If it selected by Ethereum Academic Grants, it will be greate contribution to Tokamak ecosystem

### 2. UX Improvement

- In this quarter, L2 economics team update UX of simple staking & DAO. In the past system, there are lots of repeated functionality. And it make user confused. So, to solve that issue, we updated our services.

---

## Strengths and Weaknesses Analysis

---

### Strengths

- The FW proposed in our project this quarter is a method that other projects have not tried. So we applied to Ethereum Academic Grants because our model was judged to have academic value.


### Weaknesses

- In this quarter, 2 types of FW models were suggested. So we discussed both models. We thought implementing both was a good idea but had to choose one because of a lack of resources.


---

## Challenges Faced

---

**High Gas Fee**

- Due to expensive gas fee, contract deployment was delayed about 2 weeks. And DAO re-open was also delayed.
- So, we have to consider put more effort into gas optimization in contract development

**Consideration of the FW model**

- In this quarter, 2 types of FW models were suggested. So we discussed both models. We thought implementing both was a good idea but had to choose one because of a lack of resources.
- Although, it affects to our roadmap and timeline, this conversation was so meaningful. Because it gave us several options about FW

---

## Lessons Learned

---

| Team | Lessons |
| --- | --- |
| Modelling | Decentralized actions require more computations than non-decentralized actions. Sometimes to make an application economically viable, certain compromises need to be made. |
| Contract | When distributing a contract, it requires a lot of gas, which is a burden. I thought that more effort should be put into gas optimization in contract development.

As there are many things that need to be updated in DAO this quarter, what I have come to realize is that contracts should be developed as proxy, and among proxy, a version that can implement multiple contracts should be developed so that future development can be much more convenient. |
| Service | I found out that even if the service was previously well operated, there may be inconvenience from the user's point of view. I thought I should consider this part more |
| Design | Even if the service development at the project level was completed, I thought more effort and attention should be paid to respond to changes in the system environment or to improve usability. |

---

## Goals in Q2, 2024

### Staking V2 → 90%

- **Members: Zena, Jason, Monica, Suah **
- **Motivation**
  - Seigniorage economics for L2 operators of Titan, Thanos and on-demand L2 is needed
- **Explanation**
  - Ultimate goal of Staking V2 is consist of 2 parts
    - **Staking V2** →  Staking V1 distribute seigniorage to only candidates. After staking v2 is developed, we can provide to seigniorage to L2 sequencer(like Sequencer of Titan).
    - **Provide FW seigniorage by using staked TON** → Tokamak Network will provide maximum 3 types of FW, one of them will be implemented in Bridge team, second one is submmitted as Ethereum Academic Grants. And last one is provide FW liquidity by using staked TON in staking service. This feature will be implemented after Staking V2 is open.
    - In Q2, 2024, L2 Economics team focus on open Staking V2 in testnet
- **Goals**
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the thanos-sepolia-test
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **Expected result**
  - Internal audit & contract test
  - Open staking v2 page on sepolia

### FW (work moved to P13 Tokamak Bridge)

- **Goals**
  - Staked TON based FW **will not be** **developed** during Q2.
    - Non staked TON based FW will be conducted in P13 Tokamak Bridge contract 

### Tokamak DAO V2 → 40%

- **Members:** Jason, Harvey, Zena, Suah, Praveen
- **Motivation**
  - DAO is important part of Tokamak Network, we want to see how we can effectively communicate with the community by building our next DAO
- **Explanation**
  - This task is for next generation of Tokamak DAO. 
  - Currently, we focus on check compatibility with Tally which is provide interface for DAO.
  - And, we also focus on writing new DAO policy.
- **Goals**
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend) 
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (model) Finalize Tokamak DAO Policy/ Guidelines
- **Expected result**
  - Set Tokamak DAO on sepolia Tally

### Porting DAO to react(optional) → 95%

- **Motivation**
  - Before end of service of current hosting environment we have to porting current DAO to react
- **Goals**
  - migrate DAO to react
  - open react version of DAO to public
- **Expected result**
  - Migrate react version of DAO on sepolia

## Detail task per each team

### Model

**Motivation**

- Prepare FW & staking v2 service before Thanos opens
- Tally Testing for Tokamak DAO and finalize policy/guidelines

**Goals**

- Work on improving FW scheme and implement PoC and service
- Work on staking v2 service policies and 
- Test tally interface on Sepolia with all features and figure out how to make use of Tally for Tokamak DAO functioning
- Finish writing the policy/guidelines for Tokamak DAO 

### Contract

**Motivation**

- we should provide seigniorages to the sequencer of Titan, Thanos and on-demand L2. 

**Goals**

- gas optimization and refactoring contracts to provide seigniorage to the sequencer of Titan, Thanos and on-demand L2. 
- do audit the contracts to provide seigniorage to the L2 sequencer 
- create Titan and Thanos Candidate on the simple staking contracts of the thanos-sepolia-test.

### Service

**Motivation**

- To provide FW service to user of Tokamak network

**Goals**

- implement Staking V2 front-end
- implement Staking V2 subgraph
- migrate DAO to react

### Plan & Design

**Motivation**

- Current simple staking service is based on old plasma evm L2 structure and we need to update it based on Titan on demand and Titan L2 service.

**Goals**

- make storyboard and design for staking v2 to upgrade current simple staking page

## Budget Request

|  | request | approved | get |
| --- | --- | --- | --- |
| endowment | 20,300 |  |  |
| Q1 | 24,000 |  |  |
| Q2 | **24,000 + 3283** |  |  |
| Q3 | 8,000 |  |  |
| Q4 | 15,000 | 15,000 |  |
| Q1, 2024 | 33,000 | 26,000 | 13,000 |
| Q2, 2024 | 21,000 |  |  |

## Changes

- FW task will be moved to P13. Because all of the UX/UI related with FW will be served at bridge.
- L2 Registry will submit another grants and seperated from this project

## Comments from Tokamak Network

- 전체적인 goal 에 한 그림이 부족
- 교훈을 바탕으로한 개선점, 그와 관련된 고민이 부족
- 투자 계획서 작성하듯 일반 대중에게 설명할 수 있기에는 너무 테크니컬함, 조금 더 일반적인 설명이 필요
- 체크리스트 바탕으로한 템플릿 제공 예정