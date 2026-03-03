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

createCanddiateAddOn memo, manager address
```

- 2024.10.01 현재 상태 

```javascript
DAOCommitteeProxy 0xA2101482b28E3D99ff6ced517bA41EFf4971a386

impl : 0x399A7Aa3BF8da93319494CdFC495Ab20541eC1D4. DAOCommitteeProxy2

DAOCommitteeProxy2
implementation : 0x399A7Aa3BF8da93319494CdFC495Ab20541eC1D4

implementation2(0) : 0xaDf24e3885D4c8DB092514dF364b09f314F1e794 DAOCommittee_V1
implementation2(1) : 0x63f116823B6Ed37271B0204A51e8ea4Eaa09c9a6 DAOCommitteeOwner
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
impl(1):  ~~0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3 ~~
           **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**
impl: (2) : 0
SeigManagerV1_3Logic : ~~0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3
~~              **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**

```

- DepositManager

```javascript
DepositManagerProxy : 0x90ffcc7f168dcedbef1cb6c6eb00ca73f922956f
impl(0) :  0x2d361b25395907a897f62e87A57b362264F36d7a 
impl(1): 0x82039558f14C900fC42c155281f7A4E765962b18 (not verified) 
impl(2):  DepositManager_setWithdrawalDelay : 0x7E459BC07736f735E3E758fbB740c385FB4d466B
impl(3): ~~0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211~~  **0x14b288C49C3aCc125CF88AADe631B52Fa4C2e679 **DepositManagerV1_1
```

           

### 초기값 확인하기 

이전 버전에서 배포한 값 초기화 해야 한다. 

## Deploy  Contracts On Sepolia (L1) 

## deploy v2 contracts   (배포완료)

`npx hardhat deploy --network sepolia `

created contracts gas used : 2209286+1816676+1232480+1079274+1955015+2622515+1418724+2289003+1491085

setting gas used : **16114058 * **

가스 구해서 진행 

```javascript
   
minimumInitialDepositAmount BigNumber { value: "1000100000000000000000" }
developer : 0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2
reusing "L1BridgeRegistryV1_1" at 0xB1A0002AC7Aef1545069e8CB7Dd37D040BE51f33
reusing "L1BridgeRegistryProxy" at 0x58813D18b019F670d43be0D80Af968C99cc82c05
reusing "OperatorManagerV1_1" at 0xce16ad78c7ef98Fd0eEa2D9fC44E48B52fcB830e
reusing "OperatorManagerFactory" at 0xd33Cb6D1b9374362877A701C16AF48f7D0a06B0b
reusing "CandidateAddOnV1_1" at 0x9f539cd4591735C7403B18D87b62B9D69be03f29
reusing "CandidateAddOnFactory" at 0x9Ef2fF3a9Cdb42064F15a2795C0E76227F49f425
reusing "CandidateAddOnFactoryProxy" at 0x2f60005daA6294081a7688bAb9BCb21ad45b0A90
reusing "Layer2ManagerV1_1" at 0xF95147a0eA27f0803b3f35693a902564E5fF0E4f
reusing "Layer2ManagerProxy" at 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b

```

## deploy SeigManagerV1_3 (실행함)

`npx hardhat run scripts/4.deploy_SeigManagerV1_3.js --network sepolia`

SeigManagerV1_3Logic **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**

gas:  4,056,252 

- add functions 
```javascript
  '0xac28e2ed', '0xbaa12536',
  '0x0c1da8df', '0x764a7856',
  '0x1fbeab54', '0xf7b99a62',
  '0x51e1e1e6', '0x6e71186b',
  '0x5f6fb8b9', '0xcf8f9110',
  '0x16b5d5bd', '0xd0d2ff70',
  '0xf9bae41a', '0x9b370dea',
  '0xca608089', '0x9473cafe', 
  '0xcb7f9f06', '0xd3099e1e',
  '0xc5e2e745', '0x4101dd24',
  '0xd2ca6e26'
  
  

