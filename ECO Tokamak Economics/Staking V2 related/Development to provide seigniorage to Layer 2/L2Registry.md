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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ac80d8c2-9505-44c9-9f57-8cb0a997a244/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.56.43.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6WV3IN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3SxU0wqF3CWIDjWnR12I1%2BjI3LKttobxUivQIt7RekwIhAPtCIW%2FVHFXzdEAKtUi00X8N%2Fj3Gpk%2FoxZ7YIgCAI4Y%2BKv8DCHoQABoMNjM3NDIzMTgzODA1IgyKuXY0lYMk3pATE8oq3APjiinOWRyUJ5YoBnGUQijWstyE0dh8jZgNQ6%2B2Qp21HhQo2P6m5fjbkCg92DHQlOH6z552lZcbZnF%2BbmvffxX%2FH9tfZDGSa3baeYKzl9NONVV5i3taMCMWPehxGknm273pFXAvNYOHiO9gkrjw81GmUfWm%2Fg3hnjsk5qpE%2BlPeVlN2GeXMPfdE9jpnsnAJLubABf539pVpvxee8kEcogMveuRdZbetg%2BYAyfDqHGoqoX9aFGG6B3Qb1mW2qx5%2BUxm%2BaMaFNWTGJNbGc09t31IOOR1pwh%2FLVm0XChP6BcXbsyVNKBnvg0Man%2FB7p2LCOu6XnMA%2F%2F8IiB%2BrdFvQoVGAkXOooneKz7LAak6bLPYgMtWIibF49IdDT5z4%2BJu8kHb1Ru%2Fe3ug8rY1BNwCiY7ygM2bqeLd31jxngHoIdAFdX%2BKBjU8w%2BKk8rkXxBzAkOtiIwnyxBoAS6hE17J0NHAHzBCT3hIcuQkhC31fuJFjQfk6CPhg%2BSUgdRy6IyTTGiKezi8OpUjnmucgpvrXsiqR8xZqEF3IVTPOs%2Fm5qwSuolGkl5XayrEGxJl2TDrgEWkxuGB8oUlI6l8RaUHFTC1K2YRz7B1OdbN7MfhPMYFvL2bQdahdzDB%2FJUHQNdEjDbmdvMBjqkAaBcI%2F8tgIu13g3Lhfjesj2rAyXFEBOMQgjsuu8QbB4sFMCz85db1dmtA6GYJnU65RWsjBf%2BmJvC9xhHzdSYfR6lVwLKzVL5FKb3XaAq3iwL9GC4DaxSyi552iFLYxtS%2Fshhpep6nM6aRNElbkXdqf9qNFs9c2jjXiitwqHUe3cRiHHx76FmN8%2BfwTS7jAMmmjF9dAu4WMfMk3X9LiaJsoZfUWw%2F&X-Amz-Signature=9546afceb25ac98b2140e94a1cc81cebf8bf174e1f493eca369c673115b225d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)