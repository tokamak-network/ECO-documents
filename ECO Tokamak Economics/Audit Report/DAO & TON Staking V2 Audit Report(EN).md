# **Introduction**

Hello, Tokamak Network community members!

The Tokamak Network has recently conducted an audit along with the DAO and TON Staking V2 upgrades.

If you are interested in the background and details of the DAO and TON Staking V2 upgrade, you can find comprehensive information in [the article linked](https://medium.com/tokamak-network/introducing-ton-staking-v2-9eee7b56c56b). We encourage you to review the article carefully for a deeper understanding.

Following a successful audit, the DAO and TON Staking V2 have been deployed to the mainnet, and a new DAO agenda has been created to implement the upgrade. You can view the agenda and related issues at the links([DAO Agenda #14](https://dao.tokamak.network/#/agenda/14), [DAO Agenda issue](https://github.com/tokamak-network/ton-staking-v2/issues/310)).

This report aims to share the results of the audit conducted prior to deploying the DAO & TON Staking V2 upgrade to the mainnet. The audit was carried out by four parties: professional audit firms CertiK and Omniscia, as well as independent audit experts Hammer and Carl, who all conducted thorough reviews.

The DAO & TON Staking V2 upgrade marks a significant milestone in enhancing Tokamak Network’s staking system and substantially strengthening its security. Before applying this upgrade to the mainnet, we prioritized ensuring protocol reliability through rigorous audits by multiple experts.

This report comprehensively summarizes the audit findings from CertiK, Omniscia, Hammer, and Carl. We have provided concise overviews of each audit’s results, detailed major findings and improvements, and clearly communicated the current security status of the DAO and TON Staking V2. Detailed results from each audit can be found in the attached final reports and GitHub links.

Through this audit process, we have meticulously identified and addressed protocol vulnerabilities to deliver a safer and more efficient DAO and staking system. We deeply appreciate the ongoing interest and support from our community, and we hope this report contributes to greater transparency and trust in the Tokamak Network.

By reading this report, you will gain a clear understanding of each audit agency’s professional findings and be able to confirm the stability and reliability of the DAO & TON Staking V2 upgrade.

# Audit Overview

We engaged four audit firms (CertiK, Hammer, Carl, Omniscia) to review the systems related to the DAO & TON Staking V2 upgrade.

## Audit Scope

### Repo (Branch)

- [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request)
- The latest commit hash: **01e198130b178757dd194bd8726a1ab678fca167**

### Contract scope

- [DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol)
- [DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol) 
- [DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol) 
- [SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol)
- [DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol)
- [L1BridgeRegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol) 
- [Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol) 
- [OperatorManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol) 
- [CandidateAddOnV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol) 

## Audit Periods and Issues Identified by Each Auditor

Thanks to the efforts of the four audit parties, a total of 66 issues of varying severity were discovered. The Tokamak Network is pleased to have diligently addressed these findings, demonstrating our commitment to delivering a secure and robust TON Staking V2 platform.

### 1. CertiK

- Link: [Homepage](https://www.certik.com/), [tokamaknetwork_project_page](https://skynet.certik.com/ko/projects/tokamak-network)
- Audit Period: **January 31, 2025 - April 1, 2025**
- Total Issues Found: **15** **issues**
- Distribution by Severity Level:
- *CRITICAL : 0 issues*
- *MAJOR: 1 issue (Resolved)*
- *MEDIUM: 3 issues (Resolved)*
- *MINOR: 6 issues (4 Resolved, 2 Acknowledged)*
- *INFORMATIONAL: 4 issues (Resolved)*
- *CENTRALIZATION: 1 issue (2/3 Multi-Sig)*
- [Audit Report](https://drive.google.com/file/d/1aabEgZdXD6y4t_ZM-BXd2xSi9kD2qVGK/view)

### 1. CertiK

| **Distribution by Severity Level** |  | **Distribution by Category ** |  |
| --- | --- | --- | --- |
| ***CRITICAL*** | 0 *issues* | ***Logical Issue*** | *4 issues* |
| ***MAJOR*** | *1 issue (Resolved)* | ***Design Issue*** | *2 issues* |
| ***MEDIUM*** | *3 issues (Resolved)* | ***Volatile Code*** | *3 issues* |
| ***MINOR*** | *6 issues (4 Resolved, 2 Acknowledged)* | ***Coding Issue*** | *2 issues* |
| ***INFORMATIONAL*** | *4 issues (Resolved)* | ***Concurrency*** | *1 issue* |
| ***CENTRALIZATION*** | *1 issue (2/3 Multi-Sig)* | ***Coding Style*** | *2 issues* |
|  |  | ***Centralization*** | *1 issue* |
| **Total Issues Found** | 15 issues |  |  |

| **Distribution by Severity Level** |  |
| --- | --- |
| ***CRITICAL*** | 0 *issues* |
| ***MAJOR*** | *1 issue (Resolved)* |
| ***MEDIUM*** | *3 issues (Resolved)* |
| ***MINOR*** | *6 issues (4 Resolved, 2 Acknowledged)* |
| ***INFORMATIONAL*** | *4 issues (Resolved)* |
| ***CENTRALIZATION*** | *1 issue (2/3 Multi-Sig)* |
|  |  |
| **Total Issues Found** | 15 issues |

- Link: [Homepage](https://www.certik.com/), [tokamaknetwork_project_page](https://skynet.certik.com/ko/projects/tokamak-network)
- Audit Period: **January 31, 2025 - April 1, 2025**
- [Audit Report](https://drive.google.com/file/d/1aabEgZdXD6y4t_ZM-BXd2xSi9kD2qVGK/view)

### 2. Hammer

- Audit Period: **February 5, 2025 — March 13, 2025**
- Total Issues Found: **9 issues**
- Distribution by Severity Level:
- *CRITICAL: 2 issues (Resolved)*
- *HIGH: 1 issue (Resolved)*
- *MEDIUM: 0 issues*
- *LOW: 6 issues (Resolved)*
- [Audit Report](https://github.com/hooki/audit/blob/main/STAKING_V2_AUDIT_REPORT_EN.pdf)

| **Distribution by Severity Level** |  | **Distribution by Category ** |  |
| --- | --- | --- | --- |
| ***CRITICAL*** | *2 issues (Resolved)* | ***Logical Issue*** | *2 issues* |
| ***HIGH*** | *1 issue (Resolved)* | ***Design Issue*** | *1 issue* |
| ***MEDIUM*** | *0 issues* | ***Volatile Code*** | *1 issue* |
| ***LOW*** | *6 issues (Resolved)* | ***Coding Issue*** | *5 issues* |
| **Total Issues Found** | 9 issues |  |  |

| **Distribution by Severity Level** |  |
| --- | --- |
| ***CRITICAL*** | *2 issues (Resolved)* |
| ***HIGH*** | *1 issue (Resolved)* |
| ***MEDIUM*** | *0 issues* |
| ***LOW*** | *6 issues (Resolved)* |
|  |  |
| **Total Issues Found** | 9 issues |

### 3. Carl

- Audit Period: **February 3, 2025 — March 5, 2025**
- Total Issues Found: **21 issues**
- Distribution by Severity Level:
- *CRITICAL: 2 issues (Resolved)*
- *MAJOR: 0 issues*
- *MEDIUM: 4 issues (Resolved)*
- *MINOR: 1 issue (Resolved)*
- *INFORMATIONAL: 14 issues (Resolved)*
- [Audit Report](https://github.com/4000D/audit-reports/blob/main/Tokamak%20Network%20-%20Staking%20v2%20Security%20Assesment.pdf)

| **Distribution by Severity Level** |  |
| --- | --- |
| ***CRITICAL*** | *2 issues (Resolved)* |
| ***MAJOR*** | *0 issues* |
| ***MEDIUM*** | *4 issues (Resolved)* |
| ***MINOR*** | *1 issue (Resolved)* |
| ***INFORMATIONAL*** | *14 issues (Resolved)* |
|  |  |
| **Total Issues Found** | 21 issues |

### 4. Omniscia

- Link: [Homepage](https://omniscia.io/), [X](https://x.com/Omniscia_sec/status/1889721009311195529), [linkedin](https://www.linkedin.com/feed/update/urn:li:activity:7295486669867171840)
- Audit Period: **January 31, 2025 — February 26, 2025**
- Total Issues Found: **21 issues** (Only Minor and above counted)
- Distribution by Severity Level:
- *MAJOR: 3 issues (Resolved)*
- *MEDIUM: 10 issues (Resolved)*
- *MINOR: 8 issues (Resolved)*
- Note: **In Omniscia’s case, the final resolution of issues was handled by Hammer.**
- Audit Result: [Issues of Label "by omniscia" in ton-staking-v2 repo](https://github.com/tokamak-network/ton-staking-v2/issues?q=is%3Aissue%20label%3A%22by%20omniscia%22%20)

| **Distribution by Severity Level** |  |
| --- | --- |
| ***MAJOR*** | *3 issues (Resolved)* |
| ***MEDIUM*** | *10 issues (Resolved)* |
| ***MINOR*** | *8 issues (Resolved)* |
|  |  |
| **Total Issues Found** | 21 issues |

# Resolve Major Issues

## DAO

1. Potential Storage Collision
- **Problem** : Risk of storage layout conflicts and data corruption due to changes in inheritance order during upgrade
- **How to resolve** : Fix the problem by keeping the existing layout without changing the inheritance order.
- **Related Audit Issues** : [CON-02(CertiK)](https://drive.google.com/file/d/1aabEgZdXD6y4t_ZM-BXd2xSi9kD2qVGK/view), [TS-01(Carl)](https://github.com/4000D/audit-reports/blob/main/Tokamak%20Network%20-%20Staking%20v2%20Security%20Assesment.pdf)
- **Expected Impact : **After fixing, Storage Collisions will no longer occur.

2. Centralization Risks

- **Problem** : the DEFAULT_ADMIN_ROLE account may allow the hacker to take advantage of this authority
- **How to resolve** : The DEFAULT_ADMIN_ROLE authority held by the personal EOA account has been transferred to the MultiSigWallet Contract
- **Related Audit Issues** : [CON-01(CertiK)](https://drive.google.com/file/d/1aabEgZdXD6y4t_ZM-BXd2xSi9kD2qVGK/view), [TS-02(Carl)](https://github.com/4000D/audit-reports/blob/main/Tokamak%20Network%20-%20Staking%20v2%20Security%20Assesment.pdf)
- **Expected Impact : **Even if a personal EOA account is hacked, the hacked personal EOA account cannot use DAO permissions.
- **MultiSigWallet Repo** : [https://github.com/tokamak-network/tokamak-multisig-wallet](https://github.com/tokamak-network/tokamak-multisig-wallet)

3. Inexistent Delay Between Membership States

- **Problem** : The changeMember and retireMember functions can be executed consecutively without Delay. By utilizing this, the candidate with the highest totalStaked can replace all existing Members in a single transaction.
- **How to resolve** : changeMember has a cooldownTime added to prevent it from being changed continuously, and when retireMember is executed, the corresponding Member is put in a blacklist.
- **Related Audit Issues** : [Issue No.274 DAO-11M by Omniscia](https://github.com/tokamak-network/ton-staking-v2/issues/274), [Issue No.62 by Hammer](https://github.com/tokamak-network/ton-staking-v2/issues/62)
- **Expected Impact : **After changeMember is executed, the same candidate can call changeMember again only after cooldownTime has elapsed And Members who execute retireMember are added to the blackList and cannot use DAO functions unless they are excluded from the blackList via the DAO Agenda.

Through this DAO upgrade and audit process, the key areas mentioned above have been significantly improved. Details of the changes made as a result of the audit can be found in each audit report. If you are interested in learning more about what has changed with this DAO upgrade, please refer to the [link](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/doc/en/dao-upgraded-en.md).

## TON Staking V2

### ** 1. Vulnerability in Layer2 TVL Manipulation**

**Description**

The increaseTot method allowed attackers to register a malicious CandidateAddOn as a Layer2, enabling them to hijack another Layer2’s rollup config and artificially inflate its TVL, disrupting seigniorage distribution.

**Resolution**

A mapping was created between the operator and the Layer2 address for verification during TVL checks, effectively resolving this vulnerability.

**Related Issues**

- [Issue No 303.](https://github.com/tokamak-network/ton-staking-v2/issues/303) [[CRITICAL #02] A vulnerability that allows manipulating Layer2 TVL by hijacking another Layer2’s rollup config (by Hammer)](https://github.com/hooki/audit/blob/main/STAKING_V2_AUDIT_REPORT_EN.pdf)

**Expected Impact**

By creating a mapping between the operator and the Layer2 address, the system eliminates the risk of an attacker manipulating the rollup configuration and hijacking the TVL. This ensures that only legitimate Layer2s can be verified for their TVL, thus safeguarding the integrity of the seigniorage distribution process.

### **2. Seigniorage Distribution Error**

**Description**

The SeigManager inaccurately distributed seigniorage due to miscalculations with initialDebt, failing to update this value when the Layer2's TVL changed, leading to unfair reward allocation.

**Resolution**

Logic modifications were implemented to ensure initialDebt is consistently updated with any TVL changes across all calculations.

**Related Issues **

- [[HIGH #01] Seigniorage distribution error due to miscalculation of initialDebt (by Hammer)](https://github.com/hooki/audit/blob/main/STAKING_V2_AUDIT_REPORT_EN.pdf)
- [SMV-07 | Inconsistent Reward Calculation for Layer2 by Certik](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/audits/certik/PRE-preliminary-20250305T015421Z.pdf)

**Expected Impact**

With the corrected logic for updating initialDebt when the TVL changes, the seigniorage distribution becomes fairer. It prevents scenarios where a Layer2 might receive disproportionately high rewards due to outdated TVL calculations, ensuring that all participants get the rewards they rightfully earn based on current metrics.

### **3. Incorrect Layer 2 Distribution Management**

**Description**

The seigniorage distribution mechanism was incorrectly implemented, not calculating l2TotalSeigs in the l2RewardPerUint variable for non-layer2 calls.

**Resolution**

Code changes ensured that seigniorage is distributed to Layer2s regardless of initiated calls from non-layer2 users.

**Related Issues **

- [SMV-05 | Unused Minted Tokens in `layer2Manager` Contract by Certik](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/audits/certik/PRE-preliminary-20250305T015421Z.pdf)
- [[SM3-08M] Incorrect Layer 2 Distribution Management by Omniscia](https://github.com/tokamak-network/ton-staking-v2/issues/156)

**Expected Impact**

By allowing seigniorage to be distributed even when calls come from non-layer2 users, the system ensures that all valid Layer2s receive their entitled rewards consistently. This means that seigniorage distribution is more robust and equitable, reducing the chances of skewed allocations.

### 4. InitialDebt Calculation Error with Pause/Unpause

**Description**

Calling the pause and unpause methods consecutively could cause Initial Debt to be initialized, which could cause the seigniorage distributed to the Layer 2 sequencer to be calculated unintentionally.

**Resolution**

Restricted the pause method from being called consecutively.  

**Related Issues **

- [SMV-06 | Incorrect Reward Allocation After Unpause by Certik](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/audits/certik/PRE-preliminary-20250305T015421Z.pdf)
- [[SM2-04M] Improper Management of Pause States by Omniscia](https://github.com/tokamak-network/ton-staking-v2/issues/148)

**Expected Impact**

Restricting consecutive calls to pause eliminates the potential for unintended resets of the pause period, which would otherwise disrupt the seigniorage distribution. This change prevents quick toggling between paused and unpaused states that could lead to inconsistencies in reward calculations.

### **5. Incorrect Evaluation of Negative Commission State**

**Description**

The _calcSeigsDistribution function may update a Layer2's commission rate negatively, using outdated data instead of reflecting the most recent updates.

**Resolution** 

The determination of negative commissions is now assessed after updating Layer2’s commission rate.

**Related Issues **

- [[SM3-07M] Incorrect Evaluation of Negative Commission State by Omniscia](https://github.com/tokamak-network/ton-staking-v2/issues/155)

**Expected Impact**

By updating the mechanism for evaluating whether a Layer2’s commission rate is negative after a fresh update, the system ensures that commission rates reflect the most current and accurate data. This prevents erroneous assumptions about commissions, helping maintain trust and accountability within the Layer2’s financial mechanisms.

### Overall Impact

Overall, these changes enhance the security and reliability of the Tokamak Network's staking and seigniorage distribution processes. They help prevent vulnerabilities, ensure fair reward distribution, and maintain the integrity of Layer2 operations, contributing to a more robust decentralized finance ecosystem.

# Conclusion

The Tokamak Network sincerely thanks CertiK, Hammer, Carl, and Omniscia for their dedicated efforts and valuable insights. Through this audit process, the security and stability of TON Staking V2 have been further strengthened, with all critical and major issues promptly resolved. Additionally, minor issues were addressed with care, and recommendations were thoroughly implemented, further enhancing the overall reliability of the system.

This comprehensive and systematic audit process demonstrates Tokamak Network’s strong commitment to providing a safe and trustworthy platform for the community and Layer2 partners. Based on the success of this audit, we are now able to prepare for the TON Staking V2 mainnet upgrade — scheduled for Q2 2025 and pending DAO approval — with even greater confidence.

Tokamak Network will continue to prioritize transparency, security, and community trust, striving for ongoing technical excellence.