# vTON DAO 거버넌스 업그레이드 가이드

> Tokamak Network DAO를 vTON 기반 거버넌스 모델로 업그레이드하기 위한 개발자 가이드

---

## 목차

1. 개요
1. 아키텍처 변경 요약
1. 컨트랙트 구조 다이어그램
1. 신규 컨트랙트 상세
1. 기존 컨트랙트 수정 사항
1. 구현 순서
1. 배포 체크리스트

---

## 1. 개요

### 1.1 업그레이드 목적

| 현재 | 변경 후 |
| --- | --- |
| Member만 투표 가능 | Delegator도 투표 가능 |
| 스테이킹 기반 투표권 | vTON 토큰 기반 투표권 |
| 3단계 투표 프로세스 | 6단계 투표 프로세스 |
| Security Council 없음 | 2/3 멀티시그 Security Council |

### 1.2 핵심 원칙

```
✅ Solidity 0.7.6 유지 (기존 호환성)
✅ 점진적 마이그레이션 (프록시 패턴 활용)
✅ 기존 Member 시스템 영구 유지 (공존)
```

---

## 2. 아키텍처 변경 요약

### 2.1 변경 유형별 컨트랙트

```
┌─────────────────────────────────────────────────────────────────┐
│                        변경 유형별 분류                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🔴 신규 컨트랙트 (6개)                                          │
│  ├── vTON.sol                 거버넌스 토큰                      │
│  ├── DelegationManager.sol    위임 관리                          │
│  ├── SecurityCouncil.sol      긴급 대응 멀티시그                  │
│  ├── SnapshotManager.sol      투표권 스냅샷                       │
│  ├── DAOCommitteeV2.sol       새 Implementation                  │
│  └── DAOAgendaManagerV2.sol   6단계 투표 프로세스                 │
│                                                                  │
│  🔵 수정 컨트랙트 (3개)                                          │
│  ├── StorageStateCommittee.sol   V2 상태 변수 추가               │
│  ├── DAOVault.sol                vTON 분배 기능 추가             │
│  └── Agenda.sol (lib)            V2 상태 enum 추가               │
│                                                                  │
│  ⚪ 유지 컨트랙트 (4개)                                          │
│  ├── DAOCommitteeProxy.sol    프록시 (변경 없음)                 │
│  ├── DAOCommittee.sol         기존 Implementation (레거시)       │
│  ├── DAOAgendaManager.sol     기존 의제 관리 (레거시)            │
│  └── Candidate.sol            후보자 관리                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

```

### 2.2 변경 전후 비교표

| 항목 | Before | After | 비고 |
| --- | --- | --- | --- |
| 거버넌스 토큰 | ❌ 없음 | ✅ vTON | 신규 |
| 투표 주체 | Member only | Member + Delegator | 확장 |
| 위임 시스템 | ❌ 없음 | ✅ 20% 상한 | 신규 |
| 스냅샷 | ❌ 없음 | ✅ 7일 전 기준 | 신규 |
| 투표 프로세스 | 16일+2일+7일 | RFC+Snap+Review+Vote+Lock | 확장 |
| Security Council | ❌ 없음 | ✅ 3명 (2/3) | 신규 |
| Quorum | Member 50%+ | vTON 4% | 변경 |

---

## 3. 컨트랙트 구조 다이어그램

### 3.1 현재 구조

```
                    ┌─────────────────────────┐
                    │   DAOCommitteeProxy     │
                    │   (Upgradeable Proxy)   │
                    └───────────┬─────────────┘
                                │ delegatecall
                                ▼
                    ┌─────────────────────────┐
                    │     DAOCommittee        │
                    │   (Implementation)      │
                    └───────────┬─────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
    ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
    │DAOAgendaManager│   │   Candidate   │   │   DAOVault    │
    │  (의제 관리)   │   │  (후보자/멤버) │   │  (Treasury)   │
    └───────────────┘   └───────────────┘   └───────────────┘
            │                   │                   │
            ▼                   ▼                   ▼
    ┌───────────────────────────────────────────────────────┐
    │                     Member (투표자)                    │
    │                     TON/WTON (토큰)                    │
    └───────────────────────────────────────────────────────┘

```

