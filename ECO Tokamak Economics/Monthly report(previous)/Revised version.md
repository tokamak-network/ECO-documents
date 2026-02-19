# 1. Final Goals

-  Project ECO's final goals are twofold:
  1. Design and implement Tokamak Network's staking system—including slashing mechanisms and fast withdrawals—as specified in the [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md). This will enhance L2 security, increase TON and staked TON utility, and strengthen the Tokamak Network DAO's decentralization and security. 
  1. Deploy the Simple Staking & DAO community version and discontinue the hosted frontend and backend services, while minimizing any resulting TON withdrawals

## 1-a. Milestone

### A. Simple Staking 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Simple Staking V2.5** | Propose DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Staking V2.5 testnet | 1 service |  |
|  | Launch Simple Staking V2.5 with DAO candidate and L2 support | 1 service | 2 service + 1 DAO agenda |
| **Community version
** | Launch **community version v1.0 + community guide** with Simple Staking V2.5 support | 1 service with 1 guide |  |
|  | Release TON staking SDK v1.0 with Simple Staking V2.5 support | 1 code release | 1 code release, 1 service with guide |
| **Addition of slashing protocol** | **Release TON staking SDK v2.0** with slashing support | 1 code release |  |
|  | Launch **community version v2.0 + community guide** with slashing support | 1 service update with 1 guide | 1 code release, 1 service update with guide |
| **Addition of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support for staked TON | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support for staked TON | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

### B. Tokamak DAO V2 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Tokamak DAO v2** | Open DAO v2.0 on Sepolia | 1 service | 1 service |
| **Added use of Snapshot and forum** | **Open community version v1.0 + community guide**: Include documentation for new agenda creation via Snapshot and forum | 1 service with 1 guide | 1 service, 1 guide, 1 document |
| **Improvement of proposal interface** | **Open community version v2.0**: Add support for arbitrary code execution | 1 service | 1 service |
| **Apply the security council** | **Open community version v3.0**: Remove EOA from DAOCommittee Proxy, implement security council, enhance contract security, and define security council roles | 1 service | 1 service |

### C. Tokamak Network Landing page

| Category | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Landing page** | Open a new landing page  | 1 service |  |
|  | Open sub-landing page for Protocols  | 1 service update |  |
| **Price API 2.0** | **Open price API v2.0**: optimize current price API without affecting widely used functions   | 1 service update |  |

## 1-b. Easy to understand explanation even outside of team and typical community participant (non-technical persons): **The importance of each milestone deliverable, considering the Tokamak Foundation's strategy and the current Tokamak ecosystem**

