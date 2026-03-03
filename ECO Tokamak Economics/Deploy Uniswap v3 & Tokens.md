[[simulation: deploy uniswap on titan-goerli]]

[[simulation2: deploy uniswap on titan-goerli  ]]

[[pools info, titan-goerli]]

유니스왑 관련된거 싹 다 적어주시고, 지금 현재 0.8버전에 걸려있는 LP id 집계를 해야한다. 거기 유동성이 다 빠져야한다. Smart Router탭하나 만들면 제나님이 업데이트해주실거다.

다른 도메인도 적어주시면 각각 프론트사이트도 달라집니다.

적힌 노션도 하나 있으면 반영해서 알려드리겠습니다.

일정은 어떻게 잡으면 될까요? : 타이탄 고엘리꺼 먼저 작동되는지 하시고, 그다음에 한번 얘기를 해보죠.

타이탄 메인넷에 있는 LP는 내부적으로 일단, 더이상 만들지 말라고 notice를 해주겠다.

titan - goerli를 다시 잡아주고. 수요일날 (컨트랙트팀 콜 캔슬하고 콜), titan-goerli만 한다.

수요일, 목요일 테스트하고, 금요일 오전에 하면될것같아요. (오전 10시)

프론트엔드 작업하고, 타이탄 고엘리 기준으로 프론트에서 문제가 없다고 하면, 그때 메인넷 스케줄 잡으면 된다.

일정이 늦춰지면 말씀을 달라… (에러나는 사항)

상세 내용을 정리해서 미디움글로 올린다.

제이슨이, 오늘 출산휴가를 간다. 바로는 안갈텐데 그 전에 끝내는게 좋을 것 같다. 서브그래프도 새로 배포해야한다. (titan-goerli)로.

**deployer address **: **0xE49c9ea00337182374E112C452247A2D1db61798 **

필요한 가스 : OVM_GasGracle: **0x420000000000000000000000000000000000000F**

1. Deploy UniswapContracts + (Permit2) :  30413266 + **3849570 = 34262836**
1. 0.01Fee Activation : **47916**
1. Set Owner : 25798

**34262836 + 47916 + **25798 = **34336550**

**34336550 * 250000 = 8584137500000 ⇒ 0.0000085841375 ETH**

---

**address **: **0xB68AA9E398c054da7EBAaA446292f611CA0CD52B**

1. Approve NonfungiblePositionManager TON,TOS,WETH,USDC,USDT : **231328**
1. createAndInitialize TOS_TON, WETH_TOS, WETH_TON, WETH_USDC, WETH_USDT  : **22851506**
1. mint(add_liquidity) TOS_TON, WETH_TOS, WETH_TON, WETH_USDC, WETH_USDT : **2932014**

**231328 + 22851506 + 2932014 = 26014848**

**26014848 * 250000 = 6.503712e+12 ⇒ 6503712000000 ⇒ 0.000006503712 ETH **

- 유동성 제공
0.112 ETH =⇒ 0.112 + **0.000006503712  = 0.11200650371**
70 TON
50 TOS
50 USDC
50 USDT

---

**address **: 0x6dDE76BD012Af35d7d2e2F6E23700Cc101DDead0

Deploy (Unsupported + UniversalRouter) = 4035126

4035126 * gasPrice(250000) = 0.0000010087815 ETH **+ α**

---

# 필요한 가스 

- Justin 
  - for uniswap deployment + liquidity
- [x] **L2**: 0xE49c9ea00337182374E112C452247A2D1db61798** : 0.00102 ETH **
- [ ] **L2**: 0xB68AA9E398c054da7EBAaA446292f611CA0CD52B :  

      **0.11201 ETH (gas + liquidity) + ( 0.0011 ETH for swap Test) = **

- [x] **L2**: 0x6dDE76BD012Af35d7d2e2F6E23700Cc101DDead0 : 0.001002 ETH 
- Zena
  - for deterministic proxy deployment
- [x] **L2: **0x3fab184622dc19b6109349b94811493bf2a45362 : **0.011 ETH **  
  - for token deployment
- [ ] **L2: **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F : **0.000002 ETH**
- Harvey
  - for BridgeSwap deployment  
- [x] **L1** : 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea : **0.2 ETH , 2TON, 2WTON, 0.02WETH**