### 3.2 새 구조 (업그레이드 후)

```
                    ┌─────────────────────────┐
                    │   DAOCommitteeProxy     │  ⚪ 유지
                    │   (Upgradeable Proxy)   │
                    └───────────┬─────────────┘
                                │ delegatecall
                                │ upgradeTo(V2)
                                ▼
                    ┌─────────────────────────┐
                    │    DAOCommitteeV2       │  🔴 신규
                    │  (New Implementation)   │
                    │  - 기존 기능 100% 유지   │
                    │  - 새 기능 추가          │
                    └───────────┬─────────────┘
                                │
    ┌───────────────┬───────────┼───────────┬───────────────┐
    │               │           │           │               │
    ▼               ▼           ▼           ▼               ▼
┌─────────┐   ┌─────────┐ ┌─────────┐ ┌─────────┐   ┌─────────┐
│Agenda   │   │AgendaV2 │ │Candidate│ │Delegat- │   │Security │
│Manager  │   │(NEW)    │ │(유지)   │ │ionMgr   │   │Council  │
│(유지)   │   │6단계    │ │         │ │(NEW)    │   │(NEW)    │
└─────────┘   └─────────┘ └─────────┘ └────┬────┘   └────┬────┘
⚪             🔴           ⚪              🔴             🔴
                                           │              │
                                           ▼              │
                                    ┌─────────────┐       │
                                    │ Snapshot    │◄──────┘
                                    │ Manager     │
                                    │ (NEW)       │
                                    └──────┬──────┘
                                           🔴
                                           │
    ┌──────────────────────────────────────┼──────────────────┐
    │                                      │                  │
    ▼                                      ▼                  ▼
┌─────────┐                         ┌─────────────┐    ┌─────────┐
│DAOVault │                         │    vTON     │    │TON/WTON │
│(수정)   │                         │   (NEW)     │    │(유지)   │
└─────────┘                         │ 거버넌스토큰 │    └─────────┘
🔵                                  └──────┬──────┘
                                           🔴
                                           │
    ┌──────────────────────────────────────┼──────────────────┐
    │                                      │                  │
    ▼                                      ▼                  ▼
┌─────────┐                         ┌─────────────┐    ┌─────────┐
│ Member  │                         │  Delegator  │    │  vTON   │
│ (유지)  │                         │   (NEW)     │    │ Holder  │
└─────────┘                         └─────────────┘    └─────────┘
⚪                                        🔴                 🔴

```

### 3.3 투표 흐름 비교

**현재 투표 흐름:**

```
Member ──► Candidate.castVote() ──► DAOCommittee.castVote() ──► AgendaManager

```

**새 투표 흐름 (2가지 경로 공존):**

```
경로 1 (기존 유지):
Member ──► Candidate.castVote() ──► DAOCommitteeV2.castVote() ──► AgendaManager

경로 2 (신규):
vTON Holder ──► DelegationManager.delegate() ──► Delegator
                        │
                        ▼ (7일 후)
Delegator ──► DAOCommitteeV2.castVoteAsDelegator() ──► AgendaManagerV2

```

---

## 4. 신규 컨트랙트 상세

### 4.1 vTON (거버넌스 토큰)

```
📁 contracts/tokens/vTON.sol

```

```solidity
/**
 * @title vTON - Tokamak Network 거버넌스 토큰
 *
 * 특성:
 * - ERC20 기반
 * - 무한 발행 (발행 비율 조정 가능: 0~100%)
 * - 소각 불가 (burn 함수 revert)
 * - 거래 가능 (transfer 허용)
 *
 * 분배 대상:
 * - L2 Operator: ✅
 * - Validator: ✅
 * - DAO Treasury: ❌
 */

interface IvTON {
    // 발행 (onlyMinter)
    function mint(address to, uint256 amount) external;

    // 발행 비율 설정 (0 ~ 1e18)
    function setMintRatio(uint256 ratio) external;

    // 현재 발행 비율 조회
    function mintRatio() external view returns (uint256);

    // 투표권 위임
    function delegate(address delegatee) external;

    // 위임받은 투표권 조회
    function getVotes(address account) external view returns (uint256);

    // 특정 블록 기준 투표권 조회 (스냅샷)
    function getPastVotes(address account, uint256 blockNumber)
        external view returns (uint256);
}

```

