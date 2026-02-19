# 1. Goals

- Staking & DAO are the most successful services of Tokamak Network. However, it is not fit for the L2 environment.
- The ultimate goals of Project Eco are to implement & publish to the public TON Staking V2 and DAO V2, which can support & fit the L2 environment.
- After the implementation of Staking V2 is finished, we can provide seigniorage to the L2 sequencer and FW liquidity based on staked TON. 
- When the implementation of DAO V2 is finished, we can provide improved DAO governance that fits the L2 environment.

# 2. Output Overview

## 2.1. Outputs of team

### 2.1.1 Service maintenance

| Goal | Migrate DAO to react & Open the react version of DAO to the public |
| --- | --- |
| Progress per goal | 80% |

- **Additional outputs**
  - **(DAO)** Aws server & DB migration for DAO collector & API (mainnet, testnet)
  - **(Price-API)** Aws server migration for Price collector & API
- **Explain the progress**
  - Migrate DAO to react in the PC version. But it needs a QA process.

### 2.1.2 Staking V2

| **Goal** | Create Titan and Thanos candidates  & test | internal audit | Finalize storyboard and design | Implement front-end & subgraph |
| --- | --- | --- | --- | --- |
| **Progress per goal** | 100% | 100% | 97% | 60% |

- **Additional outputs**
  - **(Contract)** define the process & develop for stopping seigniorage issuance to Layer2Candidate
  - **(Model)** worked on the user guide
- **Explain the progress**
  - There were urgent tasks in this quarter. So, It takes more time than expected. And, it affects the service team’s progress. 
  - We have a plan to give seigniorage to the L2 sequencer. However, we were not concerned about the sequencers who did not operate their L2 properly. So, we started research for it.

### 2.1.3 Tokamk DAO V2

| Goal | Finalize policy & guidelines | Tally testing based on the policy & guidelines | Check DAO functionality for the new contract |
| --- | --- | --- | --- |
| Progress per goal | 40% | 0% | 0% |

- **Explain the progress**
  - The modeling team couldn’t spend time on Tally testing in Q2 since the team members got really busy with other projects. We expect to cover the defined goals in Q3.

## 2.2 Outputs per person

<!-- Unsupported block type: unsupported -->

# 3. Challenges and Lessons Learned

## 3.1. Challenges

- In this quarter, we needed more resources. Because our modeling team members are too busy for other tasks. It affects our DAO V2 related task. So, there is less progress in DAO v2 tasks.

## 3.2. To Prevent Similar Challenges

- We are considering checking progress based on goals. And find more people to participate in our project, especially the modeling part.
- Nowadays, there are many unexpected tasks. It affects project resources and goals. So, I think about something like reserve forces, but it is not realistic.
- So, we will check the project schedule more frequently. If there are too many delays, we will 1-on-1 meeting for it.

## 3.3 Lessons Learned

| **Team** | **Lessons** |
| --- | --- |
| Model | Understanding current DAO trends and trying to modify our DAO seems to be very difficult. It is possible that our initial model for delegating staking power to the L2 Operator (that does not actually operate L2) was not a good model. 
We need to quickly transition from 3 person voting structure to an individual+delegate voting structure. |
| Contract | We are trying to make development suitable for an open project by making the contract development process and contents public.
So, we registered the work that needed to be done as an issue and started managing it in Git. We will work hard and learn to make the development process suitable for open projects. |
| Service | There are many common components In the DAO front-end. But, we were not concerned about it. So, it causes more delay when migrating DAO.
So, we have to be concerned about common components to prevent this situation. |
| Design | Constant effort and learning are required to respond to changes in the environment of blockchain, and attention and effort are required to develop systematic common components for efficient response. |

# 4. Goals of Q3, 2024

## 4.1. Service maintenance

- **Goals**
  - Start to implement mobile + tablet version.(If we can use Tally for DAO, this task will not proceed )
  - An internal test for the migrated version
- **Explanation for the outside**
  - This task is something like reserve. We have a plan to use Tally as our next generation of DAO. But, Tally may not be used. So, this task is intended to prepare for any contingency. And, if we can use Tally, this task will not proceed.

## 4.2. Staking V2

- **Goals**
  - deploy contracts on mainnet
  - Update white paper
  - publish it to testnet & mainnet(pc/mobile)
- **Explanation for the outside**
  - In Q3, we are planning to open Staking V2 on sepolia testnet. After this implementation is over. The layer2 sequencer also can get seigniorage. And, it will give motivation to become Tokamak Netowork’s sequencer. The progress is implementing the PC version → mobile version → QA → reflecting feedback → open testnet.

## 4.3 Tokamak DAO V2

- **Goals**
  - Seminar on DAO Proposal
  - Document defining integration of Staked WTON with Tally
  - Finalize policy guidelines of DAO
  - Seminar on using Tally to interact with Arbitrum DAO
  - Build an MVP on Sepolia with proposed structure and guidelines
- **Explanation for the outside**
  - In Q2, we cannot focus on the DAO V2 task. So, we make a tight plan for it. There are many considerations for our new DAO.  Such as FIT 21 & compatibility between Tally and Tokamak DAO contracts. After this quarter is over, we will build an MVP on sepolia with a new structure and guidelines.

# 5. Budget Request

## 5.1. Budget Usage in Q2

|  | Income (TONs) | Outcome (TONs) | Total |
| --- | --- | --- | --- |
| Q1 Budget | 25,550 | 24,000 | 1,550 |
| Q2 Budget | 12,500 |  | 12,500 |
| BOE |  |  | 1,136 |
| Total | 38,050 | 25,136 | **15,186(L1+L2)** |

## 5.2 Budget Request in Q3

|  | Grant | Operation cost | Reserve fund(BOE + additional people) | Total |
| --- | --- | --- | --- | --- |
| Amount | 18,000 | 1,300  | 3,000 | 22,300 |

- **Operation cost detail: **
  - May(317$) + June(450$)**(expected)** + Q3(450$ * 3) = 2117$ 
  - 2117$ / 1.67$ = 1267.6646 TON

## 5.3 Gap

- In Q2, we requested 21,000 TON as budget and approved 25,000 TON.
- In this quarter, operation cost is added to the grant request.
- And we are considering additional recruitment, so we also request reserve funds for it.