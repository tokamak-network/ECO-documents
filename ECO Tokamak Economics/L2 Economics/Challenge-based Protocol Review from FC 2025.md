- Title: (Im)possibility of Incentive Design for Challenge-based

Blockchain Protocols

Review #149A

===========================================================================

Paper summary

- ------------

The submitted paper proposes an economic model for fraud proof protocols in e.g., optimistic L2s. This formalizes two questions: (1) are honest participants incentivized to challenge? (2) are dishonest proposers suitably damaged? The paper's key result is to show that when the protocol chooses only one winner in the fraud proof protocol, it is impossible to reasonably incentivize both (1) and (2). On the other hand, for multiple winner protocols, the paper shows a concrete feasibility result.

Comments for authors

- -------------------

Thank you for your submission. Overall, I do very much like the general theme of the work; it is an important goal to develop a formal theory for the space of fraud proof protocol designs.

The paper builds a model to show its main result that multiple-winner fraud proof protocols fare better. However, I do not think that this model correctly captures the design space. For example, it does not seem to capture existing fraud proof systems such as Bold / Dave.

My major concerns with the paper's model are given below:

- My largest issue is that the paper's model only considers a single challenge game (e.g., State S is proposed and the challenge game only figures out whether S is incorrect *but not* what the correct state is). In real fraud proof systems, the incentives are really over the *full* game which consists of many proposals/challenges that result in finalizing the correct proposal. This means that the paper's model will not correctly capture existing fraud proof protocols such as Bold / Dave (also see below for details).
- The paper's framework mentions two goals: (1) Incentivizing honest participants to challenge; (2) Sufficiently penalizing malicious proposers. The results then come from combining the constraints for both goals. But why are both goals necessary in the first place? For example, even if malicious proposers are not significantly demotivated, as long as an honest party is incentivized to challenge, the fraud proof protocol will function correctly. In this case (e.g., \nu >\approx 0 in the paper's model), the impossibility result will not hold.
- Why does the amount slashed / rewarded to the challenger a fixed fraction of the deposit? A different strategy (used in Bold for example) is to reimburse the winning challenger(s) only their cost $c$ to carry out the challenge (perhaps with an additional amount \epsilon); the other $D - c$ portion of the proposer's deposit is slashed. Further, even in permissionless protocols like Bold, the reimbursement is really bounded by the costs of a single party to perform the challenge. The entire challenge can be thought to be performed a single "logical" party staked on the same state. Then, each individual step within the challenge is reimbursed to the challenger that performed that step.
- Typically, each challenger needs to place a stake on its claimed state as part of the challenge. This means that at the eventual end of the protocol, unless the challengers colluding with the original proposer stake on the honest state, they will also lose their stake. Combined with the previous point, all the colluding challengers together will never profit more than a small \epsilon.

Some other comments

- Why does the model split the reward equally among participants? I don't think it's appropriate to base the impossibility result with this assumption. If e.g., only one challenger at random receives the reward, then does the impossibility result change?
- In the proposer model (U-P), why is only one proposer considered? All the challenger needs to do is get its challenge within a period of time (which is orders of magnitude longer than 1 block). The probability that all block proposers within the challenge period will be colluding is negligible.
- In both Bold and Dave, there is no bound on the total cost to challenge an adversarial proposal. It grows with the budget of the adversary. Further, these protocols assume that all but one challengers can be malicious rather than an honest majority (as modeled in this paper)

Suggested improvements for Revision

- ----------------------------------

There would be significant changes (see above) which could also change the main results of the paper. I also think this submission would benefit from being developed into a full-length paper.

Overall merit

- ------------

2. Weak reject

Reviewer expertise

- -----------------

3. Knowledgeable

- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Review #149B

===========================================================================

Paper summary

- ------------

This paper studies the incentive-compatibility of dispute/challenge-based blockchain protocols (e.g., Truebit-style verification, optimistic rollup fraud proofs, DA audits). The authors formalize a mechanism-agnostic model with (i) multiple challengers of heterogeneous (bounded) costs, (ii) a proposer deposit Dp and reward share α, (iii) a colluding minority of size A < N/2, and (iv) three ordering regimes that reflect real-world priority capture: unfair-by-proposer (U-P), unfair-by-builder/market (U-B), and fair (F). They pose two design goals: O1 (ex-ante non-loss for honest challengers in fraudulent states) and O2 (η-fraction deterrence against dishonest proposers).

