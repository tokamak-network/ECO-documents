# 1. Final Goals

-  Project ECO's final goals are twofold:
  1. Design and implement Tokamak Network's economic system—including slashing mechanisms and fast withdrawals—as specified in the [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md). This will enhance L2 security, increase TON and staked TON utility, and strengthen the Tokamak Network DAO's decentralization and security. 
  1. Deploy the Simple Staking & DAO community version and discontinue the hosted frontend and backend services while minimizing any resulting TON withdrawals

## 1-a. Milestone

### A. Tokamak Staking 

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
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support  | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

### B. Tokamak DAO V2 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Improvement of proposal interface** | **Open community version for DAO V1**: Add support for arbitrary code execution | 1 service | 1 service |
| **Testing DAO V2 on testnet** | Testing Snapshot with PoU  | 1 testnet |  |
| **Policy document for DAO V2** | Including Discord based RFC, Snapshot, PoU for sybil-attack | 1 documents |  |
| **Added use of Snapshot and forum** | **Open community version for DAO V2 **: Include new agenda creation via Discord and Snapshot with PoU | 1 service | 1 service, |

### C. Tokamak Network Landing  Page

| Category | Subcategory | Deliverable |
| --- | --- | --- |
| **Landing page** | Open a new landing page  | 1 service |
|  | Open sub-landing page for Protocols  | 1 service update |
| **Price API 2.0** | **Open price API v2.0**: optimize current price API without affecting widely used functions   | 1 service update |

## 1-b. Easy to understand explanation even outside of team and typical community participant (non-technical persons): **The importance of each milestone deliverable, considering the Tokamak Foundation's strategy and the current Tokamak ecosystem**

### **About Tokamak Economics**

Tokamak Economics research is fundamental to building a sustainable and secure L2 ecosystem. Our Randomized Attention Test (RAT) model represents a breakthrough in making network security both effective and cost-efficient. By developing and testing this economic security model, we're ensuring that Tokamak Network can scale while maintaining the highest security standards. This research isn't just academic—it directly informs how we design incentives, penalties, and rewards across the entire ecosystem, making Tokamak competitive with other leading L2 solutions.

### **About Tokamak Staking **

Our transition to the Staking Community Version represents a pivotal shift from centralized service provision to true community empowerment. While we continue to follow our whitepaper's vision of creating a developer-centric staking environment, we've taken it further by eliminating all backend dependencies. The Community Version allows anyone in the ecosystem to independently operate staking services without relying on Tokamak Network's infrastructure. This is crucial for our long-term strategy: building a resilient, censorship-resistant staking ecosystem where the community has full control. Even if Tokamak Network ceases operations, staking services can continue indefinitely through community hosting.

### **About Tokamak DAO**

The DAO Community Version achieves what we believe is the most important milestone for any DAO: genuine autonomy. Traditional DAO interfaces, while enabling on-chain voting, still depend on centralized services for access—creating a fundamental contradiction. Our Community Version solves this by becoming completely self-contained, allowing the community to operate their own governance interfaces. This ensures that democratic participation can never be restricted or censored by any single entity. Combined with enhanced security features (blacklist, cooldown mechanisms) and improved accessibility (Etherscan guides, simulation tools), we're creating a truly resilient democratic institution. This aligns perfectly with the Tokamak Foundation's strategy of progressive decentralization—transitioning from a foundation-led project to a genuinely community-governed ecosystem.

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

# 2. This quarter's outputs

## 2-a. Easy to understand explanation even outside of the team and typical community participant (non-technical persons): How did your team contribute to achieving the milestone this quarter?

**Tokamak Economics**

- 

**Staking V2**

- 

**Tokamak DAO V2**

- 

## 2-b. Actual outputs description

### 2-b-i. Deliverable

**Tokamak Economics**

