# SeigManagerV1_1 upgrade details

- SeigManagerV1_1 : [[upgrade SeigManager]]  
1. 기존 SeigManager의 **totalSupplyOfTon()**** **함수 안에 상수로 쓰여진 부분( <u>시뇨리지 발생 시작 블록번호 , 다오에 의해 번된 양</u>) 을 <u>스토리지 변수로 변경</u>하였습니다.  → 코드의 가독성을 높이고,  같은 컨트랙 코드로 다른 네트웤에서 사용할 수 있게 하기 위해서 수정하였습니다. 
The parts written as constants in the function (block number where seigniorage occurred, amount burned by DAO) were changed to storage variables. → Modifications were made to improve the readability of the code and allow the same contract code to be used in other networks.
1. **stakeOfAllLayers() **함수 추가 : 모든 레이어의 스테이킹 총량 조회 (발행된 시뇨리지에서 레이어에 할당된 시뇨리지만 포함됨) 
Added function: View the total staking amount of all layers (only the seigniorage assigned to the layer in the issued seigniorage is included)

1. **unallocatedSeigniorage() **함수 추가 :  시뇨리지가 발행되었으나, 아직 레이어에 할당되지 않은 양 조회
Added function: Queries the amount of seigniorage issued but not yet assigned to a layer.
1. **totalSupplyOfTon_2**()  함수 추가 : 18732908 블록전에 totalSupplyOfTon()으로 사용되던 함수 
Function added: Function used as totalSupplyOfTon() before block 18732908
1. **CommitLog1  **이벤트 추가 : 업데이트 시뇨리지 실행시  CommitLog1 이벤트 추가함. 실제 시뇨리지 발행양과 팩터에 의해 계산되어 시뇨리지 발행량 확인 가능함. 
Added event: Added CommitLog1 event when executing update seigniorage. It is possible to check the amount of seigniorage issuance as it is calculated based on the actual seigniorage issuance amount and factors.
- repo :  [https://github.com/tokamak-network/ton-staking-v2/blob/SeigManagerV1/contracts/stake/managers/SeigManagerV1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/SeigManagerV1/contracts/stake/managers/SeigManagerV1.sol)

# 계정 및 대상 주소 

- DAO **어드민 계정 :  0xb4983da083a5118c903910db4f5a480b1d9f3687**
- DAOCommitteeProxy:   [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26) 
  - impl (DAOCommitteeDAOVault) : 0xba5634e0c432Af80060CF19E0940B59b2DC31173
  -  (DAOCommitteeOwner) : 0xe070ffd0e25801392108076ed5291fa9524c3f44
- SeigManagerProxy :  [0x0b55a0f463b6defb81c6063973763951712d0e5f](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f)
  - impl (SeigManager) 0xB1f172d81caED5f264cc4F8908E13C0d2FfB09EE

# 1. deploy contract  

## 1-1. deploy SeigManagerV1    

**deployer**: **0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F**

`npx hardhat deploy --network mainnet`

deploying "SeigManagerV1_1" (tx: 0xc490704b4cc0d4df2419dfb35ba9a74b69c2b1fb5a0b41b9d19af87b523b2230)...: deployed at 0x40aB76c898f30468807fFE823E4ea00570568061 with 5257491 gas

`npx hardhat verify --network mainnet`

- 배포된 SeigManagerV1 :  **0x40aB76c898f30468807fFE823E4ea00570568061**
- tx:   0xc490704b4cc0d4df2419dfb35ba9a74b69c2b1fb5a0b41b9d19af87b523b2230
- used gas : 5,257,491 gas , 50gwei  → **0.26287455 ETH **

# 2. function execution

- DAO **어드민 계정 :  0xb4983da083a5118c903910db4f5a480b1d9f3687**
- DAOCommitteeProxy:   [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26) 
- 마이이더 월렛으로 할경우 [https://www.myetherwallet.com/wallet/interact](https://www.myetherwallet.com/wallet/interact)

Abi 
```javascript
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
    },
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
    },
	{
      "inputs": [
        {
          "internalType": "address",
          "name": "target",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "logic",
          "type": "address"
        }
      ],
      "name": "setTargetUpgradeTo",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
		{
      "inputs": [
        {
          "internalType": "address",
          "name": "_wton",
          "type": "address"
        }
      ],
      "name": "setWton",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
]
```

- 총사용 가스  : **238591 gas , 50 gwei → 0.01192955 ETH **

## 2-1. Change DAO logic  

- Write Contract Tab ([link](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeContract))
- ** **실행함수 :  **upgradeTo**
  - impl :  (DAOCommitteeOwner) : **0xe070ffd0e25801392108076ed5291fa9524c3f44**
- tx :  [https://etherscan.io/tx/0x960f3bccaa8805e8da332b1fe96077c921bb6f8746fc12aad07e05e4b2dc59e7](https://etherscan.io/tx/0x960f3bccaa8805e8da332b1fe96077c921bb6f8746fc12aad07e05e4b2dc59e7)
- gas :   46,041  gas** **

## 2-2. DAO pause  stop 

- Write Contract Tab ([link](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeContract))
- 실행함수 :  **setProxyPause**
  - _pause :  false
- tx: [https://etherscan.io/tx/0xd1333e98c52547be95e8982e7a5f43ab3c100db74ef53fa71746d46feffeb9fd](https://etherscan.io/tx/0xd1333e98c52547be95e8982e7a5f43ab3c100db74ef53fa71746d46feffeb9fd)
- gas : 43,458 gas 

## 2-3. Change SeigManager logic

- Write Proxy Contract Tab : [link](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeProxyContract) 
- ** **실행함수 :  **setTargetUpgradeTo**
  - target :   0x0b55a0f463b6defb81c6063973763951712d0e5f
  - logic : 1-1에서 배포한 SeigManagerV1 주소    **0x40aB76c898f30468807fFE823E4ea00570568061**
- tx :  [https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3](https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3)
- gas :   105,616 gas 

## 2-4. DAO pause open  

- Write Contract Tab ([link](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#writeContract))
- 실행함수 :  **setProxyPause**
  - _pause :  true
- tx: [https://etherscan.io/tx/0x99c8a160874e740d05c3ef4e5ca9e17396fa7befe9da7804313f73702111ae5a](https://etherscan.io/tx/0x99c8a160874e740d05c3ef4e5ca9e17396fa7befe9da7804313f73702111ae5a)
- gas :   43,476 gas 

# 3. test

- Check if all the view functions below are in operation in SeigManager.
  - **totalSupplyOfTon()**
  - **stakeOfAllLayers()**
  - **unallocatedSeigniorage()**
  - **totalSupplyOfTon_2**()
- Update seigniorage runs normally ( web site : [https://simple.staking.tokamak.network/staking](https://simple.staking.tokamak.network/staking)) 
  - tx : [https://etherscan.io/tx/0xfffef62c09686ac4f112fe4927ee302cd04396e4436664840cf25bdbbc3745a4](https://etherscan.io/tx/0xfffef62c09686ac4f112fe4927ee302cd04396e4436664840cf25bdbbc3745a4)

  