**핵심 구현 포인트:**

```solidity
// 소각 방지
function burn(uint256) public pure override {
    revert("vTON: burning is disabled");
}

function burnFrom(address, uint256) public pure override {
    revert("vTON: burning is disabled");
}

// 발행 비율 적용
function _mintWithRatio(address to, uint256 seigniorageAmount) internal {
    uint256 vtonAmount = seigniorageAmount * mintRatio / 1e18;
    if (vtonAmount > 0) {
        _mint(to, vtonAmount);
    }
}

```

---

### 4.2 DelegationManager (위임 관리)

```
📁 contracts/dao/DelegationManager.sol

```

```solidity
/**
 * @title DelegationManager - vTON 위임 관리
 *
 * 핵심 기능:
 * - Delegator 등록 (프로필, 투표 철학, 이해관계)
 * - 위임 상한 20% 강제
 * - 7일 위임 기간 요건
 * - 위임 자동 만료 (선택적)
 */

struct DelegatorProfile {
    string name;           // 이름/가명
    string philosophy;     // 투표 철학
    string interests;      // 이해관계 공개
    uint256 registeredAt;  // 등록 시간
    bool isActive;         // 활성화 상태
}

struct DelegationInfo {
    address delegator;     // 위임받는 사람
    uint256 amount;        // 위임량
    uint256 delegatedAt;   // 위임 시작 시간
    uint256 expiresAt;     // 만료 시간 (0=무기한)
}

```

**핵심 상수:**

```solidity
uint256 public constant DELEGATION_CAP_BPS = 2000;      // 20%
uint256 public constant DELEGATION_MATURITY = 7 days;   // 7일 요건

```

**핵심 로직:**

```solidity
// 위임 실행
function delegateTo(address delegator, uint256 amount) external {
    // 1. Delegator 등록 확인
    require(delegatorProfiles[delegator].isActive, "Not a delegator");

    // 2. 20% 상한 체크
    uint256 totalDelegated = getTotalDelegated();
    uint256 newTotal = delegatorVotes[delegator] + amount;
    require(
        newTotal * 10000 <= totalDelegated * DELEGATION_CAP_BPS,
        "Exceeds 20% cap"
    );

    // 3. vTON 잠금
    vton.transferFrom(msg.sender, address(this), amount);

    // 4. 위임 기록
    delegations[msg.sender] = DelegationInfo({
        delegator: delegator,
        amount: amount,
        delegatedAt: block.timestamp,
        expiresAt: 0
    });
}

// 유효 투표권 계산 (7일 기준)
function getValidVotingPower(address delegator, uint256 snapshotTime)
    external view returns (uint256)
{
    uint256 cutoff = snapshotTime - DELEGATION_MATURITY;
    uint256 validPower = 0;

    // 7일 이전에 위임된 것만 유효
    for (각 위임자) {
        if (delegatedAt <= cutoff && !expired) {
            validPower += amount;
        }
    }
    return validPower;
}

```

---

### 4.3 SecurityCouncil (긴급 대응)

```
📁 contracts/dao/SecurityCouncil.sol

```

```solidity
/**
 * @title SecurityCouncil - 긴급 대응 멀티시그
 *
 * 구성:
 * - 초기 멤버: 3명 (재단 1명 + 외부 2명)
 * - 임계값: 2/3 (67%)
 *
 * 권한:
 * - 악의적 제안 취소
 * - 긴급 업그레이드
 * - 프로토콜 일시정지/재개
 */

enum ProposalType {
    CANCEL_AGENDA,       // Timelock 대기 중인 제안 취소
    EMERGENCY_UPGRADE,   // 긴급 컨트랙트 업그레이드
    PAUSE_PROTOCOL,      // 프로토콜 일시정지
    UNPAUSE_PROTOCOL,    // 프로토콜 재개
    ADD_MEMBER,          // 멤버 추가 (DAO 투표 후)
    REMOVE_MEMBER        // 멤버 제거 (DAO 투표 후)
}

struct SCProposal {
    uint256 id;
    ProposalType proposalType;
    bytes data;
    uint256 approvalCount;
    bool executed;
    mapping(address => bool) hasApproved;
}

```