- **Tokamak Economics**
  - [TON-total-supply data sheet](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004)  is updated 
  - [Tokamak Network Dashboard](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard) Enhancement with TON Staking Metrics ([X](https://tokamak-network.slack.com/archives/C07JU42NK9R/p1765356417343769?thread_ts=1765333228.226249&cid=C07JU42NK9R), [Telegram](https://t.me/tokamak_network/84147), [Discord](https://discord.com/channels/696270789472682034/697032888570609696/1448235106266517544)) 
  - Request [RFC #17](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/17), [PR #330 ](https://github.com/tokamak-network/ton-staking-v2/pull/330/commits/21d21c96aef082c603d11dae1277e4db31229a37): : Add WithdrawalRequestCanceled Event to DepositManager 
  - 

**Tokamak Governance**

- [Tokamak DAO Agenda: A Proposal Culture Built with the Community](https://medium.com/tokamak-network/tokamak-dao-agenda-a-proposal-culture-built-with-the-community-0b0b72bac6c1) Medium Post
- Sample [RFC#11](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/11) provided ([X](https://x.com/Tokamak_Network/status/1990709415121727860), [Telegram](https://t.me/tokamak_network/83800), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1438776269000015882)) : Create a sample based on the passed Agenda 14
- Request [RFC#12](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/12) ([X](https://x.com/Tokamak_Network/status/1991764654968959411), [Telegram](https://t.me/tokamak_network/83802), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1439861794817577000)) : DAO Contract Upgrade for DAO Lifecycle Enhancement and Bug Fixes
- Request [RFC#13](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13) ([X](https://x.com/Tokamak_Network/status/1996107770647773630), [Telegram](https://t.me/tokamak_network/83803), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1440229027678785666)) : Added signature verification function to DAO contracts
- gitbook changes to official documentation ([EN](https://docs.tokamak.network/home/service-guide/tokamak-network-dao), [KOR](https://docs.tokamak.network/home/kor/service-guide/tokamak-network-dao)) : Update on the changed agenda creation process & DAO-related page renewal

### 2-b-ii. Work

1. **Product**
**Tokamak Economics**

  - **Tokamak Economics**
    - Basic slashing mechanism release & PoC
      - Contract design for developing a basic slashing mechanism ([ppt](https://docs.google.com/presentation/d/168dRYgyJdSP45wOUGMbTC2e7qSGTNXQBy-myAxthApU/edit?slide=id.g39e0ef9ec83_0_0#slide=id.g39e0ef9ec83_0_0), [seminar](https://drive.google.com/file/d/1peN_2568Jn_kXuJSi8clRqHkeYSe4SzH/view))
      - discussion on slashing policy ([notion](/2a1d96a400a380f186dceabf24750bbb), [meeting](https://drive.google.com/file/d/1GMtSgBhVyn-mrDK8btlGwLa1bP0eTWlR/view))
      - cleanup the Slashing policy ([notion](/2a7d96a400a3805c940fcf5db44e6e17))
      - Change the development environment to foundry ([branch](https://github.com/tokamak-network/ton-staking-v2/tree/25-Q4-slashing-foundry))
      - Basic logic development ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/25-Q4-slashing-foundry/))
    - Assess the current tokenomics situation
      - Define Key Metrics** **: [notion](/2a9d96a400a380e9bce5e186a8bd9bc4) 
      - Develop the basic staking metrics aggregator: [readme](https://github.com/tokamak-network/tools/tree/aggregate_staking_metrics/aggregate_staking_metrics#tokamak-network-basic-staking-metrics-aggregator), [commits](https://github.com/tokamak-network/tools/commits/aggregate_staking_metrics/) 
      - Develop [Dune Queries](https://dune.com/workspace/t/project_eco_test/library/queries), [Test Dashboard ](https://dune.com/project_eco_test/test1). [notion](/2b5d96a400a3803ab96fda7ca8816eba#2b7d96a400a38022aba2eac9938fbfb6)
      - notice [X](https://tokamak-network.slack.com/archives/C07JU42NK9R/p1765356417343769?thread_ts=1765333228.226249&cid=C07JU42NK9R), [Telegram](https://t.me/tokamak_network/84147), [Discord](https://discord.com/channels/696270789472682034/697032888570609696/1448235106266517544)
      - Request [RFC #17](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/17), [PR #330 ](https://github.com/tokamak-network/ton-staking-v2/pull/330/commits/21d21c96aef082c603d11dae1277e4db31229a37): : Add WithdrawalRequestCanceled Event to DepositManager 
    - Research Challenger System   
      - Challenger System Architecture Analysis [EN](https://github.com/tokamak-network/tokamak-thanos/blob/feature/challenger-gametype3/op-challenger/docs/challenger-system-architecture.md) / [KR](https://github.com/tokamak-network/tokamak-thanos/blob/feature/challenger-gametype3/op-challenger/docs/challenger-system-architecture-ko.md)   
      - Integrated Challenger GameType 2 (Asterisc) and GameType 3 (Asterisc-Kona) into Tokamak-Thanos (PoC on Local).  Readme: [EN](https://github.com/tokamak-network/tokamak-thanos/blob/feature/challenger-gametype3/op-challenger/scripts/README.md) / [KR](https://github.com/tokamak-network/tokamak-thanos/blob/feature/challenger-gametype3/op-challenger/scripts/README-KR.md), [commits](https://github.com/tokamak-network/tokamak-thanos/commits/feature/challenger-gametype3/) 
      - develop the e2e tests in optimism [readme](https://github.com/tokamak-network/optimism/blob/feature/challenger-game-type-check/op-challenger/scripts/docs/test-cases/README.md),  [cannon](https://github.com/tokamak-network/optimism/blob/feature/challenger-game-type-check/op-challenger/scripts/docs/test-cases/faultproofs-cannon-test-report-en.md#fault-proofs-cannon-test-report) , [asterisc](https://github.com/tokamak-network/optimism/blob/feature/challenger-game-type-check/op-challenger/scripts/docs/test-cases/faultproofs-asterisc-test-report-en.md#asterisc-fault-proofs-test-report)
      - [bond cost analysis](https://github.com/tokamak-network/optimism/blob/feature/challenger-game-type-check/op-challenger/scripts/docs/test-cases/bond-cost-measurement-report-en.md#output-cannon-bond-cost-measurement---test-analysis-report) for Challenger System (Dispute Game)
      - feature/challenger-game-type-check: [commits](https://github.com/tokamak-network/optimism/commits/feature/challenger-game-type-check/)
      - BOLD challenge system code analysis: [draft](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1764669424097319), [notion](/2cfd96a400a380afabf5cb268295e8b0)
    - Writing a Tokamak Network Contract Specification
      - [Tokamak Network Contracts](/2bed96a400a380058418f4d67661ba5c)
      - the [specification](https://docs.google.com/spreadsheets/d/14tDP6pKdwN-boIUCisFzA8ggCNxSBHYwK7AZadDwbRs/edit?gid=1527791472#gid=1527791472) on tokamak network contracts 
    - White paper development specification
      - White paper development: [specification](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v3/dev/docs/specs-kr/readme.md#ton-staking-v3-system-specification)
      - Developing Staking V3: [readme](https://github.com/tokamak-network/ton-staking-v2/tree/ton-staking-v3/dev?tab=readme-ov-file#ton-staking-v3) [commits](https://github.com/tokamak-network/ton-staking-v2/commits/ton-staking-v3/dev/) 
    - Writing the new version of L2 tokenomics white paper
      - Survey on the shared validators set concept: ppt, seminar
      - Designing the new structure of L2 tokenomics white papar: [notion](/2a2d96a400a38000a2d7fb16b2e7ab78)
      - Drafting Tokenomics design: [notion](/286d96a400a38012a496d43965b05e8f)
      - Collecting and organizing white paper [feedbacks](/2c3d96a400a38083b842e09fdb50b19f)
      - Writing the updated version of L2 tokenomics white paper: [overleaf](https://www.overleaf.com/project/68de1e8ef6e2f12217be4a9a)
    - Tokamak Network MCP
      - Core functionality development completed (wrap / unwrap / staking / unstaking): [github](https://github.com/tokamak-network/tokamak-network-mcp)
      - WEB UI style changed to Windows style

**Tokamak Governance**

  - Introducing RFC steps to DAO
    - Discussion about isValidSignature ([doc](/28bd96a400a3800fbc12ff5cb57a6362))
    - Apply the new format when before submitting the DAO Agenda ([doc](/28cd96a400a380218b9fe81b16606316))
    - Creating a template for writing RFCs ([Template](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/new?category=discussion-rfc))
    - Added TokamakDAO candidate registration section ([candidate_registration](https://github.com/tokamak-network/TokamakDAO/commit/a1584ef53f65ee3dcf78bb0878d941ab7edfc923))
    - gitbook changes to official documentation ([EN](https://docs.tokamak.network/home/service-guide/tokamak-network-dao), [KOR](https://docs.tokamak.network/home/kor/service-guide/tokamak-network-dao)) : Update on the changed agenda creation process & DAO-related page renewal
    - Medium Post : [Tokamak DAO Agenda: A Proposal Culture Built with the Community](https://medium.com/tokamak-network/tokamak-dao-agenda-a-proposal-culture-built-with-the-community-0b0b72bac6c1) 
    - announcement about Discussion channel ([announcement](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/15))
    - Sample [RFC#11](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/11) provided ([X](https://x.com/Tokamak_Network/status/1990709415121727860), [Telegram](https://t.me/tokamak_network/83800), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1438776269000015882))
    - Request [RFC#12](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/12) ([X](https://x.com/Tokamak_Network/status/1991764654968959411), [Telegram](https://t.me/tokamak_network/83802), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1439861794817577000))
  - Designing a New DAO Architecture
    - discussion on the overall direction ([Doc](https://docs.google.com/presentation/d/1w8k59HVo6191nxmQq1AH5FO7OiEiHMrsH3qpUA6frnk/edit?usp=sharing))
  - DAO upgrade
    - finish Internal Review ([Report](/29cd96a400a380caa213f645727901c2))
    - DAO Committee Contract Code Review to Support SafeWallet ([slack](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1765358870011899),[Apply](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13#discussioncomment-15323920))
    - Request [RFC#13](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13) ([X](https://x.com/Tokamak_Network/status/1996107770647773630), [Telegram](https://t.me/tokamak_network/83803), [Discord](https://discord.com/channels/696270789472682034/1430107114071789620/1440229027678785666))
    - feedback on the Discussion ([comment](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13#discussioncomment-15072623))
    - apply the feedback on the discussion ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/safeWallet-protocol/)[Nov 28~Dec 2], [test](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/test/SafeWalletGovernanceValid.test.ts))
    - SafeWallet transaction execute test ([doc](/2bdd96a400a3808c9619f49c276e99f3), [commits](https://github.com/tokamak-network/safeWallet-ProtocolKit/commits/Self-development/)[Dec])
    - preparing to create to agenda ([mainnet](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/14.createAgendaAboutRFC13_Mainnet.js), [sepolia](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/15.createAgendaAboutRFC13_Sepolia.js), [Create Tx on sepolia](https://sepolia.etherscan.io/tx/0xbce5f0740d3685521eaed28aeb910385be1d44f34f0e167c1333d6888f55fecf))

## 2-c. The reason why each under

### 2-c-i. List of challenges faced for each under-achieved deliverable

- **Tokamak Economics**
  - We attempted to implement RAT in the Thanos environment, but since the Thanos system does not support challengers, we were unable to apply RAT. Therefore, we forked the Optimism Repository, implemented the RAT system, and researched the challenger system.
- **Staking Community Version: **  
  - 
- **DAO V2**
  - 


### 2-c-ii. List of solved challenges

- 

### 2-c-iii. Strategy for unsolved challenges

- 

# 3. Change in next quarter's deliverables

### **3-a. Delayed Deliverables**

- 

### **3-b. Updated Deliverables**

### **3-c. Additional Milestone**

- 

# 4. Change in the road map

## 4-a. Change in the milestone

### **A. Tokamak Staking**

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
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

### B. Tokamak DAO V2 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Improvement of proposal interface** | **Open community version for DAO V1**: Add support for arbitrary code execution | 1 service | 1 service |
| **Testing DAO V2 on testnet** | Testing Snapshot with PoU  | 1 testnet |  |
| **Policy document for DAO V2** | Including Discord based RFC, Snapshot, PoU for sybil-attack | 1 documents |  |
| **Added use of Snapshot and forum** | **Open community version for DAO V2 **: Include new agenda creation via Discord and Snapshot with PoU | 1 service | 1 service, |
| **DAO upgrade** | Recover SafeWallet's signer in the DAO | 1 code release
1 dao Agenda |  |

### C. Tokamak Network Landing  Page

- No changed milestone

### **D. Tokamak Economics R&D**

| **Category** | **Subcategory** | **Delivarable** |
| --- | --- | --- |
| **Economics Whitepaper Update** | - | 1 paper |
| **Validator Economics** | Randomized Attention Test | 1 paper, 1 codebase |
|  | Slashing Mechanism | 1 paper, 1 codebase |

## 4-b. Change in the timeline

| Year-Quarter | Milestone |
| --- | --- |
| 2025-Q1 | - Landing page |
| 2025-Q2 | - Open Simple Staking V2 |
| 2025-Q3 | - DAO 1.0 community version
- Staking community version |
| 2025-Q4 | - Launch PoU on mainnet(SYB)
   - DAO V2: Snapshot test with PoU
- Price API V2.0
- DAO V2: Publish Policy document(without snapshot)
- DAO upgrade : Recover SafeWallet's signer in the DAO
- Basic slashing mechanism release & PoC
- Layer 2 Challenger (RAT) System
- White paper new version release
- Tokamak Utility Expansion: Contract Audit System |
| 2026-Q1 | - Advanced slashing mechanism release & PoC
- Staking V2: Slashing protocol
- Finalize integrate Challenge game type to Thanos Challenger
- DAO 2.0 Community version(SYB score + snapshot) - after SYB mainnet
- Research of fast withdrawal protocol |
| 2026-Q2 | - Add new game type to Challenger system(research) |

- DAO 2.0 Community version(SYB score + snapshot) can proceed after the launch of PoU on mainnet