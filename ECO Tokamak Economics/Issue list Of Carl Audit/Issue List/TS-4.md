TS-4 - Multiple init possible (CandidateAddOnV1_1)

ID Type Severity Location Status

TS-4 Logical Issue Medium

contracts/dao/

CandidateAddOnV1_1.sol#L41 Pending

**Description**

CandidateAddOnV1_1 컨트랙트는 owner에 의해 initialize 함수가 여러번 호출될 수 있습니다. 이는 컨트

랙트의 주요 상태 변수인 candidate, isLayer2Candidate, committee, seigManager, memo, ton,

wton 들을 새로운 값으로 변경할 수 있는 가능성이 있습니다.

**Recommendation**

이를 방지하기 위해 initialize 함수에서 초기화하는 상태 변수들의 값이 zero value인지 확인합니다.

---

## Feedback

[Link](https://github.com/tokamak-network/ton-staking-v2/commit/b8435ae3bc08bdc9c1b715843e057ba84d25008d)