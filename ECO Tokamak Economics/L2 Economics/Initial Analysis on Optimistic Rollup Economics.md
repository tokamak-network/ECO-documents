Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-02-11

In this document, where the terms '<u>**fraud proof**</u>' and '<u>**fault proof**</u>' are used interchangeably in the context of Optimistic Rollups to refer to the mechanism that challenges invalid state transitions, we have chosen to use 'fraud proof.’ It is because the challenge is to target malicious behaviors rather than accidental faults.

## Notation

$D$: Proposer’s deposit

$T$: Challenge duration

$S$: Proposed state update

$F$: Submitted fraud proof

$P$: Potential profit by malicious behaviors

$V(S,F)$: Fraud proof validation function

$f$: slashing ratio ($0 < f \leq 1)$, usually 1 (= 100%)

$r$: reward ratio for challengers ($0 < r \leq 1)$, the rest of reward can be burned or awarded to DAO

$C$: Cost of the challenger for the dispute process

## Goals

- (**Fraud Deterrence**) The attacker’s profit shouldn’t be bigger than damage
 $f \times D > P$
- (**Challenger Incentive**) The challenger’s reward should be bigger than the challenge cost
$r \times (f \times D) > C$

## Process

1. Deposit and Proposal:
  1. The proposal with a desposit $D$ submits a state update $S$
$\text{Submit}(S,D)$
1. Challenge Period:
  1. After $S$ is submitted, any participant may initiate a challenge by submitting a fraud proof $F$ within a challenge period $T$
  1. To initiate the challenge, the challenger must also stake a deposit $D_c$
1. Fraud Proof Verification:
  1. A verification function $V(S,F)$ is executed:
    1. If $V(S,F)=\text{true}$, the state transition $S$ is determined to be fraudulent 
      1. A fraction $f$ of the proposer’s deposit $D$ is slashed
      1. A fraction $r$ of the slashed deposit is rewarded to the challenger
    1. If $V(S,F)=\text{false}$, the fraud proof is invalid, and the challenge fails
      1. The challenger loses the deposit $D_c$ and it’s awarded to the proposer

## Parameter Modeling

### Easy parameters

- Slashing factor ($f$): There are conventions
- Challenge period ($T$): There are conventions
- Challenger reward factor ($r$): There are conventions
- Challenge cost ($C$): This cost can be computed by the dispute mechanism

### Tricky parameters

- Potential profit of attackers ($P$): There are different types of attacks (e.g., delay attack, exhaustion attack) and also contexts matter
- Deposit amount ($D$): There are many scenarios for it

### Check points before applying the Tokamak cryptoeconomics whitepaper

- Does a challenger should succeed the sequencer’s position?
  - Some challengers may not want to be a sequencer
  - This can be a huddle for some challengers
- Group challenge scheme is ambiguous

## References

- Tokamak Docs
[https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics)
- Research Posts
[https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup](https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup)

[https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a](https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a)

[https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html](https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html)
- Research Papers
[https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf](https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf)

[https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3](https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3)

[https://arxiv.org/pdf/2308.02880](https://arxiv.org/pdf/2308.02880)