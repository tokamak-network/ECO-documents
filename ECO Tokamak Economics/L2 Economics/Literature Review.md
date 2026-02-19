Reasons for attention test
  - Outline rationales from past literature
    - Verifier’s dilemma: miners have to allocate resources between (i) verifying the validity of transactions in a new block and (ii) using their computational resources to mine the next block. While verifying transactions is crucial for the security and integrity of the network, it doesn't offer a direct economic reward.
Rational verifiers have the incentive to skip verification because:

(1): verification is resource-intensive => might delay honest verifiers from mining the new blocks

(2) chasing the new block might yield more benefit for miners/verifiers than trying to keep the correctness of the block, since by consensus, longer blockchain is accepted as correct

(3) malicious nodes can attack the honest verifiers by including resource-intensive transaction to blocks, thus “lock” the honest verifiers in a resource-consuming process and reduce competition for finding new blocks.

      - Consequences if verifier’s dilemma is not addressed
        1. Loss of the overall credibility of the network (common good)
        1. Waste of resources for honest participants

⇒ addressing verifier’s dilemma is also addressing the security, credibility & sustainability problem of a network. 
      - Narrow down the problems
        - Approaches to address the verifier’s dilemma
          1. Incentivize validators to validate by giving them extra rewards if they keep attention 