0xac28e2ed,0xbaa12536,0x0c1da8df,0x764a7856,0x1fbeab54,0xf7b99a62,0x51e1e1e6, 0x6e71186b,0x5f6fb8b9,0xcf8f9110,0x16b5d5bd,0xd0d2ff70,0xf9bae41a,0x9b370dea,0xca608089,0x9473cafe,0xcb7f9f06,0xd3099e1e,0xc5e2e745,0x4101dd24,0xd2ca6e26 
```

  - Contract : SeigManagerProxy  0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
  - Function : setImplementation2 
    - logic : seigManagerV1_3 ⇒   **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**
    - index : 2
    - flag : true 
    - tx: 85,129.  
  - Function : setSelectorImplementations2
    - **functionBytecodes : [0xac28e2ed,0xbaa12536,0x0c1da8df,0x764a7856,0x1fbeab54,0xf7b99a62,0x51e1e1e6,0x6e71186b,0x5f6fb8b9,0xcf8f9110,0x16b5d5bd,0xd0d2ff70,0xf9bae41a,0x9b370dea,0xca608089,0x9473cafe,0xcb7f9f06,0xd3099e1e,0xc5e2e745,0x4101dd24,0xd2ca6e26]**
    - logic :  **0xE9E8E5Cf8C950AA52C6A231B149454AC8612481f**
    - tx:  229,242   

## deploy DepositManagerV1_1  (실행함)

`npx hardhat run scripts/5.deploy_DepositManagerV1_1.js --network sepolia`

DepositManagerV1_1 **0xBe01894f335923dC19D0b63BFAbDfE0155D664CF**

DepositManagerV1_1 ~~0x14b288C49C3aCc125CF88AADe631B52Fa4C2e679~~

DepositManagerV1_1 ~~0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211~~

gas: 1,655,615 

- add functions 
  - Contract : DepositManagerProxy → 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
  - Function : setImplementation2
    - logic :   **0xBe01894f335923dC19D0b63BFAbDfE0155D664CF**
    - index : 3
    - flag : true 
    - tx:  85,161     
    - [https://sepolia.etherscan.io/tx/0x79dbebc022b90088e7fc4f33e13cdf7e03bbb661830f4746e900e507d6d23702](https://sepolia.etherscan.io/tx/0x79dbebc022b90088e7fc4f33e13cdf7e03bbb661830f4746e900e507d6d23702)
  - Function : setSelectorImplementations2
  - 
    - functionBytecodes : [**0xcc48b947,0xdd283f97,0x96dd1d97,0x9f382d11,0xcf8f9110,0x16b5d5bd,0x90107afe**]
    - logic :  **0xBe01894f335923dC19D0b63BFAbDfE0155D664CF**
    - tx : 88,231     

 

— 값체크 

`npx hardhat test test/layer2/sepolia_test/5.check_seig_dep.ts`

- Set SeigManager,  

npx hardhat run scripts/7.run_set_SeigManagerV1_3.js --network sepolia

1. execute setLayer2Manager  
1. execute setL1BridgeRegistry   
- DepositManager 의 스토리지는 세그매니저에서 조회해서 자동으로 설정됨. 

## DAO update Logic 

1. add function 
1. execute setCandidateAddOnFactory
 "CandidateAddOnFactoryProxy" at 0x2f60005daA6294081a7688bAb9BCb21ad45b0A90
1. execute setLayer2Manager
 "Layer2ManagerProxy" at 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b
1. execute SeigManager setTargetSetLayer2Manager 
 "Layer2ManagerProxy" at 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b
1. execute SeigManager setTargetSetL1BridgeRegistry 
 "L1BridgeRegistryProxy" at 0x58813D18b019F670d43be0D80Af968C99cc82c05

### 2. register SystemConfig by manager

- Contract: L1BridgeRegistry  0x58813D18b019F670d43be0D80Af968C99cc82c05
- Function: registerRollupConfigByManager 
  - _systemConfig :     
  - _type :  
  - l2TON:
  - Titan Sepolia
[https://sepolia.etherscan.io/tx/0x5902b7ecdf5a2fa2df3aa76c8761710a6c427fde2ff997f65525d65ff8d5913a](https://sepolia.etherscan.io/tx/0x5902b7ecdf5a2fa2df3aa76c8761710a6c427fde2ff997f65525d65ff8d5913a)

```javascript
const titan_info = {
  systemConfig : "0x1cA73f6E80674E571dc7a8128ba370b8470D4D87",
  type: 1,
  amount: ethers.BigNumber.from("1000100000000000000000"),
  flagTon: true,
  name: "Titan Sepolia",
  bridge: "0x1F032B938125f9bE411801fb127785430E7b3971",
  portal: "",
  l2TON: "0x7c6b91d9be155a6db01f749217d76ff02a7227f2"
}
```
  - Thanos Sepolia
    - [https://sepolia.etherscan.io/tx/0xa269cdcbbfbcea760f359288535b224df864b14230d643926a53f8f7b0d65df3](https://sepolia.etherscan.io/tx/0xa269cdcbbfbcea760f359288535b224df864b14230d643926a53f8f7b0d65df3)

```javascript
const thanos_info = {
  systemConfig : "0xB8209Cc81f0A8Ccdb09238bB1313A039e6BFf741",
  type: 2,
  amount: ethers.BigNumber.from("1000100000000000000000"),
  flagTon: true,
  name: "Thanos Sepolia",
  bridge: "0x385076516318551d566CAaE5EC59c23fe09cbF65",
  portal: "0x7b6db1316e22167b56211cDDC33431098BaBC3c2",
  l2TON: "0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000"
}
  
