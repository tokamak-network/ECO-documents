# **Tokamak Improvement Proposal (TIP) Lifecycle**

Tokamak DAO는 제안을 체계적으로 다루고, 커뮤니티가 적극적으로 참여할 수 있도록 **Tokamak Improvement Proposal(TIP) 라이프사이클**을 운영합니다. 이 문서는 TIP이 어떤 과정을 거쳐 최종 결정되고 실행되는지, 각 단계에서 어떤 역할과 절차가 필요한지를 상세히 설명합니다.

# **1. 개요 (Overview)**

 TIP은 Tokamak 생태계를 개선하기 위한 공식 제안 문서로, 기술 업그레이드, 정책 변경, 재정 운영 등 다양한 영역의 변화를 포함합니다. 제안이 최초 아이디어로 제시된 후, 커뮤니티 토론과 투표를 거쳐 실행되기까지 네 가지 핵심 단계를 밟습니다. 먼저, 초안 성격의 제안은 **RFC(Request for Comment)**를 통해 커뮤니티의 의견을 수렴하고, 다음으로 **Temperature Check(Temp Check)** 단계에서 오프체인 투표(예, Snapshot)를 통해 제안에 대한 지지 여부를 확인합니다. 이 과정을 통과한 제안은 **On-chain Vote** 단계에서 온체인 투표를 거쳐 최종 결정되며, 긴급 상황 발생 시에는 **Security Council**이 거버넌스 과정을 일부 단축하거나 사후 승인 절차를 진행할 수 있습니다. 이러한 구조는 제안에 대해 충분한 토론이 이루어진 후 실행함으로써, 불필요한 가스비 낭비와 의사결정 지연을 최소화하는 데 목적이 있습니다.

 Tokamak DAO에서는 다양한 아이디어와 피드백이 나오지만, 이를 공식적인 제안으로 발전시킬 틀이 없다면 실행으로 이어지기 어렵습니다. TIP 제도는 이러한 아이디어를 하나의 문서로 구체화하여 **명확한 형식과 절차**에 따라 검토하도록 합니다. 이를 통해 모든 이해 관계자가 제안을 쉽게 이해하고 토론에 참여할 수 있으며, **의사결정 과정의 투명성**을 확보할 수 있습니다. 또한, TIP 제도를 도입하면 제안자가 **사전에 충분한 검토와 커뮤니티 합의를 이끌어낸 후** 투표에 부칠 수 있으므로, **실행력 있고 실효성 있는 제안**만이 채택될 가능성이 높아집니다.

# **2. TIP의 구성 (Anatomy of a TIP)**


Tokamak Improvement Proposal은 보통 다음과 같은 항목들로 구성됩니다. 상황에 따라 추가 문단을 삽입할 수 있습니다. TIP 작성은 Discord 내 전용 채널(예: `#💡｜proposal-rfc`)에서 RFC 형태로 이루어집니다. 아래는 TIP 작성 시 포함해야 할 주요 요소입니다.

## 1. 필수 요소

1. **제목 및 작성자**: 
제안의 간략한 제목과 작성자(또는 팀)의 이름을 명시합니다. 필요 시 Tokamak DAO의 제안 번호나 태그를 함께 기재합니다. 예를 들어 “**TIP-1: 거버넌스 보상 구조 개선**”과 같이 작성합니다.
1. **요약 (Summary)**: 
제안의 핵심 내용을 두세 문장으로 요약합니다. 무엇을 제안하는지 간략히 설명하여 한눈에 파악할 수 있도록 합니다.
1. **배경 및 동기 (Background & Motivation)**: 
제안을 하게 된 배경, 문제 인식, 그리고 개선이 필요한 이유를 상세히 서술합니다. 현재 상황에서 어떤 문제가 존재하며, 이 제안이 Tokamak 생태계에 어떤 가치를 가져올지 설명합니다.
1. **세부 제안 내용 (Proposal Details / Execution Plan):** 
제안을 구현하거나 실행할 구체적인 계획을 단계별로 기술합니다. 스마트 컨트랙트 코드 변경이 필요한 경우, 어떤 코드를 어떻게 수정하거나 추가할지 명시하며, 필요 시 타 프로젝트의 유사 사례를 참고하여 설명합니다**.
**세부내용으로는 코드의 스펙, 이전버전과의 호환성, 코드의 수정 및 추가 내용 등을 기술합니다.
1. **예상 효과 및 영향 (Expected Impact):** 
제안이 실행되었을 때 예상되는 결과와 효과를 서술합니다. 긍정적인 영향(예: 프로토콜 성능 향상, 거버넌스 참여 증가)과 잠재적인 부작용 또는 리스크도 함께 고려합니다.

