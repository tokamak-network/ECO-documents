## 1. Architecture Overview & Design Principles

This governance model pursues performance-driven governance for the sustainable growth of Tokamak Network. It seeks complete alignment between the economic model and governance by combining decision-making authority with practical activities such as strengthening network security and securing ecosystem liquidity, going beyond simple asset holding.

### 1.1. Background & Motivation

The Layer 2 (L2) rollup ecosystem, which emerged to address Ethereum's scalability issues, is evolving beyond general-purpose solutions toward an era of application-specific rollups (App-specific Rollups). However, small to medium-sized independent rollups have a structure vulnerable to the 'Verifier's Dilemma,' where validators abandon voluntary monitoring because the rollups fail to provide sufficient economic compensation relative to the operational costs required for verification. This makes network security dependent on a small number of participants, intensifying censorship and operational risks.

Tokamak Network overcomes these structural limitations by building a **Shared Verification Economics layer**. On this layer, the **TON token** functions as a **unified economic asset** that binds together security collateral, gas fee payments, and decision-making rights, tightly connecting network security with economic activity.

This governance model adopts the **'performance-driven distribution' philosophy of Tokamak Economic Model V3** for the efficient operation of TON, which plays this integrated role. By directly linking decision-making authority not to simple asset holdings but to actual ecosystem contribution (Bridged TON), it establishes a sustainable virtuous cycle ecosystem led by operators and validators, who are the real engines of the network.

### 1.2. Alignment of Economics & Governance

This model follows three core principles based on the premise that **"if the economic model is the engine, the governance model is the steering wheel"**:

- **Performance-driven Governance**: Governance authority is calculated in proportion to actual performance (Bridged TON) contributed to the network ecosystem, not token holdings.
- **Skin in the Game**: Those with decision-making authority bear economic responsibility for their decisions. Non-participation in voting or malicious behavior is subject to punishment.
- **Optimistic Control**: All proposals are voted on swiftly by L2 operators. At the same time, a 'Challenge Window' is provided where validators can raise objections to maintain system integrity.

### 1.3. Governance Participants & Hierarchy

Governance participants are divided into the following roles to simultaneously secure **openness** and **expertise**, and to establish an **'optimistic checks and balances system'** that prevents monopolistic control by specific entities:

- **Proposer**: **Anyone** wishing to contribute to the development of the Tokamak ecosystem can submit proposals. By lowering the governance entry barrier, creative ideas from various L2 solutions and users are reflected in policies.
- **L2 Operators (Voters)**: Vote on proposals with **voting power proportional to Bridged TON performance**. As entities leading network growth, they drive decision-making while being under constant monitoring by validators.
- **Validators (Challengers)**: Monitor operators' voting processes and results in real-time, performing a **'checks and monitoring'** role. If operators make decisions that harm network security or economic stability, they can immediately suspend proposal execution through **'governance challenges'** and transfer them to the Tokamak Foundation, the higher arbitration body.
- **Tokamak Foundation (Arbiter)**: The **highest-level arbiter** that conducts final reviews and rulings on the technical and economic integrity of challenged proposals. When the executive power of operators and the monitoring power of validators conflict, it makes final approval or rejection decisions based on the system's long-term sustainability and security principles.

### 1.4. Progressive Decentralization: Transitional Arbitration Model

While complete decentralized governance is a goal to pursue, in the early stages of a complex rollup ecosystem, it is difficult to manage decision-making paralysis or governance attack risks. Therefore, this model introduces a Foundation arbitration model as an **'Intermediate Stage'**.

- **Bridge from Centralization to Decentralization**: To address the power concentration issues of centralized structures, voting power is distributed based on performance. At the same time, system stability is secured through Foundation verification at the final execution stage.
- **Need for Technical Arbitration**: Changes to rollup parameters (challenge windows, slashing ratios, minimum staking requirements, etc.) require highly technical judgment. Foundation intervention following validator challenges functions not as simple exercise of power, but as a 'technical guardrail' that protects system integrity.
- **Evolutionary Roadmap**: As the ecosystem matures and the stability of governance algorithms is proven, the Foundation's arbitration authority will be gradually transferred to on-chain committees or algorithm-based automated execution systems. Complete decentralization is the ultimate goal.

## 2. L2 Sequencer Governance: Voting & Responsibility

L2 operators (Sequencers) are the core driving force leading the growth of the Tokamak Network ecosystem. Operators have decision-making authority proportional to the performance they have attracted. Governance participation is both a right and an essential responsibility to maintain network operational integrity.

