# **TS-8 - Cannot disable functions once set (DAOCommitteeProxy2) **

| ID | Type | Severity | Location |
| --- | --- | --- | --- |
| TS-8 | Codeing Style | Minor | contracts/proxy/DAOCommitteeProxy2.sol#L64  |

**Description**

setSelectorImplementations2 함수는 _selectors에 해당하는 함수들의 로직 컨트랙트를 _imp로 설정합

니다.

컨트랙트 업그레이드 과정에서 이미 등록된 함수들을 비활성화해야 할 수도 있습니다. 등록된 함수를 다시 제거하

기 위해선 아래와 같은 트랜잭션이 실행되어야 합니다.

1. setAliveImplementation2(0x00, true)

2. setSelectorImplementations2(SELECTORS_TO_REMOVE, 0x00)

이러한 방식은 불필요한 함수를 추가로 실행해야하기 때문에 가스를 추가로 소비해야 합니다. 또한 컨트랙트가 아

닌 주소를 aliveImplementation에 등록하는 것은 해당 상태 변수의 맥락에 맞지 않아 코드의 가독성을 떨어뜨

릴 수 있습니다.

**Recommendation**

만약 setAliveImplementation2(0x00, true) 와 같은 방식을 사용해 등록된 함수를 제거하는 것이 의도된 방

식이었다면, 관련된 내용을 setSelectorImplementations2 함수와 aliveImplementation 변수의 주석에

추가하십시오.

그렇지 않다면 유연한 컨트랙트 유지보수를 위해 setSelectorImplementations2 함수의 unset 버전의 함수

를 추가하십시오

## Feedback

Commit: [061f2a2dbae3bf377446965873ff38d14b44a95d](https://github.com/tokamak-network/ton-staking-v2/commit/061f2a2dbae3bf377446965873ff38d14b44a95d)