## 2. 보조 요소

1. **실행 계획 (Implementation Plan)**: 
 제안의 기술적 구현, 필요한 스마트 컨트랙트 변경, 개발 일정, 관련 자원 등을 간략히 설명합니다.
1. **추가 자료 및 참고문선:**
제안의 타당성을 뒷받침할 외부 자료, 유사 사례, 기술 명세서 등
1. **투표 및 다음 단계 (Next Steps)**: 
RFC 논의가 종료된 후, 제안자가 Temp Check 투표로 진행할 시기나 조건 등을 명시합니다.

필요에 따라 추가 정보를 제공할 수도 있습니다. 예를 들어, 제안이 기술적 변경을 포함한다면 상세 **기술 명세서**나 **보안 고려 사항**을 부록으로 포함할 수 있고, 예산 집행을 제안할 경우 **예산 내역**과 **자금 사용 계획**을 명확히 명시해야 합니다. 일관된 템플릿을 따름으로써 모든 TIP는 유사한 구조를 가지게 되고, 커뮤니티는 핵심 내용을 빠르게 파악하여 효과적으로 토론할 수 있습니다.


추가 정보가 필요한 경우, 예를 들어 제안이 기술적 변경을 포함한다면 상세 **기술 명세서**나 **보안 고려 사항**을 부록에 첨부할 수 있고, 예산 집행 제안의 경우 **예산 내역**과 **자금 사용 계획**을 포함합니다. 일관된 템플릿을 사용함으로써 모든 TIP는 통일된 구조를 갖게 되어 커뮤니티가 쉽게 내용을 이해하고 검토할 수 있습니다.

만약 초기 제출된 TIP가 승인되지 않는다면, 제안자는 커뮤니티의 피드백을 반영하여 수정한 후 안건을 재상정할 수 있습니다. 이때 아래와 같은 내용들이 포함되어야 합니다.

- 원본 TIP로의 링크
- **TIP가 왜 승인되지 않았는지에 대한 설명 **
- **자세한 개선 사항 **
- **보충정보 **

# **3. TIP Lifecycle 단계별 설명**


Tokamak DAO에서 TIP의 승인 절차는 **여러 단계의 거버넌스 프로세스**로 구성되며, 각 단계마다 역할과 진행 방식이 명확히 정의되어 있습니다. 전체 흐름은 **아이디어 논의 (RFC) → 임시 투표 (Temperature Check) → 온체인 투표 → 결과 집행**으로 이루어집니다.

## **3.1. RFC(Request for Comment)**

*Timeframe*: At least 7 days

Where:  Discord (전용 채널: `#💡｜proposal-rfc`)

### **개요**

RFC 단계는 제안자가 자신의 아이디어를 Discord 전용 채널에 “RFC: [제안 제목]” 형식으로 게시하여, 커뮤니티의 자유 토론과 피드백을 받는 비공식 단계입니다. 커뮤니티 구성원들은 댓글이나 별도 스레드(Thread)를 통해 질문, 찬반 의견, 개선 제안을 자유롭게 제시할 수 있습니다. 이 과정을 통해 제안 내용이 다각도로 검토되며, 제안자는 이를 반영하여 TIP 초안을 보완합니다.

**주요 구현 방안:**

- **Discord 전용 채널 및 스레드 관리:**
모든 RFC는 Discord 내 전용 채널에서 별도의 스레드로 생성되어 진행됩니다. 채널 상단에는 “RFC 작성 체크리스트”가 고정되어 있어, 제안자는 [제목], [요약], [배경 및 동기], [세부 제안 내용], [예상 효과] 등의 필수 항목을 반드시 포함해야 합니다.
- **봇 알림 기능:**
새 RFC가 게시되면, 디스코드 봇이 이를 자동으로 감지하여 #announcements 채널 또는 특정 역할(@RFC-Notify)로 알림을 전송합니다. 이를 통해 커뮤니티 전체가 새로운 제안을 즉시 인지할 수 있습니다.
- **논의 기간 및 피드백 반영:**
최소 [7일]의 논의 기간을 두어 충분한 피드백을 수렴합니다. 제안자는 논의 과정 중 제기된 의견을 반영하여 초안을 수정하고, 필요시 중간 요약을 스레드 상단에 고정(Pin)하여 업데이트합니다.

