[[discussion about Layer2Manager managing L2 TVL]] 

- The layer2 to receive seigniorage **must be registered with Layer2Manager.**
- **Layer2Manager 컨트랙은 Layer2의 오퍼레이터에게 지급되는 시뇨리지를 보유하고 있다.  **
- Layer2Operator는 Layer2Manager를 통해 시뇨리지를 청구할 수 있다.  청구시에는 별도의 대기시간없이 바로 시뇨리지를 받을 수 있다. 
- 업데이트 시뇨리지 실행시마다 Layer2오퍼레이터에게 지급되는 시뇨리지를 정산받는다. ( 굳이 해당 Layer2Candidate레이어의 업데이트 시뇨리지 실행이 아니어도 상관없다.) 

Description of Layer2 Seigniorage 
[[SeigManagerV1_3]] 

# Permission Role 

- **Owner **:  오너는 로직 업그레이드 권한을 갖으며, 설정값들을 설정할 수 있다. 

# ABI

# Storage

```javascript
address public l2RegistryForVerify; // L2Registry
address public operatorFactory;

address public ton;
address public wton;
address public dao;
address public depositManager;
address public seigManager;
address public swapProxy;

uint256 public minimumInitialDepositAmount;

/// issueStatus for giving seigniorage
/// systemConfig - stateIssue ( 0: none , 1: registered, 2: paused )
mapping (address => uint8) public issueStatusLayer2;

/// systemConfig - operator
mapping (address => address) public operatorOfSystemConfig; 

/// operator - systemConfig
mapping (address => address) public systemConfigOfOperator;

/// operator - layer2Candidate
mapping (address => address) public layer2CandidateOfOperator;

```

# Event

```javascript
event SetAddresses(
        address _l2RegistryForVerify,
        address _operatorFactory,
        address _ton,
        address _wton,
        address _dao,
        address _depositManager,
        address _seigManager,
        address _swapProxy
);

event SetMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount);

event RegisteredLayer2Candidate(address systemConfig, uint256 wtonAmount, string memo, address operator, address layer2Candidate);
 

```

# Functions 

```javascript

modifier onlyL2Register() {
    require(l2Register == msg.sender, "sender is not a L2Register");
    _;
}

modifier onlySeigManger() {
    require(seigManager == msg.sender, "sender is not a SeigManager");
    _;
}
```

## onlyOwner

```solidity
 function setAddresses(
        address _l2Register,
        address _operatorFactory,
        address _ton,
        address _wton,
        address _dao,
        address _depositManager,
        address _seigManager,
        address _swapProxy
    )  external  onlyOwner 


function setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)  external  onlyOwner
 
     
```

## onlySeigManger

```solidity
 function updateSeigniorage(address systemConfig, uint256 amount) external onlySeigManger
```

## anyone

```solidity
 function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool)
   // data : _systemConfig(20bytes), memo(string)

function registerLayer2Candidate(
        address systemConfig,
        uint256 amount,
        bool flagTon,   // if true , use TON , otherwise use WTON 
        string calldata memo
) external;



function checkLayer2TVL(address _systemConfig) public view returns (bool result, uint256 amount) 

function claimableSeigniorage(address systemConfig) public view returns (uint256 amount)  
```

# Test  ( using Titan on Mainnet fork) 

A scenario where Titan's Layer2Candidate is created, deposited, seigniorage is issued, and withdrawal is made.

`npx hardhat test test/layer2/units/2.Layer2Manager.test.ts`

