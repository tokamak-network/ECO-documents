[[시나리오]]

[[가스]]

**deployer address **: **0xE49c9ea00337182374E112C452247A2D1db61798**

필요한 가스 : OVM_GasGracle: **0x420000000000000000000000000000000000000F**

1. Deploy UniswapContracts + (permit2 + universalRouter) :  30413266 + 7884696** = 38297962 **
1. Approve NonfungiblePositionManager TON,TOS,WETH,USDC,USDT : **231328**
1. createAndInitialize TOS_TON, WETH_TOS, WETH_TON, WETH_USDC, WETH_USDT  : **22851506**
1. mint(add_liquidity) TOS_TON, WETH_TOS, WETH_TON, WETH_USDC, WETH_USDT : **2932014**

합계 : 30413266 + 231328 + 22851506 + 2932014 = **64312810**

---

1. Approve SwapRouter TON,TOS,WETH,USDC,USDT + swapTest : **1113024**

합계 : 1113024 + 64312810**= 65425834**

---

1. 0.01Fee Activation : **47916**

합계 : 64312810+ 47916 **= 64360726**

# deploy uniswap 

@Unknown 

### Uniswap V3 

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
  "SwapRouter02": "0x9Cabe266e34C7B60858BD55B0a3C00b83e511619",
  "UniswapV3PoolSwapTest": "0xCd07B2845B6997FA181742dA8CA77C16d599E1E3",
  "Multicall": "0x2C86Fa58c3FAb8AD5860aF8222Fb375a5634F1AD"
}
```

### Permit2, UniversalRouter

```json
UnsupportedProtocol : 0xf6290b11D1B632a8D6a90094643E7cE8C8B2B777
permit2: 0x6d82498723c607C8F4A5a4dd3ba5C508e71588EB
UniversalRouter 0x00c089f0639821Bf6670A51707361561950458BD
```

### 0.01Fee Activation : enableFeeAmount(100,1)

```json
https://goerli.explorer.tokamak.network/tx/0xbeb10c35fb7c819ba2dd81faa01fad3388728dad5d0c80cbc1e8b3ad9d3d0509
```

poolAddress

```json
poolAddressTOSTON: 0x2C1C509942D4f55e2BfD2B670E52b7A16ec5e5C4 :fee 3000
poolAddressWETHTOS: 0xD305b3A89B4bc414Ea13ce891B0767340fEe720D : fee 3000
poolAddressWETHTON: 0x2D676468aa747f23E8dC5A9102aFa418983885B7 : fee 3000
poolAddressWETHUSDC: 0x000be04EcFD9fB06Ecc65a3bFF2e137c08397AC6 fee: 500
poolAddressWETHUSDT: 0xE2625e4c3dd7B86e5E14c43B16F973FaC4f926F9 fee: 500

poolAddressWETHUSDT: 0x83f0F8BbBC38246824F9aCe988c48f9bA06eCd4E fee: 100
```

TokenAddress

```json
TON = '0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa';
TOS = '0x6AF3cb766D6cd37449bfD321D961A61B0515c1BC';
WETH = '0x4200000000000000000000000000000000000006';
USDC = '0x9c53338c48181035D96884946C34ea81818F743C';
USDT = '0xd1e405F1154BE88aC84f748C1BcE22442B12309F';
```

poolAddress Create and Initialize TX:

```json
======createAndInitialize poolAddressTOSTON=======
transactionHash: 0xdd6f4faf160de6a3c5741c7393613c7a56c6d38b6031e523d461e20c4d7dce9b
gasUsed:  BigNumber { value: "4570356" }

======createAndInitialize poolAddressWETHTOS=======
transactionHash: 0x012d0cceb64581aa33202e940f7b1ed72bcd2afffd9439bf720f964a91b9ca76
gasUsed:  BigNumber { value: "4570023" }

