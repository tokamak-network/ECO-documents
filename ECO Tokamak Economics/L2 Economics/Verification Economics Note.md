Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-04-30

Reference: Task Analysis for Verification Economics

## Overview

The goals of this document is as follows:

- To confirm the appropriate slashing ratio of collateral for rule violators
- To draft verification economics for Tokamak L2 economics white paper (Chapter 3)

## Researh Questions and Answers:

1. If a sequencer’s deposit is slashed, where is the slashed deposit transferred?
  1. List of Potential Recipients and Distribution (discussion is needed):
    1. Challenger → 50%
      - Why not 100%? Our WTSC paper pointed out the self dispute will cover all the loss of the malicious attacker. Therefore, it should be less than 100%.
    1. 0x0000 (Token burning) → 50%
      - Buring the slashed tokens will support the price of the token. I guess many participants will welcome this policy, but the slashed one.
    1. DAO → 0 %
      - Arbitrum sends 99% of the slashed deposit to DAO
      - But, I don’t think we need this and also why DAO should take the prize?
1. If a seqeuncer’s deposit is slashed, what percentage of the total deposit is slashed?
  1. 100% for the multi-sequencer environment
    - No reason to give opportunities to a faulty sequencer if the environment has multiple sequencers
    - The slashed sequencer is blacklisted
  1. 20/30/50% for the single-sequencer environment (three strikes and you’re out)
    1. In the single-sequencer environment, we can’t blacklist the sequencer suddenly because of the sequencing liveness
    1. It indicates that at the 1st fault, 20% of the total deposit is slashed, at the 2nd fault, 30% of the total deposit is slashed, and the 3rd fault, the rest (50%) of the total desposit is slashed
    1. After the final punishment, the sequencer is blacklisted. At this point if there’s no other sequencer appears, the rollup sequencing stops.
    1. Therefore, we assume that the rollup ecosystem will find a new sequencer before the 3rd punishment

To-do:

- <u>Reward distribution when the sequencer wins (it needs Kevin’s confirmation)</u>
- Simulation of this policy
- Rewriting Chapter 3 of the economics whitepaper
- Attention test design
- Measurement of the security impact