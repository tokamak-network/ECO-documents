## I. Introduction

- Problem Statement: Fragmentation of economic security in the L2 ecosystem.
- Solution: Tokamak Network's "Economics Whitepaper V2" and the proposed shared verification economics layer.
- Core Focus: Solution to the Verifier's Dilemma.

## II. The Verifier's Dilemma in L2 Ecosystems

- Definition: Verification as a public good, leading to rational actors abstaining from work.
- Amplification in L2s: Large rollups can afford security; small/niche rollups create a security vacuum.

## III. Tokamak's Multi-tier Security Layer

- Three Tiers of Security:
**Tier 1: Public Challenge (Fraud Proofs)**

This is the foundational layer common to optimistic rollups. It allows any participant to submit a fraud proof to the L1 if they detect an invalid state transition.

  - Mechanism: If a sequencer's state transition is proven fraudulent, the sequencer's bond is slashed.
  - Multi-Challenger Approach: Unlike single-winner systems, Tokamak rewards all valid fraud proofs submitted within the dispute period. This prevents "front-running" or exclusion by malicious L1 proposers.
  - Limitation: It does not guarantee that any specific party is actively monitoring the network at any given time.

**Tier 2: Dedicated Validators**

This tier introduces professional entities that have a formal obligation to monitor the network.

  - Mechanism: Validators must stake TON as collateral. They are eligible for protocol-level incentives and bounties from successful challenges.
  - Shared Validator Set: A single validator can monitor multiple L2s. This allows smaller L2s to inherit security from the global TON staking pool without bootstrapping their own validator sets.
  - Limitation: Validators still face the Verifier's Dilemma, as they may be tempted to "free-ride" on the efforts of others to save operational costs.

**Tier 3: Randomized Attention Test (RAT)**

The RAT is the primary mechanism for ensuring continuous validator engagement by addressing the incentive problem of Tier 2.

  - Mechanism: The protocol selects validators at random intervals to verify specific L2 transaction batches. Validators must submit an attestation within a defined timeframe.
  - Economic Alignment: Failure to provide a timely attestation results in a portion of the validator's stake (the Coff penalty) being slashed. The penalty is mathematically calibrated so that the expected cost of inattentiveness exceeds the cost of continuous monitoring (cm).
  - Outcome: Because selection is unpredictable, consistent monitoring becomes the only rational and profitable strategy for validators.
- Model Scope: Proof-system agnostic (secures optimistic and ZK proofs).
- Paradigm Shift: Eliminating the need for independent security bootstrapping.

## IV. The Randomized Attention Test (RAT)

- Purpose: Ensures continuous validator engagement.
- Mechanism: Random selection of validators to verify transaction batches; attestation required within a short window.
- Economic Alignment: Penalty for failure ensures cost of inattentiveness exceeds cost of monitoring

## V. Evolution of Economic Philosophy

- Shift in Focus: From individual L2 growth to collective economic security.
- Updated Seigniorage Model (TON Staking V3):
  - Metric: Rewards based on "Bridged TON" (actual economic activity) instead of raw TVL.
  - Distribution: Sigmoidal function to mitigate excessive concentration.

## VI. Practical Application of the Economic Model

- Example 1:  Sequencer’s POW: Sequencer Reward Calculation
DeFi-Chain Bridged TON: 1,000,000 TON

  - Total Ecosystem Bridged TON: 50,000,000 TON
  - Total Seigniorage Rewards: 100,000 TON
  - Your Reward Calculation:(Your Bridged TON / Total Bridged TON) * Total Seigniorage Rewards = (1,000,000 / 50,000,000) * 100,000 TON = 2,000 TON
- Example 2: Validator’s POW: Calculate payoffs for 02 scenarios: (i) attentive and (ii) inattentive in presence of RAT and a hypothetical amount of base seigniorage reward)
  - Your Stake: You have 50,000 TON staked as collateral deposit. Let’s assume this is the minimum stake required to participate as a validator.
  - Cost of Verification: operational cost to stay online and attentive for a given period is equivalent to 1 TON.
  - The seigniorage reward for this period is 100 TON
  - RAT Parameters:
    - The reward for a valid challenge is 10 TON.
    - The penalty for failing a RAT (slashing) is 1,000 TON.
    - The probability of being selected for a test in any given period is 10%.

Payoff for being attentive = Base seigniorage reward + expected RAT reward - costs = 100+ 0.1*10 -1 = 100 (TON)

Payoff for being inattentive = operation cost saved + expected RAT penalty = 1 + 0.1*(-1000) = -99 (TON). This would be deducted to the staked amount
- Example 3: User’s POW: Immediate Asset Exit & liquidity providing via fast withdrawal
  - A user initiates a withdrawal of 1,000 TON from an L2 to L1. Standard optimistic rollups impose a 7-day challenge period.
  - A Fast Withdrawal provider, acting as an economically motivated verifier, assesses the L2 state. The provider's confidence in the state's validity is high due to the three-tier security system (Public Challenge, Dedicated Validators, and RAT).
  - The provider immediately fronts the 1,000 TON to the user on L1, minus a small fee. If the L2 state went unchallenged, after 7 days, the provider received the "locked" 1,000 TON that was supposed to be withdrawn by the user. If the L2 state were later proven fraudulent, the provider is compensated by the slashing of the Sequencer's bond or the Validator's stake

## VII. Conclusion

- Summary: Robust framework addressing Verifier's Dilemma and economic fragmentation.