======createAndInitialize poolAddressWETHTON=======
transactionHash: 0x400906a547aaeba19a4b5b583b26e0c3dee2dbe0c4bb77cbdb50c9fc1d6dd9c7
gasUsed:  BigNumber { value: "4570123" }

======createAndInitialize poolAddressWETHUSDC=======
transactionHash: 0x600979d5f8c0f96a87d29917ba9f508ccc554da7ef6797152caf60c7ee984ba3
gasUsed:  BigNumber { value: "4570127" }

======createAndInitialize poolAddressWETHUSDT======= 0.05%
transactionHash: 0x85dd50ca3f00375bb2b320704b35876f3ec47d30f794d7a162c0e4e5d6280c4f
gasUsed:  BigNumber { value: "4570025" }

======createAndInitialize poolAddressWETHUSDT======= 0.01%
transactionHash: 0x3e26e1f4271c13903c764cd0e9a1581bd9366ecbb6d85325bbc5b9244d4b9691
gasUsed:  BigNumber { value: "4570013" }
```

approve to NonfungibleManager TON and WETH

```json
TON Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0x7782b49a8688a9394ad354ba483899e42bfd681acc0aa898af16cd490787bff9
gasUsed:  BigNumber { value: "46286" }

WETH Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xcbab1580dc681402b0109ae9a5beec0b9843ef48e56100e59cb1074dedbd2c28
gasUsed:  BigNumber { value: "46079" }

TOS Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xab429f9bc21b6985308433630593fe380d1428a754e599d5360cf87eadf6dbee
gasUsed:  BigNumber { value: "46286" }

USDCContract Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0x6e2d2e71282682785461a6cc08a79f539a5ca3efdfd8cab498ce3ce9b59dcc44
gasUsed:  BigNumber { value: "53752" }

USDTContract Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xdfb351dd0162ff58c4a0ba513cfdcef035c26482f821b101799ab7aa691e42b6
gasUsed:  BigNumber { value: "47254" }
```

approve to SwapRouter TON,TOS, WETH, USDT, USDC

```json
TON Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xe117c4505d0e1fb0331374af469b1a0e71958b12b784b69841e5338281ba1ef9
gasUsed:  BigNumber { value: "46286" }

TOS Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0x4bc1f796e3ce110af341c353821ef9d4ecfcfc2273c4712912b9207b5abe75c3
gasUsed:  BigNumber { value: "46286" }

WETH Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0x1861c541e62002f13441f983a1c9c15ddc25f13925312f7aa0866ff753a221c5
gasUsed:  BigNumber { value: "46079" }

USDCContract Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xbba3c09f7302f40a4d94bede38f5c9e34d2858d9762545bca8ebcfa8e591d48c
gasUsed:  BigNumber { value: "53752" }

USDTContract Contract 1000000000000000000000000000000 ether amount Approved
transactionHash: 0xb5341dff974488f0a2318c19240306849ee47cc6a0b3d1ea59c0787750829836
gasUsed:  BigNumber { value: "47254" }
```

add_Liquidity to TON/WETH

```json
====== poolAddressWETHTON mint ==========
transactionHash: 0x9b48b0e67e0aaf6f4eca02da0875b024966639eb10c4032032f29f9446f36be2
gasUsed:  BigNumber { value: "587317" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "1" },
  BigNumber { value: "134984785496092" },
  BigNumber { value: "18353267" },
  BigNumber { value: "34999999999999942959" },
  tokenId: BigNumber { value: "1" },
  liquidity: BigNumber { value: "134984785496092" },
  amount0: BigNumber { value: "18353267" },
  amount1: BigNumber { value: "34999999999999942959" }
]

====== poolAddressTOSTON mint ==========
transactionHash: 0x6876d8596a66be4413d441e1c1638438412b9d90eb0d43c1238f4a841d8765a8
gasUsed:  BigNumber { value: "489561" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "10" },
  BigNumber { value: "9193645778668617594359" },
  BigNumber { value: "1178269602095150513267" },
  BigNumber { value: "2500000000000000000000" },
  tokenId: BigNumber { value: "10" },
  liquidity: BigNumber { value: "9193645778668617594359" },
  amount0: BigNumber { value: "1178269602095150513267" },
  amount1: BigNumber { value: "2500000000000000000000" }
]
//현재 tick : 3568
===================================================

