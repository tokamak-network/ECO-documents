## DAO Snapshot 업그레이드 배경 

1. 사전 지식 : 지난 1분기에  DAO V2.0의 Lifecycle에 대한 글을 Jason님께서 작성하셨습니다. (참조 : [[Lifecycle of  TIP (KR)]])
1. 배경 요약 : Tokamak DAO는 제안을 체계적으로 다루고, 커뮤니티가 적극적으로 참여할 수 있도록 Tokamak DAO의 Lifecycle에서 DAO Agenda 생성 전 RFC와 Temperature Check단계가 추가되었습니다. 이 중 **Temperature Check단계는 Snapshot에서 진행되는데 해당 Snapshot을 진행한 링크를 DAO Agenda를 넣을때 입력하여서 Agenda의 배경을 확인할 수 있도록 하기 위해서 DAO Agenda를 생성 시 Snapshot 링크를 추가할 수 있도록 Agenda Memo 필드를 추가하는 업그레이드 할려고 합니다.**

## DAO Snapshot 업그레이드 내용

1. 함수 변경 
  1. onApprove : Memo값도 decode해서 createAgenda에 정보 넘겨줌
  1. _decodeAgendaData : Memo값도 decode하도록 변경
  1. _createAgenda : input으로 Memo값도 받으며 storage에 AgendaID에 대한 Memo값 저장 과정 추가
1. Storage 추가
  1. DAO Contract에서 AgendaID에 대한 Memo값을 확인할 수 있도록 mapping storage 추가

## DAO Contract 관련 추가 Bug 수정 내용

1. 버그 발견 함수 : currentAgendaStatus
1. 함수 탄생 배경 : 지난 DAO 업그레이드에서 투표가 끝낫는데 Storage가 변경되지 않은 Agenda에 대해서 다시 해당 Storage를 알맞게 변경시키기 위해서는 endAgendaVoting함수를 실행해서 tx를 발생시켜야 했습니다.
그래서 tx을 생성하지 않아도 현재 Agenda에 대한 상태를 정확히 보여줄 수 있는 함수인 currentAgendaStatus를 추가하여서 언제든 Agenda에 대한 내용을 view함수로 확인할 수 있게 하기 위해서 currentAgendaStatus함수를 추가하게 되었습니다.
1. 버그 발견 : 해당 함수에 대한 테스트를 진행하다 agenda를 생성하였는데 agenda에 대한 Result와 Status의 값들이 일부 제대로 나오지 않는 것을 발견하였습니다. 그래서 이에 대한 로직 수정을 하고자 합니다.

## DAO Snapshot 업그레이드 시기

