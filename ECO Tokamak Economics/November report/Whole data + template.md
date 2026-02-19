# Project ECO Monthly Report (November 2025)

## 1. DAO

The DAO project proceeded with the systematization of governance processes (introduction of RFCs), improvement of smart contract functions, and analysis of the governance structure through the onboarding of new researchers.

### 1.1. Introduction of Governance Standards (RFC) and Community Expansion

We introduced an RFC (Request for Comments) procedure for community discussion prior to proposal submission, standardized templates for this purpose, and conducted announcements via social media (Medium, X).

- **github (Harvey):** Update discussion-rfc.yml / Rename DiscussionOfIdeas.yml (2025-11-18)
- **slack (Harvey):** "We're introducing RFC process to Tokamak DAO! ... Agenda 14 (Sample) & 15 (Progress)" (2025-11-06, 11-14)
- **slack (Harvey):** "Currently working on adding an RFC phase to Discord" (2025-11-18)
- **notion (Harvey):** share RFC_Sample / share Ongoing agenda (2025-11-12)

### 1.2. DAO Contract Function Improvement & Audit Platform

Discussions and testing were conducted to add signature verification (`isValidSignature`) functionality to the DAO contract, and initial development of the Audit platform began.

- **github (Jeongun Baek):** initial commit [audit-platform] (2025-11-16)
- **slack (Harvey):** "Adding isValidSignature functionality to the DAO Contract... Create a GitHub discussion" (2025-11-19)
- **slack (Thomas):** "I tried to call the `createCandidate` function... getting a StorageStateCommittee: invalid SeigManager" (2025-11-26)

### 1.3. Governance Research and Onboarding

A new DAO Governance Researcher (Thomas) joined the team and began analyzing the current DAO structure and contract code.

- **slack (Thomas):** "I’m currently going through the onboarding process... reviewing DAO documentation and contract codes" (2025-11-24)
- **slack (Jason):** "Hello this is @shinthom, new DAO governance researcher." (2025-11-24)

---

## 2. Staking

The Staking project focused on establishing and implementing the Slashing policy for V2, and integrating Dune Analytics to strengthen data analysis capabilities.

### 2.1. Staking V2 Development and Slashing Policy Establishment

We implemented the Slashing Manager and Deposit Manager contracts and conducted in-depth discussions with Kevin and team members regarding specific slashing ratios (burn rates) and logic.

- **github (Harvey):** Create SeigManagerV1_Slashing.sol / DepositManagerV1_Slash.sol (2025-11-24)
- **github (Harvey):** add slashing logic / Change Slash Contract (2025-11-05)
- **slack (Harvey):** "Organize slashing-related content... Confirm the content with Kevin... Proceed with development." (2025-11-10)
- **slack (Suhyeon):** "ECO: Slashing discussion... I left comments except for 4 and 7." (2025-11-26)

### 2.2. Establishment of Data Analysis Infrastructure (Dune & Metrics)

We performed script development and query writing to visualize the Tokamak Network's economic metrics (Total Supply, Staked Amount, APY, etc.) via Dune Analytics.

- **github (Zena):** feat: Add Dune Analytics integration / metrics calculation script (2025-11-24)
- **slack (Zena):** "Sharing the completion of Basic Staking Metrics extraction... TON Staked Amount & TON Price link" (2025-11-27)
- **slack (Suhyeon):** "I updated daily staking APY query in Dune and it shows the identical APY with the Simple staking community version." (2025-11-27)
- **slack (Zena):** "Total circulating amount = Total supply - Total staked amount - DAO Vault..." (2025-11-25)

### 2.3. V1 Subgraph Maintenance

Completed the mainnet reflection and documentation for the Staking V1 Subgraph.

- **github (Jason):** Merge pull request #1 from tokamak-network/mainnet (2025-11-24)
- **github (Jason):** add Readme (2025-11-24)

---

## 3. Economics

The Economics project concentrated on a comprehensive overhaul of the L2 whitepaper, advancement of the Fault Proof system, and research on the Shared Validator model.

### 3.1. Whitepaper Redesign

We agreed to reorganize the existing whitepaper into the structure of 'Verification Economics -> Utility (Demand) -> Seigniorage (Supply)', and proceeded with drafting and reviewing each section.

- **slack (Suhyeon):** "Bernanrd and I’ve drafted a revised whitepaper outline... 1. Verification Economics 2. Utility of TON 3. Seigniorage" (2025-11-10)
- **slack (Bernard):** "Drafted the overall structure of the updated L2 Whitepaper" (2025-11-12)
- **notion (Suhyeon):** Whitepaper Update Plan (EN) (2025-11-04)

### 3.2. L2 Fault Proofs and Cost Analysis

We established an E2E test environment for Asterisc and Kona challengers and drafted Bond Cost measurement reports in both Korean and English.

- **github (Zena):** Add Asterisc and Kona fault-proof E2E suites (2025-11-11)
- **github (Zena):** docs: add bond cost measurement analysis set (Korean/English) (2025-11-12)
- **github (Zena):** feat: add Asterisc helper functions for trace provider (2025-11-20)
- **slack (Zena):** "End-to-end evaluation (E2E) testing of the fault game (gametypes 0 and 2) has been completed." (2025-11-12)

### 3.3. Research: Shared Validator & RAT

We conducted a seminar analyzing the security and cost-efficiency of the Shared Validator model and performed research on RAT (Random Attention Test) game theory and collusion possibilities.

- **slack (Bernard):** "Analysis of Shared Validator Sets for Securing Multi-Rollup Systems... shared validator set model is significantly superior to the partitioned model" (2025-11-08, 11-13)
- **slack (Eugenie):** "Critique on the game model being unclear... discussion on collusion is missing" (2025-11-21)
- **slack (Suhyeon):** "ECO: RAT game discussion... formal game type definition / collusion analysis approach" (2025-11-27)

---

## 4. Price API

The Price API project expanded database capabilities and improved logic for accurate withdrawal data aggregation.

### 4.1. Feature Expansion and Data Consistency Improvement

We implemented post storage functionality through MongoDB integration and applied accurate data aggregation logic based on 'Unstaked' events rather than simple 'Withdrawals'.

- **github (Zena):** feat: Add withdrawals event aggregation and improve price API (2025-11-26)
- **github (Zena):** Update subgraphClient to query unstakeds instead of withdrawals (2025-11-27)
- **github (Jason):** store medium post in db / test mongo db connection (2025-11-26)
- **slack (Zena):** "Instead of removing the Deposited event, add the WithdrawalRequestCanceled event." (2025-11-27)
- **slack (Jason):** "I made new API for Medium. It stores recent 10 blog post in DB" (2025-11-26)

---

## 5. Team & General

- **New Hire Onboarding:** Thomas (DAO Governance) and Eugenie (L2 Economics Researcher) joined and familiarized themselves with tasks.
- **Slack Discussion:** Monitoring metrics related to GOPAX listing (wallet count, transactions, etc.) (Suhyeon, 2025-11-27).
- **Notion Logs:** Weekly/Monthly reports and meeting minutes organization (Jason).

---

### Submission Details

- **The scope of Ati data used:** 2025.11.01-2025.11.27 / Notion, Github, Slack
- **The hash of the extracted Ati data:** d71329583b63264426217462cc8d80f68045610ec0d25683236e744007b8cc40
- **The prompt(s) used for report generation:** 이 데이터를 기반으로 다시 작성해주ㅓ