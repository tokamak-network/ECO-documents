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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7cbb9c17-36b1-4c52-a6e7-3f6a96db378e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-12_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.33.55.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6QCPW4C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAr%2BQlU2I6pZ2FLKim5Bc5JHZ6Gop6W2id72J5jeYssNAiASeEeR%2FmDkR6b1ZARkh8in%2BTLkET%2FaL4SWm6stRA9KPir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMiI5RVCKJcQzIhNGkKtwDU82WFQptuouyaoZPVwYUIyhedW7hzfZdXsmhv0D6wTC2WMlEwtfCVqgcI1ulA7IF%2FUK97AXuUPx4sSx1QFeZ44Vg94CA%2BBkMhVbnyxpE1ShfUirAXEUxtMb6sSg%2FvzFjk9RdAEWjLuiFdH%2FEsCjf51MQK62sAv9DkxdxaMNRacTXANCxAkHuWVvjzF4X4B57iQSDsho0wfCgnIMsSwMg1VFivbtAULywNcnRPY81BUmnXmAMCu2QnK1rP57ere1CPE%2BWuLpC0yK4dpUBC79RPGUp6xrUY1yXnzNoSt0vx%2FRLf6MOCYhEQTvJYlhul2a97xPXb8cNgPpmTq4D1JE%2Bmdd5GvaJLud3X6RQ8wk6BckRtw3I8f25kA7rSefOe9wOAk22%2BoEoOyEwfg%2F1Y4LyGoFkS%2F2G3h%2FW7mPJhKYV1fyY1OrIyRtixHIfSiCMxRZDMSxbXC1XvmTf94zhsvyqQtD9%2BRp%2F50eeRXqKSu80L4G9TFl1PxXWaBFoYrDzVXwZ7T8SWuPgTA8%2FZpCzdjt5jG51qAU4DK%2Bf%2BJEfwNNb9npmFUe97g3DCyusJR2sk1TuNVuTmQF2heO97W4t9Goru7KFmJDr64ONIjvYa73PFu1JawVdWGtUkw2srpMwivLZzAY6pgFu9QjIy%2BHajp5DHi3uByvwt0bt3vlneMxxbhwdPye1Yid2qL33N%2BfYiyUFSp7vFhXIjcvcCJgVTedwf0gxtl5DA%2F6IlAaKpUfRRF4Svs0eoEeSsU9fgquu%2BxFGW34lNFFl0jrGE7AuZzqxfJVNN7IQs6ENo41wI5GnG7DPVhlEp%2FcJkpPuSIWtR4eo3tq9fnQbF8FkMSjX5tf6EECvTPQCNjBVPTKd&X-Amz-Signature=1f36e238a6af178287c1b07dae2f50d4889c6a5dac4304fbb54c83e81002d689&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)