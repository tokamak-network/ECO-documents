# Survey: Major Rollup-as-a-Services at the Market

## AltLayer

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

### Security

- AltLayer offers three modular Actively Validated Services (AVSes) to improve security, finality, and decentralization:
  - **SQUAD**: decentralized sequencing; allows multiple sequencers or minimum economic collateral; reduces single-sequencer risks like censorship or MEV rent extraction
  - **VITAL**: verifies that state transitions proposed by rollup sequencers are valid; allows fraud proofs if needed
  - **MACH**: aims for faster finality; several modes including optimistic with on-demand ZK-fault proofs, validity proof modes. Helps reduce delay (for example, challenge periods) in final settlement

---

## **Espresso**

- Espresso Docs: [https://docs.espressosys.com](https://docs.espressosys.com/?utm_source=chatgpt.com)

### **Overview**

- Espresso is a **shared sequencing layer** for rollups, designed to provide **fast confirmations** and **decentralized ordering** across many L2s
- Uses the **HotShot BFT consensus** protocol to achieve near-instant confirmations (seconds), enabling better UX and cross-rollup composability
- Supports integration with multiple rollup stacks (OP Stack, Polygon CDK, Arbitrum Orbit, etc.), allowing those chains to opt-in to Espresso sequencing while keeping their own execution/proof systems
- **Not a RaaS platform**: Espresso does not spin up rollups directly (unlike AltLayer). Instead, it provides a common sequencer/DA service that existing rollups can plug into

### **Tokenomics**

- **Functions of ESP**:
  1. Utility and governance token for the Espresso L2 network
  1. Governance: holders vote on protocol upgrades and policy changes
  1. Sequencer and DA rewards: payment for validation and data availability services
  1. Ecosystem incentives: staking, airdrops, and developer/user rewards
- **Supply / Distribution**:
  - Chain: Ethereum L1 (ERC-20 token)
  - Total supply: 1,000,000,000 ESP
  - Circulating: ~100–200M ESP (~10–20%) post-IDO
  - Splits among team, investors, community/ecosystem, foundation, and marketing
- **Roadmap (PoS transition)**:
  - Espresso plans to introduce **PoS-based validators/sequencers**, who will stake a (future) native token to participate
  - Stakers will earn sequencing/confirmation fees and be subject to slashing for misbehavior

### **Security**

- **HotShot Consensus**: BFT protocol that finalizes ordering within seconds; ensures safety and liveness with a small validator set (currently permissioned).
- **EspressoDA**: a three-layer data availability subsystem designed to work natively with HotShot:
  - **VID Layer**: erasure-coded data chunks distributed to all nodes.
  - **DA Committee Layer**: small group stores full data and guarantees recovery.
  - **CDN Layer**: improves efficiency of data retrieval.
- **Roadmap**: EspressoDA + HotShot will eventually be secured by PoS validators (permissionless), providing both sequencing and DA guarantees.

---

## **Snapchain**

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

## **Caldera**

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

## **Conduit**

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

## Summary

| Project | RaaS Architecture | Tokenomics | DA | Security |
| --- | --- | --- | --- | --- |
| AltLayer | Full-stack RaaS (multi-stack launchpad) | ALT token (ERC-20). Staking, governance, protocol fees, incentives | Ethereum, Celestia, EigenDA (modular) | AVSes: VITAL (validators), MACH (finality/ZK), SQUAD (sequencers) |
| Espresso | Shared sequencing / confirmations | ESP token (ERC-20). Governance, sequencer & DA rewards, staking incentives
 | EspressoDA (VID, DA Committee, CDN) | HotShot BFT (permissioned now, PoS later) |
| Caldera | General-purpose RaaS | No native token. Tenant pays fees. Gas in ETH/stable/custom | Ethereum or Celestia | Depends on config: OP Stack (fraud proofs), zkEVM (validity proofs) |
| Conduit | Managed RaaS (OP Stack) | No native token. Subscription/management fees | Ethereum DA (default), Celestia/EigenDA roadmap | Inherits OP Stack + Ethereum settlement |

# **Shared Security Models and Formal Implications**

### **1. Background**

In multi-layer rollup architectures, such as those separating sequencer and validator domains, system security can be categorized as:

- **Model M (Modular / Independent):** each layer maintains its own security boundary; a failure in one domain compromises that domain only.
  - Example - Most of multi-layer rollup architectures
- **Model S (Shared / Unified):** a single verification or slashing layer enforces correctness and accountability across all subordinate layers, creating collective defense.
  - Example - AltLayer’s SQUAD/VITAL (Shared Sequencer/Validator Set)

---

### **2. Basic Formulation**

Let

- $C_i = \theta_i \Delta_i$: the minimum economic cost to corrupt layer $i$
($\Delta_i$ = total stake or weight, $\theta_i$ = fraction required for control)
- $\pi$: expected payoff from a successful attack

**Model M – Independent Security:**

$C_{\text{attack}}^{(M)} = \min\{C_1, C_2, \dots, C_k\}$

**Deterrence:** $\min\{C_i\} > \pi$

**Model S – Shared Verification Layer:**

$C_{\text{attack}}^{(S)} \approx \sum_{i=1}^{k} w_i C_i,
\qquad w_i \ge 0,\; \sum w_i \ge 1$

**Deterrence:** $\sum_{i=1}^{k} w_i C_i > \pi$

→ Attack cost rises from a *minimum* (weakest-link) to a *weighted sum* (aggregate defense), quantitatively capturing the advantage of shared security.

---

## **3. Detailed Formulation (Validator Set/OP-Assumption, One-Honest-Suffices)**

Base equation

$\mathbb{E}[C_{\text{attack}}] = dS + (1-d)kHM$

- $d$: detection probability
- $S$: loss upon detection (slashing, penalties, reverted profit, etc.)
- $kHM$: expected cost to bribe or suppress challengers
  - $k$: per-validator bribe cost
  - $H$: honest share
  - $M$: effective validator count

---

### **(1) Without Shared Security —**

### **Model M**

$\mathbb{E}[C]_{\text{M}} = dS_{\text{local}} + (1-d)kH M_{\text{local}}$

- Each rollup has its **own validator pool**.
- The attacker only needs to corrupt validators of the targeted rollup.
- $S_{\text{local}}$ is small → weak deterrence.

---

### **(2) With Shared Security —**

### **Model S**

$\mathbb{E}[C]{\text{S}} = dS_{\text{shared}} + (1-d)kH M_{\text{shared}}$

- A **common validator set** protects all rollups.
- $S_{\text{shared}}$ includes shared-stake slashing → larger detected-loss term.
- Since $M_{\text{shared}} > M_{\text{local}}$, non-detection bribery also becomes harder.
- Result: much stronger deterrence.

### **3. Immediate Implication**

- Under Model M, compromising the least-secure domain is sufficient to undermine the system.
- Under Model S, an attacker must corrupt multiple domains that are jointly verified.
- The mathematical shift $\min → \sum$ represents the core security amplification achieved through shared-security design.

## **Possibility of Shared Security Layer for Tokamak’s L2 platform**

### **1. Scenario I - Shared Validators Set**

Introducing Tokamak’s validation (or RAT) layer as the *shared verification and slashing mechanism* changes the security structure fundamentally:

Even if sequencer sets remain modular, a single** top, shared layer enforcing global accountability** yields:

$C_{\text{attack}}^{\text{system}} \approx \sum_{i=1}^{k} w_i C_i$

The entire rollup architecture thus inherits **Model S-level deterrence**, because successful compromise now requires defeating the top verification layer’s additional, unified slashing rule.

### **2. Scenario II - RAT on Top of Modular Validators Set**

Validators are randomly tested with test rate $p$, and Tokamak bears an accountability cost $L_{\text{Tokamak}}$ if misbehavior is undetected. This can create deterrence through oversight rather than pooled collateral.

$C_{\text{attack}} = \displaystyle \min_i \big(\alpha(p)\,C_i\big),~~~~~p \ge \tau$

- $\tau:$ activation threshold — the minimum test rate required for the system to reach effective deterrence
- $\alpha(p)$: activation function; scales the validator’s effective cost once $p$ exceeds $\tau$

When

$\displaystyle \min_i \big(\alpha(p)\,C_i\big) > \sum_i w_i C_i,$

An RAT-added model can achieve stronger deterrence than stake-based Model S systems.

### **3. Scenario III - RAT + Shared Validators Set**

When the audit probability $p$ exceeds the activation threshold $\tau$, the shared-validator (Model S) security cost — the aggregate deterrence across all rollups — is amplified by the activation factor $\alpha(p) > 1$. RAT thus strengthens the entire system’s deterrence once activated.

$C_{\text{attack}} \;=\; \alpha(p)\,\sum_{i} w_i\,C_i \qquad (p \ge \tau)$

| **Architecture** | **Attack Cost** | **Behavior** | **Security Responsibility** |
| --- | --- | --- | --- |
| Model M | $C_{\text{attack}}=\min{C_i}$ | Weakest-link; localized compromise | Layer-local |
| Model S (Shared staking) | $C_{\text{attack}}=\sum_i w_i C_i$ | Aggregate defense; multi-layer breach required | Shared / Unified |
| Shared validator set | $C_{\text{attack}}=\sum_i w_i C_i$ | Equivalent deterrence if the top layer enforces unified accountability | Shared / Unified |
| RAT only | $C_{\text{attack}} = \displaystyle \min_i \big(\alpha(p)\,C_i\big)$ | Probabilistic deterrence: mix of oversight and weakest-link; RAT triggers enforcement when caught | responsibility remains primarily layer-local |
| RAT + Shared validator set | $C_{\text{attack}} \;=\; \alpha(p)\,\sum_{i} w_i\,C_i$ | Amplified aggregate defense: shared staking deterrence multiplied by RAT activation | Shared / Unified (aggregate security, enhanced by RAT oversight) |

### 4. Shared security at the validator level alone would be sufficient?

- **Security Transfer** - security accountability can propagate upward rather than being distributed across all layers
- A single accountable top layer (i.e., the validator level) can ensure systemic deterrence across multiple validator or sequencer sets, without requiring full shared staking across every rollup

# **Other Considerations and Takeaways**

### 1.  Modular Design

- Each module (*VITAL*, *MACH*, *SQUAD*) has a **clear technical role** and a **memorable identity**, making the system easier to explain and adopt.
- **Modular Branding – **Names like *VITAL*, *MACH*, *SQUAD* show how strong branding enhances comprehension and trust.
- **Tokamak** also may need to consider naming its additional, unified security layer - e.g., **Sentinel (RAT)**.

### 2. Shared Security** (Model S/Shared Security) and Token Value Dynamics**

- **Security aggregation efficiency** reduces the total stake S required for the same security level, freeing some capital into circulation and slightly increasing **velocity **$V$.
- At the same time, network trust and reliability improve, raising **utility **$U$.
- Token value roughly follows $P \propto U/V$.
- If the increase in utility outweighs the rise in velocity — $\Delta U > \Delta V$
— overall token value strengthens.
- Thus, shared security can **raise liquidity without weakening value**, turning efficiency gains into **utility-driven appreciation** rather than dilution.

### 3. **Performance Layer – Lessons from AltLayer’s MACH**

- AltLayer’s **MACH** shows the value of a **hybrid model** combining optimistic speed with ZK verification - In partnership with Sussinct Labs [[Link](https://blog.altlayer.io/altlayer-partners-with-succinct-bringing-op-succinct-to-developers-77a7630d8a16)]
- Tokamak can adopt a similar approach:
  - Use higher fees for **fast-finality** when speed matters.
  - Switch to **zkEVM** for high-assurance or dispute-sensitive cases.
- This adaptive use of Tokamak’s **multi-stack design** balances **speed, cost, and security** efficiently.

### **4. Fully Managed vs. BYO Cloud**

- Most leading RaaS platforms (e.g., **AltLayer**, **Caldera**, **Conduit**) provide **fully managed** infrastructure — developers launch a rollup through a simple dashboard or API, with all sequencing, DA, and monitoring handled automatically.
- In contrast, **Tokamak** currently follows a **BYO Cloud** model: developers must deploy and maintain their own hosting and validator nodes.
- Moving toward a **fully managed (optional) deployment mode** would significantly improve **developer UX and onboarding**, reducing setup friction and aligning Tokamak with modern RaaS usability standards.