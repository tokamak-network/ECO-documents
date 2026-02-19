*##This could be included in Part 3: Model & Design Goal. In particular, between sub section 3.3 and  3.4, as all variables are defined in these sections. *

Consider a game between an Honest Challenger (HC) and the Adversarial Coalition (AC). The HC always challenge a potentially fraudulent transaction, while the AC decides whether to Commit Fraud.

Let:

- $c_i^{init}$ be the initial cost for an honest challenger to verify and submit a challenge.
- $c_i^{proc}$ be the processing cost for an honest challenger
- $c_i$ be the total cost for an honest challenger (including innitial and processing cost).
- $D_p$ be the proposer's deposit.
- $\alpha$ be the fraction of $D_p$ distributed as reward.
- $\phi$ be the fraction of colluding challengers in the adversarial coalition.
- $\eta$ be the minimum deterrence level for fraud.
- $f$ be the priority fee.
- $f^*$ be the market-clearing priority fee.

##*To directly address the concerns in Review 2, introduce pay-off where the adversarial coalition decide not to fraud, but this is of little value since we assume from the beginning that they are adversarial. As for the strategies available for Honest Challenger (HC), since we assume they are honest and the problem we are solving is not lazy validator problem, I only include Challenge as the only strategy. *

*##I think the problem with why this kind of review keep showing up is that ****we are not making it clear enough in the text that this is NOT a Game Theory Analysis but a Mechanism Design (reverse game theory) paper.**** We could explicitly explain this point in the intro text of Section 3*

We are only interested in the scenario where the HC decide to challenge (as they are honest and not lazy) and assume that once an honest challenger initiates a dispute, the fraud is always detected.

Payoff matrix for Single winner regime

|  | **AC: Commit Fraud** | **AC: Not Commit Fraud** |
| --- | --- | --- |
| **HC: Challenge (U-P)** | alpha D_p - c_i - f*; -(1-phi*alpha) D_p | -c_i - f*, 0 |
| **HC: Challenge (U-B)** | alpha D_p - c_i - f*; -(1-phi*alpha) D_p  | - c_i - f*, 0  |
| **HC: Challenge (Fair)** | alpha D_p - c_i ; -(1-phi*alpha) D_p | -c_i , 0 |

(1-phi*alpha) D_p = D_p - phi*alpha*D_p = loss of the adversarial coalition, is a function of the size of coalition (phi = A/N) and the proportion of slashed deposit (alpha) if fraud proof success.

Payoff matrix for Multiple Winner regime

Under the multi-winner setting, the economic value of transaction ordering is significantly diminished. Therefore, the ordering fee is nearly zero with all the order fairness environments (U-P, U-B, and F)

|  | **AC: Commit Fraud** | **AC: Not Commit Fraud** |
| --- | --- | --- |
| **HC: Challenge** | (1/N)(alpha D_p) - c_i ; -(1-phi*alpha) D_p | -c_i , 0 |

Check list

- [x] Modify the intro text in section 3, clearly explain that this is mechanism design (**Fine tuning rules to achieve a desired outcome) **and not a game theory analysis **(analyzes outcomes of existing, fixed rules)**
- [x] Add variable definition table
- [x] Add payoff matrices for Single-winner and Multi-winner cases