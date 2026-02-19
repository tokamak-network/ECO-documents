# **TS-1 - Storage layout conflict (DAOCommitteeProxy2) **

| ID | Type | Severity | Location |
| --- | --- | --- | --- |
| TS-1 | Logical Issue | Critical | contracts/proxy/DAOCommitteeProxy2.sol#L13 |

Description 

메인넷에 배포되어있는 DAOCommitteeProxy 컨트랙트(0xDD9f0cCc044B0781289Ee318e5971b0139602C26)는 DAOCommittee_V1 컨트랙트(0xdf2ecda32970db7db3428fc12bc1697098418815)를 로직 컨트랙트로 사용합니다. test/layer2/units/6.dao-staking-v2.5.mainnet.test.ts 테스트 파일에 따르면, 컨트랙트 업그래이드는 아래와 같이 진행됩니다.   

- 기존 DAOCommitteeProxy 컨트랙트의 로직 컨트랙트를 DAOCommitteeProxy2 컨트랙트로 업그래이드   

- DAOCommitteeProxy2의 로직 컨트랙트를 두 개의 새로운 컨트랙트들(DAOCommittee_V1, DAOCommitteeOwner)로 업그래이드 따라서 DAOCommitteeProxy 컨트랙트가 실행하는 함수는 DAOCommitteeProxy -> DAOCommitteeProxy2 -> DAOCommittee_V1 or DAOCommitteeOwner 순으로 실행됩니다.   

- DAOCommitteeProxy: _implementation(Slot#14) 변수에서 로직 컨트랙트 주소를 불러옵니다.   - DAOCommitteeProxy2: msg.sig에 따라 proxyImplementation(Slot#14) 변수 혹은 selectorImplementation(Slot#16) 변수에서 로직 컨트랙트 주소를 불러옵니다. 하지만, 기존 컨트랙트 (DAOCommitteeProxy, DAOCommittee_V1)와 새로운 컨트랙트 (DAOCommitteeProxy2, DAOCommitteeOwner, DAOCommittee_V1)는 Slot#14 부터 Storage layout이 충돌합니다.  

 1. 기존 _implementation, pauseProxy 는 신규 proxyImplementation 와 충돌합니다.   

 2. 신규 _implementation는 기존 _implementation과 다른 Slot을 사용하기 때문에 해당 변수를 실행하는 컨트랙트에 따라 다른 값을 반환합니다. 

 3. 신규 pauseProxy는 기존 pauseProxy과 다른 Slot을 사용하기 때문에 해당 변수를 실행하는 컨트랙트에 따라 다른 값을 반환합니다.   

 4. 기존 _oldCandidateInfos 는 신규 aliveImplementation 와 충돌합니다.   

 5. 신규 _oldCandidateInfos 는 Slot#18에 위치하기에 기존 상태 변수에 접근할 수 없습니다.   

 6. 기존 wton 은 selectorImplementation 와 충돌합니다.   

 7. 신규 wton 은 Slot#19에 위치하기에 업그래이드 직후 zero address를 반환합니다. 

Recommendation

기존 DAOCommitteeProxy, 기존 DAOCommittee_V1, 새 DAOCommittee_V1, DAOCommitteeProxy2, DAOCommitteeOwner 컨트랙트들의 storage layout을 변경

## Feedback

Commit: [1462678133ab422114821c0feb194a8eafc5b5b4](https://github.com/tokamak-network/ton-staking-v2/commit/1462678133ab422114821c0feb194a8eafc5b5b4)