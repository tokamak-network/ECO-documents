![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/578d29f4-1a52-4197-aac8-43363ce5dbb3/attention_challenge.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEAU3M4V%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTvRO9504B0VJ6UoznH23xlHkQXeX%2F9K1TWgfLMA%2ByrgIgNsEx4f4EBX8oNIrcs7RW%2FWZttZa9GYDAbDBGxBMZDX8q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDPGEk2FV0nAZJbKYmircA9ZZZUeVLEgMD1XNIu3ddp4mBVLK7M%2BwlXk8nr8V5nPSORthMU3CJ9AcpRjottWtKYTUdoCiernxk%2FT1BOBgWm1A81380ArCUzBEmxrqlmWIcG9PTR6rL%2B9iWygeL4p1tjPpcgM4darKBEDk7f1PQ2FsrQTRxETfsJYxTWaulJ1mYb2fW8ECDzLp6uFAUIo60etZfWReVdkVLZMKTo1U3%2Bwty7ybaAVfP8aR0uuzj7qYqldCrCUA%2FkrFQDk0skCk3%2BGRP5DIU6S7ksWpFIETkrT2Qvjp0iL4cDNE9nZuUv9O9Gccc5OjXo%2F3Sm3p4tieQlZSvcDVrw6KSgfAf50pQ9AoUUuefjjkTVSlKpiQyrbqmkF5ZmNyx7fgcLE%2FS%2B9MrSUvaCNA5NC7GSYL5AogbgwpzONcfsnEAoQXZCDEH2f3dy%2FM8cHPcwdxx31%2FlSpTY%2BvFzopBO5oig6XIr4uJj985NWzbayYqLB9JSe3q%2BC9eXiTXMi2nu3uXAy7mzjqfbQOfFbA6Q9mtbqJ1o4b1L2SaN7%2F7M23uh%2BnCw874oRC09BXjKdvf9L%2B2%2FpqN%2B4pQ5D7kqJP%2FLsHnwuAAGi32sAKIVWK9e8ohT1cU7uYQcNVYcs63o05x4Po62DurMI2a28wGOqUBWqqFjSCE37WFm6IEiNiu9M%2BXhEn0RaY2GnWjbLS8G4swTpQlsGd73YZqL1T9%2Fx8vbsSINECWOPe4rP%2Ft9FiqXqXvofdmENZgCXrOHZaybl3GaKe4Hz%2BL%2Bo559ehTyFXfg4xbmuWTBanyF4Oja%2BBtvU9IlfO8QJC2DZJsyMKphFpRS0bet%2Bq%2FqdeW2gQ%2BeJEX5atTaLPsITu6uDNloG1Kcsa3J8v7&X-Amz-Signature=4ef5f237bb7e09210000c49c848e577d710e85db364391bc4e70b11d2d6de327&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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