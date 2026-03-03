# Goals

- Staking & DAO are the most successful services of Tokamak Network. However, it is not fit for the L2 environment.
- The ultimate goals of Project Eco are to implement & publish to the public TON Staking V2 and DAO V2, which can support & fit the L2 environment.
- After the implementation of Staking V2 is finished, we can provide seigniorage to the L2 sequencer and FW liquidity based on staked TON. When the implementation of DAO V2 is finished, we can provide improved DAO governance that fits the L2 environment.

# Output Overview

# Expected vs Actual outputs

## Service maintenance

### What is it?

- The service maintenance task is for the service that is served by Tokamak Network.
- Although Tokamak Network does not want to operate the service directly, some of the services must be operated by Tokamak Network Foundation.
- So, the L2 Economics team has a task to operate of services such as Staking, DAO, and Price Dashboard.
- The scope of this task is to reflect feedback from the community, update UX/UI, and migration.

### Result of Q1 compared with original plan

- **Price dashboard & Dune dashboard**
  - **goal:** no task
  - **progress:** additional task
  - **details:**
    - **(Additional Output) **upload price-api docker image to a new account
    - **(Additional Output) **make task definition for a collector in ECS
    - **(Additional Output) **make task definition for API in ECS
    - **(Additional Output) **make ECS cluster to a new account
    - **(Additional Output) **make load balancer & target group for ECS
    - **(Additional Output) **assign DNS to new service
- **Staking V1**
  - **goal:** no task
  - **progress:** additional task
  - **details:**
- **DAO V1**
  - **goal:** no task
  - **progress:** additional task
  - **details:**
    - **(Additional Output) **migrate DB for sepolia & mainnet to a new account
    - **(Additional Output) **upload docker image for sepolia & mainnet to a new account
    - **(Additional Output) **make task definition about collector for sepolia & mainnet to a new account
    - **(Additional Output) **make task definition about API for sepolia & mainnet to a new account
    - **(Additional Output) **make ECS cluster for sepolia & mainnet to a new account
    - **(Additional Output) **make load balancer & target group for ECS
    - **(Additional Output) **assign DNS for sepolia & mainnet to new service
- **Migrate DAO(optional)**
  - **goal:** 90%
  - **progress:** 80%
    - Vercel, which is used for hosting our services, notice that node 16 will not supported. After support for node 16 is end, we cannot update services which is implemented with node 16. So, we have to prepare for that situation.
    - But, there are lots of urgent tasks than this, and we have to work on this task when there are remaining resources in the service team.
  - **details:**
    - **(Original Plan) **finalize to publish the agenda page.
    - **(Original Plan) **connect server data with the agenda page & get agenda-related data from the server.
    - **(Original Plan) **finalize agenda detail page
    - **(Original Plan) **connect contract function in the election page
    - **(Under Achieved)** Internal test

## Staking V2

### What is it?

- Staking V2 is for the next-generation staking service of Tokamak Network
- Because Staking V1 is implemented when there is no L2 in Tokamak Network, Its background and concepts fit the Plasma EVM environment.
- But, mainnet of Tokamak Network is based on rollups. So, we have to change our staking service fit for rollup environment.
- Staking V2 aims to give seigniorage to L2 Sequencer.

### Result of Q1 compared with original plan

- **goal:** 90% - total progress
  - (service) Update UX/UI simple staking page  / Implement subgraph for staking v2
  - (contract) Create Titan and Thanos candidates on the simple staking contracts of the thanos-sepolia-test
  - (contract) internal audit
  - (design) Finalize storyboard and design for staking V2
- **progress**: 85%
  - Design UX/UI simple staking page is done. Implementing UX/UI is in progress.
  - Creating Titan and Thanos candidates on the simple staking contracts of the thanos-sepolia-test is done
  - An internal audit is done. And we are refactoring the contract for gas optimization.
  - **Reason**
    - Because of AWS resource migration. There are some delays in implementing UX/UI of simple staking v2
    - We have no plan when some of the sequencers have a problem. Based on the current white paper, we have to issue seigniorage to sequencers even if they are doing wrong. So, we spend time implementing stop-issue functions
