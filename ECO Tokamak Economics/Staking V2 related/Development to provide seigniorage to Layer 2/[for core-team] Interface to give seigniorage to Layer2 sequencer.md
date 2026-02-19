- branch: [https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/](https://github.com/tokamak-network/ton-staking-v2/commits/L2Seigniorage/) 

> **On-demand L2 layers must be registered in the L2Registry when created to be able to register them in Simple Staking. **

### L2Register

- address 
  - We will inform you later.
- Permission
  - In order to register with L2Registry, the address to be registered must be granted Operator privileges. This is manually authorized by the manager.
- Function 
```javascript
/* ========== onlyOperator ========== */

///@param _systemConfig systemConfig address
///@param _type  (0:empty, 1: optimism legacy, 2: optimism bedrock )
function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyOperator ;


///@param _systemConfig systemConfig address
///@param _type  (0:empty, 1: optimism legacy, 2: optimism bedrock )
///@return valid If true, registration is possible, if false, registration is not possible.
function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid) ; 
  
```