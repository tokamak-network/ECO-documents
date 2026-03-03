**index**

### deploy-contracts

`$ trh-sdk deploy-contracts --network testnet --stack thanos`

> `$ trh-sdk deploy-contracts`를 하면 `$ trh-sdk verify-register-candidate`도 자동 실행된다. 즉 L1 컨트랙트 배포와 함께 candidate 등록이 이루어진다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c18a18d8-8941-4f4c-8d30-b4b4e9ad0855/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCJLFEK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkVTNDiImN7b%2BAsuMqe2DG%2FtmrfUgLYDHlAr7GqKmJGgIgeBtLaiEd0V0HB09R%2FkWwzWTzFhjSp4Skhoimx64gS5Yq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDb%2FvaQGdBb%2FcBdu0yrcA661iMNABI3aJrDxcS%2BJ71atnVv75WKOwKK9SEjCJt3i6Hes6wR5iHswJvLcKwuKSNtq1pLYMiyLxO7Jm9cw5BXa%2FdMMt1Sm8tfFlCLZ6KJ2MBWkmRRt%2BQIJFdTYWR0bNAs196i6RaderYdMOHuKyydBz1RmJtTIIKc%2FD4GMaOb2R9PVWeoR6FeOJuVjAhLobFsNNg57ZwEcTbfLYgIE0osGm4PKOEhiSRDqAwRc%2F5GcbOl1iufo69Xf2nVu4O4lsNgCkGF3RgYfCcK9zlGzVJzXoa3JZz05M2tfAmKgioiTh7EKRdl7jX2YIlinGQpGFtrxXBeC1vcFyGJgEzArp9m%2BvApZCl3P872WdtsfdOn8ro3KL8rc6%2B5BPt1ETXipjcice8rTAeW5c%2BdX7NzBeoY5JJYnZIJ5jOvNsidiYFXnL%2Ba5s4ufznAJ6g4Nk7iAoBwsv4NLmbkRjn5ceWLvTZTo1O%2BKsW8KCyvzAQJMDQb%2Fc87WTa52JHdfV9uaVnlBlqMsAZSr1MdpUk6MBWnTXQuc5gu8E1apXVn9uI1U2jexf3l8AcjSnmkGFzlTS%2FyU9BYMO4UXldAEbYJK6yOVcNeQ18dIXQJrcl2qDhGvSGJ6LbJeQgCoYqxos%2BiKMOuZ28wGOqUBp9yzfGh9Y6gWxXfh0%2FgbMFn%2BznuRpv5OJJUZb7AnlRMpZzSHbcKy6YiboVJrvXhjMMNSpXPqoqUW%2FIhCtBju7fskZB5E4iU8YYOWUc43wnWJifGL%2Bf9vUX1VkogHuRKfirChyEoUVW9XykZdqeHeFINtcRzmq1E%2BDJhDwQKhYbBqEj4lqqUGrF6vB%2F31QhsRlnfh5GH8KTVGYk96MMbzptAI5mIz&X-Amz-Signature=efc4c677048e4d2c94d64273923094940fb590184518be42caf9f838fde063cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

배포가 진행되면 여러 스마트 컨트랙트들이 L1에 배포되고 그 주소들이 

`{deploymentPath}/tokamak-thanos/packages/tokamak/contracts-bedrock/deployments/{l1-chain-id}-deploy.json` 파일에 저장된다.

저장되는 컨트랙트(types.Contracts)는 아래와 같다:

```json
{
  "SystemConfigProxy": "0xABC123...",      // 👈 the L2’s unique identifier
  "ProxyAdmin": "0xDEF456...",
  "SystemOwnerSafe": "0x789GHI...",
  "OptimismPortalProxy": "0x111JKL...",
  "L1StandardBridgeProxy": "0x222MNO...",
  "L1CrossDomainMessengerProxy": "0x333PQR...",
  // ... a total of 39 contract addresses
}

```

- **SystemConfigProxy**: L2의 시스템 설정 관리를 하는 컨트랙트로 L2 식별자로 사용된다.
> **Optimism에는 Proxy가 아닌 SystemConfig 그대로 사용하는데 thanos는 Proxy 컨트랙트를 사용한다.**
> ![](images/7afce986fbac.png)
- **ProxyAdmin**: 프록시 컨트랙트 관리자 역할을 하는 컨트랙트이다.
- **SystemOwnerSafe**: L2 소유권을 관리하는 컨트랙트(SafeWallet)이다.
- …

