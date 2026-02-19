## Table of Contents

- [Disccusion](/2a1d96a400a380ae9fe1ff591563a0b4#2a1d96a400a381039f69e09333519108)
- [Old structure](/2a1d96a400a380ae9fe1ff591563a0b4#2a1d96a400a381c19210da3618887f79)
- [New structure](/2a1d96a400a380ae9fe1ff591563a0b4#2a1d96a400a3817cb8e8f86febbcc35c)

## (Discussion) Existing Structure Review & Comment

### Background summary → Summary or Executive Summary

### TL;DR → If there is a summary, it is natural not to include it at the whitepaper level

### 1. Terminology

- Main comment: This section should be removed in the new version. Many of the terms are not too difficult to understand now that rollups and coins are emerging as major solutions, and the context is clearly defined in the text to avoid misunderstandings.
  - Operator-Sequencer-Proposer definition
  - inflation case, completely different definitions
  - DTD → Dispute window
  - Deposit → refine to Bridged Deposit to L2, etc.
  - Withdraw → not defined, better judged by context
  - Bridging ? L2 → L1 / L1 → L2
  - Fraud proof / Validity proof → No problem to remove it
- **However, Seigniorage is unfamiliar, so it should be introduced or as a footnote. **

### 2. Seigniorage

- Overall rewrite with new Tokenomics specification
- Introduce new Tokenomics specification as TON staking V3
- TON staking V1, V2 are separated into links or appendixes of previous versions (unnatural flow)
- 2.3 Sustainable growth of L2 is closer to the design intent and should not appear after the TON staking specification, which is currently at a very abstract level. Therefore, the new Tokenomics design intent should be explained first before the TON staking V3 specification, while reflecting the existing 2.3 intent within it. 

### 3. Verification economics

- Existing: Introduction to the challenge system → FW → Verifier's dilemma
- New: Optimistic rollup and verifier problems (verifier's dilemma, decentralization, verifier incentives) → System architecture: Challenge system and shared validators that meet security goals → Mechanisms to mitigate verifier problems (RAT, FW, etc.)
- **Economic feasibility of validation proof in the abstract? → If this part is not included, the utility of TON converges to zero when switching to validation proof.**
  - We are assuming that the dispute window is of significant duration. If this is reduced to a significantly smaller window, → consideration needed (important)

### 4. Utilities of TON

- L2 deposit (security) → L2 fee → DAO

### ~~5. Validity Proof → Privacy support~~

- Ooo project related contents (privacy transaction through zk state channel)

### 6. Examples → Removed → Supplemented separately with blog post

## Old Structure

1. Terminology
1. Seigniorage
  1. Sieg. generation
  1. Seig. distribution
    1. TON staking V1
    1. TON staking V2
  1. Sustainable growth of L2
    1. Quantitative/Qualitative growth of L2
    1. Alleviation of L2 fee token dilemma
1. Verification economics (Note the capitalization at the end)
  1. Challenge
  1. Fast withdrawal
  1. Verifier's dilemma
1. Utilities of TON
  1. Sustainable growth of L2
  1. Enhanced L2 security
1. Validity Proof
1. Examples
1. References
1. Appendix

## New Structure

1. Siegniorage
  1. Sustainable growth of L2
  1. Seigniorage generation
  1. Seigniorage distribution: TON staking V3
1. Verification economics
  1. Optimistic protocol and verification concerns
  1. Economics structure
  1. Risk mitigation mechanisms
    1. RAT (Randomized Attention Test)
    1. FW (Fast Withdrawal)
1. Utilities of TON → First section looks natural
  1. L2 Security
  1. L2 Gas
  1. TON DAO
1. ~~Privacy Support~~
  1. About ZK state channel
1. Reference
1. Appendix
  1. Terminology (if needed)
  1. TON staking v1, v2

## Final structure: "Verification economics → Demand → Supply" 