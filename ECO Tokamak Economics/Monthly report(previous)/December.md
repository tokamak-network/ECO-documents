# 1. Goal

- The final goal of ECO consists of two parts
  1. Finalize implementation of the next landing page and manage them
  1. Implement Simple Staking & DAO community version and shut down service. One of its goals is to minimize the withdrawal of funds when shut down official staking services.

## i. Milestone

### A. Simple Staking

- A1. Propose DAO agenda for upgrade staking contract
- A2. Open Staking V2.5 testnet (25, Q1)
- A3. Open Simple Staking V2.5: DAO candidate with L2 open [Jason] (25, Q1)
- A4. Open **community version v1.0 + community guide: **support simple staking v2.5 [Jason, Lucas, Max, Zena] (25, Q1)
- A5. Publish TON staking SDK v1.0: support simple staking v2.5 [Zena] (25, Q1)
- A6. Shutdown Simple staking V2.5 [Jason] (25, Q1)
- A7. Publish slashing protocol (collaborate with TOP + TRH team) [Suah, Harvey]  (25, Q3)
- A8. Open 1st hackathon or development event using TON staking SDK with prize money [Ale] (25, Q3)
- A9. Open public seminar/workshop about slashing [Suah, Harvey] (25, Q3)
- A10. Peer reviewed article about slashing [Suah] (25, Q3)
- A11. **Publish TON staking SDK v2.0**: support slashing [Harvey] (25, Q3)
- A12. Open **community version v2.0 + community guide: **support slashing [Jason, Lucas, Max, Harvey] (25, Q3)
- A13. **Publish fast withdraw using staked TON protocol** [Suah, Zena] (26, Q1)
- A14. **Publish TON staking SDK v3.0**: support fast withdraw using staked TON [Zena] (26, Q1)
- A15. **Open** **community version v3.0 + community guide: **support fast withdraw using staked TON [Jason, Lucas, Max, Zena] (26, Q1)
- A16. Open 2nd hackathon using TON staking SDK with prize money [Ale] (26, Q1)

### B. Tokamak DAO V2 

- B1. DAO v2 implementation on Sepolia using Tally
- B2.** Publish DAO V2.0 policy document**: add information about snapshot and forum [Praveen] (25, Q1)
- B3. **Open community version v1.0 + community guide**: Add information about new agenda creation (snapshot and forum). [Zena, Lucas, Harvey, Max] (25, Q2)
- B4. Shutdown DAO frontend and backend
- B5. **Open community version v2.0**: Add support for arbitrary code execution like Tally interface. [Zena, Lucas, Max] (25, Q2)
- B6. **Publish DAO V2.1 policy document**: add security council related policies [Praveen] (25, Q3)
- B7. **Publish DAO v2.1 protocol + community guide:** Remove EOA from DAOCommittee Proxy, Open security council, update existing contracts to improve security and define roles of security council. [Harvey] (25, Q4)
- B8. **Open community version v3.0**: Remove EOA from DAOCommittee Proxy, Open security council, update existing contracts to improve security and define roles of security council. [Zena, Lucas, Harvey, Max] (25, Q4)
- B9. **Publish Tokamak Network DAO L2 support + community guide** [Harvey, Suah] (26, Q1)

### C. Tokamak Network Landing page

- C1. Open new landing page [Ale, Max, Lucas] (24, Q4)
- C2. Open sub-landing page for Protocols [Ale, Max, Lucas] (25, Q1)
- C3. Shutdown price dashboard [Jason] (25, Q1)
- C4. Open price API v2.0: optimize current price API without affecting widely used functions [Jason] (25, Q3)  

## ii. Timeline

| Year | Quarter | Milestone output | Outputs | Milestone |
| --- | --- | --- | --- | --- |
| Up until 2024 | Q4 | A1, B1, C1 | 2 service open |  |
| 2025 | Q1 | A2, A3, A4, A5, A6, B2, C2, C3 | 1 service, 1 sdk, 1 document, 1 guide, 1 service update | Simple staking & price dashboard shut down |
|  | Q2 | B3, B4, B5 | 2 service update, 1 guide  |  |
|  | Q3 | A7, A8, A9, A10, A11, A12, B6 | 1 protocol, 1 hackathon, 1 seminar, 2 service update |  |
|  | Q4 | B7, B8 | 1 document, 2 service update, 1 guide |  |
| 2026 | Q1 | A13, A14, A15, A16, B9 | 2 service update, 1 protocol, 1 hackathon |  |