[https://docs.google.com/spreadsheets/d/19quEPPYYT7eJSgAY-cp46Qqbk9NF2o9YFIax8SlncTM/edit#gid=0](https://docs.google.com/spreadsheets/d/19quEPPYYT7eJSgAY-cp46Qqbk9NF2o9YFIax8SlncTM/edit#gid=0)

# 필요한 재단 주소 

1. Uniswap V3 Factory Owner 
  - **0x340C44089bc45F86060922d2d89eFee9e0CDF5c7**
1. USDC Token Owner
  -  **0x340C44089bc45F86060922d2d89eFee9e0CDF5c7**

# 1. deterministic deployment proxy

> git: [https://github.com/Zena-park/deterministic-deployment-proxy/tree/darius_v0.1](https://github.com/Zena-park/deterministic-deployment-proxy/tree/darius_v0.1)

> 실행 : ./deploy-proxy-at-darius.sh

0x3fab184622dc19b6109349b94811493bf2a45362 주소로 0**.**01 ETH 보내고, 실행한다.

```json
{
	"gasPrice": 100000000000,
	"gasLimit": 100000,
	"signerAddress": "3fab184622dc19b6109349b94811493bf2a45362",
	"transaction": "f8a58085174876e800830186a08080b853604580600e600039806000f350fe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe03601600081602082378035828234f58015156039578182fd5b8082525050506014600cf31ba02222222222222222222222222222222222222222222222222222222222222222a02222222222222222222222222222222222222222222222222222222222222222",
	**"address": "4e59b44847b379578588920ca78fbf26c0b4956c",**
	"data": "604580600e600039806000f350fe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe03601600081602082378035828234f58015156039578182fd5b8082525050506014600cf3"
}
```

> tx : [https://explorer.titan.tokamak.network/tx/0xeddf9e61fb9d8f5111840daef55e5fde0041f5702856532cdbb5a02998033d26](https://explorer.titan.tokamak.network/tx/0xeddf9e61fb9d8f5111840daef55e5fde0041f5702856532cdbb5a02998033d26) 

# 2. deploy uniswap 

@Unknown 

---

> **계정 : 0xE49c9ea00337182374E112C452247A2D1db61798 (Metamask계정이름 : TitanDeployer), 계정 .env 파일 Private Key 셋팅**

### 2-1. Uniswap V3

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat tokamak-uniswap-v3-deploy --network titan
```

deployed address (주소확인) (v0.8)

```json
{
  "UniswapV3Factory": "0x8C2351935011CfEccA4Ea08403F127FB782754AC",
  "SwapRouter": "0x365FC907394A4858EcdbF24b874048C0bBF54CE9",
  "NFTDescriptor": "0x39463E80fb909827C8DDB27953264A7B6c2cE0c9",
  "NonfungibleTokenPositionDescriptor": "0xDC1Fa1B1F3d28E23A2877Fe2de80224aF4e944A2",
  "NonfungiblePositionManager": "0x324d7015E30e7C231e4aC155546b8AbfEAB00977",
  "Quoter": "0xE3a8EbF3f0bC0f752C44737533E4a5273b201dE4",
  "QuoterV2": "0x4Fe186d98bbb99C4B2f9c8c7F82E1Bb8231CF4d6",
  "TickLens": "0x15054be74B3957d038c2FCC983D6Ccc0D441fE67",
  "UniswapInterfaceMulticall": "0x0A6F0A493a2eec1822D95D1A4A30D747ae285777",
  "BancorConverterRegistry": "0xb3d480c1249DB2ab8ED0ff628EDCe37A86155139",
  //"SwapRouter02": "0x9Cabe266e34C7B60858BD55B0a3C00b83e511619", (새주소로 바뀜 바로 아래 참고)
  "UniswapV3PoolSwapTest": "0xCd07B2845B6997FA181742dA8CA77C16d599E1E3",
  "Multicall": "0x2C86Fa58c3FAb8AD5860aF8222Fb375a5634F1AD",
	"Permit2": "0x66d2011D1C9a11a37c816180886f9aE975e7fE5F**",
	"**UniversalRouter**": "**0xC4cDD44DA6824582A4Fd819B5Ab7b7924a8834Ef**",
	"**Unsupported**": "**0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759**",**
}
```

SwapRouter02 : 0x1316822b9d2EEF86a925b753e8854F24761dA80E (새주소)

deployer 0x303fA4366973C510d25AA003b48313fA1556f520

> verify : 

1. V3-Core (Factory) 완료

```json
npx hardhat run scripts/verify.js --network titan
```

1. V3-Periphery (NonfungiblePositionManager, SwapRouter, NFTDescriptor, NonfungibleTokenPositionDescriptor, NonfungiblePositionManager, Quoter, QuoterV2, TickLens, UniswapInterfaceMulticall) 완료

```json
npx hardhat run scripts/verify.js --network titan
```

1. tokamak-uniswap-v3-contract (Mulltical, UniswapV3PoolSwapTest, BancorConverterRegistry) 완료

```json
npx hardhat run scripts/v3/mainnet/0.verify.js --network titan
```

1. tokamak-swap-router-contracts (SwapRouter02) 완료

```json
npx hardhat run scripts/verify.js --network titan
```

### 2-2. 0.01Fee Activation : enableFeeAmount(100,1) onlyOwner

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/0.100_fee.js --network titan
```

> tx: 
> transactionHash: 0x38c2fc6097ef9cb5c65f8782b2c561ec93fe6b500cc29c1dabe66192a7f1d148
> gasUsed:  BigNumber { value: "47916" }
> ETH_Used 0.000000011979007089

### 2-3. Set Owner to Tokamak address

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 실행 전 : Tokamak address 셋팅 필요

```json
npx hardhat run scripts/v3/mainnet/0.set_owner.js --network titan
```

> tx: 
> transactionHash: 0xe91ccb5a3f88433d7ba4796321326b39d86f32650f7607597766f67175c854e5
> gasUsed:  BigNumber { value: "28598" }

### 2-4. Permit2

> git: [**universal-router**](https://github.com/usgeeus/universal-router)

> 실행 : 실행전 **<private key> 셋팅 (화면안보이게)**

```json
forge script --legacy --broadcast \
--rpc-url https://rpc.titan.tokamak.network \
--private-key <private-key> \
--sig 'run()' \
script/deployParameters/DeployTokamak.s.sol:DeployTokamak \
--etherscan-api-key WM7SZ8W48JWGVZ7CA2QHJMM76SW45UPB38 \
--verify
```

Permit2 address  : [**0x66d2011D1C9a11a37c816180886f9aE975e7fE5F**](https://explorer.titan.tokamak.network/address/0x66d2011D1C9a11a37c816180886f9aE975e7fE5F/contracts#address-tabs)

> verify : 완료

```json
forge verify-contract --chain 55004 --watch --verifier etherscan --verifier-url https://explorer.titan.tokamak.network/api 0x66d2011D1C9a11a37c816180886f9aE975e7fE5F lib/permit2/src/Permit2.sol:Permit2 WM7SZ8W48JWGVZ7CA2QHJMM76SW45UPB38
```

---

> **계정 : 0x6dDE76BD012Af35d7d2e2F6E23700Cc101DDead0 (Metasmask 계정이름 : unsupuniversal), script에 <private key> 셋팅**

### 2-5. UniversalRouter, Unsupported

> git: [**universal-router**](https://github.com/usgeeus/universal-router)

> 실행 : 

```json
forge script --legacy --broadcast \
--rpc-url https://rpc.titan.tokamak.network \
--private-key <private-key> \
--sig 'run()' \
script/deployParameters/DeployTokamak.s.sol:DeployTokamak \
--etherscan-api-key WM7SZ8W48JWGVZ7CA2QHJMM76SW45UPB38 \
--verify
```

 (주소확인)

UniversalRouter : 0xC4cDD44DA6824582A4Fd819B5Ab7b7924a8834Ef

Unsupported :  [0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759](https://explorer.titan.tokamak.network/address/0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759/contracts#address-tabs)

> verify : 

1. Unsupported 완료

```json
forge verify-contract --chain 55004 --watch --verifier etherscan --verifier-url https://explorer.titan.tokamak.network/api 0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759 contracts/deploy/UnsupportedProtocol.sol:UnsupportedProtocol WM7SZ8W48JWGVZ7CA2QHJMM76SW45UPB38
```

1. UniversalRouter 완료

```json
forge verify-contract --chain 5050 --watch --verifier etherscan --verifier-url https://explorer.titan.tokamak.network/api 0x86a2c829477Bd76c4634134Db2F5aADa5E94C400 contracts/UniversalRouter.sol:UniversalRouter --constructor-args $(cast abi-encode "constructor((address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,bytes32,bytes32))" "(0x768569Ba5994B73c51a5F9F7240a509157D8d00B,0x4200000000000000000000000000000000000006,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x0e8020BF0cd65959E04880c858f5b0A5ed2A0Ed8,0x8C2351935011CfEccA4Ea08403F127FB782754AC,0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f,0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54)") YY46TZ8HN26I7RKV3PKH1YE6Y9CJN7VMMS
```

or

```json
forge verify-contract --chain 55004 --watch --verifier etherscan --verifier-url https://explorer.titan.tokamak.network/api 0xC4cDD44DA6824582A4Fd819B5Ab7b7924a8834Ef contracts/UniversalRouter.sol:UniversalRouter --constructor-args 0x00000000000000000000000066d2011d1c9a11a37c816180886f9ae975e7fe5f000000000000000000000000420000000000000000000000000000000000000600000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a75900000000000000000000000059c603458f8d3c5079a0d78eb1ba28a9fae0a7590000000000000000000000008c2351935011cfecca4ea08403f127fb782754ac0000000000000000000000000000000000000000000000000000000000000000a598dd2fba360510c5a8f02f44423a4468e902df5857dbce3ca162a43a3a31ff WM7SZ8W48JWGVZ7CA2QHJMM76SW45UPB38
```

```javascript
forge verify-contract --chain 55004 --watch --verifier etherscan --verifier-url https://explorer.titan.tokamak.network/api 0xC4cDD44DA6824582A4Fd819B5Ab7b7924a8834Ef contracts/UniversalRouter.sol:UniversalRouter --constructor-args $(cast abi-encode "constructor((address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,address,bytes32,bytes32))" "(0x66d2011D1C9a11a37c816180886f9aE975e7fE5F,0x4200000000000000000000000000000000000006,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x59c603458F8d3C5079a0D78eb1BA28A9FAe0a759,0x8C2351935011CfEccA4Ea08403F127FB782754AC,0x0000000000000000000000000000000000000000000000000000000000000000,0xa598dd2fba360510c5a8f02f44423a4468e902df5857dbce3ca162a43a3a31ff)") YY46TZ8HN26I7RKV3PKH1YE6Y9CJN7VMMS
```

---

## 3. Deploy TON/TOS  

> 실행 :  **L2TokenFactory**:   [0x4200000000000000000000000000000000000012](https://explorer.titan.tokamak.network/address/0x4200000000000000000000000000000000000012/write-contract#address-tabs)  에서 실행 

- TON  
  - L1Token address : [0x2be5e8c109e2197D077D13A82dAead6a9b3433C5](https://etherscan.io/token/0x2be5e8c109e2197D077D13A82dAead6a9b3433C5#readContract)
  - Name: Tokamak Network 
  - Symbol: TON
  - Decimals : 18
  - TON L2Token address : 0x7c6b91d9be155a6db01f749217d76ff02a7227f2

> verify
> git  : [https://github.com/tokamak-network/tokamak-optimism-v2/tree/L2Token_verify/packages/contracts](https://github.com/tokamak-network/tokamak-optimism-v2/tree/L2Token_verify/packages/contracts)

```json
npx hardhat verify 0x7c6b91d9be155a6db01f749217d76ff02a7227f2 0x4200000000000000000000000000000000000010 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5 'Tokamak Network' 'TON' --network titan
```
- TOS
  - L1Token address : [0x409c4D8cd5d2924b9bc5509230d16a61289c8153](https://etherscan.io/address/0x409c4D8cd5d2924b9bc5509230d16a61289c8153#readContract)
  - Name: TONStarter
  - Symbol: TOS 
  - Decimals :18 
  - TOS L2Token address : 0xD08a2917653d4E460893203471f0000826fb4034

> verify
> git  : [https://github.com/tokamak-network/tokamak-optimism-v2/tree/L2Token_verify/packages/contracts](https://github.com/tokamak-network/tokamak-optimism-v2/tree/L2Token_verify/packages/contracts)

```json
npx hardhat verify 0xD08a2917653d4E460893203471f0000826fb4034 0x4200000000000000000000000000000000000010 0x409c4D8cd5d2924b9bc5509230d16a61289c8153 'TONStarter' 'TOS' --network titan
```

# 4. deploy USDC, USDT  

> git : [https://github.com/tokamak-network/tokamak-testnet-token/tree/use-deterministic-proxy](https://github.com/tokamak-network/tokamak-testnet-token/tree/use-deterministic-proxy)

> 실행  

```json
npx hardhat deploy —network titan
```

- USDC **  **
  - L1Token address (goerli) :   0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
  - owner : **0x340C44089bc45F86060922d2d89eFee9e0CDF5c7**
  - Name:  USD Coin
  - Symbol: USDC 
  - Decimals : 6
  - USDC L2Token address :   **0x46BbbC5f20093cB53952127c84F1Fbc9503bD6D9**

> *verify*

```json
*npx hardhat verify ***0x46BbbC5f20093cB53952127c84F1Fbc9503bD6D9*** 0x4200000000000000000000000000000000000010  0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 * **0x340C44089bc45F86060922d2d89eFee9e0CDF5c7** *'USD Coin' 'USDC' 6 --network titan *
```
- USDT **  **
  - L1Token address :  0xdac17f958d2ee523a2206206994597c13d831ec7
  - Name:  Tether USD
  - Symbol:   USDT
  - Decimals : 6
  - USDT L2Token address :   **0x2aCC8EFEd68f07DEAaD37f57A189677fB5655B46**

> *verify*

```json
*npx hardhat verify ***0x2aCC8EFEd68f07DEAaD37f57A189677fB5655B46** *0x4200000000000000000000000000000000000010 0xdac17f958d2ee523a2206206994597c13d831ec7 --network titan *
```

```json
deploying "OVMFiatToken" (tx: 0x6a9490c63d3c8de119c36fc9758d5946510d04f24d0478e3d823996e58ff6285)...: deployed at 0x46BbbC5f20093cB53952127c84F1Fbc9503bD6D9 with 1792897 gas
OVMFiatToken **0x46BbbC5f20093cB53952127c84F1Fbc9503bD6D9**
deploying "USDT" (tx: 0xedf0a893f8ab7cc25a54782d49e26eaf6253b3fda177d77eefb6aaf741265980)...: deployed at 0x2aCC8EFEd68f07DEAaD37f57A189677fB5655B46 with 942464 gas
USDT **0x2aCC8EFEd68f07DEAaD37f57A189677fB5655B46**
```

# 5. Transfer token from L1 to L2 

At Git:  [https://github.com/tokamak-network/layer2-interface-test](https://github.com/tokamak-network/layer2-interface-test)

@Zena 

From address on L1 : 0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F 

To address on L2 (justin):  **0xB68AA9E398c054da7EBAaA446292f611CA0CD52B**

- L1 Tokens 
```json
TON: 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5
TOS: 0x409c4D8cd5d2924b9bc5509230d16a61289c8153
USDC: 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
USDT: 0xdac17f9568d2ee523a2206206994597c13d831ec7
```
- L2 Tokens 
```json
"TON": "0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2",
"TOS": "0xD08a2917653d4E460893203471f0000826fb4034",
"WETH": "0x4200000000000000000000000000000000000006",
"USDC": "0x46BbbC5f20093cB53952127c84F1Fbc9503bD6D9",
"USDT": "0x2aCC8EFEd68f07DEAaD37f57A189677fB5655B46"
```
- TON : 76 TON  
  - L1 tx : [https://etherscan.io/tx/0xf85e996afa609e53fb56871b15b38cb61545199a21d817dbd1d7c86b14762e06](https://etherscan.io/tx/0xf85e996afa609e53fb56871b15b38cb61545199a21d817dbd1d7c86b14762e06)
  - L2 tx : [https://explorer.titan.tokamak.network/tx/0x71243007f83a9e45cc07413dbb52680250eaaa3b78f9114a71284b9a78ae5175](https://explorer.titan.tokamak.network/tx/0x71243007f83a9e45cc07413dbb52680250eaaa3b78f9114a71284b9a78ae5175)
- TOS : 50 TOS 
  - L1 tx  : [https://etherscan.io/tx/0xabaa5d7455c80e4fbcd98f72d08c75989b462e73e2a5d819c60c402cb5885417](https://etherscan.io/tx/0xabaa5d7455c80e4fbcd98f72d08c75989b462e73e2a5d819c60c402cb5885417)
  - L2 tx : [https://explorer.titan.tokamak.network/tx/0xed73b60c80884063d07d8dc2f11032df7d57f4b45b2b779d5aab05238adcf178](https://explorer.titan.tokamak.network/tx/0xed73b60c80884063d07d8dc2f11032df7d57f4b45b2b779d5aab05238adcf178)
- USDC : 50 USDC
  - L1 tx : [https://etherscan.io/tx/0x0f7c67ad13989c54ebe179b97d8d9c2ee3b306a20e858271466f33588362a6bf](https://etherscan.io/tx/0x0f7c67ad13989c54ebe179b97d8d9c2ee3b306a20e858271466f33588362a6bf)
  - L2 tx : [https://explorer.titan.tokamak.network/tx/0x60c99425c25c7825358a7cd8ffd866008aa5a6444c2a2bc0cc9a7117baf7880e](https://explorer.titan.tokamak.network/tx/0x60c99425c25c7825358a7cd8ffd866008aa5a6444c2a2bc0cc9a7117baf7880e)
- USDT  : 50 USDT
  - L1 tx : [https://etherscan.io/tx/0xb1a233af1cce91bc0b066957b10db3078f10535ee9e955a81ddcfcbb505d22c7](https://etherscan.io/tx/0xb1a233af1cce91bc0b066957b10db3078f10535ee9e955a81ddcfcbb505d22c7)
  - L2 tx : [https://explorer.titan.tokamak.network/tx/0x01a1f6163340f3abce2bd62f7ee5908091f8c6f4c57c716680d54c2a4e80cd18](https://explorer.titan.tokamak.network/tx/0x01a1f6163340f3abce2bd62f7ee5908091f8c6f4c57c716680d54c2a4e80cd18)
- ETH : 
  - tx 

# 6.1 Create Pool and Initialize

계정 : **0xB68AA9E398c054da7EBAaA446292f611CA0CD52B 으로 전**

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/1.create_pools.js --network titan
```

- TON/TOS
  - fee 0.3%
  - 현재 가격 1 WTON = 0.75058 TOS, 1 TOS = 1.3323 WTON (06.28 16:32 기준)
  - 유동성 제공 범위 : -40% ~ 
- ETH/TOS
  - fee 0.3%
  - 현재 가격 1 TOS = 0.0011 ETH, 1 ETH = 912.128 TOS (06.28 16:34 기준)
  - 범위  -40% ~
- ETH/TON
  - fee 0.3%
  - 현재 가격  1 ETH = 1,231.38 WTON TON, 1 WTON = 0.00081 ETH (06.28 16:35 기준)
  - 범위  -40% ~
- ETH/USDC
  - fee 0.3%
  - 현재 가격 1 ETH = 1,853.50 USDC, 1 USDC = 0.00054 ETH (06.28 16:37 기준)
  - 범위  -40% ~
- ETH/USDT
  - fee 0.3%
  - 현재 가격 //USDC 와 동일하게
  - 범위 -40% ~

> verify : Pools 다 배포 후, **tokamak-uniswap-v3-contract** 폴더에서 deployed.uniswap.tokamakgoerli.poolAddress.json 폴더 복사해서 v3-core 폴더로 옮기기

```json
npx hardhat run scripts/verifyPools.js --network titan
```

tx :

```json
======createAndInitialize poolAddressWETHTON=======
transactionHash: 0x9cd4918384d6695a093496ccfa99a16f55885ce4cda27f8e81786c349b9975ce
gasUsed:  BigNumber { value: "4570199" }

======createAndInitialize poolAddressWETHTOS=======
transactionHash: 0x27427a490fd9ac4c88ff308d3ce503cb011a20ead40e164f9be7a1018fc64e68
gasUsed:  BigNumber { value: "4570018" }

======createAndInitialize poolAddressWETHTON=======
transactionHash: 0x926246db559de593ea468a66d306feef2cc899b11e4628c3d876c1602dc82918
gasUsed:  BigNumber { value: "4569800" }

======createAndInitialize poolAddressWETHUSDC=======
transactionHash: 0x7ded96ea31bbe6de9b18820b55ab0e94d4a045263df3327ea84f0cc4d0420c71
gasUsed:  BigNumber { value: "4570014" }

======createAndInitialize poolAddressWETHUSDT=======
transactionHash: 0x9c95c4afe196a4d5c7030212a1a225bc6b996badbcee476afa229bb7fa1d72e8
gasUsed:  BigNumber { value: "4570099" }

totalGasUsed: BigNumber { value: "22850130" }
```

poolAddress : 

```json
poolAddressTOSTON: 0x124C9eE4fe1f7eC5aDBFC9d475ae2a52eBC50365
poolAddressWETHTOS: 0x72234a44116F971E890C8D1fd956e2e2E5aBf410
poolAddressWETHTON: 0x5Da46dD4229d2b6BF048D3A9d6B400Ef6d7CD35f
poolAddressWETHUSDC: 0xCD55aa8BEc623E17147059ab5cF91C77299c2Cee
poolAddressWETHUSDT: 0xf573dd4915F8F3ED73E5f3B9431A4869da38bBa3
```

# 6.2  Approve TON, TOS, USDC, USDT to NonfungibleManager 

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/2.approve_nftManager.js --network titan
```

tx:

```json
TON approved amount: BigNumber { value: "0" }
TON 1000000000000000000000000000000 * 10e18 amount Approved
transactionHash: 0x76e2153a750b2859499509612a8d3db07b39f7d89e93ff8618cf25f93f7fe811
gasUsed:  BigNumber { value: "46286" }

TOS approved amount: BigNumber { value: "0" }
TOS 1000000000000000000000000000000 * 10e18 amount Approved
transactionHash: 0x42b07d2f96fe62e6984c26797ffbcf7566dddbd63b2b6e18fb6022a9608ace22
gasUsed:  BigNumber { value: "46286" }

USDC approved amount: BigNumber { value: "0" }
USDC 1000000000000000000000000000000 * 10e18 amount Approved
transactionHash: 0x6c624fc92735f67b5fa6660cce216305cd31516a9dc49a816a5be3f3ce369b28
gasUsed:  BigNumber { value: "52965" }

USDT approved amount: BigNumber { value: "0" }
USDT 1000000000000000000000000000000 * 10e18 amount Approved
transactionHash: 0x7d43ddc8bcdfaad75d8f7e84a3b4646dd3593fe456f533d489ede718259b1239
gasUsed:  BigNumber { value: "46487" }

totalGasUsded: BigNumber { value: "192024" }
```

# 6.3  addLiquidity

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/3.add_liquidity.js --network titan
```

결과 : 

```json
====== poolAddressTOSTON mint ==========
tickLower: -7980
tickCurrentThen: -2870
tickUpper: 2520
transactionHash: 0xf7b33adb9402848b13d8c6581c7961f9281fa93626e4633002645df23c04f508
gasUsed:  BigNumber { value: "577897" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "1" },
  BigNumber { value: "127971422615189209945" },
  BigNumber { value: "34889349617975879900" },
  BigNumber { value: "25000000000000000000" },
  tokenId: BigNumber { value: "1" },
  liquidity: BigNumber { value: "127971422615189209945" },
  amount0: BigNumber { value: "34889349617975879900" }, 35 TON
  amount1: BigNumber { value: "25000000000000000000" }  25 TOS
]

====== poolAddressWETHTON mint ==========
tickLower: 66060
tickCurrentThen: 71165  
tickUpper: 76200
transactionHash: 0x9478b611034fffbc7f3a213f71dec87d3d698202b233460b9eb5ec8b07713090
gasUsed:  BigNumber { value: "484121" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "7" },
  BigNumber { value: "4416458029596775947" },
  BigNumber { value: "28000000000000000" },
  BigNumber { value: "34923442168171161646" },
  tokenId: BigNumber { value: "7" },
  liquidity: BigNumber { value: "4416458029596775947" },
  amount0: BigNumber { value: "28000000000000000" }, 0.028 ETH
  amount1: BigNumber { value: "34923442168171161646" } 35 TON
]
totalGasUsed: BigNumber { value: "484121" }

====== poolAddressWETHTOS mint ==========
tickLower: 63060
tickCurrentThen: 68161
tickUpper: 73380
transactionHash: 0x016bd06f64d59e25cda3c324ab4580230050f14f7969bced158ec806424aa157
gasUsed:  BigNumber { value: "570949" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "3" },
  BigNumber { value: "3677028375277556476" },
  BigNumber { value: "27961402707719993" },
  BigNumber { value: "24999999999999999995" },
  tokenId: BigNumber { value: "3" },
  liquidity: BigNumber { value: "3677028375277556476" },
  amount0: BigNumber { value: "27961402707719993" }, 0.028 ETH
  amount1: BigNumber { value: "24999999999999999995" } 25 TOS
]

====== poolAddressWETHUSDC mint ==========
tickLower: -206160
tickCurrentThen: -201072
tickUpper: -195780
transactionHash: 0x33a03ee5e8dbf706f8aeff3b11a5c2ab05041c22082547cb81dc71303a4db4e3
gasUsed:  BigNumber { value: "597977" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "4" },
  BigNumber { value: "5170636001269" },
  BigNumber { value: "27920569159772022" },
  BigNumber { value: "50000000" },
  tokenId: BigNumber { value: "4" },
  liquidity: BigNumber { value: "5170636001269" },
  amount0: BigNumber { value: "27920569159772022" }, 0.028 ETH
  amount1: BigNumber { value: "50000000" } 50 USDC
]

====== poolAddressWETHUSDT mint ==========
tickLower: 195960
tickCurrentThen: 201071
tickUpper: 205980
transactionHash: 0x3bd9691675da1965e17b5a6f15c5f4e3f9e2fe5b72b25d52c57c23475441df61
gasUsed:  BigNumber { value: "588662" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "5" },
  BigNumber { value: "5337199639712" },
  BigNumber { value: "50000000" },
  BigNumber { value: "27959811415020974" },
  tokenId: BigNumber { value: "5" },
  liquidity: BigNumber { value: "5337199639712" },
  amount0: BigNumber { value: "50000000" }, 50 USDT
  amount1: BigNumber { value: "27959811415020974" } 0.028 ETH
]

totalGasUsed: BigNumber { value: "2860138" }
```

## 7.1 Test Quote

> git:[https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/4.test_quote.js --network titan
```

```json
1 TON => 0.733410659767039344 TOS
1 TOS => 1.334218768623314049 TON
1 TON => 0.000804204211611148 ETH
0.000804204211611148 ETH => 0.981403085574748608 TON
1 TOS => 0.001083322483507678 ETH
0.001083322483507678 ETH => 0.976501613746587797 TOS
1 USDC => 0.000535502894904843 ETH
0.000535502894904843 ETH => 0.985197 USDC
1 USDT => 0.000535577420106933 ETH
0.000535577420106933 ETH => 0.98547 USDT
```

## 7.2 Test, approve TON to SwapRouter 

> git: [https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/5.approve_swapRouter.js --network titan
```

결과 : 

```json
TON approved amount: BigNumber { value: "0" }
TON 1000000000000000000000000000000 * 10e18 amount Approved
transactionHash: **0xf15c72b39fa5df6eab6156ef2b161c264fee18c6bf14c6bc67fb4234fc2c9b87**
gasUsed:  BigNumber { value: "46286" }

totalGasUsded: BigNumber { value: "46286" }
```

## 7.3 Swap Test 

> git: git:[https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)

> 실행 : 

```json
npx hardhat run scripts/v3/mainnet/6.swap_test.js --network titan
```

결과 : 

```json
===TON => TOS (ERC20->ERC20)
transactionHash: 0xe31a4008fafcd71aea58c37e3de4843fab323856b901ba115004232999434de5
gasUsed:  BigNumber { value: "130049" }

===ETH => TON (ETH->ERC20)
transactionHash: 0x50f9beb1e0af5bbed9950fbcb42535ef98450f02b5aae60fd9ec1c4c478ea161
gasUsed:  BigNumber { value: "128563" }

===TON => ETH (ERC20->ETH)
transactionHash: 0x2363b867e4ac3d3e3363e4ec80a2c0acdf180ef776ac1a7809b6c3fc9b1494d8
gasUsed:  BigNumber { value: "128823" }

```

 ===TON => TOS (ERC20->ERC20)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fd9b186f-1594-4c4f-b7e0-b114fc5ac6d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FRKNDJM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzkGLhXIooa05UFZ53VAkQakI9UeDWenWarhGsbHHHIwIgSwsKDsYxzt0iY2zszd0akmsZ2FNGQIk8Iet3otYaOhAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKeLhg6jvTkRbrtIoCrcA20TN40P2%2F3NPoxk6%2FgXkW23QNrS7QRLzaIcisNkG%2FGVGSdaSfWU7n3Igqmahq%2BAUrNSOQgqmcm9pgfhBZ8ZBhQFOFPGpaWDPRUSIkITfGNHi%2FKAzhFSul5o7Q5q3D0vjA2j2kfVM%2BGOf%2BxZ4D5lkbSIPJm4jvfgE6TkkcbRrYysG6hsIcFN6SsxmJmiAvSl4kvMEqFfskCx%2B5p9OUc58HuW%2BZBy51U4utIjxYcYU80OhBJsg6dFs1hOoIg8EXGl7dMFUu5rGDNm8HA5TLrxG5N7hsJ%2BiWfa62fnz9FkkmFV0wbu%2BXHSsQFrmMQ3TkXlTEpW3sSYoIyl40R7U2OUdQKXiBftOpfbqUt%2BpPoFhIcrXK0YLyJtJLxqhjvV%2BoKRdkQMRehGu1tOOOfkF%2BMZWTS1uOXXHcyugtbFWw7OMl759yE19OjsipICA5CS9YqQ507ZVl5f5IrnoZHMVoXhRAMSYIAdHZgjQ8FoKcWBwEEK2eAqBXOFq4Cak426HY3%2Bf0GtL62aHfHSioZvBXiFqii39%2B4jlMfir%2B30xyyoT9VugVKInU7pA5lDb5cJ%2BXwCDXacCwnzIm89d1JKTlGsW%2Ba52bjPdeBlMQUs3HsBfe2GOnx5xBDBHk65aQ1fMK2Y28wGOqUBn90foSFTKHmgF6ZueoNDw5debPrbyMc0ZcOuqH5EROQWNFVOESmjow0NckZE3JubOh%2Bx2slAvIENes0Zw8h3ocmyhLRmJOx5vk73aiYLe1rnCiAH2kWG7Jj8EgMVN7tLWjTBXINNJP2Ik%2FEwcYfzqrgtFLvo6ifnH6biimDWcN0Dh281GCn2ezm18Yi4UBqgL0i%2FCz0IbTSyVDOeGTeE68j4L4RN&X-Amz-Signature=839cb8ac88f203c16deb735ac76a498b4e9cb929cf97f20f0d99c7bfe66f1bf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 ===ETH => TON (ETH->ERC20)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7fcdfe07-f44a-4828-b224-8c6bcc11890b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FRKNDJM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzkGLhXIooa05UFZ53VAkQakI9UeDWenWarhGsbHHHIwIgSwsKDsYxzt0iY2zszd0akmsZ2FNGQIk8Iet3otYaOhAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKeLhg6jvTkRbrtIoCrcA20TN40P2%2F3NPoxk6%2FgXkW23QNrS7QRLzaIcisNkG%2FGVGSdaSfWU7n3Igqmahq%2BAUrNSOQgqmcm9pgfhBZ8ZBhQFOFPGpaWDPRUSIkITfGNHi%2FKAzhFSul5o7Q5q3D0vjA2j2kfVM%2BGOf%2BxZ4D5lkbSIPJm4jvfgE6TkkcbRrYysG6hsIcFN6SsxmJmiAvSl4kvMEqFfskCx%2B5p9OUc58HuW%2BZBy51U4utIjxYcYU80OhBJsg6dFs1hOoIg8EXGl7dMFUu5rGDNm8HA5TLrxG5N7hsJ%2BiWfa62fnz9FkkmFV0wbu%2BXHSsQFrmMQ3TkXlTEpW3sSYoIyl40R7U2OUdQKXiBftOpfbqUt%2BpPoFhIcrXK0YLyJtJLxqhjvV%2BoKRdkQMRehGu1tOOOfkF%2BMZWTS1uOXXHcyugtbFWw7OMl759yE19OjsipICA5CS9YqQ507ZVl5f5IrnoZHMVoXhRAMSYIAdHZgjQ8FoKcWBwEEK2eAqBXOFq4Cak426HY3%2Bf0GtL62aHfHSioZvBXiFqii39%2B4jlMfir%2B30xyyoT9VugVKInU7pA5lDb5cJ%2BXwCDXacCwnzIm89d1JKTlGsW%2Ba52bjPdeBlMQUs3HsBfe2GOnx5xBDBHk65aQ1fMK2Y28wGOqUBn90foSFTKHmgF6ZueoNDw5debPrbyMc0ZcOuqH5EROQWNFVOESmjow0NckZE3JubOh%2Bx2slAvIENes0Zw8h3ocmyhLRmJOx5vk73aiYLe1rnCiAH2kWG7Jj8EgMVN7tLWjTBXINNJP2Ik%2FEwcYfzqrgtFLvo6ifnH6biimDWcN0Dh281GCn2ezm18Yi4UBqgL0i%2FCz0IbTSyVDOeGTeE68j4L4RN&X-Amz-Signature=fdb071b6d90e0351b65322d7551cbf3c72b7b70e58ec8692d981380852c10ccc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

===TON => ETH (ERC20->ETH)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c1bbce80-15be-455b-85ab-2a087317afa3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FRKNDJM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzkGLhXIooa05UFZ53VAkQakI9UeDWenWarhGsbHHHIwIgSwsKDsYxzt0iY2zszd0akmsZ2FNGQIk8Iet3otYaOhAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKeLhg6jvTkRbrtIoCrcA20TN40P2%2F3NPoxk6%2FgXkW23QNrS7QRLzaIcisNkG%2FGVGSdaSfWU7n3Igqmahq%2BAUrNSOQgqmcm9pgfhBZ8ZBhQFOFPGpaWDPRUSIkITfGNHi%2FKAzhFSul5o7Q5q3D0vjA2j2kfVM%2BGOf%2BxZ4D5lkbSIPJm4jvfgE6TkkcbRrYysG6hsIcFN6SsxmJmiAvSl4kvMEqFfskCx%2B5p9OUc58HuW%2BZBy51U4utIjxYcYU80OhBJsg6dFs1hOoIg8EXGl7dMFUu5rGDNm8HA5TLrxG5N7hsJ%2BiWfa62fnz9FkkmFV0wbu%2BXHSsQFrmMQ3TkXlTEpW3sSYoIyl40R7U2OUdQKXiBftOpfbqUt%2BpPoFhIcrXK0YLyJtJLxqhjvV%2BoKRdkQMRehGu1tOOOfkF%2BMZWTS1uOXXHcyugtbFWw7OMl759yE19OjsipICA5CS9YqQ507ZVl5f5IrnoZHMVoXhRAMSYIAdHZgjQ8FoKcWBwEEK2eAqBXOFq4Cak426HY3%2Bf0GtL62aHfHSioZvBXiFqii39%2B4jlMfir%2B30xyyoT9VugVKInU7pA5lDb5cJ%2BXwCDXacCwnzIm89d1JKTlGsW%2Ba52bjPdeBlMQUs3HsBfe2GOnx5xBDBHk65aQ1fMK2Y28wGOqUBn90foSFTKHmgF6ZueoNDw5debPrbyMc0ZcOuqH5EROQWNFVOESmjow0NckZE3JubOh%2Bx2slAvIENes0Zw8h3ocmyhLRmJOx5vk73aiYLe1rnCiAH2kWG7Jj8EgMVN7tLWjTBXINNJP2Ik%2FEwcYfzqrgtFLvo6ifnH6biimDWcN0Dh281GCn2ezm18Yi4UBqgL0i%2FCz0IbTSyVDOeGTeE68j4L4RN&X-Amz-Signature=8cbdaedac64fe50e72eaa8073017a1d11ec2ef2ed6477e95ad95b88ba82c3687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 8. Deploy BridgeSwap

@Unknown 

> git: [https://github.com/tokamak-network/bridgeSwapTest](https://github.com/tokamak-network/bridgeSwapTest)

> 실행 (Deploy)

```json
npx hardhat run scripts/BridgeDeploy_mainnet.ts --network mainnet
```

필요한 가스 : [https://docs.google.com/spreadsheets/d/12rz6J0gTC2UD1rSIdyZ7tP3De1Xv1jl_nrL_IpkWCEM/edit#gid=0](https://docs.google.com/spreadsheets/d/12rz6J0gTC2UD1rSIdyZ7tP3De1Xv1jl_nrL_IpkWCEM/edit#gid=0) (L1 ETH 필요)

- Set Address
  - L1 TON : [0x2be5e8c109e2197D077D13A82dAead6a9b3433C5](https://etherscan.io/address/0x2be5e8c109e2197D077D13A82dAead6a9b3433C5)
  - L1 WTON : [0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2](https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2)
  - L2 TON : [0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2](https://explorer.titan.tokamak.network/token/0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2/token-transfers)
  - L1 Bridge : [0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#code)
  - L1 WETH : [0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2](https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#code)

**Deployed Tx : **[https://etherscan.io/tx/0x071c6f2f239f779dc7cadcbea88c819c9a00b385a5e6e69c821bc36808af41ee](https://etherscan.io/tx/0x071c6f2f239f779dc7cadcbea88c819c9a00b385a5e6e69c821bc36808af41ee)

**Deployed BridgeSwap Address : 0xA3139764F343f44A7809dA51DC3a34C3d94450d0**

> verify  

```json
npx hardhat verify --constructor-args arguments_mainnet.js contract_Address --network mainnet
```

- check storage
  - L1 TON : [0x2be5e8c109e2197D077D13A82dAead6a9b3433C5](https://etherscan.io/address/0x2be5e8c109e2197D077D13A82dAead6a9b3433C5)
  - L1 WTON : [0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2](https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2)
  - L2 TON : [0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2](https://explorer.titan.tokamak.network/token/0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2/token-transfers)
  - L1 Bridge : [0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#code)
  - L1 WETH : [0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2](https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#code)

```json
npx hardhat run scripts/checkStorage_mainnet.ts --network mainnet
```

### Test 

- test tx : 
  - L1 depositWTON tx : [https://etherscan.io/tx/0xbce6672d6be510dd362bbacbcb1a697f875397f9d313942721b0a185ebeec9a2](https://etherscan.io/tx/0xbce6672d6be510dd362bbacbcb1a697f875397f9d313942721b0a185ebeec9a2)
  - L2 depositWTON tx : [https://explorer.titan.tokamak.network/tx/0x48f158872d3d00710d473a2d3d5655a6ee1713b5b3bbe821f85ab60c9b5d06fb](https://explorer.titan.tokamak.network/tx/0x48f158872d3d00710d473a2d3d5655a6ee1713b5b3bbe821f85ab60c9b5d06fb)
  - L1 depositWTONTo tx : [https://etherscan.io/tx/0x0521e542e6621765855ccafca8f8c1a784583b18be72798b97ba671fcb53ab27](https://etherscan.io/tx/0x0521e542e6621765855ccafca8f8c1a784583b18be72798b97ba671fcb53ab27)
  - L2 depositWTONTo tx : [https://explorer.titan.tokamak.network/tx/0x18044d44c57880dfb6973d91d633f56c004d54d5b544f5d7a3df8d24f99518da](https://explorer.titan.tokamak.network/tx/0x18044d44c57880dfb6973d91d633f56c004d54d5b544f5d7a3df8d24f99518da)
  - L1 depositWETH tx : [https://etherscan.io/tx/0xd6efc9d9fa33940719334ce01167e62683f5c14caf7928de9ec9f5057b4d424c](https://etherscan.io/tx/0xd6efc9d9fa33940719334ce01167e62683f5c14caf7928de9ec9f5057b4d424c)
  - L2 depositWETH tx : [https://explorer.titan.tokamak.network/tx/0x86e33296e3503305347216cebe12e30558e865f1628fa780d0773927d522f2d5](https://explorer.titan.tokamak.network/tx/0x86e33296e3503305347216cebe12e30558e865f1628fa780d0773927d522f2d5)
  - L1 depositWETHTo tx : [https://etherscan.io/tx/0x9fc7c6ba05c87492055505cf69a098a665b636a97dc571da1853af89804f2d7f](https://etherscan.io/tx/0x9fc7c6ba05c87492055505cf69a098a665b636a97dc571da1853af89804f2d7f)
  - L2 depositWETHTo tx : [https://explorer.titan.tokamak.network/tx/0x7b8e04b309bdc13638f3b3d53fd137c9a76f91d403d8c07784be050ce2c92122](https://explorer.titan.tokamak.network/tx/0x7b8e04b309bdc13638f3b3d53fd137c9a76f91d403d8c07784be050ce2c92122)
- 반납 
  - TON tx : [https://etherscan.io/tx/0x9801c83dd8efe07242889c36d9e70544f7d56f3a81cb99f80ca687cb9190dd93](https://etherscan.io/tx/0x9801c83dd8efe07242889c36d9e70544f7d56f3a81cb99f80ca687cb9190dd93)
  - ETH tx : [https://etherscan.io/tx/0x476efad836f47dac7e1ff1a8ad3e318707205fe694873a8609f17425d69d3fe9](https://etherscan.io/tx/0x476efad836f47dac7e1ff1a8ad3e318707205fe694873a8609f17425d69d3fe9)

# Deployed Address

0f691cab-f28f-4643-b26e-fb31a88a370d 