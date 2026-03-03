# Tokamak Network's Economic Model for Shared L2 Security

## Introduction

The growth of the Layer 2 (L2) ecosystem has introduced the problem of fragmented economic security. As new rollups are created, each is responsible for its own security, there are disparities where larger L2s are more secure than smaller ones. Tokamak Network's "Economics Whitepaper V2" proposes a solution to this with its **Layered Verification Economics** framework. This model is designed to address the Verifier's Dilemma by creating a shared security layer for the L2 ecosystem.

## The Verifier’s Dilemma in L2 Ecosystems

Verification in a decentralized network is a public good. The security benefits of verification are shared by all network participants, but the costs are borne by the individual verifier. This can lead to a free-rider problem, where rational actors may choose not to verify transactions, assuming others will perform the work. This is known as the Verifier’s Dilemma.

In the L2 ecosystem, this problem is more pronounced. Large rollups with significant TVL can incentivize a community of verifiers, but smaller rollups may lack the resources to do so. This can result in a security deficit for smaller chains, making them more vulnerable to attack.

## Tokamak's Multi-tier Security Layer

Tokamak Network's solution is a multi-tiered security model that uses economic incentives to encourage verification. The model consists of three layers:

### **Tier 1: Public Challenge (Fraud Proofs)**

This is the base layer of security, which is standard for optimistic rollups. Any network participant can submit a fraud proof to the L1 if they identify an invalid state transition. If the proof is valid, the sequencer's bond is slashed, and the challenger is rewarded.

Tokamak's implementation includes a Multi-Challenger Approach. Unlike systems where only the first challenger is rewarded, Tokamak rewards all valid proofs submitted within the dispute period. This is intended to prevent censorship of challenges.

### **Tier 2: Dedicated Validators**

This tier introduces professional validators who are formally obligated to monitor the network. They are required to stake TON as collateral and are eligible for protocol-level incentives and bounties from successful challenges.

A key feature of this tier is the Shared Validator Set. A single validator can monitor multiple L2s, which allows smaller rollups to utilize the security of the ecosystem’s pool of validators without needing to establish their own validator sets.

### **Tier 3: Randomized Attention Test (RAT)**

The Randomized Attention Test (RAT) is designed to address the Verifier's Dilemma for dedicated validators. The protocol randomly selects validators to verify specific L2 transaction batches and requires them to submit an attestation within a set timeframe.

If a validator fails to provide a timely attestation, their stake is slashed. The penalty is calculated to make the expected cost of inattentiveness greater than the cost of continuous monitoring. As the selection is random, consistent monitoring becomes the most economically rational strategy for validators. The RAT is compatible with both optimistic and ZK-proof-based rollups.

## Updated Seigniorage Distribution

Tokamak Network has also updated its seigniorage distribution model to align with the goal of collective economic security. The new model, TON Staking V3, bases rewards on "Bridged TON," a metric that reflects economic activity, rather than raw TVL.

The Total Annual Seigniorage issuance is fixed, and a fixed proportion of this will be allocated to Treasury DAO. The rest of Annual Seigniorage will be distributed to participants based on Bridged TON. To prevent the concentration of rewards, the distribution is determined by a hyperbolic function, which is designed to promote a more equitable allocation of resources. The remaining undistributed seigniorage is then sent to Treasury DAO. This is to ensure that there are no more circulating tokens in the market than needed for actual economic activities. 

## Demonstration of the Economic Model

Suppose Total Annual Seigniorage is 10,000,000 TON. A fixed proportion of this (e.g, 10%, which equals 1,000,000 TON) will be allocated to DAO, and the remaining 9,000,000 TON would be available for L2 Reward. 

The actual L2 reward is determined based on the performance of each L2 (measured in Bridge TON), which follows a Hyperbolic Saturation Function. Suppose the function dictates that total annual rewards of all L2s is 2,181,800 TON, of which 20% (equivalent to 436,360 TON) will be allocated to Validators, and the rest (1,745,440 TON) for Operators/Sequencers. The remaining unclaimed seigniorage (which equals to 9,000,000 - 2,181,800 = 6,818,200 TON in this case) would be sent to Treasury DAO. 

[Image: Annual Seigniorage Distribution]

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dbed1852-e5b8-40da-9d33-99383d755640/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7IYTX2D%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIByLrdJPaXYJtoq7lUYMmJcucHkSnUrmh5QKu9B8EPykAiAXzFxONIapdyJwnDursl4nmbV6WjuprljJcL3KBHrKgSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMGUj4SB7qab4W5o8AKtwDD%2BbFXEBi6utDmipH1%2BWsiI6OJF60J96ZeY6SirEMu6aIoocdonaNZeLCIxBC7ckiHd%2F7ykpHZ%2FhUbkSHEmXyhUQfZ2kjljcmqY9HVbv7jpjmDRTFr95nZ%2FBfMLuhSoMF47fNVLQIP0jMmpKAs1o9bqXpIj9nhsT4QZTjGwlejDXvl%2B0%2BVC0SwMWdiDgeERIe%2FOffVuIFN1a%2BdNDsK%2FghBw1TrEwqENl5OwZiJ9Py9b%2BfSF72%2Bj1VVcV6CwF7IcolId1VkfOXuX0j%2FuIER7co3S7BtDGWf2VSmJP60l2VqBgHzfjtJwhOcJT14JPtkLudK9twJ4U5Y88NaRhUVlEeBumYe4J1UmtgBx6lfvXieQkwWyhxYKmNpZUFv5uR2X1kZklmDpeKUoNMOQI6yRecIfjVlraSoNpQL62l2xOHHRwlw9%2BMN7E2ZJ5VuDw28%2F%2Fw1jnP61iU7BHOCGnRzv5q0dpPIROl27%2FeI%2FbwpVsz9xb7%2BNKZizpNGzwcGASoOdYmC%2FQk3zfvd8wELGAD8W%2BCxXQf2fna6oU%2B7wgMeWlSWJvZPT4tSI2o%2BvkbmLKM8Q6m2kj5gOynKRDc%2BHTgsYQTR%2FKz3pWXzRTi4CDUL%2F%2F7Y31731yKO3e9Lfjx0Y4w95jbzAY6pgGVkdp1ArzXa9OX6vE4hSuWCozB9ANnXouCndBvf4rVsc56NfInos2xF%2B%2FLO3Sl3Uu7jUut1xqmXn0G1MCU8d6Uq3KYZUHsaLySchS7WM0R7uHtiMah5vM6r0Y0EXuenmJuk1UCOjUr7qAP2hKHWnfACNqbRqji2q1r4Ev%2FmFi5rsJU%2BQb%2BmJuBQldC7oo20Ag6wd4O8RFMgbts7MfjQGt%2BI0ZJMZQ7&X-Amz-Signature=627e02fc2c3770cf605f4579f101e492e70c34fa24d9a5510c4a5fbe7bf9227c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<!-- Unsupported block type: unsupported -->

## Conclusion

Tokamak Network's Layered Verification Economics presents a framework for a more secure and interconnected L2 ecosystem. By addressing the Verifier's Dilemma and the fragmentation of economic security, the model creates a system where participants are incentivized to contribute to the collective good. This is a step toward enabling innovation on a foundation of shared security.