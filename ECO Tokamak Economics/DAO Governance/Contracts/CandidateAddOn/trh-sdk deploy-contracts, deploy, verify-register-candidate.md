**index**

### deploy-contracts

`$ trh-sdk deploy-contracts --network testnet --stack thanos`

> `$ trh-sdk deploy-contracts`를 하면 `$ trh-sdk verify-register-candidate`도 자동 실행된다. 즉 L1 컨트랙트 배포와 함께 candidate 등록이 이루어진다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c18a18d8-8941-4f4c-8d30-b4b4e9ad0855/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SQ3THVX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFt8siMXz7%2FQ5iBivVX4zfi3TnSiYV8YQbRfRLCorZIAiEAqGkW6JGhEf2tOShnxjhvd5Aq4wOrFHsDPndLglUqSzwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMzxQo6P50FaLGhCoyrcAzkufxTgGjjh4G8N0cDgP6fK9agyRhqWpOo5vzdvgf5ZVYxNHhfH%2BDNoGX3JNaeHARXhobkQyL%2BJf3xvKSJlf5v5bvjMqM%2FXXPYvCBePLLhd1L7on44ueoi21DekQPOvTYl1YO%2FUMNfyLbhTKH2yZ4CZYDqNAhnS0ZabZ37q0zqOln%2F8HhdfvyhJHR8eEnWSo%2F5%2ByLygLiy7BjYtCz4unCA6xf7tnYsP%2BR58j3Dbkc%2F45cZ7Ae8L1SyTcLceD9JXzVZrzPRrwTWYEi1AuVuI9Yq0BmsSFQc2g1JkD3YFYRzWpCcStmiEUW43nOQQEvnD1Y0JwmHj4q6JzGO%2FO%2F55%2BaIwifYGSVoBwX5RpJQOeVoGctLosbY%2BcYF5i2EkKLWLHTwljIV%2BxULESuk%2Bef65ESOuyv%2Bio3SwYnSYCP4WxTthNneK%2Fr76RewcdkV2XscW3F9lcrb6oAmgjMy%2FPbQomysXKkmY4hUHCnM3El%2F%2BAdwZ6HGRzzDasOMKUrua2GbtrMfYdgdELXPxlMPsuQyqX7DVLRzktCFrn8274Dp3aqJRrPUKb93ruwqV0Cjmrl%2BrSw%2BkDF7KFY5vAssn%2FcCSYQ2I8kPzoLgbmGCHLNmeVEdhKaDF6DRBs6%2B7ruOcMJfw2cwGOqUB83T4YhQPpDeUnLXs%2F90LPrV3QbNl9JAj1BRy80%2FpqNa4ta7BtYFlDYlQB476mw2QXHG%2FDkgtlwclK9JlaLnjLm08b4pC37T7y2Hpk5e7cBQQ6QFXACFaupjEJQKcR5eF87sEp9WgIvYpuHnsJzXhHiRENkgkujLk1Gyi5Vnj7XUqogfMc2jXW8YDtZ2ilbWGzavAu57L0%2FiPoxQpKwSWxgdTdtkG&X-Amz-Signature=a3dad0c908c222f27ad01c19633c2e994d18a2b8674e08caf66fcc975924bb4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
> ![](images/f9fd1b04eb47.png)
- **ProxyAdmin**: 프록시 컨트랙트 관리자 역할을 하는 컨트랙트이다.
- **SystemOwnerSafe**: L2 소유권을 관리하는 컨트랙트(SafeWallet)이다.
- …

### deploy

`$ trh-sdk deploy`

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8020def5-7a2e-425d-9b55-7da582eef458/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SQ3THVX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFt8siMXz7%2FQ5iBivVX4zfi3TnSiYV8YQbRfRLCorZIAiEAqGkW6JGhEf2tOShnxjhvd5Aq4wOrFHsDPndLglUqSzwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMzxQo6P50FaLGhCoyrcAzkufxTgGjjh4G8N0cDgP6fK9agyRhqWpOo5vzdvgf5ZVYxNHhfH%2BDNoGX3JNaeHARXhobkQyL%2BJf3xvKSJlf5v5bvjMqM%2FXXPYvCBePLLhd1L7on44ueoi21DekQPOvTYl1YO%2FUMNfyLbhTKH2yZ4CZYDqNAhnS0ZabZ37q0zqOln%2F8HhdfvyhJHR8eEnWSo%2F5%2ByLygLiy7BjYtCz4unCA6xf7tnYsP%2BR58j3Dbkc%2F45cZ7Ae8L1SyTcLceD9JXzVZrzPRrwTWYEi1AuVuI9Yq0BmsSFQc2g1JkD3YFYRzWpCcStmiEUW43nOQQEvnD1Y0JwmHj4q6JzGO%2FO%2F55%2BaIwifYGSVoBwX5RpJQOeVoGctLosbY%2BcYF5i2EkKLWLHTwljIV%2BxULESuk%2Bef65ESOuyv%2Bio3SwYnSYCP4WxTthNneK%2Fr76RewcdkV2XscW3F9lcrb6oAmgjMy%2FPbQomysXKkmY4hUHCnM3El%2F%2BAdwZ6HGRzzDasOMKUrua2GbtrMfYdgdELXPxlMPsuQyqX7DVLRzktCFrn8274Dp3aqJRrPUKb93ruwqV0Cjmrl%2BrSw%2BkDF7KFY5vAssn%2FcCSYQ2I8kPzoLgbmGCHLNmeVEdhKaDF6DRBs6%2B7ruOcMJfw2cwGOqUB83T4YhQPpDeUnLXs%2F90LPrV3QbNl9JAj1BRy80%2FpqNa4ta7BtYFlDYlQB476mw2QXHG%2FDkgtlwclK9JlaLnjLm08b4pC37T7y2Hpk5e7cBQQ6QFXACFaupjEJQKcR5eF87sEp9WgIvYpuHnsJzXhHiRENkgkujLk1Gyi5Vnj7XUqogfMc2jXW8YDtZ2ilbWGzavAu57L0%2FiPoxQpKwSWxgdTdtkG&X-Amz-Signature=6e0e88daaa9acc6c3baf9d5a4c30f484956cb87424bc95b57d9f8dd4ed40fe8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### verifyRegisterCandidate

