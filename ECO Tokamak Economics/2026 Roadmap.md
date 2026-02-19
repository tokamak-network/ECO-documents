### A. Tokamak Economics

- Add new game type to Challenger system(research) - Q2

**RAT Client**
  - Implement RAT client for Optimism Stack [Zena] Q1
  - Development the RAT Client for OOO project [Zena] Q3
  - Merge the RAT Client for OOO project to Staking V3 [Zena] Q4

UX/UI for RAT(?) [Jason] Q2 
    - Response to RAT
    - Submit fraud proof
    - Visualization and current status about $D_{sequencer}, H_{max}, \Delta_{sequencer}$
    - Management UI (community-version)
      - Validator registration/management UI
      - Collateral status and reward inquiry
      - RAT test history and response rate statistics
      - Real-time notifications (immediate notification upon RAT trigger)
      - Transaction execution log (registration, withdrawal, reward claim, etc.)
      - Current status inquiry

**Staking V3** 
  - Staking V3: Modeling & V2-V3 Migration plan [Zena] Q2
  - Advanced Slashing Mechanism release & PoC [Harvey] Q1

Staking V3: Contract implementation - Slashing + Validator  [Zena, Harvey, Jeongun, Thomas] Q1
    - Whitepaper analysis and LLM specification document creation (including RAT contract, client, staking module changes, V2→V3 transition)  [Zena, Harvey, Jeongun, Thomas]
    - AI-powered code development, unit test script development, E2E test script development
      - RAT system 
      - Staking module changes (including V2→V3 transition)  
      - Sequencer slashing  
      - Validator slashing 
    - Contract function-by-function code review and tuning [Zena, Harvey, Jeongun, Thomas]

Staking V3: Update Dune dashboard [Zena, Suhyeon, Bernard, Eugienie] Q2
    - Select metrics appropriate for V3
    - develop scripts, and implement

Staking V3: Contract audit [Zena, Harvey, Jason, Jeongun, Thomas] Q2
    - Internal audit [Zena, Harvey, Jeongun, Thomas]
    - External audit [Zena, Harvey, Jason]

Staking V3: Migration & Deployment [Zena, Harvey] Q3
    - Documentation [Harvey]
    - Set migration plan  [Zena] 
    - Write and simulate migration script [Zena, Harvey]
    - Write and simulate deployment script [Zena, Harvey]
    - Deploy [Zena, Harvey]

Staking V3: Open community version [Jason] Q4
    - V2 staking screen maintenance (module changes if there are any changes)
    - Functional support according to V3 seigniorage deployment
      - Seigniorage claim support (sequencer, validator)
      - Seigniorage distribution status inquiry (sequencer, validator)
      - Layer 2 status check (whether eligible to receive seigniorage)
      - View slashing  status (sequencer, validators)  
      - Register and deregister (verifiers) 
    -   

Staking V3 : develop Staking V3 SDK [Harvey, Thomas] Q4
    - Slashing part [Harvey]
    - Staking part [Thomas]
    - RAT part [Harvey, Thomas]
    - internal Test [Harvey, Thomas]
    - Documentation [Harvey, Thomas]

**Fast withdrawal(?)**
  - FW with new Optimism dispute game [Jeongun] 

### B. Tokamak Governance

New DAO Governance
  - DAO Governance research [Thomas] Q1
  - DAO Governance modeling based on research [Thomas] Q1
  - Upgrade DAO Governance contract based on modeling [Thomas, Harvey] Q2
  - Update DAO community version based on new governance [Thomas] Q3

- Adopt Off-chain voting (Snapshot) - after SYB mainnet

### C. Utility of TON

- L2 Delegated Stake/L2 Native Staking

### Timeline

| Year-Quarter | Milestone |
| --- | --- |
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
- Staking V3: Contract Development ( included RAT )   |
| 2026-Q2 | - Add new game type to Challenger system(research)
- Staking V2: Slashing protocol audit
- Staking V3: Contract Audit  |
| 2026-Q3 | - Staking V2: Slashing protocol open to community version
- Staking V3: Migration & Publish 
- RAT Client Development for Project OOO 
- Research: ZK Fraud proof |
| 2026-Q4 | - Merge RAT Client for Project OOO 
- Staking V3 : develop Staking V3 SDK |
| 2027-Q1 |  |