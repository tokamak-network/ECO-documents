[**Security Council Election and Membership Management**](https://github.com/ArbitrumFoundation/governance/blob/main/docs/security-council-manager.md#security-council-manager-as-a-source-of-truth)

[https://github.com/ArbitrumFoundation/governance/blob/main/src/security-council-mgmt/SecurityCouncilManager.sol](https://github.com/ArbitrumFoundation/governance/blob/main/src/security-council-mgmt/SecurityCouncilManager.sol)

## Storage 

```javascript
/// @notice Addresses to be given specific roles on the Security Council Manager
struct SecurityCouncilManagerRoles {
    address admin;
    address cohortUpdator;
    address memberAdder;
    address[] memberRemovers;
    address memberRotator;
    address memberReplacer;
}

/// @notice Data for a Security Council to be managed
struct SecurityCouncilData {
    /// @notice Address of the Security Council
    address securityCouncil;
    /// @notice Address of the update action contract that contains the logic for updating council membership. Will be delegate called by the upgrade executor
    address updateAction;
    uint256 chainId;
}

```

```javascript
 // The Security Council members are separated into two cohorts, allowing a whole cohort to be replaced, as specified by the Arbitrum Constitution.
// These two cohort arrays contain the source of truth for the members of the Security Council. When a membership change needs to be made, a change to these arrays is first made here locally, then pushed to each of the Security Councils
// A member cannot be in both cohorts at the same time
address[] internal firstCohort;
address[] internal secondCohort;

/// @notice Address of the l2 timelock used by core governance
address payable public l2CoreGovTimelock;

/// @notice The list of Security Councils under management. Any changes to the cohorts in this manager
///         will be pushed to each of these security councils, ensuring that they all stay in sync
SecurityCouncilData[] public securityCouncils;

/// @notice Address of UpgradeExecRouteBuilder. Used to help create security council updates
UpgradeExecRouteBuilder public router;

/// @notice Maximum possible number of Security Councils to manage
/// @dev    Since the councils array will be iterated this provides a safety check to make too many Sec Councils
///         aren't added to the array.
uint256 public immutable MAX_SECURITY_COUNCILS = 500;

/// @notice Nonce to ensure that scheduled updates create unique entries in the timelocks
uint256 public updateNonce;

/// @notice Size of cohort under ordinary circumstances
uint256 public cohortSize;

/// @notice Magic value used by the L1 timelock to indicate that a retryable ticket should be created
///         Value is defined in L1ArbitrumTimelock contract https://etherscan.io/address/0xE6841D92B0C345144506576eC13ECf5103aC7f49#readProxyContract#F5
address public constant RETRYABLE_TICKET_MAGIC = 0xa723C008e76E379c55599D2E4d93879BeaFDa79C;

bytes32 public constant COHORT_REPLACER_ROLE = keccak256("COHORT_REPLACER");
bytes32 public constant MEMBER_ADDER_ROLE = keccak256("MEMBER_ADDER");
bytes32 public constant MEMBER_REPLACER_ROLE = keccak256("MEMBER_REPLACER");
bytes32 public constant MEMBER_ROTATOR_ROLE = keccak256("MEMBER_ROTATOR");
bytes32 public constant MEMBER_REMOVER_ROLE = keccak256("MEMBER_REMOVER");

```

보안 위원회  목록 보유 

멤버십에 대한 변경 사항이 있을 경우 업데이트 

모든 멤버십 변경은 관리자를 통해 이루어져야 하며, 관리자는 이러한 변경 사항을 협의회에 전파합니다. 

협의회에 직접 적용된 모든 변경 사항은 관리자가 다음에 업데이트를 푸시할 때 덮어쓰여집니다. 

일반적인 선거 흐름은 다음과 같습니다.

- **SecurityCouncilNomineeElectionGovernor.createElection**
- T가 첫 번째 선거일 이후 6개월의 배수인 T+0에서 호출됨
- **SecurityCouncilNomineeElectionGovernor.execute**
- T+21일에 호출됨
- **SecurityCouncilMemberElectionGovernor.execute**
- T + 42일 후에 호출됨
- **ArbitrumTimelock.execute**
(L2에서) - T + 42일 후에 호출됨
- **Outbox.executeTransaction**
- T + 49일 후에 호출됨
- **L1ArbitrumTimelock.executeBatch**
- T + 52일 후에 호출됨
- ArbOne 및 Nova에서 재시도 가능한 티켓 실행 - T + 52일에도 호출됨

**Public functions**

**Replace cohort**

Can only be called by the Member Election Governor. It is used to replace a whole cohort of (6) members. This is the function that will be called for the standard elections that take place every 6 months.

**Remove member**

Can be called by the Non-Emergency Security Council and the Removal Governor. Is used to remove a member. The Constitution allows members to be removed if 9 of 12 members wish them to be, or if the DAO votes to remove a member and 10% of votable tokens cast a vote, with 5/6 of voted tokens are in favour of removal.

**Replace member**

Can only be called by the Non-Emergency Security Council. This is a utility function to allow the council to call Remove and Add in the same transaction. Semantically this means that an entity has been removed from the council, and a different one has been added.

**Rotate member**

Can only be called by the Non-Emergency Security Council. Functionally this is the same as Replace, however semantically it infers different intent. Rotate should be called when a entity wish to replace their address, but it is the same entity that controls the newly added address.

**Add Security Council**

Can be called by DAO and the Emergency Security Council. Adds an additional security council whose members will be updated by the election system.

**Remove Security Council**

Can be called by DAO and the Emergency Security Council. Removes a security council from being updated by the election system.