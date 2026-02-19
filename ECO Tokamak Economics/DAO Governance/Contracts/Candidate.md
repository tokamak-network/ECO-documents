**index**

## plasma-evm-contracts

### (legacy) [Layer 2](https://github.com/tokamak-network/plasma-evm-contracts/blob/master/contracts/Layer2.sol)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7f2d6070-4b86-4176-a7d2-6cc5ffce121e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVPCSML3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfxVe2CP6A0r5ltUMJLTLyvzyVf2FdvhEK4AGZcih1mwIhAKw6L8N%2F6NeRk%2BvDaIcirjvUqTb4tdXvqFVFQgL8ZgebKv8DCHQQABoMNjM3NDIzMTgzODA1IgwEuGJFefFnreK2wjEq3AM8LH11dV8%2B4KJ1ZXbahYVKwUhEXt6zT86YQMdAMpwOzCQLXXxQLRjeRsJxbOEAbDHUPZoZUKueVexIBlMSTfN4rhL5NYrJrhGvwvQ3SeUyC5mJgGur54RMefebefyWwkCN%2BYmaFJ7OAprXVHqKzJNqscTS%2F%2Frh3o%2F68lJlVGUdrCkg5eL%2FxVCfvIWFjXc36qPqx6clJGrdV%2BwRCK4ESHKOMuK8dZZtFgDsId2GzgdzgSqH%2BgHlIBYaXyU2Fy4P3DBedOcpFew%2F3c8mp%2FWMGPys0tQ3V3jsKtChgSRcvsdFB%2FEQ3nCw9OIFMvhiR4jOF0UvxZ9NWbUzH6%2FWEKYCfdMc7433nxPNzYuhRO%2F0%2FUixFSCuh00%2FNotRizS%2FKVl17hMNcfE435%2BN7jKO5Q5KbaMrN4ylsj5pAGUi6zkfO6KStnhxx307T%2FX08FSfHB3dP4c%2B8LyFw0QfYjgRBvjZ8k9PG1tNfPKG4iyG55MdC7PCX7KmVNbeBBdzqU9b686qYJsnUJ%2FrUIZJzjbXk%2FCTjTJOZUcLEIRVGWV7M94ikNEe4ndUDnnPQ%2FHFU7SRnUjZXhhbakSoGS4R4Dhr44b0v2dRYWw0Gk65NPTeya4B1p5lzbuWF9n8K8YFOk6tFTCw8dnMBjqkAecQE6foYOFDeLkbTpot5UZITDo37AKedP%2FgCyIooQko7wOHaWH5NouV4Mqm%2FRMzjcJWY%2BztU9QUl8meW0rVsiSoiORL2l%2BE0quU%2BGiuq7OgzgipRvP93UpkBZu177mbEUffaZ2q0ikGDLEb7Qi1k5E4DyoPch7shmRSOfspXb0l0zhnOaDvm9iLwW6Yst9MTMgd%2BpgbOmPeTGV9l5U%2B2rr9DkvW&X-Amz-Signature=0a002db04d31bf06c5bec6ca35625ba4205b0815b5015d45ac9056d518218acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[*plasma-evm-contracts의 Layer2 컨트랙트*](/2b9d96a400a38059be32ef43551d1eec)*를 배포한다. 배포자(deployer, msg.sender)는 operator가 된다. Layer2Registry 컨트랙트의 Owner 또는 Layer2 컨트랙트의 operator는 해당 layer2를 Layer2Registry에 등록하고 Coinage를 배포(**`registerAndDeployCoinage`**)할 수 있다.*

> ***Layer2 컨트랙트는 CandidateProxy 컨트랙트로 모두 migration—***a8add4af-a99b-4407-b40d-d429fa080bec***, ***9a1e3e63-03a4-4daa-9cdb-41874a93e433***—되었다. Candidate를 생성하기 위해서는 기존의 DAOCommitteeV1_1.sol 컨트랙트의 함수를 호출한다.***
> ![](images/64495900fd8c.png)

