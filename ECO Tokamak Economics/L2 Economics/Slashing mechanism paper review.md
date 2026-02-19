The paper’s argument could be improved with more defined game description & stronger argument for the multi-winner case.

- [x] Refine game model description
- Normal form - all players play at the same time
- Complete information - each validator know their expected utility function before participating
- Allow for collusion
- [x] Clarify notation - Use E(Ui) consistently across the paper
- In O1, we are using E(Ui) to denote payoff but in the proof we use EVi. 

In defense of the equal splitting rule

- rationale 1: since we assume identical deposit amount and cost function, it is sensible to also assume that rewards to be divided equally among winners
- rationale 2: in practice, this equal split rule aims to prevent the "rich get richer" dynamic. Equal reward distribution incentivizes validators to run multiple smaller nodes rather than concentrating stake in one large validator, leading to a more distributed network. 
- concern: equal rewards may not adequately differentiate between high-performing and low-performing validators, potentially leading to a "race to the bottom" in infrastructure investment. An effective watchtower mechanism is needed to maintain the integrity of the network in such case. 

Address [FC25 reviews](/2b6d96a400a380b5a3d8df8a08b14fef): 

- Notes: not all written in Column 3 would go to the paper, to keep the flow of argument beautiful. Only some parts of what is written has been added; the rest serves as a reference for response, in case we received the questions again. 
- [x] Fully addresed Concern#1 in the paper: added “Model Scope and Limitations" subsection & added future direction
- [x] Added a footnote for U-P case in the paper to address Concern#2. 

| Reviewer’s concern | Analysis | Approach to address |
| --- | --- | --- |
| **Concern#1**

The model only considers a single challenge game rather than the full multi-stage protocol that determines the correct state. This means the model does not correctly capture existing protocols like Bold and Dave.

(149A) | While we should acknowledge this limitation, we also must defend the value of the single-stage analysis. This is a classic trade-off in theoretical modeling: simplicity and tractability versus completeness. The key is to position the single-stage model as a building block for understanding more complex systems rather than claiming it fully represents any specific protocol | 1. Add a "Model Scope and Limitations" subsection in the model section. Our model focuses on a single-stage challenge game. This is a simplification of real-world protocols like Bold and Dave, which involve multiple rounds of proposals and challenges.

This single-stage abstraction allows us to isolate and formally analyze the fundamental incentive problem: how to ensure that honest parties are motivated to challenge fraudulent proposals while deterring malicious proposers. The insights from this analysis provide a foundation for understanding the incentive structure of more complex multi-stage protocols. 

While our model does not capture the full complexity of multi-stage protocols, the core incentive problems we identify—priority capture, auction dynamics, and reward sharing—are present in each stage of these protocols. Our analysis therefore provides insights into the incentive challenges that must be addressed at each level

2. Add to future work: An important direction for future research is to extend our model to capture the full multi-stage nature of protocols like Bold and Dave, analyzing how incentives compound across multiple rounds of challenges |
| **Concern#2**

Why consider only one proposer? The challenge period is much longer than one block, so the probability that all proposers are colluding is negligible.

(149A) | We might clarify that the U-P model represents a worst-case scenario, and even in the better scenario, the problem still persist ⇒ assume the worst case is sensible from a risk management point of view | The U-P model represents a worst-case scenario where a malicious proposer has full control over transaction ordering within a single block. While the challenge period typically spans multiple blocks, this model captures the maximum advantage a malicious proposer could have in any single block. 

In a multi-proposer setting where only a fraction of proposers are malicious, the advantage of the adversary is reduced and honest challengers have multiple opportunities to submit their challenges in blocks controlled by honest proposers. However, even in this setting, the fundamental problem of priority capture remains: within any block controlled by a malicious proposer, the adversary can still front-run honest challengers |
| **Concern#3**

what happens if a majority is allowed to collude

(149D) | We might explain security assumption and explain the implications of violating it. If it is asummed to be a distributed system, majority cannot be allowed to collude | If a majority of participants collude with the malicious proposer, then no incentive mechanism can guarantee protocol correctness, as the adversary can simply outvote or outnumber honest parties. In this case, the security of the system is fundamentally compromised, and the problem shifts from incentive design to cryptographic or consensus-layer solutions |
|  |  |  |