### deploy

`$ trh-sdk deploy`

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8020def5-7a2e-425d-9b55-7da582eef458/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCJLFEK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkVTNDiImN7b%2BAsuMqe2DG%2FtmrfUgLYDHlAr7GqKmJGgIgeBtLaiEd0V0HB09R%2FkWwzWTzFhjSp4Skhoimx64gS5Yq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDb%2FvaQGdBb%2FcBdu0yrcA661iMNABI3aJrDxcS%2BJ71atnVv75WKOwKK9SEjCJt3i6Hes6wR5iHswJvLcKwuKSNtq1pLYMiyLxO7Jm9cw5BXa%2FdMMt1Sm8tfFlCLZ6KJ2MBWkmRRt%2BQIJFdTYWR0bNAs196i6RaderYdMOHuKyydBz1RmJtTIIKc%2FD4GMaOb2R9PVWeoR6FeOJuVjAhLobFsNNg57ZwEcTbfLYgIE0osGm4PKOEhiSRDqAwRc%2F5GcbOl1iufo69Xf2nVu4O4lsNgCkGF3RgYfCcK9zlGzVJzXoa3JZz05M2tfAmKgioiTh7EKRdl7jX2YIlinGQpGFtrxXBeC1vcFyGJgEzArp9m%2BvApZCl3P872WdtsfdOn8ro3KL8rc6%2B5BPt1ETXipjcice8rTAeW5c%2BdX7NzBeoY5JJYnZIJ5jOvNsidiYFXnL%2Ba5s4ufznAJ6g4Nk7iAoBwsv4NLmbkRjn5ceWLvTZTo1O%2BKsW8KCyvzAQJMDQb%2Fc87WTa52JHdfV9uaVnlBlqMsAZSr1MdpUk6MBWnTXQuc5gu8E1apXVn9uI1U2jexf3l8AcjSnmkGFzlTS%2FyU9BYMO4UXldAEbYJK6yOVcNeQ18dIXQJrcl2qDhGvSGJ6LbJeQgCoYqxos%2BiKMOuZ28wGOqUBp9yzfGh9Y6gWxXfh0%2FgbMFn%2BznuRpv5OJJUZb7AnlRMpZzSHbcKy6YiboVJrvXhjMMNSpXPqoqUW%2FIhCtBju7fskZB5E4iU8YYOWUc43wnWJifGL%2Bf9vUX1VkogHuRKfirChyEoUVW9XykZdqeHeFINtcRzmq1E%2BDJhDwQKhYbBqEj4lqqUGrF6vB%2F31QhsRlnfh5GH8KTVGYk96MMbzptAI5mIz&X-Amz-Signature=61023ca196e7e7bd0dd8c5a60ca725f813bac9b9776ab9a6094cf1e19a62b9dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### verifyRegisterCandidate

`$ trh-sdk verify-register-candidate` — 