**핵심 로직:**

```solidity
uint256 public constant THRESHOLD_NUMERATOR = 2;
uint256 public constant THRESHOLD_DENOMINATOR = 3;

// 승인 (멤버만)
function approve(uint256 proposalId) external onlyMember {
    SCProposal storage p = proposals[proposalId];
    require(!p.hasApproved[msg.sender], "Already approved");

    p.hasApproved[msg.sender] = true;
    p.approvalCount++;

    // 2/3 도달 시 자동 실행
    if (p.approvalCount * THRESHOLD_DENOMINATOR >=
        members.length * THRESHOLD_NUMERATOR) {
        _execute(proposalId);
    }
}

```

---

### 4.4 SnapshotManager (투표권 스냅샷)

```
📁 contracts/dao/SnapshotManager.sol

```

```solidity
/**
 * @title SnapshotManager - 투표권 스냅샷 관리
 *
 * 기능:
 * - 스냅샷 생성 및 저장
 * - 특정 시점 투표권 조회
 * - Quorum 계산 (4%)
 */

struct Snapshot {
    uint256 id;
    uint256 timestamp;
    uint256 blockNumber;
    uint256 totalDelegatedVotes;
}

// Quorum = 전체 위임된 vTON의 4%
uint256 public constant QUORUM_BPS = 400;

function getQuorumAt(uint256 snapshotId) external view returns (uint256) {
    Snapshot memory s = snapshots[snapshotId];
    return s.totalDelegatedVotes * QUORUM_BPS / 10000;
}

```

---

### 4.5 DAOCommitteeV2 (새 Implementation)

```
📁 contracts/dao/DAOCommitteeV2.sol

```

```solidity
/**
 * @title DAOCommitteeV2 - 새 거버넌스 Implementation
 *
 * 변경사항:
 * - 기존 Member 투표 로직 100% 유지
 * - 새 Delegator 투표 로직 추가
 * - Security Council 통합
 * - 프로토콜 일시정지 기능
 * - vTON 분배 로직
 */

// 기존 함수 유지
function castVote(uint256 _agendaID, uint256 _vote, string calldata _comment)
    external override validAgendaManager
{
    // 기존 로직 그대로 유지
    // Member가 Candidate Contract를 통해 투표
}

// 새 함수 추가
function castVoteAsDelegator(
    uint256 _agendaID,
    uint8 _support,      // 0: Against, 1: For, 2: Abstain
    string calldata _reason
) external whenNotPaused {
    // 1. Delegator 확인
    require(
        delegationManager.isDelegator(msg.sender),
        "Not a delegator"
    );

    // 2. 중복 투표 확인
    require(!hasVotedV2[_agendaID][msg.sender], "Already voted");

    // 3. 유효 투표권 조회 (7일 전 기준)
    AgendaV2 storage agenda = agendasV2[_agendaID];
    uint256 weight = delegationManager.getValidVotingPower(
        msg.sender,
        agenda.snapshotTimestamp
    );
    require(weight > 0, "No voting power");

    // 4. 투표 기록
    hasVotedV2[_agendaID][msg.sender] = true;

    if (_support == 1) {
        agenda.forVotes += weight;
    } else if (_support == 0) {
        agenda.againstVotes += weight;
    } else {
        agenda.abstainVotes += weight;
    }
}

// V2 제안 생성 (6단계 프로세스)
function createAgendaV2(
    address[] calldata targets,
    bytes[] calldata calldatas,
    string calldata description
) external returns (uint256) {
    // 100 TON 소각
    payCreatingAgendaFee(msg.sender);

    // 스냅샷 생성
    uint256 snapshotId = snapshotManager.createSnapshot();

    // AgendaV2 생성
    return agendaManagerV2.newAgenda(...);
}

// Security Council 전용
function cancelAgenda(uint256 _agendaID) external onlySecurityCouncil {
    // Timelock 대기 중인 제안 취소
}

function pause() external onlySecurityCouncil {
    _pause();
}

function unpause() external onlySecurityCouncil {
    _unpause();
}

```