test script : [link](https://github.com/tokamak-network/ton-staking-v2/blob/Layer2Manager/test/layer2/units/2.Layer2Manager.test.ts)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a252c1ea-c452-4311-900c-651064632408/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.10.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWJ5BHE3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzjC%2FtS6vTFAprfH1LHQyTylGgqCayz8bB7fa4lIBT2AiB2nWYGyZ0v%2B%2BUg4UUg%2BzgOCtQHfEdK3aWenXKCScUOpCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM%2BcF47Zu2LKBkqMqlKtwDj28GSEfenE3weEl0APEVIPUIt%2F7X4R%2BLl7AdmkwWFF%2FVyCfzgJisYUjLn5R8e42uZ0z8FMOQO8aEgTdoKRz9nBYBiZlUpVn%2FNjAGv%2FHhcTzNXyyyMmF3iwre7Bd4wlBzQrvH4FVB7JLIzbTiszF2OV9EXCQWCjNpuZHafd%2FMRR%2BZMQpvwruXe7nSuonmuM2VdqRvgfyy2MvjsfRk3DUs01lmc5YMdHEIvI%2BelXMMaYaiN%2FhGSUOxgw0KOQs5hifUnG5xeRjzIEID%2FAxG%2B%2BAMkDKUpBAH83ECts3IqmZNHXXJrU9%2FGZ3gVg6XtBs8Fwq%2FYKG1Sfd3C56y%2BuWdZKyvWTMHf5ZmBcLFWzW6ouT1I5ubGaV4Rgm7RdiPcrBj8E7rORVmF9FE87CA3dGNzbGsX67bk%2FLJNQFYymUMy%2F4XdO0%2Fvd3Cf07FO7DMg%2FmCVYlwnf0w5o0gxzRPepYHsOQVZ7zSLW8JPwhgfbhC%2FF5WcEuE1HOGqwdjWFV1Fypfc%2Bsl3p%2BJj63r4VUveuBw5onbjiUpihSa4pUnnLrr3NBa9d%2Bay2lPBggwZCzqwPtHo089mzcFKvEZkSLtusv4UwZub7xV1Hk91JDlOWwkisBErGd8Ot0BpM9FT%2Fked%2FMwrZrbzAY6pgHbcl%2BTCj2xVi8Vrrl7VtoBMWeyjlWqL77nYLYk69CqVt6g%2Ff7tFHwjy0ygvcDvfqrReI4W47n4BsOAc8yVGgkttYOQQ4CHnKxO5I23nU2Db8WBEMypHUVznGTpqaObmvLHfPNQxjXaHNcvk23vu2iCZeFtaPP%2BNj%2FBiGS%2FnNCP6hR34MhZ7kTABNMQF465W4f03I9xl8%2BDynHgKontmR9r4hGRn3Xl&X-Amz-Signature=2f50068046b6243a15264262d8990fb49691d961e7391024acba0df718e5b32e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/902701da-6a9c-4295-a398-ff7a96066c2c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.11.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWJ5BHE3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzjC%2FtS6vTFAprfH1LHQyTylGgqCayz8bB7fa4lIBT2AiB2nWYGyZ0v%2B%2BUg4UUg%2BzgOCtQHfEdK3aWenXKCScUOpCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM%2BcF47Zu2LKBkqMqlKtwDj28GSEfenE3weEl0APEVIPUIt%2F7X4R%2BLl7AdmkwWFF%2FVyCfzgJisYUjLn5R8e42uZ0z8FMOQO8aEgTdoKRz9nBYBiZlUpVn%2FNjAGv%2FHhcTzNXyyyMmF3iwre7Bd4wlBzQrvH4FVB7JLIzbTiszF2OV9EXCQWCjNpuZHafd%2FMRR%2BZMQpvwruXe7nSuonmuM2VdqRvgfyy2MvjsfRk3DUs01lmc5YMdHEIvI%2BelXMMaYaiN%2FhGSUOxgw0KOQs5hifUnG5xeRjzIEID%2FAxG%2B%2BAMkDKUpBAH83ECts3IqmZNHXXJrU9%2FGZ3gVg6XtBs8Fwq%2FYKG1Sfd3C56y%2BuWdZKyvWTMHf5ZmBcLFWzW6ouT1I5ubGaV4Rgm7RdiPcrBj8E7rORVmF9FE87CA3dGNzbGsX67bk%2FLJNQFYymUMy%2F4XdO0%2Fvd3Cf07FO7DMg%2FmCVYlwnf0w5o0gxzRPepYHsOQVZ7zSLW8JPwhgfbhC%2FF5WcEuE1HOGqwdjWFV1Fypfc%2Bsl3p%2BJj63r4VUveuBw5onbjiUpihSa4pUnnLrr3NBa9d%2Bay2lPBggwZCzqwPtHo089mzcFKvEZkSLtusv4UwZub7xV1Hk91JDlOWwkisBErGd8Ot0BpM9FT%2Fked%2FMwrZrbzAY6pgHbcl%2BTCj2xVi8Vrrl7VtoBMWeyjlWqL77nYLYk69CqVt6g%2Ff7tFHwjy0ygvcDvfqrReI4W47n4BsOAc8yVGgkttYOQQ4CHnKxO5I23nU2Db8WBEMypHUVznGTpqaObmvLHfPNQxjXaHNcvk23vu2iCZeFtaPP%2BNj%2FBiGS%2FnNCP6hR34MhZ7kTABNMQF465W4f03I9xl8%2BDynHgKontmR9r4hGRn3Xl&X-Amz-Signature=53a33e889500fb9a0fe0feb64ae15826754b8c1fdc2dae6918589513770c4ad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f83a0294-0311-491d-b6ad-3c84c695d524/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.11.13.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWJ5BHE3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzjC%2FtS6vTFAprfH1LHQyTylGgqCayz8bB7fa4lIBT2AiB2nWYGyZ0v%2B%2BUg4UUg%2BzgOCtQHfEdK3aWenXKCScUOpCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM%2BcF47Zu2LKBkqMqlKtwDj28GSEfenE3weEl0APEVIPUIt%2F7X4R%2BLl7AdmkwWFF%2FVyCfzgJisYUjLn5R8e42uZ0z8FMOQO8aEgTdoKRz9nBYBiZlUpVn%2FNjAGv%2FHhcTzNXyyyMmF3iwre7Bd4wlBzQrvH4FVB7JLIzbTiszF2OV9EXCQWCjNpuZHafd%2FMRR%2BZMQpvwruXe7nSuonmuM2VdqRvgfyy2MvjsfRk3DUs01lmc5YMdHEIvI%2BelXMMaYaiN%2FhGSUOxgw0KOQs5hifUnG5xeRjzIEID%2FAxG%2B%2BAMkDKUpBAH83ECts3IqmZNHXXJrU9%2FGZ3gVg6XtBs8Fwq%2FYKG1Sfd3C56y%2BuWdZKyvWTMHf5ZmBcLFWzW6ouT1I5ubGaV4Rgm7RdiPcrBj8E7rORVmF9FE87CA3dGNzbGsX67bk%2FLJNQFYymUMy%2F4XdO0%2Fvd3Cf07FO7DMg%2FmCVYlwnf0w5o0gxzRPepYHsOQVZ7zSLW8JPwhgfbhC%2FF5WcEuE1HOGqwdjWFV1Fypfc%2Bsl3p%2BJj63r4VUveuBw5onbjiUpihSa4pUnnLrr3NBa9d%2Bay2lPBggwZCzqwPtHo089mzcFKvEZkSLtusv4UwZub7xV1Hk91JDlOWwkisBErGd8Ot0BpM9FT%2Fked%2FMwrZrbzAY6pgHbcl%2BTCj2xVi8Vrrl7VtoBMWeyjlWqL77nYLYk69CqVt6g%2Ff7tFHwjy0ygvcDvfqrReI4W47n4BsOAc8yVGgkttYOQQ4CHnKxO5I23nU2Db8WBEMypHUVznGTpqaObmvLHfPNQxjXaHNcvk23vu2iCZeFtaPP%2BNj%2FBiGS%2FnNCP6hR34MhZ7kTABNMQF465W4f03I9xl8%2BDynHgKontmR9r4hGRn3Xl&X-Amz-Signature=2f195da1e1640def372dc7bdf9889a407a2714ddda6f04aea722c25c4a61166d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)