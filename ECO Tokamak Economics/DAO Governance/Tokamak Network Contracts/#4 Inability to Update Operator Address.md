***—> 모든 Candidate가 Layer 2라는 가정하에 설계된 컨트랙트였기 때문에 이를 고려하지 않고 만들어졌다.***

(plasma-evm) Layer 2 Candidate의 key 값은 Layer2 contract address를 사용하지만, Candidate의 key 값은 operator 주소를 사용한다. Candidate의 operator 주소는 변경 가능해야 하지만, operator 주소를 변경하면 key 값도 함께 변경되는 문제가 발생한다. 이를 방지하기 위해 [changeOperator 함수](https://github.com/tokamak-network/ton-staking-v2/blob/a4813da3d461d7d2bffe8c59ef64fd73061e725b/contracts/dao/Candidate.sol#L165-L167)를 비활성화했으며, 처음 create를 생성한 msg.sender가 항상 operator로 활동하도록 구현했다.

하지만 다음과 같은 상황에서는 operator 주소 변경이 필요하다. 첫째, operator의 개인키 분실이나 보안 사고가 발생한 경우. 둘째, operator가 개인이 아닌 기업이나 팀이어서 EOA가 아닌 멀티시그 지갑으로 이전해야 하는 경우. 이러한 상황에서 operator 주소를 변경해야 하지만, 현재 컨트랙트는 이를 막고 있다. 설령 수정하더라도 key 값이 변경되기 때문에 문제가 발생한다.