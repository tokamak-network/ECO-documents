# Introduction

A Tokamak Improvement Proposal (TIP) is a proposal submitted by a member of the Tokamak DAO to suggest changes or enhancements to the Tokamak ecosystem. TIPs are categorized into two types:

- **Tokamak Core**: Proposals that address the core architecture of the Tokamak ecosystem, including changes to essential system components such as core contracts, staking mechanisms, bridges, or any actions requiring chain owner permissions.
- **Tokamak General**: Proposals that involve requests for funding, grants, or general community guidelines and informational updates.

The following sections outline the core principles, proposal lifecycle, and governance mechanisms that define Tokamak DAO V2, ensuring an inclusive, transparent, and efficient governance structure.

# The Anatomy of a Tokamak Improvement Proposal (TIP)[](https://docs.arbitrum.foundation/concepts/lifecycle-anatomy-aip-proposal#the-anatomy-of-an-arbitrum-improvement-proposal-aip)

The Tokamak DAO encourages proposers to include the following sections within Improvement Proposals:

- **Abstract** - Two or three sentences that summarize the TIP. (TLDR)
- **Rationale** - A statement on why the community should implement the TIP.
- **Specifications** - How will this proposal affect the protocol both technically, socially, financially (if applicable), and governance-wise?
- **Steps to Implement** - The steps to implement the TIP, including any associated costs, code (optional in RFC, mandatory in Snapshot proposal), and any other resources for each step where applicable.
- **Voting**: Define what a “yes” and “no” vote entails. 

If a TIP is not approved on the initial submission, the proposer has the option to resubmit it after addressing the community's feedback. The resubmitted TIP should include the following additional sections:

- **A link to the original TIP**
- **Explanation of why the TIP was not approved**
- **Details of the revisions made to the TIP**
- **Supplementary information** (Providing clearer intentions, comprehensive details, and implications can assist the community in better understanding the revised TIP, thereby enhancing its chances of being approved).

# **The lifecycle of a Tokamak Improvement Proposal**

## Technical overview[**​**](https://docs.arbitrum.foundation/concepts/lifecycle-anatomy-aip-proposal#technical-overview)

For a technical overview of implementation details

<CONTRACT INFORMATION> etc.

# **Process**[**​**](https://docs.uniswap.org/concepts/governance/process#process)

Below we outline the Tokamak DAOv2 governance process, detailing where these venues fit in. These processes are subject to change according to feedback from the community.

### **Phase 1: Request for Comment (RFC)**[**​**](https://docs.uniswap.org/concepts/governance/process#phase-1-request-for-comment-rfc)

*Timeframe*: At least 7 days

Where:  Discord

As a proposer, you should use the RFC phase to introduce the community to your proposal. Your post should detail exactly what you are asking delegates to vote on as well as your rationale for why it is a good idea. You should be prepared to answer questions about your proposal. Willingness to adjust based on community feedback is a hallmark of successful past proposals.

To post an RFC, l**abel your post “RFC - [Your Title Here]”**. Before moving to Phase 2, give the community at least 7 days to read and comment on the RFC. Please respond to questions in the comments, and take feedback into account in the next iteration of the proposal posted in Phase 2.

### **Phase 2: Temperature Check**[**​**](https://docs.uniswap.org/concepts/governance/process#phase-2-temperature-check)

*Timeframe*: 5 days

Threshold(Minimum): 0.01 % of TVT (Can we check with zero first?)

*Quorum (Yes)*: 1 % of TVT

Precondition:  NIL

Where: Snapshot

The purpose of the Temperature Check is to signal community sentiment on a proposal before moving towards an on-chain vote.

To create a Temperature Check:

1. Incorporate the community feedback from the RFC phase into the proposal.
1. Create and post this version of the proposal in  <Github Issue/Discord> with the title “Temperature Check — [Your Title Here]”. Include a link to the RFC post. You will update the post to include a link to the Snapshot poll after you’ve posted that.
1. Create a Snapshot poll. The voting options should consist of those which have gained support in the RFC Phase. This poll can be either binary or multiple choice but must include a `No change` option. Set the poll duration to 5 days. Include a link to the Forum Temperature Check post.
1. Update the Forum post with a link to the Snapshot Poll.

At the end of 5 days, the option with the majority of votes wins. There must be at least _ staked TON `Yes` votes to move onto Phase 3. If the “No change” option wins, the proposal will not move on to Phase 3.

