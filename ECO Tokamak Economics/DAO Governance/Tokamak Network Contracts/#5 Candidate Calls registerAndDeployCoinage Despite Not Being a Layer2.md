***—> 모든 Candidate가 Layer 2라는 가정하에 설계된 컨트랙트였기 때문에 이를 고려하지 않고 만들어졌다.***

Candidate는 layer2가 아닌데 [registerAndDeployCoinage 함수](https://github.com/tokamak-network/ton-staking-v2/blob/a4813da3d461d7d2bffe8c59ef64fd73061e725b/contracts/dao/DAOCommittee_V1.sol#L168-L171)를 호출한다. Candidate 컨트랙트의 isLayer2는 항상 true를 반환한다.