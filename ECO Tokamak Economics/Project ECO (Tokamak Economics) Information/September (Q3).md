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
| Progress per goal | stopped |

- **Additional outputs**
  - **(Design)** Transfer of [Simple staking](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=14-8924&t=oGVriYzmjmRUT7q8-11) design environment.
  - **(Design) **Transfer of [Zeplin account](https://app.zeplin.io/workspace/66b31e96552e207da12065ae/projects) (Onther -> Tokamak)
  - **(Price-API)** Fix API to get total staked amount in price dashboard
- **Explain the progress**
  - DAO migration is stopped because we will use Tally as our next generation of DAO.

### 2.1.2 Staking V2

| **Goal** | deploy contracts on mainnet | Update white paper | publish it to testnet & mainnet(pc/mobile) |
| --- | --- | --- | --- |
| **Progress per goal** | 90% | 100% | 90% |

- **Additional outputs**
  - **(Model)** 
  - **(Contract)** Upgrade staking v2 contract to v2.5 & DAO contract was changed based on staking v2.5 contract
  - **(Service & Design)** After internal feedback, there are some changes in UX/UI part. So, it takes more time than we expected
- **Explain the progress**
  - Currently, we opened an internal test on sepolia and collected feedback from team members. After collecting and reflecting on feedback, we can deploy contracts & services on mainnet.

### 2.1.3 Tokamk DAO V2

| Goal | Seminar on DAO Proposal | Document defining integration of Staked WTON with Tally | Finalize policy guidelines of DAO | Seminar on using Tally to interact with Arbitrum DAO | Build an MVP on Sepolia with proposed structure and guidelines |
| --- | --- | --- | --- | --- | --- |
| Progress per goal | 100% | 90% | 80% | 100 (This task is modified using Uniswap DAO and Tally as reference. Arbitrum DAO is too complex and we agreed to follow a hybrid approach). | Will be done in Q4 |

- **Additional outputs**
  - 
- **Explain the progress**
  - Policy guidelines of DAO were finalized(80%)
    - Research on Security council is completed and conducted a seminar with Kevin
    - Voting pattern and other numerical parameters are yet to be finalized
  -  Research Cross-chain governance on Uniswap (Completed) 
  - A demo using Tally on Sepolia testnet for dao v2 will be proceed in Q4.
  - When we set a goal for this quarter at the end of the second quarter, we set a larger goal than we expected to be able to do to make up for what we failed to move forward in the second quarter.

## 2.2 Outputs per person

<!-- Unsupported block type: unsupported -->

# 3. Challenges and Lessons Learned

## 3.1. Challenges

- Making a multi-L2 support service on L1 is more complex than expected. Because to show transaction history, each L2 needs its own subgraph. So, it is hard to provide transaction history to all of the L2  

## 3.2. To Prevent Similar Challenges

- Consider another way to provide the transaction history of several L2. One of the options is using RPC directly. But it will take a long time to get data from it. So, we will consider another option.

## 3.3 Lessons Learned

| **Team** | **Lessons** |
| --- | --- |
| Model | DAO : Creating a complex DAO without an active user base isn't practical. Instead, a simple DAO with a hybrid approach that evolves naturally alongside the community is a better fit for our needs |
| Contract | With the change in the seigniorage distribution ratio according to Whitepaper V2, the TON staking service now reflects multiple Layer 2s. We thought that we should expand the existing service to Layer 2, and do more research on various services that consider Layer 2, and we thought that we should do more research on contract development that considers Layer 2. |
| Service | Connecting multiple Layer 2s are not easy way. And he more features added to the service, the more complicated the service becomes and the code becomes messy. So, we have to consider refactoring or something to make maintenece easier. |
| Design | The blockchain environment seems like the season. We need to prepare before the season changes and always be ready and respond quickly to changes in the environment, just as no season has the same as the past. |

# 4. Goals of Q4, 2024

## 4.1. Service maintenance

- **Goals**
  - Update price dashboard
    - Total Supply -> update the definition, as this is the accurate value.
    - replace uniswap v3 links
    - update C2 + C3 definition (TONStarter mining has ended)
- **Explanation for the outside**
  - The migration of Tokamak DAO was stopped, because we can use Tally as our next generation of DAO. So from Q4, we don’t have any expected goal for this task.

## 4.2. Staking V2

- **Goals**
  - open staking v2 desktop version on mainnet
  - update mobile version from staking v2 to staking v2.5
- **Explanation for the outside**
  - In early Q4(may be in October), we expected to open service on mainnet. After the service is opened, L2s of Tokamak Network will be registered as an operator on our staking service. Users can stake their TON to the L2 operator and get seigniorage from it.

## 4.3 Tokamak DAO V2

- **Goals**
  - Finalize the policy guidelines 
    - Voting Pattern and other numerical parameters 
  - Build a prototype of DAOv2 on Sepolia with proposed structure and guidelines (Including security council)
  - Seminar on Cross-chain governance implementation (Uniswap DAO as reference)
- **Explanation for the outside**
  - Launch the prototype of the new Tokamak DAO (DAO v2) on the testnet, along with all finalized policies. This will allow users to explore and try out DAO v2, helping them understand how the process works and the role of new features like the security council.

# 5. Budget Request

## 5.1. Budget Usage in Q3

|  | Income (TONs) | Outcome (TONs) | Total |
| --- | --- | --- | --- |
| Q1 Budget | 25,550 | 24,000 | 1,550 |
| Q2 Budget | 25,000 | 20,500 | 4,500 |
| Q3 | 11,150 |  | 11,150 |
| BOE |  | 600 |  |
| Total | 61,700 | 45,100 | 16,600 |

## 5.2 Budget Request in Q4

- **Operation cost detail: **
  - 450$/Month * 3 = 1350$ 

|  | Grant | Operation cost | Reserve fund(BOE + additional people) | Total |
| --- | --- | --- | --- | --- |
| Amount | 18,000 | 1,300  | 3,000 | 22,300 |

  - 1350$ / 1.1$ = 1227.27 TON

## 5.3 Gap

- .