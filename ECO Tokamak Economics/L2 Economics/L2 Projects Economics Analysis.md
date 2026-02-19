Author: Bernard, Suhyeon

Last Change: 2025-09-21

---

# Summary

| Project | RaaS Architecture | Tokenomics | DA | Security | Comment |
| --- | --- | --- | --- | --- | --- |
| AltLayer | Full-stack RaaS (multi-stack launchpad) | ALT token (ERC-20). Staking, governance, protocol fees, incentives | Ethereum, Celestia, EigenDA (modular) | AVSes: VITAL (validators), MACH (finality/ZK), SQUAD (sequencers) |  |
| Espresso | Shared sequencing / confirmations | No token yet. PoS staking planned | EspressoDA (VID, DA Committee, CDN) | HotShot BFT (permissioned now, PoS later) |  |
| Eclipse | Modular L2 chain (Ethereum + SVM + Celestia) | No native token. Infra + DA fee model | Celestia (default), Ethereum optional | Settlement: Ethereum, Execution: Solana VM |  |
| Caldera | General-purpose RaaS | No native token. Tenant pays fees. Gas in ETH/stable/custom | Ethereum or Celestia | Depends on config: OP Stack (fraud proofs), zkEVM (validity proofs) |  |
| Conduit | Managed RaaS (OP Stack) | No native token. Subscription/management fees | Ethereum DA (default), Celestia/EigenDA roadmap | Inherits OP Stack + Ethereum settlement |  |

### Target: AltLayer, Espresso, Eclipse, Snapchain, Caldera, Conduit

---

# AltLayer