- **About Simple Staking: **Our primary goal is to implement a community version of staking services that encourages outside developer participation, launching in Q1. This implementation requires two key protocols: slashing and fast withdrawal (FW) using staked TON. Slashing, which is essential for L2 and specified in our [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md), takes priority over FW, though FW will enhance staked TON utility. Given that slashing requires collaboration with other teams, we anticipate this being a complex but necessary undertaking.
- **About DAO:** The current Tokamak Network DAO operates through a 3-member DAO Committee with exclusive voting rights. To enhance community engagement, we are implementing features like temperature checks (snapshot) and a forum where community members can share their opinions. Initially, we planned to use [Tally](https://www.tally.xyz/) as our new DAO interface. However, since Tally is not viable, we have revised our approach. We will implement the community version promptly and establish additional policies for direct DAO operations. 
- **About Tokamak Landing Page:** With Tokamak Network's evolving strategy, we're developing a new landing page to better showcase our strategy and ecosystem. The new page will incorporate features from the [Price dashboard](https://price.tokamak.network/) and provide comprehensive documentation about Tokamak Network protocols. This will help developers understand and build services using our protocol, fostering a developer-centric community. 
- **About Price API: **Tokamak Network plans to remove all frontend and backend resources. However, the Price API will remain active as we must continue providing data to centralized exchanges (such as Upbit). We will remove unused API functions and optimize the logic for active ones.

## 1-c. Timeline

| Year-Quarter | 2024-Q4 | 2025-Q1 | 2025-Q2 | 2025-Q3 | 2025-Q4 | 2026-Q1 |
| --- | --- | --- | --- | --- | --- | --- |
| Milestone | Open Tokamak DAO v2.0 on Sepolia,
 | Simple Staking V2.5,
Community version,
Landing page | Added use of Snapshot and forum,
Improvement of proposal interface
Price APi 2.0 | Addition of slashing protocol | Apply the security council | Addition of fast withdrawal protocol |

# 2. This quarter outputs

## 2-a. Easy to understand explanation even outside of team and typical community participant (non-technical persons): How did your team contribute to achieving the milestone this quarter?

Simple Staking V2 and Tokamak DAO on Tally.

- **Simple Staking **

We planned to complete internal testing and launch Simple Staking V2 by November. During testing, we received substantial UI feedback that prompted us to implement comprehensive interface improvements to enhance user experience.
Here are the key accomplishments this quarter:

1. **Incorporation of Internal Testing Feedback**: We resolved usability issues and implemented improvements based on internal testing results.
1. **UX/UI Update**: We redesigned the interface to be more intuitive and user-friendly.
1. **Propose DAO Agenda**: Since contract upgrades require DAO approval, we thoroughly tested the upgrade process through multiple DAO executions before submitting our proposal to Tokamak DAO.

These improvements strengthen our foundation for stable operations post-launch. We are now conducting final stability checks before proceeding with the scheduled launch.

- **Tokamak DAO V2**

This quarter's work on Tokamak DAO V2 focused on evaluating Tally as our next-generation DAO interface. We conducted thorough research on new DAO policies and hosted an internal seminar to determine our strategic direction.

After reviewing our seminar findings with the foundation and incorporating their feedback, we determined that the Tally interface was incompatible with our staking contract and chose a different approach. We developed a new smart contract with essential features for the next-generation DAO, laying the technical groundwork for implementation.

- **Tokamak landing page**

Following Tokamak Network's strategic shift, we need a new landing page that better reflects our core values and improves user experience. We are currently removing outdated content and reorganizing the page to showcase Tokamak Network's projects in a clear, engaging way.

- **Service maintenance**

Project ECO manages and maintains key Tokamak Network services, including Simple Staking, DAO, Price Dashboard, and the Tokamak landing page all operating on the mainnet. The project focuses on enhancing features, maintaining stability, and promptly addressing operational issues.

## 2-b. Actual outputs description

### 2-b-i. Deliverable

**Staking V2**

- Deploy TON staking V2.5 contract + upgrade DAO to support preliminary security council features
  - [issue #59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
  - [DAO Agenda #13](https://dao.tokamak.network/#/agenda/13): End the notice on Nov 15, 2024, 18:35**,  waiting to vote **

**DAO V2**

- DAO v2 implementation on Sepolia using Tally: [https://www.tally.xyz/gov/tokamakgovernor-upgradable](https://www.tally.xyz/gov/tokamakgovernor-upgradable)

### 2-b-ii. Work

1. **Resource**
  - A new member joined: Max
    - He is contributing to the Tokamak Landing page.
1. **Product**
**Staking V2**

  - Simple Staking V2 - Added more detailed information about sequencer seigniorage
    - Reflect feedback from the internal test to frontend([commit](https://github.com/tokamak-network/simple-staking-v2/commit/00fcbd8893c85b3ad9817b28ca17c649a74d6c5f))
  - Simple Staking V2.5 - Reflected DAO candidate with L2 idea from whitepaper to the frontend and improved overall user experience
    - Created Simple Staking V2.5 storyboard ([figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=14-2740&t=g9BqQslSMzhRcJty-0))
    - Created APY estimator for Staking v2.5 ([calculator](https://docs.google.com/spreadsheets/d/1oMbK3sYFu3Svq0yaPhBw4FQ4FArOFwjf2Y3WzLRlvyY/edit?gid=0#gid=0))
    - Simple Staking v2.5 UX/UI [usability improvement](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=82-240&node-type=frame&t=f9uGdunUtUUaONH2-11)
    - Simple Staking v2.5 UX/UI [update](https://github.com/tokamak-network/simple-staking-v2/commit/c5e21083c916057590b0b8c0d9b4b5ebc4801039), [page](https://simple-staking-v2-git-feat-v25-tokamak-network.vercel.app/home)
  - Prepare to propose agenda for upgrade staking & DAO contracts
    - Make scripts to test the staking v2.5 deployment using the agenda ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/test-mainnet/))
    - Rehearsal of upgrading staking v2.5 on the sepolia [#57 ](https://github.com/tokamak-network/ton-staking-v2/issues/57)doc
    - Test agenda with script on Mainnet Forking ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/mainnet-agenda-test/))
    - wrote a draft about the DAO agenda (doc)
    - Gas fee calculation required for deployment/setup and agenda submission [doc](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0)
    - Preparing/Deploy staking v2.5 contracts on mainnet [#54, ](https://github.com/tokamak-network/ton-staking-v2/issues/54)doc
    - Created templates for DAO agenda to increase transparency ([link](https://github.com/tokamak-network/ton-staking-v2/issues/59))

**Created a new Tokamak Network landing page**

  - Workflow [doc](/d84d1bbf22014b198c973d10c56e5db8)
  - Research v2 [slide](https://docs.google.com/presentation/d/1m9WvGJutdnc-dH0xTMuV49Ggnr19vWqkGSrWJrJWivs/edit#slide=id.g2f91639884e_1_0)
  - Storyboard v0.2, v0.3, v0.4 [figma](https://www.figma.com/design/7u09jK09RXmdi9umRSQZoy/Tokamak-Network-Landing-Page?node-id=706-1359&p=f&t=b0SiWlzQlMyYa3UI-0)
  - Code [commits](https://github.com/tokamak-network/tokamak-landing-page/commits/main/)
1. **Knowledge**
**DAO V2**

  - Research on Quadratic voting
    - Research on [Quadratic Voting in Gitcoin](https://docs.google.com/presentation/d/1-j9ElorDROxieqaZH67GjTXH8QlgOKnVkGcZn_DAXm0/edit#slide=id.g3071e1d25e4_0_0) and noted some observations. 
    - Quadratic voting seminar([Video](https://drive.google.com/file/d/11c7Pj_xhQKHv6MEDGHVuVbfc_o2oaTHX/view?usp=sharing))
    - shared QV research to get Kevin's comments([link](https://w1724828219-i4h810456.slack.com/archives/C07JU6K4KDY/p1729167410529389))
  - Research and test different security council features from Tally 
    - Research The Security Council Management Contract of ArbitrumFoundation(doc) 
    - Develop the functions of DAO for only the security council and the TokamakTimelock  ([issue#60](https://github.com/tokamak-network/ton-staking-v2/issues/60), [commit](https://github.com/tokamak-network/ton-staking-v2/commit/bae4ce783774487ca6d61d558723e4d7090a7f2e))
    - Tested security council features and a proposal using Tally  [doc](/149d96a400a3804d810cd3565c7382f9)
    - Develop the test scripts to check the security council's functions [issue#8](https://github.com/tokamak-network/ton-staking-tally-contract/issues/8)
  - Research and test out Snapshot (off-chain voting platform for temperature check)
    - Worked on creating a test environment for snapshot use. doc  task-2
    - Creating a voting strategy [ issue](https://github.com/tokamak-network/ton-staking-v2/issues/61) 
    - Summary of functions related to voting tokens doc
    - Designed the parameters for a voting strategy [a tokamak-dao voting strategy readme](https://github.com/tokamak-network/snapshot-strategies/tree/tokamak-dao/src/strategies/tokamak-dao) 
  - Research and test out Tokamak Network DAO features on L2
    - develop & Test the L2 DAO in Sepolia ↔ Thanos ([doc](/14bd96a400a380008be5d9eb5b127876#14bd96a400a3802aa5eee0ad4bef53b4), [commits](https://github.com/tokamak-network/ton-staking-v2/tree/L2-DAO-Test))
    - DAO readme logic Changed update & address update ([link](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/README.md#dao-contract-upgraded-work-contents), [commits](https://github.com/tokamak-network/tokamak-dao-contracts/commits/main/), [link](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/README.md#dao-contract-upgraded-work-contents), [commits](https://github.com/tokamak-network/tokamak-dao-contracts/commits/main/))
1. **Policy**
  - L2 DAO Research & Decided the Policy (doc)
  - DAO V2 Policy Document([doc](/135d96a400a3808ebad2ea61e879db8b))
1. **Maintenance**
**DAO**

  - Add new contract & new function to existing contracts([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/959af1e8b48ef0a324f271f35b8f8ad65914d071))
  - resolve event monitor issue on Sepolia([commit](https://github.com/tokamak-network/tokamak-dao-server/commit/3c0b625a4d9688155b85f5101be12eba12b7fd2f))
  - update dao front-end to resolve on-chain effect related issues ([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/b974cb6871398856de30b3e749ab034a4b143582))

**Price Dashboard**

  - Update price dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/6b0e589f51bed55b52470bb7752592f937dd73e3))

**Design update**

  - Integrated GNB, Footer Design for New L2 On-Demand(TRH) Service Addition. (Notion)

## 2-c. The reason why each under

### 2-c-i. List of challenges faced for each under-achieved deliverable

- **DAO V2:** This quarter, we established three goals for DAO development. While our initial plan involved using Tally as our new DAO interface, discussions with the Tokamak Foundation revealed that contract modification limitations would make it difficult for users to vote with staked TON. This limitation has impacted our Q4 progress.
- **Staking V2:** Although we aimed to launch Staking V2 this quarter, significant UI feedback during internal testing led us to postpone the launch and develop an enhanced version—Staking V2.5. While development is complete, the extensive UI changes require additional internal testing. 
The service launch awaits both testing completion and approval of a DAO agenda containing staking contract upgrade details. The DAO agenda is currently pending vote. Once approved, we anticipate launching the service within approximately one week, allowing time for mainnet infrastructure setup.

### 2-c-ii. List of solved challenges

- **DAO V2:** The Project ECO team has revised its plan to prioritize developing the DAO community version. Policy guidelines and related tasks will be updated to align with this new direction.
- **Staking V2:** We have implemented a notification system to alert stakeholders about agenda voting.

### 2-c-iii. Strategy for unsolved challenges

- While there are no unresolved challenges, we plan to complete all remaining tasks in the next quarter. 

# 3. Change in next quarter's deliverables

- Since we have not yet defined next quarter's deliverables prior to this report, we will establish them in the next quarter based on the findings presented here.

# 4. Budget request

## 4-a. (this quarter)Previous budget requested

- Original budget: 22,300 TON
- Prepaid budget: 1,000 TON
- Request budget: 22,300 - 1,000 = 21,300 TON

## 4-b. (next quarter)Next budget request

- Budget request: 16,500 TON

## 4-c. Gap(Next - Previous) and why?

- Due to a reduction in the total grant allocation budget, we have adjusted our funding request downward. Given Project ECO's substantial operating costs, we are requesting a revised amount that accounts for both the reduced budget and our ongoing expenses.

# 5. Change in the road map

- As this is our first report using the new format, there are no changes to the roadmap yet. We will develop the roadmap and include it in our next quarterly report, incorporating the information presented here.