# Review #34A

## Overall merit

1. Weak reject

## Reviewer expertise

1. Expert

## Paper summary

The paper proposes attention test design for optimistic rollup validators. It identifies relevant players and their costs for running state transition, essential for validating the rollup progress. The paper argues that their design results into equilibrium in which all validators are online and validating, while the proposer sends the right state root each time.

## Comments for authors

The paper misses a key reference to "Proof of Diligence: Cryptoeconomic Security for Rollups" (AFT, 2024), which essentially proposes the solution to the same "verifier's dilemma" identified in the paper. While there are some obvious design differences between the two proposals, the authors should do a thorough comparison and identify why their proposed mechanism is better than the "watchtower" design from the missing reference.

Fixing N -- the number of validators assumes the set of validators is (somewhat) permissioned, while a big point of validating is that this set is permissionless. Does the design allow permissionless validation nevetheless? If yes, does it modify incentive structure?

More technically, from its proof, it is not clear why Proposition 1 holds: two homogenous agents face a slightly different optimization problem, as their own strategies are different. I think the result is still correct, but the reason lies into indifference condition.

---

# Review #34B

## Overall merit

1. Weak reject

## Reviewer expertise

1. Knowledgeable

## Paper summary

This paper presents a protocol, the Randomized Attention Test, that solves the verifier’s dilemma in Optimistic Rollups.
In RAT, validators are randomly challenged to test their attentiveness: they must prove that they have computed the next state transition or they will be penalised.

The authors provide a detailed game-theoretic analysis to demonstrate that the RAT protocol can lead to an Ideal Security Equilibrium, where all validators are attentive and the proposer behaves honestly. They also suggest some practical way to compute the different parameters.

## Comments for authors

This paper provides a nice game-theoretical analysis of a solution that has been discussed in the L2 community.
Section 7 is very nice as it provides some practical parameters evaluation.
The biggest problem of the paper, in my opinion, is how little discussion there is around the pseudo-randomness of the trigger, although Observation 2 acknowledges this, a deeper analysis would strengthen the paper.
Although this is a nice protocol, the "one honest validator" assumption isn't the biggest problem of L2s, right now, especially given their current level of centralisation.

Some minor comments:

- p2: "While the concept of an “attention test” to proactively verify validator engagement has been discussed within the blockchain community for several years" -> add reference
- p7: "It is SC that then probabilistically determines if an attention test should be initiated for this specific σ_P. This determination, along with the selection of a target validator, is made deterministically by SC" -> this sounds confusing and is weirdly phrased.

---

# Review #34C

## Overall merit

1. Weak reject

## Reviewer expertise

1. Knowledgeable

## Paper summary

This paper presents a Randomized Attention Test to keep L2 validators diligent. The paper presents a practical design and a game-theoretic analysis.

Strength

- Keeping rollup validators diligent is an important problem with practical impact.

Weakness

- "Proof of Diligence: Cryptoeconomic Security for Rollups" by Sheng et al. published last year in AFT apparently addresses exactly the same problem using a similar approach. I'm surprised to see that this paper does not compare to Sheng et al. The contribution by Sheng et al. is "a carefully-designed incentive mechanism that is provably secure when watchtowers are rational actors, under a mild rational independence assumption" which appears to be highly overlaping with this work.
An explicit comparison is thus necessary for this work.

## Comments for authors

Can you explicitly detail how the proposed approach uniquely addresses the shortcomings of existing methods. Specifically, which particular innovations create the critical differences that overcome the limitations of existing systems.

---

# Review #34D

## Overall merit

1. Accept

## Reviewer expertise

1. Some familiarity

## Paper summary

With optimistic rollups (ORU), blockchain transactions are bundled and processed
off-chain first. Only their results, i.e. the changes to the shared state
managed by the blockchain, are then posted to the main chain. To combat
malicious transactions, optimistic rollups rely on validators independently
re-calculating and verifying these off-chain transactions. When they detect a
faulty transaction, they must submit a fraud proof to the chain, so that the
affected transaction can be rolled back.

As such, safety relies on validators doing their job. However as these are
off-chain operations, this cannot easily be verified. To improve on this, this
paper introduces 'randomized attention tests' (RAT), a mechanism by which
liveness of validators can be verified. RAT periodically targets single
validators with a challenge, requiring them to prove that they have correctly
verified past transactions. If they are unable to do so in a timely manner,
they are punished by having some of their stake slashed. The challenge is
computed by an on-chain RAT smart contract, which contains the main
protocol. It uses essentially the same cryptographic proof method as
the rollup validators use; the chosen external validator is asked for
a mandatory verification of the state update done by the rollup. The
RAT contract then compares the responses and distributes rewards accordingly.
The protocol itself is fairly simple.

The paper subsequently analyzes this mechanism under the assumption that
participants are acting rational in the game-theoretic sense. It shows that
system parameters can be chosen in such a way as to guarantee honest behavior
from all participants.

## Comments for authors

The paper is cleanly written and well-structured. The need to ensure validators
perform as expected when wanting to use optimistic rollups is clear. Thus,
designing a mechanism which can be applied atop any ORU deployment is a useful
contribution. The assumption that participants of the system act rationally may
be rather strong, but is understandable in a system such as a blockchain.

Some comments on the content:

- 5.3: At first reading, the state space covered by Table 1 was not quite clear
to me. From context I later understood it as:
- Network Status: Whether at least one honest validator is verifying L2
transactions.
- Validator: Whether one specific validator (who may be challenged) is online
(and attentive).
- Attention Test: Whether that validator is being challenged, and if so, what
the result of the challenge is. The choice of a hyphen ("-") for "no
attention test taking place" specifically seemed odd.
It may be worthwhile to more clearly introduce the state space before the
reader encounters the table.

Similarly, the payoff of validator and proposer being encoded as a two-tuple
could be made more clear in e.g. the table's caption.

The same considerations apply to Table 2.

- 6.1.1 Calculation of the probability that fraud is not detected by any
validator as $(1 - \pi_v)^{N - 1}$ assumes that validators and proposers
independently select slots during which they are offline respectively
dishonest. This assumption may be challenged in real-world deployments, where
e.g. the cost of operating a validator may fluctuate over the course of a
day, due to e.g. spot pricing.
- 6.2: The 'Ideal Security Equilibrium' is defined as the state where all
proposers are honest, and all validators are live. From the point of view of
the network it seems sufficient if all proposers are honest, there is no need
for all validators to be live. Can it be shown that all validators being live
is a requirement for all proposers being honest?
- 7.2.1: You assume that L2 state commitments to the L1 chain happen every
10 minutes. Is this congruent with aggregation windows commonly seen in
real-life ORU deployments?

Minor remarks and typos:

- L161-163 and L165-166 state the same thing twice.
- L219: "The validator submits a solution and verified for the proposer's
attention test in the contract." there seems to be an incorrect, or missing,
word.
- L230: "the smart contract proceeds *to/with* the dispute game"
- p7, Footnote 1:
a) "manipulable" or "susceptible to manipulation", rather than
"manipulative"
b) "randmoness"
- L449: "Presetned"