The main results separate single-winner from multi-winner (non-exclusion) designs. For single-winner, they show: under U-P, honest participation cannot be incentivized (O1 fails) because a coalition can recycle priority fees; under U-B, auction competition drives the winner’s surplus to 0 so O1 cannot be guaranteed; under F, meeting O1 requires rewards that scale with N, creating a scalability limit.

By contrast, in multi-winner with non-exclusion (all valid challenges are included), priority rents vanish (f ≃ 0) and O1/O2 reduce to explicit bounds on \alpha, yielding a feasible interval with non-emptiness conditions and a scale-free calibration: it suffices to set \(D_p \ge \tilde c\cdot A/(1-\eta)\), independent of the total number of challengers N. This shows that non-exclusion can simultaneously achieve honest non-loss and deterrence, and scale in honest participants.

Comments for authors

- -------------------

This is a timely and well-scoped paper that clarifies when challenge-based protocols are economically viable. The model captures key realities (priority markets/PBS-like ordering, collusion, heterogeneous costs) and cleanly distills the design problem into O1/O2. The split between single-winner impossibility/scale limits and multi-winner feasibility is crisp, with clear parameter recipes for α and Dp. The derivations of the O1 lower bound and O2 upper bound are simple yet powerful lenses for practitioners.

Strengths:

- Clear formalization of the incentive question for dispute-based verification; results align with practice (priority capture undermines first-valid).
- Impossibility/limits for single-winner under realistic ordering; feasibility with non-exclusion and explicit feasible interval.
- Useful “calibration recipes” (α, Dp) including the scale-free deposit bound \(D_p \ge \tilde c A/(1-\eta)\).

Concerns (mostly presentation/coverage rather than correctness):

- Some practically relevant variants are relegated to intuition: finite m>1 (non-exclusion not fully attainable in busy systems), non-equal splits, and small but positive priority fees f>0. Making these sensitivities explicit would aid deployment.
- In the U-B analysis, the private-value definition mixes stages; a clarifying sentence relating \(c_{init}\) vs. \(c_{proc}\) and the surplus argument would improve readability.
- A short “systems mapping” paragraph (e.g., to optimistic rollup dispute games/watchtower markets) would help non-theory readers apply the results.

Suggested improvements for Revision

- ----------------------------------
- Add a short lemma or remark that adapts O1’s bound to finite m and discuss how attainable m affects feasibility in busy windows. This is largely algebraic and feasible in shepherding.
- Briefly compare equal-split with lottery or cost-proportional splits and how they change the O1 lower bound; a 1–2 paragraph sensitivity note suffices.
- Include a footnote or appendix line quantifying how small \(f>0\) shifts the feasible interval in Theorem 4 and the scale-free condition (the formulas are already set up for it).
- Add a short discussion connecting O2 to a bounded censorship budget under U-P/U-B (how η relates to required burn or deposit to defeat self-challenge and recapture). This improves practical guidance without changing results.
- One paragraph mapping parameters to optimistic rollups/watchtowers with suggested defaults and KPIs (e.g., adoption of non-exclusion and partial burn).

Overall merit

- ------------

4. Accept

Reviewer expertise

- -----------------

3. Knowledgeable

- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Review #149C

===========================================================================

Paper summary

- ------------

The paper studies challenge mechanism for optimistic rollups.

In particular, it studies when the following two desired properties can be achieved:

(1) honest challengers are incentivized to challenge by a positive financial reward,

(2) dishonest proposers are disincentivized to propose wrongly by a financial penalty.

The paper examines several different types of challenge mechanisms: single/multi-winner challenges and different challenge winner determinations.

Very roughly speaking, the paper's results can be described as follows:

For single-winner challenge systems:

Theorem 1: If the winner is determined in an auction whose proceeds go to the (adversarial) proposer, the adversary can always outbid an honest challenger (since the former keeps the bid).

Hence, any honest challenger has a negative expected return, and is not incentivized to challenge.

Theorem 2: If the winner is determined in an auction whose proceeds go to an (external) "builder", and initial proving costs are considered "sunk costs", competition among challengers leads to a negative expected return for challengers.

