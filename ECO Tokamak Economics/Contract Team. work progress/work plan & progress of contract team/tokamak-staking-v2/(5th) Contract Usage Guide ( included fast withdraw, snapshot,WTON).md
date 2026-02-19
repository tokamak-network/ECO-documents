# The basics concept of services 

[https://docs.google.com/presentation/d/19rKQoBhNQ2tHhfWJBRbGn2BbGcLUvWPnvfofaOyLQj0/edit#slide=id.g1ee16850fbf_0_54](https://docs.google.com/presentation/d/19rKQoBhNQ2tHhfWJBRbGn2BbGcLUvWPnvfofaOyLQj0/edit#slide=id.g1ee16850fbf_0_54)

[[Function description of TON Staking V2 (deprecated) ]] 

# Change log

- v0_1 : 2023.3.29 : initial document 
- v0_2 : 2023.4.4 : 
  - [ ](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_2_dao_committee)[[(2nd) Contract Usage Guide ]] 
  - modify createCandidate , createOptimismSequencer function 
  - modify event of CreatedCandidate
  - modify event of Staked
  - modify createCandidate function 
- v0_3 : 2023.4.21 : [ ](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_3_fast_withdraw)(current document)
  - modify  createOptimismSequencer function 
  - add provideLiquidity function 
  - add cancelRequest function
  - add finalizeFastWithdraw function
  - add event related the fast withdrawal
  - change [LibOptimism.info](http://liboptimism.info/) structure 
  - change LibStake.StakeInfo structure 
- v0_4 : 2023.4.27 : [ ](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_3_fast_withdraw)(current document)
  - add functions from #45 ~  
- **v0_5 : 2023.5.4 : **[** **](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_3_fast_withdraw)**(current document)**
  - change TON to WTON 
  - 

# Repo 

- v0_5 :  [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_7_TONtoWTON](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_7_TONtoWTON)

# ABI 

- v0_5:  [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_7_TONtoWTON/artifacts/contracts](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_7_TONtoWTON/artifacts/contracts)

# Structure 

```javascript

**library Layer2**
{

    struct **Layer2Info** {
        address layers;
        uint32 index;
    }

    struct **Layer2Holdings** {
        uint256 securityDeposit;     // ton unit
        uint256 seigs;               // ton unit
    }

}

**library LibOperator**
{
  struct **Info** {
      address operator;
      uint32 sequencerIndex;
      uint16 commission;  // denomitor 10000 , 
  }

  function getKey(
      address operator,
      uint32 sequencerIndex
  ) external pure returns (bytes32 key_) ; 

  function parseKey(bytes memory data) public pure returns (Info memory info) ;

}

**library LibOptimism**
{
    struct **Info** {
        address addressManager; 
				address l1Bridge;
        address l2Bridge;
        address l2wton;
    }

    function getKey(
        address addressManager,
				address l1Bridge,
        address l2Bridge,
        address l2wton
    ) external pure returns (bytes32 key_)  ;

    function parseKey(bytes memory data) public pure returns (Info memory info); 

    function getAddressManager(bytes memory data) public pure returns (address addr);
}

**library LibStake**
{
    struct **StakeInfo** {
        uint256 stakePrincipal; 
        uint256 stakelwton; 
        bool stake; 
    }

    struct **WithdrawalReqeust** {
        uint32 withdrawableBlockNumber;
        uint128 amount;
        bool processed;
    } 
}

**library LibFastWithdraw**
{
  using BytesParserLib for bytes;

  enum STATUS {
      NONE,
      CANCELED,
      PROVIDE_LIQUIDITY,
      NORMAL_WITHDRAWAL,
      CANCEL_WITHDRAWAL,
      FINALIZE_WITHDRAWAL,
      CALLER_NOT_L1_BRIDGE,
      ZERO_L1_BRIDGE,
      ZERO_AMOUNT,
      ZERO_REQUESTOR,
      INVALID_LAYERINDEX,
      INVALID_AMOUNT,
      PAST_DEADLINE,
      WRONG_MESSAGE,
      FAIL_FINISH_FW,
      ALREADY_PROCESSED,
      INVALID_LENGTH,
      INVALID_FUNC_SIG,
      UNSUPPORTED_VERSION
  }

  struct Request {
      address l1wton;
      address l2wton;
      address requestor;
      address fwReceipt;
      uint256 amount;
      uint16 feeRates;
      uint32 deadline;
      uint32 layerIndex;
  }
 
struct FwRequestInfo {
        uint16 feeRates;
        uint32 deadline;
        uint32 layerIndex;
    }

struct Message {
      uint8 status;
      bytes data;
      bytes liquidities;
  } 
 
struct Liquidity {
      address provider;
      uint256 amount;
      bool isCandidate;
      uint32 indexNo;
  }

  function decodeLiquidity (bytes memory data) public pure returns (Liquidity memory _liq) ;

  function encodeLiquidity (Liquidity memory _data) public pure returns (bytes memory data);

  function decodeLiquidities (bytes memory data) public pure returns (Liquidity[] memory _liquidities) ;

  function encodeLiquidities (Liquidity[] memory _datas) public pure returns (bytes memory data) ;
 
  function totalLiquidity(bytes memory data) public pure returns (uint256 amount)
	// Message.liquidities 의 모든 유동성의 합을 리턴한다. 
	
  function decodeLiquidities (bytes memory data) public pure returns (Liquidity[] memory _liquidities)  
	// Message.liquidities을 Liquidity 배열로 리턴한다. 

  function encodeLiquidities (Liquidity[] memory _datas) public pure returns (bytes memory data)
  // Liquidity 배열을 바이트로 리턴한다. 
 
```

# Storage

## SeigManagerV2

```javascript
// 스냅샷 구조체 
struct Snapshots {
        uint256[] ids;
        uint256[] values;
    }

IERC20 public ton;
address public wton;
address public dao;
address public stosDistribute;
address public seigManagerV1;
address public tot;
address public layer2Manager;
address public optimismSequencer;
address public candidate;

uint256 public seigPerBlock;
uint256 public lastSeigBlock;
uint256 public startBlock;
uint256 public indexLwton; // for staker or bonder

uint16 public ratesDao;   // divided ratesUnits
uint16 public ratesStosHolders; // divided ratesUnits
uint16 public ratesTonStakers; // divided ratesUnits
uint16 public ratesUnits; // divided uint. 10000
uint32 public minimumBlocksForUpdateSeig; // the number of block

uint256 internal _currentSnapshotId;
uint256 internal _indexLwton; // for staker
Snapshots internal _indexLwtonSnapshots;
uint32[] public snapshotTime; // 스냅샷 아이디별 스냅샷 타임. 
```

## Layer2Manager

```javascript
IERC20 public wton;
address public seigManagerV2;
address public optimismSequencer;
address public candidate;

uint256 public minimumDepositForSequencer;  // 초기 시퀀서의 최소 디파짓 금액,
uint256 public minimumDepositForCandidate;  // candidate의 최소 스테이킹 금액,

uint256 public delayBlocksForWithdraw;
uint256 public maxLayer2Count;              // 배포시 디폴트 5개로 함.

uint256 public totalSecurityDeposit; //시퀀서의 총 담보금
uint256 public totalSeigs; //아직 배분되지 않은 시퀀서를 위한 시뇨리지

//====================
uint32[] public optimismSequencerIndexes ;
mapping (uint32 => bytes32) public optimismSequencerNames;
mapping (uint32 => bytes32) public candidateNames;

mapping (uint32 => Layer2.Layer2Holdings) public holdings;

mapping (bytes32 => bool) public layerKeys;   // 이미 생성된 키는 true 로 설정 

//==================
uint32[] public candidatesIndexes ; // 길이가 총 candidate 개수
uint32 public indexSequencers ;  // 계속 증가만 함. 시퀀서 인덱스로 사용
uint32 public indexCandidates ;  // 계속 증가만 함. candidate 인덱스로 사용

uint16 public ratioSecurityDepositOfTvl; //TVL의 몇 퍼센트를 시퀀서의 최소 담보금으로 할것인가 
```

## OptimismSequencer  

```javascript
// 스냅샷 구조체 
struct Snapshots {
        uint256[] ids;
        uint256[] values;
    }

address public wton;
address public seigManagerV2;
address public layer2Manager;
address public fwReceipt;
uint256 internal _totalStakedLwton;
Snapshots internal _totalStakedLwtonSnapshot;

mapping (uint32 => uint256) public layerStakedLwton;

// layer2Index => account => StakeInfo
mapping (uint32 => mapping(address => LibStake.StakeInfo)) public layerStakes;  

// layer2Index => msg.sender => withdrawal requests (언스테이크시 등록 )
mapping (uint32 => mapping (address => LibStake.WithdrawalReqeust[])) public withdrawalRequests;

// layer2Index => msg.sender => index
mapping (uint32 => mapping (address => uint256)) public withdrawalRequestIndex;

// pending unstaked amount
// layer2Index => msg.sender => ton amount
mapping (uint32 => mapping (address => uint256)) public pendingUnstaked;

// layer2Index => ton amount
mapping (uint32 => uint256) public pendingUnstakedLayer2;

// msg.sender =>  ton amount
mapping (address => uint256) public pendingUnstakedAccount;

// layer2Index - info
mapping (uint32 => bytes) public layerInfo;

address[] public stakeAccountList; 
```

## Candidate  

```javascript
// 스냅샷 구조체 
struct Snapshots {
        uint256[] ids;
        uint256[] values;
    }

address public wton;
address public seigManagerV2;
address public layer2Manager;
address public fwReceipt;
uint256 internal _totalStakedLwton;
Snapshots internal _totalStakedLwtonSnapshot;

mapping (uint32 => uint256) public layerStakedLwton;

// layer2Index => account => StakeInfo
mapping (uint32 => mapping(address => LibStake.StakeInfo)) public layerStakes;  

// layer2Index => msg.sender => withdrawal requests (언스테이크시 등록 )
mapping (uint32 => mapping (address => LibStake.WithdrawalReqeust[])) public withdrawalRequests;

// layer2Index => msg.sender => index
mapping (uint32 => mapping (address => uint256)) public withdrawalRequestIndex;

// pending unstaked amount
// layer2Index => msg.sender => ton amount
mapping (uint32 => mapping (address => uint256)) public pendingUnstaked;

// layer2Index => ton amount
mapping (uint32 => uint256) public pendingUnstakedLayer2;

// msg.sender =>  ton amount
mapping (address => uint256) public pendingUnstakedAccount;

// layer2Index - info
mapping (uint32 => bytes) public layerInfo;

address[] public stakeAccountList; 

// layerIndex - candidator - candidateIndex
mapping (uint32 => mapping(address => uint32)) public operators;
```

# Events

- SeigManagerV2

```javascript
event Snapshot(uint256 id, uint256 snapshotTime);

event UpdatedSeigniorage(
                uint256 lastSeigBlock_,
                uint256 increaseSeig_,
                uint256 totalSupplyOfTon_,
                uint256[4] amount_,
                uint256 prevIndex_,
                uint256 index_
                );

**** amount[4] -> [amountOfstaker, amountOfsequencer, amountOfDao, amountOfStosHolders]
**
event Claimed(address caller, address to, uint256 amount);
```

- Layer2Manager 

```javascript
event Claimed(uint32 _index, address _sequencer, uint256 amount);

event CreatedOptimismSequencer(uint32 _index, address _sequencer, bytes32 _name, address addressManager, address l1Messenger, address l1Bridge, address l2ston, uint256 depositAmount);

event CreatedCandidate(uint32 _index, address _operator, bytes32 _name, uint32 _sequencerIndex, uint16 _commission, uint256 depositAmount);

event Distributed(uint256 _totalSeigs, uint256 _distributedAmount);


event IncreasedSecurityDeposit(uint32 _index, address caller, uint256 amount);
event DecreasedSecurityDeposit(uint32 _index, address _sequencer, uint256 amount);
```

- OptimismSequencer , Candidate 

```javascript
event Staked(uint32 _index, address sender, uint256 amount, uint256 lwton, address commissionTo, uint16 commission);

event Unstaked(uint32 _index, address sender, uint256 amount, uint256 lwton);

event Restaked(uint32 _index, address sender, uint256 amount, uint256 lwton);

event Withdrawal(uint32 _index, address sender, uint256 amount);

event FastWithdrawalClaim(bytes32 fwHashMessage, uint32 layerIndex, address from, address to, uint256 amount);
=>  L1에서 from주소가 유동성을 제공할때, 제공한 금액만큼 from 스테이킹 금액에서 to(L2 요첮자)에게 출금을 해줍니다. 이때 발생되는 이벤트 입니다.이 함수는 FwReceipt 컨트랙에 의해서만 호출됩니다. 

event FastWithdrawalStaked(bytes32 fwHashMessage, uint32 layerIndex, address staker, uint256 amount, uint256 lwton)
=> FastWithdrawalStaked : L1에서 유동성이 제공된후, DTD 이후 정산할때, L1 유동성 제공자(staker)에게 수수료로 받아야 할 금액(amount)을 자동 스테이킹(lton) 해줍니다. 이 때 발생되는 이벤트 입니다. 이 함수는 FwReceipt 컨트랙에 의해서만 호출됩니다. 

```

- FwReceipt

```javascript
event ProvidedLiquidity(bytes32 fwHashMessage, address provider, uint256 provideAmount, uint256 feeAmount, bool isCandidate, uint32 indexNo);
=> 빠른 출금에 유동성 제공시 발생되는 이벤트 입니다. 

event CanceledRequest(bytes32 fwHashMessage, address caller);
=> 빠른 출금 요청을 요청자가 직접 취소할때 발생하는 이벤트 입니다. 
  
event NormalWithdrawal(bytes32 fwHashMessage, address from, address to, uint256 amount, uint8 status);
=> DTD이후, 유동성 제공자가 없어, 요청자가 일반출금한 경우 발생되는 이벤트입니다. 

event FinalizedFastWithdrawal(bytes32 fwHashMessage, address from, address to, uint256 providedAmount, uint256 feeAmount, bool isCandidate, uint32 indexNo);
=> DTD이후, 빠른 출금이 정산될 때 발생하는 이벤트입니다. 
    
```

# Functions 

## F1. Create Sequencer ( Optimism Sequencer)  

- contract : Layer2Manager
- Interface 
```javascript
function createOptimismSequencer(
        bytes32 _name,
        address addressManager, 
				address l1Bridge,
        address l2Bridge,
        address l2wton,
				uint256 depositAmount
    )
        external
```
- sample   
```javascript
const receipt = await(
	deployed.layer2Manager.connect(sequencer1).createOptimismSequencer(
                    ethers.utils.formatBytes32String(name),
                    deployed.addressManager.address, 
										deployed.l1Bridge.address, 
										deployed.l2Bridge.address, 
                    deployed.l2wton.address,
										depositAmount
                )).wait();
```
- comments 
  - You should approve the depositAmount of WTON to Layer2Manager.
  - The depositAmount is changed according to layer2 TVL. 
**depositAmount** ≥ 

### Query ratioSecurityDepositOfTvl  

- contract : Layer2Manager
- interface :
```javascript
function ratioSecurityDepositOfTvl() public returns (uint26)

result value is used by divided 10000.
ex ) 500 -> 500 / 10000 = 0.05 
```

### Query minimumSecurityDepositAmount  

- contract : Layer2Manager
- interface :
```javascript
function minimumSecurityDepositAmount(address l1Bridge, address l2wton) public view returns (uint256 amount)
```

## F2. Query all Sequencers  

- contract : Layer2Manager
- Interface
```javascript
function getAllLayers()
        external view
        returns (
            bytes32[] memory optimismSequencerNames_,
            uint32[] memory optimismSequencerIndexes_,
            Layer2.Layer2Holdings[] memory holdings_,
            bytes[] memory infos_
            )

** bytes's format of **info (one of infos_) **: 
**info** = abi.encodePacked(addressManager, l1Bridge, l2Bridge, l2wton) 

**info **is composed of 8**0 bytes (addressManager address)| 20 bytes (**l1Bridge** address)| 20 bytes (**l2Bridge** address) | 20 bytes (l2wton address)** , it is 80 bytes.
```
- sample  
```javascript
let getAllLayersAfter = await deployed.layer2Manager.getAllLayers();
```

## F3. Create Candiate 

- contract : Layer2Manager
- Interface
```javascript
function createCandidate(
        uint32 _sequenceIndex,
        bytes32 _name,
				uint16 _commission,
				uint256 stakeAmount
    )
```
- sample 
```javascript
const receipt = await(deployed.layer2Manager.connect(addr1).createCandidate(
                sequenceIndex,
                ethers.utils.formatBytes32String(name),
								commission,
								stakeAmount
            )).wait();
```
- comments 
  - You should approve the stakeAmount of WTON.
    - stakeAmount ≥ minimumDepositForCandidate
  - You will stake the stakeAmount of WTON through createCandidate function. 

### Query minimumDepositForCandidate  

- contract : Layer2Manager
- interface :
```javascript
function minimumDepositForCandidate() public view returns (uint256 amount)
```

## F4. Query all Candidates   

- contract : Layer2Manager
- Interface
```javascript
function getAllCandidates()
        external view
        returns (
            bytes32[] memory candidateNames_,
            uint32[] memory candidateNamesIndexes_,
            bytes[] memory infos_
            )

** bytes's format of **info (one of infos_) **: 
**info** = abi.encodePacked(operator, sequencerIndex, commission) 
 
**info **is composed of **20 bytes (operator address) | 4 bytes (**sequencerIndex**) | 2 bytes (**commission), it is 26 bytes.

**commission** is used by multiplying 10000.
ex) 0.5% -> 0.005 => commission : 50 , we should use it like 50 / 10000 = 0.005 .
```
- sample 
[sample](https://github.com/tokamak-network/tokamak-staking-v2/blob/99872bc2245be20026c98832c5a0471cfa1838ff/test/4.IntegratedTest.spec.ts#L312)

```javascript
let getAllCandidatesAfter = await deployed.layer2Manager.getAllCandidates();
```

## F5. View Sequencers’s info  

- contract : OptimismSequencer
- Interface
```javascript
function layerInfo(uint32 layerIndex) public returns (bytes) 

Retuen bytes is same to F2's info.
```

## F6. View Candidate’s info  

- contract : Candidate
- Interface
```javascript
function layerInfo(uint32 layerIndex) public returns (bytes) 

Retuen bytes is same to F4's info.
```

## F7. Check if the Sequencer is already registered 

- contract : Layer2Manager
- Interface
```javascript
function existedLayer2Index(uint32 _index) external view returns (bool exist_) 
```
- contract : OptimismSequencer
- Interface
```javascript
function layerInfo(uint32 _index) external view returns (bool bytes) 

if returnbytes's length is 0, it is not existed .

```

## F8. Check if the Candidate is already registered 

- contract : Layer2Manager
- Interface
```javascript
function existedLayer2Index(uint32 _index) external view returns (bool exist_) 


```
- contract : Candidate
- Interface
```javascript
function layerInfo(uint32 _index) external view returns (bool bytes) 

if returnbytes's length is 0, it is not existed .

```

## F9. The total staked amount ( sequencer  + candidate )  

- contract : SeigManager
- Interface
```javascript
function getTotalLwton() public view returns (uint256 amount)
```

## F10. The total staked amount of Sequencer  

- contract : OptimismSequencer
- Interface
```javascript
function getTotalLwton() public view returns (uint256 amount)
```

## F11. The total staked amount of Candidate  

- contract : Candidate
- Interface
```javascript
function getTotalLwton() public view returns (uint256 amount)
```

## F12. The staked amount of special sequencer  

- contract : OptimismSequencer
- Interface
```javascript
function balanceOfLwton(uint32 _index) public view returns (uint256 amount)
```

## F13. The staked amount of special candidate

- contract : Candidate
- Interface
```javascript
function balanceOfLwton(uint32 _index) public view returns (uint256 amount)
```

## F14. The staked amount of special sequencer's account

- contract : OptimismSequencer
- Interface
```javascript
function balanceOfLwton(uint32 _index, address account) public view returns (uint256 amount)
```

## F15. The staked amount of special candidate's account

- contract : Candidate
- Interface
```javascript
function balanceOfLwton(uint32 _index, address account) public view returns (uint256 amount)
```

## F16. Total pending amount  by unstaking on a specific sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function pendingUnstakedLayer2(uint32 _index) public view returns (uint256 amount)
```

## F17. Total pending amount  by unstaking on a specific candidate 

- contract : Candidate
- Interface
```javascript
function pendingUnstakedLayer2(uint32 _index) public view returns (uint256 amount)
```

## F18. Total pending amount  by unstaking on a specific sequencer’s account 

- contract : OptimismSequencer
- Interface
```javascript
function getPendingUnstakedAmount(uint32 _index, address account) public view returns (uint256)
```

## F19. Total pending amount  by unstaking on a specific candidate’s account

- contract : Candidate
- Interface
```javascript
function getPendingUnstakedAmount(uint32 _index, address account) public view returns (uint256)
```

## F20. Total pending amount of account on sequencer

- contract : OptimismSequencer
- Interface
```javascript
function pendingUnstakedAccount(address account) public view returns (uint256)
```

## F21. Total pending amount of account on candidate

- contract : Candidate
- Interface
```javascript
function pendingUnstakedAccount(address account) public view returns (uint256)
```

## F22. Query accounts that have staked on a specific sequencer

- contract : OptimismSequencer
- Interface
```javascript
function getStakeAccountList() public view returns (address[] memory)
```

## F23. Query accounts that have staked on a specific candidate

- contract : Candidate
- Interface
```javascript
function getStakeAccountList() public view returns (address[] memory)
```

## F24. Query accounts that have staked on a specific candidate

- contract : Candidate
- Interface
```javascript
function getStakeAccountList() public view returns (address[] memory)
```

## F25. Update Seigniorage

- Execute update seigniorage (immediate interest payment) 
  - contract : SeigManager2
  - Interface 
`SeigManager2.runUpdateSeigniorage()`

```javascript
function runUpdateSeigniorage() public  returns (bool res)
```

sample
- We can know the amount that can be issued when seignorage is executed
  - contract : SeigManager2
  - Interface 
`SeigManager2.mintableSeigsAmount()`

```javascript
function mintableSeigsAmount() external view returns (uint256 amount)
```

 

## F26. Query the seigniorage amount to distribute to sequencers

- contract : Layer2Manager
- Interface
```javascript
function totalSeigs() public view returns (address[] memory)
```

## F27. Distribute the seigniorage amount to sequencers

- contract : Layer2Manager
- Interface
```javascript
function distribute() external 
```

## F28. Query the sequencer's seignorage query

- contract : Layer2Manager
- Interface
```javascript
function layerHoldings(uint32 layerKey_) external view returns (**Layer2.Layer2Holdings** memory)


 struct **Layer2Holdings** {
        uint256 securityDeposit;     // ton unit
**        uint256 seigs;               // this is seignorage of sequencer 
**    }
```

## F29. Claim to the sequencer's seignorage  

- contract : Layer2Manager
- Interface
```javascript
unction claim(uint32 layerIndex) external
```

## F30. Stake to the special sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function stake(uint32 layerIndex, uint256 amount) public 
```

## F31. Stake to the special candidate 

- When a non-operator account stakes, the commission rate is staked to the operator.
- contract : Candidate
- Interface
```javascript
function stake(uint32 candidateIndex, uint256 amount) public 
```

## F32. Unstake to the special sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function unstake(uint32 _index, uint256 lwton_) external
```

## F33. Unstake to the special candidate 

- contract : Candidate
- Interface
```javascript
function unstake(uint32 _index, uint256 lwton_) external
```

## F34. Re-stake to the special sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function restake(uint32 _index) public
```

## F35. Re-stake to the special candidate 

- contract : Candidate
- Interface
```javascript
function restake(uint32 _index) public
```

## F36. Multi-restake to the special sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function restakeMulti(uint32 _index, uint256 n) public
```

## F37. Multi-restake to the special candidate 

- contract : Candidate
- Interface
```javascript
function restakeMulti(uint32 _index, uint256 n) public
```

## F38. Withdraw to the special sequencer 

- contract : OptimismSequencer
- Interface
```javascript
function withdraw(uint32 _index) public
```

## F39. Withdraw to the special candidate 

- contract : Candidate
- Interface
```javascript
function withdraw(uint32 _index) public
```

## F40. Provide the liquidity to fast-withdraw request in special sequencer/candidate   

- contract : FwReceipt
- Interface
```javascript
function provideLiquidity(
        address requestor,
        uint256 requestAmount, 
        uint256 provideAmount,
        uint32 deadline,
        bool isCandidate,
        uint32 indexNo,
        uint16 feeRate,
        uint32 layerIndex, 
        uint256 messageNonce,
        bytes32 hashMessage
        )
        external

- requestAmount: fast withdrawal request amount
- isCandidate : if sequencer, it is false, if candidate, it's true.  
- indexNo :  sequencerIndex or candidateIndex 
- layerIndex : SequencerIndex for fast withdrawal request
- messageNonce : Message nonce used when requesting fast withdrawal in L2
- hashMessage : Message hash value requested for fast withdrawal from L2
```

  - hashMessage 

```javascript

encodedRelayMessage = abi.encodeWithSignature(
                "relayMessage(address,address,bytes,uint256)",
                _target,  // L1 bridge address 
                _sender,  // L2 bridge address 
                _message,  // 
                _messageNonce  //              
)

hashMessage = keccak256(encodedRelayMessage) 

_message = abi.encodeWithSignature(
                "finalizeERC20Withdrawal(address,address,address,address,uint256,bytes)",
                wton,     // L1 wton address
                _layerInfo.l2wton, // L2 wton address
                requestor,   // 
                FwReceiptContractAddress, // L1 FwReceipt Contract address
                amount,  // request amount 
                abi.encodePacked(feeRate, deadline, layerIndex)
            )
```

## F41. Cancel the fast-withdraw request  

- contract : FwReceipt
- Interface
```javascript
function cancelRequest(
        address requestor,
        uint256 requestAmount,
        uint32 deadline,
        uint16 feeRate,
        uint32 layerIndex,
        uint256 messageNonce,
        bytes32 hashMessage) external


-  parameter details : same as [F40] 
```

## F42. L2: Request The Fast Withdraw  

- contract : L2Bridge 
- Interface
```javascript
function withdrawTo(
        address _l2Token,
        address _to,
        uint256 _amount,
        uint32 _l1Gas,
        bytes calldata _data
    ) external
 
- _l2Token : L2 ton token 
- to : L1's fwReceiptContract address 
- amount : 
- l1Gas : 
- data : abi.encodePacked(feeRate, deadline, layerIndex) 
```

## F43. How to check whether L2 request is executed or not in L1.  

- contract : L1CrossDomainMessenger 
- Interface
```javascript
function successfulMessages(bytes32 hashMessage) external view returns (bool)
```

  - hashMessage : 
```javascript

encodedRelayMessage = abi.encodeWithSignature(
                "relayMessage(address,address,bytes,uint256)",
                _target,  // L1 bridge address 
                _sender,  // L2 bridge address 
                _message,  // 
                _messageNonce  //              
)

hashMessage = keccak256(encodedRelayMessage) 

_message = abi.encodeWithSignature(
                "finalizeERC20Withdrawal(address,address,address,address,uint256,bytes)",
                wton,     // L1 wton address
                _layerInfo.l2wton, // L2 wton address
                requestor,   // 
                FwReceiptContractAddress, // L1 FwReceipt Contract address
                amount,  // request amount 
                abi.encodePacked(feeRate, deadline, layerIndex)
            )
```

## F44. After DTD,  finalize fast withdraw in L1 

- contract : FwReceipt 
- Interface
```javascript
function finalizeFastWithdraw(
        address requestor,
        uint256 requestAmount,
        uint32 deadline,
        uint16 feeRate,
        uint32 layerIndex,
        uint256 messageNonce,
        bytes32 hashMessage
        )
        external returns (uint8 status)


-  parameter details : same as [F40] 
```

  - status
```javascript
enum STATUS {
      NONE,
      CANCELED,
      PROVIDE_LIQUIDITY,
      NORMAL_WITHDRAWAL,
      CANCEL_WITHDRAWAL,
      FINALIZE_WITHDRAWAL,
      CALLER_NOT_L1_BRIDGE,
      ZERO_L1_BRIDGE,
      ZERO_AMOUNT,
      ZERO_REQUESTOR,
      INVALID_LAYERINDEX,
      INVALID_AMOUNT,
      PAST_DEADLINE,
      WRONG_MESSAGE,
      FAIL_FINISH_FW,
      ALREADY_PROCESSED,
      INVALID_LENGTH,
      INVALID_FUNC_SIG,
      UNSUPPORTED_VERSION
    }
```

## F45. Snapshot 

- contract : SeigManagerV2 
- Interface
```javascript
function snapshot() external virtual returns (uint256)
```

## F46. Current snapshot Id 

- contract : SeigManagerV2 
- Interface
```javascript
function getCurrentSnapshotId() public view virtual returns (uint256)
```

## F47. Get snapshot time 

- contract : SeigManagerV2 
- Interface
```javascript
function getSnapshotTime() public view returns (uint32[] memory)
```

## F48. Get indexLwton 

- contract : SeigManagerV2 
- Interface
```javascript
function indexLwton() public view returns (uint256)
```

## F49. Get indexLwton at a specific snapshot Id 

- contract : SeigManagerV2 
- Interface
```javascript
function indexLtonAt(uint256 snapshotId) public view returns (uint256)
```

## F50. Convert  WTON amount to LWTON

- contract : SeigManagerV2 
- Interface
```javascript
function getWtonToLwton(uint256 _amount) public view returns (uint256 amount)
```

## F51.  Convert  WTON amount to LWTON at a specific snapshot Id 

- contract : SeigManagerV2 
- Interface
```javascript
function getWtonToLwtonAt(uint256 _amount, uint256 _snapshotId) public view returns (uint256 amount)
```

## F52. Convert  LWTON amount to WTON

- contract : SeigManagerV2 
- Interface
```javascript
function getLwtonToWton(uint256 lwton) public view returns (uint256 amount)
```

## F53. Convert  LWTON amount to WTON at a specific snapshot Id 

- contract : SeigManagerV2 
- Interface
```javascript
function getLwtonToWtonAt(uint256 lwton, uint256 _snapshotId) public view returns (uint256 amount)
```

## F54. Get totalLwton amount of staked  

- contract : SeigManagerV2 
- Interface
```javascript
 function getTotalLwton() public view returns (uint256 amount)
```

## F55. Get  totalLwton amount of staked  at a specific snapshot Id

- contract : SeigManagerV2 
- Interface
```javascript
function getTotalLwtonAt(uint256 _snapshotId) public view returns (uint256 amount)
```

## F56. Get total staked Lwton of sequencers   

- contract : OptimismSequencer 
- Interface
```javascript
 function totalStakedLwton() public view returns (uint256 amount)
```

## F57. Get  total staked Lwton of sequencers  at a specific snapshot Id

- contract : OptimismSequencer 
- Interface
```javascript
function totalStakedLwtonAt(uint256 snapshotId) public view returns (uint256 amount)
```

## F58. The staked Lwton amount of special sequencer  at a specific snapshot Id

- contract : OptimismSequencer
- Interface
```javascript
function balanceOfLwtonAt(uint32 _index, uint256 snapshotId) public view returns (uint256 amount)
```

## F59. The staked Lwton amount of special candidate  at a specific snapshot Id

- contract : Candidate
- Interface
```javascript
function balanceOfLwtonAt(uint32 _index, uint256 snapshotId) public view returns (uint256 amount)
```

## F60. The staked Lwton amount of special sequencer's account at a specific snapshot Id

- contract : OptimismSequencer
- Interface
```javascript
function balanceOfLwtonAt(uint32 _index, address account, uint256 snapshotId) public view returns (uint256 amount)
```

## F61. The staked Lwton amount of special candidate's account at a specific snapshot Id

- contract : Candidate
- Interface
```javascript
function balanceOfLwtonAt(uint32 _index, address account, uint256 snapshotId) public view returns (uint256 amount)
```

## F62. The staked WTON amount of special sequencer's account  

- contract : OptimismSequencer
- Interface
```javascript
function balanceOf(uint32 _index, address account) public view returns (uint256 amount)
```

## F63. The staked WTON amount of special sequencer's account at a specific snapshot Id

- contract : OptimismSequencer
- Interface
```javascript
function balanceOfAt(uint32 _index, address account, uint256 snapshotId) public view returns (uint256 amount)
```

## F64. The staked WTON amount of special candidate's account  

- contract : Candidate
- Interface
```javascript
function balanceOf(uint32 _index, address account) public view returns (uint256 amount)
```

## F65. The staked WTON amount of special candidate's account at a specific snapshot Id

- contract : Candidate
- Interface
```javascript
function balanceOfAt(uint32 _index, address account, uint256 snapshotId) public view returns (uint256 amount)
```

# Addresses on Goerli 

```javascript

```