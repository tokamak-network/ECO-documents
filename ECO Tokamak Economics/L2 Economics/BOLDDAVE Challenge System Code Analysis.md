- **Author: Donghwan Lee**
- **Last Update: 12/21/2025**
- **Reference Code Repository**
  - BOLD: [https://github.com/OffchainLabs/nitro-contracts/](https://github.com/OffchainLabs/nitro-contracts/tree/0b8c04e8f5f66fe6678a4f53aa15f23da417260e)
  - DAVE: [https://github.com/cartesi/dave](https://github.com/cartesi/dave)

# BOLD

# 1. Overall Call Flow

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1879ca1d-60f9-4fee-b679-09d499e7669a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z33WIUP4%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdFuBt0dpY4n3Qdk%2FGk0dGQC%2FJBX2wCIpqtht5V5w9FgIgat%2Fg%2FQhM4WU32TB7bp78aLbwFHFJaOx9Kk4MCbWSVcMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEVLlc300dx3SssAmyrcA3WFq1iJyfp0uMKLiJJYc7tnEwoZ0WkLVhrrwzzzlZR4WYr6N5URg0Ly%2BQirKYY%2FyZQILQIJrq1zTa1z9WSDhJC6QbnNS0Ckw7%2BjRdJzc%2FmG1bkk%2FmuyuxIE5XR%2FUU29DM1m1mKy5SoeaCOCwoJ3Xyw9Js3mZBG8ZDvbgHbtYpvOw9yGpuRZPJe4zM7O9%2FFr4LeRHxhpxNhtBYW3x8L%2FVE5UynwCBTtjTFDvMrzuP0doNTcJdkfBuq5pmCgjq38%2BMGB626LHgOFON711G9E1FQ7UThtzJtpY%2B%2FHWERlXjA70u04QXdo%2FO7GPazDnOXD3hsR%2B20C1ucBRCINPQHF1dUFhUNbyosfZ7Log%2BBmN9YZqdqQYqpiqGVa8TDhwAjOcw5J0AvKbe24tKAyOoZzcUnM0M1pDwpHO%2F9fHXNnue0WK1ptkseVrpoRD%2FDNyfYSt8K%2FuZOexaK5kq1Blswygsfvk%2FY4dK2CCm1Zem7TLWeZD50LaQyf1wnOlqHwQ8cvUeiI8rgosUp2VVJI9rnGH%2FwGALduO%2FMHKYKpyPff5WsPDeP0FOlr1znLBh6AqO7blMKT0EXOC7zMk2IgptoBbpASiK%2BVmSMt7IXQbDdxPZlMDg1x3vxJ5CPp3CNvdMKyY28wGOqUBQPPetzo6EJSm9ZWhwtO3u2VA5pXEdHboWLz0sqQVL6Hf3%2BhxiffAxpZpGqYGNhzvBB%2FMwoGnmCEJESiB%2F1Adhb9yV1Ke53V%2FHAXou%2FqxB3%2FFx7TnXLZDbqxbdO7DOgv8lysg8UvOhkTB59AuZqvObRlrG1J1AWnrGukZjBqbg1s6foxnwE7rr8v5SAMEdZbhp3PAXuplECRsONrU8LVXj5CMyK%2B2&X-Amz-Signature=2cfcb9942ff371642fa9d0baf5b6d273d47cc2e9f874ec65064f3f6d69f62124&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 2. Contract Code Analysis

## 2.1. AssertionStakingPool.sol

### 2.1.1 Constructor

solidity

`constructor(address _rollup, bytes32 _assertionHash) 
    AbsBoldStakingPool(IRollupCore(_rollup).stakeToken()) 
{
    rollup = _rollup;
    assertionHash = _assertionHash;
}`

**Role:** Initialize pool and determine which assertion to defend

**Information stored:**

- `rollup`: Target rollup address
- `assertionHash`: Hash of the correct state the pool claims (immutable, public)

---

### 2.1.2 createAssertion()

solidity

`function createAssertion(AssertionInputs calldata assertionInputs) external {
    uint256 requiredStake = assertionInputs.beforeStateData.configData.requiredStake;
    IERC20(stakeToken).safeIncreaseAllowance(rollup, requiredStake);
    IRollupUser(rollup).newStakeOnNewAssertion(
        requiredStake, assertionInputs, assertionHash, address(this)
    );
}`

**Role:** Pool creates counter-assertion on rollup

**Information stored:**

- Pool address registered as a single staker on rollup
- `address(this)` = Entire pool treated as one economic entity

---

### 2.1.3 withdrawStakeBackIntoPool()

solidity

`function withdrawStakeBackIntoPool() public {
    IRollupUser(rollup).withdrawStakerFunds();
}`

**Role:** Retrieve stake refund from rollup back into pool

**Information stored:**

- Only pool's token balance increases
- `depositBalance` not updated (no reward distribution logic)

---

## 2.2. AbsBoldStakingPool.sol

### 2.2.1 depositIntoPool()

solidity

`function depositIntoPool(uint256 amount) external {
    depositBalance[msg.sender] += amount;
    IERC20(stakeToken).safeTransferFrom(msg.sender, address(this), amount);
}`

**Role:** Users deposit tokens into pool

**Information stored:**

- Who deposited how much (public mapping)
- No weighting by deposit order or time

---

### 2.2.2 withdrawFromPool()

solidity

`function withdrawFromPool(uint256 amount) public {
    depositBalance[msg.sender] = balance - amount;
    IERC20(stakeToken).safeTransfer(msg.sender, amount);
}`

**Role:** Users withdraw based on their deposit amount

**Information stored:**

- Withdrawal limited to initial deposit amount
- Reward distribution is separate process (DAO offchain)

---

## 2.3. RollupUserLogic.sol

### 2.3.1 stakeOnNewAssertion()

solidity

`function stakeOnNewAssertion(
    AssertionInputs calldata assertion,
    bytes32 expectedAssertionHash
) public {
    require(
        expectedAssertionHash == bytes32(0) ||
        getAssertionStorage(expectedAssertionHash).status == AssertionStatus.NoAssertion,
        `<u>`"EXPECTED_ASSERTION_SEEN"  // ← Prevents duplicates`</u>`
    );
    
    // Stake handling for second child (rival)
    if (!getAssertionStorage(newAssertionHash).isFirstChild) {
        IERC20(stakeToken).safeTransfer(
            loserStakeEscrow, 
            assertion.beforeStateData.configData.requiredStake
        );
    }
    
    (bytes32 newAssertionHash, ) = createNewAssertion(...);
}`

**Role:** Create assertion and check for duplicates

**Information stored:**

- <u>Same </u><u>`assertionHash`</u><u> can only be created once → No same state argument accepted anymore!</u>
- <u>First pool succeeds, second pool reverts</u>
- **→ Multiple pools impossible**
- Second child stake → `loserStakeEscrow` immediately

---

### 2.3.2 Staker Mapping

solidity

`_stakerMap[msg.sender] = Staker({
    amountStaked: requiredStake,
    latestStakedAssertion: assertionHash,
    withdrawalAddress: address(this)
});`

**Role:** Register pool as a single staker

**Information stored:**

- Pool address (`msg.sender` = pool address)
- Entire pool treated as one economic entity
- Rollup has no knowledge of internal participants

---

## 2.4. RollupCore.sol

### 2.4.1 createNewAssertion()

solidity

`function createNewAssertion(
    AssertionInputs calldata assertion,
    bytes32 prevAssertionHash,
    bytes32 expectedAssertionHash
) internal returns (bytes32 newAssertionHash, bool overflowAssertion) {
    
    // Duplicate check
    require(
        getAssertionStorage(newAssertionHash).status == AssertionStatus.NoAssertion,
        "ASSERTION_SEEN"
    );
    
    // Create new assertion node
    AssertionNode memory newAssertion = AssertionNodeLib.createAssertion(
        prevAssertion.firstChildBlock == 0, // isFirstChild
        configHash
    );
    
    prevAssertion.childCreated();
    _assertions[newAssertionHash] = newAssertion;
}`

**Role:** Create assertion node and track children

**Information stored:**

- `assertions[assertionHash]` = new AssertionNode
- `firstChildBlock` / `secondChildBlock` for fork detection
- `isFirstChild` determines stake handling

---

### 2.4.2 childCreated()

solidity

`function childCreated(AssertionNode storage self) internal {
    if (self.firstChildBlock == 0) {
        self.firstChildBlock = uint64(block.number);  // First child
    } else if (self.secondChildBlock == 0) {
        self.secondChildBlock = uint64(block.number); // Second child = Fork!
    }
}`

**Role:** Track fork creation

**Information stored:**

- First child: `isFirstChild = true`, stake stays
- <u>Second child: </u><u>`isFirstChild = false`</u><u>, stake → </u><u>`loserStakeEscrow`</u>
- <u>No third child in the code → No another challenging entity possbile!</u>

---

### 2.4.3 loserStakeEscrow

solidity

`// State variable
address public loserStakeEscrow;`

**Role:** Store address for loser stakes

**Information stored:**

- Simple address (not a contract with distribution logic)
- No automatic reward distribution
- DAO manually processes defender's bounty offchain

# DAVE

# 1. Overall Call Flow

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3a3ba40c-b892-4530-a7cc-bf411e76c314/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z33WIUP4%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdFuBt0dpY4n3Qdk%2FGk0dGQC%2FJBX2wCIpqtht5V5w9FgIgat%2Fg%2FQhM4WU32TB7bp78aLbwFHFJaOx9Kk4MCbWSVcMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEVLlc300dx3SssAmyrcA3WFq1iJyfp0uMKLiJJYc7tnEwoZ0WkLVhrrwzzzlZR4WYr6N5URg0Ly%2BQirKYY%2FyZQILQIJrq1zTa1z9WSDhJC6QbnNS0Ckw7%2BjRdJzc%2FmG1bkk%2FmuyuxIE5XR%2FUU29DM1m1mKy5SoeaCOCwoJ3Xyw9Js3mZBG8ZDvbgHbtYpvOw9yGpuRZPJe4zM7O9%2FFr4LeRHxhpxNhtBYW3x8L%2FVE5UynwCBTtjTFDvMrzuP0doNTcJdkfBuq5pmCgjq38%2BMGB626LHgOFON711G9E1FQ7UThtzJtpY%2B%2FHWERlXjA70u04QXdo%2FO7GPazDnOXD3hsR%2B20C1ucBRCINPQHF1dUFhUNbyosfZ7Log%2BBmN9YZqdqQYqpiqGVa8TDhwAjOcw5J0AvKbe24tKAyOoZzcUnM0M1pDwpHO%2F9fHXNnue0WK1ptkseVrpoRD%2FDNyfYSt8K%2FuZOexaK5kq1Blswygsfvk%2FY4dK2CCm1Zem7TLWeZD50LaQyf1wnOlqHwQ8cvUeiI8rgosUp2VVJI9rnGH%2FwGALduO%2FMHKYKpyPff5WsPDeP0FOlr1znLBh6AqO7blMKT0EXOC7zMk2IgptoBbpASiK%2BVmSMt7IXQbDdxPZlMDg1x3vxJ5CPp3CNvdMKyY28wGOqUBQPPetzo6EJSm9ZWhwtO3u2VA5pXEdHboWLz0sqQVL6Hf3%2BhxiffAxpZpGqYGNhzvBB%2FMwoGnmCEJESiB%2F1Adhb9yV1Ke53V%2FHAXou%2FqxB3%2FFx7TnXLZDbqxbdO7DOgv8lysg8UvOhkTB59AuZqvObRlrG1J1AWnrGukZjBqbg1s6foxnwE7rr8v5SAMEdZbhp3PAXuplECRsONrU8LVXj5CMyK%2B2&X-Amz-Signature=f4e1c91e4fd70e0138a17763635fd9d0477ff77f96056612e3b1d936a1e9b079&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 2. Contract Code Analysis

## 2. Clock.sol

### 2.1 State struct

solidity

`struct State {
    Time.Duration allowance;
    Time.Instant startInstant;
}`

**Role:** Track time budget and initialization status for each commitment

**Information stored:**

- `allowance`: Remaining time in blocks (**also serves as initialization flag**)
- `startInstant`: 0 = paused, non-zero = ticking

**Key insight:**

- `allowance == 0` → Not initialized
- `allowance != 0` → Initialized (duplicate prevention)

---

### 2.2 requireNotInitialized()

solidity

`function requireNotInitialized(State memory state) internal pure {
    require(state.notInitialized(), "clock is initialized");
}

function notInitialized(State memory state) internal pure returns (bool) {
    return state.allowance.isZero();
}`

**Role:** Duplicate prevention check

**Information stored:** None (reads existing state)

**Mechanism:**

- Checks if `allowance == 0`
- Reverts if `allowance != 0` (duplicate)
- **Critical for single-winner enforcement**

---

### 2.3 setNewPaused()

solidity

`function setNewPaused(
    State storage state,
    Time.Instant checkinInstant,
    Time.Duration initialAllowance
) internal {
    Time.Duration _allowance = 
        initialAllowance.monus(Time.currentTime().timeSpan(checkinInstant));
    _setNewPaused(state, _allowance);
}

function _setNewPaused(State storage state, Time.Duration allowance) private {
    require(!allowance.isZero(), "can't create clock with zero time");
    state.allowance = allowance;  // ← Marks as initialized!
    state.startInstant = Time.ZERO_INSTANT;
}`

**Role:** Initialize clock (marks commitment as registered)

**Information stored:**

- `allowance`: Set to non-zero (e.g., 1000 blocks)
- `startInstant`: Set to 0 (paused)

**Key mechanism:**

- Once set, `requireNotInitialized()` will fail
- **This enforces duplicate prevention**

---

## 3. Tournament.sol

### 3.1 Storage Mappings

solidity

`mapping(Tree.Node => Clock.State) clocks;
mapping(Tree.Node => address) claimers;
mapping(Tree.Node => Machine.Hash) finalStates;
mapping(Match.IdHash => Match.State) matches;

Tree.Node danglingCommitment;
uint256 matchCount;`

**Role:** Protocol state storage

**Information stored:**

- `clocks[commitmentRoot]`: Clock per commitment (**duplicate prevention via allowance**)
- `claimers[commitmentRoot]`: Address of joiner
- `finalStates[commitmentRoot]`: Claimed final state
- `matches[matchIdHash]`: Active match states
- `danglingCommitment`: Unmatched commitment waiting
- `matchCount`: Number of active matches

---

### 3.2 joinTournament()

solidity

`function joinTournament(
    Machine.Hash _finalState,
    bytes32[] calldata _proof,
    Tree.Node _leftNode,
    Tree.Node _rightNode
) external payable override tournamentOpen {
    require(msg.value >= bondValue(), InsufficientBond());
    
    Tree.Node _commitmentRoot = _leftNode.join(_rightNode);
    
    _commitmentRoot.requireFinalState(
        args.commitmentArgs.height, _finalState, _proof
    );
    
    Clock.State storage _clock = clocks[_commitmentRoot];
    _clock.requireNotInitialized(); // ← DUPLICATE CHECK!
    _clock.setNewPaused(args.startInstant, args.allowance);
    
    pairCommitment(_commitmentRoot, _clock, _leftNode, _rightNode);
    claimers[_commitmentRoot] = msg.sender;
}`

**Role:** Entry point for joining tournament

**Information stored:**

- `clocks[_commitmentRoot]`: Clock initialized (allowance set to non-zero)
- `claimers[_commitmentRoot]`: Joiner's address
- `finalStates[_commitmentRoot]`: Claimed final state

**Critical flow:**

1. Bond check
1. Calculate `commitmentRoot`
1. Verify final state Merkle proof
1. **Duplicate check** (`requireNotInitialized()`)
1. Initialize clock (marks as used)
1. Pair for match

**Duplicate prevention:**

- First claim: `allowance == 0` → Pass, set to 1000
- Second claim: `allowance == 1000` → Revert "clock is initialized"

---

### 3.3 pairCommitment()

solidity

`function pairCommitment(
    Tree.Node _rootHash,
    Clock.State storage _newClock,
    Tree.Node _leftNode,
    Tree.Node _rightNode
) internal {
    (bool _hasDanglingCommitment, Tree.Node _danglingCommitment) =
        hasDanglingCommitment();
    
    if (_hasDanglingCommitment) {
        (Match.IdHash _matchId, Match.State memory _matchState) = 
            Match.createMatch(...);
        
        matches[_matchId] = _matchState;
        
        clocks[_danglingCommitment].addMatchEffort(...);
        _newClock.addMatchEffort(...);
        
        clocks[_danglingCommitment].advanceClock();
        
        clearDanglingCommitment();
        matchCount++;
    } else {
        setDanglingCommitment(_rootHash);
    }
}`

**Role:** Asynchronous matchmaking

**Information stored:**

- `danglingCommitment`: Set or cleared
- `matches[matchIdHash]`: Created if paired
- `matchCount`: Incremented when match created

---

### 3.4 advanceMatch()

solidity

`function advanceMatch(
    Match.Id calldata _matchId,
    Tree.Node _leftNode,
    Tree.Node _rightNode,
    Tree.Node _newLeftNode,
    Tree.Node _newRightNode
) external override {
    Match.State storage _matchState = matches[_matchId.hashFromId()];
    
    _matchState.advanceMatch(
        _matchId, _leftNode, _rightNode, _newLeftNode, _newRightNode
    );
    
    clocks[_matchId.commitmentOne].advanceClock();
    clocks[_matchId.commitmentTwo].advanceClock();
}`

**Role:** Progress bisection game

**Information stored:**

- `matchState`: Height decreases, position updates
- Both clocks: Toggled (turn switch)

---

### 3.5 winMatchByTimeout()

solidity

`function winMatchByTimeout(
    Match.Id calldata _matchId,
    Tree.Node _leftNode,
    Tree.Node _rightNode
) external override {
    Clock.State storage _clockOne = clocks[_matchId.commitmentOne];
    Clock.State storage _clockTwo = clocks[_matchId.commitmentTwo];
    
    if (_clockOne.hasTimeLeft() && !_clockTwo.hasTimeLeft()) {
        _clockOne.deducted(_clockTwo.timeSinceTimeout());
        pairCommitment(_matchId.commitmentOne, _clockOne, _leftNode, _rightNode);
        deleteMatch(_matchId, MatchDeletionReason.TIMEOUT, WinnerCommitment.ONE);
    }
    // Mirror logic for commitmentTwo
}`

**Role:** Determine winner by timeout

**Information stored:**

- Winner's clock: Time deducted
- Loser: Deleted from `claimers`
- Match: Deleted from `matches`
- `matchCount`: Decremented

---

### 3.6 tryRecoveringBond()

solidity

`function tryRecoveringBond() public override returns (bool) {
    require(isFinished(), TournamentNotFinished());
    
    (bool hasDangling, Tree.Node winningCommitment) = hasDanglingCommitment();
    require(hasDangling, NoWinner());
    
    address winner = claimers[winningCommitment];
    uint256 contractBalance = address(this).balance;
    (bool success,) = winner.call{value: contractBalance}("");
    
    if (success) {
        deleteClaimer(winningCommitment);
    }
    return success;
}`

**Role:** Final bond distribution

**Information stored:**

- All bonds transferred to winner
- Winner deleted from `claimers`

## 4. Match.sol

### 4.1 advanceMatch()

solidity

`function advanceMatch(
    State storage state,
    Id calldata id,
    Tree.Node leftNode,
    Tree.Node rightNode,
    Tree.Node newLeftNode,
    Tree.Node newRightNode
) internal {
    state.requireParentHasChildren(leftNode, rightNode);
    
    if (!state.agreesOnLeftNode(leftNode)) {
        leftNode.requireChildren(newLeftNode, newRightNode);
        state._goDownLeftTree(newLeftNode, newRightNode);
    } else {
        rightNode.requireChildren(newLeftNode, newRightNode);
        state._goDownRightTree(newLeftNode, newRightNode);
    }
}`

**Role:** Bisection logic - find disagreement point

**Information stored:**

- `currentHeight`: Decremented by 1
- `runningLeafPosition`: Updated based on direction
- `otherParent`, `leftNode`, `rightNode`: Updated to next tree level

**Mechanism:**

- Check if both commitments agree on left child
- Disagree → Go down left subtree
- Agree → Go down right subtree (disagreement must be in right)
- Height decreases each step until finding exact divergence point