**효과:**

 이 단계는 제안이 충분히 숙성되고, 커뮤니티의 합의를 이끌어내며, 불필요한 오해를 줄이는 데 도움을 줍니다. 또한, Discord 기반의 접근 방식은 사용자들이 익숙한 환경에서 쉽게 참여할 수 있도록 하여 거버넌스 참여율을 높입니다.

## **3.2. Temperature Check(Temp Check)**

**Timeframe: **[5일]

**조건: **최소 [0.01%]의 TON 참여, 정족수: [1%] 이상

Where: Snapshot

### **개요**

RFC 단계를 통과한 제안은 커뮤니티의 지지 여부를 정량적으로 파악하기 위해 Snapshot을 사용한 Temp Check 투표에 부쳐집니다. 이 단계에서는 제안 요약 및 투표 옵션(예: 찬성/반대)이 포함된 투표가 생성됩니다. 투표 생성은 일정 TON 보유(또는 위임 요건)를 충족한 계정만 할 수 있습니다.

**주요 구현 방안:**

- **투표 생성:**
제안자는 Temp Check 투표를 Snapshot에 생성하며, Discord RFC 게시물의 링크를 함께 첨부해 투표자들이 제안 내용을 쉽게 확인할 수 있도록 합니다.
- **투표 기간 및 결과 기준:**
Temp Check 투표는 [5일] 동안 진행됩니다. 투표 결과는 전체 발행량의 [1%] 이상의 참여와, 단순 다수(>50%)의 찬성표를 기준으로 평가됩니다. 만약 투표 결과에서 찬성 의견이 충분치 않거나, 참여가 저조할 경우 제안은 온체인 투표 단계로 넘어가지 않고 재논의(또는 폐기)됩니다.
- **효과:**
이 단계는 오프체인에서 비용 부담 없이 커뮤니티의 지지를 측정할 수 있어, 실행 가능한 제안만 온체인 투표로 이관할 수 있도록 도와줍니다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/99e9710c-0e90-451e-b2f3-4241352e5a61/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PY2QKMB%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDiD8p19FX4RsJ8uOsOViiRXTzXLyVeqjEFsVXvq050QAiEAmYZIst0Eunrese1WHXDjw3OXBmeLuGrh%2FRS3Jn3ULBwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDCic1oQ0cNV44OWAdircA7DmUeH7i%2Bgjr1pvYs%2FM%2Fac0olqaoydLFTH5CU4t%2FZvGoPs5fRwzRDrxjWb8YoePZga8NVBnPcsCcI1T%2FM6KlLJZ7PJTKbGyjx3HWHK2NSv8BoYkGsBVlfYGxiczLOq6cxZ1lf6FzSKxTrXwdhH%2Bzzw1XtGpQxtreTul5PTEzvkRRgVaS%2FmThWgeywRUBjkAkGkm7sYh%2B2OR84A0%2Fd8TUW45qFweqHbF6q0qafv1atu62ApmXAd%2Fy4d1N8hG2vSWEG1x8jtTVxFotlo5m72m8uD0VE55m%2BGk%2ByCAJnYrRkQbChzATyYDx9P%2B20KDvMuEbMP%2BEP4WwuyHnHIjR%2BcnRe457%2BaI9np7E7reZ27k%2Fp5uB2IFjTAc5l270miOF7iYSBLZtIGBkoEiNtFtcILesGICHZjWaQzoMffn2S%2FcXL3a6ZZGrgdzSxE2O%2BL%2FNtspfp8QeXg5hEXSRF2dBtL6TDD7CZ1kObaYts1aS%2FSb2lgQH7DpAC5cIvf5BNLRdqSO8dwpklrnCwxryMaHnclkmre4aCo%2FtzYAjrC1lyKGvADYOle1oT73yQDmbhSeXtzufBvS8rXzZMTgwNDZmZU5ZYymdumctRBYHCWPcZSl%2FAZpP7yoJPgPTfF2Sg%2B1MMzw2cwGOqUBro%2Fp1V6SsmeTtISkj%2BbVmwJRb2icPsEyyzb0b5OyVj6uDfuU%2BvYyFQeCLoBEHx5fe2soGz27gCphAl%2F7Q5bLthh1kMnLJEnKuU07UyQCxrenB5OZHSWMxx7IIlzX3V2%2FkUcNu%2BfDqquob0vH%2FH601z807AFecHa9s%2B9pvmtdWYLjlkmyAgFNrpUE0jM1Wpa808qun3T9%2F9yVZm0f8Vhcgsjcwpmx&X-Amz-Signature=bcfaf0e0978833dd90c5fc0083a333ff7359775a8b032907cd2e1f8b437d173e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## **3.3. On-chain Vote**

