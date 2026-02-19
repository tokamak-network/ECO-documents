[[discussion about Layer2Manager managing L2 TVL]] 

# Permission Role 

- **Owner **:  오너는 로직 업그레이드 권한을 갖으며, 매니저를 지정할 수 있다. 
- **Manager** : 재단은 MANAGER_ROLE 을 보유하고 있고, 매니저는 오퍼레이터를 등록하거나 제거할 수 있다.  SeigniorageCommittee
- **Registrant:  on-de**mand-L2 오픈시, L2를 실제 배포하는 서버의 EOA에게 REGISTRANT_ROLE 을 주어야 한다. 

L2 **Registrant 정책 :  Core Team **

# ABI

[dir](https://github.com/tokamak-network/ton-staking-v2/tree/Layer2Manager/contracts/layer2)

# Storage

```javascript
/// Power permission, DEFAULT_ADMIN can register or delete users with other permissions.
// owner - DEFAULT_ADMIN 

/// authority to register or modify systemConfig address
bytes32 public constant MANAGER_ROLE = keccak256("MANAGER");

/// When creating on-demand-L2, permission to register systemConfig address in L2Registry
bytes32 public constant REGISTRANT_ROLE = keccak256("REGISTRANT");
```

```javascript
 
 address public layer2Manager;
 address public seigManager;
 address public ton;
 
 /// systemConfig - type (**0:empty, 1: optimism legacy, 2: optimism bedrock-native TON** )
 mapping (address => uint8) public systemConfigType;

 mapping (address => bool) public l1Bridge;
 mapping (address => bool) public portal;
```

# Event

```javascript
event SetAddresses(address _layer2Manager, address _seigManager, address _ton);

/**
 * Occurs when registering SystemConfig (Layer2Candidate)
 * @param systemConfig  SysremConfigAddress
 * @param type_  0: none, 1: legacy, 2: bedrock with nativeTON
 */
event RegisteredSystemConfig(address systemConfig, uint8 type_);
event ChangedType(address systemConfig, uint8 type_);
event SetSeigniorageCommittee(address _seigniorageCommittee);
event RejectedLayer2Candidate(address _systemConfig);
event RestoredLayer2Candidate(address _systemConfig);

```

# Functions

```solidity
modifier onlySystemConfig() {
    require(systemConfigType[msg.sender] != 0, "unregistered systemConfig");
    _;
}

modifier onlyLayer2Manager() {
    require(layer2Manager == msg.sender, "sender is not layer2Manager");
    _;
}
```

## onlyOwner

```javascript
function setAddresses(
        address _layer2Manager,
        address _seigManager,
        address _ton
    )  external onlyOwner   
```

## onlyManager

```solidity

function registerSystemConfigByManager(address _systemConfig, uint8 _type)  external  onlyManager

-  _type   (0:empty, 1: optimism legacy, 2: optimism bedrock )
    
```

## onlyRegistrant

**This is something that must be reflected in order to receive seigniorage.**

```solidity
function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyRegistrant  

- _type   (0:empty, 1: optimism legacy, 2: optimism bedrock )

function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant 

```

 

# Public

```solidity
function layer2TVL(address _systemConfig) external view returns (uint256 amount)

function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid) 

```

# Test 

`npx hardhat test test/layer2/units/0.L2Registry.test.ts`

[link](https://github.com/tokamak-network/ton-staking-v2/blob/Layer2Manager/test/layer2/units/0.L2Registry.test.ts)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ac80d8c2-9505-44c9-9f57-8cb0a997a244/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.56.43.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYPF54AX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFsi6o7VJvEl%2FjJi5kKo54oPRIs%2F%2BO79myG3roEnPswAiEAoYQrWdbewRKYMK7udPK3XGV%2B7r2NJIHZDD9c7o1qY04q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDG2L0YdUchzlID52%2BSrcAxuSj9tWDghcPMyBjSXfeGzTIbcpIC7Rx7vOFF8MLk1MYfx%2BCAcF8%2FO7fyDG1tPHjENmAiIJAZez%2BQfB17lV1AVSYE29aoY%2FbDeB48ltdOoC28IRfB1RXG6Qtg0H86fWKVcgdJHBmtZnx6TLZwMBoKTw5AQglxSSX7KR88wyuPx55GCR06f6ypRujj%2Bhn4ZZFdKK68MzJfSq77HArBjltA1F72yi7Drw8adosym4ebRxZp7Vv1ldTgPsyG81Q9tFQLKsAV5mu0e7XTuRzL3%2F9%2FgrtkaayBK6QsHh483nwJeQeY6RTq9pgOJZ8oHOti9dvTeB3XbgK4kESHlCi57WRpxaX4YuSjwYHeWQIkKUzjM6S%2FXM6VPCwrLPFOtiE6WY3MadYqMKD%2FI9iBEbJ3bxgpQ62jwHaO2Ny53dpOe8yDqQtC04haHemhIeUcvRXZZhHuILQpnWSVjq1jVPLgEPMoKy0oWvWWmZsNU%2FfcJdigeBiisWErFHiXOe4K9eVL8OH4CiiY%2BYCP95OkPfeDZnsc0ze20Uup21MTKiCut1TTs25ECNZ%2F01yc6XmEeKQwYYIwyaorETWquy1Ari54GuxGi%2FPV7G5JEpnNdENRUqqBVXTg28LYsw2Ks%2FiQNsMIzw2cwGOqUB0XDQS4IeWK6D1dD08NSp4Fphja8TIn45mjczEfCy%2FVtq1orTkryFusA2ZTsBKK%2BUQdJEFHQmTswhYiGaohQHmWibERvDDY%2FKDOWnMuB0fSOusfkCINwU641w0RwOQSoyeU3bYXprGQYF0uvWBdlcAvNtyEgHsSdcG5zBHmXvgHT8qXT4dfWoMnS%2FTQbsOyh5hZ4V0jndXONQKUBuuv5fNyLK5%2BGE&X-Amz-Signature=01b5bafcbca3d94c2f80340fe605e19b2004317e1db8f85d3e00af2dfa3725cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)