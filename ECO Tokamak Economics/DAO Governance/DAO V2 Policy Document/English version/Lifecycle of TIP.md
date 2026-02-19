# **1. Overview**

A TIP is an official proposal document aimed at improving the Tokamak ecosystem. It covers a wide range of topics, including technical upgrades, policy changes, and financial operations. From the initial idea to execution, each proposal passes through four key stages. First, a draft proposal gathers community feedback via an **RFC (Request for Comment)**; then, a **Temperature Check (Temp Check)** uses off-chain voting to assess the level of support. Proposals that pass these steps advance to an **On-chain Vote**, where an on-chain vote determines the final outcome. In emergency situations, the **Security Council** may shorten part of the governance process or perform post-approval actions. This structure ensures thorough discussion of proposals while minimizing unnecessary gas fee expenditures and decision-making delays.

Tokamak DAO receives various ideas and feedback regularly; however, without a formal framework to evolve these into official proposals, they are unlikely to be implemented. The TIP system formalizes these ideas into a single document that is reviewed according to **clear formats and procedures**. This enables all stakeholders to easily understand the proposal and participate in the discussion, thereby ensuring **transparency in the decision-making process**. Moreover, by implementing the TIP system, proposers can bring forward proposals that have already undergone thorough review and achieved community consensus, thereby increasing the likelihood that only **effective and impactful proposals** are adopted.

# **2. Anatomy of a TIP**


A Tokamak Improvement Proposal typically consists of the following elements, with additional sections added as needed. TIPs are drafted in RFC format within a dedicated Discord channel (e.g., `#💡｜proposal-rfc`). The following are the key components that must be included when drafting a TIP.

## 1. Essential Elements

1. **Title and Author**: 
A brief title for the proposal and the name of the proposer (or team). When necessary, include the corresponding Tokamak DAO proposal number or tag. For example, “**TIP-1: Improvement of Governance Reward Structure**.”
1. **Summary**:
Provide a two- or three-sentence summary of the core content of the proposal so that its purpose is immediately clear.
1. **Background & Motivation**: 
Describe the background that led to the proposal, identifying the problem and the need for improvement. Explain what issues currently exist and how the proposal will add value to the Tokamak ecosystem.
1. **Proposal Details / Execution Plan**: 
Detail the specific plan for implementation or execution in a step-by-step manner. If changes to smart contract code are required, specify which parts of the code will be modified and how. Where applicable, reference similar cases from other projects.
1. **Expected Impact**: 
Explain the anticipated outcomes and effects once the proposal is executed. Discuss both the positive impacts (e.g., improved protocol performance, increased governance participation) and any potential side effects or risks.

## 2. Optional Elements

1. **Implementation Plan**:
Briefly describe the technical implementation, any necessary smart contract modifications, development timeline, and required resources.
1. **Additional Materials and References**:
Include external resources, case studies, technical specifications, and any other documents that support the proposal’s validity.
1. **Voting and Next Steps**:
Specify when and under what conditions the proposer will move the proposal forward to a Temp Check vote after the RFC discussion is complete.


Additional information may be provided as needed. For example, if the proposal involves technical changes, detailed **technical specifications** or **security considerations** may be attached as an appendix. If the proposal includes budget execution, the **budget breakdown** and **fund allocation plan** must be clearly stated. By adhering to a consistent template, every TIP will have a uniform structure, enabling the community to quickly grasp the key points and engage in effective discussion.

If an initially submitted TIP is not approved, the proposer may revise it based on community feedback and resubmit. In such cases, the following must be included:

- **A link to the original TIP**
- **Explanation of why the TIP was not approved**
- **Details of the revisions made to the TIP**
- **Supplementary information** (Providing clearer intentions, comprehensive details, and implications can assist the community in better understanding the revised TIP, thereby enhancing its chances of being approved).

# 3. Explanation of the TIP Lifecycle Stages