**Timeframe: **[최소 투표 알림 기간 : 16일] + [최소 투표 기간: 2일]

**Where: **Tokamak DAO 

Temp Check를 통과한 제안은 이제 공식적인 온체인 투표로 넘어갑니다. 제안자는 온체인 거버넌스 컨트랙트를 통해 제안을 등록하며, 이때 일정 TON 보유(또는 위임) 요건([예: 최소 20,000 TON])을 만족해야 합니다.

**주요 구현 방안:**

- **제안 등록:**
온체인 제안을 등록할 때, 제안 내용은 Temp Check 단계의 내용과 동일해야 하며, 필요 시 RFC 및 Temp Check에서의 피드백을 반영해 수정된 내용을 포함하고 Temp Check를 진행했던 링크를 같이 제안에 같이 등록합니다. 
- **투표 지연 및 투표 기간:**
제안 등록 후, [16일]의 투표 알림 기간을 두어 토큰 홀더들이 위임이나 스테이킹 상태를 조정할 수 있도록 합니다. 이후, [2일] 동안 온체인 투표가 진행되며, 모든 Member들은 투표에 참여합니다.
- **가결 조건:**
온체인 투표는 미리 정해진 정족수와 과반수 이상 찬성 조건을 만족해야 합니다. 예를 들어, 멤버들 중 과반수이상이 투표에 참여하고, 그 중 [50% 초과]의 찬성이 있어야 합니다.  투표 종료 후, 최종 검토를 거친 후 제안이 실행됩니다.

 

Temp Check를 통과한 제안은 “On-chain Vote”로 옮겨지며, 이 단계에서 최종적으로 DAO 프로토콜이나 자금이 변경될 수 있습니다. *보통 제안자가 DAO의 온체인 투표 dApp 또는 직접 구현한 투표 인터페이스에 제안 내용을 업로드**하*고, 투표 알림 기간(Notice Delay)과 투표 기간(Voting Period)를 설정합니다. 여기서 [최소 투표 알림 기간](https://etherscan.io/address/0xcD4421d082752f363E1687544a09d5112cD4f484#readContract#F20)은 16일이고 [최소 투표 기간](https://etherscan.io/address/0xcD4421d082752f363E1687544a09d5112cD4f484#readContract#F21)은 2일입니다. 이때 제안은 누구나 올릴 수 있으며 제안을 만드는 수수료로 [10TON](https://etherscan.io/address/0xcD4421d082752f363E1687544a09d5112cD4f484#readContract#F4) 필요하며, 제안 내용은 Snapshot 단계의 것과 동일해야 합니다 (단, RFC/Snapshot에서의 피드백을 반영하여 수정된 내용이어야 함). 투표 알림 기간은 제안이 올라온 것을 알려주는 기간이며, 투표 기간에는 Candidate Contract들 중 Member로 선별된 Candidate Contract만 투표권을 가지게 됩니다. 
먼저 Candidate의 역할을 하기 위해서는 Candidate 생성자가 자신의 Candidate에 최소한 1000.1TON 이상을 Staking하여야 합니다. 그 이후 Candidate의 역할을 할 수 있고 Member보다 Staking된 TON의 양이 많으면 해당 Member에게 Challange하여서 Member가 될 수 있습니다. Candidate가 아닌 일반 유저들은 Candidate들에게 Staking하여서 자신의 투표권을 위임하게 되고 따로 투표에 참여하지는 않습니다.
온체인 투표가 시작되면, 투표권을 가진 Member는 스마트 컨트랙트를 통해 찬성 또는 반대, 기권 투표를 행사할 수 있습니다. 투표 기간은 보통 2~3일로 설정되지만, Tokamak DAO의 거버넌스 규정에 따라 변경될 수 있습니다. 이 기간 동안 커뮤니티는 Discord 및 기타 채널에서 추가 토론을 이어갈 수 있으며, **투표 독려 캠페인**이나 **보충 설명 AMA** 등이 진행될 수도 있습니다. 

온체인 투표가 완료되어 가결 조건(현재 기준 : 총 Member 3명 중 2명이상 찬성에 투표)을 충족 했다면 실행(Execution)이 이루어집니다. 실행 기간은 [7일](https://etherscan.io/address/0xcD4421d082752f363E1687544a09d5112cD4f484#readContract#F5)로 누구나 실행가능하지만 7일기간 동안 아무도 실행하지 않으면 해당 제안은 더 이상 실행되지 않습니다. 이 실행 과정에서 스마트 컨트랙트 상의 함수가 자동으로 호출되어 파라미터 변경, 자금 이체, 컨트랙트 업그레이드 등이 적용될 수 있습니다. 



## **3.4. Security Council 및 긴급 대응(TBD)**


표준 TIP 프로세스 외에, Tokamak DAO는 긴급 상황에 대비하여 **Security Council**을 마련합니다. Security Council은 멀티시그(Multi-signature) 방식으로 운영되어, 예를 들어 2/3 이상의 서명이 모여야만 긴급 상황에서 제안을 중단하거나 변경할 수 있습니다. 이 기능은 해킹이나 치명적 버그 등 긴급 사안에만 적용되며, 평상시에는 커뮤니티의 온체인 투표 결과가 그대로 반영됩니다. Security Council의 거부권은 매우 제한적으로 사용되며, 행사 시 반드시 투명하게 커뮤니티에 보고됩니다.

# 4. 거버넌스 품질 관리 및 남용 방지

Tokamak DAO는 거버넌스 절차의 남용을 막고 제안의 품질을 유지하기 위해 다음과 같은 조치를 취합니다:

- **제안 상정 요건 강화:**
Snapshot Temp Check 투표를 생성하기 위해 최소 [1,000 TON] 이상의 투표권을 요구하여 무분별한 제안 상정을 방지합니다.
- **중복 제안 방지:**
제안 제출 전 기존 제안 아카이브를 확인하도록 하며, 동일하거나 유사한 내용의 제안은 [최소 한 달]의 쿨다운 기간을 적용하여 재 상정을 제한합니다.
- **절차 준수 및 피드백 반영:**
모든 제안은 정해진 템플릿과 절차를 준수해야 하며,  운영진은 RFC 단계에서 충분한 토론이 이루어졌는지 확인하고 미흡한 경우 보완을 요청합니다.

# 5. FAQ

**Q1) RFC 없이 바로 Temp Check나 온체인 투표로 갈 수 있나요?**

A1) 일반적인 경우, 충분한 토론과 커뮤니티 피드백을 위해 RFC 단계를 반드시 거칩니다. 다만, 긴급한 사안에서는 Security Council이 예외적으로 허용할 수 있습니다.