====== poolAddressWETHTOS mint ==========
transactionHash: 0x4c4422247a664f0679d4eda7d033da38dbc875ad70a61b05d90440e7ac378648
gasUsed:  BigNumber { value: "571253" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "3" },
  BigNumber { value: "5888587871897841" },
  BigNumber { value: "27999999999999996" },
  BigNumber { value: "43143640919297" },
  tokenId: BigNumber { value: "3" },
  liquidity: BigNumber { value: "5888587871897841" },
  amount0: BigNumber { value: "27999999999999996" },
  amount1: BigNumber { value: "43143640919297" }
]

poolAddressWETHTON liquidity: BigNumber { value: "134984785496092" } 279025
USDC Deciamls 6
poolAddressWETHUSDC liquidity: BigNumber { value: "0" }
====== poolAddressWETHUSDC mint ==========
transactionHash: 0xf6f41a0f3b3a1e2e3611dc869340cab23bfce0e1b24c71f0902974e34f02d793
gasUsed:  BigNumber { value: "604571" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "4" },
  BigNumber { value: "9453" },
  BigNumber { value: "1" },
  BigNumber { value: "49995149" },
  tokenId: BigNumber { value: "4" },
  liquidity: BigNumber { value: "9453" },
  amount0: BigNumber { value: "1" },  **<==== . 확인해보기**
  amount1: BigNumber { value: "49995149" } //50 USDC 맞음
]
확인중: tick range : 196080 ~ 204600, 현재 틱 : 201207

