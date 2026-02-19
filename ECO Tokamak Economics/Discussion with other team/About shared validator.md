# How Small Rollups Secure Validators

## 1. It's Impossible to Validate All Chains Equally

- The initial idea behind shared validator pools was to allow small rollups that struggle to secure validators to easily borrow a validator pool from TRH.
- However, it was pointed out that it's realistically impossible for a single validator to simultaneously validate all rollups from a resource, sync, and memory perspective.
- Therefore, we reached the conclusion that "selective validation" is inevitable.

## 2. Problems with Fully Selective Structure — Weakening the Purpose of Shared Validators

- With selective validation, there's insufficient motivation to validate small rollups
→ This could ultimately regress to the original problem of "small rollups struggling to secure validators."
- Therefore, designing incentives around "which chains to validate and why" has been identified as a core challenge for shared pools.
- **Example:** Without a reward structure, no one will monitor small rollups.

## 3. The Real Value of Shared Validators — Operational Rather Than Engineering Value

- Technically, efficiently monitoring multiple chains from a single server or node is nearly impossible or has low value.
- However, operationally, there's significant value in "integrating and simplifying the reward system."
  - Validators don't need to worry about each chain's economic structure
→ The Shared Pool provides a consistent reward/slashing mechanism
  - Providing operational efficiency and management convenience is the actual strength of the Shared Pool.

## 4. Shared Pool is an "Economic Concept"

- **Kevin's summary:** The Shared Validator Pool is closer to an economic structure than a technical one.
  - The "declaration to monitor multiple chains" is simply the shared concept,
  - while actual node operation can be performed by each validator on individual servers.
- The reason for not being able to monitor all chains isn't resource limitations but economic costs (operational costs, sync costs, risk relative to rewards).

## 5. Reward Design Issues for Small Chains

- Key questions:
"Does validating a large chain with significant TON deposits yield greater rewards?"
"Or are rewards the same regardless of chain size?"
- Large chain = Large rewards / Large slashing
- Small chain = Small rewards / Small risk
→ A structure is needed where validators can choose based on their risk preference
- However, "the problem of having no reason to monitor chains with small rewards" still exists,
and designing additional incentives to address this remains a challenge.

# The Necessity of Validators in ZK State Channels

## 1. Why Did Threshold Signatures Emerge?

- In the original design, it was sufficient for channel users to each generate their own ZKPs and submit them directly on-chain.
- The problem is that the on-chain submission cost for individual users' ZKPs is very high.
- A temporary solution emerged for cost reduction:
  1. Users generate ZKPs locally
  1. They only perform signatures on those ZKPs
  1. An aggregator (router) combines them using threshold signature methods and submits once
- In other words, **threshold signatures are just a temporary engineering hack for on-chain cost reduction**, not an essential component of channels.

## 2. Does RAT Replace Threshold Signatures? → No

RAT (Randomized Attestation Test) is an attention test concept that forces challenges,
→ It has absolutely no function to replace threshold signatures.

RAT's purpose:

- Periodically test whether validators are actually monitoring the state
- A mechanism to filter out stale or lazy validators

Therefore,

- Threshold signatures = Cost reduction device
- RAT = Validator monitoring/assurance device
→ Their roles are completely different.

## 3. Alternative Role of Shared Validator Pool

- If ZKP verification can be performed instead through the Shared Validator Pool,
→ Channel users no longer need to optimize costs using threshold signatures.
- In other words, if the condition
"Cost of using shared validators < Cost of directly submitting ZKP on-chain"
- Is satisfied, threshold signatures could become completely unnecessary.

## 4. Position of Threshold Signatures — Insurance Role

- As a contingency for the possibility that Shared Validators may not be successfully implemented
→ The threshold signature method needs to be maintained as a **fallback option (insurance)**.
- In a POA (Proof of Authority) style,
it's a basic safety mechanism that can be used immediately, even if a perfect shared validator pool isn't ready.

## 5. Priority Requirement: Meta-Research Analysis

**Before proceeding with ZK state channel implementation, a comprehensive meta-research analysis has been prioritized and requested.** This analysis should:

- **Compare our ZK state channel approach with related projects** (e.g., Celer Network's state channels, Connext, Perun, Raiden Network, Lightning Network)
- **Identify the advantages and disadvantages** of different architectural choices
- **Evaluate trade-offs** between security, cost efficiency, user experience, and decentralization
- **Assess the necessity and role of validators** in various state channel implementations
- **Determine best practices** from existing solutions that can inform our design decisions

This comparative analysis is essential to validate our approach and ensure we're not duplicating existing solutions or overlooking critical design considerations that have been addressed by other projects.