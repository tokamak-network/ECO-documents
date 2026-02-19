# The basics concept of services 

[https://docs.google.com/presentation/d/19rKQoBhNQ2tHhfWJBRbGn2BbGcLUvWPnvfofaOyLQj0/edit#slide=id.g1ee16850fbf_0_54](https://docs.google.com/presentation/d/19rKQoBhNQ2tHhfWJBRbGn2BbGcLUvWPnvfofaOyLQj0/edit#slide=id.g1ee16850fbf_0_54)

[[Function description of TON Staking V2 (deprecated) ]] 

# Change log

- v0_1 : 2023.3.17 : initial document 
- 

# ABI 

# Structure 

```javascript
struct Info {
    address addressManager;
    address l1Messenger; 
    address l1Bridge; 
    address l2ton;
}

struct Holdings {
    uint256 securityDeposit;
    uint256 seigs;
    bool bonding;
}

struct StakeInfo {
      uint256 stakePrincipal;
      uint256 bondPrincipal; 
      uint256 stakelton;
      uint256 bondlton; 
      bool staker;
      bool bonder;
  }

  struct WithdrawalReqeust {
      uint32 withdrawableBlockNumber;
      uint128 amount;
      bool processed;
  }
```

# Storage

## SeigManagerV2

```javascript
IERC20 public ton;
address public wton;
address public dao;
address public stosDistribute;
address public seigManagerV1;
address public tot;
address public layer2Manager;
address public stakingLayer2;
uint256 public seigPerBlock;
uint256 public lastSeigBlock;
uint256 public startBlock;
uint256 public indexLton; // for staker or bonder

uint16 public ratesDao;   // divided ratesUnits
uint16 public ratesStosHolders; // divided ratesUnits
uint16 public ratesTonStakers; // divided ratesUnits
uint16 public ratesUnits; // divided uint. 10000
uint32 public minimumBlocksForUpdateSeig; // the number of block
bool internal free = true;
```

## Layer2Manager

```javascript
IERC20 public ton;
address public seigManagerV2;
address public stakingLayer2;
uint256 public minimumDepositForSequencer;
uint256 public delayBlocksForWithdraw;
uint256 public maxLayer2Count;

uint256 public totalSecurityDeposit; //시퀀서의 담보금
uint256 public totalSeigs; //아직 배분되지 않은 시뇨리지
```

## StakingLayer2

```javascript
address public ton;
address public seigManagerV2;
address public layer2Manager;
uint256 public totalStakedLton;
uint256 public totalBondedLton;

mapping (bytes32 => uint256) public layerStakedLton; // 레이어별 스테이킹된 톤
mapping (bytes32 => mapping(address => LibStake.StakeInfo)) public layerStakes; // ltos uint

// layer2Key => msg.sender => withdrawal requests (언스테이크시 등록 )
mapping (bytes32 => mapping (address => LibStake.WithdrawalReqeust[])) public withdrawalRequests;
// layer2Key => msg.sender => index
mapping (bytes32 => mapping (address => uint256)) public withdrawalRequestIndex;

// pending unstaked amount
// layer2 => msg.sender => ton amount
mapping (bytes32 => mapping (address => uint256)) public _pendingUnstaked;
// layer2 => ton amount
mapping (bytes32 => uint256) public _pendingUnstakedLayer2;
// msg.sender =>  ton amount
mapping (address => uint256) public _pendingUnstakedAccount;

address[] public stakeAccountList;
address[] public bondAccountList;
```

# Functions 

## Key to distinguish Layer2 is LayerKey 

There are two kind of layer2. 

### StakingOnlyLayer2

- Registering a layer2 that **can only be staked** (Bonder cannot be provided later, fast withdrawal function cannot be supported)

### StakingLayer2 

- The sequencer can register layer 2 in TON staking v2 system using the address information of layer2 operated by the sequencer.
- **This layer2  supports  fast withdrawal of layer2**.

## How to define layer2 on smart contract 

we can distinguish layer2 with layerKey.

**`LayerKey`** is calculated with bytes32(keccak256(encode(addressManager, L1messanger, L1Bridge, L2tokan of TON))).

If it is a **StakingOnlyLayer2** that does not operate the actual layer2, The `addressManager` address becomes the calling account address, and the `l1Messenger`, `l1Bridge`, and `l2ton` of TON addresses are set to address(0).

`bytes32 layerKey = Layer2Manager.getLayer(addressManager, l1Messenger, l1Bridge, l2ton)` 

`Layer2.Info memory layer = Layer2Manager.getLayer(addressManager, l1Messenger, l1Bridge, l2ton)`  

`Layer2.Info memory layer = Layer2Manager.getLayerWithKey(layerKey)` 

```javascript
function.getLayer(
        address addressManager,
        address l1Messenger,
        address l1Bridge,
        address l2ton
    ) external view returns (Layer2.Info memory layer) {
            layer = layers.get(
                addressManager,
                l1Messenger,
                l1Bridge,
                l2ton);
    }

function getLayerWithKey(bytes32 _key) public view returns (Layer2.Info memory layer) {
        layer = layers.getWithLayerKey(_key);
    }

function layerKey(
        address addressManager,
        address l1Messenger,
        address l1Bridge,
        address l2ton
    ) public pure returns (bytes32 key) {
            key = bytes32(keccak256(abi.encode(
                addressManager,
                l1Messenger,
                l1Bridge,
                l2ton
            )));
    }
```

## Register Layer2

There are two kind of layer2.

- StakingOnlyLayer2
  - Registering a layer2 that can only be staked (Bonder cannot be provided later, fast withdrawal function cannot be supported)
  - Interface 
`Layer2Manager.createStakingOnly()`  

```javascript
function createStakingOnly() external
```

sample
- StakingLayer2
  - Register a layer2 that supports staking and fast withdrawal
  - Interface 
`Layer2Manager.create(address addressManager, address l1Messenger , address l1Bridge,  address l2ton)`  

```javascript
function create(
        address addressManager,
        address l1Messenger, 
        address l1Bridge, 
        address l2ton
    )
        external
```

sample

## Get Layer2 List 

- It must be possible to check whether fast withdrawal is supported. 
- Interface 
`Layer2Manager.getAllLayers()`

```javascript
function getAllLayers()
        external view
        returns (bytes32[] memory layerKeys_, Layer2.Info[] memory layers_, Layer2.Holdings[] memory holdings_)


** ***If ***[***Layer2.Holdings***](http://layer2.holdings/)***.bonding == true, this layer2 supports a fast withdraw .***
```

sample

## Get total staked amount of Layer2

- Interface 
`StakingLayer2.balanceOfLton(byte32 layerKey)` 

```javascript
function balanceOfLton(bytes32 layerKey) public view returns (uint256 amount)
```

sample

## Get total staked amount of Layer2’s account

- Interface 
`StakingLayer2.balanceOfLton(byte32 layerKey, address account)` 

```javascript
function balanceOfLton(bytes32 layerKey, address account) public view returns (uint256 amount) {
        LibStake.StakeInfo memory info = layerStakes[layerKey][account];
        amount = info.stakelton;
    }
```

sample

 

## Get total staked amount of account

- Interface 
`LayerManager2.balanceOfLton(address account)` 

```javascript
function balanceOfLton(address account) public view returns (uint256 amount) {
    uint256 len = layerKeys.length;
    for(uint256 i = 0; i < len; i++){
        amount += StakingLayer2I(stakingLayer2).balanceOfLton(layerKeys[i], account);
    }
}
```

sample

 

## Claim by sequencers 

- The following functions are available for only Sequencer.
  - Check Sequencer’s Seigniorage
    - interface 
`Layer2Manager.layerHoldings(bytes32 layerKey_)`

```javascript
function layerHoldings(bytes32 layerKey_)
        external view
        returns (Layer2.Holdings memory)
    {
        return holdings[layerKey_];
    }

** [***Layer2.Holdings***](http://layer2.holdings/)***.seigs is an claimable amount.  ***
```

sample 
  - Make a Sequencer’s seigniorage claim
    - interface 
`Layer2Manager.claim(bytes32 layerKey_)`

```javascript
function claim(bytes32 layerKey_) external
```

sample

## Update Seigniorage

- Execute update seigniorage (immediate interest payment) 
  - Interface 
`SeigManager2.runUpdateSeigniorage()`

```javascript
function runUpdateSeigniorage() public  returns (bool res)
```

sample
- We can know the amount that can be issued when seignorage is executed
  - Interface 
`SeigManager2.mintableSeigsAmount()`

```javascript
function mintableSeigsAmount() external view returns (uint256 amount)
```

sample

## Stake 

- Interface in case of prior approval and execution
- Interface 
`SeigManager2.stake(bytes32 layerKey, uint256 amount)`

```javascript
function stake(bytes32 layerKey, uint256 amount) public 
```

sample
- When executing without prior approval,
  - Interface 
 
```javascript
 
```

sample

## Restake 

- `numberOfPendings`
  - After unstaking, we can see the pending information waiting for a withdrawal request.
    - totalRequests: all unstaking requests so far
    - withdrawIndex: Minimum value of the index that has not been withdrawn yet
    - pendingLength: Number of pending requests
    - **pendingLength requests from index withdrawIndex have not been withdrawn yet.**
  - Interface 
`SeigManager2.numberOfPendings(bytes32 layerKey, address account)`

```solidity
function numberOfPendings(bytes32 layerKey, address account)
        public view returns (uint256 totalRequests, uint256 withdrawIndex, uint256 pendingLength)
```
- Restake
  -  Cancel 1 unstake (the first requested).
`SeigManager2.restake(bytes32 layerKey)`

```javascript
function restake(bytes32 layerKey) external view returns (bool)
```

sample
  - Cancel multiple unstakes (requested first).
`SeigManager2.restakeMulti(bytes32 layerKey, uint256 n)`

```javascript
function restakeMulti(bytes32 layerKey, uint256 n) external view returns (bool)
```

sample

## Unstake 

- Interface 
`SeigManager2.unstake(bytes32 layerKey, uint256 lton_)`

```javascript
function unstake(bytes32 layerKey, uint256 lton_) external view  
```

sample

## Withdraw 

- Interface 
`SeigManager2.withdraw(bytes32 layerKey)`

```javascript
function withdraw(bytes32 layerKey) external view  
```

sample

# Addresses on Goerli 

```javascript

```