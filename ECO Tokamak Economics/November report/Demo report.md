Here is the consolidated work report for November 2025, categorizing the team's efforts into **L2 Whitepaper & Economics**, **Protocol Engineering**, **Data Infrastructure**, and **DAO Governance**.

**Note:** Work related to *Project DRB* and *External Communications (Marketing/Social Media)* has been excluded as requested.

---

### **1. Tokamak L2 Economics Whitepaper & Theoretical Research**

The team focused heavily on restructuring and drafting the new L2 Whitepaper, supported by deep theoretical research into game theory, collusion, and validator incentives.

- **Whitepaper Restructuring & Drafting:**
  - **Suhyeon** led the strategic redesign of the whitepaper, defining the new structure: *1. Verification Economics, 2. TON Utility (Demand), 3. Seigniorage (Supply).*
    - *Plan:* https://www.notion.so/tokamak/Whitepaper-Update-Plan-EN-2a2d96a400a38000a2d7fb16b2e7ab78
  - **Bernard** drafted the "L2 Security" and "Economics" sections, incorporating OP-style slashing logic and refining bond requirements to cover gas costs for multi-winner challenges.
  - **Zena** contributed technical specifications for the "Simple Staking" and "DAO" contract sections to ensure accuracy.
    - *Specs:* [https://docs.google.com/spreadsheets/d/14tDP6pKdwN-boIUCisFzA8ggCNxSBHYwK7AZadDwbRs/edit?gid=1527791472#gid=1527791472](https://docs.google.com/spreadsheets/d/14tDP6pKdwN-boIUCisFzA8ggCNxSBHYwK7AZadDwbRs/edit?gid=1527791472#gid=1527791472)
- **Academic Research & Peer Review:**
  - **Eugenie** established a **Literature Review** knowledge base and provided critical analysis on internal papers ("RAT" and "Multi-winner challenges"), specifically identifying gaps in collusion analysis.
    - *Review:* [https://docs.google.com/document/d/1eJGpjOcleLNmR2KDF8oSugBiLb4oLcSbhUVziF89tHE/edit?tab=t.gnt2q2qdlmg2](https://docs.google.com/document/d/1eJGpjOcleLNmR2KDF8oSugBiLb4oLcSbhUVziF89tHE/edit?tab=t.gnt2q2qdlmg2)
  - **Suhyeon** reviewed the "(Im)possibility of Incentive Design" paper and led discussions comparing Tokamak’s model against Arbitrum’s BOLD protocol.
  - **Jason** authored a comparative analysis on "Optimistic Rollup Dispute Game Processing Methods."
    - *Analysis:* https://www.notion.so/tokamak/Optimistic-Rollup-Dispute-Game-Processing-Methods-Comparison-2a9d96a400a380dd86b6dbbb69c814f6
- **Shared Validator Research:**
  - **Bernard** conducted analytical modeling proving the security/cost superiority of Shared Validator Sets over Partitioned Models and presented a seminar on the topic.
    - *Slides:* [https://docs.google.com/presentation/d/1hMZ06ss9XToyE2XrUMKAg91UUoagS4Cr/edit?usp=sharing&ouid=112457105414325263650&rtpof=true&sd=true](https://docs.google.com/presentation/d/1hMZ06ss9XToyE2XrUMKAg91UUoagS4Cr/edit?usp=sharing&ouid=112457105414325263650&rtpof=true&sd=true)
  - **Jason** managed the documentation and summarization of the Shared Validator technical discussions.

---

### **2. Protocol Engineering & Smart Contracts**

Development focused on Fault Proofs for the Optimism stack and the implementation of Slashing mechanisms.

- **Optimism Fault Proofs (Asterisc & Kona):**
  - **Zena** completed End-to-End (E2E) evaluation testing for fault game types 0 and 2. She implemented test suites for **Asterisc** (RISC-V) and **Kona**, covering edge cases like large preimage handling, and published a **Bond Cost Measurement Report**.
    - *Code:* [https://github.com/tokamak-network/optimism/commit/3820098e](https://github.com/tokamak-network/optimism/commit/3820098e)
- **Slashing Mechanism:**
  - **Harvey** designed and implemented the foundational Solidity contracts for slashing, including `SeigManagerV1_Slashing`, `DepositManagerV1_Slash`, and `Layer2ManagerV1_Slash`.
    - *Code:* [https://github.com/tokamak-network/ton-staking-v2/commit/c3559e3b](https://github.com/tokamak-network/ton-staking-v2/commit/c3559e3b)
  - **Bernard** provided the theoretical logic for the slashing bond requirements used in these contracts.
- **Audit Platform Initialization:**
  - **Jeongun Baek** initialized the `audit-platform` repository, pushing the foundational codebase (~15,000 lines).
    - *Commit:* [https://github.com/tokamak-network/audit-platform/commit/2b08f5e4](https://github.com/tokamak-network/audit-platform/commit/2b08f5e4)

---

### **3. Data Infrastructure & Analytics**

The team built a comprehensive pipeline to extract on-chain data and visualize it via Dune Analytics to support economic monitoring.

- **Dune Analytics Integration:**
  - **Zena** built a custom Node.js toolset to calculate 12 basic staking metrics and automate data uploads to Dune via REST API. She also set up the team workspace (`@project_eco_test`).
    - *Tooling:* [https://github.com/tokamak-network/tools/commit/43a2d32a](https://github.com/tokamak-network/tools/commit/43a2d32a)
  - **Suhyeon** validated the Staking APY queries on Dune against legacy community tools to ensure accuracy.
    - *Query:* [https://dune.com/queries/6258200/9976117](https://dune.com/queries/6258200/9976117)
- **API & Subgraph Development:**
  - **Jason** upgraded the **Price API** with MongoDB integration to store blog posts and updated the **Staking V1 Subgraph** to better handle mainnet data.
    - *API Update:* [https://github.com/tokamak-network/price-api/commit/3c6e5904](https://github.com/tokamak-network/price-api/commit/3c6e5904)
  - **Zena** fixed subgraph logic to correctly distinguish between "Unstaking" and "Withdrawal" events.
- **Metric Design:**
  - **Eugenie** defined the logic for **Average Staking Duration** (matching deposit/unstake events) to measure user holding intention.
  - **Bernard** proposed the **VWASD (Volume-Weighted Average Staking Duration)** metric, adapting financial VWAP concepts for tokenomics.

---

### **4. DAO Governance & Operations**

Efforts were made to formalize the proposal process and improve the technical governance infrastructure.

- **RFC (Request for Comments) Process:**
  - **Harvey** technically configured the GitHub repository to support the new RFC process, creating discussion templates for Agendas 14 & 15.
    - *Config:* [https://github.com/tokamak-network/tokamak-dao-contracts/commit/5e6eb8b6](https://github.com/tokamak-network/tokamak-dao-contracts/commit/5e6eb8b6)
- **Governance Contract Research:**
  - **Thomas** (new hire) analyzed the `DAOCommittee` architecture and successfully debugged candidate creation issues on the Sepolia testnet (identifying `CommitteeProxy` usage requirements).
  - **Harvey** investigated adding `isValidSignature` functionality to DAO contracts.
- **Internal Operations:**
  - **Jason** restructured the internal Notion documentation, organizing knowledge into Staking V2, DAO, and Weekly Logs.
  - **Zena** managed the monthly audit of TON Total Supply and Circulating Supply data.