2.initialize_pool first
poolAddressWETHUSDT liquidity: BigNumber { value: "0" }
====== poolAddressWETHUSDT mint ==========
transactionHash: 0x4a075ebf1f9ddaace43742502f22d0bc03c831bb0317ae1d7a78f219235cdda4
gasUsed:  BigNumber { value: "591192" }
eventName: IncreaseLiquidity
[
  BigNumber { value: "5" },
  BigNumber { value: "5168003190633" },
  BigNumber { value: "18839034748693554" },
  BigNumber { value: "50000000" },
  tokenId: BigNumber { value: "5" },
  liquidity: BigNumber { value: "5168003190633" },
  amount0: BigNumber { value: "18839034748693554" },
  amount1: BigNumber { value: "50000000" }
]
```

SwapRouter

```json
===ETH => TON (ETH->ERC20)
transactionHash: 0x5056bddd3c8b7a091e4fd1b8b50395a6fca6009e471eb40e1696a6d61e72fbb9
gasUsed:  BigNumber { value: "128188" }
```

+decrease, collect, burn, 

verify도 스크립트로 준비하겠습니다.

### deploy TON 

**L2TokenFactory**:  [https://goerli.explorer.tokamak.network/address/0x4200000000000000000000000000000000000012/write-contract#address-tabs](https://goerli.explorer.tokamak.network/address/0x4200000000000000000000000000000000000012/write-contract#address-tabs)

- TON  **( L2TokenFactory 사용하여 배포) **
  - L1Token address (goerli): 0x68c1F9620aeC7F2913430aD6daC1bb16D8444F00
  - Name: Tokamak Network 
  - Symbol: TON
  - Decimals : 18
  - TON L2Token address : [0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa](https://goerli.explorer.tokamak.network/address/0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa/write-contract#address-tabs)
- tx : [https://goerli.explorer.tokamak.network/tx/0x3080e77526d4689af06d634af80ae59ce86a214d7d3065fe265a25d160e6a426](https://goerli.explorer.tokamak.network/tx/0x3080e77526d4689af06d634af80ae59ce86a214d7d3065fe265a25d160e6a426)
- npx hardhat verify 0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa 0x4200000000000000000000000000000000000010 0x68c1f9620aec7f2913430ad6dac1bb16d8444f00 'Tokamak Network' 'TON' --network titangoerli

### deploy TOS 

**L2TokenFactory**:  [https://goerli.explorer.tokamak.network/address/0x4200000000000000000000000000000000000012/write-contract#address-tabs](https://goerli.explorer.tokamak.network/address/0x4200000000000000000000000000000000000012/write-contract#address-tabs)

- TOS **( L2TokenFactory 사용하여 배포) **
  - L1Token address (goerli):  0x67F3bE272b1913602B191B3A68F7C238A2D81Bb9
  - Name: TONStarter
  - Symbol: TOS 
  - Decimals :18 
  - TOS L2Token address : [0x6af3cb766d6cd37449bfd321d961a61b0515c1bc](https://goerli.explorer.tokamak.network/address/0x6AF3cb766D6cd37449bfD321D961A61B0515c1BC)
- tx :  [https://goerli.explorer.tokamak.network/tx/0x50937a211e7a74a3a74c62335f71fbf3b4ef81ee7202f34f3be8070307f170ba](https://goerli.explorer.tokamak.network/tx/0x50937a211e7a74a3a74c62335f71fbf3b4ef81ee7202f34f3be8070307f170ba)
- npx hardhat verify 0x6af3cb766d6cd37449bfd321d961a61b0515c1bc 0x4200000000000000000000000000000000000010 0x67f3be272b1913602b191b3a68f7c238a2d81bb9 'TONStarter' 'TOS' --network titangoerli

### Transfer ownership 재단 주소로 

- newOwner: [`0xb68aa9e398c054da7ebaaa446292f611ca0cd52b`](https://goerli.explorer.tokamak.network/address/0xb68aa9e398c054da7ebaaa446292f611ca0cd52b)
- tx : [https://goerli.explorer.tokamak.network/tx/0xbcd2dcf1f3f4866d64ca3c4f3acd40db19cd2de4bac33666d190038b15376399](https://goerli.explorer.tokamak.network/tx/0xbcd2dcf1f3f4866d64ca3c4f3acd40db19cd2de4bac33666d190038b15376399)

# deploy USDC, USDT  

배포하는 계정의 개인키가 .env에 설정되어 있는지 확인한다. 실행전 .env 의 **0xA42C3599f9a36e7CDdFeBA712EE31A6aaa9b7777 의 **PRIVATE_KEY로 수정한다. 

내일 작업시, 코드에서 owner 를 꼭 수정해야 한다.  

- USDC **( 컨트랙 직접 배포 deployer:  0xA42C3599f9a36e7CDdFeBA712EE31A6aaa9b7777)  **
  - L1Token address (goerli) :  0x07865c6e87b9f70255377e024ace6630c1eaa37f
  - Name:  USD Coin
  - Symbol: USDC 
  - Decimals : 6
  - USDC L2Token address : 0x9c53338c48181035D96884946C34ea81818F743C
  - tx: [https://goerli.explorer.tokamak.network/tx/0xac9fe5891bc4805835e876d7cdaea6e31eca9c3e144f65b57b689fc4a1efbe62](https://goerli.explorer.tokamak.network/tx/0xac9fe5891bc4805835e876d7cdaea6e31eca9c3e144f65b57b689fc4a1efbe62)
- USDT **( 컨트랙 직접 배포 deployer: 0xA42C3599f9a36e7CDdFeBA712EE31A6aaa9b7777) **
  - L1Token address (goerli):  0xfad6367e97217cc51b4cd838cc086831f81d38c2
  - Name:  Tether USD
  - Symbol:   USDT
  - Decimals : 6
  - USDT L2Token address : [0xd1e405F1154BE88aC84f748C1BcE22442B12309F](https://goerli.explorer.tokamak.network/address/0xd1e405F1154BE88aC84f748C1BcE22442B12309F/read-contract#address-tabs)
    - tx: [https://goerli.explorer.tokamak.network/tx/0x42d3695a176fc669f7031a41c237093abcba75a60762aa7c6ac4aa16c9382f59](https://goerli.explorer.tokamak.network/tx/0x42d3695a176fc669f7031a41c237093abcba75a60762aa7c6ac4aa16c9382f59) 
    - 
  - at git: [https://github.com/tokamak-network/tokamak-testnet-token/tree/main](https://github.com/tokamak-network/tokamak-testnet-token/tree/main)
실행전 .env 의 **0xA42C3599f9a36e7CDdFeBA712EE31A6aaa9b7777 의 **PRIVATE_KEY로 수정한다. 

```json
npx hardhat run scripts/deploy-usdc-titan-goerli.js —network titan-goerli