```

 

### 3. Register CandidateAddOn 

- [ton.approve](https://sepolia.etherscan.io/address/0xa30fe40285b8f5c0457dbc3b7c8a280373c40044#writeContract#F2) ( layer2Manager, 1000.1 ton) 
- Contract : Layer2Manager 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b
- Function : registerCandidateAddOn
  - systemConfig : 
  - amount : 1000100000000000000000
  - flag Ton : true
  - memo:  
- Titan Sepolia
  - approve transaction  [approve](https://sepolia.etherscan.io/tx/0x5be3cb69b53cb5ac70a6a43431a0564e159c058d4cbeaa684d1a264d34929ab5) 
  - registerCandidateAddOn transaction : [https://sepolia.etherscan.io/tx/0x27434addcf117d62f6e125cdb7a5a72e3adfa95940eea3f3d130e25bab22df8c](https://sepolia.etherscan.io/tx/0x27434addcf117d62f6e125cdb7a5a72e3adfa95940eea3f3d130e25bab22df8c)
```javascript
const titan_info = {
  systemConfig : "0x1cA73f6E80674E571dc7a8128ba370b8470D4D87",
  type: 1,
  amount: ethers.BigNumber.from("1000100000000000000000"),
  flagTon: true,
  name: "Titan Sepolia",
  bridge: "0x1F032B938125f9bE411801fb127785430E7b3971",
  portal: "",
  l2TON: "0x7c6b91d9be155a6db01f749217d76ff02a7227f2"
}

operatorManager: 0xE5FB250775D559373206bA5380a7AE4CbFD5CA54
CandidateAddOn : 0xcC81D50Aae6d7d646d1AEA08917Cc84a8e35755D 

