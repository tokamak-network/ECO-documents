59084b60-5b72-4674-904e-107aada970c3 

## DAO Contract 구성도

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/42a29018-dc75-4208-ae06-57a693db61d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TREL56TD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoCIURF7ZM8FmZGT1FzjwBBG0VEggBfdRDh%2BK2kKxyVwIhAIytrnhELvLdYW65dQjYe0PWddECezaCMSdbRzqQutt%2BKv8DCHQQABoMNjM3NDIzMTgzODA1Igx7HT8xq7C8tm6byDUq3AMaB2UiplNdj07ESYyBh2XH0YZNV4FRyqs5Z96eyoWtcnoJl5N6twts42%2BVaTeC0kwVI6dzrgQafraqx3RXzsqXzPZYCdM4FTb1sRag9a2VKiohQxV5yFH8vJLlTrySITgM31F7id%2FhBoOadGJWuSMizTkmqq3rRDNukNE80dAgn5M80O0IYA0u%2FiL4Vm6Uo0VhpwEQnXAnv1wGZ9H%2FRW61uw8VGkXqMCMWNf%2FGwPBRHbfYxsXTPL%2BdHAtGdfQ2TL6lzSULXH%2B5uQmZJNDW8ffZzTacm1CGfDfpyamkfTY4ciVJa6Iy%2BNH8fBs6G1SiQyTx0KWYNvW4gAqrePv7%2F54h5JdJyLU0P8QEs7R%2F2BrGkXPwzspkCMstzYLOQK7%2BDnGPiwhPqzW55ACKVC7W1ku1p9VCYda888EEv65ocTrFcsqLiJVDP6dUHkmpk77lzS40OwtXY%2Bk8wGrDMuhBR6HvVyHMfvdDGN%2FWIboXt8TWd1xZkmN8Qy%2B8P9CFbAbaXlMAxetdzo1M6mTifyBtbUlrtpMxtmUgzLWjcOnv5KojdpLFd9RUE%2B9yoeAR6gLP6xfuUxZwjA3NRfPQFp79FgiPYejzybUeSdHfnQVWAdERE%2FwLiyeZDGlTdlkQuzCP8dnMBjqkAYNAoNzd9%2FufrMTlinOjqHdLPt%2FQI0bc1pveiGR4bX5HLezkf1uyXIe4SSEzgO98YNpCT6d79sckWex%2FdF0%2BFSQntr52JwZdVsci%2B9EfsqDYrWcDgNe02QZPGiIqqH5YrV16oclutZFMpf9wNHyuCXNPHf689gW90Rb7ceJ0S4I3QgUOBayv3YALTsotDUCyVsqfhtUdleO9hp8vnwuJzxVlcpZC&X-Amz-Signature=5792e313f7bfa9d30c8ae5a1fb005f69238989694c3c427b4a81cc761b50b055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

DAOCommittee에는 Candidate와 Member들이 있다.

Candidate는 Member가 될 수 있는 후보자들이고 Member는 그 후보자들중 대표해서 의결권이 있다.

Candidate는 2가지 종류가 있는데 userAddress로 등록하는 Candidate와 Layer2Address를 등록하는 Candidate가 존재한다.

userAddress로 등록하게 되면 유저는 후보자와 동시에 CandidateContract를 배정받습니다.

candidateContract는 registry에서 layer2로 Address가 등록됩니다.

operator도 layer2Address로 등록가능합니다.
먼저 layer2 Contract을 operator로 배포하고 seigManager를 등록합니다.
그후 registry에서 registerAndDeployCoinage를 실행합니다.
committeeContract에서 registerLayer2Candidate을 실행해서 committe에 Layer2를 candidate로 등록합니다.


중요 포인트