`$ trh-sdk verify-register-candidate` — 

> **Candidate를 등록하기 위해 아래의 메타데이터를 사용한다.**
> ![](images/477d35ca9165.png)
> 
> - **Amount: 예치할 톤의 수량이다.**
> - **UseTon: TON or WTON TON만 사용한다.**
> - **Memo: CandidateAddOn을 등록할 때 사용된다.**
> - **NameInfo: RollupConfig에 등록될 때 사용되고 Rollup의 이름으로 사용된다.**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7503307f-7363-4ab9-82a4-f9f7905b6be2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SQ3THVX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFt8siMXz7%2FQ5iBivVX4zfi3TnSiYV8YQbRfRLCorZIAiEAqGkW6JGhEf2tOShnxjhvd5Aq4wOrFHsDPndLglUqSzwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMzxQo6P50FaLGhCoyrcAzkufxTgGjjh4G8N0cDgP6fK9agyRhqWpOo5vzdvgf5ZVYxNHhfH%2BDNoGX3JNaeHARXhobkQyL%2BJf3xvKSJlf5v5bvjMqM%2FXXPYvCBePLLhd1L7on44ueoi21DekQPOvTYl1YO%2FUMNfyLbhTKH2yZ4CZYDqNAhnS0ZabZ37q0zqOln%2F8HhdfvyhJHR8eEnWSo%2F5%2ByLygLiy7BjYtCz4unCA6xf7tnYsP%2BR58j3Dbkc%2F45cZ7Ae8L1SyTcLceD9JXzVZrzPRrwTWYEi1AuVuI9Yq0BmsSFQc2g1JkD3YFYRzWpCcStmiEUW43nOQQEvnD1Y0JwmHj4q6JzGO%2FO%2F55%2BaIwifYGSVoBwX5RpJQOeVoGctLosbY%2BcYF5i2EkKLWLHTwljIV%2BxULESuk%2Bef65ESOuyv%2Bio3SwYnSYCP4WxTthNneK%2Fr76RewcdkV2XscW3F9lcrb6oAmgjMy%2FPbQomysXKkmY4hUHCnM3El%2F%2BAdwZ6HGRzzDasOMKUrua2GbtrMfYdgdELXPxlMPsuQyqX7DVLRzktCFrn8274Dp3aqJRrPUKb93ruwqV0Cjmrl%2BrSw%2BkDF7KFY5vAssn%2FcCSYQ2I8kPzoLgbmGCHLNmeVEdhKaDF6DRBs6%2B7ruOcMJfw2cwGOqUB83T4YhQPpDeUnLXs%2F90LPrV3QbNl9JAj1BRy80%2FpqNa4ta7BtYFlDYlQB476mw2QXHG%2FDkgtlwclK9JlaLnjLm08b4pC37T7y2Hpk5e7cBQQ6QFXACFaupjEJQKcR5eF87sEp9WgIvYpuHnsJzXhHiRENkgkujLk1Gyi5Vnj7XUqogfMc2jXW8YDtZ2ilbWGzavAu57L0%2FiPoxQpKwSWxgdTdtkG&X-Amz-Signature=494b9a018155bfbc2c5b043751b0d32854e0c66dc1353fceda1deda3ad7f06d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **verifyRegisterCandidate 과정에서 2개의 컨트랙트가 사용된다: ****[[L1ContractVerification]]**** 컨트랙트와 ****[[L1BridgeRegistry]]****이다.**

1. ReadDeployementConfigFromJSONFile 함수를 호출해서 L1 배포 컨트랙트 정보를 읽는다.
![](images/19a86178d1d4.png)
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