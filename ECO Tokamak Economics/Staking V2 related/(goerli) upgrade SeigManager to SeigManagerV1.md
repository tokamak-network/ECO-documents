# SeigManagerV1 로직 업그레이드 내용 

- SeigManagerV1 : [[upgrade SeigManager]]  
1. 기존 SeigManager의 **totalSupplyOfTon()**** **함수 안에 상수로 쓰여진 부분( <u>시뇨리지 발생 시작 블록번호 , 다오에 의해 번된 양</u>) 을 <u>스토리지 변수로 변경</u>하였습니다.  → 코드의 가독성을 높이고,  같은 컨트랙 코드로 다른 네트웤에서 사용할 수 있게 하기 위해서 수정하였습니다. 
1. **stakeOfAllLayers() **함수 추가 : 모든 레이어의 스테이킹 총량 조회 (발행된 시뇨리지에서 레이어에 할당된 시뇨리지만 포함됨) 
1. **unallocatedSeigniorage() **함수 추가 :  시뇨리지가 발행되었으나, 아직 레이어에 할당되지 않은 양 조회
1. **totalSupplyOfTon_2**()  함수 추가 : 18732908 블록전에 totalSupplyOfTon()으로 사용되던 함수 
1. **CommitLog1  **이벤트 추가 : 업데이트 시뇨리지 실행시  CommitLog1 이벤트 추가함. 실제 시뇨리지 발행양과 팩터에 의해 계산되어 시뇨리지 발행량 확인 가능함. 

# 계정 및 대상 주소 

- DAO **어드민 계정 :  0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2**
- DAOCommitteeProxy:  **0x3C5ffEe61A384B384ed38c0983429dcDb49843F6**
  - current impl (DAOCommitteeDAOVault) : 0x3C5ffEe61A384B384ed38c0983429dcDb49843F6
  - (DAOCommitteeOwner) : 0x3689483f75c89ca28046350a839efc4e5e174d53
  - (DAOCommitteeOwnerTestBed) : 0x43197b6c38eb35467e40d9Cba25277c0805F0244
- SeigManagerProxy : **0x50255c955d0F760C8512ff556453AEe6502ef47f**
  - current impl(SeigManager) : 0x378D9eF8B71CC8bcEe6F858Fe3aB2a13497f335B

총 사용 : gas :    gas,  ** **ETH , 40 gwei기준   

# 1. 컨트랙 배포 

## 1-1. SeigManagerV1 배포 

deployer: 0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2

`npx hardhat deploy --network goerli `

deploying "SeigManagerV1" (tx: 0xff6fdc874fce32c9de6edf600003cebe8e2904eb938e4b4e8abd3c1b352718ca)...: deployed at 0xD28724CF7a8c35c05b86F4d418109993f6c6F95F with 5257491 gas

`npx hardhat verify 0xD28724CF7a8c35c05b86F4d418109993f6c6F95F --network goerli`

- 배포된 SeigManagerV1 : **0xD28724CF7a8c35c05b86F4d418109993f6c6F95F**
- tx:   [https://goerli.etherscan.io/address/0xd28724cf7a8c35c05b86f4d418109993f6c6f95f](https://goerli.etherscan.io/address/0xd28724cf7a8c35c05b86f4d418109993f6c6f95f)
- used gas : 5,257,491 gas 

# 2. 함수 실행 

- 실행 계정 : DAO **어드민 :  0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2**
- DAOCommitteeProxy:  **0x3C5ffEe61A384B384ed38c0983429dcDb49843F6**

## 2-1. DAO 로직 변경 

- Write Contract 탭 
- ** **실행함수 :  **upgradeTo **
  - imple : (DAOCommitteeOwnerTestBed) : 0x43197b6c38eb35467e40d9Cba25277c0805F0244
- tx :   [https://goerli.etherscan.io/tx/0xb9bb1ab999ee34f8a9d75a7f139dfdce45ad0bc19a2bf2044af6488980768280](https://goerli.etherscan.io/tx/0xb9bb1ab999ee34f8a9d75a7f139dfdce45ad0bc19a2bf2044af6488980768280)
- gas :   46,041  gas,  ** **ETH , 40 gwei기준

## 2-1. DAO puase 중지

실행함수 :  **setProxyPause**

- tx: [https://goerli.etherscan.io/tx/0xa1ea28bce311668c8816a61c1f6c146993af126afc3a5052b4c03a25ae0fbd10](https://goerli.etherscan.io/tx/0xa1ea28bce311668c8816a61c1f6c146993af126afc3a5052b4c03a25ae0fbd10)
- gas : 43,458 gas,  ** **ETH , 40 gwei기준

## 2-2. SeigManager 로직 변경 

- ** **실행함수 :  **setTargetUpgradeTo**
  - target :   **0x50255c955d0F760C8512ff556453AEe6502ef47f**
  - logic : 1-1에서 배포한 SeigManagerV1 주소    **0xD28724CF7a8c35c05b86F4d418109993f6c6F95F**
- tx :  [https://goerli.etherscan.io/tx/0x438b6195e0c4abb747ca0c433cdc7d444a89ae07535c8743f356ea6edcc25d2f](https://goerli.etherscan.io/tx/0x438b6195e0c4abb747ca0c433cdc7d444a89ae07535c8743f356ea6edcc25d2f)
- gas :   105,616 gas,  ** **ETH , 40 gwei기준

## 2-3. DAO puase 실행 

실행함수 :  **setProxyPause**

- tx: [https://goerli.etherscan.io/tx/0x4e3e76ad82b90f96cceeaa78967820ff496031bcb97bf6a41be2d0b51fc8cfb9](https://goerli.etherscan.io/tx/0x4e3e76ad82b90f96cceeaa78967820ff496031bcb97bf6a41be2d0b51fc8cfb9)
- gas :   43,476 gas,  ** **ETH , 40 gwei기준

# 3. 테스트

세그매니저에서 아래 view 함수가 모두 있는지 동작확인 

- **totalSupplyOfTon()**   
- **stakeOfAllLayers()**
- **unallocatedSeigniorage()** 
- **totalSupplyOfTon_2**()  

업데이트 시뇨리지 정상 실행 ( test site : [https://goerli.staking.tokamak.network/staking](https://goerli.staking.tokamak.network/staking) )  

  