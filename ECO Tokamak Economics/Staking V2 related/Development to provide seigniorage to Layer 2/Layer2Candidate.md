- 심플스테이킹(톤 스테이킹)의 기본기능(예치, 업데이트시뇨리지-이자지급, 출금 기능)을 지원한다. 
- DAOCandidate에서 할 수 있는 다오 멤버 기능을 지원한다. 
- 업데이트 시뇨리지 실행시, Layer2Candidate의 시퀀서(오퍼레이터)가 시뇨리지를 받을 수 있다.
- 톤스테이킹 출금을 하면서, 동시에 해당 Layer2에 예치할 수 있는 기능을 지원한다.

# ABI

# Storage

```javascript
contract CandidateStorage   {
    mapping(bytes4 => bool) internal _supportedInterfaces;
    bool public isLayer2Candidate;
    address public candidate;
    string public memo;

    address public committee;
    address public seigManager;

}

 address ton;
 address wton;
```

# Event 

```javascript
event Initialized(address _operateContract, string memo, address committee, address seigManager);

event SetMemo(string _memo);
```

# Function 

```solidity
modifier onlyOwner() {
    require(isAdmin(msg.sender), "AuthControl: Caller is not an admin");
    _;
}

modifier onlyCandidate() {
    require(IOperateContract(candidate).isOperator(msg.sender),
    "sender is not an operator");
    _;
}
```

## onlyOwner 

```solidity
function initialize(
        address _operateContract,
        string memory _memo,
        address _committee,
        address _seigManager,
        address _ton,
        address _wton
    ) external onlyOwner  


function setMemo(string calldata _memo) external onlyOwner
```

## onlyCandidate

```solidity
function changeMember(uint256 _memberIndex)
        external
        onlyCandidate
        returns (bool)


function retireMember() external onlyCandidate returns (bool)

function castVote(
        uint256 _agendaID,
        uint256 _vote,
        string calldata _comment
    )  external onlyCandidate

function claimActivityReward() external  onlyCandidate

```

## Anybody

 

```javascript
function updateSeigniorage() external returns (bool)

/// @param afterCall 0: none, 1: claim, 2: staking
///                  param 1 and 2 are executed when the sender is an operator
///                	 otherwise executed with 0 option.
function updateSeigniorage(uint256 afterCall) public returns (bool)

function totalStaked()
        external
        view
        returns (uint256 totalsupply)

function stakedOf(
        address _account
    )
        external
        view
        returns (uint256 amount)

     
function operator() external view returns (address) 


function isCandidateContract() external pure returns (bool) {
        return true;
  }

function operator() external view returns (address) { return candidate; }
function isLayer2() external pure returns (bool) { return true; }

```

# Test 

- The basic functions of Simple Staking (deposit, update seigniorage, withdrawal function) must be supported.
- When executing update seigniorage, seigniorage must be given to the sequencer (operator) of Layer2Candidate.

`npx hardhat test test/layer2/units/2.Layer2Manager.test.ts`

[[SeigManagerV1_3]] 