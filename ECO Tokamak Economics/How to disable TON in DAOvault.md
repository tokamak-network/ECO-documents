DAOVault의 변경 없이 DAOContract의 변경으로 DAOVault의 TON을 사용하지 못하게 하는 방법 정리

## 변경 지점

1. DAOContract의 onApprove함수 변경 → Agenda 생성자체 불가능 (O)
1. DAOContract의 executeAgenda함수 변경 → Agenda가 통과되어도 실행 불가능

## 변경 내용

1. DAOVault의 claimTON agenda 실행불가
1. DAOVault의 claimERC20 function실행일때 address가 ton일 경우 실행불가
1. DAOVault의 claimWTON function일때 amount값이 DAOVault가 가진 WTON보다 높을 경우 실행불가

or

1. DAO Agenda로 DAOVault의 ton주소 변경 (setTON함수 실행) 
DAOCommitteeOwner로 이용하여서 함수 추가하여 변경
1. DAOVault의 claimERC20 function실행일때 address가 ton일 경우 실행불가

claimActivityReward 수정

daoVault.claimTON(_receiver, amount);  → claimWTON → 수정하면서 WTON이 모지랄 경우 TON으로 변경될 가능성이 있어서 setTON을 필수적으로 진행하여야함.

## Git

[https://github.com/tokamak-network/ton-staking-v2/tree/daoVault_agenda_check](https://github.com/tokamak-network/ton-staking-v2/tree/daoVault_agenda_check)

## 
Test

npx hardhat test test/DAOVault/1.test.js

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3afb46b1-debe-4151-a467-83c5d4941c39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSIAKN5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T035928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5yi7n%2Fxo2tZawtkp40ZNP9JS7mAu%2BmNcZfyr2Nq3oMwIgSfq2llzvBKEPCHFn15rY8UyzPFcTAfp%2FJESjpu06F50q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFcNdtNRmrO9XYP45ircA6cXTbDQ9h%2B6Muip63p9RzPOT2%2FkvYF%2BkUfsHLg2KdgEWJvPfJBPjyK3suzNZ7igUN2ufSwIlaXJ1Kjv%2FFQlsYYaVvBfd9GlQEfZgy620DVQ5PGUPJ20vpt5iIc1xZzghezTK4NGiu0Pb3u4lza%2FTTqHdlbBR9ODRnU%2FvbV%2BDaxK8EA9Xw9VhewZO0eL8VN1LczvNvYnVGAgsUOX1WbE3NkzKdjxQL7ONHHKfKwiPTYEPQJSltaDitNU8T3tseYS7z%2BNXdnqml%2FtH9PDSswfczincI3TFp6vg0x9x58gY8TxL074k2uJS8l04gFkGxFQY%2FIpomaAuo%2BO86TPyLqBMByo9svClfV9MJJvLjd6JOzOTje1poSvTlNe9sOElgS8sDh8%2FQr8s9LXryXeodjBet21klxPvb32rR4u9YVccMpc96ttv%2FkVYYp%2FLGxVvYLjCmb8l9ohHcRCvNKcCalYTxsyK0RYwmxf9IZutEzYDd7ddonjNcrTCLO6qFlaTGZwjO01sKKvS%2BNthbg0EyKKBpRF5AtENTnMmBI%2B2U5asu%2F9baSKEjJdz7TjippsPhEiffr5BYaEVYS0e0%2B3hCui%2FtV4KXkvpli%2FnQwqHdf191WITcCfp5I4MP2XxfgVMMrz2cwGOqUBWviOYvigTdUn5tCoFpP6Z9cNdBrIUhiibJ2ieI79dXloJEXCVUOL7I9xbDIQhzCn%2BqAsuntGRM9%2B4oBRM1naIml1P3GPrIRAhJYPOJI26r%2BN%2F3EqL6H80fK4n2lhu%2BjpmGqE0HREkROnAa9kCuJGQkhQ5X9Zz0mn2xF8JN9qOKvbDqPRituGBkwVfheGW1c0N7JJScpRxdKEuIo1G1sg8A7j%2FxnY&X-Amz-Signature=d8d954eb439cb0c8d2929ebf34f0fd1bd658ff8a0020b926b2d589c4b21b3751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Setting the DAOCommitteeDAOVault
  - DAOContract 배포 및 세팅
- Agenda Test
  - DAOVault의 claimTON agenda 생성 불가 테스트
  - DAOVault의 claimERC20 address가 ton일때 agenda 생성 불가 테스트
  - DAOVault의 claimERC20 address가 wton일때 agenda 생성 가능 테스트
  - DAOVault의 claimWTON (amount가 넘었을때) agenda 생성 불가 테스트
  - DAOVault의 claimWTON (amount가 넘지않았을때) agenda 생성 가능 테스트

## Audit

[[Audit for DAOVault dont use TON]]

## 컨트랙 배포

1. DAO 로직 배포
  1. ContractName : DAOCommitteeDAOVault
  1. tx : 
  1. 배포된 DAOCommitteeDAOVault 주소 : 
1. DAOCommitteeProxy puaseProxy 변경
  - DAO **어드민 계정 : 0xb4983da083a5118c903910db4f5a480b1d9f3687**
  - DAOCommitteeProxy: [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)
  - 현재 값 : True ([https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F17](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#readContract#F17))
  - setProxyPause abi 
```javascript
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
```
  - 변경 값 : false
1. DAOCommitteeProxy upgradeTo
  - DAO **어드민 계정 : 0xb4983da083a5118c903910db4f5a480b1d9f3687**
  - DAOCommitteeProxy: [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)  
  - upgradeTo abi
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
    }
]
```
  - upgradeTo addr : 
  - tx : 
1. DAOCommitteeProxy puaseProxy true
  - DAO **어드민 계정 : 0xb4983da083a5118c903910db4f5a480b1d9f3687**
  - DAOCommitteeProxy: [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)
  - setProxyPause abi 
```javascript
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
```
  - 변경 값 : true