### 2.1. Proposal-specific $vTON$ Issuance and Calculation

To ensure fairness and currency of voting power, all authority is allocated based on actual contributions at the time of proposal (Agenda) $\gamma$ creation.

- **Snapshot and Issuance Mechanism**: At block height $H$ when proposal $\gamma$ is created, proposal-specific voting power $vTON_{i, \gamma}$ is issued for each L2 $i$ based on the quantity of **valid Bridged TON (**$B_{i}$**)**.
- **Voting Power Calculation Based on Saturation Function**: To prevent voting power monopolization by specific large L2s and enable balanced participation by operators of various scales, a hyperbolic saturation function is applied.
$$
vTON_{i, \gamma} = L_{gov} \cdot \frac{B_i}{k_{gov} + B_i}
$$

  - $B_i$: Quantity of valid Bridged TON within the L2 at the time of proposal creation
  - $L_{gov}$: Theoretical upper limit of voting power that a single L2 can possess
  - $k_{gov}$: Semi-saturation point where the marginal utility of voting power begins to decrease
- **Non-transferability and Independence**: Issued $vTON$ is a vested right that cannot be transferred or traded, and its validity expires upon completion of the voting procedure for that proposal.

### 2.2. Voting Participation Obligation

To secure the swiftness and legitimacy of the decision-making process, operators are given an obligation to participate in voting faithfully.

- **Participation Obligation**: All operators granted proposal-specific $vTON$ must record their position (approve, reject, abstain, etc.) on-chain within the designated governance period.
- **Responsibility-based Governance**: Governance participation means that sequencers not only optimize key network parameters such as slashing ratios and minimum staking requirements, but also directly contribute to determining the network's direction and maintaining the activity of the entire ecosystem by expressing their positions on various topics including technical and economic proposals for ecosystem development and community proposals.

### 2.3. Economic Penalties and Eligibility Management

When collateral is deducted for non-participation in voting, it directly affects the operator's reward eligibility.

- **Collateral Slashing (**$T_i$** Slashing)**: If an operator does not participate in voting, a predefined amount of collateral ($T_i$) deposited in the L1 staking contract is deducted and attributed to the DAO treasury ($S_{DAO}$).
- **Eligibility Loss Risk**: If the remaining collateral ($T_i$) falls below the minimum staking requirement due to collateral deduction, the operator immediately loses seigniorage reward eligibility.
  - Eligibility determination formula: The seigniorage distribution eligibility indicator $1_i$ is defined as follows:
$$
1_i = \begin{cases} 1 & \text{if } T_i \ge \theta \cdot B_i \\ 0 & \text{otherwise} \end{cases}
$$

> $T_i$ is the remaining collateral after slashing, $\theta$ is the minimum staking ratio ($\theta \in (0, 1]$), and $B_i$ is the Bridged TON of the L2.
- **Reward Restriction**: Operators who have lost eligibility ($1_i = 0$) are excluded from seigniorage distribution for that round, and the rewards that were scheduled to be allocated are entirely attributed to the DAO treasury.

## 3. Validator Governance: Security Monitoring & Karma

Validators are key entities that monitor operators' decision-making and safeguard the network's security principles. Validators participate in governance through 'governance challenges' and the 'karma system,' which lead to substantial economic rewards.

### 3.1. Participation Eligibility

The authority to raise challenges within governance is limited only to validators who are actually contributing to network security.

- **Economic Collateral (**$D_{validator}$**)**: Validators wishing to exercise challenge authority must stake ($D_{validator}$) a minimum quantity of TON or more as predefined in the L1 contract.
- **Activity Eligibility (RAT Compliance)**: Beyond simple staking, validators must maintain eligibility by passing the **Random Attestation Test (RAT)** defined in Whitepaper V2, proving they are actively monitoring the network.

### 3.2. Optimistic Challenge Process

Validators can block voting results if they determine that operators' voting results harm security or economic stability.

- **Challenge Window (**$W_{gov}$**)**: A grace period given from the end of operators' voting until the proposal is finally executed. (e.g., 7 days)
- **Challenge Execution and Transfer**: When validator $j$ raises a challenge based on technical or security flaws in proposal $\gamma$, the proposal's execution is immediately suspended, and the review is automatically transferred to the Tokamak Foundation.

### 3.3. Administrative Fee Mechanism

To prevent indiscriminate delay attacks (griefing) that may occur in the value judgment domain of governance, a 'participation cost' is designed.

