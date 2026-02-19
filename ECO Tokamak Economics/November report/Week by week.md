# **November 2025 Monthly Progress Report (Technical & Research Focus)**

**Period:** November 1, 2025 – November 29, 2025

## **1. Research & Whitepaper (Project ECO)**

**Overview:** Full overhaul of the L2 Economics Whitepaper, verification of Shared Validator modeling, and technical analysis of competing protocols.

- **Whitepaper Overhaul & Drafting**
  - **Structure Design & Finalization:** Redesigned and established the writing process for the whitepaper structure: Verification Economics → Utility of TON (Demand) → Seigniorage (Supply).
  - **Drafting:** Drafted overviews and full text for each section; updated content to reflect feedback, such as avoiding the term "Burn" and clarifying incentive structures.
    - *Proof (Plan):* Notion: Whitepaper Update Plan
    - *Proof (Draft):* [Google Drive Draft](https://drive.google.com/file/d/1pQwEkrhLzUaFaRG6ngTHaAWIUEw44Y0B/view?usp=sharing) (Nov 25)
- **Shared Validator Research**
  - **Modeling Analysis:** Derived results proving the superiority of the Shared Validator model over the Partitioned model in terms of security and cost.
  - **Seminar:** Presented "Analysis of Shared Validator Sets for Securing Multi-Rollup Systems" and shared technical documentation.
    - *Proof (Slack):* "results show that the shared validator set model is significantly superior..." (Nov 8)
    - *Proof (Slides):* [Presentation Link](https://docs.google.com/presentation/d/1hMZ06ss9XToyE2XrUMKAg91UUoagS4Cr/edit?usp=sharing)
    - *Proof (Minutes):* [Seminar Minutes](https://docs.google.com/document/d/1Lwa3NhCHR_AYfq6bWGReHuazAtpvE077g4qbETY1xTw/edit?usp=sharing)
- **Game Theory & Technical Analysis**
  - **Protocol Comparison:** Analyzed security mechanism differences between Arbitrum BOLD (absence of centralized Guardian) and the Tokamak Challenge-based model.
  - **RAT Collusion Analysis:** Conducted extended research on the possibility of collusion within the RAT (Random Attention Test) model.
  - **External Audit (Technical):** Confirmed resolution of technical issues in the CertiK audit and received the final report.
    - *Proof (Research):* Notion: RAT Paper Game Model & Collusion Analysis
    - *Proof (Audit):* Notion: External Audit Progress

## **2. Development: L2 Core & Staking (Thanos/Tokamak)**

**Overview:** Enhancement of the Optimism-based Fault Proof System and implementation of Staking V2/Slashing logic.

- **Optimism/Thanos (Fault Proof System)**
  - **Challenger Implementation:** Developed Challenger functions based on Kona and Asterisc. Added Preimage helper functions and enhanced VM options.
  - **E2E Testing:** Added and documented End-to-End test scenarios for GameType 2 & 3; improved the logging system.
    - *Proof (Docs):* [Fault Proofs E2E Test Cases Readme](https://github.com/tokamak-network/optimism/blob/feature/challenger-game-type-check/op-challenger/scripts/docs/test-cases/README.md)
    - *Proof (Commits - **`optimism`**):*
      - `50a725ed`: feat: add Asterisc preimage helper functions
      - `fd9ead47`: Add challenger E2E docs and operational tooling
      - `ad787baa`: fix: harden kona challenger config
- **Staking V2 & Slashing (Smart Contracts)**
  - **Slashing Logic Development:** Implemented core slashing contracts (`SeigManagerV1_Slashing`, `DepositManagerV1_Slash`) and math libraries (`FullMath.sol`) in the `ton-staking-v2` repository.
    - *Proof (Commits - **`ton-staking-v2`**):*
      - `c3559e3b`: Create SeigManagerV1_Slashing.sol
      - `b5843377`: Create DepositManagerV1_Slash.sol
      - `39243311`: Create FullMath.sol
      - `e428b68c`: Update SeigManagerV1_Slashing.sol

## **3. Data & Infrastructure**

**Overview:** In-house development of economic metrics analysis tools, Dune Analytics integration, and API server setup.

- **Economic Metrics Tool Development**
  - **In-house Extraction Tool:** Developed Node.js-based scripts for on-chain data extraction and metric calculation (built `tools` repository for 12 basic staking metrics, etc.).
  - **Dune Analytics Integration:** Created Dune queries (TON Price, Total Staked, Seigniorage, etc.), set up a Team Space, and verified data consistency against existing documentation.
    - *Proof (Commits - **`tools`**):*
      - `baa45e05`: feat: Add metrics calculation script
      - `43a2d32a`: feat: Add Dune Analytics integration
    - *Proof (Dune):* [Dune Query: TON Staked Amount](https://dune.com/queries/6260451/9979850)
- **API & Subgraph**
  - **Price API:** Built an API server (MongoDB integration) to link Medium posts and provide token price information.
  - **Subgraph:** Updated and merged the Mainnet Subgraph.
    - *Proof (Commits - **`price-api`**):* `3c6e5904` (store medium post in db), `d403b836` (update post related section)
    - *Proof (PR):* `staking-v1-subgraph` merged PR #1 "Mainnet"

## **4. DAO & Governance**

**Overview:** Technical introduction of the RFC process and restructuring of documentation/contract structures.

- **RFC Process & Agenda Processing**
  - **Process Setup:** Established an RFC (Request for Comments) process using GitHub Discussions and created Agenda 14 & 15.
  - **Feature Proposal:** Conducted technical review and created a Discussion for adding the `isValidSignature` function to the DAO contract.
    - *Proof (Discussion):* [Agenda 14 (Sample)](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/11), [Agenda 15](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/12)
    - *Proof (Technical Discussion):* [isValidSignature Proposal](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13)
- **Documentation & Contract Verification**
  - **Doc Separation:** Separated DAO and Staking sections in GitBook and added a TIP (Tokamak Improvement Proposal) section.
  - **Contract Testing:** Tested major DAO functions (e.g., `createCandidate`) in the Sepolia environment and performed troubleshooting.
    - *Proof (Doc Update):* [GitBook Change Log](https://docs.tokamak.network/home/kor/~/changes/v/staking-dao-separation)