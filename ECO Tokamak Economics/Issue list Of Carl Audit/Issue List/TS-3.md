# TS-3 - Duplicate proxy pausing mechanism (DAOCommitteeProxy2)

| ID | Type | Severity | Location |
| --- | --- | --- | --- |
| TS-3 | Control Flow | Medium | contracts/proxy/DAOCommitteeProxy2.sol#L125 |

**Description**

DAOCommitteeProxy2 컨트랙트는 pauseProxy 상태 변수를 통해 해당 프록시 컨트랙트의 프록시 기능

이 정지 되었는지 구별합니다. 하지만 기존에 배포된 DAOCommitteeProxy 컨트랙트 내부에 동일한 기능 하

고 있습니다.

이는 SLOAD 를 추가로 사용해 가스 소비를 늘릴 뿐 아니라 컨트랙트 소스코드의 가독성을 해칩니다. 또한 컨트

랙트의 관리 지점이 추가되는 비효율성을 야기합니다.

**Recommendation**

1. 만약 두 개의 프록시 정지 기능을 별도로 관리하고 싶다면, DAOCommitteeProxy2는 별도의 상태 변수를

통해 정지 기능을 구현해야 합니다. 추가적인 상태변수와 함수 (예: pauseProxy2, setProxyPause2()) 를

추가하십시오.

2. 만약 프록시 정지 기능을 기존 DAOCommitteeProxy 컨트랙트에서만 사용할 것이라면,

DAOCommitteeProxy2는 컨트랙트에서는 프록시 정지 기능을 삭제하십시오.

## Feedback

가스비 효율만이 문제인 부분으로 Medium이 아닌 informational 같습니다.

Commit: [945643cc8e7666f9357e411115bdb9cd47e15940](https://github.com/tokamak-network/ton-staking-v2/commit/945643cc8e7666f9357e411115bdb9cd47e15940)