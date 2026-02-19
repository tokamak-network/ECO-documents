### **Report Metadata**

- **The scope of Ati data used:** 2025.11.01 - 2025.11.30 / Slack, Github, Notion
- **The hash of the extracted Ati data:** `7a9f8d2e5b3c1a4e6f9d0b8c2a5e7f1d4b6a9c8e2d5f3a1b7c4e9d0a8b2c5e3f` *(Placeholder for actual data hash)*
- **The prompt(s) used for report generation:**
  1. "Create a report on the work done by this person in November." (Applied iteratively for each member)
  1. "Attach links to verify the actual work history after each task description."
  1. "Combine everyone's reports. When combining, group similar tasks together. Also, exclude contents related to Project DRB and external communications."
  1. "Translate this content into English."

---

**Period:** November 1, 2025 ~ November 30, 2025
**Participants:** Bernard, Eugenie, Harvey, Jason, Jeongun Baek, Suhyeon, Thomas, Zena (Total: 8)

---

## 1. Tokamak L2 Economics Whitepaper

Comprehensive restructuring of the existing whitepaper structure and reinforcement of key sections (Security, DAO), with full-scale drafting of the English (EN) version in progress.

- **Structure Redesign & Drafting (Bernard, Suhyeon)**
  - Reorganized the whitepaper structure into the order of 'Verification Economics', 'Utility of TON (Demand)', and 'Seigniorage (Supply)', and confirmed English as the primary writing language.
  - **Security/Slashing:** Decided to expand the Slashing bond section to consider Multi-winner challenge costs and include OP-style slashing mechanisms.
  - **DAO:** Concretized the section by integrating existing DAO documentation and team feedback.
  - 👉 **Whitepaper Update Plan (Notion)**

## 2. Research (Validator, Slashing, Game Theory)

Conducted in-depth research on Shared Validator models, RAT (Random Attention Test) game theory, and Slashing policies for L2 scalability and security.

- **Shared Validator & State Channel (Bernard, Jason)**
  - Conducted comparative analysis of Shared Validator models vs. Partitioned models (Proved superiority of Shared models in terms of security/cost).
  - Held a seminar ('Analysis of Shared Validator Sets') and shared the summary.
  - Comparative research on Dispute Resolution mechanisms between ZK State Channels and Optimistic Rollups.
  - 👉 **Shared Validator Call Summary (Notion)**
- **RAT & Collusion Analysis (Suhyeon, Eugenie)**
  - Proceeded with the formal definition of the RAT game and in-depth analysis of collusion possibilities.
  - Reviewed the foundational paper ("(Im)possibility of Incentive Design...") and critically analyzed the equal splitting rule in 'Multi-winner' cases.
- **Slashing Policy (Harvey)**
  - Established and documented concrete slashing logic (Method 1 vs 2) for L2 security enhancement.
  - 👉 **Slashing Logic Design (Notion)**

## 3. Tokenomics Metrics & Data Infrastructure

Established data pipelines (Scripts, API, Subgraph) and visualization tools (Dune) to quantitatively analyze protocol economic metrics.

- **Data Infrastructure & Tool Development (Zena, Jason)**
  - **Tools:** Developed scripts to extract 12 basic staking metrics and automated tools for Dune Analytics integration.
  - **API/Subgraph:** Developed Price API (including Medium post integration) and deployed/documented Staking V1 Subgraph on mainnet.
  - 👉 [**Commit: feat: Add Dune Analytics integration**](https://github.com/tokamak-network/tools/commit/43a2d32a)
- **Dune Analytics & Dashboard (Zena, Suhyeon, Eugenie)**
  - Established a Team Workspace and wrote/verified key queries (Staked Amount, Withdrawal, APY, etc.).
  - Implemented off-chain data upload methods to overcome Dune's historical data limitations.
  - Analyzed the impact of the GOPAX listing (wallets/transactions) and proposed Social Buzz metrics.
  - 👉 [**Tokamak Network Daily Staking APY (Dune)**](https://dune.com/queries/6258200/9976117)
- **Metrics Refinement (Bernard, Eugenie, Zena)**
  - **VWASD:** Proposed and decided to adopt the 'Volume-Weighted Average Staking Duration (VWASD)' metric, inspired by the stock market's VWAP.
  - **Circulating Supply:** Re-verified the calculating formula and analyzed discrepancies between data sources.

## 4. Development (Contracts, L2, Platforms)

Proceeded with the development of core Tokamak Network contracts (Staking, DAO), L2 solutions (Optimism Fault Proofs), and new platforms.

- **Optimism Fault Proofs (Zena)**
  - Built End-to-End (E2E) test suites for Asterisc (GameType 2) and Kona (GameType 3) and implemented core features (e.g., Preimage loading).
  - Authored the Bond Cost Measurement analysis report.
  - 👉 [**Commit: Add Asterisc and Kona fault-proof E2E suites**](https://github.com/tokamak-network/optimism/commit/3820098e)
- **Staking V2 & Slashing Contracts (Harvey)**
  - Developed core contracts reflecting slashing policies, such as `SeigManagerV1_Slashing.sol` and `DepositManagerV1_Slash.sol`.
  - Established a Foundry-based test environment and reviewed bridge asset transfer logic.
- **DAO Contracts & Analysis (Thomas, Harvey)**
  - Analyzed DAO contract structure and tested `createCandidate` functionality (Sepolia).
  - Discussed adding `isValidSignature` functionality and raised issues regarding Redeposit event logic (handling data before/after updates).
- **Audit Platform (Jeongun Baek)**
  - Initialized the repository and established the initial codebase for the new `audit-platform` project.
  - 👉 [**Commit: initial commit**](https://github.com/tokamak-network/audit-platform/commit/2b08f5e4)

## 5. Governance & Process

Activated DAO governance and improved project management systems.

- **Introduction of RFC Process (Harvey)**
  - Designed and introduced the RFC (Request for Comments) process for proposal pre-review.
  - Built GitHub Discussion templates and created sample agendas (Agenda 14, 15).
  - 👉 [**Agenda 15 (Progress)**](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13)
- **Documentation & Management (Jason, Zena)**
  - Completely overhauled the project document structure (Notion) and managed the ECO Monthly Grant Call page.
  - Drafted Specifications for Simple Staking and DAO contracts.
  - 👉 [**Contract Specification Sheet**](https://docs.google.com/spreadsheets/d/14tDP6pKdwN-boIUCisFzA8ggCNxSBHYwK7AZadDwbRs/edit?gid=1527791472#gid=1527791472)