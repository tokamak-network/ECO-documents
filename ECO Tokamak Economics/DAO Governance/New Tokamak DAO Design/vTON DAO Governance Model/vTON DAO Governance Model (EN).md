## 1. Overview

This document defines the DAO governance model for Tokamak Network. Based on the Verification Economics and TON Staking V3 model presented in the Tokamak Network Economics Whitepaper V2, we establish a decentralized decision-making structure. The following core design principles are applied:

- Separation of TON and vTON roles prevents conflicts between economic and governance functions.
- Structural limitations on voting power concentration prevent governance capture by a minority.
- The Security Council enables rapid response to emergencies while preventing abuse of authority.

## 2. TOKEN (vTON)

### 2.1 vTON Definition

vTON is the governance token of Tokamak Network. TON handles economic utility (gas, collateral, bridge), while vTON is used for voting rights. The separation of the two tokens' roles prevents conflicts between economic and governance functions.

### 2.2 vTON Distribution

vTON is distributed to seigniorage recipients according to their seigniorage ratio. Seigniorage is received by three entities: L2 Operators, Validators, and DAO Treasury. However, vTON is distributed only to L2 Operators and Validators.

| Recipient | Seigniorage (TON) | vTON |
| --- | --- | --- |
| L2 Operator (Sequencer) | ✓ | ✓ |
| Validator | ✓ | ✓ |
| DAO Treasury | ✓ | ✗ |

The DAO Treasury receives seigniorage but not vTON. The Treasury's primary purposes are economic expenditures such as ecosystem grants, operational costs, liquidity provision, and emergency response, which are covered by TON. Since vTON represents voting rights, if the Treasury held vTON, it would create unnecessary complexity requiring another vote to determine "who exercises those voting rights on its behalf." The Treasury's role is to store and manage funds, not to make decisions itself, so excluding vTON is appropriate.

### 2.3 Issuance Method

An unlimited issuance method is adopted. However, the DAO can adjust the vTON issuance ratio relative to seigniorage, with this ratio settable from a minimum of 0 to a maximum of 1. Setting it to 0 means no additional vTON issuance occurs with seigniorage.

| Parameter | Initial Value | Range | Description |
| --- | --- | --- | --- |
| vTON Issuance Ratio | 1 | 0 ~ 1 | vTON issuance ratio relative to seigniorage |

### 2.4 Tradeable

vTON is tradeable. Instead of delegating directly to a delegator, vTON holders can sell their vTON to other participants who need voting power. This allows holders uninterested in governance participation to realize economic value, while those seeking active governance participation can acquire voting power in the market.

### 2.5 Not-burnable

vTON is not burned when voting. Voting is not an act of consuming tokens but an exercise of authority based on holdings. If vTON were burned with each vote, holders would only vote on important matters, hindering routine governance participation.

## 3. VOTING MECHANISM

### 3.1 Delegation

Governance proposals require diverse expertise including technical complexity, economic impact, and security considerations. It is realistically difficult for all vTON holders to have sufficient time and expertise to thoroughly review each proposal. Delegation solves this problem. Holders delegate their voting rights to trusted experts, and delegators analyze proposals and participate in decision-making based on the delegated voting power.

### 3.2 Delegator Registration

To become a delegator, the following information must be publicly registered:

- Profile (identity or pseudonym)
- Voting philosophy and decision-making criteria
- Interests (affiliations, investment portfolio, consulting relationships, etc.)

This requirement deters Sybil attacks. While creating multiple anonymous wallets is easy, earning community trust as a delegator to receive delegation is difficult. Additionally, interest disclosure prevents issues like the Optimism Griff Green conflict of interest incident (2024).

### 3.3 Delegation Method

vTON holders cannot vote directly and must delegate to a delegator. Undelegated vTON cannot be exercised as voting rights.

To exercise voting rights directly, one must register as a delegator, and the same registration requirements apply. Operators and Validators must also delegate the vTON received through seigniorage to a delegator. They can register themselves as delegators and delegate to themselves, or delegate to other delegators.

Delegation can be withdrawn (undelegated) at any time and re-delegated to another delegator.

### 3.4 Delegation Rules

The DAO can set the following rules to prevent voting power concentration:

| Rule | Initial Value | Description |
| --- | --- | --- |
| Delegation Cap | 20% | Maximum percentage of vTON each delegator can receive (relative to total supply) |
| Delegation Auto-Expiry | No limit | Delegation maintenance period. Re-delegation required after expiry |

