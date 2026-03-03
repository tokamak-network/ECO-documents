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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3afb46b1-debe-4151-a467-83c5d4941c39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLCSWJ5Z%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHYd563sYtSgJjcaPEyzw7%2FyAfQoa6vIuxxpxvhqBfJAiBLceG9ep2xMIaWffrwgUr6bMYtPxCRTN21w%2BDHidoWYSr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMkEFHHTfYgrIjhPWBKtwDrFasX6pfjxugB8Ft72pciEUSP76QqVTqqXl%2FJgYWtsBdEufE8TOfjVvn67V2imtL1NJm5GbmlYhHifl03Kn7BcrCkTZrZ0r9SutujPhsRiuyl2j3Xj%2FHVqqkUApjKv4wc6GHzH%2BHmjcaFny%2Ff27SZmGlbm3ZDJ8IkeEHufT8SzfNDl00P41iEOQHDLy%2BEScefUgj4a7WNZ6fdUUmJgWescVn9ReE984wSUbY8SrVURJKzp%2B3cavdP86fHrROFtASBiQepMNOT8N8IhZh5MptmTqCZRiyk6QhoSIawDLSMThYqFKA%2FDPnMtMourUnDmoki4EARMwlSXieoEYXAASzf8fz%2B%2BP1pJzafBeRmOiM66fEEyVUjTlSCnhckGKy3CCI90YN3xCa69eKcba5T8xzJx1oq5LtSs7sMI%2BB5FIBuqNsiuh8TWYwvRK8o9R7OlVPbepadVbPF0rJygFHn%2B2bxNbZcxQvB6FqWXkIeT56A22HDlG99hL%2Fb9KL706jwdrd9lQ8gj3q3ytrWh6X0f2Jw50Lj%2FWSXLxN%2BTFGtzIWYg47JuFTlv%2FEy9%2Bbu8zDxhKF3SR8nK58sYR2r0yJwQfI31oqzlciHJexevRf4W6amAZjAwjTHXSgeY6XeJUw2O%2FazAY6pgGv2ZgenriTl2JtBDhx8XTKG5CSJlpbvUgKHU9VdyeqPq9oMOeFax6xITuoi0R%2FugCQijYtlXsM0XvLnbHkIWujAKPZPHxs4ucWKq0MdVo8%2FZknDKSA1kpWbxQ%2Brqc%2FQJtRl6mqbTyteDiQK5wkBhEJX%2FzRTN7%2BkcgHZpCVnNsJKWe8Ui9fBN%2BB6MY0DZni%2FGwGo7V%2BWXubGRbwoc1eu0TtWLsoFPgS&X-Amz-Signature=d5489154a9008e3bf4a09f723ee677fbf948199164875eedf3ed49848e724e7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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