⇒ but at the extreme, financial rewards can incentivize rent-seeking behaviours if the network is not truly decentralized
            - Eg: Ed Felten’s attention test
            - Eg: Proof of Diligence [Proof of Diligence: Cryptoeconomic Security for Rollups](https://arxiv.org/pdf/2402.07241)
          1. Punishment for dishonest behavior, if found (eg: slashing)
          1. Limit resource-intensive transactions (e.g: gas limit, introduced by ethereum) by asking the sender to pay transaction fee. This intuitively discourages sender from generating resource-intensive transations ⇒ protocol-level solution
          1. Limit the amount of work required to verify all transactions ⇒ protocol-level solution
            - Eg: placing an upper bound on gas limit for the whole block and thus all transactions included – Loi Luu’s paper) – thus also limit the advantages gained by being dishonest. [ethereum-cc.pdf](http://people.cs.uchicago.edu/~teutsch/papers/ethereum-cc.pdf)
            - Eg: using probabilistic verification (random sampling) - guarantee the correctness of the solution to a certain (adjustable) extent [ethereum-cc.pdf](http://people.cs.uchicago.edu/~teutsch/papers/ethereum-cc.pdf) 
          1. Peer prediction (where verifiers are rewarded based on how their reports of a block's validity align with those of their peers) [It Takes Two: A Peer-Prediction Solution for Blockchain Verifier’s Dilemma](https://arxiv.org/html/2406.01794v3)
          1. False flags: intentionally plant invalid transactions to find miners who don't verify these and slash them [2004.12768](https://arxiv.org/pdf/2004.12768)
          1. Lessen the resource burden of validators (eg: staking pool, shared validators)
          1. Eliminate the verifier’s dilemma by requiring that prover submit proofs proactively and this proof is sound. (Eg: ZKP). In this case the economic disincentive for verifiers is removed
  - Attention test
    - Why someone may choose attention test and not other solutions?
      1. Simplest to integrate into existing protocols. Does not have to change the whole policy at protocol level (such as changing rules on gas limit, or adding another layer network of watchtowers)
      1. Flexible to design the challenge ⇒ the unpredictability could discourage malicious actors from trying to game the system
    - Attention test is closest to proof of diligence, as they both work with incentivizing the verifiers to be attentive. Yet the execution & rationale is different.
| Feature | Attention Test | Proof of Diligence (PoD) |
| --- | --- | --- |
| **Primary Goal** | To catch non-verifying miners/validators after the fact. | To have validators proactively prove they did the verification work. |
| **Mechanism** | **Reactive (Challenge-Response):** A challenge is issued that requires knowledge of the block’s state to solve. | **Proactive (Evidence Generation):** A proof is generated as a natural byproduct of the verification process itself. |
| **Who Initiates?** | The block proposer or a designated challenger. | The verifier themselves. |
| **What is Produced?** | A correct answer to a specific, unpredictable question. | A standardized, verifiable piece of data (the “proof”). |
| **Overhead** | Can introduce communication overhead and latency due to the back-and-forth challenge-response cycle. | Minimal overhead, as the proof is generated during a process that must happen anyway. The main cost is submitting the proof. |
| **Security Focus** | **Deterrence:** Discourages skipping verification through the threat of being caught and penalized. | **Accountability:** Creates a system where verification is an accountable, provable action. |
| **Example Use Case** | A block proposer challenges a validator to provide the resulting state root of a specific, randomly chosen transaction within the block. | A validator processes all transactions and, as a result, generates a small cryptographic proof (e.g., a Merkle root of intermediate state changes) that could only be created by executing the entire block. |
|  |  |  |
  - An Attention Test is like a spot-check. It doesn't require every verifier to prove their work all the time. Instead, it introduces a risk of being checked. The system assumes most verifiers are honest and uses challenges to probabilistically catch and punish those who are not. This can be very efficient, as it doesn't add work for everyone in every block, but it relies on the threat of punishment to function => AT only works if the punishment is harsh enough
  - Proof of Diligence is a system of universal accountability. It shifts the burden of proof to the verifier. Instead of being challenged, verifiers must proactively submit evidence of their work with every block they validate. This creates a transparent and auditable record of verification activity. The core idea is that if verification produces a cheap-to-generate side effect, that side effect can be used as proof.

Economic Aspects/ Scheme design/ Tokenomics
  1. Traditionally, cryptographic protocols are designed under the assumption
that some parties are honest and faithfully follow the protocol, while some
parties are malicious and behave in an arbitrary fashion. 
  1. The game-theoretic perspective, however, is that all parties are simply rational and behave in
their own best interests. This viewpoint is incomparable to the cryptographic one
  1. SO a viable game-theoretic protocol for crypto-economy must satisfy that while no one can be trusted by default to follow the protocol, the protocol need not prevent “irrational” behaviours (otherwise there is no place for honest participants)

Reference books/papers
[Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf)

[MULTIAGENT SYSTEMS - Algorithmic, Game-Theoretic, and Logical Foundations](https://jmvidal.cse.sc.edu/library/shoham09a.pdf)

[SoK: Tools for Game Theoretic Models of Security for Cryptocurrencies](https://alexanderlhicks.com/papers/GameTheoreticModels-CES20.pdf)

[Breaking Omert`a: On Threshold Cryptography, Smart Collusion, and Whistleblowing](https://eprint.iacr.org/2025/1582.pdf)

Tokamak Economics Whitepaper
    - Assumptions
    - Predictions
    - Outcomes

What does all of it mean for Layer 2?
  1. The feedbacks on Tokamak’s papers
  - Would be valuable to mention in both papers the general assumptions: 
    - is it a normal-form game? (participants choose their action **simultaneously?) **or sequential (extensive form) game? Execution of a protocol can naturally be regarded as an extensive form game since proposers and verifiers take turns.
    - is it a game of incomplete/ complete information?
  - Besides addressing the behaviours of a single actor, it would be valuable to analyze the action of a Coalition, since rational actors can form coalitions.
    - Insights of such could look like:
      - Coalition C prefers a to a’ only if every player in C weakly prefers a to a’ , and some
player in C strictly prefers a to a’
      - C prefers to only if the sum of the utilities of the parties in C improves
      - C prefers a to a’ if any player in C prefers a to a’
    - Interesting phenomena could happen in the case of coalition, e.g: what if we allow players to communicate to each other using “cheap talk” - communication with no on-chain cost occured? [0704.3646](https://arxiv.org/pdf/0704.3646)  