Delegations exceeding the cap are rejected. This fundamentally blocks any single delegator from accumulating excessive voting power. When delegation auto-expiry is set, holders periodically reconsider the delegator's activities and voting tendencies. These settings can be changed through DAO voting.

### 3.5 Voting Power Calculation

Each time vTON is delegated to a delegator, that timestamp is recorded on-chain. On-chain voting rights are only granted to vTON that has been delegated at least 7 days before the snapshot.

| Parameter | Initial Value | Description |
| --- | --- | --- |
| Delegation Period Requirement | 7 days | Minimum delegation period for on-chain voting rights recognition (from snapshot) |

**Snapshot-based Voting Power Determination**

```
Proposal Creation (Block #1000) ← Snapshot Point
        │
        ▼
On-chain Voting Starts (Only delegations from 7+ days before snapshot recognized)
        │
        ▼
Delegation after snapshot or 6 days prior → No voting rights for this proposal

```

This design defends against the vulnerability exploited in the Beanstalk Flash Loan attack (2022). In that attack, no snapshot was applied, allowing immediate voting with just-acquired tokens. By adding the delegation period requirement, mass accumulation attacks just before the snapshot are fundamentally blocked. This setting can be changed through DAO voting.

### 3.6 Proposal Creation

TON burning during proposal creation prevents spam. Burned TON is permanently removed, economically deterring proposal abuse. The amount can be changed through DAO voting.

| Parameter | Initial Value | Description |
| --- | --- | --- |
| Proposal Creation Cost | 100 TON | TON burned when creating a proposal |

### 3.7 Voting Period

The process follows these stages: RFC (7+ days) → Snapshot Vote (5 days) → Review Period (3 days) → On-chain Vote (7 days) → Timelock (7 days) → Execution.

| Stage | Duration | Purpose | Activity |
| --- | --- | --- | --- |
| RFC | Minimum 7 days | Community feedback collection | Draft writing, feedback incorporation |
| Snapshot Vote | 5 days | Determine on-chain progression | Off-chain yes/no vote |
| Review Period | 3 days | Snapshot preparation, delegation adjustment | Proposal finalization, delegation changes |
| On-chain Vote | 7 days | Final execution approval | Yes/No/Abstain vote |
| Timelock | 7 days | Emergency response, security review | Security Council review |

### 3.8 Quorum

For a vote to be valid, a minimum quorum of total delegated vTON must participate. Proposals that fail to meet quorum are automatically rejected.

### 3.9 Pass Rate

If quorum is met and approval exceeds the passing threshold, the proposal passes. Abstentions are included in quorum calculation but not in pass/fail determination.

| Parameter | Initial Value | Description |
| --- | --- | --- |
| Quorum | 4% | Minimum vTON percentage required to participate (relative to total delegated vTON) |
| Pass Rate | Majority | Approval ratio required for proposal passage when quorum is met |

These settings can be changed through DAO voting.

## 4. SECURITY COUNCIL

The Security Council can bypass the governance process to take emergency measures. When hacks or critical bugs are discovered, waiting 7+ days for voting is not feasible.

### 4.1 Member Count and Execution Threshold

Major L2 protocols typically have Security Councils with 8 or more members. Arbitrum operates with 12 members (9/12 threshold), Optimism with 13 members (10/13 threshold), and L2Beat recommends a minimum of 8 members with a threshold exceeding 75% for Stage 1 requirements.

Tokamak Network's initial Security Council consists of 3 members: 1 from the Foundation and 2 external partners. Since externals hold the majority, the Foundation cannot make unilateral decisions. This is a minimum configuration suitable for the project's early stage, with plans to gradually expand to industry standard levels as the network grows.

| Category | Initial Configuration |
| --- | --- |
| Total Members | 3 |
| Foundation | 1 |
| External Partners | 2 |
| Execution Threshold | 2/3 (67%) |

### 4.2 Authority

The Security Council has the following powers:

| Power | Description |
| --- | --- |
| Malicious Proposal Cancellation | Can reject proposals waiting in Timelock |
| Emergency Upgrade | Can immediately upgrade contracts when security vulnerabilities are discovered |
| Protocol Pause | Can halt protocol functions during emergencies |

These powers are executed immediately, bypassing the normal governance process. However, all emergency measures must be disclosed to the community afterward.

### 4.3 External Partners

Initial external partners are appointed by the Foundation. As the DAO grows, the selection method will transition to DAO voting. Qualification requirements for external partners will be defined through DAO governance in the future.

### 4.4 Term

Initial Security Council members have no set term. However, terms can be established through DAO governance.

