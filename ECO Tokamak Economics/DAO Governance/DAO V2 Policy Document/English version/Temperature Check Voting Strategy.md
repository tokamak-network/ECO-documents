**Tokamak DAO’s Temperature Check (Temp Check) Stage** is a non-binding voting phase designed to quantitatively gauge the community’s opinion on a proposal before it advances to on-chain voting. In this stage, Snapshot is used to verify whether the community supports the proposal.

# 1. Voting Weight Model

To design a fair governance voting weight model, it is essential to balance the influence of each asset so that no single asset holder can easily dominate the vote. In this model, the weight functions for the three types of assets are defined as follows:

- **sWTON (Staked WTON):** A 1:1 weight is applied so that each staked WTON token is given one vote.
- **TON:** A quadratic (square-root) weight is applied.
- **WTON:** A lower weight than TON’s voting influence is applied, ensuring that, especially for holdings below 100,000 TON, holding TON is more advantageous than holding WTON.

This approach aims to reward participants with long-term staking and to grant relatively lower voting power to liquidity providers, thereby promoting decentralization in governance. Below, the weight functions for each asset and corresponding scenarios are described in detail.

## 1. Weight Functions and Design Rationale

### 1.1 sWTON – **Linear 1:1 Weight**

**Weight Function:**

$W_{sWTON}(x) = x $ (one vote per sWTON token)

**Design Rationale:**

sWTON represents tokens staked specifically for governance participation. Since staked tokens demonstrate long-term commitment and trust in the network, they are awarded a 1:1 weight. This ensures that stakeholders who lock up their tokens gain voting power equal to the number of tokens staked, encouraging active governance participation.

---

### 1.2 TON – **Quadratic Weight**

**Weight Function:**

$W_{TON}(x) = \sqrt x $ 

**Design Rationale:**

For the general liquid token TON, a square-root function is applied to determine the voting weight. This method means that while voting power increases as the token holding increases, the rate of increase gradually tapers off. For example, holding 25 TON yields 25=5 $\sqrt 25 = 5$ votes, and holding 100 TON yields $\sqrt 100 = 10$

- **Effect:**
The quadratic weighting helps prevent large holders from exerting excessive influence. Smaller holders, on a per-token basis, enjoy relatively higher voting effectiveness, thereby promoting governance decentralization.

---

### 1.3 WTON

**Weight Function:**

- $W_{WTON}(x) = k ⋅ x, (0 < k <1)$
- In this model, $k = 0.003$

**Objective:**

To ensure that, especially for amounts below 100,000 TON, holding TON is more advantageous than holding WTON.

**Example:**

- Holding 100,000 WTON : $100,000 × 0.003 = 300$
- Holding 100,000 TON : $\sqrt 100,000 ≈ 316.22$


**Adjustability:**

The value of kk can be adjusted as needed.

---

## 2. Scenario Examples

Below are three scenarios that demonstrate how the model operates in practice:

### Scenario 1: Small Holder vs. Small Liquidity Provider

- **Holder A:** 10,000 TON (liquid holding)
- **Holder B:** 10,000 WTON (liquidity pool holding)
- **Holder C:** 10,000 sWTON (staked)

**Voting Power Calculation:**

- **Holder A (10,000 TON): **10,000 TON → $\sqrt 10,000 = 100$ Votes
- **Holder B (10,000 WTON): **10,000 WTON → $10,000 × 0.003 = 30$
- **Holder C (10,000 sWTON): **10,000 sWTON ⇒ 10,000 Votes

In this scenario, Holder C (staked sWTON) obtains the highest voting power. For the same amount of 10,000 tokens, the TON holder (Holder A) gets 100 votes, while the WTON holder (Holder B) gets only 30 votes. This demonstrates that holding TON is more advantageous than holding WTON, and that staking further amplifies influence.

---

### Scenario 2: Medium-Sized Holder – TON vs. WTON vs. Mixed Holding

- **Holder A:** Holds 500,000 TON.
- **Holder B:** Holds 500,000 WTON.
- **Holder C:** Holds a mix: 250,000 TON + 250,000 WTON.

**Voting Power Calculation:**

- **Holder A (500,000 TON): **500,000 TON** → **$\sqrt 500,000 ≈ 707$** **Votes
- **Holder B (500,000 WTON):  **500,000 TON → $500,000 × 0.003=1,500 $ Votes
- **Holder C (250,000 TON + 250,000 WTON): **$\sqrt 250,000 + (250,000 * 0.003)=500+750=1,250$** **Votes