1. TON을 많이 staking한 곳에서 Member가 되며 이는 더많이 가진사람이 신청하여서 언제든 더많이 가지고 있는 것이 확인되면 언제든 변경가능하다.
1. 투표는 과반이상이 찬성하여야지 아젠다가 실행되며 동률인 경우에도 아젠다는 실행되지 않는다.
1. 아젠다를 만들때 드는 비용은 100TON(agendaFee)이며 이는 변경가능하다.
1. 현재는 candidate를 등록할때 contract가 생성된다 → 많은 gasFee소모..
1. 시퀀서의 담보금과 오퍼레이터의 담보금은 다르다
1. 오퍼레이터가 수수료 설정이 가능하다. 
1. 오퍼레이터는 자신이 지원하는 레이어2를 지정해야한다
1. 오퍼레이터는 최소 스테이킹 금액이 필요하다
1. 시퀀서의 최소 담보금액은 추후 TVL에 따라서 변경될 수 있다
1. 시퀀서는 최소 담보금 이상은 뺄 수 있다
1. 시퀀서는 L2를 만들고 DAO쪽에 시퀀서로 등록하면서 TON을 예치하여야한다.

Candidate는 Factory에서 언제든 생성가능

- Candidate(초기 생성시 candidate,layer2,name,committee,seigManager를 입력) - candidate, committee, seigManager는 미리 주소를 알고 있어야한다. (committee는 DAOcommittee) (candidate는 Reward받는 주소)
  - setSeigManager → 시그매니저 address 설정 (Owner만 가능)
  - setCommittee → committee address 설정 (Owner만 가능)
  - setMemo → 메모 (Owner만 가능)
  - updateSeigniorage → seigManager.updateSeigniorage()를 실행 (누구나가능)
  - changeMember → DAOcommittee의 memberIndex를 변경함 (Candidate만 가능)
  - retireMember → DAOcommittee의 retireMember 실행 (Candidate만 가능)
  - castVote → DAOcommittee의 castVote를 실행 (Candidate만 가능)
  - claimActivityReward → DAOcommittee의 claimActivityReward를 실행 (Candidate만 가능)
  - isCandidateContract → true만 반환 (누구나 가능)
  - operator → candidate 반환 (누구나 가능)
  - isLayer2 → true 반환 (누구나 가능)
  - currentFork → 1만 반환 (누구나 가능)
  - lastEpoch → 1만 반환 (누구나 가능)
  - changeOperator → ? 아무것도 반환하지 않음 (누구나 가능)
  - totalStaked → coinage의 totalSupply 반환 (누구나 가능)
  - stakedOf → coinage의 balanceOf(_account) 반환 (누구나 가능)