### 4.5 Removal Procedure

Changes to Security Council members (removal and election) are decided through DAO voting. However, the Security Council cannot exercise veto power over proposals related to the Security Council itself, and the Foundation executes according to DAO voting results.

## 5. DAO Parameters

The following parameters can be adjusted through DAO voting:

| Category | Parameter | Initial Value | Range/Description | Related Section |
| --- | --- | --- | --- | --- |
| Token Issuance | vTON Issuance Ratio | 1 | 0 ~ 1 | 2.3 |
| Delegation | Delegation Cap | 20% | Relative to total supply | 3.4 |
| Delegation | Delegation Auto-Expiry | No limit | In days | 3.4 |
| Voting Power | Delegation Period Requirement | 7 days | From snapshot | 3.5 |
| Proposal | Proposal Creation Cost | 100 TON | Burned | 3.6 |
| Voting | Quorum | 4% | Relative to total delegated vTON | 3.8 |
| Voting | Pass Rate | Majority | Approval/(Approval+Rejection) | 3.9 |
| Security Council | Member Count | 3 | - | 4.1 |
| Security Council | Execution Threshold | 2/3 (67%) | - | 4.1 |
| Security Council | Term | No limit | Days/years | 4.4 |

## Appendix: DAO Governance Attack Case Analysis

This appendix systematically organizes major DAO governance attacks and issues that have occurred in the blockchain ecosystem. Each case serves as the basis for defense mechanisms in the Tokamak Network vTON DAO design.

**Case Summary Table**

| # | Protocol | Year | Attack Type | Damage | Key Details |
| --- | --- | --- | --- | --- | --- |
| 1 | Beanstalk | 2022 | Flash Loan | $182M | Acquired 67% with $1B loan, proposal-vote-execute-drain in single block |
| 2 | Aragon | 2023 | Treasury Drain | $155M | Market cap < Treasury arbitrage. Accumulated 47% over 45 days, forced liquidation |
| 3 | Radiant | 2024 | Multisig Takeover | $50M | Only 3 of 11 signatures needed. Malicious PDF compromised exactly 3 signers |
| 4 | Compound | 2024 | Voting Power Concentration | $24M | Single entity accumulated 81% of quorum (325K COMP), passed proposal allocating funds to own vault |
| 5 | Balancer | 2022 | Emission Manipulation | $1.8M | Acquired 35% veBAL, directed excessive token emissions to low-volume pool |
| 6 | Build Finance | 2022 | Hostile Takeover | $470K | Disabled notification systems, submitted proposal, passed with 0 opposition votes |
| 7 | Uniswap | 2020-24 | Delegation Concentration | - | Gini coefficient 0.881→0.943 over 4 years, 88% decrease in participants |
| 8 | Optimism | 2024 | Conflict of Interest | - | Delegate supported consulting clients without disclosing relationship |
| 9 | Arbitrum | 2024-25 | Incentive Failure | - | Retroactive rule changes reduced active delegates from 49 to 21 |
| 10 | Aave | 2024 | Timing Manipulation | - | Forced brand ownership proposal during Christmas holiday |

**1. Beanstalk Flash Loan Attack (2022)**

On April 17, 2022, the most sophisticated governance attack in history occurred at Beanstalk. The attacker submitted two malicious proposals (BIP-18, BIP-19) and waited for the 24-hour emergency proposal period. Then everything was executed within a single transaction. After borrowing over $1B via Flash Loans from Aave, Uniswap, and SushiSwap, the tokens were deposited into Beanstalk's "Silo" to generate governance tokens. This secured 67% voting power, meeting the supermajority requirement for emergency execution. The malicious proposals were passed and immediately executed, draining $182M before repaying the Flash Loan. The entire process was completed within a single block. The key vulnerability was that the `emergencyCommit` function allowed voting and execution in the same block. Additionally, no snapshot was applied to voting power calculation, allowing immediate voting with just-acquired tokens.

**Lesson**: Voting power must be calculated based on snapshots at proposal creation. Voting and execution must be separated, and a grace period for newly acquired tokens is necessary.

**2. Aragon "RFV Raiders" Attack (2023)**

Aragon had a structural vulnerability. Its market cap was approximately $129M, but the Treasury held $177-200M. Buying all tokens and liquidating the Treasury would yield a profit. An attacker group called "RFV Raiders" identified this. Over approximately 45 days, they infiltrated Discord to monitor community trends while quietly accumulating ANT tokens from the market. Through token wrapping, they secured over 47% voting power and prepared a proposal for full Treasury liquidation. Eventually, the Aragon Association decided to dissolve the project, disbursing a total of $155M at a rate of 0.0025376 ETH/ANT. The attackers effectively achieved their goal.

