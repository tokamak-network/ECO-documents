![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/578d29f4-1a52-4197-aac8-43363ce5dbb3/attention_challenge.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFQK4K7W%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3Y%2BSXbBjMU3iYXfoMEuruJOfts4QrGC%2BkNDtZwWtslgIgOj8rLSWIvoxu9%2FHwjGWbS4BUrg90z0J8CNW6QoQHoR4q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDBYLP2KhT6nZO53lVCrcA99bm1QP%2Bbtad4uUICvzxNTqeKvKui4oU2UDvnKr76ZA2MdwT%2BtPnQ1gcVCgtdk%2Fa8L8hlb6nvW1c%2FUxvhRMdbIzF5cfS7uYIGDtOQ3ULOMxkmfn9iSBnJqhQTVd%2FoHfYdDlrexUM9UamrERH5MZCWlcatV9%2BkICPuQTiAGgIUTX0WX9px4Ceqy7sCQ5b1zk%2FlC46BkwWA%2BDS0mHgIWNvSrqIf0cKmEunTqRaZ%2BIxlWCSu1doK10LgGz3ts7RUZQJ2DziC%2FWPGgg6EtWn1KCpPH7kPzBb756TWA6U6usqRtgMHNvpls1i4Po932KHIP39FByd79cfPoUgj2p0I%2BKsdqihYR7reBxNR6adMB95bRuPeb2Egt7mGd4DxxMdN13D%2FayjKe9aSYHixIAN91ggl68MoZ%2FCrR5tXCX3mdabukIxj6tzcDuQyhLmKXpWu0xIqRE7J%2BLeqG7%2FPXWQuD1RavoVrey3ta8N7v7yg9P%2FO%2FNibTD5mA0nhQKDAJhz2EXOXd%2BwknNpZmJCNYMRJZtn8CvAT3um0vckLqHtIHMzhNEiETAd2T%2Fjnfbtbfc3AzFhvnbEsFWHwJ1KX2j0VO6P0UlT5lBF4XKgfOH0UYGkfc40GjWATAtSkBI%2B1MOMIzv2cwGOqUBV%2BIQkePatX1%2BPGYgeIsWprsQLrJDvnTyzc1T3c0NkyjicINgvJudsvYIlrDRolEk4RZdTQz3peiZJBys3MCmBhryGqF9pRwslmNgRJlXQ49hMblmiPCbivF56kcIa07pANKEebYc1zjbTCFOZZuWuEZpS2aYaxZJREkBBA17Rwj0%2FGuyHIRxG1k%2FF0ziH30Y02sbKP7fblaLmka9sxe2hTPc7lsl&X-Amz-Signature=7137ffc3b6a5e8d0b1ff1bdf1e865d67a0b4ac3ce6453133ddccef29efcab040&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## **1. Problem to Solve**

Optimistic Rollups (ORUs) are a key technology for blockchain scaling, offering increased throughput while inheriting the security of the Layer 1 (L1) chain. They achieve this by executing transactions off-chain and posting only essential data and state commitments to L1, optimistically assuming the Sequencer's proposed state transitions are valid by default. Security relies on the possibility for validators to submit Fraud Proofs during a challenge period if they detect an invalid state transition.

However, this security model fundamentally rests on the critical assumption that at least one honest and diligent validator is continuously monitoring L1, processing L2 data, and submitting Fraud Proofs when necessary. This assumption can be fragile due to the well-known "Verifier's Dilemma." Validators may lack direct economic incentives to perform the costly verification work, leading to potential free-riding if they believe other validators will undertake the effort. An inactive ("lazy") validator that remains online but does not perform actual verification poses a significant security risk, as a malicious Sequencer could potentially finalize fraudulent states unchallenged. Simple liveness checks are insufficient as they do not ascertain a validator's capability or willingness to perform the core computational tasks required for verification.

## **2. Core Idea**

To address this challenge, we propose **CRAC (Commit-Reveal Attention Challenges)**, a novel protocol designed to proactively verify validator liveness and computational readiness within the ORU framework.

- **Probabilistic Individual Challenges:** The system randomly selects individual validators for specific state updates and requests them to perform a verification task.
- **Verification of Computational Capability:** The challenge requires the validator to prove it has independently computed the relevant state transition, going beyond simple online checks.
- **Direct Economic Incentives:** If the challenged validator fails to respond correctly and within the specified time limit, it faces direct penalties (e.g., stake slashing). This provides individual economic motivation to maintain operational readiness.
- **Utilization of Commit-Reveal Scheme:** To prevent validators from simply waiting for the Sequencer's result before submitting their own, CRAC employs a cryptographic commit-reveal scheme. Both the Sequencer and the challenged validator first submit cryptographic commitments to their respective results on L1, and only later reveal the actual values for verification.

## **3. Protocol Description**

The CRAC protocol integrates into the Sequencer's state commitment process and is triggered probabilistically.

1. **Challenge Trigger and Target Selection:** Before submitting a new state root, the Sequencer computes a hash derived from the relevant data. If this hash falls below a predefined threshold, a CRAC challenge is triggered. The hash value also deterministically selects a specific validator (Vi) to receive the challenge.
1. **Commit Phase:**
  - If challenged, the Sequencer submits a commitment to its calculated state root hash to the L1 smart contract, identifying the target validator Vi.
  - The challenged validator Vi detects the challenge on L1, independently computes its own version of the state root, and must submit its own commitment to its result hash to the L1 smart contract within a strict time limit (T_commit).
1. **Reveal Phase:**
  - After the commit phase (or timeout), the Sequencer reveals its original state root value and the nonce used for commitment to the L1 contract, which verifies consistency with the initial commitment.
  - Subsequently, validator Vi reveals its computed state root value and nonce to the L1 contract within another time limit (T_reveal). The contract verifies consistency with Vi's commitment and checks timeliness.
1. **Outcome Determination:** The L1 smart contract assesses the timeliness of commits and reveals, verifies the consistency of reveals against commitments, and crucially compares the revealed state root hashes from the Sequencer and Vi.
  - **Success:** If all steps are timely, commitments are valid, and the hashes match, the challenge is passed.
  - **Dispute:** If timely and valid, but hashes mismatch, the standard ORU dispute resolution (Fraud Proof game) is initiated.
  - **Failure:** If Vi violates time constraints or fails commit/reveal verification, Vi incurs a direct penalty.

## **4. Expected Impact**

The introduction of the CRAC protocol is expected to yield several benefits:

- **Mitigation of Free-Riding:** By imposing direct, individual penalties for failing challenges, CRAC reduces the incentive for validators to rely solely on the efforts of others and motivates individual readiness.
- **Increased Average Validator Attentiveness:** The incentives provided by CRAC are expected to raise the overall average operational readiness (Attentiveness) level across the entire validator set compared to the baseline scenario.
- **Enhanced Sequencer Deterrence:** A dishonest Sequencer faces an additional risk beyond traditional Fraud Proofs: the probabilistic chance of being immediately challenged and potentially exposed by an attentive validator via CRAC. This strengthens the incentives for the Sequencer to act honestly.
- **Basis for Quantitative Security Assessment:** The game theoretic and cost analyses provide a framework to quantitatively estimate the level of validator attentiveness induced by specific CRAC parameter settings and assess the resulting security improvements.
- **Tunable Security-Cost Balance:** The protocol allows system operators to adjust the challenge frequency (p), enabling them to strike a rational balance between the desired level of security assurance and the acceptable L1 operational costs and latency overhead.

In summary, CRAC aims to enhance the security and reliability of Optimistic Rollups by complementing the existing reactive Fraud Proof mechanism with proactive, incentive-compatible monitoring of validator readiness, addressing weaknesses stemming from the verifier's dilemma.