- AltLayer Docs: [https://docs.altlayer.io/altlayer-documentation](https://docs.altlayer.io/altlayer-documentation?utm_source=chatgpt.com)

### Overview

- AltLayer is an **open and decentralized protocol** for rollups, especially “Restaked Rollups” that combine rollup stack flexibility with EigenLayer’s restaking security
- Supports multiple rollup stacks (OP Stack, Arbitrum Orbit, ZKStack, Polygon CDK, etc.) and multiple execution environments (EVM, WASM)
- Provides a **no-code Rollups-as-a-Service (RaaS) launchpad** so that developers (and non-developers) can spin up customized rollups quickly
- Supports both **persistent** rollups and **ephemeral rollups** (rollups spun up temporarily for special demand / application events, and can be “disposed” via settlement on L1)

### Tokenomics

- **Functions of ALT**:
  1. Economic bond / staking stake + restaked assets; instruments for securing the protocol, slashing on misbehavior
  1. Governance: holders vote on parameters, upgrades
  1. Protocol fees: used to pay for services inside the network (RaaS, AVS, sequencing, etc.)
  1. Incentives: rewards to operators, sequencers, validators, etc
- **Supply / Distribution**:
  - Chain: Ethereum L1 (ERC-20 token)
  - Total supply: ~10,000,000,000 ALT
  - Circulating initially ~1.1B ALT (~11%) at listing
  - Splits among launchpool, team, investors, ecosystem/community, treasury, development, etc
- **FYI: Restaking: Return vs. Risk**
  - $\mathbb{E}[\text{APR}] \approx r_0 + \sum_i r_i - \sum_i s_i p_i$


### Security

- AltLayer offers three modular Actively Validated Services (AVSes) to improve security, finality, and decentralization:
  - **VITAL**: verifies that state transitions proposed by rollup sequencers are valid; allows fraud proofs if needed
  - **MACH**: aims for faster finality; several modes including optimistic with on-demand ZK-fault proofs, validity proof modes. Helps reduce delay (for example, challenge periods) in final settlement
  - **SQUAD**: decentralized sequencing; allows multiple sequencers or minimum economic collateral; reduces single-sequencer risks like censorship or MEV rent extraction

### Implication to Tokamak:

- How can we apply ZK-proof to Tokamak’s RaaS? on-demand ZK fault proofs?
- module-based approach, which can be a marketing point when writing a whitepaper

---

# **Espresso**

- Espresso Docs: [https://docs.espressosys.com](https://docs.espressosys.com/?utm_source=chatgpt.com)

### **Overview**

- Espresso is a **shared sequencing layer** for rollups, designed to provide **fast confirmations** and **decentralized ordering** across many L2s.
- Uses the **HotShot BFT consensus** protocol to achieve near-instant confirmations (seconds), enabling better UX and cross-rollup composability.
- Supports integration with multiple rollup stacks (OP Stack, Polygon CDK, Arbitrum Orbit, etc.), allowing those chains to opt-in to Espresso sequencing while keeping their own execution/proof systems.
- **Not a RaaS platform**: Espresso does not spin up rollups directly (unlike AltLayer). Instead, it provides a common sequencer/DA service that existing rollups can plug into.

### **Tokenomics**

- **Current status**:
  - No public native token model announced yet.
  - Mainnet 0 (today) runs with a permissioned sequencer set, no PoS staking or token economics active.
- **Roadmap (PoS transition)**:
  - Espresso plans to introduce **PoS-based validators/sequencers**, who will stake a (future) native token to participate.
  - Stakers will earn sequencing/confirmation fees and be subject to slashing for misbehavior.
- **Economic considerations**:
  - Goal: distribute sequencing revenue and MEV more fairly across many L2 tenants.
  - Until PoS is live, RaaS or rollup tenants using Espresso likely compensate via off-chain/contractual arrangements.

### **Security**

- **HotShot Consensus**: BFT protocol that finalizes ordering within seconds; ensures safety and liveness with a small validator set (currently permissioned).
- **EspressoDA**: a three-layer data availability subsystem designed to work natively with HotShot:
  - **VID Layer**: erasure-coded data chunks distributed to all nodes.
  - **DA Committee Layer**: small group stores full data and guarantees recovery.
  - **CDN Layer**: improves efficiency of data retrieval.
- **Roadmap**: EspressoDA + HotShot will eventually be secured by PoS validators (permissionless), providing both sequencing and DA guarantees.

### Implication to Tokamak:

- Not much; quite different from Tokamak’s approach

---

# Eclipse

- Eclipse Docs: [https://www.eclipse.builders](https://www.eclipse.builders/)

## **Overview**

- Eclipse is an L2 platform built around a modular architecture:
  - Execution: Solana VM (SVM) for high throughput and parallel execution, or optionally EVM.
  - Settlement: Ethereum L1 for finality and security.
  - Data Availability (DA): Celestia, providing low-cost, scalable DA.
- Branded as the “Ethereum security + Solana performance + Celestia scalability” rollup model.
- Allows developers to launch L2 rollups that inherit Ethereum’s security while enjoying Solana’s execution speed and Celestia’s cheap DA.

## **Tokenomics**

- Current status: Eclipse has not yet launched a native token.
- Rollups created via Eclipse typically use ETH (for settlement) in their operation.
- Future token model (if any) has not been formally announced.
- Economic security is currently derived from Ethereum (settlement) and Celestia (DA PoS), rather than Eclipse-native staking.

## **Security**

- Settlement on Ethereum: All rollup state roots are posted to Ethereum L1, inheriting its consensus security.
- Data Availability via Celestia:
  - DA is guaranteed by Celestia’s PoS validator set with TIA staking/slashing.
  - Transactions are erasure-coded and stored across Celestia validators, ensuring availability.
- Execution integrity via Solana VM: Parallel execution provides performance, but correctness is ultimately enforced by settlement proofs on Ethereum.
- Overall: A modular combination — Ethereum (finality), Celestia (DA), Solana VM (execution).

## Implication to Tokamak:

- Mudular approach - especially Celestia DA

# **Snapchain**

- Docs: [https://docs.snapchain.dev](https://docs.snapchain.dev/?utm_source=chatgpt.com)

## **Overview**

- Snapchain is a **Rollup-as-a-Service (RaaS) platform** with a focus on **zk-rollups and fast finality**.
- Provides a **no-code/low-code console** for developers to configure, launch, and manage rollups.
- Snap V1: brings fast finality (≈1–5s) to OP Stack rollups compared to the ~15–30 min finalization delay via Ethereum L1.
- Claims minimal intrusion and full EVM equivalence with “zero-downtime upgrades.”
- Supports integration with multiple frameworks: OP Stack, Polygon CDK, ZK Stack, etc.
- Powered by Babylon Bitcoin staking: Snapchain integrates a security layer where BTC can be staked to provide shared security for rollups.
  - BTC is staked and acts as collateral.
  - Rollup blocks receive finality votes backed by this staked BTC.
  - A block is finalized once enough finality votes are attached.
  - If validators sign two conflicting blocks at the same height, the staked BTC is slashed.
  - Goal: “Bitcoin security for all chains” – extend Bitcoin’s economic weight as a deterrence mechanism to Ethereum L2 rollups (starting with OP Stack).

## **Tokenomics**

- Current status: No native Snapchain token announced.
- Gas token within L2 tenants: configurable (EVM-equivalent → ETH likely default).
- Service fee model (tenant ↔ Snapchain): not fully disclosed.
- BTC staking (via Babylon) introduces an economic security model:
  - Security = proportional to staked BTC.
  - Risks = BTC stakers can be slashed for equivocation.
  - Rewards/fee distribution not yet fully detailed.

## **Security**

- Finality Layer: Snapchain provides an additional consensus/finality layer that reduces time-to-finality from minutes to seconds.
- Bitcoin staking (Babylon): BTC is used as a collateralized security resource, with slashing penalties.
- Settlement: Still relies on Ethereum L1 for ultimate settlement & challenge windows → Snapchain finality is UX-level only, not a replacement for L1 finality.
- Key distinction: Snapchain rollups gain faster confirmation and extra economic security from Bitcoin staking, but cannot bypass Ethereum’s L1 withdrawal/challenge rules.

## **Open Questions**

- How BTC staking is custodial/non-custodial and where BTC is held.
- Rewards mechanism for BTC stakers (currently unspecified).
- How exactly rollup bridges and liquidity providers will treat Snapchain “fast finality” vs Ethereum’s ultimate finality.
- DA (Data Availability) layer choice: not yet detailed (Celestia? EigenDA? custom?).

## Implication to Tokamak:

- Not much; quite different from Tokamak’s approach

# **Caldera**

- Docs: [https://docs.caldera.xyz](https://docs.caldera.xyz/)

## **Overview**

- Caldera is a **Rollup-as-a-Service (RaaS)** platform that enables teams to deploy their own **custom L2 rollups** quickly.
- **Execution environments**: Supports **EVM** and **zkEVM** options.
- **Settlement**: Typically Ethereum L1, but configurable depending on needs.
- **Data Availability**: Pluggable — options include Ethereum (expensive, secure), **Celestia**, and others.
- **UX focus**: Provides a console/dashboard for developers to configure rollup parameters (stack, DA, gas token, etc.) and launch without deep infra expertise.

## **Tokenomics**

- **No native Caldera token announced**.
- Cost model: tenants pay service fees (infra, ops, sequencing).
- Rollup fees are set by the tenant (can denominate in ETH, stablecoins, or project’s own token).
- Economic security is tied to the chosen stack (e.g., OP Stack fraud proofs, zk proofs, and DA guarantees via Celestia/Ethereum).

## **Security**

- Security properties depend on chosen configuration:
  - If OP Stack rollup → optimistic fraud proof model, 7-day challenge window.
  - If zkEVM → zk validity proofs for settlement.
  - DA choice (Ethereum vs Celestia) defines data availability guarantees.
- Caldera itself doesn’t run consensus; it orchestrates and hosts the infra.

---

# **Conduit**

- Conduit Docs: [https://docs.conduit.xyz](https://docs.conduit.xyz/)

## **Overview**

- Conduit is a **fully-managed RaaS** service with strong ties to the **OP Stack (Optimism)**.
- **Focus**: Allows developers to launch **OP Chains** easily — Conduit provides infra, upgrades, monitoring, and integrations.
- **Execution environment**: Primarily EVM via OP Stack.
- **Settlement**: Ethereum L1 (through Optimism rollup protocol).
- **DA**: Ethereum DA by default; roadmap includes alternative DA integrations (e.g., Celestia, EigenDA).
- Provides “one-click” deployment and ongoing management of rollups.

## **Tokenomics**

- **No native Conduit token**.
- Revenue model: subscription/management fees for providing infra + monitoring.
- Gas fees on the launched chain can be in ETH or project’s custom token.
- Economic guarantees tied to OP Stack design — inherits Optimism’s security model.

## **Security**

- Inherits **OP Stack fraud-proof + Ethereum settlement** security.
- DA is Ethereum by default, but can be swapped to modular DA in the future.
- Conduit’s value-add is operational security: uptime, infra resilience, monitoring.