**Lesson**: When Treasury size exceeds market cap, it becomes a target for "legitimate plunder." Treasury withdrawal caps, tiered quorums, and long-term accumulation monitoring are essential.

**3. Radiant Capital Key Theft (2024)**

In October 2024, $50M was stolen from Radiant Capital. This incident demonstrates the fundamental pitfall of multisig design. Radiant had 11 signers, but only 3 signatures were needed for execution (3/11 = 27%). The attacker distributed a PDF file containing malware and compromised exactly 3 signers. That was sufficient. They gained control of the multisig wallet and stole $50M. The number 11 was meaningless. If only 3 could be compromised, that was the end. Following this incident, L2Beat recommended a minimum of "8 or more signers with a threshold of 75% or higher" for Security Councils.

**Lesson**: Multisig security depends more on threshold than number of signers. The threshold must be at least 70-75% to provide meaningful security. A structure that can be breached by compromising just 3 people is meaningless even with 11 members.

**4. Compound "Golden Boys" Attack (2024)**

In July 2024, an attacker known as "Humpy" began systematically withdrawing COMP tokens from the Bybit exchange. The final accumulated amount was 325,333 COMP, representing 81% of Compound's quorum requirement of 400,000 COMP. After two failed proposals, Humpy submitted Proposal 289. The proposal content was to allocate $24M worth of COMP to a "goldCOMP" vault under his control. Targeting weekend timing when delegate response was difficult, the vote proceeded, with a final result of 682,191 for versus 633,636 against (51.84%), passing. Through urgent community coordination, negotiations with Humpy occurred, and while the fund allocation was executed, it triggered discussions on future governance improvements.

**Lesson**: Quorum is merely a "minimum participation requirement" and does not limit the influence of large holders. Voting power caps for single entities and weekend/holiday blackout periods are necessary.

**5. Balancer veBAL Concentration Attack (2022)**

The same attacker Humpy from the Compound attack was also active at Balancer. He accumulated 35% of total veBAL and manipulated Gauge voting. He directed BAL token emissions to a low-volume CREAM/WETH pool under his control. The results were extreme. The pool generated only $17,846 in protocol revenue over 6 weeks but received $1.8M in BAL emissions during the same period. The revenue-to-emission ratio was approximately 100:1. Balancer DAO subsequently introduced Gauge Framework V1, setting a maximum emission cap of 10-15% for single pools, and concluded a "peace agreement" with Humpy.

**Lesson**: For systems based on seigniorage or token emissions, emission caps and mechanisms linking to protocol revenue are essential. Devices limiting veToken concentration itself should also be considered.

**6. Build Finance DAO Hostile Takeover (2022)**

The Build Finance attack was simple yet fatal. The attacker (ENS: Suho.eth) first disabled the proposal notification bot and gitbook documentation. This created a situation where the community could not be aware of new proposals. In that state, a governance takeover proposal was submitted. Since no one knew of the proposal's existence, there were 0 opposition votes, and the proposal passed as-is. Approximately $470,000 of the entire Treasury was stolen. The attacker claimed to have "only acted according to the rules," and the protocol was effectively terminated. This case starkly revealed the limits of Code is Law.

**Lesson**: Timelocks, minimum voting participation requirements, and multiple notification systems are not optional but mandatory. Single points of failure must be eliminated.

**7. Uniswap Delegation Concentration (2020-2024)**

Academic research analyzing 21,791 Uniswap voters and 68 governance proposals over 4 years revealed unintended side effects of the delegation system. Before delegation introduction, the Gini coefficient of voting power distribution was 0.881. Four years later, this figure rose to 0.943. Inequality increased by 6.6%. Average participants per proposal decreased from 503 to 267, an 88% decrease. The top 1% controlled 47.5% of total voting power, and for technical proposals, concentration reached 99.97%, effectively a monopoly. The psychological effect of "someone else will do it" is analyzed as a factor. There was no delegation cap, no measures against inactive delegates, and the phenomenon of concentration toward large delegates intensified.

**Lesson**: Contrary to the intention of increasing participation, delegation can actually intensify inequality and apathy. Complementary measures such as delegation caps, activity requirements, and auto-expiry are necessary.

**8. Optimism Griff Green Conflict of Interest (2024)**