Theorem 3: If the winner is determined randomly, the expected return per honest challenger will turn negative when the number of challengers grows too large (since the reward is randomly split between all).

Furthermore, the paper discusses that in a multi-winner challenge process both properties can be achieved, and provides a necessary condition on the model parameters.

Comments for authors

- -------------------

The introduction, problem and model description (the first 4 pages) are clearly written and easy to follow.

The remaining 4 pages containing the results and proofs, on the other hand, leave room for improvement:

Several pieces of notation are missing precise definitions, there are a number of inaccuracies, and the proofs would benefit from more detailed explanations.

Major comments:

O1: How precisely is U_i defined? In particular, since an expectation is being taken, what's the source of randomness?

Lemma 1:

"The worst case is c_i = c^hat so O1 is equivalent to..."

This argument could be made more explicit. Is it that:

E[U_i] >= 0 for all i \in A

<=> min_{i \in A} E[U_i] >= 0

<=> alpha*D_p/m - max_{i \in A} c_i - f >= 0

<=> alpha*D_p/m - c^{hat} - f >= 0

The latter holds iff c^{hat} = max_{i \in A} c_i. So should c^{hat} be defined only over i \in A, and equal the max/sup?

Lemma 2:

The proof is missing a brief explanation (in words) of what's being calculated.

In particular, what assumptions are made to bound the adversary's challenge reward? Which ordering (Section 3.3) and number of challenge winners is assumed, or why is the statement true in all models?

Corollary 1: What does phi-free mean?

Theorem 2:

"The winning bid f* will approach v_i":

- which v_i?
- Previously c^{init} was stated to be a sunk cost. Wouldn't this imply the bid approaching alpha * D_p instead of alpha * D_p - cˆ{init}?

Minor comments:

P.1: First, are honest challengers are...

P.2: but bounded costs , a proposer (extra whitespace)

P.3: c^hat >= sup_i c_i: since the number of c_i is finite, why not use max_i c_i?

P.5: the phi-free in the proof of Corollary 1 uses a different symbol

P.6: "Work in a fraudulent state." The meaning of this is unclear.

P.6: private value vi -> $v_i$

P.6: the upfront cost c^{init}... Should this be c_i^{init}?

P.8: "And it is optimistically considered." Is this sentence complete? What does "it" refer to?

Suggested improvements for Revision

- ----------------------------------

Possibly, the comments above can be addressed in the given time.

Overall merit

- ------------

2. Weak reject

Reviewer expertise

- -----------------

3. Knowledgeable

- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Review #149D

===========================================================================

Paper summary

- ------------

This short paper studies incentive design in challenge-based protocols like optimistic rollups. The authors give a simple model featuring a proposer and multiple challengers/validators, a proposer deposit, and a reward scheme for successful challenging. A minority of parties is allowed to collude. The two goals are (O1) having an ex-ante expected utility $\geq 0$ for every honest challenger, and (O2) incurring a loss for adversarial coalitions. The paper presents three different ordering regimes: fair ordering, unfair-by-builder, and unfair-by-proposer. They analyze single-winner and multi-winner designs, showing an impossibility (or infeasibility) result for the different regimes in the single-winner case, while presenting bounds for the multi-winner case in which both goals hold.

Comments for authors

- -------------------

Strengths:

- Important problem
- Clear and minimal model
- Results are interesting and seem useful for designing callenge-based protocols

Weaknesses:

- The goal O1 seems a bit strict. Wouldn't it be enough that there exists one honest challenger that has a non-negative ex-ante expected utility?
- Some things were not clear to me, see questions below.
- I am not an expert in this area, but it was not easy to estimate the novelty and impact of this work, also wrt. related work.

Questions:

- Does the positive result for including all valid challengers have some other limitations, e.g., block space, gas costs, etc.?
- This may be obvious, but what happens if a majority is allowed to collude?
- Why is it enough to look at these three ordering cases?

Minor:

- I am not familiar with Truebit, it would be good to introduce it or at least reference it somehow.
- are honest challengers are incentivized -> drop second "are"
- environemtns -> environments
- non-trivial vs nontrivial -> inconsistent usage

Suggested improvements for Revision

- ----------------------------------

Address/clarify the questions above.

Overall merit

- ------------

3. Weak accept

Reviewer expertise

- -----------------

2. Some familiarity