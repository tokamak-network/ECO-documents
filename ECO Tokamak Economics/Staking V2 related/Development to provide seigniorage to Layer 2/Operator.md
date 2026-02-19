# Considerations 

# Abi

# Storage 

```javascript
address privaye _owner;
address public systemConfig;
address public layer2Manager;
address public depositManager;
address public ton;
address public wton;

address public manager;
mapping(address => bool) public operator;

```

# Event

```javascript
event TransferredManager(address previousManager, address newManager);
event AddedOperator(address operator);
event DeletedOperator(address operator);
event SetAddresses(address _layer2Manager, address _depositManager, address _ton, address _wton);

```

# Function

## onlyOwnerOrManager

```solidity
function transferManager(address newManager) external nonZeroAddress(newManager) onlyOwnerOrManager  

function addOperator(address addr_) external nonZeroAddress(addr_) onlyOwnerOrManager 

function deleteOperator(address addr_) external nonZeroAddress(addr_) onlyOwnerOrManager
```

## onlyLayer2Candidate

```solidity
/// deposit an amount to the Layer2Candidate  
function depositByLayer2Canddiate(uint256 amount) external onlyLayer2Candidate  

/// transfer the WTON holdings to the manager's account.    
function claimByLayer2Candidate(uint256 amount) external onlyLayer2Candidate 
```

## onlyOperator 

```solidity
/*
execute a transaction (called directly from owner, or by entryPoint)
*/
function execute(address dest, uint256 value, bytes calldata func) external onlyOperator 

 /**
 * execute a sequence of transactions
 */
function executeBatch(address[] calldata dest, bytes[] calldata func) external onlyOperator {

```

## only SystemConfig's owner

```solidity
function acquireManager() external
```

## Public 

```javascript

function isOperator(address addr) public view returns (bool)   
function checkL1Bridge() public view returns (bool result, address l1Bridge, address l2Ton)  
```

#   