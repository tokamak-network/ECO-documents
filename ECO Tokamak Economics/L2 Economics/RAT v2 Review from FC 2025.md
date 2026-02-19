- Title: Looking for Attention: Randomized Attention Test Design for

Validator Monitoring in Optimistic Rollups

Review #92A

===========================================================================

Paper summary

- ------------

This paper presents the Randomized Attention Test (RAT), a novel mechanism that ensures validator diligence in Optimistic Rollups. The work addresses the lazy validator problem that stems from the economic disincentive for validators to continuously verify rollup state transitions when fraud is infrequent.

The authors propose integrating a probabilistic, on-chain attention test i where validators are occasionally and unpredictably challenged to demonstrate that they have correctly processed the L2 state transitions by solving an “attention puzzle” tied to the submitted state root. Failure to respond or incorrect computation results in penalties, thereby providing continuous incentive for validator attentiveness. The paper develops a detailed game-theoretic model analyzing the strategic interactions between proposers and validators, demonstrating the conditions under which an Ideal Security Equilibrium—where proposers are honest and validators are attentive—is achieved.

Comments for authors

- -------------------

The lazy validator problem is an acknowledged yet underexplored weakness in optimistic rollups. RAT addresses this gap with a simple but effective design. I hereby discuss some weaknesses of this paper which make me concerned about its acceptance:

1) I am concerned about the game theoretic analysis, as it lacks rigor and precise definitions. What is the model (complete/incomplete, perfect/imperfect, timing of players)? Which is the equilibrium definition (e.g., subgame perfect equilibrium, or Bayesian-Nash equilibrium, or...)?

2) The paper claims that RAT can be integrated into current ORU protocols but does not carefully analyze this integration wrt timings, dispute games, etc. A more explicit integration analysis with live systems like Optimism or Arbitrum would clarify its compatibility.

Below, I suggest some improvements and highlight other necessary clarifications.

Suggested improvements for Revision

- ----------------------------------

1) In page 6, authors say "SC uses the state root and a source of on-chain data". Which on-chain data? Later, they say that the state root and the block height are sufficient - and this seems to be the case on Algorithm1 as well. This is confusing: if only the block number is necessary, then clarify that and not say "source of on-chain data".

2) The authors should compare more in depth their protocol with the Proof-of-Diligence. IIRC, PoD uses VRF and execution traces: how does RAT compares to this? Are the overheads different, which are the pros and cons of the two solutions?

3) Typos:

- page 2: "vlaidators"
- page 4: "requires to two key properties"
- page 5: "The the rest of this..."

Overall merit

- ------------

2. Weak reject

Reviewer expertise

- -----------------

3. Knowledgeable

- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Review #92B

===========================================================================

Paper summary

- ------------

This paper proposes a protocol that ensures rollup validators are online, termed randomized attention-test scheme or RAT. After the state Merkle tree root is published by the proposer of the rollup, a validator is randomly selected to reconstruct the two immediate children of that root by re-executing the transactions. Validators are incentivized to remain online, since failing to answer the test will lead to a penalty.

Comments for authors

- -------------------

This paper addresses an important and timely research topic given the widespread adoption of rollup protocols, and the authors provide useful cost data for operating a validator in the protocol, which is much appreciated.

Despite the potential feasibility of the presented solution, I have several concerns that mainly focus on the game-theoretic security analysis:

- The model of the paper is not clear. For example, the authors analyze their solution in a game-theoretic setting, but when defining the participants, they refer to honest validators. Given that the model is not properly defined, it is hard to estimate the correctness of the analysis.
- Several descriptions and definitions are missing in the “game model”. For instance, (1) the game form used in the analysis (normal-form or extensive-form, perfect information or not); (2) description of interaction and collusion, including whether external incentive and collusion deviations are permitted and how they are modeled; (3) the Nash equilibrium, since the security goal is introduced based on the equilibrium condition. My understanding is that the authors aim to model the attention test as a normal form game (NFG) with N rational validators and one rational proposer choosing strategies simultaneously. The closest description is Table 1, but it is not sufficiently formal, and some parts are hard to interpret; for instance, “network status” is not defined, which I assume represents whether other validators are online or not.
- Some parts of the analysis may be incorrect: In Table 1, in the validator’s utility for row {Online, Offline, Timeout} and column {Fraud}, the term “-c_v” appears even when the validator is offline; if a validator is offline, I assume there should be no execution cost. And in Section 6.1’s the validator analysis, why does the utility for the “offline” strategy not include when incorrectly published data is disputed, because other validators are online and dispute it? A more formal and clear definition of the game model would be beneficial for the utility analysis.
- The analysis for the possible collusion between the proposer and validators is missing in the current analysis. This renders the game-theoretic analysis incomplete, given that in the current scheme, validator-proposer collusion is easy. Specifically, the paper seems to assume that when the proposer chooses “online,” incorrect data will be rejected, but this omits scenarios in which the proposer bribes the selected validator, which chooses strategy “online” and answers the test with the help of the proposer. Appendix G briefly states that bribed validators cannot pass the check, which does not necessarily hold without more explanation of how the protocol works. Since the contract code is public, the proposer may predict the selected validator at posting time (depending on the randomness design in the smart contract) and attempt to bribe it. A bribed validator could be told the two children of the published state root and pass the attention test without executing the batch. I believe the protocol may still function under such conditions, but the outcome should depend not only on validator collateral at risk of penalty but also on proposer collateral (or budget) available to fund bribery. It would help to specify the randomness mechanism for validator selection and to clarify unpredictability and unbiasedness assumptions, and then incorporate both validator and proposer collateral into the final result.
- Finally, there is an inconsistency in section 8.2. At first, it is said that $600 cost per validator will be used for analysis, but in the next paragraph, it is actually using $200 for calculating c_m.

Suggested improvements for Revision

- ----------------------------------

The following changes would improve the paper significantly:

- Add a “Threat model” subsection within the system model that states the security setting used in the analysis (honest–Byzantine or rational) and sticks to one model throughout, or analyzes under both different models.
- Provide additional details on the game model (some material can go to an appendix) to make the analysis formal. For instance, which game is used for the analysis, what is the definition of Nash Equilibrium, and how the security goal is defined under such a model.
- Analyze possible collusion between the proposer and validators, or explain in the main text why such collusion is ruled out by assumptions or mechanisms.
- Check whether there are other inconsistencies in the utility formula and the numbers used in the evaluation section.

If collusion between the proposer and validators cannot be excluded and would affect protocol correctness, then a substantial part of the protocol and analysis may need to change, which is not possible in 4-5 weeks. If the current solution is correct, then a substantial part of the analysis must change to reflect this, which is borderline feasible in 4-5 weeks and would constitute a major revision, not a shepherding phase with minor fixes.

Overall merit

- ------------

2. Weak reject

Reviewer expertise

- -----------------

3. Knowledgeable