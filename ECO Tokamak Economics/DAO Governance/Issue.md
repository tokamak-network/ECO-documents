1. registerLayer2Candidate 함수는 제거해도 될 것 같다. 이 함수는 기존 legacy layer2를 Candidate로 등록하는 역할을 하지만, 현재 모든 Candidate는 CandidateProxy 컨트랙트이다. 앞으로 생성될 모든 Candidate도 CandidateProxy 컨트랙트가 된다. 모든 candidate를 조회한 결과, 이 값은 더 이상 사용되지 않을 것으로 보인다. `mapping(address => bool) public privateLayer2;` 상태 변수도 사용되지 않는 변수가 된다.
[[Verify that privateLayer2 exists]]
1. 프록시 체인 구조로 인해 Etherscan에서 Owner와 V1 함수를 조회할 수 없다. 표준 프록시 구조를 따르지 않아 Etherscan에서 DAOCommitteeV1_1 함수를 호출할 수 없다. 이더리움 표준을 최대한 준수해야 하므로 이에 대한 논의가 필요하다.
> Proxy 컨트랙트의 storage는 변하지 않는 값을 hashed storage slot에 저장을 해둔다. (1) Proxy 컨트랙트에는 Logic 컨트랙트의 storage를 갖고 있지 않아도 된다. (2) Logic 컨트랙트에 Proxy Storage를 갖고 있지 않아도 된다. eg. *contract ****Layer2ManagerV1_1**** is ****ProxyStorage****, AccessibleCommon, Layer2ManagerStorage*
1. ***가짜* Layer2 컨트랙트**를 배포하여 `operator()` 함수를 악용할 수 있는 공격 가능성이 있는지 확인이 필요하다. 예를 들어, coinage 컨트랙트를 무제한으로 생성할 수 있다. 더 강력한 제한이 필요할 수 있다.
```solidity
modifier onlyMinterOrOperator(address layer2) {
    require(
        hasRole(MINTER_ROLE, msg.sender) || ILayer2(layer2).operator() == msg.sender,
        'sender is neither admin nor operator'
    );
    _;
}
```
1. Candidate를 생성할 때는 TON을 staking하지 않아도 된다. (2) 하지만 Candidate로 활동하려면 1000.1 TON 이상이 staking되어 있어야 한다.
> CandidateAddOn 함수는 TON을 미리 보내는 것으로 보인다(?). *_transferDepositAmount(msg.sender, rollupConfig, amount, flagTon, memo);*

  - ***Creating a candidate without staking TON:***

```bash
$ *cast send 0xA2101482b28E3D99ff6ced517bA41EFf4971a386 \
"createCandidate(string)" "https://snapshot.box/#/explore" \
--rpc-url https://ethereum-sepolia-rpc.publicnode.com \
--private-key dc719aa7ad72b35f639a38fe17422e18bd5b05bdcb76e2e98bacfd3827a90c5a*
```