In Tokamak DAO, the approval process for a TIP consists of **multiple stages in the governance process**, with each stage having clearly defined roles and procedures. The overall flow is: **Idea Discussion (RFC) → Temperature Check (Temp Check) → On-chain Vote → Execution**.

## 3.1. RFC (Request for Comment)

**Timeframe**: At least 7 days

**Where**: Discord (dedicated channel: `#💡｜proposal-rfc`)

### Overview

During the RFC stage, the proposer posts their idea on the dedicated Discord channel using the format “RFC: [Proposal Title]” to solicit open discussion and feedback from the community. Community members can freely ask questions, share supportive or opposing views, and offer suggestions for improvement via comments or separate threads. This process enables the proposal to be examined from multiple perspectives, allowing the proposer to refine the TIP draft accordingly.

**Key Implementation Measures:**

- **Discord Dedicated Channel and Thread Management**:
All RFCs are conducted in a dedicated Discord channel with each RFC having its own separate thread. A “RFC Writing Checklist” is pinned at the top of the channel, ensuring that the proposer includes required elements such as [Title], [Summary], [Background & Motivation], [Proposal Details], [Expected Impact], [Implementation Plan], and [Voting and Next Steps].
- **Bot Notification Feature**:
When a new RFC is posted, a Discord bot automatically detects it and sends a notification to the #announcements channel or mentions a specific role (e.g., @RFC-Notify). This ensures that the entire community is promptly made aware of the new proposal.
- **Discussion Period and Feedback Incorporation**:
A minimum discussion period of [7 days] is set to gather sufficient feedback. During this period, the proposer revises the draft in light of the feedback and, if necessary, pins a mid-discussion summary at the top of the thread for updates.

**Effect:**

This stage ensures that the proposal is sufficiently matured, that community consensus is achieved, and that misunderstandings are minimized. Furthermore, by using Discord—a platform familiar to the users—participation in governance is enhanced.

## 3.2. Temperature Check (Temp Check)

**Timeframe**: [5 days]

**Requirements**: Minimum participation of [0.01%] of TON; Quorum: At least [1%]

**Where**: Snapshot

### Overview

Proposals that have passed the RFC stage are then submitted to a Temp Check vote on Snapshot to quantitatively gauge community support. In this stage, a vote is created that includes a summary of the proposal and voting options (e.g., For/Against). Only accounts that meet a certain TON holding (or delegation) requirement can create this vote.

**Key Implementation Measures:**

- **Vote Creation**:
The proposer creates a Temp Check vote on Snapshot and attaches a link to the corresponding Discord RFC post, allowing voters to easily review the proposal details.
- **Voting Period and Result Criteria**:
The Temp Check vote runs for [5 days]. The vote results are evaluated based on achieving at least [1%] participation of the total supply and a simple majority (more than 50% approval). If the proposal fails to garner sufficient support or if voter participation is low, it does not proceed to the on-chain vote stage and may be subject to further discussion or cancellation.
- **Effect**:
This stage allows the community’s support to be measured off-chain, without incurring gas fees, ensuring that only viable proposals are advanced to the on-chain vote stage.