## iii. Easy to understand explanation even outside of team and typical community participant (non-technical persons): **The importance of each milestone deliverable, considering the Tokamak Foundation's strategy and the current Tokamak ecosystem**

- **About Simple staking:** The first goal is to implement a community version of staking services can encourage outside developers to participate. It will be launched in Q1. Even though we implement a community version, we have to implement 2 types of protocols. One is about slashing the other is fast withdraw using staked TON. Slashing is a necessary part of L2 and FW is for increased utility of Staked TON. We think slashing protocol is more important protocol than FW. So, we will focus on slashing first. It will be not an easy task because we have to collaborate with other teams.
- **About DAO:** Current Tokamak Network DAO is based on 3 member DAO Committee where they have the exclusive voting rights. To improve communication with community members, we are working towards adding features such as temperature check (snapshot) and forum where community members can voice their opinions. Our original plan was to use [Tally](https://www.tally.xyz/) as our new DAO interface. But we cannot use Tally. So, we have to change the whole plan. We gonna implement the community version as soon as possible, and will add more policies for operate DAO directly.  
- **About Tokamak Landing page****:** As we change the strategy of Tokamak Network, we need a new landing page to show our strategy and ecosystem more effectively. So we are making the next Tokamak Network landing page and some of the functions in the [Price dashboard](https://price.tokamak.network/) will be integrated into a new landing page. We will also provide more detailed information about protocols developed by Tokamak Network to encourage developers to build services around our protocol; create a developer centric community. 
- **About Price API:** Tokamak Network plans to remove all of the back-end related resources. But price-API will remain because we have to provide some information to centralized exchange (such as Upbit). So we have to remove unused API functions & update logic for used API functions

# 2. This quarter outputs

## Easy to understand explanation even outside of team and typical community participant (non-technical persons): How did your team contribute to achieving the milestone this quarter?

This quarter, we mainly focused on the Simple Staking V2 and Tokamak DAO on Tally. 

- **Simple Staking**

The original plan was to complete internal testing for Simple Staking V2 and launch it by November. However, during the internal testing phase, we received extensive feedback regarding the existing UI. Based on this feedback, we decided to implement a comprehensive update to the UI to enhance the overall user experience.

The key tasks completed this quarter are as follows:

1. **Incorporation of Internal Testing Feedback**: We addressed usability issues and improvement requests identified during internal testing, ensuring the necessary adjustments were made.
1. **UX/UI Update**: The existing UI was thoroughly reviewed and redesigned to create a more intuitive and user-friendly interface.

These efforts were aimed at improving user satisfaction and establishing a solid foundation for stable operation post-launch. Moving forward, we plan to complete final checks to ensure stability and proceed with the service launch as scheduled.

dao agenda 준비

- **Tokamak DAO V2**

During this quarter, the work related to Tokamak DAO V2 focused on preparing to utilize Tally as the next-generation Tokamak DAO interface. To achieve this, we conducted in-depth research on new DAO policies and held an internal seminar to discuss the direction based on the research findings.

The conclusions from the seminar were shared with the foundation, and feedback was incorporated to finalize the future course of action. Additionally, a new smart contract with features essential for the next-generation DAO was developed, laying the technical groundwork for its implementation.

- **Tokamak landing page**

With the strategic shift in Tokamak Network, the need for a new landing page that effectively reflects the network's core values and enhances user experience has emerged. To address this, we are in the process of removing outdated elements from the existing landing page and restructuring it to clearly and attractively showcase the various projects under the Tokamak Network.

- **Service maintenance**

Project ECO is responsible for managing and maintaining various services currently operated within the Tokamak Network. The primary targets include Simple Staking, DAO, Price Dashboard, and the Tokamak landing page, all of which are running on the mainnet. The project supports continuous operational efficiency through feature enhancements, ensuring stability, and resolving any issues that arise.

## Actual outputs description

### i. Deliverable

**Staking V2**

- Deploy TON staking V2.5 contract + upgrade DAO to support preliminary security council features
  - [issue #59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
  - [DAO Agenda #13](https://dao.tokamak.network/#/agenda/13): End the notice on Nov 15, 2024, 18:35**,  waiting to vote **

**DAO V2**

- DAO v2 implementation on Sepolia using Tally: [https://www.tally.xyz/gov/tokamakgovernor-upgradable](https://www.tally.xyz/gov/tokamakgovernor-upgradable)

### ii. Work

1. Resource
  - A new member joined: Max
    - He is contributing to Tokamak Landing page.
1. Product
**Staking V2**

Simple Staking V2 - Added more detailed information about sequencer seigniorage
    - Reflect feedback from the internal test to frontend([commit](https://github.com/tokamak-network/simple-staking-v2/commit/00fcbd8893c85b3ad9817b28ca17c649a74d6c5f))
    - Reflect feedback from internal test([commit](https://github.com/tokamak-network/simple-staking-v2/commit/00fcbd8893c85b3ad9817b28ca17c649a74d6c5f))

Simple Staking V2.5 - Reflected DAO candidate with L2 idea from whitepaper to the frontend and improved overall user experience
    - Created Simple Staking V2.5 storyboard ([figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=14-2740&t=g9BqQslSMzhRcJty-0))
    - Created APY estimator for Staking v2.5 ([calculator](https://docs.google.com/spreadsheets/d/1oMbK3sYFu3Svq0yaPhBw4FQ4FArOFwjf2Y3WzLRlvyY/edit?gid=0#gid=0))
    - Simple Staking v2.5 UX/UI [usability improvement](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=82-240&node-type=frame&t=f9uGdunUtUUaONH2-11)
    - Simple Staking v2.5 UX/UI [update](https://github.com/tokamak-network/simple-staking-v2/commit/c5e21083c916057590b0b8c0d9b4b5ebc4801039), [page](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/home)

Prepare to propose agenda for upgrade staking & DAO contracts
    - Make scripts to test the staking v2.5 deployment using the agenda ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/test-mainnet/))
    - Rehearsal of upgrading staking v2.5 on the sepolia [#57 ](https://github.com/tokamak-network/ton-staking-v2/issues/57)doc
    - Test agenda with script on Mainnet Forking ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/mainnet-agenda-test/))
    - wrote a draft about the DAO agenda (doc)
    - Gas fee calculation required for deployment/setup and agenda submission [doc](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0)
    - Preparing/Deploy staking v2.5 contracts on mainnet [#54, ](https://github.com/tokamak-network/ton-staking-v2/issues/54)doc
    - Created templates for DAO agenda to increase transparency ([link](https://github.com/tokamak-network/ton-staking-v2/issues/59))

**DAO V2 - 이동**

Research and test different security council features from Tally
    - Research The Security Council Management Contract of ArbitrumFoundation(doc) 
    - Develop the functions of DAO for only the security council and the TokamakTimelock  ([issue#60](https://github.com/tokamak-network/ton-staking-v2/issues/60), [commit](https://github.com/tokamak-network/ton-staking-v2/commit/bae4ce783774487ca6d61d558723e4d7090a7f2e))
    - Tested security council features and a proposal using Tally  [doc](/149d96a400a3804d810cd3565c7382f9)
    - Develop the test scripts to check the security council's functions [issue#8](https://github.com/tokamak-network/ton-staking-tally-contract/issues/8)

Research and test out Snapshot (off-chain voting platform for temperature check)
    - Worked on creating a test environment for snapshot use. doc  task-2
    - Creating a voting strategy [ issue](https://github.com/tokamak-network/ton-staking-v2/issues/61) 
    - Summary of functions related to voting tokens doc
    - Designed the parameters for a voting strategy [a tokamak-dao voting strategy readme](https://github.com/tokamak-network/snapshot-strategies/tree/tokamak-dao/src/strategies/tokamak-network-dao#tokamak-network-dao-voting-strategy) 

Research and test out Tokamak Network DAO features on L2
    - L2 DAO Research & Decided the Policy (doc)
    - develop & Test the L2 DAO in Sepolia ↔ Thanos ([doc](/14bd96a400a380008be5d9eb5b127876#14bd96a400a3802aa5eee0ad4bef53b4), [commits](https://github.com/tokamak-network/ton-staking-v2/tree/L2-DAO-Test))
    - DAO readme logic Changed update & address update ([link](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/README.md#dao-contract-upgraded-work-contents), [commits](https://github.com/tokamak-network/tokamak-dao-contracts/commits/main/), [link](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/README.md#dao-contract-upgraded-work-contents), [commits](https://github.com/tokamak-network/tokamak-dao-contracts/commits/main/))

**Created new Tokamak Network landing page**

  - Workflow [doc](/d84d1bbf22014b198c973d10c56e5db8)
  - Research v2 [slide](https://docs.google.com/presentation/d/1m9WvGJutdnc-dH0xTMuV49Ggnr19vWqkGSrWJrJWivs/edit#slide=id.g2f91639884e_1_0)
  - Storyboard v0.2, v0.3, v0.4 [figma](https://www.figma.com/design/7u09jK09RXmdi9umRSQZoy/Tokamak-Network-Landing-Page?node-id=706-1359&p=f&t=b0SiWlzQlMyYa3UI-0)
  - Code [commits](https://github.com/tokamak-network/tokamak-landing-page/commits/main/)
1. Knowledge
Research on Quadratic voting
    - Research on [Quadratic Voting in Gitcoin](https://docs.google.com/presentation/d/1-j9ElorDROxieqaZH67GjTXH8QlgOKnVkGcZn_DAXm0/edit#slide=id.g3071e1d25e4_0_0) and noted some observations. 
    - Quadratic voting seminar([Video](https://drive.google.com/file/d/11c7Pj_xhQKHv6MEDGHVuVbfc_o2oaTHX/view?usp=sharing))
    - shared QV research to get Kevin's comments([link](https://w1724828219-i4h810456.slack.com/archives/C07JU6K4KDY/p1729167410529389))
1. Policy
  1. Praveen policy regarding new DAO
1. Maintenance
**DAO**

  - Add new contract & new function to existing contracts([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/959af1e8b48ef0a324f271f35b8f8ad65914d071))
  - resolve event monitor issue on Sepolia([commit](https://github.com/tokamak-network/tokamak-dao-server/commit/3c0b625a4d9688155b85f5101be12eba12b7fd2f))
  - update dao front-end to resolve on-chain effect related issues ([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/b974cb6871398856de30b3e749ab034a4b143582))

**Price Dashboard**

  - Update price dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/6b0e589f51bed55b52470bb7752592f937dd73e3))

**Design update**

  - Integrated GNB, Footer Design for New L2 On-Denad(TRH) Service Addition. (Notion)

## The reason why each under

### i. List of challenges faced for each under-achieved deliverable

- **DAO V2:** In this quarter, we set 3 goals for this task. And our original plan is to use Tally as our new DAO interface. As a result of the discussion with the Tokamak Foundation, we cannot use Tally due to limitations from contract modification which makes it harder for users to vote using staked TON. So, It affects our Q4 progress.
- **Staking V2:** Our goal for this quarter was to launch Staking V2. However, during internal testing, significant UI feedback was received, leading us to postpone the launch and focus on upgrading to a more refined Staking V2.5.
The development of Staking V2.5 has been completed, but due to the extensive UI changes, additional internal testing is required. The service will be officially launched after the testing phase is finalized. Furthermore, the release of Staking V2.5 requires the approval of a DAO agenda that includes the upgrade details for the staking contract. 

Currently, this agenda has not yet been voted on. Considering the necessary mainnet infrastructure setup, the service launch is expected to occur approximately one week after the DAO agenda is approved.

### ii. List of solved challenges

- **DAO V2:** Project ECO team changed the plan to make the DAO community version as soon as possible. And other tasks such as policy guidelines will also be modified accordingly.
- **Staking V2:** To respond to the voting result, we set an alarm for agenda voting.

### iii. Strategy for unsolved challenges

- There are no unsolved challenges, but we will try to finish the outstanding tasks in next quarter. 

# 3. Change in next quarter's deliverables

- 

Currently there are no changes in next quarter’s deliverables as we have not defined it before this report. We will fill this out during next quarter based on this report.

# 4. Budget request

|  | Grant | Operation cost | Reserve fund(BOE + additional people) | Total |
| --- | --- | --- | --- | --- |
| Amount | 15,000 | 1,150 | 1,000 | 17,150 |

- Grant detail
  - previously we requested 4,500 TON per person as a grant
  - We will request 3,000 TON per person as a grant in this quarter
- **Operation cost detail: **
  - AWS: 450$ / month 
  - Subgraph: 150$ / month
  - Figma: 42 $ / month 
  - (1800 + 126) / 1.74 = 1106.89

# 5. Change in the road map

Currently there are no changes in next quarter’s road map as we have not defined it before this report. We will fill this out during next quarter based on this report.