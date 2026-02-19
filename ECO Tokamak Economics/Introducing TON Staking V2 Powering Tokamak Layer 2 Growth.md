# Subject: Introducing TON Staking V2

> Sub-title: **Powering Tokamak Layer 2 Growth**
> Keywords: Tokamak Network, Staking, Tokamak Rollup Hub 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/168c3770-b6ac-4013-a2ab-0eeaf0836806/TN-Introducing_TON_Staking_V2_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWASACOE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T035907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ps9SrHlflB%2BvO48s9y7lxt0Ydwd24U6s06TFNMFemwIgHRlpNW1PR9p9IRMliQuRWgFUenfbdh8tHnvMIEWT4tsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDP1g4x7rSLoxzbj%2BcSrcAxWFSnyIW8Y%2FQoXBHzmhuo25JbURDCcCZXCxEePn7I2nDUw3i7w%2Fr3xE7AxC0JGI9iXwQbCA62IMjcM%2BzOQcPGJjSvrNGJUtRPHUsbs%2FAmm6Tu68sM5Xb9MAFFPnlg2rMJXffenilI0CZI2sXcgJ1ze5IlmTSrakYgQCo6VJGtOjc0%2BY5ZWSLSzmMoGd7OZwKj7OdAIcSZiXLo6AOr0Rj0SQZXUUAidgE86xyVMIK7FG9gUxtTKQuAFx9%2BNRLDVOfNWw27cQQcU%2BHoMCJbYgPr8ROjXNMqgfcivcZeBi7B1076K5PGlYpL7wt4LV8Y%2B3%2FK3N0spji2bulBsgCckIYUGtB%2FlwI6uKHBNzc46c3rsmFe%2BhGPWmiQJNJgIHeHl3CyOQj2%2BirvRdtKV0f9mkBZ6roS6EWIzJl2CA46kTIE8%2FYWvKDyVO1zmX2wof8s%2BjMDqetrIa35iTcNOD4rDI1kEAgjzlegMWDqMKY0%2BH3Rgmx8NIILB%2BzvvaOMY1FQhywMdUrCxMtJe4TYquZTD%2F%2BmtGhWGSMpVwSKD%2F5BESIuiKWm7algK58MGhnpS0AGoK4e2TvxyJkkLUZgJFLhvK8jDFsvdHSeBwREQwvGJq39lrPYSehzR6R9HarwUbMIPw2cwGOqUBRhMcr8%2B6H9zOmuVC3Pwo8BY8rhP0c6gj0WfD8ztFIjPbmiawfGgoiHLEK51OxFUSjw2puo9G8nHMeBQh3D0odNiOlYn52w9boCVOA8PervDkuO93qDSFdIY7kIXiSenTD68be9EVfyKyrq2RHB%2F%2F9bynEttrP7taGvpGQPQVCHOR7UleTCP3bgama7wpwt%2Fvej%2Be9gzu2qOX79QKSULfuT3y02Df&X-Amz-Signature=c4a09311ca29588c8d07d37ccbd04f070ce3a2ba6ba82a171111c121f49acc15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Introduction

We are thrilled to announce the development of TON Staking V2, a significant upgrade to the existing TON staking mechanism. This evolution is strategically designed to foster the growth and sustainability of the Tokamak ecosystem by directly incentivizing the operation of Tokamak Layer2 solutions. The detailed logic has been designed in [Tokamak Network WhitePaper 2.2.2](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2).

TON Staking V2 will introduce a crucial new feature: the distribution of seigniorage to sequencers of Tokamak’s Layer 2 networks. Seigniorage, made from issuing TON, will be allocated to these sequencers as a reward for their vital role in maintaining and expanding the Layer 2 infrastructure.

## This strategic move aims to

### **Fuel Layer 2 Operation**

By directly rewarding Layer 2 sequencers with seigniorage, TON Staking V2 will provide the necessary economic incentives for the robust and efficient operation of these scaling solutions.

### **Support Ecosystem Growth**

A thriving Layer 2 ecosystem is essential for the overall scalability and usability of the Tokamak Network. By empowering Layer 2 sequencers, TON Staking V2 will contribute directly to the expansion and adoption of the entire Tokamak ecosystem.

### **Enhance Decentralization**

A well-incentivized and diverse set of Layer 2 sequencers will contribute to a more decentralized and resilient Tokamak network.

We believe that TON Staking V2 represents a pivotal step forward in realizing the full potential of the Tokamak Network. As TON staking participants’ incentives are adjusted based on their TON Total Value Locked on Layer 2, this upgrade will pave the way for a more scalable, efficient, and vibrant Tokamak ecosystem.

## TON Staking V2: Deep Dive into Technicals, Timeline, and Participation

We provide a more detailed look into the technical specifications, implementation timeline, and participation guidelines for the upcoming **TON Staking V2**. This upgrade is a crucial step in empowering the Tokamak ecosystem’s Layer 2 solutions by rewarding their sequencers with seigniorage.

## **I. Technical Specifications**

### **Core Mechanism: Seigniorage Distribution**

The fundamental change in TON Staking V2 is the introduction of seigniorage distribution to Layer 2 sequencers. A portion of the newly issued TON (seigniorage) will be algorithmically allocated to Layer 2 networks based on predefined metrics, TON TVL.

