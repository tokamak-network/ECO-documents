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
[CertiK-AuditReport.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ae67a68e-e1ee-41c4-87bf-9fd6fc960feb/CertiK-AuditReport.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DFEBGIZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T110421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAdb7xdSZXkJ08EnUzzP26f96nvtnuMhi%2FhqqLO4l4kAIgKFWSZaudejFzEbwUm3bEEhqDGMti9MNO92t3XpimauQq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDEVn8eG1NvuA8mmW1yrcA19DjydYg%2FgWrWIbX4gAD%2BplqHn1kYuP7M1uBDSRzFLxL1f7VvnE7wNegLyt4jL2L5N23OUSMYxv2Icfbf70mOW3KsvV8CwOYLRveK7S1e%2FprQdNvyodS%2Fx4guzFYZ5C%2BerhoC4Lu8rguDuVV8QLB03ZvG4Vba8HuJ5ftaXUEzHh4LCEDqmIla8gy77glqrDTsYroQLgmsoP6r1RJF6VZjoOW9qDYuZktIOqkIw%2BHy4u4e%2FLKuHf9P1JE48o2HiG5iS6qwmOTx1iyoMgOKneYlfYt48vE%2BdD%2BYKbnhf%2BkfF0rbXIUYRZSEBrBFrwO6AthPVK%2BBds4VNWWdpwAVGBFXi2Iboi0PkgL1thJ9GGrdnP%2BDVyTiE1nCDxYn2%2Ft76yDUXPO%2BjHAz2LinnupIDnyHVLd8C0gN1TG3AlqKmu3mQle2WMkhx2V2PDOb%2BCWEgxBA%2FKIh4%2F0a0k6dbcVEWB60mIpKPE4OcvP2hk%2FfX3REE%2BJJq4U3o4Tto1eziUHqlJTRLQpnp75HoAAic2%2B2mM7zf0fOYjkofqWiv64%2FxNUthN6DjNzVhaOG9sYcgczgD88WTvppLFzMXzvWTQFh5kEBTdHkQpOrB81MkB8mrOqfFknhbHLQQgOQ1QDp8WMKPM28wGOqUBBOR5aJT9C%2FUnTf1%2BcDXg5blWP%2FYMEMPUk6NReGLIwaGyIOKox%2Fos%2B2tHw7TYuM45%2BawmANkF%2Fkh6rve9Fdg9CP8ui77jrDqMsnv8MXo8KoZp2RQI3avyx5AymXgOyR8FJPF0TwGHV4vkmxXHNSblJcnmgY78TUVDGtUc8WXVbOL2EkmIjrxHK0aindADtYb4XzZJ95gxrT%2BszkdsLAW01B9oFCxF&X-Amz-Signature=91a376ecad145ed055536504301a307729f35db6096bb9a36c15bae47c3796d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
[Hammer_AuditReport_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0b913e35-e37e-49d7-9fba-45fa01c1774e/Hammer_AuditReport_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2FDIVYK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T110422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1EWzVV5%2F19qgsNMq2LwGDQt%2FqtfnWZsj5WuNzebxrUQIhAL%2FcK1JDe%2BNezJoAsdVd2tOEBmhFdXe%2BvryezVLxd91SKv8DCHwQABoMNjM3NDIzMTgzODA1Igz%2FiBwY8yfMA1WtSjsq3AOcHi6X48z1h9%2BfDpFJIDmG9za9ElmhoMI5QXWtU3ZDPPwYmWljdpIpKe%2B%2FwV8ssO0rxqL5lryDIEB4XDE9y%2FP6EZV%2BmfM8pRG%2FtweNGDZzVeLDwkg4Op%2B%2BLBw2cADjjSZARlrovRKH4neAGV4YQdwsZdSn8rGr2xaoVmd5SjR4nghobEl%2F9lKmMP1dz12faKoKfHbxMBkU8ytlHNS6X%2BDVn44g6S19K0y56sD7S8%2FT4xSNCc%2BrfIqkiCpI330sK7vj7yWtC%2FPAyTd8nALK12VAaclfdbjyCTfPeWL3nhVUmO1aZRjRgt%2F5%2FODnE4MFJzEONFfhmlUK43BBQaPuby6Yidm423iO%2FY5KJthvCZb4Bk6L0CHX4Nrpco9fhVZuW8O1Uj1jmKdgjM2w6YrT54voMZlhH3H%2FImkc6pSpBs4vKAx8AKCmtEdc4Mt6FnTD6B2MB4bLoeUE9Lt%2F7kvVmKJX9Zjsz7JFtWIeIej2CstxLjg1Y5dtdsjDmwW7lhCM1Eup8VDCdYLtUu2N2bFro5to5Wo89xw1mZeIJ9Ic9VgkDI0FyS2jyygs1cOP7ZT76aKDHtldSyM9tLiO%2BQpMINqtdOHVKma3gi3a2s%2FNPDhM0RXRUgpf7J59vvuo1TDZzNvMBjqkASmLmuT7zt5HgmhXpPJYQkKlkkZb0VA1Aqaeq1SPJaFr5IFULP%2FjUudRh1ZALFLUoa%2BtQrN2Spvnc%2Bsll5ylr3uG8uO%2FoYnBpWMc3SOIjtZsAw07FEO5600eD3v79qzY8DzRu9ydPgn%2BHgxFh5WMiPw4%2BOrLfW4E8XJF01Dx84qvkFsgQNaXqEFruihNOQ9DDnrCfFHD2yKnH8O8IGjHkQlkQosz&X-Amz-Signature=287241b91c47a8918f8d25b8090a77c868185057503d73009d3a2885d975dde8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
[Carl_AuditReport_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8a6d9fc5-5a10-48ec-86d2-efa2ee945d2e/Carl_AuditReport_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB3TOGIF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T110425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDl0DcYvc8yb2mpawLAto8Bdp137O%2FaPzlqXFKHtCf07gIhAP4f%2FuW%2BBYkaw%2Bs1UwzgHhurVdnsFuLcmaYENyyQqIGOKv8DCHwQABoMNjM3NDIzMTgzODA1Igw3WY9KCp2f%2FjL5r0Qq3AOLYrEPoe8n%2BWrJyDzp6YJaEuNz%2Bas411FkKNR16Q4w27d%2FAeLDT9%2BV2MHBnty6fJ6qjwb2PlgnQaRuuv9QRhVbab7hzENcQJ%2B%2BgrgF90DA8ZJl%2B89%2BQWOI8GR8kmOVCOMeoQeUeLLOnHgqqbcNIoQ%2FvHVDRD05zDCojfxtbRqr1dLgbojDdNsMz5xepaTwQD6ts%2Byj9vNTnP06eIwkRpUEG6Lc0sM5aUIf9t9NkenQTCv5a5qcBxLOvGuibbMf8bfM%2B28JrPsdlnNRiHjmnS7ul0tiVSq%2FEpPhiEmXaEzYBYVciSCJ6AAK%2BxyybxbSRWMUYyizJNdKbZFTGzESI7SUT0RfnPr1s9jSQtXXvls1Wop6o5V4FCaZOvnIm8i8T8ruJCW%2BGmenZmYIthC%2BqdhuXPhZfFpksHsZq1QgINiSD%2Bm8oEtrZRqbE1oaO%2B6OKuSegD3DCjbs%2F2ju%2FWsbi%2B0%2Bp4CQMN1LsSl%2B7sicm9HVLvX10wTuz168HG712rAxjE3gjIy5mUsUBlgAILqUABwam3BODB3NIkda02S3uT8ShS8i1NB8f4YmQZ%2Fb0925L8vt%2B6ekVrA9OTZjKhvzViog6B0n%2B%2B3moLp7nQPxxKteyOKbj7AmZ7ZEyRG0OTCuzNvMBjqkAcAdpjafsYwyUzJ7hJIADG%2FW2mBkCYSFDXnjTbtAHthFox2q1VYbAfglV9DmAPd%2BvlKuORemQlbB8vUADtd7M65fjVhMa86%2FRPSsSgXouh%2FgNyozkD8Tw0epO8XcESYfTxLCVsf3QKGPSOFJUGqM7UaC8NRNDeYWRrUM%2Fj4oOTV1U3Pe3jTxMce8xD28ueghST4rpR6%2B7wPO5W1A64x9G5JLCMnv&X-Amz-Signature=58ebd0690f655a8d310b054a00640e08c92e3e66292a3c16c9209168b80e94cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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