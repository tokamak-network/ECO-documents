We offer Layer2Candidate Layer and have to provide the seigniorage to L2 sequencer in Simple Staking Service.

# ABI

- SeigManagerV1 : [https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/test/abi/SeigManagerV1.json](https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/test/abi/SeigManagerV1.json)
- Layer2Manager : [https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/artifacts/contracts/layer2/Layer2ManagerV1_1.sol/Layer2ManagerV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/artifacts/contracts/layer2/Layer2ManagerV1_1.sol/Layer2ManagerV1_1.json)
- Layer2Candidate : [https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/artifacts/contracts/dao/Layer2CandidateV1_1.sol/Layer2CandidateV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/artifacts/contracts/dao/Layer2CandidateV1_1.sol/Layer2CandidateV1_1.json)

# Interface for service 

## Register the Layer2Candidate   

- Contract:  **Layer2Manager**
- Function: 
  - method 1: [sample link](https://github.com/tokamak-network/ton-staking-v2/blob/5ea462bf9f0e260527851d6e85b343dc40f92790/test/layer2/units/2.Layer2Manager.mainnet.test.ts#L617-L630)
    - you have to approve ton before executing the below function.
    - amount is greater than Layer2Manager.minimumInitialDepositAmount()

```solidity
/// @notice Register the Layer2Candidate
/// @param systemConfig     systemConfig's address
/// @param amount           transfered amount
/// @param flagTon          if true, amount is ton, otherwise it it wton
/// @param memo             layer's name
function registerLayer2Candidate(
        address systemConfig,
        uint256 amount,
        bool flagTon,
        string calldata memo
    )
        external
```
  - method 2: 
    - ton.approveAndCall  또는 wton.approveAndCall 을 이용할 수 있음. Layer2Manager 컨트랙의 아래 함수를 호출함. 
    - amount is greater than Layer2Manager.minimumInitialDepositAmount()

```solidity
/// @notice ERC20 Approve callback
/// @param owner    Account that called approveAndCall
/// @param spender  OnApprove function contract address
/// @param amount   Approved amount
/// @param data     Data used in OnApprove contract
function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool) 
    
    
    - data : 20 bytes (systemConfig 주소) + memo bytes  
```
- Event:
  - Layer2Manager 
```solidity
/**
 * Occurs when registering Layer2Candidate
 * @param systemConfig      the systemConfig address
 * @param wtonAmount        the wton amount depositing when registering Layer2Canddiate
 * @param memo              the name of Layer2Canddiate
 * @param operator          a opperator contract address
 * @param layer2Candidate   a layer2Candidate address
 */
event RegisteredLayer2Candidate(address systemConfig, uint256 wtonAmount, string memo, address operator, address layer2Candidate);
```
  - L2Registry 
```solidity
 /**
 * Occurs when registering SystemConfig
 * @param systemConfig  the systemConfig address
 * @param type_         0: none, 1: legacy, 2: bedrock with nativeTON
 */
event RegisteredSystemConfig(address systemConfig, uint8 type_);
```
- 

## Deposit 

- same as previously version.

## RequestWithdraw 

- same as previously version.

## ProcessWithdraw 

- same as previously version.

## UpdateSeigniorage

- Contract: **Layer2Candidate**
- Function:
  - If you are an operator, you can choose among the claim, the staking, and no options.
  - If you are not an operator, it will execute with no option though you choose the particular option.

```solidity
/// @param afterCall 0: none, 1: claim, 2: staking
function updateSeigniorage(uint256 afterCall) public returns (bool)  

```

  - How to check if you are the sequencer for a specific Layer2Candidate 
```javascript

OperatorContract address = Layer2Contract.operator()

/// If it is true, account is an operator who receives the seigniorage assigned to the L2 sequencer  
OperatorContract.isOperator(account) 

/// If it is not address(0), it is Layer2Candidate 
OperatorContract.systemConfig()  

```
- Event:
  - SeigManager Contract 안에서 발생되는 이벤트임  
  - **deleted SeigGiven event**
  - **added SeigGiven2 event**
    - l2TotalSeigs : 모든 L2 sequencer 에게 할당된 시뇨리지 
    - layer2Seigs : 현재 실행되고 있는 레이어의 시뇨리지에게 정산된 시뇨리지 

```javascript
event AddedSeigAtLayer(address layer2, uint256 seigs, uint256 operatorSeigs, uint256 nextTotalSupply, uint256 prevTotalSupply);

event SeigGiven2(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig, uint256 l2TotalSeigs, uint256 layer2Seigs);
```

## WithdrawAndDepositL2 

-  Contract: **DepositManager** 
- Function:
```javascript
 /**
   * @dev withdrawAndDepositL2 `amount` WTON in RAY
   */
  function withdrawAndDepositL2(address layer2, uint256 amount) external returns (bool)  
  
```
- Event:
```solidity
event WithdrawalAndDeposited(address indexed layer2, address account, uint256 amount);
```

# How to determine which layer has stopped issuing L2 sequencer seigniorage

- Contract: **Layer2Manager**
- Function :  If systemConfigInfo(systemConfig).**stateIssue is 2, this layer has stopped the l2 sequencer seigniorage.  **
> [!tip]
> 💡 In the layer with “systemConfigInfo(systemConfig).stateIssue is 2”, the operator cannot use the claiming and staking functions when performing update seigniorage.
That layer cannot execute the withdrawAndDepositL2 function.

```javascript
function systemConfigInfo(address systemConfig) external view returns (SystemConfigInfo) 


struct SystemConfigInfo {
    uint8 **stateIssue**; // status for giving seigniorage ( 0: none, 1: registered, 2: paused )
    address operator;
}
```

# Stop giving L2 sequencer seigniorage   

 [ton-staking-v2/docs/en/ton-staking-v2.md at codeReview · tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/docs/en/ton-staking-v2.md#for-seignioragecommittee)

- Contract: **L2Registry** 
- Function:
  - **rejectLayer2Candidate(address _systemConfig)** external <u>**onlySeigniorageCommittee**</u>()
```
/**
 * @notice Stop issuing seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function rejectLayer2Candidate(
    address _systemConfig
)  external onlySeigniorageCommittee()
```
- Event
  - L2Registry 

```javascript
/**
 * @notice  Event occurs when onlySeigniorageCommittee stops issuing seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param   _systemConfig  the systemConfig address
 */
event RejectedLayer2Candidate(address _systemConfig);

```

  - SeigManager

```javascript
/**
 * @notice Event that occurs when calling excludeFromSeigniorage function
 * @param layer2        the layer2 address
 * @param layer2Tvl     the layer2 TON TVL
 * @param initialDebt   the layer2 initial debt for calculating a reward
 */
event ExcludedFromSeigniorage(address layer2, uint256 layer2Tvl, uint256 initialDebt);

```
- Other View Functions 
  - seigniorageCommittee()  : query the seigniorageCommittee address
```javascript
function seigniorageCommittee() external returns (address)
```
  - If the value of <u>rejectSystemConfig(_systemConfig) is true</u>, that Layer2 <u>has stopped providing the seigniorage to l2sequencer</u>.
```javascript
function rejectSystemConfig(address _systemConfig) external returns (bool) 
```

# **Cancel stopping distributing a seigniorage to the L2 sequencer**

- Contract: **L2Registry** 
- Function:
  - **restoreLayer2Candidate(address _systemConfig)** external <u>**onlySeigniorageCommittee**</u>()
```
/**
     * Restore cancel stoping seigniorage to the layer 2 sequencer of a specific systemConfig.
     * @param _systemConfig the systemConfig address
     */
    function restoreLayer2Candidate(
        address _systemConfig
    )  external onlySeigniorageCommittee() 
```