1. Contract : 이번 CandidateAddOnProxy patch와 TRH팀의 VerificationContract에 대한 아젠다를 생성할 때 같은 아젠다로 진행하면 좋을 것 같습니다. (아직 TRH팀의 VerificationContract 개발완료시기가 확정이 안나서 언제 업그레이드 될지는 확정이 안났으나 만약 DAO Snapshot 및 버그 수정 작업을 한다면 5월 16일까지 작업이 진행될 것 같아서 그전에 TRH팀에서 진행하자고 하면 5월 19일날 진행하자고 논의될 것 같습니다 [5월 19일 이후 TRH팀에서 요청 시 바로 적용 가능])
  1. 위와 같이 되면 아젠다 내용은
    1. DAO Snapshot 로직 업그레이드
    1. CandidateAddOnProxy patch (참조 : https://www.notion.so/tokamak/Patch-CandidateAddOnProxy-1dfd96a400a380e69602ce6b7c590782)
    1. L1BridgeRegistry을 통해 TRH팀에서 개발한 VerificationContract에 등록자권한을 할당 (참조 : [https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/common/AuthControlL1BridgeRegistry.sol#L37-L40](https://github.com/tokamak-network/ton-staking-v2/blob/ca54301b984474c07b3ce026e24f885ff83fd99a/contracts/common/AuthControlL1BridgeRegistry.sol#L37-L40) )
1. Front : 기존 계획인 3분기에 테스트넷에서 진행될 예정입니다.

## Kevin’s Feedback

- 1,2번 먼저 Agenda 생성하고 그 후 3번은 따로 아젠다 진행

## Progress

## Interanl Audit

[[DAO upgraded internal Audit]] 

- Hammer’s report (AuditAgent)
[final_audit_agent_report_1.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/29a96353-3832-445f-83aa-a2cf9944e220/final_audit_agent_report_1.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UV56WJX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9QAPJJ8TzTbiARKhbzcwqQBCNN3oymGyPkpjLpgSWPwIhAPo7Xao38EmqEc6k9I9zXPkxMOQ6XljUsh5Owu6CGg2gKv8DCHQQABoMNjM3NDIzMTgzODA1IgyUpF4zbxa1NFI1yGcq3AMUgZAzkvnAWSzcyIN0oYvIodyragTxzcSCcbvOkyN8uQxxdqIV%2FL%2F1jCLC4qEbf%2BwKGQuHppE%2B5fEQx7D6h0m0%2BwOEasCkL7ZaDe%2FovmGFsoybE8wQlnkQg7NZ7XDXvbOM2owkNKszGCiNKHnZ4vQhpxXiDHvpjUgNJlZ5ReVoEYnfsgeLak1vIxiGOUSZ%2BO%2Bs36yPHF1KBnpZqrcJCbTSOIdneRLWiP0dmeWuZRtQaD0Z3PqAOkSg3fz0Eca%2Ban4I691x92vmwgN7vztsSfMdyF4RQFxYOgtGaKvbvT0ChR7LV%2BedAoSlZxm2Kh10VO7xVywdrlKFznPkiXozxK%2B5xqEWmTXlOclTfpTrHCjxl61FwIxCrFaUpSlvRvyv9MdrYhlvBBIcArG16laq%2Fwf8idDMlz%2Bao9%2F9bVYrm6X%2FfhtmatQ5w%2B0L6bqJtNqXsWi%2FeqJV0%2BUuF%2FerpN3D7Y94Rx49W0EAVEsQm73aKkxVf9YWHi%2FiopYLr6QDa2KvyiOv5eNCtmeCaKRYA%2FIN36ay2T7aTpuCAyNDMumiOSDUCpTueHtTeWR1Y7GCN1EUMsV2HBEOxwgfZy%2BEQGBrPsXaPcV5Lf5U48HDB0E9YYIYkx1e8jjgItuXvf4aNDCP79nMBjqkAU%2BghZUS45EBO6kWq5s%2FYufN%2F5ZTFcEIKuJXG1pYP4BFSBQhbyOaDAhAob3JOuW7d7efWXnzaaIDTaX9Fk5h2gX8PuEl4nSjexl8h%2Fn0HlXJpHdenl7pL2IJ%2BvcLu66Wo75Yl2L1a78AfeeRv1FFE1uHjrF6TmJFWhJ3XSfabhgceJ9K%2BeUgRi%2F%2FxZrD47C0KdLzbNXdzlaCSkhGDdoKddXb3D8p&X-Amz-Signature=3b6c8b38ad1ebe3a94ac82a0908a7ae7506fec7a6a8b0dc86f917d3d989bc395&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Report Summary 
  - The parts that are called Risks in the report are not Risks except for 4, and they were intentionally developed.
  - 1 - WTON is possible with ERC20 call -> Intentionally done
  - 2 - DAOVault call is possible -> Only Owner was called in DAOVault, but this part seems to be a result of not seeing the DAOVault Contract.
  - 3 - Burn to address(1) -> TON does not have a burn function, and giving it to 0 is also blocked, so it was sent to 1
  - 5 - Gas price may increase because multiple functions can be executed -> I did not mention it because it was intended for one agenda to execute multiple functions.
  - 6 - currentAgendaStatus does not have a default value -> Even if there is no default value, the result is always displayed when agendaID is entered, so it is not a problem.
  - 7 - Version issue - Version 0.8.4 is actually more compatible with the currently distributed contract.
But Hammer also knows that there are no problems with other parts and only mentioned part 4.
- Item 4: No upper bound on noticePeriodSeconds or votingPeriodSeconds allows governance
freeze
  - problem : If you submit an agenda with an extremely large value, you will submit an agenda that cannot be executed.
  - Personal opinion: I don't think it's a problem, so I don't think it needs to be fixed.

## Front Test

[[Sample DAO Community Version Front Test]] 

## Set schedule

- Deploy
  - DAOCommittee_V2.sol
  - CandidateAddOnFactory.sol
- Create Agenda
  - set candidateAddOnFactoryProxy upgradeTo CandidateAddOnFactoryAddr
  - set daoCommitteeProxy upgradeTo2 DAOCommittee_V2Addr
- Next Tuesday without Kevin