Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-03-28

**Note:** The core development team of TRH (Lead: Theo) should be involved and kept informed throughout the process.

# Construction of Chapter 3. Verification Economics

Global issue: Concepts of Proposer and Sequencer are not defined in this paper. 

- Recent Ethereum articles specify and distinguish sequencers and proposers w.r.t. PBS (Proposer Builder Separation) scheme

## 3.1. Challenge

Concerns:

1. Ambiguous information in 3.1.2. Procedure 
  - e.g., 7 or 14 days challenge period → 7 days challenge period
1. The group challenge system is not in the implemented dispute games
1. No exact information of the reward amount for the challenge winner
1. The statement "The challenger inherits the rights of the sequencer" seems to greatly exceed the intended role of the challenger (validator) and appears unrealistic in various scenarios

Revision directions:

1. Perhaps, we need to define characteristics of the L2 validator economy prior to working on this section
1. Formal description for challenge economics
1. Clear wording and notations

## ~~3.2. Fast Withdrawal~~

**This section will be removed**

Identified issues:

1. The direction of fast withdrawals using staked TON is still valid → should be checked with Kevin
  - <u>**Kevin said this section should be deprecated **</u>

## 3.3. Verifier’s Dilemma

Concerns:

1. <u>***Attention test***</u> is still valid? or should be deprecated?

Revision directions:

1. WIP

### References

[https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#3-verification-economics](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#3-verification-economics)