![](images/91aafe7ef7a8.png)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/21960fca-2b91-4a19-923c-d03cef7b52f6/8f57e7a3-f7b5-4ba1-ab1c-682a84532bea.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHJIY4D%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFTOLphyyoLlysu2H0srusEB3Tj%2Bpc3YuM%2BoiiFqs2zAIhAOY30yOHu99leY8FiXN%2BiPuUYei9s5p4H2me22zDrKLkKv8DCHQQABoMNjM3NDIzMTgzODA1Igx53tKWdlSzCGrgIScq3AMHFmz6WmXUfDemt3FKln7kWMtjUNTL3IBI2wY4BAKamBinMXdVAI637ijtPDS8EycARJ9vXbarKwrlrK45H5kzssqRtyE08o29zEws3KZtZc06c35%2B9lPJAMp4n86JhblHDBZiwrlyRfacWIF7Yq3iWTHFJj6ju2ZqOGQWavGNrprwpc25W%2BKGl1OuWV1tQF5RF5qbTyQKzxUiqEqheJqC7UWlmmS2iTvr43PvdVTJte8WSiihkMqYQWSZOU0z7Yz84mChlreplAQJAmLFY8jMU5q%2FWCteotzxMmlnzbverlCM6ZrCP29h%2FXaX6qZ094R4DtzTpUuVlw%2B%2Fogozu3gcgll0UH89ErZa3esNPt7cUGEq5Iwtm2doZvRC%2B2Mhw5Z4hSpHREFPU9nf%2BNzGTwy47sdbd0O%2BwpCShATfF9cgPWGnrpe7xZFsZCAObetLaMSYzuZJKhiozEweJE09jEwUXqMKXUa9bqw63KCeIXNak%2Bct2cOn5MkNHynRgGsnnaENW5e6ht1ByDDTLJv4vT%2BqrXQ%2FQVY99oPHpEhRfDtFZa9HyBG%2BCDQRtmuWLm0MSvxdddPUJUerVT3XFNlRepJ34gO6YswUlJJ7NCe8Brz6QvibrUakFmV9AD4GWzDA7tnMBjqkAR6wz%2F%2F0E1b0XyyPMSWChW9a6Xjh3t%2Bc4Ryln6KiTHfvY9HAGyXNpQRg%2B2afrlfCfRhE%2FmBIjey0AijgnQXX7SabnAA1AlQNQWvVawLbzg3mwmo4y9oMGet5eNwRrve%2BLOnfqJ73v4ACVDJiUYECMD9y5Zm0fILtkPtF0%2BQPsHJhSZYIBze8hOfhZpWG6P%2BZTNMWkXB5LF1iEI1hWSk3xcEFgl70&X-Amz-Signature=53522ef22a1ce9543c8c576b0e77df1e40beca7c8d4d9ed729fd0af3815eab8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.3. On-chain Vote

**Timeframe:** [Minimum Voting Notice Period: 16 days] + [Minimum Voting Period: 2 days]

**Where**: Tokamak DAO

Proposals that pass the Temp Check now proceed to the formal on-chain vote. The proposer registers the proposal through the on-chain governance contract, and must meet a specified TON holding (or delegation) requirement ([e.g., minimum 20,000 TON]).

**Key Implementation Measures:**

- **Proposal Registration:**
When registering an on-chain proposal, the content must match that of the Temp Check stage, incorporating any feedback received during the RFC and Temp Check phases as necessary, and including a link to the Temp Check that was conducted with the proposal registration.
- **Voting Delay and Voting Period:**
After registering the proposal, a [16-day] voting notification period is implemented to allow token holders to adjust their delegation or staking status. Subsequently, the on-chain vote runs for [2 days], during which all Members participate in the vote.
- **Approval Conditions:**
The on-chain vote must meet predetermined quorum and majority requirements. For example, more than half of the Members must participate in the vote, and [over 50%] must vote in favor. After the vote concludes, the proposal is executed following a final review.

Proposals that pass the Temp Check are moved to "On-chain Vote," where DAO protocols or funds can be finally modified. *Typically, the proposer uploads the proposal content to the DAO's on-chain voting dApp or a custom voting interface* and sets the voting notice period and voting period. The minimum voting notice period is 16 days, and the minimum voting period is 2 days. Anyone can submit a proposal, with a required fee of 10 TON, and the proposal content must be identical to that of the Snapshot stage (however, it should incorporate feedback from the RFC/Snapshot phases). The voting notice period alerts stakeholders that the proposal is live, and during the voting period, only those Candidate Contracts selected as Members are eligible to vote. To assume the role of a Candidate, a proposer must stake at least 1000.1 TON in their Candidate. After that, they can function as a Candidate, and if they have more TON staked than a Member, they can challenge that Member to become a Member themselves. Regular users, who are not Candidates, delegate their voting power to the Candidates through staking, rather than voting directly.

