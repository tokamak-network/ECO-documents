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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a252c1ea-c452-4311-900c-651064632408/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.10.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSZMFR3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFLb8wMQhjD1XUnFSYhGu4LI4LkhbtzsSH8HLwlXtb8zAiBsMtspi1RMIfty5tBwdEpat7k15%2BOatrR61VQHAMND2ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRiVF4LEr93kJ%2Bl%2BPKtwD5Gg%2FEiWeNuH0IL2pMlcRLSsJchRV3TswF6nvKiXwebjbctcGn1hSBGoCx9iUUTjtDLiAfe04tD2WmMiUliQj60Q80FZn2Kk92Dqy6yHo2IDamyGmhv4PVrQbMEuk2jH8m73ijaTA272xwJrib2m48nr1Iz8c4mTOeqRbGA%2BYsVViVg2%2F6jk2ydo0MUVEJbMkXcHde5aBGGBXNUQIMlr7BWNAxCuwubQ3tV9zLRtffeeSC01s8f3dIXkpj8aVNy1ITZQn%2B2AQNNOD%2B5cL4RCrxya6UYFt3Mw3u%2FCuX%2FYQFkkOKMre%2BJvgUB%2B3HkshtCmp4aj%2F9yiydVp76XbjHAPd46jFWhUkgKf9G59SfD9Er67OQboqOOEie6wSgAGJZg42wYdK0RFEj%2BqBeCP4snzdHx2yIp9zcudvjE08F0Ud36C5YLpTwVL262Cv77Clb5YcMAO11sQGe%2BI%2FWGlGBGWVvDch8vF3VOY%2B1XKO5DfqnxrUKyQT7TLO6cMyMzPV%2BvXhtmQYZTy7fxNjXLGSMA%2BsgAhY3K0cjOnDjdiJMPL91wm5Xhiyy7dc%2FwCzmOIvhwrjirA31bMCEhP8mwzYmQvP2VuM22q%2Fw%2F2B8DCHbZR077SzY7jBerZW317UbJcw3e7ZzAY6pgFDLbih2M008BBsPFcj3o5Hg98Rgs6ZmibVO1jmCsSmOEAR0POxww2hzb2XwduZUldSA5U53AICheEWI8uzuaQ6ZF5AuVt6RN%2F92nDq7WfnBxnzKfCoB0%2F9JushQBxGDdEC1UBi8YRJ%2F8Q2jUUb3tci%2BlR9jG91jj1Slx9m%2BYEPg5fBDK0EsqMm%2B7tt4s3FvBeYhBas8eJ1BBbautBIGcWpFPDsXYwz&X-Amz-Signature=73f53d6cc3693b4d3788f3d09151ad8999d4bdb044d735df902c2d97513f8cfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/902701da-6a9c-4295-a398-ff7a96066c2c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.11.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSZMFR3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFLb8wMQhjD1XUnFSYhGu4LI4LkhbtzsSH8HLwlXtb8zAiBsMtspi1RMIfty5tBwdEpat7k15%2BOatrR61VQHAMND2ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRiVF4LEr93kJ%2Bl%2BPKtwD5Gg%2FEiWeNuH0IL2pMlcRLSsJchRV3TswF6nvKiXwebjbctcGn1hSBGoCx9iUUTjtDLiAfe04tD2WmMiUliQj60Q80FZn2Kk92Dqy6yHo2IDamyGmhv4PVrQbMEuk2jH8m73ijaTA272xwJrib2m48nr1Iz8c4mTOeqRbGA%2BYsVViVg2%2F6jk2ydo0MUVEJbMkXcHde5aBGGBXNUQIMlr7BWNAxCuwubQ3tV9zLRtffeeSC01s8f3dIXkpj8aVNy1ITZQn%2B2AQNNOD%2B5cL4RCrxya6UYFt3Mw3u%2FCuX%2FYQFkkOKMre%2BJvgUB%2B3HkshtCmp4aj%2F9yiydVp76XbjHAPd46jFWhUkgKf9G59SfD9Er67OQboqOOEie6wSgAGJZg42wYdK0RFEj%2BqBeCP4snzdHx2yIp9zcudvjE08F0Ud36C5YLpTwVL262Cv77Clb5YcMAO11sQGe%2BI%2FWGlGBGWVvDch8vF3VOY%2B1XKO5DfqnxrUKyQT7TLO6cMyMzPV%2BvXhtmQYZTy7fxNjXLGSMA%2BsgAhY3K0cjOnDjdiJMPL91wm5Xhiyy7dc%2FwCzmOIvhwrjirA31bMCEhP8mwzYmQvP2VuM22q%2Fw%2F2B8DCHbZR077SzY7jBerZW317UbJcw3e7ZzAY6pgFDLbih2M008BBsPFcj3o5Hg98Rgs6ZmibVO1jmCsSmOEAR0POxww2hzb2XwduZUldSA5U53AICheEWI8uzuaQ6ZF5AuVt6RN%2F92nDq7WfnBxnzKfCoB0%2F9JushQBxGDdEC1UBi8YRJ%2F8Q2jUUb3tci%2BlR9jG91jj1Slx9m%2BYEPg5fBDK0EsqMm%2B7tt4s3FvBeYhBas8eJ1BBbautBIGcWpFPDsXYwz&X-Amz-Signature=3141e986e91b9a7d4343d92f92d7d4aa0c6667165e5134e02f7ee5edef3c5c7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f83a0294-0311-491d-b6ad-3c84c695d524/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.11.13.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSZMFR3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFLb8wMQhjD1XUnFSYhGu4LI4LkhbtzsSH8HLwlXtb8zAiBsMtspi1RMIfty5tBwdEpat7k15%2BOatrR61VQHAMND2ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRiVF4LEr93kJ%2Bl%2BPKtwD5Gg%2FEiWeNuH0IL2pMlcRLSsJchRV3TswF6nvKiXwebjbctcGn1hSBGoCx9iUUTjtDLiAfe04tD2WmMiUliQj60Q80FZn2Kk92Dqy6yHo2IDamyGmhv4PVrQbMEuk2jH8m73ijaTA272xwJrib2m48nr1Iz8c4mTOeqRbGA%2BYsVViVg2%2F6jk2ydo0MUVEJbMkXcHde5aBGGBXNUQIMlr7BWNAxCuwubQ3tV9zLRtffeeSC01s8f3dIXkpj8aVNy1ITZQn%2B2AQNNOD%2B5cL4RCrxya6UYFt3Mw3u%2FCuX%2FYQFkkOKMre%2BJvgUB%2B3HkshtCmp4aj%2F9yiydVp76XbjHAPd46jFWhUkgKf9G59SfD9Er67OQboqOOEie6wSgAGJZg42wYdK0RFEj%2BqBeCP4snzdHx2yIp9zcudvjE08F0Ud36C5YLpTwVL262Cv77Clb5YcMAO11sQGe%2BI%2FWGlGBGWVvDch8vF3VOY%2B1XKO5DfqnxrUKyQT7TLO6cMyMzPV%2BvXhtmQYZTy7fxNjXLGSMA%2BsgAhY3K0cjOnDjdiJMPL91wm5Xhiyy7dc%2FwCzmOIvhwrjirA31bMCEhP8mwzYmQvP2VuM22q%2Fw%2F2B8DCHbZR077SzY7jBerZW317UbJcw3e7ZzAY6pgFDLbih2M008BBsPFcj3o5Hg98Rgs6ZmibVO1jmCsSmOEAR0POxww2hzb2XwduZUldSA5U53AICheEWI8uzuaQ6ZF5AuVt6RN%2F92nDq7WfnBxnzKfCoB0%2F9JushQBxGDdEC1UBi8YRJ%2F8Q2jUUb3tci%2BlR9jG91jj1Slx9m%2BYEPg5fBDK0EsqMm%2B7tt4s3FvBeYhBas8eJ1BBbautBIGcWpFPDsXYwz&X-Amz-Signature=7be2599eaf5739e079cc4ee23d6909d09cdc4bd1fd4a55df8ccecfc6c82e1dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)