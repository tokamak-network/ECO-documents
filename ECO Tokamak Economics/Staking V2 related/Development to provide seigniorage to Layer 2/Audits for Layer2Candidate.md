## Repo 

[https://github.com/tokamak-network/ton-staking-v2/tree/audit_v1_Layer2Candidate](https://github.com/tokamak-network/ton-staking-v2/tree/audit_v1_Layer2Candidate)

## Contracts 

- L2Registry 
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/L2RegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/L2RegistryV1_1.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/L2RegistryProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/L2RegistryProxy.sol)
- OperatorFactory
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol)
- Layer2Manager
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerProxy.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol)
- Operator
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorProxy.sol)
- Layer2CandidateFactory
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactoryProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactoryProxy.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactory.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactory.sol)
- Layer2Candidate
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/Layer2CandidateProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/Layer2CandidateProxy.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/Layer2CandidateV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/Layer2CandidateV1_1.sol)
- SeigManagerV1_3
  - [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/stake/managers/SeigManagerV1_3.sol)

## Contracts Design  

[[Development to provide seigniorage to Layer 2]] 

[[Development to provide seigniorage to Layer 2]] 

### Reference ( Old Contracts ) 

[https://github.com/tokamak-network/plasma-evm-contracts](https://github.com/tokamak-network/plasma-evm-contracts)

[https://medium.com/onther-tech/looking-into-tokamak-networks-staking-contract-7d5f9fa057e7](https://medium.com/onther-tech/looking-into-tokamak-networks-staking-contract-7d5f9fa057e7)

[https://docs.google.com/presentation/d/1Uhjd3xF6OVoucAwZ7AuL_N1HJE5q-U6fLlvHKtZ0Hhw/edit#slide=id.p](https://docs.google.com/presentation/d/1Uhjd3xF6OVoucAwZ7AuL_N1HJE5q-U6fLlvHKtZ0Hhw/edit#slide=id.p)

## List 

### Harvey 

- [ ] H_1. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol#L47](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol#L47) DepositManager 한번 세팅시 변경이 안되는데 변경이 안되게 할 계획이신가요? (Layer2Manager에서는 변경가능하게 하였음)
- [ ] H_2. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol#L75](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/factory/OperatorFactory.sol#L75) systemConfig 컨트랙트 하나당 오퍼레이터 컨트랙트 하나로 세팅되나요?
- [ ] H_3. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol#L158](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol#L158) 
0.8.4 버전으로 개발하는 이유가 있을까요? 0.8.24 버전에선 mload가 아닌 tload를 쓸 수 있고 가스비가 더 효율 적입니다. 
- [ ] H_4. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol#L293-L296](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/Layer2ManagerV1_1.sol#L293-L296) 
approveAndCall로 호출하는 것보다 _approve형식처럼 ton.allowance로 검사하고 WTON Contract의 swapFromTON함수만 호출하는 것이 가스비가 더 절약되지않나요? 
- [ ] H_5. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L51](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L51) 
layer2Manager, DepositManager를 한번 등록하면 변경할 계획이 없으신건가요?
- [ ] H_6. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L47-L49](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L47-L49) 
현재 누구나 세팅할 수 있도록 되어있습니다. (OperatorFactory에서만 호출가능하게 변경하거나 owner가 호출가능하게 변경해야할 것 같습니다.) (현재 한번세팅하면 변경을 못하고 한트랜잭션에서 세팅을 다해서 문제없어보이긴 합니다.)
- [ ] H_7. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L133](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/layer2/OperatorV1_1.sol#L133)
더이상 추천하지않는 payable방식입니다. (참조 : [https://solidity-by-example.org/sending-ether/](https://solidity-by-example.org/sending-ether/))
- [ ] H_8. [https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactory.sol#L43C1-L68C2](https://github.com/tokamak-network/ton-staking-v2/blob/audit_v1_Layer2Candidate/contracts/dao/factory/Layer2CandidateFactory.sol#L43C1-L68C2)
이 함수도 dao에서 세팅할 수 있도록 하면 어떨까요? 
- [ ] H_9. 