**Q2) Temp Check에서 부결된 제안도 재제출이 가능한가요?**

A2) 부결 사유가 명확해지고 제안 내용이 크게 수정된 경우, 재제출이 가능합니다. 단, 동일하거나 유사한 제안은 중복 방지를 위해 제한될 수 있습니다.

**Q3) 온체인 투표는 반드시 투표 알림 기간을 거쳐야 하나요? 그렇다면 너무 길지않나요?**

A3) 투표 알림 기간은 모든 Tokamak 커뮤니티 유저분들이 제안에 대해서 알리기 위해서 필요한 기간입니다. 하지만 최소 16일이란 기간은 RFC와 Temp Check가 생기기전의 기간이여서 해당 기간은 추후 변경가능합니다.

# 6. 결론

Tokamak DAO의 TIP 라이프사이클은 RFC, Temp Check, 온체인 투표, 실행의 4단계로 구성되어 있습니다. 이 프로세스는 커뮤니티가 자유롭게 의견을 나누고, 충분한 피드백을 바탕으로 최종 결정을 내리게 하여, 거버넌스의 투명성과 신뢰성을 높입니다. 특히, Discord를 통한 RFC 전용 채널 운영과 개별 스레드 관리는 제안의 명확성과 효율성을 극대화하며, Staked TON을 기반으로 한 Temp Check는 실제 네트워크의 장기적 참여를 보장합니다. Security Council은 긴급 상황에 한해 개입할 수 있도록 설계되어 있으나, 평상시에는 전체 커뮤니티의 의사가 최종 결정을 내리도록 합니다.

Tokamak DAO 구성원들은 이 문서에 따라 제안을 작성, 논의, 투표, 실행함으로써, 네트워크의 미래를 함께 결정하는 데 적극적으로 참여할 수 있습니다. 이러한 TIP 라이프사이클은 Tokamak 생태계의 지속 가능한 발전과 혁신을 위한 핵심 메커니즘입니다