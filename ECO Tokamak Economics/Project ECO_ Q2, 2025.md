# 1. Final Goals

-  Project ECO's final goals are twofold:
  1. Design and implement Tokamak Network's staking system—including slashing mechanisms and fast withdrawals—as specified in the [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md). This will enhance L2 security, increase TON and staked TON utility, and strengthen the Tokamak Network DAO's decentralization and security. 
  1. Deploy the Simple Staking & DAO community version and discontinue the hosted frontend and backend services while minimizing any resulting TON withdrawals

## 1-a. Milestone

### A. Simple Staking 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Simple Staking V2** | Propose DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Staking V2 testnet | 1 service |  |
|  | new DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Contracts audit | 4 final reports, 1 blog post, 1 internal report |  |
|  | Launch Simple Staking V2 with DAO candidate and L2 support | 1 service | 2 service + 1 DAO agenda |
| **Community version** | Launch **community version v1.0 + community guide** with Simple Staking V2 support | 1 service with 1 guide |  |
|  | Release TON staking SDK v1.0 with Simple Staking V2 support | 1 code release | 1 code release, 1 service with guide |
| **Integration of Slashing Protocol** | **Release TON staking SDK v2.0** with slashing support | 1 code release |  |
|  | Launch **community version v2.0 + community guide** with slashing support | 1 service update with 1 guide | 1 code release, 1 service update with guide |
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support for staked TON | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support for staked TON | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

### B. Tokamak DAO V2 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Improvement of proposal interface** | **Open community version for DAO V1**: Add support for arbitrary code execution | 1 service | 1 service |
| **Testing DAO V2 on testnet** | Testing Snapshot with PoU  | 1 testnet |  |
| **Policy document for DAO V2** | Including Discord based RFC, Snapshot, PoU for sybil-attack | 1 documents |  |
| **Added use of Snapshot and forum** | **Open community version for DAO V2 **: Include new agenda creation via Discord and Snapshot with PoU | 1 service | 1 service, |

### C. Tokamak Network Landing page

| Category | Subcategory | Deliverable |
| --- | --- | --- |
| **Landing page** | Open a new landing page  | 1 service |
|  | Open sub-landing page for Protocols  | 1 service update |
| **Price API 2.0** | **Open price API v2.0**: optimize current price API without affecting widely used functions   | 1 service update |

## 1-b. Easy to understand explanation even outside of team and typical community participant (non-technical persons): **The importance of each milestone deliverable, considering the Tokamak Foundation's strategy and the current Tokamak ecosystem**

- **About Staking: **We are proceeding with development to create a developer-centric environment while faithfully following the content of the whitepaper. Therefore, we are developing two versions of staking services. The first is Staking V2, which is an upgraded version of the existing Simple Staking, and the second is the development of a Staking Community Edition.
- **About DAO:**  DAO V2 aims to provide more opportunities for community participation in decision-making on DAO agendas, not only through the development of the Community Edition but also through the introduction of off-chain voting.

## 1-c. Timeline

| Year-Quarter | Milestone |
| --- | --- |
| 2025-Q1 | - Landing page |
| 2025-Q2 | - Open Simple Staking V2
- Staking community version
- DAO 1.0 community version |
| 2025-Q3 | - Staking V2: Slashing protocol
- DAO V2: Policy document
- DAO V2: Snapshot test with PoU |
| 2025-Q4 | - Price API V2.0 |
| 2026-Q1 | - Addition of fast withdrawal protocol
- DAO 2.0 Community version |

# 2. This quarter outputs

## 2-a. Easy to understand explanation even outside of team and typical community participant (non-technical persons): How did your team contribute to achieving the milestone this quarter?

**Tokamak Economics**

- We designed an attention test mechanism for validator economics and theoretically demonstrated its security. This work will be presented at ETH CC, one of the biggest Ethereum conferences, in the next quarter.

**Staking V2**

- We opened simple staking V2 on public. To open it, we implemented smart contracts and front-end. And got security audit for smart contracts. Because of contract and communication with several audit firms, security audit was challenging. In order to create materials for other team members to refer to, we documented all the contents related to contracts and audits and held seminars to create materials.
- To make developer-centric environment, we are currently implementing Staking community version. Implementation and an internal test was finished. And after making documentation for Tokamak staking service, staking service will be converted to community version