Once the on-chain vote begins, Members with voting rights can cast their votes (For, Against, or Abstain) via the smart contract. Although the voting period is typically set for 2-3 days, this period may vary according to Tokamak DAO's governance rules. During this period, the community may continue discussions on Discord or other channels, and initiatives such as **voting encouragement campaigns** or **supplementary AMA sessions** may be conducted.

If the on-chain vote meets the approval conditions (currently, for example, if 2 out of 3 Members vote in favor), the proposal is executed. The execution period lasts 7 days during which anyone can execute the proposal; however, if no one does so within 7 days, the proposal will not be executed. During execution, a function in the smart contract is automatically triggered to implement changes such as parameter updates, fund transfers, or contract upgrades.

## 3.4. Security Council and Emergency Response (TBD)

In addition to the standard TIP process, Tokamak DAO has established a **Security Council** to handle emergency situations. The Security Council operates via a multi-signature (multi-sig) mechanism, meaning that—for example—at least 2/3 of the signatures must be obtained to halt or modify a proposal in an emergency. This mechanism is applied only to urgent issues such as hacks or critical bugs; under normal circumstances, the outcome of the on-chain vote determined by the community is implemented. The veto power of the Security Council is used very restrictively and must be transparently reported to the community when exercised.

---

# 4. Governance Quality Control and Abuse Prevention

Tokamak DAO takes the following measures to prevent abuse of the governance process and maintain the quality of proposals:

- **Strengthened Proposal Submission Requirements**:
A minimum of [1,000 TON] of voting power is required to initiate a Snapshot Temp Check vote, preventing indiscriminate proposal submissions.
- **Prevention of Duplicate Proposals**:
Proposers are required to check the existing proposal archive before submitting a new proposal. Identical or similar proposals are subject to a cooldown period of at least one month to limit resubmissions.
- **Adherence to Procedures and Feedback Incorporation**:
All proposals must follow the established template and procedures. The operations team verifies that sufficient discussion occurred during the RFC stage and requests revisions if necessary.

---

# 5. On-chain Vote and Execution

The on-chain vote stage is when TIPs that pass the Temp Check are formally decided by the community. Voting power is based on staked TON, and all token holders can participate in the on-chain vote via their wallets. The results are automatically tallied by the governance smart contract, and if the predetermined quorum and majority conditions are met, the TIP is approved. Approved TIPs then undergo a [2-day] timelock period before execution, during which the execution details are automatically implemented and the results are publicly disclosed.

---

# 6. FAQ

**Q1) Can a proposal bypass the RFC stage and proceed directly to Temp Check or an on-chain vote?**

A1) Under normal circumstances, the RFC stage is mandatory to ensure sufficient discussion and community feedback. However, in emergency situations, the Security Council may exceptionally allow this.

**Q2) Can a proposal that is rejected during the Temp Check stage be resubmitted?**

A2) Yes, if the reasons for rejection are clearly addressed and the proposal is significantly revised, it can be resubmitted. However, identical or very similar proposals may be restricted to prevent duplication.

**Q3) Is a timelock always required for on-chain votes?**

A3) A timelock is recommended for security and final review purposes; however, according to the DAO’s rules, immediate execution is also possible.

---

# 7. Conclusion

The TIP lifecycle of Tokamak DAO consists of four stages: RFC, Temp Check, On-chain Vote, and Execution. This process allows the community to freely share opinions and engage in thorough discussion, ensuring that final decisions are made transparently and reliably. Notably, the dedicated Discord RFC channel and individual thread management maximize the clarity and efficiency of proposals, while basing voting weight on staked TON ensures long-term network participation. Although the Security Council is designed to intervene only in emergency situations, under normal conditions the final decision is made by the community as a whole.

By drafting, discussing, voting, and executing proposals according to this document, Tokamak DAO members can actively participate in shaping the network’s future. This TIP lifecycle is a core mechanism for the sustainable development and innovation of the Tokamak ecosystem.