- [abi](https://github.com/tokamak-network/ton-staking-v2/blob/Layer2Manager/artifacts/contracts/layer2/L2RegistryV1_1.sol/L2RegistryV1_1.json) 
- branch :  [https://github.com/tokamak-network/ton-staking-v2/tree/Layer2Manager/contracts/layer2](https://github.com/tokamak-network/ton-staking-v2/tree/Layer2Manager/contracts/layer2)

> **Layer 2 TON liquidity change information must be transmitted. **

### SystemConfig 

- Storage 
  - l2Registry :  L2Register address.
  - name : used as a layer name in simple staking.

```javascript
string public name;
address public l2Registry;
```
- Interface 
```javascript
interface IL2Registry {
    function increaseTvl(uint256 amount) external;
    function decreaseTvl(uint256 amount) external;
}
```
- Function on legacy 
```javascript
modifier onlyL1StandardBridge() {
    require(addresses.l1StandardBridge == msg.sender, "not l1StandardBridge");
    _;
}
    
/* ========== onlyL1Bridge ========== */
function increaseTvl(uint256 amount) external onlyL1StandardBridge nonZero(amount) {
        IL2Registry(l2Registry).increaseTvl(amount);
}

function decreaseTvl(uint256 amount) external onlyL1StandardBridge nonZero(amount) {
        IL2Registry(l2Registry).decreaseTvl(amount);
}

```
- Function on bedrock 
```javascript
 modifier onlyOptimismPorrtal() {
    require(addresses.optimismPortal == msg.sender, "not optimismPortal");
    _;
}

/* ========== onlyOptimismPorrtal ========== */
function increaseTvl(uint256 amount) external onlyOptimismPorrtal nonZero(amount) {
      IL2Registry(l2Registry).increaseTvl(amount);
}

function decreaseTvl(uint256 amount) external onlyOptimismPorrtal nonZero(amount) {
      IL2Registry(l2Registry).decreaseTvl(amount);
}

```

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

## gas comparison 

- method 1 
  - increaseTvl : 92031 used gas ( 7.81  when 30 gwei ) 
  - decreaseTvl : 63516 used gas (5.39 when 30 gwei )

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7cbb9c17-36b1-4c52-a6e7-3f6a96db378e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-12_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.33.55.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622CEK2Q3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNhgVtdQyFUwznIH6wb8mJ0nEENw3TkL%2B51STmRp7GgAiBhppCBQ37Pm2MrCHvL16M7wJb2He0%2BrSaJ2x5gY0XT%2BSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMCS7dWr379f7gqpjEKtwDmEukrm1gSeDmeiAyGKePgUBd1ftcap%2FUKqjDtTsFudHT9TV8TJCGYAQSOdi3x3W0sCV8o%2BWzF2NDRaz1YxjfOmJ6zjFrPck22CByCuCqozOU1Df7HaygmO%2B7BXjl7hNrBTqlEo%2FfKMauCDKEmSYWvmRzS5pGVPCOwHWzL64fqTpXOR%2F9HJUSfevwdJtLncqB7drgxyRTTOX2Rnx1Wt19Ym1G6p0yLpZxJbDjlq7BbwVZGF13WszVpAbnGWb1cZDkohHtO8J6jbZx%2Bru4wnKpUc0D4ilt5zHL2f94QD%2BV1N1bremsPbZh%2FkstE3D7J6r8ngpAcZ0CKuVLiOqj9nhB1oM04Ud1hSiQfZsl3ZruKyScZ5QGpiCEri1FvXE9lvU443tbYSS6Vhy70EbDkQ%2BUhLEQJMSNGBPtW9cHDPk8R7Asil71zsjsskSBq%2Bt1TsmhXEx6UpYbTSL89ESRICGJRWtC1xC3pybesX26pQMUMeQ77VgITe8pUYsQdqJMxl6BTnIgmxKPLqtCSEam%2Fr%2Bh86HvDAYrWaaGhEwlko5Fv7OrwekYFCD%2F6vFHxw22xBQpKcusxiiXpfPwLBdHewbs%2BG62TSAYmRGyMoE4Bcb6i44MTWWcqEQHDDaAnFIwnpnbzAY6pgGQMGoBIOmTRdQxM62MbxVg%2FHgX7fjPmr5gKQUprPVy6br%2Bik9kDCfRga7yybfVJeY1S2%2B8JxLsjOTPvRU3fCTn9aZVW%2BJEiGRt6UueVKjaMyj0E53l8lAu0dcI6%2FxFQJyN%2BPJRyjkm2K8DOMho6jpFoG9LM%2BKzx840He0KcdoCk6OiXk7MYXeAkENePcH%2B%2FOVZik8nc%2BmspdhrxiwqGCfuYqgQ0pZD&X-Amz-Signature=bb850901e89eb383cb8815ff88fcc8fed0ab23428b59c2b4d11e540d454d49a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)