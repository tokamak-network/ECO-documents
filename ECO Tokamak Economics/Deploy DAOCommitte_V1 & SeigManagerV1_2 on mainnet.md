업데이트하는 경위 : e639690d-8b94-4af7-a77b-dc20867867ff 

Audit 진행 : 591f391c-c703-4c78-b73d-70369c44962f 

Sepolia 테스트 : 

1. [[DAO Test ]] 
1. [[취약점 수정 + TON don’t use 테스트]] 
- 추가작업 내용
  - 시그매니저 로직 업데이트 : 사용자가 스테이킹할때, 해당 레이어의 오퍼레이터가 1000톤을 스테이킹하지 않았다면 실패가 나도록 함
  - 다오 로직 업데이트 : **해당 레이어의 오퍼레이터가 1000톤을 스테이킹하지않았다면 다오 멤버 신청을 못하도록 함**
  - 프론트 화면 업데이트
- DAO **어드민 계정 : 0xb4983da083a5118c903910db4f5a480b1d9f3687**
- DAOCommitteeProxy: [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)  
- 총 필요 가스비 : 0.5 ETH (**0.43636756 ETH, 40Gwei 기준, **)

필요계정

1. Deployer 계정
  1. **0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea** (필요 가스비 : 0.25 ETH, [0.21639952 ETH] )
  1. **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F **(필요 가스비 : 0.25 ETH, [0.21293064 ETH] )
1.  Setting 계정
  1. 0xb4983da083a5118c903910db4f5a480b1d9f3687 (필요 가스비 : 0.01ETH, [0.0054216 ETH] )

## 1. DAOCommitte_V1 배포

- deployer : **0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea**
- repo : [https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit](https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit)
- ContractName : DAOCommittee_V1
- deploy script : npx hardhat run scripts/1.deploy_DAO.js --network mainnet
- expected gas : 5,409,988
- tx : [https://etherscan.io/tx/0xb3ee29dbc9a7859e0e552d875b8521dde4116fbfd2d3bc69d917b76ccc108c1d](https://etherscan.io/tx/0xb3ee29dbc9a7859e0e552d875b8521dde4116fbfd2d3bc69d917b76ccc108c1d)
- DAOCommittee_V1 주소 : 0xdF2eCda32970DB7dB3428FC12Bc1697098418815

### 2. SeigManagerV1_2 배포

- deployer : **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F**
- repo : [https://github.com/tokamak-network/ton-staking-v2/tree/SeigManagerV1_2](https://github.com/tokamak-network/ton-staking-v2/tree/SeigManagerV1_2) 
- `npx hardhat run scripts/2.deploy_SeigManagerV1_2.js --network mainnet`
- expected gas :  5,323,266deploy
- tx : [https://etherscan.io/tx/0xd1b4669e93124ebb1f4661d254f7fb2300765fce63cd85178b04c6514dc0d585](https://etherscan.io/tx/0xd1b4669e93124ebb1f4661d254f7fb2300765fce63cd85178b04c6514dc0d585)
- SeigManagerV1_2 주소 : **0x8813C76858C2fc048B14Bd4c75F2Daee43c79958**
- `npx hardhat verify `**`0x8813C76858C2fc048B14Bd4c75F2Daee43c79958`**` --network mainnet`


# 아래는 DAOProxy에서 하는 작업입니다.

- DAO **어드민 계정 : 0xb4983da083a5118c903910db4f5a480b1d9f3687**
- DAOCommitteeProxy: [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)  

myCrypto : [https://app.mycrypto.com/interact-with-contracts](https://app.mycrypto.com/interact-with-contracts)

myEtherwallet : [https://www.myetherwallet.com/wallet/interact](https://www.myetherwallet.com/wallet/interact)

## 3. DAO 프록시 오픈

- 실행함수 :  **setProxyPause**
abi
```json
[
	{
        "inputs": [
          {
            "internalType": "bool",
            "name": "_pause",
            "type": "bool"
          }
        ],
        "name": "setProxyPause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```

  - etherscan : [https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeContract#F5](https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeContract#F5)
  - _pause :  false (체크해제)
  - expected gas : 43,458
  - tx : [https://etherscan.io/tx/0xd252d5eaba0aa18bdd96af30c3285af34b322664b650b1ad797f76a9be0375f8](https://etherscan.io/tx/0xd252d5eaba0aa18bdd96af30c3285af34b322664b650b1ad797f76a9be0375f8)

## 4. SeigManagerProxy의 로직을 SeigManagerV1_2로 변경

1. ~~DAO 로직 DAOCommitteeOwner로 변경~~
  1. ~~실행함수 :  ~~~~**upgradeTo**~~

~~abi~~
```json
[
	{
        "inputs": [
          {
            "internalType": "address",
            "name": "impl",
            "type": "address"
          }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```

  - ~~impl : 0xe070fFD0E25801392108076ed5291fA9524c3f44~~
  - ~~expected gas : 46,041~~
  - ~~tx : ~~
1. SeigMangerProxy의 로직 변경
  1. 실행함수 : **setTargetUpgradeTo**
  - etherscan : [https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeProxyContract#F23](https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeProxyContract#F23)
  - target : 0x0b55a0f463b6DEFb81c6063973763951712D0E5F
  - logic : **0x8813C76858C2fc048B14Bd4c75F2Daee43c79958**
  - tx : [https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46](https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46)
  - expected gas : 40,395

## 5. DAO 로직 DAOCommittee_V1으로 변경

새로 배포한 DAOCommittee_V1로 로직 변경

- 실행함수 :  **upgradeTo**
abi
```json
[
	{
        "inputs": [
          {
            "internalType": "address",
            "name": "impl",
            "type": "address"
          }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```

  - etherscan : [https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeContract#F6](https://etherscan.io/address/0xdd9f0ccc044b0781289ee318e5971b0139602c26#writeContract#F6)
  - impl : 0xdF2eCda32970DB7dB3428FC12Bc1697098418815
  - expected gas : 46,041
  - tx : [https://etherscan.io/tx/0xbcf5cfd88aacbc7e8b8c5562c7780902c9c0e0e2ac6f807e8dd900c83f4e8094](https://etherscan.io/tx/0xbcf5cfd88aacbc7e8b8c5562c7780902c9c0e0e2ac6f807e8dd900c83f4e8094)

# Test

## `DAO 취약점 수정 internal test 확인`

`repo : `[`https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit`](https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit)

`npx hardhat test test/agenda/9.deployed-test-mainnet.js`

## `심플스테이킹 기본 기능 테스트 (fork 해서 test) `

 `npx hardhat test test/simple-staking/0.seigManger.ts `