- **details:**
  - **(contract) Create Titan and Thanos candidates on the simple staking contracts of the thanos-sepolia-test**
    - **(Original Plan)**** **develop and test to provide seigniorage to the Layer 2 sequencer** **doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/)
    - **(Original Plan)**** **seigniorage simulation based on white paper and finished verify staking v2 update [seigniorage logic](https://docs.google.com/spreadsheets/d/1khbkDRD_ATWYKdmOfOJBUngxtAMp-JRDDMvFrF-AFbk/edit#gid=0)
    - **(Original Plan) **Simple Staking V2 [withdraw modal](https://zpl.io/WQK50r7) UX/UI Update
    - **(Original Plan) **test titan-sepolia candidate on sepolia simple staking (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/deploy_sepolia_v2/)) 
    - **(Original Plan) **upgrade & test DAO Contract for DAO Structure & Layer2Candidate (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/NewDAOStructure/)) (doc, [commits](https://github.com/tokamak-network/ton-staking-v2/commits/NewDAOStructure/))
    - **(Original Plan) **deploy and setting DAOCommitteeProxy2 & DAOCommittee_V1 & DAOCommitteeOwner on sepolia ([#2](https://github.com/tokamak-network/ton-staking-v2/issues/2) ,[commits](https://github.com/tokamak-network/ton-staking-v2/commits/NewDAOStructure/), doc, [doc2](/cd40a176ef624b4a8c73c90b72afa69b))
    - **(Additional Output) **define the process for stopping seigniorage issuance to Layer2Candidate (doc)
    - **(Additional Output) **Develop/test/deploy the function for stopping seigniorage issuance to Layer2Candidate on sepolia ([task #3](https://github.com/tokamak-network/ton-staking-v2/issues/3))
  - **(contract) internal audit**
    - **(Original Plan) **Audit about Layer2Candidate (doc) & Reflecting audit content in code([#8](https://github.com/tokamak-network/ton-staking-v2/issues/8), [#9](https://github.com/tokamak-network/ton-staking-v2/issues/9) [#10](https://github.com/tokamak-network/ton-staking-v2/issues/10), [#11](https://github.com/tokamak-network/ton-staking-v2/issues/11))
  - **Design UX/UI simple staking page is done. Implementing UX/UI is in progress.**
    - **(Original Plan) **Simple Staking V2 [withdraw modal](https://zpl.io/WQK50r7) UX/UI Update
  - **(service) Update UX/UI simple staking page  / Implement subgraph for staking v2**
    - **(Under Achieved)** Implement UX/UI Staking V2 page (not finished)
  - **(Additional Output) **worked on [user guide ](https://docs.tokamak.network/)

## DAO V2

### What is it?

- DAO V2 is for the next-generation DAO service of Tokamak Network
- The current DAO is not fit for the L2 environment. So, we have to change the current DAO to L2 friendly.

### Result of Q1 compared with original plan

- **goal:** 40% - total progress
  - (model) Finalize Tokamak DAO Policy/ Guidelines
  - (model + contract) Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - (service, contract) Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend)
- **progress (5 %)**: 
  - Seminar Prep: Lifecycle of DAO Proposal 
    - This seminar aims to explain the lifecycle of a DAO proposal based on the [rule book](https://docs.google.com/document/d/1ZJGOCvMno9bGk8xah8ug5bFX4MOjY4RausDpIXCgTzM/edit?usp=sharing) we defined for new DAO 
  - **(Under Achieved)** Finalize Tokamak DAO Policy/ Guidelines
  - **(Under Achieved)** Tally testing + demo Setup new Tokamak DAO with features available in Tally, test proposal lifecycle end-to-end based on the policy/guidelines defined for the new DAO.
  - **(Under Achieved)** Check DAO functionality for the new contract (**test on Sepolia**, contract & frontend & backend)
  - **Reason**
    - The modeling team couldn’t spend time on Tally testing in Q2 since the team members got really busy with other projects. We expect to cover the defined goals in Q3.
- **details:**
  - The seminar slides based on the [rule book](https://docs.google.com/document/d/1ZJGOCvMno9bGk8xah8ug5bFX4MOjY4RausDpIXCgTzM/edit#heading=h.kf5n45qs0rn8) are currently being prepared and will be done by the end of June

# Outputs

[https://docs.google.com/spreadsheets/d/1dTV7H5ipGQWVrBd58S98_2mFtKcHfHqZ9g2BuvZcjxI/edit#gid=1276422944](https://docs.google.com/spreadsheets/d/1dTV7H5ipGQWVrBd58S98_2mFtKcHfHqZ9g2BuvZcjxI/edit#gid=1276422944)

# Challenges and Lessons Learned

## Challenges

- In this quarter, we had problems with a lack of resources. Because our modeling team members are too busy for other tasks. It affects our DAO V2 related task. So, there is less progress in DAO v2 tasks.                 

## To Prevent Similar Challenges

- We are considering checking progress based on goals. And find more people to participate in our project, especially the modeling part.
- Nowadays, there are many unexpected tasks. It affects project resources and goals. So, I think about something like reserve forces, but it is not realistic.
- So, we will check the project schedule more frequently. If there are too many delays, we will 1-on-1 meeting for it.

## Lessons Learned

| Team | Lessons |
| --- | --- |
| Model | Understanding current DAO trends and trying to modify our DAO seems to be very difficult. It is possible that our initial model for delegating staking power to the L2 Operator (that do not actually operate L2) was not a good model. 
We need to quickly transition from 3 person voting structure to an individual+delegate voting structure. |
| Contract | We are trying to make development suitable for an open project by making the contract development process and contents public.
So, we registered the work that needed to be done as an issue and started managing it in Git. We will work hard and learn to make the development process suitable for open projects. |
| Service | There are many common components In the DAO front-end. But, we were not concerned about it. So, it causes more delay when migrating DAO.
So, we have to be concerned about common components to prevent this situation. |
| Design | Constant effort and learning are required to respond to changes in the environment of blockchain, and attention and effort are required to develop systematic common components for efficient response. |

# Goals of Q3, 2024

### Staking V2 → 95%

- **Members: Zena, Jason, Suah, Lucas**
- **Motivation**
  - Seigniorage economics for L2 operators of Titan, Thanos, and on-demand L2 is needed
- **Goals**
  - (design) 
    - Assist service team with Staking v2 implementation
    - Update (stake/unstake/restake/withdraw) mobile design for staking v2 
  - (service) 
    - Open staking v2 on Sepolia testnet & Ethereum mainnet (desktop & mobile)
  - (contract) 
    - Create (L2 seigniorage related) documentation for code review & code audit
    - Deploy contract on mainnet
    - Discuss about **Seigniorage issuance restriction requirements(**[**link**](https://github.com/tokamak-network/ton-staking-v2/issues/14)**)**
  - (model) update white paper → before staking v2 is opened 
- **Expected result**
  - publish it to testnet(pc/mobile)

### Tokamak DAO V2 → 

- **Members:** Jason, Harvey, Zena, Suah, Praveen
- **Motivation**
  - DAO is an important part of Tokamak Network, we want to see how we can effectively communicate with the community by building our next DAO
- **Explanation**
  - This task is for the next generation of Tokamak DAO. 
  - Currently, we focus on checking compatibility with Tally which provides the interface for DAO.
  - And, we also focus on writing a new DAO policy.
- **Goals**
  - Look for additional members to contribute for DAO
  - [Consider FIT21 bill when designing DAO](/cdbdd12984884d99935b4a6d3bf42130)
  - Explore options to integrate Staked WTON to Tally Interface
  - Seminar on examples of DAO proposals with Specific use cases
  - Test the Tally interface for Arbitrum DAO to understand the key features
  - Expand the policy guideline to clearly define the DAO voting structure
  - Test the DAO in Sepolia with new voting structure and proposal guidelines
  - Build an MVP on Sepolia with proposed structure and guidelines
- **Expected result**
  - Seminar on DAO Proposal
  - Document defining integration of Staked WTON with Tally
  - Seminar on using Tally to interact with Arbitrum DAO
  - Build a test DAO in Sepolia with defined guidelines and rules 

### Porting DAO to react(optional) → 

- **Motivation**
  - Before the end of service of the current hosting environment, we have to migrate the current DAO to react
- **Goals**
  - Start to implement mobile + tablet version. If we can use Tally for DAO, this task will not proceed 
- **Expected result**
  - An internal test for the migrated version

# Budget request