### **Phase 3: Governance Proposal**[**​**](https://docs.uniswap.org/concepts/governance/process#phase-3-governance-proposal)

*Timeframe*: 2-day waiting period, 7-day voting period, 2-day timelock, Security Council Approval

*Threshold*: 0.1 % of TVT ( Burn 10 TON?)

*Quorum*: 4 % of TVT

Where: Tally

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e33a7a28-b920-4c2b-8b77-d6995ff5d7f1/Screenshot_2024-11-07_at_5.04.36_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPZMBHN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQZFB5dX%2B%2BpCG5aiMrUmTWYa8VFa6Fp0lz4T1PkKd4oAiB%2FUSzlqLWyiMFBsDlZ383YySp%2BE%2FRfrvPvud4Bb3PA0Cr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM7D%2Bys1yqTeYmTN%2F5KtwDw%2FHASLYGutODgDsN5LkIiBW2%2BIwpD1mjb3zWFrhVzD%2Bsf3qH0j%2FpdqhWObYakWsyQ%2B3BINbnIh4JMVczoW5iAp1ATyVYjX67bap3U3oCzRgTdIR31XycGrrq8Vi4FWo3Gr9EFhVtKg7dj6tNlh9h4yr21pxoKI3%2FZVb6FjFzNcUl7tk%2FAQmJQDvHEtmfcOKlivAvn2IEWa6lTFPy9IddnF36HyKeYGXuMZrnbpsTNPSg5IAQagzutxWpjuh3uEbYTeNk92EDQQv4xgTLr3h%2BlbyCG%2BKKEx11%2BB8g9UXdnbyhK3R4G9DO6uLMB2JWiLQQl6qim2wHbXAdxBingoWg%2FANPuxN13VdLXhcWm7%2FcdGU%2FsveVgGRCvgwGKh0om2jlTDxbzHvCjYN1ZJUekbnqeFOBPn%2ByZHHlbZdLY8%2F1VaR4Nf9KFsSQovvYFR6thD7sMHPXW%2BOS2VYiDZLu8P0xcqLB%2BRZKlyXRPCBSc2mjihPBqo5eVxEoGCwbvoJMID0OrYXGtsFznf2eLPnxoWiltOe6NgxCgKKBa%2F6CdKgv%2BohdFeOpzS7yK3ARRAxunwlEoR6Kt0wo36wspwUMCUiDz%2B8GwhP5GzoDJpXsKb9obPmXkQw%2Bzf3Pi2fePuswoJnbzAY6pgEh8nEUE1ZQ3yjhBxkVYng7FFKxwWOGR158Nf%2BhbRcFV0F5mw%2Fa90II32oDy0Hzho2edQGL1eIRPyxUZrDQs0jf7L1LgXAjiO2JBfYVNDSWVa8kV0O2s%2B9RBmiTloAM8iO%2FHLpLUZG%2BuKpuBCuLco25qpgU3eJ5f5TQd%2FKainHgJ4xenDFJ77s6xEBDAJhs%2Br64dngQfFENTq%2FkqpJWcEgUOSIYjeI%2B&X-Amz-Signature=80d49bdfc038965114c61466f33ee8092c2bd08274ef2e0f32e349741b6e23a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Phase 3 is the final step of the governance process. If this vote passes, then a change will be enacted on-chain.

To create an on-chain Governance Proposal:

1. Incorporate any last iterations to your proposal based on feedback before posting.
1. Create a topic in the Discord/Github Issue titled "Governance Proposal — [Your Title Here]" and link to previous forum posts and the Temperature Check Snapshot poll.
1. Create your proposal. This is done through an interface (Tally). If writing the calldata yourself, please review the logic with a qualified Tokamak community member before posting the proposal. If the proposal passes, this calldata will execute.
1. Ensure that at least _ staked TON is delegated to your address to submit a proposal, or find a delegate who has enough delegated staked TON to meet the proposal threshold to propose on your behalf.
1. Once you submit the proposal, a two-day voting delay will start. After the voting delay finishes, a ~seven-day voting period begins. If the proposal passes, a two-day timelock must pass. The Security Council can then take the final action to veto/execute the proposed code. A 2/3 majority vote is required for a proposal to pass the Security Council's review.

# **Typical Execution Timeline**

- Standard execution period: 30 to 40 days (RFC → Execution)