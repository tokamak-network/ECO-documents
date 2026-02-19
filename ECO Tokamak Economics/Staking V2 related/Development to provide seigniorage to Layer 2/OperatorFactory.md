오퍼레이터 컨트랙을 만드는 팩토리 컨트랙이다. 

DAOCommittee 에 Layer2Candidate가 멤버로 등록될때 Layer2Candidate의 오퍼레이터 주소가 매핑의 키값으로 등록되기 때문에 오퍼레이터 주소가 변경되어서는 안된다. 

그러나 L2레이어(SystemConfig)의 오퍼레이터는 언제든지 바뀔수 있기 때문에 Operator 컨트랙을 만들었다. 

Operator 컨트랙은 SystemConfig 컨트랙에 매핑되는 컨트랙이다. 즉, SystemConfig (L2레이어) 컨트랙 주소로 Operator 컨트랙의 주소를 생성하여야 한다.   

추후 로직 변경 가능성이 있으므로, 프록시로 구현하였다. 

# Permission Role 

- **Owner **:  오너는 배포되는 오퍼레이터의 로직을 설정할 수 있다.  

# Storage 

```javascript
address public operatorImplementation;
address public depositManager;
address public ton;
address public wton;
address public layer2Manager;
```

# Event 

```javascript
event ChangedOperatorImplementaion(address newOperatorImplementation);
event CreatedOperator(address systemConfig, address owner, address operator);
event SetAddresses(address depositManager, address ton, address wton);
```

# Function

### function createOperator(address systemConfig) external returns (address operator) 

- systemConfig 의 owner() 만 실행할 수 있다. 
- systemConfig 의 owner() 를 Operator의 owner 로 설정합니다.  

### function getAddress(address systemConfig) public view returns (address operator)

- systemConfig 주소를 알면 operator 컨트랙의  주소를 알 수 있습니다. 

# Test 

`npx hardhat test test/layer2/units/1.OperatorFactory.test.ts`

[link](https://github.com/tokamak-network/ton-staking-v2/blob/Layer2Manager/test/layer2/units/1.OperatorFactory.test.ts)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/268e5b5c-0871-4658-970f-81192b9eb609/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_9.40.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUOEIB76%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBVZyyUNVpsCW1LHeB%2FJ7ozXHXL%2FyUgTcdpVoGtXB6mNAiBPSIjjpM9HY2GYWUyv4dKLJrydqQb8oeripd1jCIm%2FOyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM613ThONTLTHqtC9xKtwDMIdpO3j7ZrfrvFOiRTz9c%2FMHDUPRzjoTwhkHZk2O9divStxIDjM6tUSQ2UVH4s49UMf0qGBLiKhZRDnq5VlKwL8ezuyw6XdU8ruDiClfcKdHX0xrh8f7IltoNOcrCzGey2N1dZPKE%2BhQOcoExC5lO0%2FSVCPZ7UV5Lw20LJn8A5WnfZMTXM%2BGyt916Y316AhyQFMXn%2F8B0mF9GBBqMFRu%2FBVZuhlpuqutL3Me6n0WWJEvgDeeW1pjQ0fTZNcU2zJrirQUeqIpPnR4zUsu9vCkGzjy8HJdZIYUM0iiWAHyro%2BSIrvXmFbtEQbRkptJiS7rhIUs8Ux1aw9M8bn%2FuSE8DmQUuWxDXWSNGnW0UuxlDEv0b0KhSi%2BsA7BgiCb9bORSnpSCZZquAvDScqkH2zogEaNTHRKeCRCh6bLcQx%2Bo%2FbIOl8npIne637YPD%2B485K%2Ba%2BAzsIUF2KPeEV%2BaxdTSDYH8JiqO6V7vIsaX5qs6Lufd%2BtZOb%2BAD7T3LogfnWFBbk2d2513KhMjF6vFt2TkZZ8%2Bt%2BziUXncx5pVZHxawmaJfNXE3pJMdLAClO0JIW%2F4XTOcZWb3Wm5VAx3YIUb0NgsIX9wsWHIQKWx2vivD5fu7NZpPZZ%2Fba4D4K7e0QwvO7ZzAY6pgGoReWML5V6aoMMBzh9jwggattbj0P6j1b1aan2LIPp0PLML1edwJD3r4KXPEkO9RU8IKgo8KAiZJtIb5TWt%2FJGkSRuaHwiBQ22rGFI36ESd%2Bo5CcosmbmDldLgX87S9%2BdgPuVQ5Px3Bwd5vSxDO4Os0NawAqSj8%2FApUBTWGiW0U5LSgcju2hZ%2BVUCsndAxfSuh5e1m4FrQMM%2FMElXz3pqbEIwDk91P&X-Amz-Signature=731a417ae3407d5a3b741b9d478fc56e67805925f23cd681a1fce9645ca657b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 