> [*https://sepolia.etherscan.io/tx/0xf71c37211691d1e30622936a4c3a61a59074071909be6882da76269ab355d0de*](https://sepolia.etherscan.io/tx/0xf71c37211691d1e30622936a4c3a61a59074071909be6882da76269ab355d0de)

  - *created two contracts:*
    - *CandidateProxy: *[*0x5cc9768a4eb0ab8af1fa4c816754ece169168616*](https://sepolia.etherscan.io/address/0x5cc9768a4eb0ab8af1fa4c816754ece169168616#code)
    - *RefactorCoinageSnapshotProxy: *[*0x4b6263de221735488b795ec04b52082fb2819968*](https://sepolia.etherscan.io/address/0x4b6263de221735488b795ec04b52082fb2819968#code)
  - ***Call updateSeigniorage():***
```bash
$ *cast send *0xA2101482b28E3D99ff6ced517bA41EFf4971a386* \
"updateSeigniorage(address)" 0x488f3660fcd32099f2a250633822a6fbf6eb771b \
--rpc-url https://ethereum-sepolia-rpc.publicnode.com \
--private-key dc719aa7ad72b35f639a38fe17422e18bd5b05bdcb76e2e98bacfd3827a90c5a*
```

—> *Error: **`Failed to estimate gas: server returned an error response: error code 3: execution reverted, data: "0x38c6bb5a": MinimumAmountError`*

*The places where the **`minimumAmount`** condition is checked are as follows:*

  - * **`changeMember(uint256)`** from DAOCommittee_V1.sol*
  - *`onDeposit(address, address, uint256)`** from SeigManager.sol, SeigManagerV1_1.sol and SeigManagerV1_2.sol*
  - *`onWithdraw(address, address, uint256)`** from SeigManager.sol, SeigManagerV1_1.sol and SeigManagerV1_2.sol*
  - *`updateSeigniorage()`** from SeigManager.sol and SeigManagerV1_1.sol*
  - *`_updateSeigniorage()`** from SeigManagerV1_3.sol*
1. optimize CreateCandidate function
> **prettier 모두 적용해서 PR. Solidity 코드에 자동으로 prettier가 적용되도록**

```solidity
/// @notice Registers a new Candidate managed by msg.sender.
/// @param _memo Candidate Memo
function createCandidate(
    string calldata _memo
) external validSeigManager validLayer2Registry validCommitteeL2Factory {
    _createCandidate(_memo, msg.sender, false);
}

/// @notice Registers a new Candidate managed by operator.
/// @param _memo Candidate Memo
/// @param _operatorAddress operatorAddress
function createCandidateOwner(
    string calldata _memo,
    address _operatorAddress
) public validSeigManager validLayer2Registry validCommitteeL2Factory onlyOwner {
    if (_operatorAddress == address(0)) revert ZeroAddressError();
    _createCandidate(_memo, _operatorAddress, false);
}

/// @notice Registers a new Candidate managed by operatorManagerContract.
/// @param _memo Candidate Memo
/// @param _operatorManagerAddress operatorManagerContract Address
/// @return candidateContract Address
function createCandidateAddOn(
    string calldata _memo,
    address _operatorManagerAddress
)
    public
    validSeigManager
    validLayer2Registry
    validCommitteeL2Factory
    returns (address candidateContract)
{
    if (_operatorManagerAddress == address(0)) revert ZeroAddressError();
    if (msg.sender != layer2Manager) revert PermissionError();

    return _createCandidate(_memo, _operatorManagerAddress, true);
}

function _createCandidate(
    string memory _memo,
    address _operator,
    bool _isAddOn
) internal returns (address candidateContract) {
    if (isExistCandidate(_operator)) revert CreateCandiateError(2);

    // (1) deploy candidate contract
    if (_isAddOn) {
        candidateContract = ICandidateAddOnFactory(candidateAddOnFactory).deploy(
            _operator,
            _memo,
            address(this),
            address(seigManager)
        );
    } else {
        candidateContract = candidateFactory.deploy(
            _operator,
            false,
            _memo,
            address(this),
            address(seigManager)
        );
    }
    emit CandidateContractCreated(_operator, candidateContract, _memo);

    // (2) set candidate info
    if (candidateContract == address(0)) revert CreateCandiateError(1);
    candidates.push(_operator);
    _candidateInfos[_operator].candidateContract = candidateContract;

    // (3) register candidate and deploy coinage
    if (!layer2Registry.registerAndDeployCoinage(candidateContract, address(seigManager))) {
        revert CreateCandiateError(3);
    }
}
```
1. 모든 Proxy에 storage가 존재한다. 하지만 표준대로라면 Proxy에는 upgrade 관련 로직만 있어도 된다. 현재 Proxy와 Logic 컨트랙트 storage를 동일하게 사용하고 있다.
1. 직관적인 함수 이름?
—> createCandidateOwner (Owner에 의해서 실행되는 것인지, Owner를 지정하는 것인지 헷갈릴 수 있음)
1. tokamak-dao-contracts 레포 —> dao 안건 정리용 수정?