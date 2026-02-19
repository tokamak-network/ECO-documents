DAO Agenda proposal link : [https://dao.tokamak.network/#/agenda/15](https://dao.tokamak.network/#/agenda/15)

## **📝 DAO Contract Upgrade for DAO Lifecycle Enhancement and Bug Fixes**

## **Summary**

Tokamak Network Foundation proposes a DAO contract upgrade to support the future TIP (Tokamak Improvement Proposal) lifecycle and fix critical bugs affecting DAO functionality.

## **Motivation**

Tokamak DAO plans to introduce the **TIP Lifecycle** to provide a more systematic governance process and better community engagement. This upgrade addresses two critical areas:

1. **TIP Lifecycle Support**: Adding memo fields to support on-chain voting processes
1. **Critical Bug Fixes**: Resolving currentAgendaStatus function and CandidateAddOnProxy storage configuration issues

## **Specification**

**1. Memo Field Addition for TIP Lifecycle Support**

**Role of Memo Field:**

- **Community Discussion Links**: Store links to preliminary community discussion processes for proposals
- **Temperature Check Links**: Store Snapshot Temperature Check voting links
- **Reference Materials**: Store additional document links that provide background and rationale for proposals
- **Enhanced Transparency**: Enable full traceability of the proposal process

**Specific Implementation:**

- **Recommended inclusion of Temperature Check Snapshot links** in memo field when creating on-chain agendas
- Utilize as reference materials to assist **member voting decisions**
- Optional inclusion of community discussion links and other reference materials
- Enable complete proposal history tracking through step-by-step links

**2. Bug Fixes**

**A. currentAgendaStatus Function Bug**

- **Issue**: Function does not display accurate agenda status
- **Impact**: Incorrect status reporting affecting governance decisions
- **Fix**: Correct logic to properly reflect current agenda status

**B. CandidateAddOnFactoryProxy Storage Configuration Bug**

- **Issue**: Memory configuration mismatch between CandidateAddOnFactoryProxy and CandidateAddOnFactory (logic contract)
- **Impact**: Registered CandidateAddOnFactory contracts cannot become DAO members, blocking critical functions:
  - changeMember: Cannot become DAO member
  - retireMember: Cannot withdraw from DAO
  - castVote: Cannot participate in voting
  - claimActivityReward: Cannot claim rewards
- **Fix**: Align memory configuration between proxy and logic contracts

## **Implementation Details**

### **Smart Contract Changes**

- Addition of memo field to support TIP lifecycle
- Modification of CandidateAddOnFactory storage layout
- Correction of currentAgendaStatus function logic
- Implementation
  - DAOCommittee_V2:
    - [onApprove(address owner, address, uint256, bytes calldata data)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L421-L465)
    - [_decodeAgendaData(bytes calldata input)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L642-L657)
    - [_createAgenda(address _creator, address[] memory _targets, uint128 _noticePeriodSeconds, uint128 _votingPeriodSeconds, bool _atomicExecute, bytes[] memory _functionBytecodes, string memory _memo)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L723-L768)
    - [currentAgendaStatus(uint256 _agendaID)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L517-L570)
  - [CandidateAddOnProxy](https://github.com/tokamak-network/ton-staking-v2/blob/d88709b1ac62c13caf88492e04dba11a54feb3c3/contracts/dao/CandidateAddOnProxy.sol#L12):
    - Storage changed from [CandidateStorage](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/CandidateStorage.sol) to [CandidateAddOnStorage1](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/CandidateAddOnStorage1.sol)
    - Upgraded CandidateAddOnFactoryProxy to new implementation (CandidateAddOnFactory) via upgradeTo(address).

### **Benefits**

- **Systematic Governance**: Complete technical support for TIP lifecycle
- **Full Transparency**: Complete traceability from preliminary discussions to final execution
- **Enhanced Community Participation**: Support for staged discussion and voting processes
- **Critical Bug Fixes**: Restoration of DAO member functionality for CandidateAddOn contracts

### **Risk Factors & Mitigation**

- **Upgrade Risk**: Thorough testing completed through internal audit
- **Backward Compatibility**: Maintained compatibility with existing agenda processes
- **Storage Layout**: Careful verification to prevent additional storage conflicts

### **References**

- **DAO Upgraded Internal Audit**: Internal Audit Documentation
- **CandidateAddOnFactory Bug**: [GitHub Issue #304](https://github.com/tokamak-network/ton-staking-v2/issues/304#issuecomment-2826891830)

### **Timeline**

- **Development**: Completed
- **Internal Audit**: Completed
- **DAO Proposal**: Current Stage
- **Implementation**: After DAO Approval

---

This upgrade prepares to support the future TIP Lifecycle, establishing systematic and transparent governance for Tokamak DAO while addressing critical bugs in the current system.

### Copyright

Copyright and related rights waived via [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

## **📝 DAO 라이프사이클 개선 및 버그 수정을 위한 DAO 컨트랙트 업그레이드**

## **요약**

토카막 네트워크 재단은 미래에 TIP(Tokamak Improvement Proposal) 라이프사이클을 지원하고, DAO 기능에 영향을 미치는 중요한 버그를 수정하기 위해 DAO 컨트랙트 업그레이드를 제안합니다.

## **동기**

토카막 DAO는 더욱 체계적인 거버넌스 프로세스와 더 나은 커뮤니티 참여를 제공하기 위해 **TIP 라이프사이클**을 도입할 예정입니다. 이번 업그레이드는 두 가지 중요한 영역을 다룹니다:

1. **TIP 라이프사이클 지원**: 온체인 투표 프로세스를 지원하기 위한 메모 필드 추가
1. **중요한 버그 수정**: currentAgendaStatus 함수 및 CandidateAddOnProxy 스토리지 구성 문제 해결

## **명세**

**1. TIP 라이프사이클 지원을 위한 메모 필드 추가**

**메모 필드의 역할:**

- **커뮤니티 토론 링크**: 제안에 대한 사전 커뮤니티 토론 과정 링크 저장
- **Temperature Check 링크**: Snapshot에서 진행된 Temperature Check 투표 링크 저장
- **참고 자료**: 제안의 배경 및 근거가 되는 추가 문서 링크 저장
- **투명성 향상**: 제안의 전체 과정을 추적 가능하게 함

**구체적 구현:**

- 온체인 아젠다 생성 시 메모 필드에 **Temperature Check Snapshot 링크 포함 권장**
- **멤버들의 투표 판단**에 도움을 주는 참고 자료로 활용
- 커뮤니티 토론 링크 및 기타 참고 자료 선택적 포함
- 각 단계별 링크를 통한 제안 이력 완전 추적 가능

**2. 버그 수정**

**A. currentAgendaStatus 함수 버그**

- **문제**: 함수가 정확한 아젠다 상태를 표시하지 않음
- **영향**: 거버넌스 결정에 영향을 미치는 잘못된 상태 보고
- **수정**: 현재 아젠다 상태를 올바르게 반영하도록 로직 수정

**B. CandidateAddOnFactoryProxy 스토리지 구성 버그**

- **문제**: CandidateAddOnFactoryProxy와 CandidateAddOnFactory(로직 컨트랙트) 간 메모리 구성 불일치
- **영향**: 등록된 CandidateAddOnFactory 컨트랙트가 DAO 멤버가 될 수 없어 중요한 기능들이 차단됨:
  - changeMember: DAO 멤버가 될 수 없음
  - retireMember: DAO에서 탈퇴할 수 없음
  - castVote: 투표에 참여할 수 없음
  - claimActivityReward: 보상을 청구할 수 없음
- **수정**: 프록시와 로직 컨트랙트 간 메모리 구성 정렬

## **구현 세부사항**

### **스마트 컨트랙트 변경사항**

- TIP 라이프사이클 지원을 위한 메모 필드 추가
- CandidateAddOnFactory 스토리지 레이아웃 수정
- currentAgendaStatus 함수 로직 수정
- 구현
  - DAOCommittee_V2:
    - [onApprove(address owner, address, uint256, bytes calldata data)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L421-L465)
    - [_decodeAgendaData(bytes calldata input)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L642-L657)
    - [_createAgenda(address _creator, address[] memory _targets, uint128 _noticePeriodSeconds, uint128 _votingPeriodSeconds, bool _atomicExecute, bytes[] memory _functionBytecodes, string memory _memo)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L723-L768)
    - [currentAgendaStatus(uint256 _agendaID)](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol#L517-L570)
  - [CandidateAddOnProxy](https://github.com/tokamak-network/ton-staking-v2/blob/d88709b1ac62c13caf88492e04dba11a54feb3c3/contracts/dao/CandidateAddOnProxy.sol#L12): 
    - Storage changed from [CandidateStorage](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/CandidateStorage.sol) to [CandidateAddOnStorage1](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/CandidateAddOnStorage1.sol) 
    - Upgraded CandidateAddOnFactoryProxy to new implementation (CandidateAddOnFactory) via upgradeTo(address).

### **이점**

- **체계적인 거버넌스**: TIP 라이프사이클의 완전한 기술적 지원
- **완전한 투명성**: 사전 토론부터 최종 실행까지 모든 단계 추적 가능
- **커뮤니티 참여 증진**: 단계적 토론 및 투표 과정 지원
- **중요한 버그 수정**: CandidateAddOn 컨트랙트의 DAO 멤버 기능 복원

### **위험 요소 및 완화 방안**

- **업그레이드 위험**: 내부 감사를 통한 철저한 테스트 완료
- **하위 호환성**: 기존 아젠다 프로세스와의 호환성 유지
- **스토리지 레이아웃**: 추가 스토리지 충돌 방지를 위한 신중한 검증

### **참고 자료**

- **DAO 업그레이드 내부 감사**: [Internal Audit Documentation](/206d96a400a380479c48e7a943e0febe)
- **CandidateAddOnFactory 버그**: [GitHub Issue #304](https://github.com/tokamak-network/ton-staking-v2/issues/304#issuecomment-2826891830)

### **일정**

- **개발**: 완료
- **내부 감사**: 완료
- **DAO 제안**: 현재 단계 
- **구현**: DAO 승인 후

---

**이번 업그레이드는 미래에 TIP 라이프사이클을 지원할 준비를 하여 토카막 DAO의 체계적이고 투명한 거버넌스를 실현하는 동시에, 현재 시스템의 중요한 버그를 수정합니다.**

### Copyright

Copyright and related rights waived via [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

---

## **📝 DAO 라이프사이클 개선 및 버그 수정을 위한 DAO 컨트랙트 업그레이드**

### **요약**

토카막 네트워크 재단은 TIP(Tokamak Improvement Proposal) 라이프사이클을 지원하고, DAO 기능에 영향을 미치는 중요한 버그를 수정하기 위해 DAO 컨트랙트 업그레이드를 제안합니다.

### **동기**

토카막 DAO는 더욱 체계적인 거버넌스 프로세스와 더 나은 커뮤니티 참여를 제공하기 위해 **TIP 라이프사이클**을 도입했습니다. 이번 업그레이드는 두 가지 중요한 영역을 다룹니다:

1. **TIP 라이프사이클 지원**: 커뮤니티 토론 → Temperature Check → 온체인 투표 프로세스를 지원하기 위한 메모 필드 추가
1. **중요한 버그 수정**: currentAgendaStatus 함수 및 CandidateAddOnProxy 스토리지 구성 문제 해결


**명세**

**1. TIP 라이프사이클 지원을 위한 메모 필드 추가**

**메모 필드의 역할:**

- **커뮤니티 토론 링크**: 제안에 대한 사전 커뮤니티 토론 과정 링크 저장
- **Temperature Check 링크**: Snapshot에서 진행된 Temperature Check 투표 링크 저장
- **참고 자료**: 제안의 배경 및 근거가 되는 추가 문서 링크 저장
- **투명성 향상**: 제안의 전체 진화 과정을 추적 가능하게 함

**구체적 구현:**

- 온체인 아젠다 생성 시 메모 필드에 **Temperature Check Snapshot 링크 포함 권장**
- **멤버들의 투표 판단**에 도움을 주는 참고 자료로 활용
- 커뮤니티 토론 링크 및 기타 참고 자료 선택적 포함
- 각 단계별 링크를 통한 제안 이력 완전 추적 가능

**2. 버그 수정**

**A. currentAgendaStatus 함수 버그**

- **문제**: 함수가 정확한 아젠다 상태를 표시하지 않음
- **영향**: 거버넌스 결정에 영향을 미치는 잘못된 상태 보고
- **수정**: 현재 아젠다 상태를 올바르게 반영하도록 로직 수정

**B. CandidateAddOnProxy 스토리지 구성 버그**

- **문제**: CandidateAddOnProxy와 CandidateAddOn(로직 컨트랙트) 간 메모리 구성 불일치
- **영향**: 등록된 CandidateAddOn 컨트랙트가 DAO 멤버가 될 수 없어 중요한 기능들이 차단됨:
  - changeMember: DAO 멤버가 될 수 없음
  - retireMember: DAO에서 탈퇴할 수 없음
  - castVote: 투표에 참여할 수 없음
  - claimActivityReward: 보상을 청구할 수 없음
- **수정**: 프록시와 로직 컨트랙트 간 메모리 구성 정렬

**구현 세부사항**

### **스마트 컨트랙트 변경사항**

- TIP 라이프사이클 지원을 위한 메모 필드 추가
- CandidateAddOnProxy 스토리지 레이아웃 수정
- currentAgendaStatus 함수 로직 수정

### **이점**

- **체계적인 거버넌스**: TIP 라이프사이클의 완전한 기술적 지원
- **완전한 투명성**: 사전 토론부터 최종 실행까지 모든 단계 추적 가능
- **커뮤니티 참여 증진**: 단계적 토론 및 투표 과정 지원
- **중요한 버그 수정**: CandidateAddOn 컨트랙트의 DAO 멤버 기능 복원

### **위험 요소 및 완화 방안**

- **업그레이드 위험**: 내부 감사를 통한 철저한 테스트 완료
- **하위 호환성**: 기존 아젠다 프로세스와의 호환성 유지
- **스토리지 레이아웃**: 추가 스토리지 충돌 방지를 위한 신중한 검증

### **참고 자료**

- **DAO 업그레이드 내부 감사**: [Internal Audit Documentation](/206d96a400a380479c48e7a943e0febe)
- **CandidateAddOnProxy 버그**: [GitHub Issue #304](https://github.com/tokamak-network/ton-staking-v2/issues/304#issuecomment-2826891830)

### **일정**

- **개발**: 완료
- **내부 감사**: 완료
- **DAO 제안**: 현재 단계 (TIP 라이프사이클 적용)
- **구현**: DAO 승인 후

---

**이번 업그레이드는 TIP 라이프사이클을 완전히 지원하여 토카막 DAO의 체계적이고 투명한 거버넌스를 실현하는 동시에, 현재 시스템의 중요한 버그를 수정합니다.**

오늘 아젠다 제출 화이팅하세요! 🚀

— 

## **📝 DAO Contract Upgrade for Lifecycle Enhancement and Bug Fixes**

**Summary**

Tokamak Network Foundation proposes to upgrade the DAO Contract to support TIP (Tokamak Improvement Proposal) lifecycle and fix critical bugs affecting DAO functionality.

**Motivation**

Tokamak DAO has introduced the **TIP lifecycle** to provide more structured governance processes and better community participation. This upgrade addresses two critical areas:

1. **TIP Lifecycle Support**: Addition of memo field to support Community Discussion → Temperature Check → On-chain Vote process
1. **Critical Bug Fixes**: Resolution of currentAgendaStatus function and CandidateAddOnProxy storage configuration issues

**Specification**

**1. Memo Field Addition for TIP Lifecycle Support**

**Role of Memo Field:**

- **Community Discussion Links**: Store links to preliminary community discussion processes for proposals
- **Temperature Check Links**: Store Snapshot Temperature Check voting links
- **Reference Materials**: Store additional documentation links that provide background and rationale for proposals
- **Enhanced Transparency**: Enable complete tracking of proposal evolution process

**Specific Implementation:**

- **Recommended inclusion** of Temperature Check Snapshot links in memo field when creating on-chain agendas
- Serve as **reference materials to assist members' voting decisions**
- Optional inclusion of community discussion links and other reference materials
- Enable complete proposal history tracking through step-by-step links

**2. Bug Fixes**

**A. currentAgendaStatus Function Bug**

- **Issue**: Function does not display accurate agenda status
- **Impact**: Incorrect status reporting affecting governance decisions
- **Fix**: Correct logic to properly reflect current agenda states

**B. CandidateAddOnProxy Storage Configuration Bug**

- **Issue**: Memory configuration mismatch between CandidateAddOnProxy and CandidateAddOn (logic contract)
- **Impact**: Registered CandidateAddOn contracts cannot become DAO members, blocking critical functions:
  - changeMember: Cannot become DAO member
  - retireMember: Cannot retire from DAO
  - castVote: Cannot participate in voting
  - claimActivityReward: Cannot claim rewards
- **Fix**: Align memory configuration between proxy and logic contracts

**Implementation Details**

### **Smart Contract Changes**

- Addition of memo field to support TIP lifecycle
- CandidateAddOnProxy storage layout correction
- currentAgendaStatus function logic fix

### **Benefits**

- **Systematic Governance**: Complete technical support for TIP lifecycle
- **Complete Transparency**: Full tracking from preliminary discussions to final execution
- **Enhanced Community Participation**: Support for step-by-step discussion and voting processes
- **Critical Bug Fixes**: Restoration of DAO member functionality for CandidateAddOn contracts

### **Risks and Mitigation**

- **Upgrade Risk**: Thoroughly tested through internal audit
- **Backward Compatibility**: Maintained compatibility with existing agenda processes
- **Storage Layout**: Carefully verified to prevent additional storage conflicts

### **References**

- **DAO Upgrade Internal Audit**: Internal Audit Documentation
- **CandidateAddOnProxy Bug**: GitHub Issue #304

### **Timeline**

- **Development**: Completed
- **Internal Audit**: Completed
- **DAO Proposal**: Current phase (TIP lifecycle applied)
- **Implementation**: Upon DAO approval

---

**This upgrade fully supports the TIP lifecycle to realize systematic and transparent governance for Tokamak DAO while fixing critical bugs in the current system.**

** **

— 

# upgradeTo DAOCommittee_V2 + CandidateAddOnFactory

## Simple Summary

토카막 네트워크 재단은 추후 있을 Tokamak DAO의 Lifecycle변화와 currentAgendaStatus view함수에서 발견된 버그 수정을 위해서 DAO Contract를 업그레이드하며 Agenda #14에서 업그레이드된 TON Staking V2에서 CandidateAddOnFactory에서 L2 Candidate를 등록할때 발생하는 버그를 발견하여서 이를 수정하고 이번 아젠다를 통해서 적용할려고 합니다.

아래 내용은 어떤가요? 

토카막 네트워크 재단은 다음 두 가지 주요 업데이트를 위해 DAO Contract 및 CandidateAddOnProxy를 업그레이드합니다:

1. **Tokamak DAO Lifecycle 개선**: 새로운 RFC 및 Temperature Check 단계 지원
1. **버그 수정**: currentAgendaStatus view 함수 및  CandidateAddOnProxy 버그 수정
  - **Tokamak DAO Lifecycle 개선**: 새로운 RFC 및 Temperature Check 단계 지원
  - **버그 수정**: currentAgendaStatus view 함수 및 CandidateAddOnProxy 버그 수정

## **DAO Snapshot 업그레이드 및 **currentAgendaStatus함수** 버그 수정**

### **배경 및 목적**

Tokamak DAO는 제안을 체계적으로 다루고, 커뮤니티가 적극적으로 참여할 수 있도록 Tokamak DAO의 Lifecycle에서 DAO Agenda 생성 전 RFC와 Temperature Check 단계가 추가되었습니다. 이 중 Temperature Check 단계는 Snapshot에서 진행되는데, 해당 Snapshot을 진행한 링크를 DAO Agenda를 병용때 입력하여서 Agenda의 배경을 확인할 수 있도록 하기 위해서 DAO Agenda를 생성 시 Snapshot 링크를 추가할 수 있도록 Agenda Memo 필드를 추가하는 업그레이드 합니다.
그리고 현재의 Agenda의 정확한 상태를 보기 위해서 만들어진 view함수인 currentAgendaStatus함수에서 Agenda의 상태를 제대로 보여주지 않는 버그를 발견하여서 해당 버그를 수정하였습니다.

아래 내용은 어떤가요? 

## **DAO Snapshot 업그레이드 및 currentAgendaStatus 함수 버그 수정**

### **배경 및 목적**

1. **DAO Lifecycle 개선**
  - Tokamak DAO에 RFC(Request for Comments)와 Temperature Check 단계가 새롭게 추가되었습니다
  - Temperature Check는 Snapshot에서 진행되며, 해당 링크를 DAO Agenda 생성 시 참조할 수 있어야 합니다
  - 이를 위해 Agenda에 **Memo 필드를 추가**하여 Snapshot 링크를 포함할 수 있도록 업그레이드합니다
1. **버그 수정**
  - **currentAgendaStatus 함수**: 현재 Agenda 상태를 정확히 표시하지 않는 버그를 수정합니다
  - **(**[**issue 304**](https://github.com/tokamak-network/ton-staking-v2/issues/304#issuecomment-2826891830)**) **CandidateAddOnProxy** 메모리 구성 불일치**: CandidateAddOnProxy와 CandidateAddOn(logic) 간 메모리 구성이 달라서 등록된 CandidateAddOn이 DAO 멤버가 될 수 없는 심각한 버그를 수정합니다
    - 이로 인해 changeMember, retireMember, castVote, claimActivityReward 등의 핵심 DAO 기능들이 작동하지 않았습니다

이번 업그레이드를 통해 DAO의 투명성과 참여도를 높이고,  정상적인 DAO 참여를 보장하여 시스템의 안정성을 개선합니다.

이번 업그레이드를 통해 DAO의 투명성과 참여도를 높이고,  정상적인 DAO 참여를 보장하여 시스템의 안정성을 개선하고 발견된 버그를 수정합니다.

### **주요 변경 사항**

1. **DAO Lifecycle 개선 관련**
**함수 변경:**

  - **onApprove**: Memo값을 decode해서 createAgenda에 정보 넘겨줌
  - **_decodeAgendaData**: Memo값도 decode하도록 변경
  - **_createAgenda**: input으로 Memo값을 받으며 storage에 AgendaID에 대한 Memo값 저장 과정 추가

**Storage 추가:**

  - DAO Contract에서 AgendaID에 대한 Memo값을 확인할 수 있도록 agendaMemo라는 mapping storage 추가
1. **버그 수정 관련 **
**함수 변경:**

  - **currentAgendaStatus**: Agenda 다양한 상태에 대한 값들을 추가

**컨트랙 재 배포 및 로직 변경** 

  - CandidateAddOnProxy 컨트랙 재배포 후, 

## **CandidateAddOnFactory 버그 리포트 및 수정**

### **버그 설명:**

CandidateAddOnFactoryProxy와 CandidateAddOnFactory(로직)의 메모리 구성이 달라, 스토리지를 정상적으로 가져올 수 없는 현상이 발생했습니다.

### **영향 범위**

등록한 CandidateAddOn(Layer2로 등록한 Candidate)이 DAO 멤버가 될 수 없으며, 아래 함수들을 호출할 수 없습니다:

- **changeMember**: DAO 멤버가 되기 위한 함수 호출 불가
- **retireMember**: 멤버가 될 수 없으므로, 함수 호출 불가
- **castVote**: 멤버가 될 수 없으므로, 함수 호출 불가
- **claimActivityReward**: 멤버가 될 수 없으므로, 함수 호출 불가

### **수정 방안**

CandidateAddOnFactoryProxy의 메모리를 CandidateAddOnFactory(로직)의 메모리와 같게 하여 스토리지 공유 문제를 해결합니다.

## 온체인 효과

1. DAO Contract upgrade
  1. DAOCommitee_V2 upgrade ([link](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/DAOCommittee_V2.sol)) : Upgrade DAOCommitte logic from V1 to V2.
1. CandidateAddOnFactory Contract upgrade
  1. CandidateAddOnFactory upgrade ([link](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-candidateAndDAO/contracts/dao/factory/CandidateAddOnFactory.sol)) : Upgrade CandidateAddOnFactory logic to a bug-fixed version.

## Copyright

Copyright and related rights waived via [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

## **📝 DAO 라이프사이클 개선 및 버그 수정을 위한 DAO 컨트랙트 업그레이드**

**요약**

토카막 네트워크 재단은 향상된 DAO 라이프사이클 프로세스를 지원하고 DAO 기능에 영향을 미치는 중요한 버그를 수정하기 위해 DAO 컨트랙트 업그레이드를 제안합니다.

**동기**

토카막 DAO는 더욱 체계적인 거버넌스 프로세스와 더 나은 커뮤니티 참여를 제공하기 위해 발전하고 있습니다. 이번 업그레이드는 두 가지 중요한 영역을 다룹니다:

1. **향상된 DAO 라이프사이클**: RFC(Request for Comments) 및 Temperature Check 단계 통합
1. **중요한 버그 수정**: currentAgendaStatus 함수 및 CandidateAddOnProxy 스토리지 구성 문제 해결

1. 1. **향상된 DAO 라이프사이클**: RFC(Request for Comments) 및 Temperature Check 단계 통합
1. 1. **중요한 버그 수정**: currentAgendaStatus 함수 및 CandidateAddOnProxy 스토리지 구성 문제 해결

**명세**

### **1. DAO 라이프사이클 개선**

- **RFC 단계 통합**: 아젠다 생성 전 Request for Comments 단계 지원
- **Temperature Check 단계**: 커뮤니티 의견 수렴을 위한 Snapshot 통합
- **메모 필드 추가**: Snapshot 링크 및 참고 자료 저장을 위한 아젠다 생성 시 새 필드
- **향상된 투명성**: RFC → Temperature Check → 정식 아젠다로의 제안 진화 과정 추적 개선

**2. 버그 수정**

**A. currentAgendaStatus 함수 버그**

- **문제**: 함수가 정확한 아젠다 상태를 표시하지 않음
- **영향**: 거버넌스 결정에 영향을 미치는 잘못된 상태 보고
- **수정**: 현재 아젠다 상태를 올바르게 반영하도록 로직 수정

**B. CandidateAddOnProxy 스토리지 구성 버그**

- **문제**: CandidateAddOnProxy와 CandidateAddOn(로직 컨트랙트) 간 메모리 구성 불일치
- **영향**: 등록된 CandidateAddOn 컨트랙트가 DAO 멤버가 될 수 없어 중요한 기능들이 차단됨:
- changeMember: DAO 멤버가 될 수 없음
- retireMember: DAO에서 탈퇴할 수 없음
- castVote: 투표에 참여할 수 없음
- claimActivityReward: 보상을 청구할 수 없음
- **수정**: 프록시와 로직 컨트랙트 간 메모리 구성 정렬

**구현 세부사항**

### **스마트 컨트랙트 변경사항**

- 메모 필드 지원을 위한 DAO 컨트랙트 업그레이드
- CandidateAddOnProxy 스토리지 레이아웃 수정
- currentAgendaStatus 함수 로직 수정

**프로세스 플로우 개선textApply to example-agen...RFC 단계 → Temperature Check (Snapshot) → 정식 아젠다 생성                                            ↓                                      메모 필드에                                      Snapshot 참조 저장**

### **이점**

- **개선된 거버넌스**: 체계적인 제안 진화 프로세스
- **향상된 투명성**: RFC부터 최종 아젠다까지 명확한 추적
- **중요한 버그 수정**: CandidateAddOn 컨트랙트의 DAO 멤버 기능 복원
- **더 나은 커뮤니티 참여**: Temperature Check를 위한 Snapshot 통합

### **위험 요소 및 완화 방안**

- **업그레이드 위험**: 내부 감사를 통한 철저한 테스트 완료
- **하위 호환성**: 기존 아젠다 프로세스와의 호환성 유지
- **스토리지 레이아웃**: 추가 스토리지 충돌 방지를 위한 신중한 검증

### **참고 자료**

- **DAO 라이프사이클 개선**: 내부 감사 문서
- **CandidateAddOnProxy 버그**: GitHub Issue #304
- **테스트 결과**: 내부 감사 성공적으로 완료

### **일정**

- **개발**: 완료
- **내부 감사**: 완료
- **DAO 제안**: 현재 단계
- **구현**: DAO 승인 후