**TON Total Value Locked (**TVL**):** The amount deposited in Layer 2, which is the total amount of TON locked in L1 bridge or portal contract. ( For more details, please refer [here](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/en/ton-staking-v2.md#changes-in-seigniorage-distribution).)

> Reward allocated to Layer 2 = Issued Seigniorage * TON Total Valued Locked on Layer2 / TON Total Supply 

### **Staking Contract Upgrade**

The existing TON staking contract will undergo an upgrade to incorporate the logic for distributing seigniorage to Layer 2 sequencers. This upgrade will aim for a seamless transition for existing TON staking participants.

### **Layer 2 Registration and Eligibility**

Layer 2 networks within the Tokamak ecosystem will need to register through a defined process to become eligible for seigniorage rewards. This process will involve:

- Submitting key information about the Layer 2 network (e.g., name, L2 TON address, L2 type, RollupConfig address including L1 contract addresses).
- Meeting minimum collateral as TON.
- Potentially undergoing a governance(DAO) approval process.

With the Tokamak Rollup Hub Deployment SDKv1, effortlessly deploy and register Thanos-based Layer 2 chain in the Tokamak ecosystem. [link](https://medium.com/tokamak-network/tokamak-rollup-hub-d8d11613ecd3)

### **Reward Distribution Frequency**

The frequency at which seigniorage is distributed to Layer 2 sequencers is determined by the execution of the “Update Seigniorage" function. The “Update Seigniorage" function is the function that distributes seigniorage. This function can be executed by anyone at any time, and was mainly executed by staking participants to distribute their seigniorage. Now, when the “Update Seigniorage" is executed, seigniorage will be distributed not only to staking participants, but also to Layer 2 sequencers. 

### **Impact on Existing TON **staking participants

Existing TON staking participants received seigniorage equal to the staked TON ratio from the issued seigniorage, plus 50% of the remaining seigniorage. However, in the upgraded distribution mechanism, they will receive seigniorage equal to the staked TON ratio from the issued seigniorage, plus 50% of the remaining seigniorage **after being distributed to Layer 2 sequencers**. Therefore, the seigniorage received by TON staking participants will be adjusted according to the Layer 2 TON TVL. The overall goal is to create a balanced incentive structure that benefits both L1 staking participants and Layer 2 growth. The detailed reward model is [here](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#22-seigniorage-distribution).

### **Instant withdrawal of staked TON(L1) to Layer2**

We are committed to making the user experience within the Tokamak ecosystem as smooth and efficient as possible. We understand that longer withdrawal times can create significant friction. Assets staked on Layer 1 are typically subject to 93046 blocks(about 13 days) withdrawal delay for security reasons. However, we have decided to remove this withdrawal delay for withdrawals to re-deposit to Layer 2. This will make the user experience within the Tokamak ecosystem as smooth and efficient as possible.

One thing to note is that when depositing to Layer 2, Staking V2 Service does not guarantee the stability of the Layer 2, and the user is responsible for depositing to Layer 2. Therefore, when withdrawing to Layer 2, the user must directly check whether there is a problem with the deposit function of the Layer 2 bridge or whether the Layer 2 network is in a safe state.

### **DAO Control Over Seigniorage Distribution of specific Layer 2**

The DAO can pause/unpause seigniorage distribution strategically to Layer 2 networks that do not align with the goals of the Tokamak ecosystem. A transparent DAO-led control for seigniorage distribution can foster greater trust and fairness within the Tokamak community.

## **II. Implementation Timeline (Tentative)**

Please note that these are estimated timelines and are subject to change based on progress and security audits.

### **Phase 1: Research & Specification (Completed)**

Initial research and high-level specifications for TON Staking V2 have been completed.

### **Phase 2: Technical Design & Development (Completed)**

The detailed technical design of the upgraded staking contract and the implementation of seigniorage distribution logic have been completed.

### **Phase 3: Security Audit (Completed)**

Comprehensive security audits by reputable third-party firms and community members  have been conducted to ensure the robustness and security of the upgraded contracts. We will be releasing a subsequent announcement with the detailed results of each audit.

### **Phase 4: Test-net Deployment & Testing (Completed)**

TON Staking V2 had been deployed on a public test-net, allowed the community and Layer 2 sequencers to test its functionality and provide feedback. For the public test, please refer [here](https://medium.com/tokamak-network/simple-staking-v2-public-test-7eec1e137ed8).

### **Phase 5: Main-net Upgrade (Q2 2025 — Subject to DAO Agenda Passing)**

Following successful test-net testing and community feedback, the TON Staking V2 upgrade will be deployed on the Tokamak Network main-net. For a DAO agenda details, please refer [the discussion ](https://github.com/tokamak-network/ton-staking-v2/issues/308)and [the DAO Agenda #14](https://dao.tokamak.network/#/agenda/14).

## **III. Participation Guidelines**

### **For Existing TON **staking participants

The upgrade process is designed to be as seamless as possible for existing TON staking participants. **You will not need to take any action** during the contract upgrade and after. We encourage you to stay informed about the updated reward structure for staking following [Staking V2 implementation.](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/en/ton-staking-v2.md#changes-in-seigniorage-distribution)

### **For Layer 2 Sequencers**

We recommend using Tokamak Rollup Hub's Deployment SDKv1 to seamlessly deploy and register your Layer 2 chain with Tokamak Ecosystem. More details will be made available soon by Tokamak Rollup hub team. Please refer [here](https://medium.com/tokamak-network/tokamak-rollup-hub-d8d11613ecd3).

### **For the Tokamak Community**

We encourage all community members to actively participate in discussions, provide feedback at any time, and stay informed about the progress of TON Staking V2. Your input is invaluable in ensuring a successful and beneficial upgrade for the entire Tokamak ecosystem.

---

We believe that TON Staking V2 will be a game-changer for the Tokamak ecosystem, fostering a symbiotic relationship between the ethereum (Layer1) and Layer 2 solutions. By directly incentivizing Layer 2 sequencers, we are laying the foundation for a more scalable, efficient, and vibrant future for Tokamak.

**Stay connected for further announcements!**

** **