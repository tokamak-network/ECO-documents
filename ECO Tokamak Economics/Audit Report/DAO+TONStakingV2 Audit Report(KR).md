# 소개

안녕하세요, 토카막 네트워크 커뮤니티 멤버 여러분!

저희는 토카막 네트워크의 지원을 받아 DAO와 TONStakingV2 업그레이드를 진행한 ECO팀입니다. 

이 보고서는 DAO+TONStakingV2의 업그레이드를 메인넷에 배포 전에 진행한 해당 Audit결과를 공유드리려고 합니다. 이번 Audit은 총 4곳에서 이루어졌으며, 전문 Audit 업체인 CertiK과 Omniscia, 그리고 개인 Audit 전문가 Hammer와 Carl이 참여해 세밀하게 점검을 진행하였습니다.

DAO+TONStakingV2 업그레이드는 토카막 네트워크의 staking 시스템을 개선하고 보안성을 대폭 강화하기 위한 중요한 이정표입니다. 이 업그레이드를 메인넷에 적용하기 전에, 우리는 여러 전문가의 철저한 감사를 거쳐 프로토콜의 신뢰성을 확보하는 데 중점을 두었습니다.

본 보고서는 CertiK, Omniscia, Hammer, Carl 4곳의 감사 기관 및 전문가가 수행한 Audit 결과를 종합적으로 요약한 내용을 담고 있습니다. 각 Audit 결과에 대한 내용을 간략히 정리하였으며, 주요한 발견 사항 그리고 개선된 내용을 상세히 다루며, DAO  및 TONStakingV2의 보안 현환을 명확하게 전달하고자 합니다. 기관별 Audit의 세부 결과는 첨부한 최종보고서와 github링크를 통해서 확인가능합니다.

이번 감사를 통해 우리는 프로토콜의 취약점을 면밀히 파악하고, 이를 보완하여 더 안전하고 효율적인 DAO와 staking 시스템을 제공할 수 있도록 노력하고 있습니다. 커뮤니티 여러분의 지속적인 관심과 지원에 깊이 감사드리며, 이 보고서가 토카막 네트워크의 투명성과 신뢰성을 한층 높이는 데 기여할 수 있기를 바랍니다.

이 보고서를 통해 여러분은 각 감사 기관의 전문적인 Audit 내용을 이해하고, DAO+TONStakingV2 업그레이드의 안정성과 신뢰성을 확인하실 수 있을 것입니다.

# Audit 개요

저희는 네 곳의 Audit 업체(CertiK, Hammer, Carl, Omniscia)가 TONStakingV2의 업그레이드 관련 시스템을 검토했습니다. 

## Audit 범위

### Repo (Branch)

- [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request)
- the latest commit hash:  **01e198130b178757dd194bd8726a1ab678fca167**

### Contract scope  

- DAOCommitteeProxy2.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol)
- DAOCommittee_V1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol) 
- DAOCommitteeOwner.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol)
- SeigManagerV1_3.sol : [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol) 
- DepositManagerV1_1.sol: [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol)
- L1BridgeRegistryV1_1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol)
- Layer2ManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol)
- OperatorManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol)
- CandidateAddOnV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol)

## Audit 업체별 기간 및 발견된 이슈

네 곳의 Audit 업체의 노력으로 다양한 심각도 수준에 걸쳐 총 66개의 문제가 발견되었습니다. ECO 팀은 이러한 발견 사항을 성실히 처리하여 안전하고 강력한 TON 스테이킹 V2 플랫폼에 대한 저희의 헌신을 입증하게 되어 기쁘게 생각합니다.

### 1. CertiK