- **Fee Payment (**$F_{challenge}$**)**: A validator submitting a challenge must pay a small administrative fee $F_{challenge}$.
- **Attribution to DAO Treasury**: The paid $F_{challenge}$ is attributed to the DAO treasury ($S_{DAO}$) regardless of whether the challenge is upheld. This serves as both compensation for the Foundation's technical review resources and a minimal economic barrier against system abuse.
- **Fee Adjustment**: In the event of governance paralysis issues, the DAO may increase the baseline value of $F_{challenge}$ through a proposal.

### 3.4. Karma and Protocol Integrity Verification

Karma ($K$) is a quantified metric of a validator's contribution to **filtering quality** and **protocol integrity protection** performed within the governance process. This goes beyond simply opposing proposals, encouraging validators to verify that operator decisions comply with the network's standard guidelines.

- **Karma Attribution Criteria**: The Tokamak Foundation reviews challenged proposals according to the following criteria and awards karma points $K_j$:
  - **Risk Detection Accuracy**: Did the challenge technically and accurately identify potential threats that the proposal poses to security parameters or the economic stability model?
  - **Necessity of Verification**: Even if the challenge is ultimately rejected, was the objection of value that warranted public examination for the integrity of the protocol?
- **Reward for Integrity Filtering**: Karma is granted to validators who perform governance challenges based on reasonable grounds. This is a core mechanism that enables validators to act as **final Quality Assurance** agents of the system without fear of slashing.

### 3.5. DAO Vault-Based Bonus Distribution

This model operates by clearly separating the 'fixed security reward' at the protocol layer from the 'flexible contribution bonus' at the governance layer.

- **Dual Reward Structure**
  - **Base Seigniorage (**$v_j$**)**: Fixed seigniorage paid by the protocol as compensation for security monitoring (such as passing RAT), based on Whitepaper.
  - **Governance Bonus (**$B_j$**)**: Additional incentive paid from the DAO treasury ($S_{DAO}$) to validators who have earned karma.
- **Reward Calculation Formula**: The total reward received by validator $j$ is defined as follows:
$$
Total\_Reward_j = v_j + B_j(K_j)
$$
- **Cumulativeness of Karma and Scalability of Rewards**: In this model, karma ($K_j$) is defined not as a one-time point but as a validator's 'cumulative reputation asset'. Karma is not reset and remains as an immutable record. Each time accumulated karma exceeds a threshold, the tier of the bonus payout rate ($B_j$) increases. Through this mechanism, long-term contributors experience a compounding reward structure where they earn progressively higher marginal returns over time.

## 4. Foundation: Final Arbitration & Ecosystem Protection

The Tokamak Foundation serves as the **supreme arbitration body** that maintains the technical integrity of the system and mediates conflicts among governance participants during the transitional phase toward decentralization.

### 4.1. Final Judgment and Arbitration (Final Arbiter)

The Foundation has final judgment authority over proposals challenged by validators.

- **Judgment Guidelines**: The Foundation reviews the validity of proposals based on the following three criteria:
  - **Security Integrity**: Does the proposal endanger the network's security parameters (slashing ratio, challenge window, etc.)?
  - **Economic Stability**: Does the proposal harm the overall ecosystem's reward balance ($\theta$, $\alpha$, $k$, etc.) for the benefit of specific entities?
  - **Protocol Consistency**: Is the proposal aligned with Tokamak Network's long-term roadmap and core philosophy?
- **Final Effect**: According to the Foundation's judgment, the proposal is either finally approved for execution or rejected and discarded.

### 4.2. DAO Treasury ($S_{DAO}$) Management and Redistribution

The Foundation manages assets flowing in from the governance process and redistributes them to active participants in the ecosystem.

- **Asset Inflow**: Includes slashed funds from operator non-participation, validators' administrative fees ($F_{challenge}$), and the treasury's allocation from protocol seigniorage.
- **Asset Outflow**:
  - **Governance Incentives**: Bonuses ($B_j$) paid to karma-holding validators.
  - **Ecosystem Development Fund**: Support for public goods and incentives for new L2 projects.
  - **Risk Management**: Security audits and protocol emergency maintenance costs.

### 4.3. Role in Progressive Decentralization

This model serves as an **interim bridge** for transitioning from centralized decision-making to a fully algorithmic DAO. The Foundation acts as a guardrail preventing catastrophic losses from governance attacks or technical errors, and as the network matures, these arbitration criteria will be codified into on-chain rules, with authority gradually transferred.