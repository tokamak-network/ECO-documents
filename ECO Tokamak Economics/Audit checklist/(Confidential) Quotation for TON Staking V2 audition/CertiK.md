1/10

- Set call with Certik on 1.17(Tue) 10:30 a.m KST

1/14

- They checked details for audit
- they request 3 things
  1. DAO upgrade commit
  1. DAO Deployment script commit
  1. TON staking 2.5 commit

1/15

Scope

1. DAO Upgrade
a. DAOCommitteeProxy: diff between [https://github.com/tokamak-network/ton-staking-v2/blob/8f89b1adf7c3f4aca32427f7756a2f9a0536da41/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/8f89b1adf7c3f4aca32427f7756a2f9a0536da41/contracts/proxy/DAOCommitteeProxy2.sol) and [https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)
b. DAOCommittee_V1: diff between [https://github.com/tokamak-network/ton-staking-v2/blob/a649acb12e2170e89fe46ab2c56361998f8ec7fc/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/a649acb12e2170e89fe46ab2c56361998f8ec7fc/contracts/dao/DAOCommittee_V1.sol) and [https://etherscan.io/address/0xdF2eCda32970DB7dB3428FC12Bc1697098418815#code](https://etherscan.io/address/0xdF2eCda32970DB7dB3428FC12Bc1697098418815#code)
c. DAOCommitteeOwner: diff between [https://github.com/tokamak-network/ton-staking-v2/blob/3482ab94a3ff63460d1dc9dc8446ffd305b06d26/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/3482ab94a3ff63460d1dc9dc8446ffd305b06d26/contracts/dao/DAOCommitteeOwner.sol) and [https://etherscan.io/address/0xe070fFD0E25801392108076ed5291fA9524c3f44#code](https://etherscan.io/address/0xe070fFD0E25801392108076ed5291fA9524c3f44#code)
1. DAO upgrade script
a. [https://github.com/tokamak-network/ton-staking-v2/blob/deploy-ton-staking-v2.5/scripts/2.deploy_NewDAOStructure.js](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-ton-staking-v2.5/scripts/2.deploy_NewDAOStructure.js)
b. [https://github.com/tokamak-network/ton-staking-v2/blob/deploy-ton-staking-v2.5/scripts/10.createAgendaTest_onMainnet.js](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-ton-staking-v2.5/scripts/10.createAgendaTest_onMainnet.js)
1. TON staking 2.5
DepositManagerV1_1.sol, DepositManagerV1_1Storage.sol, SeigManagerV1_3.sol and SeigManagerV1_3Storage.sol

Audit Quote

1. Audit: $36,000
1. Security Package (Audit + Contract Verification + KYC): $40,000
1. Premium Security (Audit + Contract Verification + KYC + Skynet Active Monitor): $43,000

Timeline
Our earliest starting slot is 01/22, with the preliminary report being available by 02/01. Please let me know how the quote and timeline work for your team — we'd love to collaborate and find solutions together.

1/17

Skynet Active Monitor entails 24/7 coverage of key assets (e.g., website, smart contracts, code repositories, and social media), delivering alerts when an incident is detected to mitigate risk.

Sample: [https://skynet.certik.com/projects/miracle-play#active-monitor](https://skynet.certik.com/projects/miracle-play#active-monitor)

KYC provides private identity and background verification for project teams through a rigorous vetting process while maintaining their privacy. The process entails a video interview with one core member (e.g. CEO/Founder, COO, CTO) and an ID check for key members, after which we publish the KYC badge (gold/silver/bronze) and any additional awards to Skynet.
[https://www.certik.com/resources/blog/7pSqAsYSLro9gMFeuIjPsj-how-we-do-kyc](https://www.certik.com/resources/blog/7pSqAsYSLro9gMFeuIjPsj-how-we-do-kyc)

2/4

What to Expect Next:

1. Our engineering team will deliver a preliminary audit report, complete with findings and recommendations, by February 21, 2025.
1. You and your technical team will be granted access to our audit integration platform, Skyharbor. Here, you can review the audit report. Skyharbor will serve as the primary platform for communication and updates on fixes between our technical team and engineers. If there are any team members to add, please let me know.
1. Upon completion of the remediation based on recommendations in the preliminary report, the final report will be released for your sign-off. You will be able to preview your Skynet score in Skyharbor.
1. A dedicated security profile for your project will be created and listed on the CertiK leaderboard. We will provide the profile URL within two working days.