- DAOCommitteeProxy ( constructor[ton, impl, seigManager, layer2Registry, agendaManager, candidateFactory, daovault ] ) - DAOCommittee가 logic으로 쓰임 
- DAOCommittee
  - setSeigManager - seigManager 변경 (Owner만 가능)
  - setCandidatesSeigManager - candidateContract의 setSeigManager를 변경 (Owner만 가능) (Candidates를 배열로 받음 → 하나의 DAOCommittee에 여러개의 Candidate가 있음)
  - setCandidatesCommittee - candidateContract의 setCommittee를 변경 (Owner만 가능)
  - setDaoVault - daoVault 주소 변경 (Owner만 가능)
  - setLayer2Registry - Layer2Registry주소를 변경 (Owner만 가능)
  - setAgendaManager - agendaManager 주소 변경 (Owner만 가능)
  - setCandidateFactory - candidateFactory 주소 변경 (Owner만 가능)
  - setTon - TON 주소 변경 (Owner만 가능)
  - setActivityRewardPerSecond - activityRewardPerSecond 값 변경 (Owner만 가능)
  - increaseMaxMember - 멤버수를 늘림? (Owner만 가능)
  - decreaseMaxMember - 멤버수를 줄임 (Owner만 가능)
  - createCandidate - candidateFactory에서 candidate를 만듬 (누구나 가능)
  - registerLayer2Candidate - Layer2 Contract 주소를 Candidate로 등록함 (operator가 등록함) (candidateFactory에서 Layer2candidate를 만듬) (누구나 가능)
  - registerLayer2CandidateByOwner - Owner가 operator대신 Layer2를 candidate로 등록시켜줌 (Owner만 가능)
  - changeMember - 변경을 위해서는 현재의 candidate보다 더 많은 totalStaked의 양이 있어야한다. (candidate Contract에서 호출 가능) (**이 호출이 존재하는 이유가 이해되지않습니다.**)
  - retireMember - candidate를 DAO에서 초기화 시킴 없앰 (candidate Contract에서 호출 가능 (왜 changeMember와 modify를 다르게 썻을까..?) )
  - setMemoOnCandidate - candidate를 이용해 candidateContract를 가지고옴 setMemoOnCandidateContract를 콜하여서 memo를 수정함 (누구나 호출가능)
  - setMemoOnCandidateContract - candidateContract에서 setMemo를 콜함 (누구나 호출가능)
  - setQuorum - quorum 값을 변경합니다. 이값은 maxMember와 maxMember/2 사이의 값이여야합니다.
  - setCreateAgendaFees - agendaFee를 설정할 수 있음, Fee는 TON으로 지불한다. (Owner만 실행가능) (agendaManager에서 호출)
  - setMinimumNoticePeriodSeconds - agendaManager에서 호출, 최소 notice기간? (Owner만 실행 가능)
  - setMinimumVotingPeriodSeconds - agendaManager에서 호출, 최소 voting 기간? (Owner만 실행 가능)
  - setExecutingPeriodSeconds - agendaManager에서 호출, 실행기간? (Owner만 실행 가능)
  - castVote - agendaManager에서 호출, agenda에 투표하는 것 (누구나 실행가능)
  - endAgendaVoting - 해당 Agenda에 대한 투표를 끝냄 (누구나 실행가능)
  - executeAgenda - 수락된 agenda 실행 (누구나 실행가능)
  - setAgendaStatus - status, result를 세팅함 (Owner만 실행가능)
  - updateSeigniorages - candidate들의 시뇨리지를 update 시킴 (누구나 실행가능)
  - claimActivityReward - daoVault에서 TON을 claim한다 (누구나 실행가능하지만 candidate만 실행했을때 효과가 있다)
  - fillMemberSlot - 멤버의 길이에서 maxMember만큼 address(0)을 넣는다 (internal)
  - payCreatingAgendaFee - agendaManager에서 fee를 계산해서 fee를 burn시킨다 (internal) (아젠다를 만들때 Fee를 지불하게한다.)
  - _createAgenda - agendaManager에서 agenda를 생성함 (internal) (OnApprove실행)
  - isCandidate - candidate주소를 이용해 candidateContract주소를 가져오고 그 주소가 유효한지 체크함
  - totalSupplyOnCandidate - candidate를 받아서 totalSupplyOnCandidateContract를 리턴함
  - totalSupplyOnCandidateContract - candidateContract를 입력받아서 해당 candidateContract의 totalStaked를 리턴함
  - balanceOfOnCandidateContract - candidateContract의 해당 addrss가 얼만큼 stake한지 리턴함
  - getClaimableActivityReward - period에 activityRewardPerSecond을 곱하여 얼만큼의 reward가 쌓였는지 리턴함
- DAOAgendaManager
  - minimumNoticePeriodSeconds = 16days → agenda에 대한 최소 notice기간 16일
  - minimumVotingPeriodSeconds = 2days → agenda에 대한 최소 voting기간 2일
  - executingPeriodSeconds = 7days → agenda의 votingEndTimestamp에서 executingPeriodSeconds을 더하여 agenda.executableLimitTimestamp 값이 된다.
  - createAgendaFees = 100 TON → agenda를 만들때 드는 fee 비용
  - getStatus(uint256 _status) - Lib의 AgendaStatus를 반환
  - setCommittee - committeeProxy를 지정
  - setCreateAgendaFees - 아젠다 생성 피 설정
  - setMinimumNoticePeriodSeconds - 최소 notice기간 값 변경
  - setExecutingPeriodSeconds - 실행기간 값 변경
  - setMinimumVotingPeriodSeconds - 최소 voting기간 값 변경
  - newAgenda - 아젠다를 새로 만듬
  - castVote - 아젠다에 대한 투표를 함
  - setExecutedAgenda - 아젠다를 실행한 것으로 상태 변경
  - setResult - 아젠다의 result를 변경
  - setStatus - 아젠다의 status상태를 변경
  - endAgendaVoting - 투표상태의 아젠다를 끝내는 상태로 변경
  - isVoter - voterInfos의 isVoter 상태를 리턴
  - hasVoted - voterInfos의 hasVoted 상태를 리턴 (isVoter, hasVoted 변수는 다르게 candidate, user 이렇게 썻지만 같은 느낌임)
  - getVoteStatus - candidate의 hasVoted와 vote를 리턴
  - getAgendaNoticeEndTimeSeconds - agenda의 noticeEndTimestamp를 리턴합니다.