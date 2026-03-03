# In L2 tab

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a2775ef0-e082-489f-8c11-cadd8b6c7c39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXO27J3W%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBv59%2FDImJP3x5P6Th57c%2BiRmdZCZM8ORxRFaeQQUEXgIgQym9Tk9qr0Wvy1TbFKW2XlLd%2FKi7ydjQBsefRNJ0JV0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDPJMn7I5JkQ%2Ftl%2BzPSrcA9S6LV9084YY7uEmy0y%2FqGtMvcn5DajQcBpuJUwMucU%2F3ylfK2zuajsKZOURU88oWyxfYp8CGUCG9ySue9gegLd%2BfzHbt4guPJnPsF57mlSM2mP7qvDPi34CCKyPI%2BILWVtFX8zCIQw2sHB4jINqQfJOhLujulbqVuDyYE1MCZcp5LW2%2BYill03kGdfRtIeVLdhQic6JrBpZYxq%2F01jE1sJx6n1kX%2FOwSQP7eOr0AZqWAnKGiyJOAbV%2F8IuJgT0orxtK3zNvVVGrQiPISe3JYkbPQKJ0E2PVCmDywLjJvap%2FSEWpw7V1rMvG1LzMjvYBnU7GgMlY0SIu6mui3PDPZWsZ5f4fu3QVw%2FkoR9ZQJ4a%2FqSK9SGphR6qvgoANlyIoWeK7L5dSKT11d4Her%2Fb7duCSIt5QnGF2Vim4C7HmUzPNngWrDWnmGOOQJel6FqtdtRz5bZr5cFmaf%2F1PaaUq7R2ZO%2BCvmEj8TPj2%2BlrH%2BiclVdP759PBvJhRa7wEFhOwZ%2BfxC%2B%2B9m697g%2FEMoH7FS9QUy%2BmKg3pjxU1w07OwIdo07oE0UKVNeCv6tFD%2FoJG3%2B%2FT%2BFbH160H7w%2FvfAIdhUEePsADdJEFkFrA9My5CD3AgAaHwL3Lo2GbYj%2FQjMMiY28wGOqUBBU%2Ff6spXdj0nGpY8Vwf3X8OvGV2EERbJRMP%2BoWZgeCq4GIOsg7mfz5kYc0KvyZPm0iRgl%2F4jTo8lElctmQWr%2FidctlTR1%2F5JDm4iuErfqV%2BLqNctUdoVFDi0L7ln8OaD69LJGSEDhEFTSNyy%2FDLTmE59gBA6WOJ1H1KYrwQYVsG2%2FIm%2F%2BGK8tXbtKc7bkHVUawmxtyr%2F3m4%2BtqWTZkP4NSsYA2ff&X-Amz-Signature=f8abb2c868a456eb48e3da651e3da63c3fb05590240e3f29282dc08e0b2a9b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **L2 registry date** → check by event Zena님 답변
  - [Layer2Candidate 등록시 발생되는 이벤트](/45bcb8cbd5064df192a93c199b07f464#775511ea43374128a3ac2d57c0a86dcc)  (RegisteredLayer2Candidate, RegisteredSystemConfig ) 가 발생될때의 트랜잭션, 블록 번호를 알 수 있습니다. 해당 블록에 정확한 시간은 따로 없기 때문에 블록정보를 조회하여 block.timestamp 로 시간을 가져올 수 있습니다.   
1. **L2 open date** → bridge contract deployment txn date Zena님 답변
  1. [systemConfig 컨트랙](https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol)에는 bridge contract 정보를 가져오는 인터페이스가 있습니다. 
  1. 해당 컨트랙에 startBlock() 함수가 있기는 하지만 초기값(설정안된경우) type(uint256).max로 설정되고, op-node에서 사용하는 목적으로 만든것 같습니다. 이 값을, bridge contract deployment txn 블록번호를 가져오는 것이 타당한것인지는 core-team에 문의해보셔야 할것 같습니다. 이 외에는 컨트랙에 다른 정보는 없는 것 같습니다. 
1. **TON locked in Bridge** → ton.balanceOf(proxy bridge contract address)
  1. L2Registry.systemConfigType(address systemConfig) 로 조회 값을 통해 해당 레이어의 종류를 먼저 알아야 합니다. 레이어의 타입에 따라 조회하는 대상이 달라집니다. 
    1. 조회결과 1 일때, legacy 이기 때문에 : ton.balanceOf(proxy bridge  address)
    1. 조회결과 2일때, bedrock 이기 때문에 : ton.balanceOf(proxy optimism portal  address)
  1. L2 컨트랙의 브릿지 및 포탈주소는 SystemConfig 를 통해 얻을 수 있습니다.  
    1. proxy bridge  address : [SystemConfig.l1StandardBridge(](https://github.com/tokamak-network/tokamak-thanos/blob/6a06d9830bd71b62795cf6a9a648195232d3cf6c/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol#L226-L227))  
    1. optimism portal address : [SystemConfig.optimismPortal()](https://github.com/tokamak-network/tokamak-thanos/blob/6a06d9830bd71b62795cf6a9a648195232d3cf6c/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol#L236C14-L237)  
1. **Earned seigniorage** → Same as candidate? Zena님 답변
  1. 업데이트 시뇨리지 실행시 변경된 이벤트가 있습니다. 
    1. 삭제된 이벤트 
```javascript
event **SeigGiven**(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig);
```
    1. 추가된 이벤트 
```javascript

/**
 * Event that occurs when seigniorage is distributed when update seigniorage is executed
 * @param layer2        The layer2 address
 * @param totalSeig     Total amount of seigniorage issued
 * @param stakedSeig    Seigniorage equal to the staking ratio in total issued seigniorage
 * @param unstakedSeig  Total issued seigniorage minus stakedSeig
 * @param powertonSeig  Seigniorage distributed to powerton
 * @param daoSeig       Seigniorage distributed to dao
 * @param pseig         Seigniorage equal to relativeSeigRate ratio from unstakedSeig amount
 *                      Seigniorage given to stakers = stakedSeig + pseig
 * @param l2TotalSeigs  Seigniorage distributed to L2 sequencer
 * @param layer2Seigs   Seigniorage currently settled (give) to layer2Candidate's operator contract
 */
event SeigGiven2(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig, uint256 l2TotalSeigs, uint256 layer2Seigs);

```
  1. 이외의 다른 이벤트는 기존과 동일합니다. 
  1. [만일 업데이트 시뇨리지를 하는 주체가 L2 오퍼레이터인경우, ](/45bcb8cbd5064df192a93c199b07f464#4507c1810b54464bae057c72c082c479)
    1. 해당 컨트랙의 오퍼레이터 여부 확인 방법 : [link](/45bcb8cbd5064df192a93c199b07f464#aba2e3a947a54c8ba31ae7852cd67928)
```javascript
OperatorContract address = Layer2Contract.operator()

/// If it is true, account is an operator who receives the seigniorage assigned to the L2 sequencer  
OperatorContract.isOperator(account) 

/// If it is not address(0), it is Layer2Candidate 
OperatorContract.systemConfig()  
```
    1. 해당 오러페이터는 기존과 동일하게 시뇨리지를 받습니다.  **Earned seigniorage **
    1. 해당 오퍼레이터는 두가지 옵션을 선택할 수 있습니다. [example](https://github.com/tokamak-network/ton-staking-v2/blob/5600646c67f0ffc9a7d2f6d16aaadb728beb0f2a/test/layer2/units/5.stake-v2-gas.sepolia.test.ts#L2311-L2314) 
      - 실행 컨트랙 : 해당 Layer2Candidate 컨트랙 
      - 실행 함수 : 
        - afterCall 이 0일때, 업데이트 시뇨리지만 실행하면서, 해당 Layer2Candidate의 시퀀서가 받을 금액을 정산받습니다 .
          -  따라서 추가되는 스테이킹 금액은 = 받을 시뇨리지
          - 추가로 Operator ⇒ Layer2Contract.operator() 컨트랙에 wton이 layer2Seigs 만큼 증가됩니다. 
        - afterCall 이 1일때, 클래임을 하면서 시뇨리지를 받습니다. 
          - 따라서 추가되는 스테이킹 금액은 = 받을 시뇨리지
          - 추가로  L2sequencer ( Operator.manager() ) 에 wton이 layer2Seigs 만큼 증가됩니다. 
        - afterCall 이 2일때, 스테이킹을 하면서 시뇨리지를 받습니다. 
          - 따라서 추가되는 스테이킹 금액은 = 받을 시뇨리지 + 정산된금액 (layer2Seigs) 이 됩니다. 

```javascript
/// @param afterCall 0: none, 1: claim, 2: staking
function updateSeigniorage(uint256 afterCall) public returns (bool)  
```
1. **L1 contract address** → Zena님 답변
SystemConfig 컨트랙을 통해 L1 Contract Address를 조회할 수 있습니다.[ link](https://github.com/tokamak-network/tokamak-thanos/blob/6a06d9830bd71b62795cf6a9a648195232d3cf6c/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol#L215-L244)

# Withdraw to TITAN

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/112a7b9e-e813-4012-88eb-bf7f08b7ed77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXO27J3W%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBv59%2FDImJP3x5P6Th57c%2BiRmdZCZM8ORxRFaeQQUEXgIgQym9Tk9qr0Wvy1TbFKW2XlLd%2FKi7ydjQBsefRNJ0JV0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDPJMn7I5JkQ%2Ftl%2BzPSrcA9S6LV9084YY7uEmy0y%2FqGtMvcn5DajQcBpuJUwMucU%2F3ylfK2zuajsKZOURU88oWyxfYp8CGUCG9ySue9gegLd%2BfzHbt4guPJnPsF57mlSM2mP7qvDPi34CCKyPI%2BILWVtFX8zCIQw2sHB4jINqQfJOhLujulbqVuDyYE1MCZcp5LW2%2BYill03kGdfRtIeVLdhQic6JrBpZYxq%2F01jE1sJx6n1kX%2FOwSQP7eOr0AZqWAnKGiyJOAbV%2F8IuJgT0orxtK3zNvVVGrQiPISe3JYkbPQKJ0E2PVCmDywLjJvap%2FSEWpw7V1rMvG1LzMjvYBnU7GgMlY0SIu6mui3PDPZWsZ5f4fu3QVw%2FkoR9ZQJ4a%2FqSK9SGphR6qvgoANlyIoWeK7L5dSKT11d4Her%2Fb7duCSIt5QnGF2Vim4C7HmUzPNngWrDWnmGOOQJel6FqtdtRz5bZr5cFmaf%2F1PaaUq7R2ZO%2BCvmEj8TPj2%2BlrH%2BiclVdP759PBvJhRa7wEFhOwZ%2BfxC%2B%2B9m697g%2FEMoH7FS9QUy%2BmKg3pjxU1w07OwIdo07oE0UKVNeCv6tFD%2FoJG3%2B%2FT%2BFbH160H7w%2FvfAIdhUEePsADdJEFkFrA9My5CD3AgAaHwL3Lo2GbYj%2FQjMMiY28wGOqUBBU%2Ff6spXdj0nGpY8Vwf3X8OvGV2EERbJRMP%2BoWZgeCq4GIOsg7mfz5kYc0KvyZPm0iRgl%2F4jTo8lElctmQWr%2FidctlTR1%2F5JDm4iuErfqV%2BLqNctUdoVFDi0L7ln8OaD69LJGSEDhEFTSNyy%2FDLTmE59gBA6WOJ1H1KYrwQYVsG2%2FIm%2F%2BGK8tXbtKc7bkHVUawmxtyr%2F3m4%2BtqWTZkP4NSsYA2ff&X-Amz-Signature=6170a865338f5510676a8d1a8a934fa35666bc9713f362f935dbe95f760caab3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 사용하는 Contract → Layer2Candidate contract 인가요?
  - Zena님 답변
  - 문서 : [link](/45bcb8cbd5064df192a93c199b07f464#afefcfbab3ae47f0978da48f291d61a1)
  - DepositManager 의 withdrawAndDepositL2 함수를 이용하여 withdraw와 L2 deposit을 함께 합니다. Layer2Candidate 일때만 함수가 정상 실행되면 DAOCandidate 일때는 실패합니다 .
```javascript
 /**
   * @dev withdrawAndDepositL2 `amount` WTON in RAY
   */
  function withdrawAndDepositL2(address layer2, uint256 amount) external returns (bool)  
  
```
1. Withdraw button → which contract function?
  1. Zena님 답변
withdraw와 L2 deposit을 함께 하는 기능이라면 위에 같이 설명함. 
1. 하단 withdraw 관련 내역 event?
  1. L1 컨트랙트 기준으로 [2]에 있는 내역 생성 및 타이머 설정 
    1. txn 기준 5분 countdown 타이머 설정
    1. 5분이 지났는데도 “Status” 가 Withdrawn 으로 변경 안됐을때 get help icon + refresh icon 추가
      1. “Status” 타이머에서 “Withdrawn” 변경 조건 → 다음글 확인 (L2 관련) 
      1. get help icon은 [google form](https://docs.google.com/forms/d/16H_To1WJjIVvdS5h6Ng9rTi2EXZhwgz5Oz4IGOdfdwc/edit) 으로 새로운 탭 오픈
      1. refresh icon은 “Status” field 업데이트 trigger 용   
  1. L2 cross domain messenger (0x4200000000000000000000000000000000000007) 기준으로 “DepositFinalized” 으로 타이머를 없에고 “Withdrawn” 으로 변경하고 관련 relayMessage transaction 링크 첨부 (블록 explorer 기준) 
    1. 주의: Thanos의 경우 추가 확인이 필요한듯. 일단 Titan 기준으로 작성함 
    1. relayMessage txn 예: [https://explorer.titan.tokamak.network/tx/0x7ec7ad663bb2f329cd763a755ccb1be354e9c80811e18f1351d224e736a8e010/logs](https://explorer.titan.tokamak.network/tx/0x7ec7ad663bb2f329cd763a755ccb1be354e9c80811e18f1351d224e736a8e010/logs)
1. 새로고침 버튼 눌렀을때 액션?
  1. [여기 확인](/769cb676d0a94d37ae5c1d7e5efc1cba#a06c04555365467885f587d4fa57cccf)

[[Untitled]]