# Abi

# Storage 

```javascript

  address public depositManager;
  address public daoCommittee;
  address public layer2CandidateImp;
  address public ton;
  address public wton;
  address public onDemandL2Registry;
```

# Event

```solidity

    event DeployedCandidate(
        address sender,
        address layer2,
        address operator,
        bool isLayer2Candidate,
        string name,
        address committee,
        address seigManager
    );
```

# Function

```javascript

    modifier onlyDAOCommittee() {
        require(msg.sender == daoCommittee, "sender is not daoCommittee");
        _;
    }
```

## onlyOwner

```solidity
 function setAddress(
        address _depositManager,
        address _daoCommittee,
        address _layer2CandidateImp,
        address _ton,
        address _wton,
        address _onDemandL2Registry
    ) external onlyOwner
```

## onlyDAOCommittee

```solidity
function deploy(
        address _sender,
        string memory _name,
        address _committee,
        address _seigManager
    )
        public onlyDAOCommittee returns (address) 
```