Here, a holder with 500,000 TON receives about 707 votes, while an equivalent amount in WTON yields about 1,500 votes. The mixed holder gains a total of approximately 1,250 votes. This indicates that above 100,000 TON, holding WTON becomes more beneficial in raw vote count, reflecting the design objective that TON is more favorable in smaller amounts.

---

## 3. Maintaining Decentralization and Preventing Governance Capture

This model is designed to promote decentralization and prevent a few large holders from dominating the vote:

- **Staking Incentive:**
sWTON offers a 1:1 weight, encouraging users to stake their tokens. This ensures that committed, long-term participants have maximum voting power.
- **Quadratic Weighting for TON:**
The square-root function limits the influence of large liquid TON holdings, ensuring that a concentration of tokens does not translate into proportionally excessive voting power.
- **Discounted Weight for WTON:**
By applying a 0.003 multiplier to WTON holdings, the model discourages reliance on liquid tokens for voting, thereby incentivizing users to convert to either TON or sWTON to maximize their influence.
- **Combined Effect:**
These mechanisms work together to prevent governance capture by ensuring that large holders must either commit (stake) or accept reduced influence. The design aims to secure a broad and decentralized base for decision-making.

---

# 2. Participation Requirements

- **Minimum Token Balance:**
For example, requiring that a voting address must hold at least **1,000 TON/WTON/sWTON** (or be delegated that amount) to participate ensures that addresses with extremely small balances do not influence the vote. This minimum is critical for mitigating Sybil attacks.
- **Delegation Requirement:**
Additional measures, such as verifying that a significant portion of a voter’s tokens is delegated to a representative, can further ensure that only genuine, engaged stakeholders participate.

These requirements can be implemented through Snapshot’s verification strategy and adjusted via community consensus if needed.

---

# 3. Utilizing the Snapshot Strategy

Tokamak DAO uses the off-chain voting tool **Snapshot** to conduct the Temp Check. Snapshot allows participants to vote without incurring gas fees, and it automatically aggregates token balances according to the defined strategy (i.e., reading TON, WTON, and staked TON balances).

The strategy relies on the correct configuration of weight functions and participation thresholds to ensure that the vote is both efficient and fair.

---

# 4. Security Council Intervention

Before a proposal is advanced to on-chain voting, the **Security Council** has the option to review and, if necessary, exercise a veto on the proposal based on the Temp Check results.

- The Security Council operates via a multisig system, requiring a 2/3 majority of signatures to veto a proposal.
- If a proposal receives over a certain threshold of support (for example, 66% approval) in the Temp Check, the Security Council’s intervention is limited to respect the community’s decision.
- If the Security Council does veto a proposal, it will not proceed to on-chain voting, and the proposer must return to the RFC stage, incorporating feedback before resubmission.

This mechanism ensures that in cases of clear security concerns or emergency, the community’s interest is protected while normally deferring to the collective will.

---

# 5. Governance Quality Control and Redundancy Prevention

Tokamak DAO implements several measures to prevent the abuse of the governance process and to maintain high proposal quality:

- **Proposal Submission Requirements:**
To initiate a Snapshot Temp Check vote, a voting address must hold or delegate a minimum amount of tokens (for example, at least 1,000 TON). This requirement helps prevent the submission of frivolous proposals by ensuring that only addresses with a meaningful stake can participate.
- **Duplicate Proposal Prevention:**
Voters are encouraged to review the existing proposal archive before submitting new proposals. If a similar proposal has already been submitted, a cool-down period (e.g., at least one month) is enforced to discourage redundant proposals.
- **Compliance with Procedures:**
Every proposal must follow the established RFC template and guidelines. If essential elements are missing, the operating team may request revisions or reject the proposal.
- **Moderator and Community Feedback:**
Moderators and active governance participants review the discussions during the RFC phase to ensure that proposals receive sufficient feedback. Proposals that do not meet the necessary standards may be sent back for improvements.

---

# 6. Final Notes

This document outlines Tokamak DAO’s Temperature Check (Temp Check) voting strategy using Snapshot. The strategy employs a voting weight model that assigns:

- 1:1 weight for staked tokens (sWTON),
- Quadratic (square-root) weighting for TON,
- A reduced linear weight (0.003 multiplier) for WTON.

Additional participation requirements (such as a minimum of 1,000 TON/WTON/sWTON per address) and Security Council intervention mechanisms are established to ensure fair, decentralized governance and to mitigate Sybil attacks.