[https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOCommittee.sol](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOCommittee.sol)

- createCandidate
- registerLayer2Candidate
> 이전의 Layer 2와 현재의 Layer 2는 다르다. 이전의 Layer 2를 배포하고 등록하는 함수는 registerLayer2Candidate 함수를 호출하는 반면 현재의 Layer 2를 배포하고 Candidate로 등록하는 함수는 createCandidateAddOn 함수를 호출해서 CandidateAddOn을 생성한다.

> registerCandidateAddOn 현재의 layer 2를 배포하고 등록하는 함수이다.

## Candidate

**createCandidate**

누구나 이 함수를 호출해서 Candidate가 될 수 있다.

![](images/53113a36dcca.png)

```solidity
function createCandidate(
    string calldata _memo
) external validSeigManager validLayer2Registry validCommitteeL2Factory {
    address _operator = msg.sender;
    require(!isExistCandidate(_operator), 'DAOCommittee: candidate already registerd');

    ***// Candidate
    address candidateContract = candidateFactory.deploy(
        _operator,
        false,
        _memo,
        address(this),
        address(seigManager)
    );***

    require(
        candidateContract != address(0),
        'DAOCommittee: deployed candidateContract is zero'
    );

***    require(
        layer2Registry.registerAndDeployCoinage(candidateContract, address(seigManager)),
        'DAOCommittee: failed to registerAndDeployCoinage'
    );***

***    _candidateInfos[_operator] = CandidateInfo({
        candidateContract: candidateContract,
        memberJoinedTime: 0,
        indexMembers: 0,
        rewardPeriod: 0,
        claimedTimestamp: 0
    });

    candidates.push(_operator);
***
    emit CandidateContractCreated(_operator, candidateContract, _memo);
}
```

**(1) candidateFactory.deploy**

1. *`new CandidateProxy`**: CandidateProxy 컨트랙트를 새로 배포한다.*
1. *`upgradeTo`**: logic 컨트랙트를 Candidate 컨트랙트로 지정한다.*
1. *`initialize`**: CandidateProxy 상태 변수를 초기화한다.*
1. *`transferAdmin`**: CandidateProxy 컨트랙트의 admin을 DAOCommitteeProxy 컨트랙트로 지정한다. *

**(2) layer2Registry.registerAndDeployCoinage(candidateContract, address(seigManager)**

```solidity
function registerAndDeployCoinage(
    address layer2,
    address seigManager
) external override onlyMinterOrOperator(layer2) returns (bool) {
    require(_register(layer2));
    require(_deployCoinage(layer2, seigManager));
    return true;
}
```

1. *CandidateProxy 컨트랙트를 layer2로 등록한다.*
1. *새로운 Coinage 컨트랙트를 배포한다.*
> ***Coinage 컨트랙트 배포는 Layer2Registry 컨트랙트만 가능하다.***
> ```solidity
> *function deployCoinage(address layer2) external onlyRegistry returns (bool) {
>     // create new coinage token for the layer2 contract
>     if (address(_coinages[layer2]) == address(0)) {
>         address c = CoinageFactoryI(factory).deploy();
>         _lastCommitBlock[layer2] = block.number;
>         // addChallenger(layer2);
>         _coinages[layer2] = RefactorCoinageSnapshotI(c);
>         emit CoinageCreated(layer2, c);
>     }
> 
>     return true;
> }*
> ```

**(3) update state variables**

```solidity
*_candidateInfos[_operator] = CandidateInfo({
    candidateContract: candidateContract,
    memberJoinedTime: 0,
    indexMembers: 0,
    rewardPeriod: 0,
    claimedTimestamp: 0
});

candidates.push(_operator);*
```

**createCandidateOwner**

createCandidate 함수와 동일한 로직이지만, operator address가 msg.sender가 아닌 지정된 주소라는 점이 다르다.