---

### 4.6 DAOAgendaManagerV2 (6단계 프로세스)

```
📁 contracts/dao/DAOAgendaManagerV2.sol

```

```solidity
/**
 * @title DAOAgendaManagerV2 - 확장된 투표 프로세스
 *
 * 6단계 프로세스:
 * RFC (7일+) → Snapshot (5일) → Review (3일) →
 * Onchain (7일) → Timelock (7일) → Execution
 */

enum AgendaPhaseV2 {
    RFC,            // 커뮤니티 의견 수렴
    SNAPSHOT,       // 오프체인 찬반 투표
    REVIEW,         // 스냅샷 준비, 위임 조정
    ONCHAIN,        // 온체인 투표
    TIMELOCK,       // Security Council 검토
    EXECUTABLE,     // 실행 가능
    EXECUTED,       // 실행 완료
    CANCELLED       // 취소됨
}

struct AgendaV2 {
    uint256 id;
    AgendaPhaseV2 phase;

    // 타임라인
    uint256 rfcEndTimestamp;
    uint256 snapshotEndTimestamp;
    uint256 reviewEndTimestamp;
    uint256 onchainEndTimestamp;
    uint256 timelockEndTimestamp;

    // 스냅샷
    uint256 snapshotId;
    uint256 snapshotTimestamp;

    // 투표 결과
    uint256 forVotes;
    uint256 againstVotes;
    uint256 abstainVotes;

    // 실행 정보
    address[] targets;
    bytes[] calldatas;
    bool executed;
}

// 기간 설정
uint256 public rfcPeriod = 7 days;
uint256 public snapshotPeriod = 5 days;
uint256 public reviewPeriod = 3 days;
uint256 public onchainPeriod = 7 days;
uint256 public timelockPeriod = 7 days;

```

**프로세스 타임라인:**

```
Day 0    Day 7    Day 12   Day 15   Day 22   Day 29   Day 29+
  │        │        │        │        │        │        │
  ├────────┼────────┼────────┼────────┼────────┼────────┤
  │  RFC   │Snapshot│ Review │Onchain │Timelock│  Exec  │
  │  7일+  │  5일   │  3일   │  7일   │  7일   │        │

```

---

## 5. 기존 컨트랙트 수정 사항

### 5.1 StorageStateCommittee.sol

**위치:** `contracts/dao/StorageStateCommittee.sol`

**추가할 상태 변수 (기존 변수 뒤에 추가):**

```solidity
// === 기존 변수 (변경 금지) ===
address public override ton;
IDAOVault public override daoVault;
IDAOAgendaManager public override agendaManager;
ICandidateFactory public override candidateFactory;
ILayer2Registry public override layer2Registry;
ISeigManager public override seigManager;
address[] public override candidates;
address[] public override members;
uint256 public override maxMember;
mapping(address => CandidateInfo) internal _candidateInfos;
uint256 public override quorum;
uint256 public override activityRewardPerSecond;

// === V2 확장 변수 (여기부터 추가) ===

// 신규 컨트랙트 참조
address public vton;
address public delegationManager;
address public securityCouncil;
address public snapshotManager;
address public agendaManagerV2;

// V2 파라미터
uint256 public vtonMintRatio;              // 발행 비율 (1e18 = 100%)
uint256 public delegationCapBps;           // 위임 상한 (2000 = 20%)
uint256 public delegationMaturitySeconds;  // 위임 기간 (604800 = 7일)
uint256 public quorumBps;                  // Quorum (400 = 4%)

// 프로토콜 상태
bool public protocolPaused;

// 미래 업그레이드를 위한 Storage Gap
uint256[40] private __gap;

```