> **Candidate를 등록하기 위해 아래의 메타데이터를 사용한다.**
> ![](images/9021605d2dff.png)
> 
> - **Amount: 예치할 톤의 수량이다.**
> - **UseTon: TON or WTON TON만 사용한다.**
> - **Memo: CandidateAddOn을 등록할 때 사용된다.**
> - **NameInfo: RollupConfig에 등록될 때 사용되고 Rollup의 이름으로 사용된다.**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7503307f-7363-4ab9-82a4-f9f7905b6be2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCJLFEK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkVTNDiImN7b%2BAsuMqe2DG%2FtmrfUgLYDHlAr7GqKmJGgIgeBtLaiEd0V0HB09R%2FkWwzWTzFhjSp4Skhoimx64gS5Yq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDb%2FvaQGdBb%2FcBdu0yrcA661iMNABI3aJrDxcS%2BJ71atnVv75WKOwKK9SEjCJt3i6Hes6wR5iHswJvLcKwuKSNtq1pLYMiyLxO7Jm9cw5BXa%2FdMMt1Sm8tfFlCLZ6KJ2MBWkmRRt%2BQIJFdTYWR0bNAs196i6RaderYdMOHuKyydBz1RmJtTIIKc%2FD4GMaOb2R9PVWeoR6FeOJuVjAhLobFsNNg57ZwEcTbfLYgIE0osGm4PKOEhiSRDqAwRc%2F5GcbOl1iufo69Xf2nVu4O4lsNgCkGF3RgYfCcK9zlGzVJzXoa3JZz05M2tfAmKgioiTh7EKRdl7jX2YIlinGQpGFtrxXBeC1vcFyGJgEzArp9m%2BvApZCl3P872WdtsfdOn8ro3KL8rc6%2B5BPt1ETXipjcice8rTAeW5c%2BdX7NzBeoY5JJYnZIJ5jOvNsidiYFXnL%2Ba5s4ufznAJ6g4Nk7iAoBwsv4NLmbkRjn5ceWLvTZTo1O%2BKsW8KCyvzAQJMDQb%2Fc87WTa52JHdfV9uaVnlBlqMsAZSr1MdpUk6MBWnTXQuc5gu8E1apXVn9uI1U2jexf3l8AcjSnmkGFzlTS%2FyU9BYMO4UXldAEbYJK6yOVcNeQ18dIXQJrcl2qDhGvSGJ6LbJeQgCoYqxos%2BiKMOuZ28wGOqUBp9yzfGh9Y6gWxXfh0%2FgbMFn%2BznuRpv5OJJUZb7AnlRMpZzSHbcKy6YiboVJrvXhjMMNSpXPqoqUW%2FIhCtBju7fskZB5E4iU8YYOWUc43wnWJifGL%2Bf9vUX1VkogHuRKfirChyEoUVW9XykZdqeHeFINtcRzmq1E%2BDJhDwQKhYbBqEj4lqqUGrF6vB%2F31QhsRlnfh5GH8KTVGYk96MMbzptAI5mIz&X-Amz-Signature=4020a0dc549c714d102b8317d127cea01f0fe1d4b74eb5b330e356498826a062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **verifyRegisterCandidate 과정에서 2개의 컨트랙트가 사용된다: ****[[L1ContractVerification]]**** 컨트랙트와 ****[[L1BridgeRegistry]]****이다.**

1. ReadDeployementConfigFromJSONFile 함수를 호출해서 L1 배포 컨트랙트 정보를 읽는다.
![](images/f943c649f839.png)
1. L2 식별자를 추출한다.
```go
systemConfigProxy := contracts.SystemConfigProxy
```
1. SystemConfigProxy가 L1BridgeRegistryContract에 등록되어 있는지 확인한다.
```go
mapping(address systemConfig => uint8 rollupType) public rollupTypes;

// rollupType == 0 → not yet registered
// rollupType != 0 → registered
```
1. 해당 정보를 RollupConfig로 등록한다.
```go
txVerifyAndRegisterConfig, err := l1VerificationContract.VerifyAndRegisterRollupConfig(
    auth,
    ethCommon.HexToAddress(systemConfigProxy),
    ethCommon.HexToAddress(proxyAdmin),  
    ethCommon.HexToAddress(safeWalletAddress),
    registerCandidate.NameInfo,
)
```
1. 예치할 TON을 approve하고 RegisterCandidateAddOn 함수를 호출하여 CandidateAddOn 등록을 완료한다. 
```go
txRegisterCandidate, err := l2ManagerContract.RegisterCandidateAddOn(
    auth,
    ethCommon.HexToAddress(systemConfigProxy),  // ← 다시 L2 식별자 사용!
    amountBigInt,                                // ← 1000.1 TON
    registerCandidate.UseTon,
    registerCandidate.Memo,
)
```
1. 등록 정보를 `{deploymentPath}/settings.json` 파일에 저장한다.
```go
t.deployConfig.StakingInfo = &types.StakingInfo{
    IsCandidate:         true,
    StakingAmount:       1000.1,
    RollupConfigAddress: "0xABC123...",  // SystemConfigProxy
    CandidateName:       "MyRollup",
    CandidateMemo:       "My awesome L2 rollup",
    RegistrationTime:    "2025-11-28 14:00:00 KST",
    RegistrationTxHash:  "0x...",
    CandidateAddress:    "0x...",  // 새로 생성된 CandidateAddOn 주소
}
```