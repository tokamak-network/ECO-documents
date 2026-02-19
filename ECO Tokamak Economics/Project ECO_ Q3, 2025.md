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

- **Published Updated Research on Network Security**: We completed and published an updated research paper on Randomized Attention Test (RAT), which is a cost-efficient way to ensure L2 networks operate honestly. This research includes proof-of-concept demonstrations showing how our economic model can protect the network while reducing operational costs.
- **Developed Security Testing Infrastructure**: We built multiple testing environments (PoC versions) that allow us to experiment with and validate our economic security model in real-world-like conditions. This helps us ensure the system works properly before full deployment.

**Staking V2**

- **Successfully Completed Community Version Transition**: We successfully transitioned our staking service from a centralized model to a community-operated model. This major infrastructure change means the community can now independently run staking services without relying on Tokamak Network's servers.
- **Minimized Disruption During Transition**: Throughout the multi-week transition process, we carefully managed the changeover to minimize the amount of TON that users needed to unstake. This ensured users could continue earning staking rewards with minimal interruption.

![Total Staked TON amount in Q3](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b7fa193a-ebea-46c6-a38d-23dcf28cd2ff/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQQLFORG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T035807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfQDTuz6HaF8mmIb%2F4g9DB2h9Kb90LEkp7lkwiEOSqLgIhALb6bZIHkXkGKf1a%2Fc3SkUZGYhvkm0JS9fk9AYfqh62UKv8DCHQQABoMNjM3NDIzMTgzODA1IgwYz8hNZ6DKk7JqG5Qq3ANnUv6o3rplyYA6pInYZeFmoNOalvS71E48tZfxv4W0mZKIepRtECwIy%2BLPm26OyvOuJqMXynwcKjvSDdnmux%2FrJ9ojdwEz8yCCboef9rzoFqW9yRJ2aaG6ujiufXvNS0BM0AafVEC9JHupo0JlY769HL9ZF10SpGu55nENutvnRdTvN3hfTgMnO1ciJESl4PjdLPuGk4qIoHwtVYCpnpOlkwOKs0%2B%2Be%2FDUQxRuGkVSBZtIxBeYMom9SRjUYClCrBOlEpWrGWal9vEN%2BOSbQLU62q9dOlH1%2B26cqFvsqw7gevFlb5GUZK9uITdTWZswfN%2F7ubh79s9vIBLloKljRho%2BN1BlgdAajP5sl8cmGwaLsNVBNPorubp1qeo9LaKmkHe1wY98LvUK6iGt%2BjVOhUkZXc55IjCJfdWqBjv0fh0%2FkCZmjfL0xvB%2BMWvXcqmsRMb2PpSuAHTO%2FPmUiuDSN3qkN6WE9yAW%2BjDtIyGbGd%2BdJPEEy94o%2F%2FD2F8KpeKxaUfyz8QFej94gq0CTFs6VANEyMJ6yCFQP59cTsjSVpwXxMoMZea%2FkorvfOa0QngwP9om4yWW9Wrm4lEPdJxKDCE2ODpcxF8EeIiO3TbEgVT3Mu7dcBl24D%2B1TpO9zHDDA79nMBjqkAanxJGrnVPSEPtljVw03%2BPsoSPrj2%2FzxKvbSWahI7EsLtyDZKGxu0D2WnkHphX%2BEAonsYNh3663dWLumPcfYIm0l%2BbYc9%2FoTBOuzn9HKyOMQUH5pZVL2ZnQqfd306mBv%2FMneBuaQ0lUiGaLxJcaXmiCz3f2hv%2BHw0mtd7gzdEU0Je47NGG2Ju9yKf%2FRX3nw%2BLD9%2FkPwbFo7zLrHo8ZZH%2Fa80dDAd&X-Amz-Signature=f41d30122763b18cfc545d7e66736df246fcdce552db443e2a714954b98bc0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Tokamak DAO V2**

- **Launched Fully Decentralized DAO Interface**: We released the DAO Community Version - a governance interface that operates without any centralized backend infrastructure. The DAO can now continue functioning even if Tokamak Network's servers go offline, achieving true autonomous governance.
- **Strengthened DAO Security**: We implemented DAO V2 upgrades, including blacklist functionality, cooldown time mechanisms, and improved SafeWallet integration to protect against malicious actors and governance attacks.
- **Improved DAO Operations**: We established a metadata repository system for transparent proposal history and developed tools to streamline multi-signature wallet operations with DAO contracts.

## 2-b. Actual outputs description

### 2-b-i. Deliverable

**Staking**

- **Tokamak Economics**
  - Updated RAT research paper with PoC and cost efficiency [[pdf](http://arxiv.org/abs/2505.24393), [X](https://x.com/tokamak_network/status/1970308337938907344?s=46)]
  - Randomized Attention Test (PoC) : [PoC V1](https://github.com/tokamak-network/optimism/blob/feature/rat-poc-v1/README.md),  [PoC (local testbed)](https://github.com/tokamak-network/optimism/blob/feature/local-setup-rat/op-challenger/scripts/README.md#build-local-network) , [RAT E2E Testing Guide](https://github.com/tokamak-network/optimism/blob/feature/local-setup-rat/op-challenger/scripts/docs/rat-e2e-testing-guide.md) 
- **Simple Staking V2**
  - TON circulation statistics have been updated. [link](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004) 
  - Complete conversion to the community version
    - X post([1](https://x.com/Tokamak_Network/status/1957362665850016009), [2](https://x.com/Tokamak_Network/status/1954801446777483757), [3](https://x.com/Tokamak_Network/status/1952257662927913167)), blog post([link](https://medium.com/tokamak-network/transition-plan-for-the-dao-community-version-c3d68ce64f16))

**Tokamak DAO**

- DAO community version :  [Readme(EN](https://github.com/tokamak-network/dao-community-version/blob/main/sample-1/README.md)/ [KN)](https://github.com/tokamak-network/dao-community-version/blob/main/sample-1/README_KR.md#tokamak-dao-%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0-%EB%B2%84%EC%A0%84-%EC%9B%B9-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98) , [medium](https://medium.com/tokamak-network/transition-plan-for-the-dao-community-version-c3d68ce64f16)1, [medium2](https://medium.com/tokamak-network/empowering-communities-announcing-the-dao-community-web-application-fa190133d7f7), X post([1](https://x.com/Tokamak_Network/status/1966005951737352668), [2](https://x.com/Tokamak_Network/status/1967803877639745623))
  - LLM prompts for DAO Agenda application development. [Readme](https://github.com/tokamak-network/dao-community-version/tree/main/prompts-for-llm#tokamak-dao-community---llm-prompt-collection) 
  - How to use DAO Agenda Contracts via Etherscan [[EN](https://github.com/tokamak-network/TokamakDAO/blob/main/docs/EN/README.md) / [KR](https://github.com/tokamak-network/TokamakDAO/blob/main/docs/KR/README.md)]
- DAO V2
  - Description of the DAO V2 Upgrade [[EN](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/docs/en/dao-v2-en.md)/ [KR](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/docs/kr/dao-v2-kr.md)]
  - Blacklist and CooldownTime Guide [[EN](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/docs/en/blacklist-cooldown-guide-en.md)/ [KR](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/docs/kr/blacklist-cooldown-guide-kr.md)]

### 2-b-ii. Work

1. **Product**
  - **Tokamak Staking**
    - **Staking V2**
      -  TON circulation statistics have been updated. [link](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004) 
    - **Staking community version**
      - Make a repository for documentation(
      - Update Readme([git](https://github.com/tokamak-network/staking-community-version/commit/b13a29925f5914a12d565e89c574eef1ef76cb81))
      - Test SDK in community version([git](https://github.com/cd4761/staking-community-version/commit/64b9a342c1e350de276b8de33f2c39eb1d9e4948))
      - Update SDK([git](https://github.com/tokamak-network/ton-staking-sdk-monorepo/commit/13b0170180d7d507b5a1eb5b8278368df1a6a953))
    - **Tokamak Network Terminal**
      - Implemented Staking tools(stake, unstake, withdrawal, …)([git](https://github.com/hooki/tokamak-network-terminal/commit/a8406fd517f6cd4ce6647abae7f430b74884a692))
    - **Tokamak Economics**
      - Research on the rollup slashing mechanism [[pdf](https://drive.google.com/file/d/1IKwqvzZNHKipEC-d1-RxbzMtPBlH-Nru/view?usp=sharing)]
      - Randomized Attention Test (PoC) : [feature/devnet-working-version](https://github.com/tokamak-network/optimism/tree/feature/devnet-working-version/op-challenger/scripts#local-devnet-development-environment), [feature/devnet-kurtosis-without-cannonn](https://github.com/tokamak-network/optimism/blob/feature/devnet-kurtosis-without-cannon/op-challenger/scripts/README.md#phase-1-challenger-network), [feature/devnet-kurtosis-cannon-cold-start](https://github.com/tokamak-network/optimism/tree/feature/devnet-kurtosis-cannon-cold-start/op-challenger/scripts#-quick-installation), [feature/op-challenger-rat-kurtosis](https://github.com/tokamak-network/optimism/blob/feature/op-challenger-rat-kurtosis/op-challenger/scripts/README.md),  [RAT optimization](https://github.com/tokamak-network/optimism/blob/feature/op-challenger-rat-kurtosis/op-challenger/rat/prompts/RAT_optimized_v1.md#-ratsol-%EB%B2%84%EC%A0%84-%EB%B3%80%EA%B2%BD%EC%82%AC%ED%95%AD-%EC%83%81%EC%84%B8-%EB%B6%84%EC%84%9D), [Re-aggregating gas costs](https://github.com/tokamak-network/optimism/blob/feature/op-challenger-rat-kurtosis/op-challenger/rat/prompts/gas_cost_analysis_methods.md#gas-usage-by-major-function), [rat-poc-v1](https://github.com/tokamak-network/optimism/blob/feature/rat-poc-v1/README.md),  [PoC (local testbed)](https://github.com/tokamak-network/optimism/blob/feature/local-setup-rat/op-challenger/scripts/README.md#build-local-network) , [RAT E2E Testing Guide](https://github.com/tokamak-network/optimism/blob/feature/local-setup-rat/op-challenger/scripts/docs/rat-e2e-testing-guide.md) 
      - TONDisputeGame simple Test on Sepolia: [repo](https://github.com/tokamak-network/DisputeGameTest), [DisputeGame analyze](/232d96a400a380179d93e9655b41679c#23fd96a400a3804792cde999ce824179), [Test Result](/245d96a400a380e8a26ed3fc04c942ae)
      - L2 Projects / Economics Analysis: [survey](/262d96a400a380f7b776e4d7cd224028)
      - Review and revision of Tokamak L2 Whitepaper: analysis
      - Others: [RAT paper quick review](/26ad96a400a380b8bb8ed9e4bcf5d720)
  - **Tokamak DAO**
    - **DAO Community version**
      - DAO community version:  [readme(EN](https://github.com/tokamak-network/dao-community-version/blob/main/sample-1/README.md)/ [KN)](https://github.com/tokamak-network/dao-community-version/blob/main/sample-1/README_KR.md#tokamak-dao-%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0-%EB%B2%84%EC%A0%84-%EC%9B%B9-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98), [gamma](https://gamma.app/docs/Tokamak-DAO-Community-Web-Application-00nnwwwx4gmefsc), [ppt, ](https://docs.google.com/presentation/d/1MjpSqEFh4nqCc05mHGhrS-Cy3xa0p3xJEt1kqB5kBMo/edit?slide=id.p1#slide=id.p1)[video](https://drive.google.com/file/d/1uJpHiO1i6rmCiuVjHHMPUM15n11PxTfU/view), [internal test](/27ad96a400a380d4a876c29aec58e804#27ad96a400a380f0be74c51ed4f69370), [commits](https://github.com/tokamak-network/dao-community-version/commits/main/)
      - LLM prompts for DAO Agenda application development. [repo](https://github.com/tokamak-network/dao-community-version/tree/main/prompts-for-llm#tokamak-dao-community---llm-prompt-collection), [commits](https://github.com/tokamak-network/dao-community-version/commits/main/)
      - Tokamak Network Terminal  : - [PR #12](https://github.com/hooki/tokamak-network-terminal/pull/12): [dao-tools](https://github.com/Zena-park/tokamak-network-terminal/commits/feature/dao-tools)   
      - Organize DAO Agenda issues for the DAO Community version (issues [[1](https://github.com/tokamak-network/ton-staking-v2/issues/316), [2](https://github.com/tokamak-network/ton-staking-v2/issues/317), [3](https://github.com/tokamak-network/ton-staking-v2/issues/318), [4](https://github.com/tokamak-network/ton-staking-v2/issues/319), [5](https://github.com/tokamak-network/ton-staking-v2/issues/313), [6](https://github.com/tokamak-network/ton-staking-v2/issues/320), [7](https://github.com/tokamak-network/ton-staking-v2/issues/321), [8](https://github.com/tokamak-network/ton-staking-v2/issues/322), [9](https://github.com/tokamak-network/ton-staking-v2/issues/315), [10](https://github.com/tokamak-network/ton-staking-v2/issues/314), [11](https://github.com/tokamak-network/ton-staking-v2/issues/33#issuecomment-3209501844), [12](https://github.com/tokamak-network/ton-staking-v2/issues/312)])
    - **DAO Agenda Metadata Repository**
      - Registering DAO Metadata ([doc](/254d96a400a380948ad4c258730aa4d2))
      - register ([11](https://github.com/tokamak-network/dao-agenda-metadata-repository/pull/96), [12](https://github.com/tokamak-network/dao-agenda-metadata-repository/pull/98), [13](https://github.com/tokamak-network/dao-agenda-metadata-repository/pull/100), [14](https://github.com/tokamak-network/dao-agenda-metadata-repository/pull/101), [15](https://github.com/tokamak-network/dao-agenda-metadata-repository/pull/102))
    - **DAO Contract upgrade**
      - Blacklist and CooldownTime script
        - Agenda [[BlackList](/27ad96a400a380d4a876c29aec58e804), [CooldownTime](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/scripts/related-dao/5.cooldownTimeAgenda.js)]
        - MultiSigWallet [[BlackList](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/scripts/related-dao/6.removeblackListMultiSigWallet.js), [CooldownTime](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/scripts/related-dao/7.cooldownTimeMultiSigWallet.js)]
      - **SafeWallet Sign Recovery Upgrade** (Added work at the request of the TRH team)
        - Regarding DAO Contract upgrade : [DAO-ERC1271upgrade](https://github.com/tokamak-network/ton-staking-v2/commits/DAO-ERC1271upgrade), [DAO-ERC1271oneshot](https://github.com/tokamak-network/ton-staking-v2/commits/DAO-ERC1271oneshot), [safeWallet-protocol](https://github.com/tokamak-network/ton-staking-v2/commits/safeWallet-protocol), [Development Background](/276d96a400a3806fa6cadd466b246890), [Develop Detail](/255d96a400a38039a686dd044d4d6663), [1st internal Review](/25bd96a400a3808e8bf0ceaee46c1ca4), [2nd internal Review](/278d96a400a380778b58f05ece93b3fa), [Using SafeWallet Problem](/265d96a400a380b3a187d723050a0109)
        - SafeWallet-script: [1. propose](https://github.com/tokamak-network/safeWallet-ProtocolKit/blob/Self-development/src/1.propose.ts), [2 foundation](http://2.foundationhttps//github.com/tokamak-network/safeWallet-ProtocolKit/blob/Self-development/src/2.foundation_confirm.ts), [3.ContractConfirmAndExecute](https://github.com/tokamak-network/safeWallet-ProtocolKit/blob/Self-development/src/3.DAOContract_confirmAndExecute.ts)
  - **Audit Platform**
    - Deployed PoC version([Link](https://bounty-mu.vercel.app/))

## 2-c. The reason why each under

### 2-c-i. List of challenges faced for each under-achieved deliverable

- **Tokamak Economics**
  - **Fast withdrawal:** We have no idea how to provide FW service yet. We have to find another way to provide liquidity and to incentivize the FW provider.
- **Staking Community Version: **  
  - **Strategic Pivot in Developer Tools**: The originally planned SDK development was reassessed against Tokamak Network's current strategic priorities. We determined that while the SDK remained valuable, a more practical command-line tool would better serve our developer community's immediate needs. This led to the parallel development of Tokamak Network Terminal alongside the SDK, which required additional development time but resulted in more comprehensive developer tool coverage.
- **DAO V2**
  - **Cross-Project Collaboration Challenges**: Collaboration discussions with the SYB project for DAO integration experienced significant delays due to time zone differences and coordination complexity. Asynchronous communication across different time zones made it challenging to maintain momentum and required careful scheduling and documentation to keep the partnership progressing.


### 2-c-ii. List of solved challenges

- **Staking Community version:** SDK & Tokamak terminal will be served 

### 2-c-iii. Strategy for unsolved challenges

- **About Fast Withdrawal**: We will start researching it. Currently, we have no idea about it.
- **DAO V2 & Snapshot: **We try to find a way to use the SYB system for off-chain voting. 

# 3. Change in next quarter's deliverables

### **3-a. Delayed Deliverables**

- **DAO V2: Policy document & DAO V2: Snapshot test with PoU:** We can proceed with these deliverables after getting support from Project SYB. We expected we could get support until this quarter, but we cannot use the current version of the SYB system. Because it doesn’t have sybil resistance when adopting quadratic voting to staked TON.

### **3-b. Updated Deliverables**

- **TON Staking SDK:** It will be opened to the public with the Tokamak Staking Terminal 

### **3-c. Additional Milestone**

- Recover SafeWallet's signer in the DAO
- slashing mechanism release & PoC
- white paper new version release

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
- Layer 2 Challenger (RAT) research
- White paper new version release
- Tokamak Utility Expansion: Contract Audit System |
| 2026-Q1 | - Advanced slashing mechanism release & PoC
- Staking V2: Slashing protocol
- Layer 2 Challenger (RAT) Implementation
- Finalize integrate Challenge game type to Thanos Challenger
- DAO 2.0 Community version(SYB score + snapshot) - after SYB mainnet
- Research of fast withdrawal protocol |
| 2026-Q2 | - Add new game type to Challenger system(research) |

- DAO 2.0 Community version(SYB score + snapshot) can proceed after the launch of PoU on mainnet