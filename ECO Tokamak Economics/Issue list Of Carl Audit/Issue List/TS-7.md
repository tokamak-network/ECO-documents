# **TS-7 - Multiple SLOAD (getSelectorImplementation2) **

| ID | Type | Severity | Location |
| --- | --- | --- | --- |
| TS-7 | Gas Optimization | Minor | contracts/proxy/DAOCommitteeProxy2.sol#L96-L99  |

**Description**

selectorImplementation[_selector] 를 여러번 실행해 동일한 상태 변수를 각 조건문을 확인할 때 마다 읽고

있습니다. 최악의 경우 3번의 SLOAD를 실행하기에 2개의 SLOAD와 추가적인 연산에 불필요한 가스를 사용

하고 있습니다.

**Recommendation**

selectorImplementation[_selector]를 로컬 변수에 저장하면 메모리를 사용할 수 있어 가스 소비를 줄일 수

있습니다.

## Feedback

Minor로 올려주셨는데 가스비를 줄이는 방향이라 Informational인 것 같습니다.

가스 소비를 줄이는 방향이라 Minor → Informational로 변경해야할 것 같습니다.

Commit: [6600a0849106a1d141fb6da207ba2a296fa0bbba](https://github.com/tokamak-network/ton-staking-v2/commit/6600a0849106a1d141fb6da207ba2a296fa0bbba)