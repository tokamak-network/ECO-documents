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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/268e5b5c-0871-4658-970f-81192b9eb609/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_9.40.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJCVB6E%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDw4PkSe0a%2FVJ26jpifoJqPVosMd7ktkofr6j3C3OJ7jQIgdOUAiZz49et4Dgs0CvQu7C6NIsUlLLgyhUDnEoRGRk0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDJ%2FqQHYkTvJOfQkeRSrcAyyULXEMiTImlB3mU8s4asUb2%2FYhmpo%2FBVvLNh%2BMhaHTJdLYqHseLQ0SzObqlUmY0AZ9iaZ9swxTFZkj92Kbvn%2BGF0SpfEGF4tFGEZNoL0lSZPcsr7QrU1kvMvdUvRDpwOmMMiP8palLE6GGh0N6Kou0qml6PZHWGgAkyN5DgFO5uVaRF6N3Ytdt6J2U15j9JtaGhrhnPY5BVwQeE3GgYqSLpDpfbCokE4QqZO6eYxxDHsXTH%2BdSZyZxbzqcp9YFaQVvmKnQBqnv0oGQp1F2%2FXnwEtKJqeS8XgHVwrcBwH0lBe3CoCxaMc%2FPLSxnuZ9WNe89zXleLMYHRRGb4%2BcF0SS1zb%2FWWGc8A4E2cO%2BMvGm%2Bh3eB1Pe2%2Bw9sawhnNAxVUJioZDiCL6yVqJzL23I2xgGPfU06BGXvRUND%2FDg%2F9%2FDiNdHYFSdBcin7QrwJm78c%2BhlZRmiN4QIN9jiEDrkTjeGbFYZlNb78WVRMKaNWeDkyAxGwzGvoERgIzTJL%2BhoGIiKT7ylgE0ls4eTr8nJ47f6Tc4GQi2NfFoU1vkegMJqZWCoWIBBoCICcZjPs6uGEQHKz1xVAfrH3wnht2FDDihyG2i4Jc7BLtFMHw%2FUtorQ8Zz9k1%2BGST3jwOUzzMJ%2BZ28wGOqUBJQzq8JKuE4Q1GohcEzAvUw%2F0RDljAe1VLQlLoR%2BmisDm5H40rHDZlPKpgJuH%2BLLZtH0E919dvjQQe7d6iZmgftxKpRkjI2%2B3325NzrO43J46mhBETCytpeFLzwCmtUqUjj9kyD5sxDugMk7egwV820dEwiuJ%2Fo3LUxL5b6tmo1dmzBBTXcB7D1rNIM0J%2FZjKQuU8VIn3leLuhqn%2Bj2ciH3QFN2rB&X-Amz-Signature=bb4fedf7eb6a9c860f76275da73b4c714323281a1b6ded97fa7484fb3d659a4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 