- Sepolia simple staking web 

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/)

[Simple Staking - Tokamak](https://simple-staking-v2-one.vercel.app/staking)

Repo :  [https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5](https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5)

- Sepolia ERC20 
c4f0547b-d7c5-406f-8763-2978e8de89a1 
- Sepolia Simple Staking Contracts 
  - 0ef21581-cb54-4875-b2c9-19593dbc8325 
  - b4f734dd-4f19-4e75-b2ca-f815934ee317 
- Titan-Sepolia Network 
  - ec715fc8-07cc-4b69-90ce-98192930fa55 
- Thanos-Sepolia Network 
  - 95ab153a-e004-4baa-9d61-92492eb81176 
- sepolia tokamak bridge 
[https://tokamak-bridge-pool.vercel.app/](https://tokamak-bridge-pool.vercel.app/)

# deploy process 

- DAO 

```javascript
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386

old implementation: 0xDC7e4c6cAe2123758f17D17572c6f6e820D2b431

DAOCommitteeAddV1_1 : ~~0x5AA500FA01b230EF2121c51e60c1bb1DFb1967eB

~~npx hardhat run scripts/3.deploy_DAOCommitteeAddV1_1.js --network sepolia
DAOCommitteeAddV1_1: 0x7a22429CcDbDdB13ff52d1598290186a5562b49B~~
~~
upgrade To : 0x7a22429CcDbDdB13ff52d1598290186a5562b49B
```

for sepolia 

```javascript
 
"Layer2RegistryProxy" : 0xA0a9576b437E52114aDA8b0BC4149F2F5c604581

SeigManagerProxy : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
- SeigManager : 0xe05d62c21f4bba610F411A6F9BddF63cffb43B63
- SeigManagerV1_1 : 
- SeigManagerV1_2 : 0x32Fa7147C4d82c821518B54196de680CA03BfA30 


--SeigManagerV1_3reset: 0xa996664C21f77C6C6e477150d3AfB5F41a508457

impl(0) :  0x32Fa7147C4d82c821518B54196de680CA03BfA30
impl(1):  0x7997F222986B71913Ea8f53AB9C5fd2Be00dbBf5
impl: (2) : 0
```

- DepositManager

```javascript
DepositManagerProxy : 0x90ffcc7f168dcedbef1cb6c6eb00ca73f922956f
impl(0) :  0x2d361b25395907a897f62e87A57b362264F36d7a 
impl(1): 0x82039558f14C900fC42c155281f7A4E765962b18 (not verified) 
impl(2):  DepositManager_setWithdrawalDelay : 0x7E459BC07736f735E3E758fbB740c385FB4d466B
impl(3): DepositManagerV1_1

```

### 초기값 확인하기 

이전 버전에서 배포한 값 초기화 해야 한다. 

## Deploy  Contracts On Sepolia (L1) 

## deploy v2 contracts   

`npx hardhat deploy --reset --network sepolia `

`npx hardhat deploy --network sepolia `

created contracts gas used : 2209286+1816676+1232480+1079274+1955015+2622515+1418724+2289003+1491085

setting gas used : 

```javascript
   
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }
0xc1eba383D94c6021160042491A5dfaF1d82694E6
reusing "L1BridgeRegistryV1_1" at 0x292253DF249f84e92f9a611f41DDb23D529074C8
reusing "L1BridgeRegistryProxy" at 0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC
impl_l1BridgeRegistry 0x292253DF249f84e92f9a611f41DDb23D529074C8
reusing "OperatorManagerV1_1" at ~~0x844D2A12b78ca4779Ce7d801c1Fc218Cd665677F~~
~~0xF33C5E2ABE4c052783AAed527390A77FAD5841FA
~~~~**0x7eEF8AA6C5aDEE3E9B172FFdEe91c929CBa45EB0**~~
0xB81Dafb6849DE9418155Cc937bf80A987CBDf09B


reusing "OperatorManagerFactory" at ~~0x3798D575d4C975bb49735c3c5424A98A96bF397A~~ 
~~0x013E47BBec8Ebd1FAf2AbA7047030dF05222e6b3~~
~~0x8a42BcFC2EB5D38Ca48122854B91333203332919~~
0x2CEe6117d43cFFbDcF46189Cac8928b1B7f92ABd

reusing "CandidateAddOnV1_1" at 0xf3d86064dCDDa2a89dfc23baEECaF5DBa40Ba6F2
reusing "CandidateAddOnFactory" at 0xA255C04dD8eC60a50883b9Be782bE90285d776C2
reusing "CandidateAddOnFactoryProxy" at 0x63c95fbA722613Cb4385687E609840Ed10262434
reusing "Layer2ManagerV1_1" at ~~0x6cded3D19FFA64EbF776d3F3448836E27bA925B5~~
~~0x05cbaF43D1c48Cc361436Dd36CAAd723c8546A62~~
0x53dC74EB89f4c0E9502F2ae396E283D67914Df2b
reusing "Layer2ManagerProxy" at 0xffb690feeFb2225394ad84594C4a270c04be0b55

```

## deploy SeigManagerV1_3

`npx hardhat run scripts/4.deploy_SeigManagerV1_3.js --network sepolia`

SeigManagerV1_3Logic 0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3

- add functions 
```javascript
  '0xac28e2ed', '0xbaa12536',
  '0x0c1da8df', '0x764a7856',
  '0x1fbeab54', '0xf7b99a62',
  '0x51e1e1e6', '0x6e71186b',
  '0x5f6fb8b9', '0xcf8f9110',
  '0x16b5d5bd', '0xd0d2ff70',
  '0xf9bae41a', '0x9b370dea',
  '0xca608089', '0x9473cafe'
  

0xac28e2ed,0xbaa12536,0x0c1da8df,0x764a7856,0x1fbeab54,0xf7b99a62,0x51e1e1e6, 0x6e71186b,0x5f6fb8b9,0xcf8f9110,0x16b5d5bd,0xd0d2ff70,0xf9bae41a,0x9b370dea,0xca608089,0x9473cafe 
```

  - Contract : SeigManagerProxy  0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
  - Function : setImplementation2 
    - logic : seigManagerV1_3 ⇒   0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3
    - index : 1 
    - flag : true 
    - tx: 85,129. [https://sepolia.etherscan.io/tx/0x677186ece8faea1d35205d60d6df7ca79b5149526deabbb88dff438dc84ce950](https://sepolia.etherscan.io/tx/0x677186ece8faea1d35205d60d6df7ca79b5149526deabbb88dff438dc84ce950)
  - Function : setSelectorImplementations2
    - functionBytecodes : [0xac28e2ed,0xbaa12536,0x0c1da8df,0x764a7856,0x1fbeab54,0xf7b99a62,0x51e1e1e6,0x6e71186b,0x5f6fb8b9,0xcf8f9110,0x16b5d5bd,0xd0d2ff70,0xf9bae41a,0x9b370dea,0xca608089,0x9473cafe]
    - logic :  0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3
    - tx:  229,242  [https://sepolia.etherscan.io/tx/0x8b9bfd79e85b033258ad6fe36c8502f1573784d4fc1021d3bc3bb2dd2170108a](https://sepolia.etherscan.io/tx/0x8b9bfd79e85b033258ad6fe36c8502f1573784d4fc1021d3bc3bb2dd2170108a)

## deploy DepositManagerV1_1 

`npx hardhat run scripts/5.deploy_DepositManagerV1_1.js --network sepolia`

DepositManagerV1_1 0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211

- add functions 
  - Contract : DepositManagerProxy → 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
  - Function : setImplementation2
    - logic :   0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211
    - index : 3
    - flag : true 
    - tx:  85,161    [https://sepolia.etherscan.io/tx/0xa9d7151ec0d2b396aa090cab9f74ebe9eaf86a25c8d4f1c247aa6aeb9cd48adf](https://sepolia.etherscan.io/tx/0xa9d7151ec0d2b396aa090cab9f74ebe9eaf86a25c8d4f1c247aa6aeb9cd48adf)
  - Function : setSelectorImplementations2
    - functionBytecodes : [0xcc48b947,0xdd283f97,0x96dd1d97,0x9f382d11]
    - logic :  0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211
    - tx : 88,231    [https://sepolia.etherscan.io/tx/0xc0bca20104ff3eeb270be0515e50a1d44c1c654870288f2022f2cfab7d649995](https://sepolia.etherscan.io/tx/0xc0bca20104ff3eeb270be0515e50a1d44c1c654870288f2022f2cfab7d649995)

Set SeigManager, DepositManager 

npx hardhat run scripts/7.run_set_SeigManagerV1_3.js --network sepolia

1. execute setLayer2Manager  
1. execute setL1BridgeRegistry   

## DAO update Logic 

1. add function 
1. execute setCandidateAddOnFactory
1. execute setLayer2Manager
1. execute SeigManager setTargetSetLayer2Manager 
1. execute SeigManager setTargetSetL1BridgeRegistry 

### 2. register SystemConfig by manager

- Contract : L1BridgeRegistry 
- Function : registerRollupConfigByManager 
  - _systemConfig :     
  - _type :  
  - l2TON:

### 3. Register CandidateAddOn 

- Contract : Layer2Manager
- Function : registerCandidateAddOn
  - systemConfig : 
  - amount : 1000000000000000000000
  - flag Ton : true 
  - memo:  

## titan-sepolia, thanos-sepolia CandidateAddOn 배포 정보 

exec: `npx hardhat run scripts/sepolia-stakingv2-register/0.register_titan-sepolia.js --network sepolia`

- Titan-sepolia 
```javascript

const titan_info = {
  systemConfig : "0x1cA73f6E80674E571dc7a8128ba370b8470D4D87",
  type: 1,
  amount: ethers.BigNumber.from("1000100000000000000000"),
  flagTon: true,
  name: "Titan-sepolia",
  bridge: "0x1F032B938125f9bE411801fb127785430E7b3971",
  portal: "",
  l2TON: "0x7c6b91d9be155a6db01f749217d76ff02a7227f2"
}
  
  owner : 0xc1eba383D94c6021160042491A5dfaF1d82694E6 
  
  tx 
```
- Thanos-sepolia 
```javascript

const thanos_info = {
  systemConfig : "0xB8209Cc81f0A8Ccdb09238bB1313A039e6BFf741",
  type: 2,
  amount: ethers.BigNumber.from("1000100000000000000000"),
  flagTon: true,
  name: "Thanos-sepolia",
  bridge: "0x385076516318551d566CAaE5EC59c23fe09cbF65",
  portal: "0x7b6db1316e22167b56211cDDC33431098BaBC3c2",
  l2TON: "0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000"
}
  
  owner : 0x7cf8aD47c1B5E18cd827633F9e25538A08dB5448 
  
  tx: 
```

```javascript
titan_rollupConfigInfo [
  1,
  '0x7afEfd134118B7eCbF25F9E4e73C1aef8BE0603d',
  status: 1,
  operatorManager: '0x7afEfd134118B7eCbF25F9E4e73C1aef8BE0603d'
]
thanos_rollupConfigInfo [
  1,
  '0xEE85eD759BcE873e0946448a7Fa922A3f177955F',
  status: 1,
  operatorManager: '0xEE85eD759BcE873e0946448a7Fa922A3f177955F'
]
titan_CandidateAddOnInfo [
  '0x1cA73f6E80674E571dc7a8128ba370b8470D4D87',
  '0x4400458626eb4d7fc8f10811e9A2fB0A345a8875',
  rollupConfig: '0x1cA73f6E80674E571dc7a8128ba370b8470D4D87',
  candidateAddOn: '0x4400458626eb4d7fc8f10811e9A2fB0A345a8875'
]
thanos_CandidateAddOnInfo [
  '0xB8209Cc81f0A8Ccdb09238bB1313A039e6BFf741',
  '0x0e5417d597CC19abFb477Fa7e760AdcABDfe60E2',
  rollupConfig: '0xB8209Cc81f0A8Ccdb09238bB1313A039e6BFf741',
  candidateAddOn: '0x0e5417d597CC19abFb477Fa7e760AdcABDfe60E2'
]
```

### Simple Staking Web 

 

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/) 에 자동으로 등록된 것 확인하기 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c7331f5-2617-43bc-99fe-6aaab5686acd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-08-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.35.29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJZBMWIT%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDGwG6fFH33yHEsPrUg1v9bXIa8PglUgdKLiOeLZ9yWsAiBrbHWjyotlR7ANAXjZsbra%2BTgI9gjoHYs%2F31D5TjHoTir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMQdLkSYrDz9YPuruZKtwDJqfEczUqU6DUjt6X1XKm9onN5sfd2I%2BOFeW8z7ASkMiZX8Ooi3Mo1EktNqeXssGuUV2MPwYxo2tO94H3H6zg%2BhXAARhNAi8inhuy4%2FDgXt0blr4LTtQ7q6CgImEQgwnABb13U4HZdyMy3HfOV1s6Tnn64pU3sI3BoKt8aMVgUTTBpQvBXZ6YzZzkKiZbfe4zMWDiJ%2FAVtFATFK%2BnvTWvy22AtmXU%2B%2B%2BWopKiMKUDaVetiG3Fp4VwosJdkX1QXm6cEAq3YYYNg5Sh9q8LzDTDCmA4HJRn%2Fb%2Bw1QfUC5EBAmsWJ%2BFRD6Bdm5fkyhpyDhOFwcC4Nxj%2BqF0UTxE6PxuYBAfp1crJFdG4tQoOiAJ7cd7yyKbzRXJXb8I%2BtRQFAMk3rIcv8gdH84Y0M0HnBwaes4F3giQx%2Ftwpj6O9XZBAUe42cwWbeDYaiwxW5o%2FL05u4w2nI18AzYbdhYkyHdu1pO%2FbHCz8fbu3jTIcXY0LKpamlIf0evtOVNiZViDkFJ5hYYv0kOeNr4Ef9ayCTOEzn%2BgczM%2BkRNvfTmfLniklwsPOgEiI3hNintc2436WPjby9vEpU9SQnGBT94sktS%2B5tmLWxeeHnRMpE07kXBSwTg3qKNA0s3GeG%2BGBJigQwnJnbzAY6pgFyG1Dt2Z6vTDgsnjtDHHG2tO9Egklw%2Bye1oYxlMIqGyBE4r42oIFYoeuzO0bBe9L2Gs2pNgNHo9THk%2FLEo7rYjCGBTR2wS9GHuWYLbKXV9L%2B39mr%2BkRSI5sJO1RGeDjINvfzvpAclqWJL34oGPWRwO7VQ%2FwRAOdDCHxuyBREzT3U8I5RE5NehN1ctY3GlZCrpgj7qMpkL5xUbEf6VO8dEMUSlZA%2FGO&X-Amz-Signature=0a6d55bb4d804f5bdd84e4cd104660f4d08b996dff1dd3511165259312e33ab8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Test 

[https://github.com/tokamak-network/ton-staking-v2/issues/12](https://github.com/tokamak-network/ton-staking-v2/issues/12)

1. test update seigniorage of Layer2Candidate  and DAOCandidate   [code](https://github.com/tokamak-network/ton-staking-v2/blob/deploy_sepolia_v2/test/layer2/sepolia_test/1.updateSeigs.ts)
1. test withdrawAndDepositL2 function of Layer2Candidate [code](https://github.com/tokamak-network/ton-staking-v2/blob/deploy_sepolia_v2/test/layer2/sepolia_test/2.withdrawAndDepositL2.ts) 
1. test to execute updateSeignorage and Claim concurrently of Operator(sequencer)     [code](https://github.com/tokamak-network/ton-staking-v2/blob/deploy_sepolia_v2/test/layer2/sepolia_test/3.updateSeigsAndClaim.ts)
1. test to execute updateSeignorage and Staking concurrently of Operator(sequencer)  [code](https://github.com/tokamak-network/ton-staking-v2/blob/deploy_sepolia_v2/test/layer2/sepolia_test/4.updateSeigsAndStake.ts) 


# Addresses on sepolia 

```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
```

```javascript
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }  
reusing "L1BridgeRegistryProxy" at 0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC
impl_l1BridgeRegistry 0x292253DF249f84e92f9a611f41DDb23D529074C8 
 

reusing "OperatorManagerFactory" at 0x8a42BcFC2EB5D38Ca48122854B91333203332919 
reusing "CandidateAddOnFactory" at 0xA255C04dD8eC60a50883b9Be782bE90285d776C2
reusing "CandidateAddOnFactoryProxy" at 0x63c95fbA722613Cb4385687E609840Ed10262434 
reusing "Layer2ManagerProxy" at 0xffb690feeFb2225394ad84594C4a270c04be0b55
```

#  