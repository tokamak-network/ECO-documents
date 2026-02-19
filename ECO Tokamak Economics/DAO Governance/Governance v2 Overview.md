# Assets Under Governance (v2)

### Please follow the below structure when you add a new entry.

- General Name/Contract Name
- Contract Github Link
- Contract Address
- Function name/ Parameters (that can get updated using DAO)
  - Criticality Level (Low, medium, high)

## Asset List

1. Staking Contract
  1. General Name/Contract Name
    - General Name : SeigManager 
    - Contract Name: SeigManagerV1_2
  1. Contract Github Link
[https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManagerV1_2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManagerV1_2.sol)
  1. Contract Address
    - SeigManagerProxy : [0x0b55a0f463b6defb81c6063973763951712d0e5f](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| pause() | High |
| unpause() | High |
| setData(
address powerton_,
address daoAddress,
uint256 powerTONSeigRate_,
uint256 daoSeigRate_,
uint256 relativeSeigRate_,
uint256 adjustDelay_,
uint256 minimumAmount_
)  | High |
| setPowerTON(address powerton_) | High |
| setDao(address daoAddress) | High |
| setPowerTONSeigRate(uint256 powerTONSeigRate_) | High |
| setDaoSeigRate(uint256 daoSeigRate_) | High |
| setPseigRate(uint256 pseigRate_)  | High |
| setCoinageFactory(address factory_)  | High |
| renounceWTONMinter() | High |
| setAdjustDelay(uint256 adjustDelay_) | High |
| setMinimumAmount(uint256 minimumAmount_) | High |
| setSeigStartBlock(uint256 _seigStartBlock) | High |
| setInitialTotalSupply(uint256 _initialTotalSupply) | High |
| setBurntAmountAtDAO(uint256 _burntAmountAtDAO) | High |
| setProxyPause(bool _pause) | High |
| upgradeTo(address impl) | High |
|  setImplementation2(
address newImplementation,
uint256 _index,
bool _alive
) | High |
| setAliveImplementation2(address newImplementation, bool _alive) | High |
| setSelectorImplementations2(
bytes4[] calldata _selectors,
address _imp
)  | High |
| addAdmin(address account) | High |
| addMinter(address account) | High |
| addOperator(address account)  | High |
| removeAdmin(address account)  | High |
| removeMinter(address account) | High |
| removeChallenger(address account) | High |
| removeOperator(address account) | High |
| transferOwnership(address newAdmin) | High |
| renounceOwnership() | High |
| revokeMinter(address account) | High |
| revokeOperator(address account) | High |
| revokeChallenger(address account) | High |
1. DepositManager Contract
  1. General Name/Contract Name
    1. General Name : DepositManager 
    1. Contract Name: DepositManager
  1. Contract Github Link
[https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/DepositManager.sol](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/DepositManager.sol)
  1. Contract Address
• DepositManagerProxy : [0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| setSeigManager(address seigManager_)  | High |
| setGlobalWithdrawalDelay(uint256 globalWithdrawalDelay_) | LOW |
| setProxyPause(bool _pause)  | High |
| upgradeTo(address impl)  | High |
| setImplementation2(
address newImplementation,
uint256 _index,
bool _alive
) | High |
| setAliveImplementation2(address newImplementation, bool _alive) | High |
| setSelectorImplementations2(
bytes4[] calldata _selectors,
address _imp
)  | High |
1. Layer2Registry 
  1. General Name/Contract Name
    1. General Name: Layer2Registry
    1. Contract Name: Layer2Registry
  1. Contract Github Link
[https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/Layer2Registry.sol](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/Layer2Registry.sol)
  1. Contract Address
• Layer2RegistryProxy : [0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| unregister(address layer2) | High |
| addAdmin(address account) | High |
| addMinter(address account)  | High |
| addOperator(address account) | High |
| removeAdmin(address account) | High |
| removeMinter(address account) | High |
| removeOperator(address account) | High |
| transferAdmin(address newAdmin) | High |
| renounceOwnership() | High |
| revokeMinter(address account) | High |
| revokeOperator(address account) | High |
1. Treasury / DAO Vault 
  1. General Name/Contract Name
    1. General Name: **DAOVault**
    1. Contract Name: **DAOVault**
  1. Contract Github Link
[https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOVault.sol](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOVault.sol)
  1. Contract Address
    1. DAOVault : [0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303](https://etherscan.io/address/0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303#writeContract)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| transferOwnership(address newOwner) | High |
| renounceOwnership() | High |
| setTON(address _ton)  | High |
| setWTON(address _wton) | High |
| approveTON(address _to, uint256 _amount) | High |
| approveWTON(address _to, uint256 _amount)  | High |
| approveERC20(address _token, address _to, uint256 _amount)  | High |
| claimTON(address _to, uint256 _amount)  | High (now don’t use) |
| claimWTON(address _to, uint256 _amount) | High (now don’t use) |
| claimERC20(address _token, address _to, uint256 _amount) | High |
1. TON Contract
  1. General Name/Contract Name
    1. General Name : TON 
    1. Contract Name : TON 
  1. Contract Github Link
    1. [https://github.com/tokamak-network/plasma-evm-contracts/blob/master/contracts/stake/tokens/TON.sol](https://github.com/tokamak-network/plasma-evm-contracts/blob/master/contracts/stake/tokens/TON.sol)
  1. Contract Address
• TON: [0x2be5e8c109e2197D077D13A82dAead6a9b3433C5](https://etherscan.io/address/0x2be5e8c109e2197D077D13A82dAead6a9b3433C5)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| enableCallback(bool _callbackEnabled)  | High |
| transferOwnership(address target, address newOwner) | High |
| renounceOwnership(address target) | High |
| renouncePauser(address target) | High |
| renounceMinter(address target) | High |
| transferOwnership(address newOwner) | High |
| renounceOwnership() | High |
1. WTON Contract
  1. General Name/Contract Name
    1. General Name : WTON 
    1. Contract Name : WTON 
  1. Contract Github Link
[https://github.com/tokamak-network/plasma-evm-contracts/blob/master/contracts/stake/tokens/WTON.sol](https://github.com/tokamak-network/plasma-evm-contracts/blob/master/contracts/stake/tokens/WTON.sol)
  1. Contract Address
• WTON: [0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2](https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| renounceTonMinter() | High |
| renounceOwnership() | High |
| renounceMinter(address target) | High |
| renouncePauser(address target) | High |
| transferOwnership(address target, address newOwner) | High |
| enableCallback(bool _callbackEnabled) | High |
| setSeigManager(SeigManagerI _seigManager) | High |
1. TOS Contract
  1. General Name/Contract Name
    1. General Name : TOS 
    1. Contract Name : TOS 
  1. Contract Github Link
[https://github.com/tokamak-network/tonstarter-token-distribution/blob/master/contracts/tokens/TOS.sol](https://github.com/tokamak-network/tonstarter-token-distribution/blob/master/contracts/tokens/TOS.sol)
  1. Contract Address
    - TOS: [0x409c4D8cd5d2924b9bc5509230d16a61289c8153](https://etherscan.io/token/0x409c4d8cd5d2924b9bc5509230d16a61289c8153)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| addMinter(address account) | High |
| addBurner(address account) | High |
| removeMinter(address account) | High |
| removeBurner(address account)  | High |
1. PowerTON
  1. General Name/Contract Name
    1. General Name: PowerTON
    1. Contract Name: PowerTONSwapperProxy
  1. Contract Github Link
[https://github.com/tokamak-network/tonstarter-project-token/blob/master/contracts/powerton/PowerTONSwapperProxy.sol](https://github.com/tokamak-network/tonstarter-project-token/blob/master/contracts/powerton/PowerTONSwapperProxy.sol)
  1. Contract Address
PowerTONSwapperProxy**:** [0x970298189050aBd4dc4F119ccae14ee145ad9371](https://etherscan.io/address/0x970298189050aBd4dc4F119ccae14ee145ad9371#code)
  1. Function name/ Parameters (that can get updated using DAO)
| Function | Criticality Level  |
| --- | --- |
| upgradeTo(address impl) | High |
| setProxyPause(bool _pause) | no impact |
| setAutocoinageSnapshot(address _autocoinageSnapshot) | no impact |
| setSeigManager(address _seigManager) | no impact |