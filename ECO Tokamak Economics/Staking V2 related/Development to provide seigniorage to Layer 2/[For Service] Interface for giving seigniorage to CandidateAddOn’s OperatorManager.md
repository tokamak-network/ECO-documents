We offer CandidateAddOn’s OperatorManager and have to provide the seigniorage to L2 sequencer(OperatorManager) in Simple Staking Service.

# ABI

ABI Folder : [https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5/artifacts/contracts](https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5/artifacts/contracts)

- SeigManagerV1 : [https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/test/abi/SeigManagerV1.json](https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/test/abi/SeigManagerV1.json)
- Layer2Manager : [https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/Layer2ManagerV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/Layer2ManagerV1_1.json)
- CandidateAddOn: [https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/artifacts/contracts/dao/CandidateAddOnV1_1.sol/CandidateAddOnV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/artifacts/contracts/dao/CandidateAddOnV1_1.sol/CandidateAddOnV1_1.json)
- OperatorManager : [https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/artifacts/contracts/layer2/OperatorManagerV1_1.sol/OperatorManagerV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/staking-v2.5/artifacts/contracts/layer2/OperatorManagerV1_1.sol/OperatorManagerV1_1.json)

# Interface for service 

## Register the CandidateAddOn   

- Contract:  **Layer2Manager **
- Function: 
  - method 1: [sample link](https://github.com/tokamak-network/ton-staking-v2/blob/d0220ab297aeae276f5160a5f3aa236ea2b3cb4e/test/layer2/units/3.Layer2Manager.sepolia.test.ts#L738-L760)
    - you have to approve ton before executing the below function.
    - amount is greater than Layer2Manager.minimumInitialDepositAmount()

```solidity
/**
* @notice Register the CandidateAddOn
* @param rollupConfig     rollupConfig's address
* @param amount           transferred amount
* @param flagTon          if true, amount is ton, otherwise it wton
* @param memo             layer's name
*/
function registerCandidateAddOn(
	address rollupConfig,
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
* @notice Event occurs when registering CandidateAddOn
* @param rollupConfig      the rollupConfig address
* @param wtonAmount        the wton amount depositing when registering CandidateAddOn
* @param memo              the name of CandidateAddOn
* @param operator          an operatorManager contract address
* @param candidateAddOn    a candidateAddOn address
*/
event RegisteredCandidateAddOn(address rollupConfig, uint256 wtonAmount, string memo, address operator, address candidateAddOn);

```
  - L1BridgeRegistry 
```solidity
/**
 * @notice  Event occurs when registering rollupConfig
 * @param   rollupConfig      the rollupConfig address
 * @param   type_         0: none, 1: legacy, 2: bedrock with nativeTON
 * @param   l2TON        the L2 TON address
 * @param   name         the candidate name
 */
event RegisteredRollupConfig(address rollupConfig, uint8 type_, address l2TON, string name);
```

## Deposit 

- same as previously version.

## RequestWithdraw 

- same as previously version.

## ProcessWithdraw 

- same as previously version.

## UpdateSeigniorage

- same as previously version
- Event:
  - SeigManager Contract 안에서 발생되는 이벤트임  
  - **deleted SeigGiven event**
  - **added SeigGiven2 event**
    - l2TotalSeigs : 모든 L2 sequencer 에게 할당된 시뇨리지 
    - layer2Seigs : 현재 실행되고 있는 레이어의 OperatorManager 에게 정산되는 시뇨리지 

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
- Function:  If rollupConfigInfo(rollupConfig).status** is 2, this layer has stopped the l2 sequencer seigniorage.  **
> [!tip]
> 💡 In the layer with “rollupConfigInfo(rollupConfig).status is 2”,  that layer cannot execute the withdrawAndDepositL2 function.

```javascript
function rollupConfigInfo(address rollupConfig) external view returns (SeqSeigStatus) 

struct SeqSeigStatus {
    uint8 status; /// status for giving seigniorage
                  /// (0:none, 1:registered, 2: paused )
    address operatorManager;
}

```

# Stop giving L2 sequencer seigniorage   

 [ton-staking-v2/docs/en/ton-staking-v2.md at codeReview · tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/docs/en/ton-staking-v2.md#for-seignioragecommittee)

- Contract: **L1BridgeRegistry** 
- Function:
  - **rejectCandidateAddOn(address rollupConfig)** external <u>**onlySeigniorageCommittee**</u>
```
/**
 * @notice Stop issuing seigniorage to the layer 2 sequencer of a specific rollupConfig.
 * @param rollupConfig the rollupConfig address
 */
function rejectCandidateAddOn(
    address rollupConfig
)  external onlySeigniorageCommittee()
```
- Event
  - **L1BridgeRegistry** 

```javascript

**/**
* @notice  Event occurs when onlySeigniorageCommittee stops issuing seigniora ge
*          to the layer 2 sequencer of a specific rollupConfig.
* @param   rollupConfig  the rollupConfig address
*/**
**event RejectedCandidateAddOn(address rollupConfig);
**

```

  - SeigManager

```javascript
/**
 * @notice Event that occurs when calling excludeFromSeigniorage function
 * @param layer2        the layer2(candidate) address
 * @param layer2Tvl     the layer2 TON TVL
 * @param initialDebt   the layer2 initial debt for calculating a reward
 */
event ExcludedFromL2Seigniorage(address layer2);

```
- Other View Functions 
  - seigniorageCommittee() : query the seigniorageCommittee address
```javascript
function seigniorageCommittee() external returns (address)
```
  - If the value of <u>rejectSystemConfig(rollupConfig) is true, that candidate(Layer2) has stopped providing the seigniorage to l2sequencer</u>.
```javascript
function rejectRollupConfig(address rollupConfig) external returns (bool) 
```

# **Cancel stopping distributing a seigniorage to the L2 sequencer**

- Contract: **L1BridgeRegistry** 
- Function:
  - **restoreCandidateAddOn(address **rollupConfig**)** external <u>**onlySeigniorageCommittee**</u>
```
**
****/**
 * Start to issue seigniorage to the layer 2 sequencer of a specific rollupConfig from now on.
 * @param rollupConfig          the rollupConfig address
 * @param rejectedL2Deposit     if it is true, allow the withdrawDepositL2 function.
 */****
function ****restoreCandidateAddOn****(
    address rollupConfig,
    bool rejectedL2Deposit
) external onlySeigniorageCommittee**
```
- Event
  - **L1BridgeRegistry** 

```javascript

**/**
 * @notice  Event occurs when onlySeigniorageCommittee cancels stopping issuing seigniorage
 *          to the layer 2 sequencer of a specific rollupConfig.
 * @param   rollupConfig  the rollupConfig address
 */
event ****RestoredCandidateAddOn****(address rollupConfig);**


```

  - SeigManager

```javascript
 
/**
 * @notice Event that occurs when calling includeFromL2Seigniorage function
 * @param layer2        the layer2 address
 */
event IncludedFromL2Seigniorage(address layer2);


```

## Redeploy Contracts on Sepolia 

[[5-Redeploy TON-Staking-v2 on sepolia  (using agenda)  ]] 

```javascript
 
"L1BridgeRegistryV1_1" at 0x16979Ee40B68Bb0e03a6Fa8cc6fb7f1FCC89ecc4
 "L1BridgeRegistryProxy" at  0x2D47fa57101203855b336e9E61BC9da0A6dd0Dbc
 "OperatorManagerV1_1" at 0x48f60aAf60D5E162b2DebFD4F70c88fE01b7c331
 "OperatorManagerFactory" at 0xEEbFD108e124bFeC9545bDbB32aB7840DBC1872e
 "CandidateAddOnV1_1" at 0xCB75860cFBe1c4668A1D90d8d6c80c1f2c9C93A4
 "CandidateAddOnFactory" at 0xF08360bdF665eCB2B91217E9843bB241b440239a
 **"CandidateAddOnFactoryProxy" at 0xf37493caC8BF8df0bD96146211D93D548d506fb9**
 "Layer2ManagerV1_1" at 0xF9d75D5814e1C3D734342bD5Ed0637b9c49c3f69
 "Layer2ManagerProxy" at 0x58B4C2FEf19f5CDdd944AadD8DC99cCC71bfeFDc
 "SeigManagerV1_2" at 0x1039C6b7C4A5920DCf2aD8BBaaB0fb3F02926898
 "SeigManagerV1_3" at  0x8C29A0C04a6A3dfee84b602fA13CD4A5a764B3dA
 "DepositManagerV1_1" at 0xfd0c0AA6505125eFab34A2195F1b9C99AFE8fB06
 "DAOCommitteeProxy2" at 0xC74b529Ad06E70fA51CDDAD11857D53E6354523d
 "DAOCommitteeOwner" at 0xf26D736db6a259AfD93ffDa027b0d7DD9748e3FB
 "DAOCommittee_V1" at 0x9Cb6e22A9a551c13159d818D540aE8bE299967fb
```

# L2 Information

## OperatorManager

- How to find the OperatorManager address
  - (1) OperatorManager is CandidateAddOn.operator() 
  - (2) Layer2Manager.operatorOfLayer( CandidateAddOn address ) returns a OperatorManager address.

## How to find the RollupConfig address

- (1) Layer2Manager.operatorInfo( OperatorManager address ) returns a CandidateAddOnInfo .
```json

    struct CandidateAddOnInfo {
        address **rollupConfig**;
        address candidateAddOn;
    }
```

## L2 Type 

### view L2 type  and status

Contract: **Layer2Manager**

Function: checkL1BridgeDetail(address _rollupConfig) 

```solidity
/**
 * @notice Layer 2 related information search
 * @param _rollupConfig     the rollupConfig address
 * @return result           whether Layer2 information can be searched
 * @return l1Bridge         the L1 bridge address
 * @return portal           the optimism portal address
 * @return l2Ton            the L2 TON address
** * @return ****_type****            the layer 2 type (1: legacy optimism, 2: TRH's thanos stack)**
 *** @return ****status****           status for giving seigniorage (0: none , 1: registered, 2: paused )**
 * **@return rejectedSeigs     If it is true, Seigniorage issuance has been stopped for this layer2.
 * @return rejectedL2Deposit If it is true, stop depositing at this layer.**
 */
function checkL1BridgeDetail(address _rollupConfig) external view
    returns (
        bool result,
        address l1Bridge,
        address portal,
        address l2Ton,
        uint8 _type,
        uint8 status,
        bool rejectedSeigs,
        bool rejectedL2Deposit
    )
```

# A function that withdraws the staking amount of operatorManager. 

- requestWithdrawal(uint256 amount)
```solidity
 function requestWithdrawal(uint256 amount) external onlyOwnerOrManager
   
```
- processRequest()
```javascript
  function processRequest() external onlyOwnerOrManager
   
```
- processRequests(uint256 n) 
```solidity
 function processRequests(uint256 n) external onlyOwnerOrManager
```

# The amount of TON in bridged L2

It is different from [L2 type](/d76ffba7cf8d428a94a250399f7b09fe#1ecaa85407a149a5986337f8351fb70c). 

- If L2 type is 1 , in case is legacy,
the amount of TON in bridged L2 = TON.balanceOf (L2Bridge Contract of L1 )
- If L2 type is 2 , in case is TRH's Thanos,
the amount of TON in bridged L2 = TON.balanceOf (Portal Contract of L1 )

# The updating seigniorage amount 

```json
let estimatedDistribute = await seigManager.estimatedDistribute(
	block1.number+1, titanLayerAddress)
 
// console.log('estimatedDistribute', estimatedDistribute)

//  시퀀서 시뇨리지 = estimatedDistribute.layer2Seigs
```

# Addresses on sepolia 

```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386


TON : 0xa30fe40285b8f5c0457dbc3b7c8a280373c40044
WTON : 0x79e0d92670106c85e9067b56b8f674340dca0bbd
```

# OperatorManager

### claimERC20(address token, uint256 amount)

## Check registered L2 information

- Contract: Layer2Manager 
- Function: 
  - layerInfo(address layer2) external view returns (address rollupConfig, address operator)
- Returns the rollupConfig and OperatorManager information mapped to the registered layer2.