- Link : [Homepage](https://www.certik.com/), [tokamaknetwork_project_page](https://skynet.certik.com/ko/projects/tokamak-network) 
- Audit 기간 : 2025년 1월 31일 ~ 2025년 4월 1일
- 발견된 이슈
  - **총 발견 이슈:** 15건
  - **이슈 등급별 분포:**
    - Critical(치명적): 0건
    - Major(중대): 1건 (해결됨)
    - Medium(보통): 3건 (해결됨)
    - Minor(경미): 6건 (4건 해결됨, 2건 인정)
    - Informational(정보성): 4건 (해결됨)
    - Centralization : 1건 (2/3 Multi-Sig)
- Audit Report
[CertiK-AuditReport.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ae67a68e-e1ee-41c4-87bf-9fd6fc960feb/CertiK-AuditReport.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z52HEEDU%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T062917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwj4q7TBhhn814wShh%2B6V4tNBT9bImjUBQGTiOtpRYcAIgdpoOH6tJhAaGWpz56iIibK6GVP31u8eny0%2BqAcabOt0q%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDAQtBz8LN1HHVAmJRSrcA52b7c0nkZiA658WtdpVPiwKq%2BI5PclJb46zGeF3kfSspDpNAqfYqX60b34PR4bLT%2FPyq69vB21AK11cL4G59rzwT1TqbrBYvGcOh3RmJ4ZGmkg9NI8ZV4LoYDtIrq5iujWqnh7UlVZaxpbznTkLbA5V0xi3EA1XIwmTt4S%2FqbKc98bQDJRc785UcB5uzu%2BzTJYAaKyQ5VUSmPJe32HnveRfQm5ujNnvv09gPFA9n8LcPjzUXim3qZIqnOIBatZ2ygo%2FiL5n5cuxin98cAsBlSLOUxTwkrovsqEYq83JAU2h9UruFdJsMY8qMAySS6KAlutjFsBzsDcpzwIx1%2Bxd9GCAGjoNYoSj7dWQrgWDKw0RPNK9GW06XIHn3jiZp6e1Z22g8C4xgAsi%2FstuTVSxRbkezcqQclTaOiJhBZbya6rxvmdcaHa5TPvJPzN6mJe%2BB5czB3%2BHGLC%2BiBVU6jpuuoUOtVtR2Ny160zzP3CludC433PxSN7lnemevbv7Pg7yjgzI0SIdci4ZTLyJuUmFEPvL%2B46qLE3XcsUE3ly29OtCcshV%2BWURFK7J5C3TFF1JfhzsYofRNOcg%2FrCeI7ierEMemEaK%2F6SvGneDVFSofbsaRVb%2FbTF3jnxq4OcSMJTE2swGOqUBbchhdDLcoJ%2F6j5QbfClqLLpxrqaH%2B%2F213EOQ%2F2ub6Y03RDEdzkDIo8OeJc9uckCQ48YPKWcbJpn3uJDEeJ08%2BFbHWwNS7c4pXSlzUaV3UQOFdBP0GXegLAiTwaPwqmCyMyykUpwHs0LyEa%2BcwbUU3iBh0HqBsfsAHLfhVUtX0%2Bg9A53lwf9eyfSCcOqW72hefMdxYAGqxcaWLwdqinZJ1EICPazO&X-Amz-Signature=ca80801b15ab79811f14e1769db9fdf646f47242fc8f434bc4cc5008bf2f147c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 2. Hammer

- Audit 기간 : 2025년 2월 5일 ~ 2025년 3월 13일
- 발견된 이슈
  - **총 발견 이슈:** 9건
  - **이슈 등급별 분포:**
    - **CRITICAL**: 2건 (해결됨)
    - **HIGH**: 1건 (해결됨)
    - **MEDIUM**: 0건
    - **LOW**: 6건 (해결됨)
- Audit Report
[Hammer_AuditReport_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0b913e35-e37e-49d7-9fba-45fa01c1774e/Hammer_AuditReport_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZZHCAJY%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T062918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6ByZ%2BUCMXmtoqi%2FNnjveWtOQHNt12oiwiVk7I8AzVjQIhANKiokO%2FQnuHuAKlW8HV1OwpijIzf9tsMWcUWmUtO0OkKv8DCHcQABoMNjM3NDIzMTgzODA1IgzWJxJ79Vi5izNLTLkq3APEJ8gLpBQFReGn5TKBv5Je7Sm%2BM%2BEGq%2FabJXk5PDRNZMHgS0%2F9Pg1knCK1ccYbZDzWWgr7egWSxWGnoYwKgPSjSyPMSQ6i2k7F%2B4oWVfJ%2FU4L%2BDvHJe5JzfnoTv3pa3dgzbtQClMcZ22dRK0yJIWGwWF%2FdJgF5KpcRyMWoSvjf5CGbj2Kuo6FQl89fY2XMJqe6hLlHs3%2BGOfK9exMmKsxj2CZ%2F3rHKlkSh5BpJO5l4tzTC4CMHf%2F7u2uYKyXxybN6Uq6bdBn2GUt1Xuz1KOBVG72%2F5Ufwot4FrvIzRP3Hs6RY7vYXjqLrnl1HCP%2BlCL306QIgwhjWm4CY%2B0b5ShanA5FTfUt0iYbf%2FdkLbA%2BFM8bef%2F26%2BfoOUPYuusa%2FPtPgAS6nDcWDiHQ6JT%2FjKedPHn%2ByAPCORqse16ztUunk79WMWtx6vARkKYVDfVciIcuZMCkHXLHCrWHm6l9O2DZpjMWCzjT7TFCeGn3gT61Zpp6PEO0LyD8QNluZrzfwaNnHCsFv5CiWPLPJg%2B0iiPU3aXGVdR4HzSlIl6PCifJzZ8jqkNWHnCc8fXH9IwZC58WBcyfJbCmYoHlvpwkUygfLa1CknSb5wDf18ogP1tXIU7J3CdwcrOEIXeTU0rzD2w9rMBjqkAfZ3Ve3YXu%2FNCMv1xznZI%2Fmw3C0f%2FQrLf2SKd6F5jQbskOuJZ1FCylNwWyrqQiwN%2BdfEOyenF8ZUOFosup1GJCOqxI6y%2BV%2FCOl%2BlUh9f0yzni2aJuGxvak%2FejzwuIYZJCkqv7pER86f8%2FMAA%2FbWQLCg29nnzqCeJbACsUZPpSfT0LQbIjGwRIPVl5b%2FbMUAG7Pn6r4wHLfRR%2FkdjKKDXQC%2FVnLOL&X-Amz-Signature=cff3aaac241f53f05bc028f97f81a26e61785cd718a2c33e8e4a88061451b85d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 3. Carl

- Audit 기간 : 2025년 2월 3일 ~ 2025년 3월 5일
- 발견된 이슈
  - **총 발견 이슈: **21건
  - **이슈 등급별 분포:**
    - **Critical **: 2건 (해결됨)
    - **Major **: 0건
    - **Medium **: 4건 (해결됨)
    - **Minor **: 1건 (해결됨)
    - **Informational **: 14건 (해결됨)
- Audit Report
[Carl_AuditReport_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8a6d9fc5-5a10-48ec-86d2-efa2ee945d2e/Carl_AuditReport_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQWSATVT%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T062920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0QoNXY0VMVRk707T38ujhflDHuDq6%2BNvQlp20FDz6OwIgVGdI0TLr6jdL48EuxRJrYZsyjchJpJxSZfcIeF7VNX0q%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDMmegIuw0uZhV2FwQSrcA54g4rwqpegJxgxVemfVF%2FsYaGsj5Vwy5YjC9UXzDWiqQElgKoBUzXIAHNGMGlz4hLPrZHQyL0r3ohFcnzT0YDi1mkKMXs6Vy9dta6hPfwnyn0Z7qyzNOsEaP5Oe%2FoitzmWKjpUKWf3obGbOQKHtuvlB3Diz90uxu54dLqp8Cm30bCOZjBbFfAzuuLDnzKKvEla4m2nl%2FxppStFjlecC1%2B6HgTZxbsJfjJ1qbVMCKYQB7wiUOy8nq5ETOIxay6dJJlWQ4cfLF7xRA802Y1PbSwOrRqBXDM8tuf2jTnyf2hA%2BEjLCeG%2B1Gmtls5cdvzCmvlVWrTog%2FpII9JKcJXyHUUWSTRMYOICt1b2DRYBp0to1k%2B7e3paVOcPE8ok7zhJ0Tp6Iq%2BKot58LDueNmC2ymqz8V8h23tlsW5iztMvq5OjpUAKfkdS3fzxuqneow5Q9yNQpgg5FVES78Ad0KN06kfnL1epMj3thZTjuzS6zl5Mq4P9HozfZ9nlCqmLRqsO%2FtDcndiSjbWXnie%2BXOsEDWEeS258ODlatBjA4PLXj4FN2RQXeXHuZG4UsHHlA545N7O9IxzwzrgUoiWiIr%2BtlLKFM0BzxRUCQJR7V%2BSTmasMBbMrTJQTGdAo6QE%2FoMPrE2swGOqUBE8JVwPh9SqQBXmNyATsgCcYQAeBfFLj1cC%2BNTCpyy7waucpLnMy81f4QYi%2FS0CXL1jtsopHo0CeOUtGqkBOYCEB5A37kKCYX%2FWzw%2BcO5EmWnU976s%2FUxZ30edHQtiaEmN1hAtokYmNqBLRbCqxs5%2BL36XjT0Q5r5NhV%2Bh3uBZj4JJxuZthqGVeubo32wEXfor4CtPN0FZ0%2BTcn8uetlxpc6Z8VZz&X-Amz-Signature=6cb0175859cd1cd5c5fe1166765b642f58b57f1995ee3197b5184727c6404d03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 4. Omniscia

- Link : [Homepage](https://omniscia.io/), [x](https://x.com/Omniscia_sec/status/1889721009311195529), [linkedin](https://www.linkedin.com/feed/update/urn:li:activity:7295486669867171840)
- Audit 기간 : 2025년 1월 31일 ~ 2025년 2월 26일
- 발견된 이슈 (Contract scope범위내에서)
  - 총 발견 이슈: 21건 (Minor이상만 측정)
  - 이슈 등급별 분포:
    - Major : 3건 (해결)
    - Medium : 10건 (해결)
    - Minor : 8건 (해결)
  - **Omniscia의 경우 issue에 대한 최종 해결은 Hammer님께서 진행해주셨습니다.**
- Audit Result
  - Issue #75~Issue #222 on [ton-stalking-v2 repo](https://github.com/tokamak-network/ton-staking-v2/issues?q=is%3Aissue%20state%3Aclosed)

## 주요한 해결 내용

DAO 

- 구조변경시 메모리 불일치.
- retire … 
  - 어떤문제였는데, 어떻게 패치했다. .
  - 관련 오딧 이슈 : 
    - Hammer…: 링크걸기..
    - Carl TH1 
    - Certik : EDSD is

이번 DAO 업그레이드와 Audit을 통해 위에서 언급한 주요 부분들이 크게 개선되었습니다. Audit을 거치며 변경된 사항들은 각 감사 보고서에서 상세히 확인하실 수 있으며, 이번 DAO 업그레이드를 통해 어떤 점들이 달라졌는지 궁금하신 분들은 아래 링크를 참고해 주시기 바랍니다.

Staking V2

- 시뇨리지 분배로직 오류 
  - 시뇨리지가 언제 안맞는데ㅔ
  - 관련 오딧 이슈
    - Certik
    - Hammer… 
    - Carl.. 
    - Omniscia.. 

# 마치며

Tokamak Network의 ECO팀은 CertiK, Hammer, Carl, 그리고 Omniscia의 헌신적인 노력과 깊이 있는 통찰에 진심으로 감사드립니다. 이번 감사 과정을 통해 TONStakingV2의 보안과 안정성이 한층 더 견고해졌으며, 확인된 모든 중요 및 심각 이슈는 신속하게 해결되었습니다. 또한, 경미한 문제들에 대해서도 세심하게 대응하거나 권고를 충실히 이행하여, 전반적인 시스템 신뢰성을 더욱 높였습니다.

이처럼 체계적이고 포괄적인 감사 절차는 Tokamak Network가 커뮤니티와 Layer2 파트너에게 안전하고 신뢰할 수 있는 플랫폼을 제공하겠다는 확고한 의지를 보여줍니다. 이번 성공적인 Audit를 바탕으로, DAO의 승인을 기다리는 동안 2025년 2분기로 예정된 TONStakingV2 메인넷 업그레이드 역시 더욱 자신감 있게 준비할 수 있게 되었습니다.

Tokamak Network는 앞으로도 투명성과 보안, 그리고 커뮤니티 신뢰를 최우선 가치로 삼아, 지속적으로 기술적 완성도를 높여가겠습니다.

##  

여기까지

---

**Tokamak Network's TON Staking V2 Undergoes Rigorous Audits, Addressing Identified Issues**

**Seoul, South Korea – April 16, 2025** – As Tokamak Network prepares for the launch of TON Staking V2, the ECO team is committed to ensuring the security and reliability of the upgraded system. We are pleased to announce the successful completion of comprehensive security audits conducted by four reputable blockchain security firms: **CertiK, Hammer, Carl, and Omniscia.**

These audits were crucial in thoroughly reviewing the smart contracts underpinning the TON Staking V2 upgrade, which introduces the innovative seigniorage distribution mechanism to incentivize Layer 2 sequencers and enhance the Tokamak ecosystem.

**Audit Scope and Methodology:**

The audits focused on the codebase located in the `v2.5-audit-request` branch of the `tokamak-network/ton-staking-v2` repository, specifically examining the contracts listed below (with the latest commit hash: `01e198130b178757dd194bd8726a1ab678fca167`):

- `DAOCommitteeProxy2.sol`
- `DAOCommittee_V1.sol`
- `DAOCommitteeOwner.sol`
- `SeigManagerV1_3.sol`
- `DepositManagerV1_1.sol`
- `L1BridgeRegistryV1_1.sol`
- `Layer2ManagerV1_1.sol`
- `OperatorManagerV1_1.sol`
- `CandidateAddOnV1_1.sol`

Each audit company conducted an independent review within their respective timeframes, meticulously analyzing the code for potential vulnerabilities, bugs, and areas for improvement.

**Key Audit Findings and Resolutions:**

The collective efforts of the four audit firms identified a total of **66 issues** across various severity levels. We are pleased to report that the ECO team has diligently addressed these findings, demonstrating our commitment to a secure and robust TON Staking V2 platform.

Here's a breakdown of the discovered issues and their resolution status by each audit company:

**1. CertiK (Audit Period: January 31, 2025 ~ April 1, 2025)**

- **Total Discovered Issues:** 15
- **Distribution by Issue Level:**
  - Critical: 0
  - Major: 1 (**Resolved**)
  - Medium: 3 (**Resolved**)
  - Minor: 6 (4 **Resolved**, 2 Acknowledged)
  - Informational: 4 (**Resolved**)
  - Audit Report : title….
  - Publish the …. link : 

**2. Hammer (Audit Period: February 5, 2025 ~ March 13, 2025)**

- **Total Discovered Issues:** 9
- **Distribution by Issue Level:**
  - **CRITICAL**: 2 (**Resolved**)
  - **HIGH**: 1 (**Resolved**)
  - **MEDIUM**: 0
  - **LOW**: 6 (**Resolved**)
  - Audit Report : title….

**3. Carl (Audit Period: February 3, 2025 ~ March 5, 2025)**

- **Total Discovered Issues:** 21
- **Distribution by Issue Level:**
  - **Critical**: 2 (**Resolved**)
  - **Major**: 0
  - **Medium**: 4 (**Resolved**)
  - **Minor**: 1 (**Resolved**)
  - **Informational**: 14 (**Resolved**)
  - Audit Report : title….

**4. Omniscia (Audit Period: January 31, 2025 ~ February 26, 2025)**

- **Total Discovered Issues (Minor and above):** 21
- **Distribution by Issue Level:**
  - Major: 3 (**Resolved**)
  - Medium: 10 (**Resolved**)
  - Minor: 8 (**Resolved**)
  - 홍보글: link  
  - Audit Result : Issue #75~Issue #222 on ton-stalking-v2 repo
    - The final resolution check for issues identified by Omniscia was performed by Hammer, further ensuring the thoroughness of the remediation process.

**Resolve the Majors**

DAO 

- 구조변경시 메모리 불일치.
- retire … 
  - 어떤문제였는데, 어떻게 패치했다. .
  - 관련 오딧 이슈 : 
    - Hammer…: 링크걸기..
    - Carl TH1 
    - Certik : EDSD is

Staking V2

- 시뇨리지 분배로직 오류 
  - 시뇨리지가 언제 안맞는데ㅔ
  - 관련 오딧 이슈
    - Certik
    - Hammer… 
    - Carl.. 
    - Omniscia.. 

**Commitment to Security:**

The ECO team extends its sincere gratitude to CertiK, Hammer, Carl, and Omniscia for their diligent work and valuable insights. The findings from these audits have been instrumental in strengthening the security and reliability of TON Staking V2. All critical and major issues identified have been resolved, and the team has taken appropriate action on other findings, including resolving or acknowledging minor issues and implementing informational recommendations.

This comprehensive audit process underscores Tokamak Network's unwavering commitment to providing a secure and trustworthy platform for our community and Layer 2 partners. With these successful audits, we are moving forward with greater confidence towards the mainnet upgrade of TON Staking V2, slated for Q2 2025, pending DAO approval.

We encourage the community to review the audit reports (links to be provided in a follow-up announcement) for a more detailed understanding of the findings and resolutions.

**Stay tuned for further updates on the progress of TON Staking V2!**

**[Link to Official Tokamak Network Channels - e.g., Website, Telegram, Discord, Twitter]**

**###**

## FOR IMMEDIATE RELEASE

**Tokamak Network Announces TON Staking V2 Contract Audit Results: High Security Standards Achieved**

**Seoul, South Korea – April 16, 2025** – Tokamak Network is pleased to announce the successful completion of comprehensive security audits for the upcoming TON Staking V2 upgrade. In our commitment to transparency and security, we engaged four leading blockchain audit firms – **CertiK, Hammer, Carl, and Omniscia** – to rigorously review the smart contracts that will power the enhanced staking mechanism.

These audits focused on the codebase within the `v2.5-audit-request` branch of the `tokamak-network/ton-staking-v2` repository (commit hash: `01e198130b178757dd194bd8726a1ab678fca167`). The scope of the audit included the following key contracts:

- `DAOCommitteeProxy2.sol`
- `DAOCommittee_V1.sol`
- `DAOCommitteeOwner.sol`
- `SeigManagerV1_3.sol`
- `DepositManagerV1_1.sol`
- `L1BridgeRegistryV1_1.sol`
- `Layer2ManagerV1_1.sol`
- `OperatorManagerV1_1.sol`
- `CandidateAddOnV1_1.sol`

**Robust Audit Process and Findings:**

Each audit firm conducted an independent and thorough review, spanning different periods between January and April 2025. Their expert analysis identified a total of **66 issues** across all severity levels.

Here's a summary of the audit results from each company:

- **CertiK (January 31, 2025 ~ April 1, 2025):** Identified 15 issues, including 1 Major, 3 Medium, 6 Minor, and 4 Informational. All Major, Medium, and Informational issues have been **Resolved**, with 4 Minor issues also **Resolved** and 2 Minor issues **Acknowledged**.
- **Hammer (February 5, 2025 ~ March 13, 2025):** Discovered 9 issues, including 2 **CRITICAL**, 1 **HIGH**, and 6 **LOW**. All identified issues across all severity levels have been **Resolved**. Notably, Hammer also performed the final resolution check for Omniscia's findings.
- **Carl (February 3, 2025 ~ March 5, 2025):** Found 21 issues, including 2 **Critical**, 4 Medium, 1 Minor, and 14 Informational. All **Critical**, Medium, Minor, and Informational issues have been **Resolved**.
- **Omniscia (January 31, 2025 ~ February 26, 2025):** **Reported** 21 issues (Minor and above), including 3 Major, 10 Medium, and 8 Minor. 
  - Hammer   All these identified issues have been **Resolved**, with the final verification conducted by Hammer.

**Commitment to Security and Next Steps:**

The ECO team is highly satisfied with the outcomes of these comprehensive audits. The identification and subsequent resolution of all critical and high-severity issues, along with the thorough attention given to medium, minor, and informational findings, demonstrate our strong commitment to the security and integrity of the TON Staking V2 upgrade.

We extend our sincere appreciation to CertiK, Hammer, Carl, and Omniscia for their professionalism and expertise in ensuring the robustness of our smart contracts.

With these successful audit results, Tokamak Network is on track for the mainnet upgrade of TON Staking V2, which is currently scheduled for Q2 2025, contingent upon the successful passage of the relevant DAO agenda.

The community will be provided with links to the full audit reports in a subsequent announcement for complete transparency and detailed review.

**Tokamak Network remains dedicated to building a secure, scalable, and thriving ecosystem.**

**[Link to Official Tokamak Network Channels - e.g., Website, Telegram, Discord, Twitter]**

**###**