Griff Green was a major Delegate at Optimism. He was also the founder of Giveth and co-founder of General Magic. The problem emerged during the grant review process. Green supported projects that were his consulting clients. The consulting structure charged 7-50% fees on grant amounts. However, Green did not disclose this conflict of interest relationship before voting. After community debate, a ruling of "no practical harm since it wasn't a marginal vote" was made. However, this incident led Optimism to introduce mandatory conflict of interest disclosure rules and implement the Badgeholder Conflict of Interest Disclosure system.

**Lesson**: Delegate conflict of interest disclosure must be mandatory, not optional. Enforcement mechanisms such as invalidating votes without prior disclosure are necessary.

**9. Arbitrum Delegate Incentive Program Failure (2024-2025)**

Arbitrum DAO introduced a $1.5M annual incentive program to encourage delegate participation. Initially, there was an effect of increasing active delegates. The problem arose with version 1.6/1.7 updates. Retroactive rule changes were implemented. Entry barriers were raised 10x (50K → 500K ARB), and delegate rewards were cut by approximately 40%. Meanwhile, program administrator rewards increased by 25%. Large inactive delegates were left alone, and rules disadvantageous to small delegates were applied. The results were dismal. Active delegate count dropped from 49 in December 2024 to 21 in February 2025, a 57% decrease. The community raised criticism calling it a "patronage system," and proposals to revert to v1.5 are under discussion.

**Lesson**: Delegate incentives must be clear and predictable. Retroactive rule changes destroy trust. Entry barriers and reward structures must be balanced.

**10. Aave Labs Christmas Vote Controversy (2024)**

In December 2024, Aave Labs submitted a proposal for "Aave" brand ownership transfer. After only 5 days of forum discussion, it was pushed to Snapshot voting. The vote stage was reached without the proposal author's consent. The voting period was December 23-26. It coincided exactly with Christmas holidays. To make matters worse, founder Stani Kulechov purchased $10-15M worth of AAVE just before the vote. Criticism of "hostile takeover attempt" was raised. The proposal was ultimately rejected. The final tally was 55.29% against, 41.21% abstain, 3.50% for, with a record 1.8 million AAVE participating in the vote. This shows how strong the community backlash was.

**Lesson**: Blackout periods prohibiting major proposals around major holidays, author consent requirements, and mandatory minimum discussion periods are necessary. Timing manipulation distorts participation rates and undermines governance legitimacy.

**References**

1. [*DeSpread Research, "The Compound Finance Governance Attack: A Recap and Its Implications" (2024)*](https://research.despread.io/compound-finance-governance-attack/)
1. [*Messari, "Governor Note: The veBAL Wars" (2022)*](https://messari.io/report/governor-note-the-vebal-wars)
1. [*Blockworks, "Arca Offers Their 2 Cents on Aragon DAO Attack Allegations" (2023)*](https://blockworks.co/news/arca-aragon-dao-attack-allegations)
1. [*The Block, "Build Finance DAO suffers 'hostile governance takeover'" (2022)*](https://www.theblock.co/post/134180/build-finance-dao-suffers-hostile-governance-takeover-loses-470000)
1. [*PANews, "A Study of Uniswap On-Chain Voting: Implications for Power, Apathy, and Evolution" (2024)*](https://www.panewslab.com/en/articles/7c66f3fa-b71d-4fa0-898d-243cf083e8a8)
1. [*DL News, "Griff Green's disclosure 'mistake' sparks heated debate among Optimism DAO" (2024)*](https://www.dlnews.com/articles/defi/green-offers-mea-culpa-to-optimism-dao-over-grants-disclosure/)
1. [*The Defiant, "Arbitrum DAO Votes on $1.5 Million Program to Reward Active Delegates" (2024)*](https://thedefiant.io/news/blockchains/arbitrum-dao-votes-on-usd1-5-million-program-to-reward-active-delegates)
1. [*Arbitrum Proposals, "Revert the Delegate Incentive Program (DIP) to Version 1.5" (2025)*](https://forum.arbitrum.foundation/t/proposal-revert-the-delegate-incentive-program-dip-to-version-1-5/29867)
1. [*DL News, "Aave Labs critics lose key DAO vote — for now" (2024)*](https://www.dlnews.com/articles/defi/aave-labs-critics-lose-key-dao-vote-for-now/)
1. [*Arbitrum Foundation, "Security Council: A conceptual overview" (2024)*](https://docs.arbitrum.foundation/concepts/security-council)
1. [*ENS Docs, "ENS DAO Security Council" (2024)*](https://docs.ens.domains/dao/security-council/)