**Tokamak DAO V2**

- We developed a comprehensive DAO Community Version platform that implements core governance features including committee member management with challenge eligibility tracking, interactive proposal creation with transaction simulation capabilities, seamless voting system, and automated metadata registration through GitHub integration - providing an intuitive interface accessible to both technical and non-technical participants.
- The platform development is currently in progress with member management and proposal creation/voting systems completed. We are working on integrating agenda functionality into the member management system to provide a unified governance experience. Next quarter, we plan to complete the remaining features and deploy to production for community rollout.
- **DAO Agenda Metadata Repository**
We developed a secure automated system for DAO agenda metadata registration that operates through Git PR workflow with automatic validation and verification. The system features cryptographic verification, on-chain validation, and comprehensive testing with 50+ test cases, enabling proposers to register agenda metadata for DAO committee voting through standardized pull request processes. Next quarter, we plan to conduct seminars, complete internal testing, and officially launch for public use.

## 2-b. Actual outputs description

### 2-b-i. Deliverable

**Staking**

- **Tokamak Economics**
  - Financial Cryptography 25 Workshop (WTSC) Presentation & Manuscript Publish ([ArXiv](https://arxiv.org/abs/2504.05094), [X](https://x.com/tokamak_network/status/1914225148540104755?s=46), [Seminar](https://drive.google.com/file/d/1dQCqiGOtiKN_2FpiDJLd61_M5BEVzS37/view))
  - Theoretical work on Attention Test ([ArXiv](http://arxiv.org/abs/2505.24393), [X](https://x.com/tokamak_network/status/1930275321598603503?s=46))
    - This work will be presented in ETH CC in July 1st ([X](https://x.com/tokamak_network/status/1933018666976903360?s=46))
- **Simple Staking V2**
  - Open Staking V2([x post](https://x.com/Tokamak_Network/status/1922964342158365049), [link](https://simple.staking.tokamak.network/home))
  - **Staking V2 Contract Audit**
    - 1 Final report
[REP-final-20250401T084012Z.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e08c488b-e6ac-4a27-b009-64ffeb01cb2b/REP-final-20250401T084012Z.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF6WSMGF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCod5tS5q5nVFqo5F1Q%2BXW2ginBcy%2Brd92sFOFm1%2FOZ6wIhAOMh3Hk5zv5qQL0z6T3%2BY%2BSr73s3QZTP7uGBrckciXpCKv8DCHoQABoMNjM3NDIzMTgzODA1IgyX4V6U45GudW7Hg7Aq3ANVBP2xmqzB6j4Yxm8d7%2Feu%2FTegAcjhtki91XQYErgaY70r2aKxlOZBcziPIE50brH5%2Byx4xcHzszSDJIOGYUecRnbqlEDEnfDhUiknBrzwNqNc2QyLjPcxnNQPte5YNrzpCg9GY0g25VrlDymZf%2B4xUoy%2Bhy06myyYLJtvokGm67tyVXVJSXhvM1sAUvGASCMwjKO7JDwOmvrulBRq6UA8W82eeg6NUSXM3Igp7eT97WSiJvig3Xn%2BJNTSVdE1nUon6DaS5y03XRcAK5mQLuXS4RR0d0LxW4wHn68ywPS7fO5%2FNRUmJTSiGeOdjyueTa553TDWkxG44qMU6TZpo9wYdeq0vHzI9ScRJEkFMfwpZYfqwuBUcsLI%2FYH7XTduX5iMVJ1kvGYIlcDwomAjLSqTdrQl8btGVtnD7Ari%2BDBixxTDLE4YqNsFHlJCBICUfF5rb%2Fi4JCvktt%2BekODdwHAy1oYl3vR6%2FGckSywtaUtc7a55nATCAnfVrayMyr%2FLAjvpvX8NnwwK4w7ADKZWsRkMgcRcfrnpHmBs2yQChEpCVUnsVADjedytAUtgV2FI2NOwTV2zf37Oy3ooDR3Vxj38GRRNHAh08s8amsCDa6PSa6JhvKwYrjcKHlCPLjDZmdvMBjqkAXOL%2FUGOG%2B3VZhkhrGUYnQ%2Fic6FzFeID5x4ecuZpny71QatIoopbw7dHZRNIsoOziXINQUNHHjJT%2F1xzWlvDOBc0BtIwJ11R2H23Nz1Ft8hmrI1Fz3Jc9cnqo7vC8NIFbeNcCvi8ucuyssq72p8499PqROx%2FYzPGTobKafJsl8bm7GVeTE%2BDQTVvqyvV66LcQgFuNx6vnW9sRIbh3RJpGcRK9U6y&X-Amz-Signature=45bca5c214b34f0236e545c0bed07057bdb743cfc1ec0c5b202283e3214162e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    - 2 blog posts: 
      - DAO & TON Staking V2 Audit Report([medium](https://medium.com/tokamak-network/dao-ton-staking-v2-audit-report-2fa7bb1a9291), [x post](https://x.com/Tokamak_Network/status/1914231055562973563), [issue#308](https://github.com/tokamak-network/ton-staking-v2/issues/308), [issue#309](https://github.com/tokamak-network/ton-staking-v2/issues/309))
      - Introducing TON Staking V2([medium](https://medium.com/tokamak-network/introducing-ton-staking-v2-9eee7b56c56b), [x post](https://x.com/Tokamak_Network/status/1913142806920761404))
    - 1 Document: Audit checklist([slack](https://tokamak-network.slack.com/archives/C07JU4P56MR/p1745821761499689), [notion](/1d9d96a400a3805e89dfe80baec86843))
    - Audit memoir([seminar](https://drive.google.com/file/d/1ZpzMkvVzFRgtMk9s2x1kLAD_QkAHLwmt/view), [slide](https://docs.google.com/presentation/d/1fjJpKtmFAGX_N2XJa7z-UtknOQiGynDkKYx6yI6mG-E/edit?slide=id.g35767e8b9d1_0_42#slide=id.g35767e8b9d1_0_42))
    - “DAO & TONStaking V2” Audit Report Seminar ([seminar](https://drive.google.com/file/d/141bl8T7Sf1CIDzvdyLuYaZc3s16OMr0g/view), [slide](https://docs.google.com/presentation/d/11dvDPptedeeYnWiFXIY0Rog7tZd3-iPB8bbOqBCc7c4/edit?slide=id.p1#slide=id.p1), [Podcast Voice](https://drive.google.com/file/d/1A4S21U9bGqhkYBYO5gH3pWIWgwGGRyry/view), [soundcloud](https://soundcloud.com/jason-hwang-726058445/dao-ton-staking-v2-audit), X)

**Tokamak DAO**

- DAO Agenda No.14 ([x post1](https://x.com/Tokamak_Network/status/1914650886871376009), [x post 2](https://x.com/Tokamak_Network/status/1915348571031044294), [agenda](https://dao.tokamak.network/#/agenda/14), [issue](https://github.com/tokamak-network/ton-staking-v2/issues/310))
- DAO Agenda No.15 ([x post](https://x.com/tokamak_network/status/1934948932490330500?s=46),  [agenda](https://dao.tokamak.network/#/agenda/15), [issue](https://github.com/tokamak-network/ton-staking-v2/issues/311) )

### 2-b-ii. Work

1. **Product**
  - **Tokamak Staking**
    - **Staking V2**
      - Developed “**Tokamak rollup metadata repository**” to display rollup details in L2 details panel of staking V2 and proposed to TRH team. Also, we proposed L2 state check and L2 contract verification using this repository. ([repo](https://github.com/tokamak-network/tokamak-rollup-metadata-repository), [ppt](https://docs.google.com/presentation/d/1gCKN7XGDL_aYNKlHseZD4PUoocNxwbjlR0y1sH3CuIY/edit?slide=id.p1#slide=id.p1), [demo](https://drive.google.com/file/d/1L6o68c4fMHnsKoH0htfM426pgE_lWyrH/view?usp=sharing), [recorded seminar](https://drive.google.com/file/d/137_iZLu-UdhfgToGUhbyZSfjE-bA3W-m/view), [readme](https://github.com/tokamak-network/tokamak-rollup-metadata-repository?tab=readme-ov-file#tokamak-rollup-metadata-repository), [docs](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/tree/main/docs) ) 
    - **Staking:**
      - [TON-total-supply data sheet](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004)  is updated ( 2025.5.31 data)
    - **Staking community version**
      - Implement front-end([commit](https://github.com/tokamak-network/staking-community-version/commit/4d05f5eceafe67448bdd24fd9a7d49e82200ecc4), [reflected issues](https://github.com/tokamak-network/staking-community-version/issues?q=is%3Aissue))
      - Added withdrawal tooltip, improved UX ([figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2264-31001&t=3AKzFAFofK5cqVPT-11))
    - **Tokamak Economics**
      - Attention Test Proof-of-Concept ([notion](/1f3d96a400a38001bb1cf6816d5479b6))
      - Ethereum Foundation Grant Application & Interview ([interview log](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1748462144428949))
      - Tokamak Economics Whitepaper Update Plan ([notion](/207d96a400a380c58b0be1c7d74c22d8), [discussion](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1749706437923769))
    - **DAO Community version**
      - Community version [design](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2462-65405&t=aF5A6WwhDAJCK38a-11) & storyboard ([v1.0](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2342-20335&t=aF5A6WwhDAJCK38a-11), [v2.0](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2455-50222&t=aF5A6WwhDAJCK38a-11), [v3.0](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2549-12347&t=aF5A6WwhDAJCK38a-11), [recording](https://drive.google.com/file/d/1y3BcCKDelSOGRaXZqCyUYm-vK6_ZlBIF/view), [slide](https://docs.google.com/presentation/d/1Oqn1XJ2vGhDwIXjpZ3PZU6snT8vO7pWsi5-cC2qax2Y/edit?slide=id.g3248837fdd2_0_0#slide=id.g3248837fdd2_0_0))
      - Develop The DAO Community Version ( [sample-1](https://github.com/tokamak-network/dao-community-version/tree/main/sample-1), [sample-2](https://github.com/tokamak-network/dao-community-version/tree/main/sample-2), [commits](https://github.com/tokamak-network/dao-community-version/commits/main/), [Test](/209d96a400a38002bae3e5d0701d11d1) )
      - DAO Snapshot upgrade & Bug Fix ([doc](/1edd96a400a380e5ba0cd467712b9636), [progress](/1f3d96a400a3809fb3acfb4e80a69562#1fcd96a400a3804b89c6c67cf95cb887), [internal Audit](/206d96a400a380479c48e7a943e0febe#206d96a400a380cc9a8ff1f9f4a027de), [TestRecord](https://drive.google.com/file/d/18Z19Uo34iq3S7O1j7PUb-pxRLhvJxUmW/view), [Audit Report](https://drive.google.com/file/d/1_3K9uAs0b8xbr5yicTXZldCBRELnlD5K/view))
      - Submit DAO Agenda for patching CandidateAddOnProxy & DAO ([ton staking v2 test after patching](/1dfd96a400a380e69602ce6b7c590782#1dfd96a400a380c39f23eb19a46d9ce2), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/deploy-candidateAndDAO/), [the deploy & agenda document](/214d96a400a380f6adbad8839baf04b6) , [Agenda](https://dao.tokamak.network/#/agenda/15), [Related Issue](https://github.com/tokamak-network/ton-staking-v2/issues/311))
    - **DAO Agenda Metadata Repository**
      - Develop The DAO Agenda Metadata Repository ( [repo](https://github.com/tokamak-network/dao-agenda-metadata-repository), [readme](https://github.com/tokamak-network/dao-agenda-metadata-repository?tab=readme-ov-file#dao-agenda-metadata-repository), [commits](https://github.com/tokamak-network/dao-agenda-metadata-repository/commits/main/), [Test](/20fd96a400a380e4ab70c7f911d8d6db))
      - The DAO Agenda Metadata Repository Seminar ( [ppt](https://gamma.app/docs/DAO-Agenda-Metadata-Repository-n7tbd5u497cwtxv?mode=doc) )
1. **Knowledge**
  - Final demo for Staking V2([recording](https://drive.google.com/file/d/1uA5TL4dS-DkZ_j2Ke30b4ZYTWuYnJwCb/view))
  - Demo for staking community version internal test ([recording](https://drive.google.com/file/d/11jiZpHLrlyhdYpALJLxS4NSQhv3UyuK8/view), [slide](https://docs.google.com/presentation/d/1Y3gl763XvtHY8gc8uj8t_k6HDptMWSt-cubw3oPLCCc/edit?slide=id.g33838c0c649_0_157#slide=id.g33838c0c649_0_157), [notice](https://tokamak-network.slack.com/archives/C07JU4P56MR/p1748247946697019))
  - [TON Analysis Report ](https://github.com/tokamak-network/TON-total-supply/blob/main/docs/README.md): [TON](https://github.com/tokamak-network/TON-total-supply/blob/main/docs/2025-05-31/README.md) , [TON Staking](https://github.com/tokamak-network/TON-total-supply/blob/main/docs/2025-05-31/staking-analysis/TON-Staking-Analysis.md) (Based on Cumulative Statistics as of 2025-05-31) 

## 2-c. The reason why each under

### 2-c-i. List of challenges faced for each under-achieved deliverable

The timeline for Staking & DAO is delayed because there are bottlenecks in both tasks.

- **Staking Community version: **We don’t use the backend in the community version. To load data, we have to depend on RPC calls. We tried to optimize RPC calls, but it was not working well. Because there are for statements when calling the operator's data using an RPC call, it looks like a DDOS. And personal RPC like Infura has less call limit than what the service needs.  
- **DAO Community version:** Due to no-backend architecture. We have to consider how to manage important historical data such as agendas. Most of the historical data is not mandatory. But agendas are very important for DAO. 

### 2-c-ii. List of solved challenges

- **Staking Community version:** We add some kinds of login pages for using Metamask RPC in the community version. Now it can work well.
- **DAO Community version: ** We are using the **DAO Agenda Metadata Repository** for managing agendas

### 2-c-iii. Strategy for unsolved challenges

- All challenges are solved

# 3. Change in next quarter's deliverables

- **DAO Community version for V1:** Concerning how to manage agenda lists, the implementation was delayed. 
- **Staking community version:** Development-related work(implementation, internal test) is done. But we need documentation like [tonstarter](https://github.com/tokamak-network/TONStarter)

# 4. Budget request

## 4-a. (this quarter)Previous budget requested

- 12,000 TON

## 4-b. (next quarter)Next budget request

- 12,000 TON

## 4-c. Gap(Next - Previous) and why?

- There is no Gap

# 5. Change in the road map

## 5-a. Change in the milestone


| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Simple Staking V2** | Propose DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Staking V2 testnet | 1 service |  |
|  | new DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Contracts audit | 4 final reports, 1 blog post, 1 internal report |  |
|  | Launch Simple Staking V2 with DAO candidate and L2 support | 1 service | 2 service + 1 DAO agenda |
| **Community version** | Launch **community version v1.0 + community guide** with Simple Staking V2 support | 1 service with 1 guide |  |
|  | Release TON staking SDK v1.0 with Simple Staking V2 support | 1 code release | 1 code release, 1 service with guide |
| **Integration of Slashing Protocol** | **Release TON staking SDK v2.0** with slashing support | 1 code release |  |
|  | Contracts audit | Final reports, 1 blog post |  |
|  | new DAO agenda for contract upgrade | 1 dao agenda |  |
|  | Launch **community version v2.0 + community guide** with slashing support | 1 service update with 1 guide | 1 code release, 1 service update with guide |
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support for staked TON | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support for staked TON | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

## 5-b. Change in the timeline

| Year-Quarter | Milestone |
| --- | --- |
| 2025-Q1 | - Landing page |
| 2025-Q2 | - Open Simple Staking V2 |
| 2025-Q3 | - DAO 1.0 community version
- Staking community version
- DAO V2: Policy document
- DAO V2: Snapshot test with PoU |
| 2025-Q4 | - Staking V2: Slashing protocol
- Price API V2.0
- Launch PoU on mainnet(SYB) |
| 2026-Q1 | - DAO 2.0 Community version(SYB score + snapshot)
- Addition of fast withdrawal protocol |

- DAO 2.0 Community version(SYB score + snapshot) can be proceed after launch PoU on mainnet