```

    - operatorManager: [https://sepolia.etherscan.io/address/0xE5FB250775D559373206bA5380a7AE4CbFD5CA54#code](https://sepolia.etherscan.io/address/0xE5FB250775D559373206bA5380a7AE4CbFD5CA54#code)
    - CandidateAddOn : [https://sepolia.etherscan.io/address/0xcC81D50Aae6d7d646d1AEA08917Cc84a8e35755D#code](https://sepolia.etherscan.io/address/0xcC81D50Aae6d7d646d1AEA08917Cc84a8e35755D#code)

[https://simple-staking-v2-one.vercel.app/staking](https://simple-staking-v2-one.vercel.app/staking)

### Simple Staking Web 

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/) 에 자동으로 등록된 것 확인하기 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c7331f5-2617-43bc-99fe-6aaab5686acd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-08-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.35.29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UDK3MAC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBsjom83vHwRdzQCmrG%2Fcek3%2Fv6JVgi4l9CmbPgiPbOvAiEAuN1Ex6h%2BWBvzU9OpUrwviql6KD005yPJTa4ufI6p5oQq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFCaC9F0%2FJll4vlPvircAwD8yQrm43zylk5RCmNfmSyBYJp3OoEdhNu7xLEp0BAMH%2F1Ehyp0LoYBftfLGSM0Nc%2BSxQA%2Fy%2B%2F4sQn3aK38hT%2B1OO0qwAX1430sF3BH%2Bxlp5gcUoLEgILr4NoubnQNAXyvn%2FhvPoRAl48TulfCiXZYvT59j1hvaKc93QhI5WkCAEHi1VjdVCu7dSwDpoxmJHBMoDXgKv8d157dvQPpLTXoJjJ9yLCoXGJWsTQGqF3NpcVqkyM2PaksDEjf9ppTDJRFdh0%2B4CVX6xxZ5Q2ExFGLGtYUQ2olpf35w4CHNBXGQSdSxuIZXIVIGACB2UfbWsiDHCqrhJSieON%2BH65pzEVQdXK90exKbNCpGN%2BcihD8r4%2FP2wOh2Weq6FM%2FmE76h4y2OHD%2BFn3a2Mh75FdL0RcmMwANkDwV%2B8ospSfTwksgxWsVVxSDLJO5WK%2B0l0PrgOhx6bi4TpMZUIC%2F4gpLXl6XHxPBBV68qnXYEWMwmpAdrp11UYr9jnkr1xGCPboXjFgUfuu8sqULxKPRU1pkAjbYneOnycyrylj8UNaHMLUOx8r%2FLHT8vZzS8NJYLvOdFSW5X6CwsfM%2BeIlcAlkAe9Rv0xTtkKEPa7yNDIWD5Ol15R3CwhYb0XV5H67nkMNyZ28wGOqUBtQBQ6gErvXB2eUdM6ezZb4i4e82myaGpmsS88uFn9YdnsGZ9G0bDpj0X5%2BBY6eQSkVUe3tfSvt2w8E9tPEbcrcK78LcRs88u8DkobGyD8qHpdUGFvafcFGocHf3optIUfF84Hy23Yv6gCw04w1eT7vLmOui%2FkKSXZ%2BKygRZJgyOxhQKdwTMJ7ZFvwfNviIza1%2FooKzVC8WCDg3F8VJylCn9l6y16&X-Amz-Signature=def5b3786bd69cd37f93379f7bb6dd03bf8d1194fc47ffd3a73dcc40e3f66148&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Addresses on sepolia 

```javascript
"SeigManagerProxy" : 0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
"DepositManagerProxy" : 0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
```

```javascript
developer : 0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2 
 "L1BridgeRegistryProxy" at 0x58813D18b019F670d43be0D80Af968C99cc82c05 

 "OperatorManagerFactory" at 0xd33Cb6D1b9374362877A701C16AF48f7D0a06B0b 
 "CandidateAddOnFactory" at 0x9Ef2fF3a9Cdb42064F15a2795C0E76227F49f425
 "CandidateAddOnFactoryProxy" at 0x2f60005daA6294081a7688bAb9BCb21ad45b0A90 
 "Layer2ManagerProxy" at 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b

```

#  