**Name**

shinthom

**About me**

I'm a DeFi researcher focused on Layer 2 scaling and tokenomics. I prioritize protocol security, sustainable treasury management, and community-driven growth. I will vote transparently and engage actively in all governance discussions.

**Why I want to be a delegate**

I want to actively contribute to shaping the future of Tokamak Network rather than being a passive observer. As a delegate, I can help make informed decisions that benefit the entire ecosystem and ensure diverse community perspectives are represented in governance.

**Address or ENS**

shinthom.eth

---

# TIP-007: Update Voting Period

## Summary

This proposal seeks to extend the governance voting period from 5 days to 7 days to allow for more comprehensive community participation and discussion.

## Motivation

Recent governance proposals have shown lower-than-expected voter turnout. Analysis indicates that many token holders, particularly those in different time zones or with limited availability during weekdays, have insufficient time to review proposals thoroughly and cast their votes.

A 7-day voting period aligns with a full weekly cycle, ensuring that all community members have at least one weekend to participate regardless of their schedule.

## Specification

| Parameter | Current Value | Proposed Value |
| --- | --- | --- |
| `votingPeriod` | 5 days | 7 days |

**Contract:** TokamakGovernor

**Function:** `setVotingPeriod(uint256 newVotingPeriod)`

## Rationale

1. **Increased Accessibility** - A full week allows global participants across all time zones to engage
1. **Better Informed Decisions** - More time for community discussion and due diligence
1. **Higher Participation** - Weekend inclusion typically increases voter turnout by 15-20%
1. **Industry Standard** - Most major DAOs (Uniswap, Compound, Aave) use 7-day voting periods

## Risks

- Slightly slower governance execution speed
- Minimal impact on urgent proposals (emergency actions remain unaffected)

## Voting Options

- **For** - Approve extending the voting period to 7 days
- **Against** - Keep the current 5-day voting period
- **Abstain** - Neutral on this proposal

TIP-008: Implement Delegate Incentive Rewards

## Summary

This proposal introduces a reward mechanism to incentivize active delegate participation in governance by distributing a portion of protocol fees to delegates who consistently engage in voting.

## Motivation

Many DAOs struggle with voter apathy and inconsistent delegate participation. By rewarding delegates who maintain high voting participation rates, we can foster a more engaged and responsive governance ecosystem.

## Specification

**Eligibility Threshold:** Delegates must vote on at least 80% of proposals within a quarter

**Reward Pool:** A small percentage of protocol fees allocated to qualifying delegates

**Distribution:** Quarterly, proportional to participation rate among eligible delegates