**추가할 modifier:**

```solidity
modifier whenNotPaused() {
    require(!protocolPaused, "Protocol is paused");
    _;
}

modifier onlySecurityCouncil() {
    require(msg.sender == securityCouncil, "Not Security Council");
    _;
}

```

---

### 5.2 DAOVault.sol

**위치:** `contracts/dao/DAOVault.sol`

**추가할 함수:**

```solidity
// vTON 참조 (StorageStateCommittee에서 상속받아 사용)
// 이미 StorageStateCommittee에 vton 변수 추가됨

// vTON 분배 (onlyOwner)
function distributeVTON(address to, uint256 amount) external onlyOwner {
    require(to != address(0), "Zero address");
    require(to != address(this), "Cannot distribute to vault");

    IvTON(vton).mint(to, amount);

    emit VTONDistributed(to, amount);
}

// 이벤트 추가
event VTONDistributed(address indexed to, uint256 amount);

```

---

### 5.3 Agenda.sol (Library)

**위치:** `contracts/lib/Agenda.sol`

**추가할 enum:**

```solidity
// 기존 enum (유지)
enum AgendaStatus { NONE, NOTICE, VOTING, WAITING_EXEC, EXECUTED, ENDED }
enum AgendaResult { PENDING, ACCEPT, REJECT, DISMISS }

// V2 enum (추가)
enum AgendaPhaseV2 {
    RFC,
    SNAPSHOT,
    REVIEW,
    ONCHAIN,
    TIMELOCK,
    EXECUTABLE,
    EXECUTED,
    CANCELLED
}

```

---

## 6. 구현 순서

### Phase 1: 인프라 준비 (Week 1-2)

```
순서  작업                              의존성
────────────────────────────────────────────────────
1.1   contracts/interfaces/ 생성        없음
      - IvTON.sol
      - IDelegationManager.sol
      - ISecurityCouncil.sol
      - ISnapshotManager.sol
      - IDAOAgendaManagerV2.sol
      - IDAOCommitteeV2.sol

1.2   contracts/lib/Agenda.sol 수정     1.1
      - AgendaPhaseV2 enum 추가

1.3   contracts/tokens/vTON.sol 생성    1.1
      - ERC20 기반 거버넌스 토큰

1.4   contracts/dao/SnapshotManager.sol 1.1, 1.3
      - 투표권 스냅샷 관리

1.5   contracts/dao/DelegationManager.sol 1.1, 1.3, 1.4
      - 위임 관리 (20% 상한, 7일 요건)

1.6   contracts/dao/SecurityCouncil.sol 1.1
      - 멀티시그 (2/3)

```

### Phase 2: 핵심 업그레이드 (Week 3-4)

```
순서  작업                              의존성
────────────────────────────────────────────────────
2.1   StorageStateCommittee.sol 수정    1.1
      - V2 상태 변수 추가
      - modifier 추가

2.2   DAOVault.sol 수정                 2.1
      - vTON 분배 함수 추가

2.3   DAOAgendaManagerV2.sol 생성       1.2, 2.1
      - 6단계 투표 프로세스

2.4   DAOCommitteeV2.sol 생성           2.1, 2.2, 2.3
      - 새 Implementation
      - 기존 기능 100% 유지
      - 새 기능 추가

```

### Phase 3: 배포 (Week 5-6)

```
순서  작업                              의존성
────────────────────────────────────────────────────
3.1   Testnet 배포                      Phase 2 완료
      - 모든 신규 컨트랙트 배포
      - 통합 테스트

3.2   Mainnet 배포 준비                 3.1
      - 보안 감사
      - 파라미터 최종 확인

3.3   Mainnet 배포                      3.2
      - 신규 컨트랙트 배포
      - DAOCommitteeProxy.upgradeTo(V2)
      - V2 변수 초기화

```

---

## 7. 배포 체크리스트

### 7.1 배포 전 체크리스트