npx hardhat run scripts/deploy-usdt-titan-goerli.js —network titan-goerli
```

 

# Transfer token from L1(goerli) to L2(titan-goerli)

At Git:  [https://github.com/tokamak-network/layer2-interface-test](https://github.com/tokamak-network/layer2-interface-test)

- **TO** (justin):  **0xB68AA9E398c054da7EBAaA446292f611CA0CD52B**

total required fund for the pools = 70 TON, 50 TOS, 0.112 ETH, 50 USDC, 50 USDT
Pools (for testing swap on L2) :
Ecosystem
TON/TOS 0.3% (35 TON, 25 TOS)
ETH/TON 0.3% (0.028 ETH, 35 TON)
ETH/TOS 0.3% (0.028 ETH, 25 TOS)
Ethereum price 0.3%
ETH/USDC 0.3% (0.028 ETH, 50 USDC)
ETH/USDT 0.3% (0.028 ETH, 50 USDT)

- TON
  - [0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa](https://goerli.explorer.tokamak.network/address/0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa/write-contract#address-tabs)
  - 70 TON 
  - send : [https://goerli.explorer.tokamak.network/tx/0x6d0354bc24a2720d7e7dc13d2c3824f60dbaa969d4f045b9b2c386b6b8b68b02](https://goerli.explorer.tokamak.network/tx/0x6d0354bc24a2720d7e7dc13d2c3824f60dbaa969d4f045b9b2c386b6b8b68b02)
- TOS
  - [0x6af3cb766d6cd37449bfd321d961a61b0515c1bc](https://goerli.explorer.tokamak.network/address/0x6AF3cb766D6cd37449bfD321D961A61B0515c1BC)
  - 50 TOS
  - send : [https://goerli.explorer.tokamak.network/tx/0x22e0b841065ef49b9ffb131aebb830da8c5ea85835d80bdd6454f17fbd7a0578](https://goerli.explorer.tokamak.network/tx/0x22e0b841065ef49b9ffb131aebb830da8c5ea85835d80bdd6454f17fbd7a0578)
- USDC 
  - [0x9c53338c48181035D96884946C34ea81818F743C](https://goerli.explorer.tokamak.network/address/0x9c53338c48181035D96884946C34ea81818F743C/read-contract#address-tabs)
  - 50 USDC 
  - send : [https://goerli.explorer.tokamak.network/tx/0x487fbe7eb548231f36d117dd1b095f5cb669e5e56bed0c673acea08b3bd3b250](https://goerli.explorer.tokamak.network/tx/0x487fbe7eb548231f36d117dd1b095f5cb669e5e56bed0c673acea08b3bd3b250)
- USDT 
  - [0xd1e405F1154BE88aC84f748C1BcE22442B12309F](https://goerli.explorer.tokamak.network/address/0xd1e405F1154BE88aC84f748C1BcE22442B12309F/read-contract#address-tabs)
  - 50 USDT 
  - send : [https://goerli.explorer.tokamak.network/tx/0x29523b8abc3d2e1ec2ddd54599b9ee7f432dfcde591b3bf79016b09386004e5d](https://goerli.explorer.tokamak.network/tx/0x29523b8abc3d2e1ec2ddd54599b9ee7f432dfcde591b3bf79016b09386004e5d)
- ETH
  - 0.2 ETH 
  - [https://goerli.explorer.tokamak.network/tx/0x46123b9429800e6f73d1afb5a0564a8a7881736d57cbb1691ffdabe360c69bf4](https://goerli.explorer.tokamak.network/tx/0x46123b9429800e6f73d1afb5a0564a8a7881736d57cbb1691ffdabe360c69bf4)

# Create Pool & increase liquidity 

 현재 메인넷 기준

- **ETH/TON **
  - fee  : 3000
  - 현재 틱 : 279034, sqrtPriceX96: 90728086610218973648330084594723118 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위 : + - 40%
- ETH/TOS
  - fee : 3000
  - 현재 틱: -68470, sqrtPriceX96: 2583216200895513280038780992 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위 :
- TON-TOS
  - fee : 3000
  - 현재 틱 : 210781 , sqrtPriceX96 : 2990295844712018212030196559742641 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위 : 
- ETH/USDC
  - fee : 500 (TVL 제일 높은)
  - 현재 틱 : 201207, sqrtPriceX96: 1852826990250527434372994649008279 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위
- ETH/USDT
  - fee : 500 (TVL 제일 높은)
  - 현재 틱: -201210, sqrtPriceX96: 3387649038864965938133741 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위
- ETH/USDT
  - fee : 100 (추가)
  - 현재 틱: -201210, sqrtPriceX96: 3387649038864965938133741 (23-06-21 8:47 PM 기준)
  - 유동성 제공 범위
- swap test (준비완료)

# Deploy BridgeSwap

@Unknown 

deployer address: [0xEB141C111a7fAf5fb494a5992dA5B1F36CA1C935](https://goerli.etherscan.io/address/0xEB141C111a7fAf5fb494a5992dA5B1F36CA1C935)

필요한 가스 : [https://docs.google.com/spreadsheets/d/12rz6J0gTC2UD1rSIdyZ7tP3De1Xv1jl_nrL_IpkWCEM/edit#gid=0](https://docs.google.com/spreadsheets/d/12rz6J0gTC2UD1rSIdyZ7tP3De1Xv1jl_nrL_IpkWCEM/edit#gid=0) 

- deployed address : [https://goerli.etherscan.io/address/0xeb141c111a7faf5fb494a5992da5b1f36ca1c935#code](https://goerli.etherscan.io/address/0xeb141c111a7faf5fb494a5992da5b1f36ca1c935#code)

- Set Address (on goerli)
  - L1 TON : 0x68c1F9620aeC7F2913430aD6daC1bb16D8444F00
  - L2 TON : 0xFa956eB0c4b3E692aD5a6B2f08170aDE55999ACa
  - L1 WTON : 0xe86fCf5213C785AcF9a8BFfEeDEfA9a2199f7Da6
  - L1 Bridge : 0x7377F3D0F64d7a54Cf367193eb74a052ff8578FD
  - L1 WETH : 0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6
- test  : 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea
  - depositTON
    - L1 tx : [https://goerli.etherscan.io/tx/0xe6c58626285e04bb7d10c6c7d7091becccee7923d9b69b45e8cca18d0094aa51](https://goerli.etherscan.io/tx/0xe6c58626285e04bb7d10c6c7d7091becccee7923d9b69b45e8cca18d0094aa51)
    - before L2 TON : 0
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0x59ac13fcf7389ae906ac5962e5b2289b788763980d298f4d89fbc8bc0c61c704](https://goerli.explorer.tokamak.network/tx/0x59ac13fcf7389ae906ac5962e5b2289b788763980d298f4d89fbc8bc0c61c704)
    - after L2 TON : 1
  - depositTONTo
    - to : 0x43700f09B582eE2BFcCe4b5Db40ee41B4649D977
    - L1 tx : [https://goerli.etherscan.io/tx/0xc0e2bf13e0a07beba7b0ee0b3b81120b9b3e7bf950f9074e0cc3e311222c602e](https://goerli.etherscan.io/tx/0xc0e2bf13e0a07beba7b0ee0b3b81120b9b3e7bf950f9074e0cc3e311222c602e)
    - before L2 TON : 0
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0x8f71a8b30f6eb9ce8aa4c7f7f571e0cbcfdf432ed022c586cb42aa38f27f5ee6](https://goerli.explorer.tokamak.network/tx/0x8f71a8b30f6eb9ce8aa4c7f7f571e0cbcfdf432ed022c586cb42aa38f27f5ee6)
    - after L2 TON : 1
  - depositWTON
    - L1 tx :[https://goerli.etherscan.io/tx/0xb20723a53b7582108d43a097e0f5d503b76f8257743216527e81271f203ecbe5](https://goerli.etherscan.io/tx/0xb20723a53b7582108d43a097e0f5d503b76f8257743216527e81271f203ecbe5)
    - before L2 TON : 1
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0xce71f6e658e21bd50a97ac4334f0835ce082c3c42c9d5c8321577e133793c6ba](https://goerli.explorer.tokamak.network/tx/0xce71f6e658e21bd50a97ac4334f0835ce082c3c42c9d5c8321577e133793c6ba)
    - after L2 TON : 2
  - depositWTONTo
    - to : 0x43700f09B582eE2BFcCe4b5Db40ee41B4649D977
    - L1 tx : [https://goerli.etherscan.io/tx/0x4ecef11a09416f6e533d7c7cb37ae33f24706b58d3712c7bc8247e695ad9c56e](https://goerli.etherscan.io/tx/0x4ecef11a09416f6e533d7c7cb37ae33f24706b58d3712c7bc8247e695ad9c56e)
    - before L2 TON : 1
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0xf65bd9030bba8f026fe5fe6c2205794048564b16e779d71b2f5b482dedcc6544](https://goerli.explorer.tokamak.network/tx/0xf65bd9030bba8f026fe5fe6c2205794048564b16e779d71b2f5b482dedcc6544)
    - after L2 TON : 2
  - depositWETH
    - L1 tx : [https://goerli.etherscan.io/tx/0x0be9b46a7db7a052ffca3b7c89ee775cac9c6c252cbd67490f0946bf1c8083b4](https://goerli.etherscan.io/tx/0x0be9b46a7db7a052ffca3b7c89ee775cac9c6c252cbd67490f0946bf1c8083b4)
    - before L2 ETH : 1.679183934120409359
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0xe5f8e0db8a3a61fa7cd4595385a919ca4375e8310d3232eb6aef2f64097f4cae](https://goerli.explorer.tokamak.network/tx/0xe5f8e0db8a3a61fa7cd4595385a919ca4375e8310d3232eb6aef2f64097f4cae)
    - after L2 ETH : 1.689183934120409359
  - depositWETHTo
    - to : 0x43700f09B582eE2BFcCe4b5Db40ee41B4649D977
    - L1 tx : [https://goerli.etherscan.io/tx/0xa01d6fe136410fde006eabac262abe5221241dc3533a81c3450b85d663150a47](https://goerli.etherscan.io/tx/0xa01d6fe136410fde006eabac262abe5221241dc3533a81c3450b85d663150a47)
    - before L2 ETH : 0.198338996147373528
    - L2 tx : [https://goerli.explorer.tokamak.network/tx/0x444249216e287a4994a2d680ec5ea6fc6e64a11dae5efd1b992641e913e616fc](https://goerli.explorer.tokamak.network/tx/0x444249216e287a4994a2d680ec5ea6fc6e64a11dae5efd1b992641e913e616fc)
    - after L2 ETH : 0.208338996147373528
  - approveAndCall (script)
    - 