```
[ ] 모든 인터페이스 파일 생성 완료
[ ] 모든 신규 컨트랙트 구현 완료
[ ] 기존 컨트랙트 수정 완료
[ ] 단위 테스트 통과 (coverage > 80%)
[ ] 통합 테스트 통과
[ ] 보안 감사 완료 (선택적)
[ ] Testnet 배포 및 검증 완료

```

### 7.2 Mainnet 배포 순서

```
Step 1: 신규 컨트랙트 배포
────────────────────────────────────────
[ ] vTON 배포
[ ] SnapshotManager 배포
[ ] DelegationManager 배포
[ ] SecurityCouncil 배포 (3명 멤버 등록)
[ ] DAOAgendaManagerV2 배포
[ ] DAOCommitteeV2 배포

Step 2: 권한 설정
────────────────────────────────────────
[ ] vTON minter 권한 → DAOCommitteeProxy
[ ] DelegationManager owner 설정
[ ] SecurityCouncil 멤버 확인

Step 3: 프록시 업그레이드
────────────────────────────────────────
[ ] DAOCommitteeProxy.upgradeTo(DAOCommitteeV2)
[ ] 업그레이드 성공 확인

Step 4: V2 변수 초기화
────────────────────────────────────────
[ ] setVTON(vton_address)
[ ] setDelegationManager(delegation_manager_address)
[ ] setSecurityCouncil(security_council_address)
[ ] setSnapshotManager(snapshot_manager_address)
[ ] setAgendaManagerV2(agenda_manager_v2_address)
[ ] setVtonMintRatio(1e18)  // 100%
[ ] setDelegationCapBps(2000)  // 20%
[ ] setDelegationMaturitySeconds(604800)  // 7 days
[ ] setQuorumBps(400)  // 4%

Step 5: 기능 검증
────────────────────────────────────────
[ ] 기존 Member 투표 동작 확인
[ ] vTON 발행 테스트
[ ] Delegator 등록 테스트
[ ] 위임 테스트 (상한 체크)
[ ] V2 제안 생성 테스트
[ ] Security Council 기능 테스트

```

### 7.3 롤백 계획

```
만약 문제 발생 시:

1. 프로토콜 일시정지
   SecurityCouncil.propose(PAUSE_PROTOCOL)
   (2/3 승인 필요)

2. 이전 Implementation으로 롤백
   DAOCommitteeProxy.upgradeTo(DAOCommittee_V1_address)

3. 원인 분석 및 수정

4. 재배포

```

---

## 부록: 파일 경로 요약

```
contracts/
├── dao/
│   ├── DAOCommittee.sol              ⚪ 유지
│   ├── DAOCommitteeV2.sol            🔴 신규
│   ├── DAOCommitteeProxy.sol         ⚪ 유지
│   ├── DAOAgendaManager.sol          ⚪ 유지
│   ├── DAOAgendaManagerV2.sol        🔴 신규
│   ├── DAOVault.sol                  🔵 수정
│   ├── DelegationManager.sol         🔴 신규
│   ├── SecurityCouncil.sol           🔴 신규
│   ├── SnapshotManager.sol           🔴 신규
│   ├── StorageStateCommittee.sol     🔵 수정
│   └── Candidate.sol                 ⚪ 유지
├── tokens/
│   └── vTON.sol                      🔴 신규
├── interfaces/
│   ├── IvTON.sol                     🔴 신규
│   ├── IDelegationManager.sol        🔴 신규
│   ├── ISecurityCouncil.sol          🔴 신규
│   ├── ISnapshotManager.sol          🔴 신규
│   ├── IDAOCommitteeV2.sol           🔴 신규
│   ├── IDAOAgendaManagerV2.sol       🔴 신규
│   └── IStorageStateCommittee.sol    🔵 수정
├── lib/
│   ├── Agenda.sol                    🔵 수정
│   └── DelegationLib.sol             🔴 신규
└── factory/
    └── CandidateFactory.sol          ⚪ 유지

```

---

**작성일:** 2024년 1월
**버전:** 1.0
**작성자:** Claude (Anthropic)