- Repo: [https://github.com/tokamak-network/ton-staking-sdk](https://github.com/tokamak-network/ton-staking-sdk)

# Versions 

- V1.0.0:  To **support simple staking v2.5**

# V 1.0.0

abi: [https://github.com/tokamak-network/ton-staking-v2/tree/ton-staking-v2/test/abi](https://github.com/tokamak-network/ton-staking-v2/tree/ton-staking-v2/test/abi)

[https://github.com/tokamak-network/ton-staking-v2/blob/deploy-5th-sepolia/test/layer2/units/12.dao-staking-v2.5.test.sepolia.test.ts](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-5th-sepolia/test/layer2/units/12.dao-staking-v2.5.test.sepolia.test.ts)

## **Features**

This library will allow you to:

### For Stakers

- Stake with TON  
  - TON.approveAndCall(WTON_ADDRESS, wei_amount, [data](https://github.com/tokamak-network/simple-staking-v2/blob/sepolia/src/actions/StakeActions.ts#L10))
- Stake with WTON
  - WTON.approveAndCall(DepositManager_Address, ray_amount, [data](https://github.com/tokamak-network/simple-staking-v2/blob/sepolia/src/actions/StakeActions.ts#L23))
- 예치한 금액의 출금요청을 합니다.
  - DepositManager.requestWithdrawal(layer2, ray_amount)
- TON으로 출금합니다.
  - DepositManager_CONTRACT.processRequests(layer2, [withdrawableLength](/18fd96a400a380dda636f3f64fc21dd1#1b6d96a400a380e4949fc7ae93954e88), true);
- WTON으로 출금합니다.
  - DepositManager_CONTRACT.processRequests(layer2, [withdrawableLength](/18fd96a400a380dda636f3f64fc21dd1#1b6d96a400a380e4949fc7ae93954e88), false);

withdrawableLength
```javascript
const numPendingRequests = await DepositManager_CONTRACT.numPendingRequests(layer2, account);
let requestIndex = await DepositManager_CONTRACT?.withdrawalRequestIndex(layer2, account);

for (const _ of range(numPendingRequests)) {
  const req = await DepositManager_CONTRACT?.withdrawalRequest(layer2, account, requestIndex);
  pendingRequests.push(req);
  requestIndex = requestIndex.add(1);
}

const withdrawableList = pendingRequests.filter(
  (req) => req.withdrawableBlockNumber.toNumber() <= blockNumber
);

withdrawableLength = withdrawableList.length;
```

## Candidate 

### Candidate 종류

- (A) Candidate
  - DAO 후보자가 되려는 목적으로 만든 일반적인 Candidate   
- (B) **Layer2Candidate**
  - 이미 SeigManager를 통해 스테이킹을 하고 있던 Layer2가 나중에  DAO 후보자가 되기위해 만든 Candidate 
- (C) CandidateAddOn 
  - TRH를 통해 Thanos L2를 만들면서, L2 운영자(시퀀서)가 시뇨리지를 받으면서, DAO 후보자가 되기 위해 만든 Candidate 

### Candidate 생성 

- (A) To create Candidate :  [doc](/1bbd96a400a380aa9b47f975110011f9#1bed96a400a380e3b9e8ce1f8d53870a)
  - **daoCommitteeContract.connect(addr1).createCandidate(memo)**
  - 오퍼레이터이름으로   1000.1 TON을 스테이킹해야, 업데이트 시뇨리지가 가능하다. 
- (B) To create **Layer2Candidate** :  [doc](/1bbd96a400a380aa9b47f975110011f9#1c0d96a400a3808bbc78e6359685c96d)
  - 오퍼레이터이름으로   1000.1 TON을 스테이킹해야, 업데이트 시뇨리지가 가능하다. 
- (C) To create CandidateAddOn : You can create a CandidateAddOn using TRH's SDK. Please refer to TRH SDK. 
  - OperatorManager 이름으로 생성하면서  1000.1 TON을 스테이킹 자동으로 함.  

### 생성된 Candidate 조회  

- DAOCommitteeProxy의 Candidate 생성 이벤트를 통해 Candidate 가 생성된 것을 인지할 수 있다. 
  - (A) Candidate 또는 (C) CandidateAddOn 가 생성될때, 트리거 되는 이벤트 
```javascript
event CandidateContractCreated(
        address indexed candidate,
        address indexed candidateContract,
        string memo
    );
```
  - (B) Layer2Candidate 가 생성될때, 트리거 되는 이벤트 
```javascript
event Layer2Registered(
        address indexed candidate,
        address indexed candidateContract,
        string memo
    );
```

### 어떤 타입의 Candidate 인지 확인하는 방법

- DAOCommitteeProxy.**privateLayer2**(layer2 address) 
  - true 이면 : (B) Layer2Candidate 타입입니다. 
  - false 인 경우, 
    - layer2.**isLayer2Candidate**() 
      - true이면 : (C) CandidateAddOn 타입입니다. 
      - false 이면 : (A) Candidate 타입입니다. 

### Change CandidateAddOn to Candidate  

CandidateAddOn으로 등록되었으나, 다오에 의해 시뇨리지 발급이 중지되어, 이제 더이상 L2시뇨리지를 주지 않아 일반 Candidate와 같은 역할만 하게 된 CandidateAddOn 

- **Layer2Manager.rollupConfigInfo(rollupConfig address) returns SeqSeigStatus**
 **리턴값에서 status 가 2가 아니면 일반 Candidate 로 인지하셔야 합니다. **

```javascript
struct SeqSeigStatus {
        uint8 status; // status for giving seigniorage ( **0: none **, 1: registered, **2: paused **)
        address operatorManager;
    }
```

## CadidateAddOn이 L2 시퀀서를 받는 레이어인지 확인하는 방법 

- Contract: Layer2Manager
- Function:
  - **layerInfo**(address layer2) external view returns (address rollupConfig, address operator)

**Layer2Manager.layerInfo(layer2 address) 함수를 이용해서, rollupConfig와 operator 주소 정보가 리턴되면. 이 layer2는 레이어2 시퀀서가 시뇨리지를 받는 레이어2이고, 리턴되는 값이 없다면 이것은 일반 DAO Candidate 라고 생각할 수 있습니다.**

위 함수가 새로 생긴함수라서, abi 를 새로 받으셔야 합니다. [https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/Layer2ManagerV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/Layer2ManagerV1_1.json)

  - **Layer2Manager.rollupConfigInfo(rollupConfig address) returns SeqSeigStatus 에서 **status=1 이야 정상적으로 시뇨리지를 받을 수 있는 상태입니다. 
  - example (thanos sepolia V2) 
    - rollupConfig :  `0x6eF61974A3CDa7BbD0a4DD0A613f56d211c8AfDC`  ←Thanos Sepolia V2
    - Layer2Manager
      - [rollupConfigInfo](https://sepolia.etherscan.io/address/0x58b4c2fef19f5cddd944aadd8dc99ccc71bfefdc#readProxyContract#F23) ( rollupConfig address ) 

```javascript

    /// rollupConfig - SeqSeigStatus
    mapping (address => SeqSeigStatus) public rollupConfigInfo;

```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/aa26cdc7-c364-48db-ae39-d111be03b39c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-24_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.40.28.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4CRKJDL%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE5E9BSkcR8qTFFNf8seGdRiYUKluDgL%2FnJcpywz9mdaAiEA4HE%2BQ3r%2FCQ%2FnlkXqnVDHLpD37cSq5ZFiCCZUEZ92STcq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDOKo62FbiXQQ4raSvCrcAwxlQNxumn6GMLs%2FshKw47o2sOpptbpBjN4BbeWrtOKdpUBvu1N%2F7LAYLhPQr0fMrh%2FtV6DuvkKRG0QuKe5CaquTQymmgOv9PfGPbLzWffK0OdXy%2FcDFijUdhvEpQ8m4%2FoZB47NAscDGaI7dN3RBBakIAkoiXy%2F8V4mHgHYJ82T5j42yZR0yrUOQEYeO6V2z5WtTZK58KLvKFlkCoSPZKmtSoGZoDcTVMhpxa9n%2Fk8CT%2FbL%2BRAlU3Nv4R4O9PbyGvRx3VrO3ewpJ7%2Fek2pBFMiB5bqAb6eip09cPV%2FE5e%2FhdoRF21Bsg97LIS53v5GqtLQi0towNZ4f4d%2BUdwPQZ6qhvBzObXFbrAJSyXTuWn0z3IBMtY2n3QTgLWEOec6%2B0KJx1FkKXRZppXznmRbzopFxYNeTYVK%2FNLaXwIq1s7kTNwwC%2BhfnXpMuDeiWW%2BWyCKcj8thOKir7Sy32NCPiWBODo0NIrol8fja0wmIbSAtFuV%2BW1M4XKGg3ArcIhj%2Fe0ZyHtftUQQXudDVZfTMzLCz7MIKRfalDu4VFu7WLJiYJOT54PGyU1IXCtpgRN2b09eT7c1PmsttSjE0Bgla8amsvdk9yFmFeCOx%2FYv0W195pt%2FLEhiP96%2BxGwUYDdMKCZ28wGOqUB9UlZNLPOxmij7JlxZCDZYfjaS3tYxBlNX5%2BnJrfHBI3nvcEbzc1qe6icXb3cE1TSHZbrllFKOmMGkNwdHCp%2BPAAkFNXC0Hkror4Q2mkg2%2BfRpKSpOM9Qe6KJRNAHQwa5xQ50wTLTVK9TzpmmfP%2BrIuBSW6yA%2BVYMeyyrZQoMGC0fpWTMVEQ2g8QhiqnmSaJpEQMKw2%2BMrzWxvm9IADxf59%2BZ4oU%2F&X-Amz-Signature=5eb24b3a92f880a94f318d793197ecf17980935a3c3e58db6bccafe2151bdc6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      - [operatorOfLayer](https://sepolia.etherscan.io/address/0x58b4c2fef19f5cddd944aadd8dc99ccc71bfefdc#readProxyContract#F19) (layer2 address: **0x0990385f7bB5b97e2250635C0391f0FfB1fd781b** ) 
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/5a395243-4bd2-4b66-955c-b241a395761f/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-24_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.42.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RJ2LCW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIE8lZwOavopmNO0VfPxnV9cY4W1K9CZQTdrFYweYXRV8Ah9QwdQzkkW5kTY9yjW03%2BAFo270eZPUaZQE%2BolCE2D3Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyNzpPWNcSM5APeAAgq3AMRf2fcBNQygHk2H30BLtuwuNYTQgu5GIOV0munMRrF%2BxZNjTc1cRCKQtuPHRjtgE9tPI1l1PTEWFRQSlXZmqoWJuKbRDB%2F6twmn07qejDnX7xpJG4Kc%2FGX5r0tZY9JgW1YAxiaaXVrpLG7RubCIapYDxFqMbq8xlAPr1rlZ67TVC%2B31kKlZuDbmiPMBab6HcK81%2Bf1GSfQetNFHSXcV7rlXBSxcrl%2FIW0WinSKKOWlkwYHpm2M%2Fynezt4d3b1qF29rZbNrKkR7srGPoECyKUzRmTmcUv8H4TRLjs64A6v5YNSZj%2Brlp1Wc4864%2Fz8Ebtt5L%2FPjzfY31TbJoNHJvjQFE4i%2Fy8QFQqKJAEgMbvo2zPtr0eD7v1BSioClzGmjMPBfc3FceZhbam37QvyWbunLdrBfnME9ErAdOHs9eLyZNMSw04j%2BExoI%2BhAdpLc9ppRhirv2PwPebYCkDM2y3ztPK8uYXJQEpfAHp4i8V1ea4sMHcMuN9PhM6OZVYmG4ty%2Ba9REuHEYVww4W%2B20MXkRlZiVmRaA0huR18NtLjbqcfMALjKtoLRPMv6lFgac57qKAyfDxNvrPylepaI5EZaMDuEXs9UBpBTLTh6przoV3tkPYJJ10t5ymYNi3PDDRmtvMBjqnAXMwBdb8LBNq6cBNCHClLB0Kg6cP%2FnAXGrct4d%2F%2FUDny1v9SlOfGftYio3megVQl9hMnkLRMlxt62M4lUaAF4%2B%2FPMyacbXiyW6VKuxelbaAWxgchf%2FAmf0f4e8bo2vepNiN2y1FjaN9jT54VCedLKvUXDV30DxcI3RbHmEQN1DlgeWLEocpp6l8gM2gu19E6jPW2N4r3wLGlf7COSWHpR9q2ao8dAmxy&X-Amz-Signature=7a385344ab1d78314a99b6ef81707b5e07cb0e11e59f9fab1bd1d70d72f6b9fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
      - [operatorInfo](https://sepolia.etherscan.io/address/0x58b4c2fef19f5cddd944aadd8dc99ccc71bfefdc#readProxyContract#F17) (operator address ) 
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8f2e64e0-6555-489b-b305-c9b0a4c549b9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-24_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.42.18.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPTHXQEM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMEIgoqh3Z%2FwzsNkOQqsd9omhuz5yT8MJbPBbmT3CloAIhAJ44E9kUsM4FSOKD4c9kRbs3iRZjWYaaNgi33Nth7vB%2FKv8DCHoQABoMNjM3NDIzMTgzODA1IgyEmdDK73QziFYHt6Aq3AN6BkrtI%2BJsEti4xRe9cNa0hoAGh%2B1PZ3XbePpPEQywEjXw%2FW%2BRLoytEFzcu6PwmND37GL5kXEgwlsD48e3iKhmWZWMKXK0iNp7J4pInE6%2Fhs1PDeQWKFspbk2doFtljP8kat8bpxoLSNuxpPo7CvVAG%2FtcZaL9g65GFmGhNvn8rFXCjdsrQyq9A%2BLj5mwWj6RdjMVeRJzDQGGJOYxltm9F%2BMMWxAOpSA3cZb8DO1COFKdjILwl3MPFWxZ0d4TwzOiVCmSvNcsZCQW5DhZYrq1YoC3QM7eHei0SbgVv%2BlOUgb22UxCcN4XD7XGkXMhcEtOuo4befezw4%2BDQhBt9ZCuYluIY6gsWHKobhhg%2FdSVPgHn6XXivFT%2FX5K45y4uXYYIPRwI21KMHYwoOmZpr5RzhonHo%2F9Y1Xw79B7s9H7ST1L3djEh%2BlM9cX9PaPVpdOb0NnY0gSvYX%2F%2BHiejWGxIBeDJO%2F%2Fm2HpEB4FeH78svu3Q%2B2V701iwkRtTweko1MgDZzxb78zumZdpliH1W50IXoTLcT3oRpeD3%2FPWKuDhx7X%2BgnVFbK4BHTHK4PqJeVIZZNipUiPaWkNLJlMtc4IsZsDlZsXJyAFFyrk90zTLshPIxKiviO2%2FxWIPdzwjCfmdvMBjqkAaXXmFomlPbYEkWbdyC8TiFncJG1hJHD0OhjLYAacecYg3oGgluiAnGeKPnEyNBHhiT6Qa62ih5wcbG6HHv5BxiJM3IKxfhzug1Wq1u32onaPeDFkmiiNRq5sT8DSdM66i%2FxEX0WNJBdgVx0aHXO5Tzx0eL1iDkNlsAWFc6ZcTgvDmmgQ0ld7CO7XDK4TWkkFGlWusn8LphqTF4ua52z7xF0CKnC&X-Amz-Signature=33bc64fabf16240364e146ed2307def08127fd496b8b9f294c6a8d6a8cc51143&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 업데이트 시뇨리지 실행하여, 시뇨리지 받는 방법 

- (A) Candidate 컨트랙주소 : 스테이킹할때 layer2 주소로 사용됨 
  - 업데이트 시뇨리지 실행방법들 [example](https://github.com/tokamak-network/ton-staking-v2/blob/34e7c13788712123a58404131eaee15721cb61a3/test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts#L217) :
    - Candidate.updateSeigniorage() 
    - SeigManager.**updateSeigniorageLayer**( Candidate address)
- (B) Layer2Canddiate
  - 스테이킹할때 **Layer2Canddiate.candidate()  **주소가 layer2 주소로 사용된다. 
  - 업데이트 시뇨리지 실행방법 [example](https://github.com/tokamak-network/ton-staking-v2/blob/34e7c13788712123a58404131eaee15721cb61a3/test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts#L321)  
    - Layer2Canddiate.updateSeigniorage() 
- (C) CandidateAddOn : 스테이킹할때 layer2 주소로 사용됨 
  - 업데이트 시뇨리지 실행방법들 [example](https://github.com/tokamak-network/ton-staking-v2/blob/34e7c13788712123a58404131eaee15721cb61a3/test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts#L425) :  
    - CandidateAddOn.updateSeigniorage() 
    - SeigManager.updateSeigniorageLayer( CandidateAddOn address)

## 스테이킹 금액 조회하는  방법 

- (A) Candidate 컨트랙주소 : 스테이킹할때 layer2 주소로 사용됨 
  - SeigManager.stakeOf(Candidate address, account)
  - Candidate.stakedOf(account)
  - DAOCommitteeProxy.balanceOfOnCandidateContract(CandidateContract, user address)
- (B) Layer2Canddiate 
  - SeigManager.stakeOf(**Layer2Canddiate.candidate() **, account)
→ 현재 서비스에는 존재 X 
- (C) CandidateAddOn : 스테이킹할때 layer2 주소로 사용됨 
  - SeigManager.stakeOf(CandidateAddOn address, account)
  - CandidateAddOn.stakedOf(account)
  - DAOCommitteeProxy.balanceOfOnCandidateContract(CandidateAddOnContract, user address)

## APY 계산 방법  

- APY를 계산합니다.([link](https://github.com/tokamak-network/staking-community-version/blob/main/src/hooks/staking/useCalculateExpectedSeig.ts))

## 업데이트 시뇨리지 실행시, 받을 수 있는 시뇨리지 양 

- 스테이커가 받을 수 있는 시뇨리지 금액을 조회합니다.
  - [hook](https://github.com/tokamak-network/simple-staking-v2/blob/sepolia/src/hooks/staking/useCalculateExpectedSeig.ts) 
  - 위에 [APY 계산하는 식에](/18fd96a400a380dda636f3f64fc21dd1#18fd96a400a380ff80edd292ff671b81) [_seigOfLayer](https://github.com/tokamak-network/staking-community-version/blob/23e7ade5fe8e8311e17c02d78c6249d777979e99/src/hooks/staking/useCalculateExpectedSeig.ts#L319C24-L319C36) 해당 레이어가 받는 시뇨리지가 계산됩니다 . 이값에서, 스테이커가 해당 레이어에 스테이킹한 비율을 _seigOfLayer 양을 곱하면, 스테이커가 받는 시뇨리지 양입니다. 코드에서 [seig](https://github.com/tokamak-network/staking-community-version/blob/23e7ade5fe8e8311e17c02d78c6249d777979e99/src/hooks/staking/useCalculateExpectedSeig.ts#L320) 값입니다. 

### 스테이킹만 되는 Layer2 ? 

## Contract addresses  

- 관련 L1 컨트랙 주소를 조회합니다. ([link](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy?node-id=297-16204#1048907019))
  - Core Contracts  [mainnet](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md) , [sepolia](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-sepolia.md)  , [dao ](https://github.com/tokamak-network/tokamak-dao-contracts)
    - mainnet
      - DAO Committee   [0xDD9f0cCc044B0781289Ee318e5971b0139602C26](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)
      - SeigManager  0x0b55a0f463b6defb81c6063973763951712d0e5f
      - Staking (DepositManager)  0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e
    - sepolia 
      - DAO Committee [0xA2101482b28E3D99ff6ced517bA41EFf4971a386](https://sepolia.etherscan.io/address/0xA2101482b28E3D99ff6ced517bA41EFf4971a386)
      - SeigManager  0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7
      - Staking (DepositManager)  0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F
  - DAO Candidate 
    - Candidate or Layer2Canddiate or CandidateAddOn address 
    - Operator address 
      - Candidate 
        - operator address : Candidate.**candidate() **
      - Candidate: Layer2Canddiate 
        - **layer2 contract : 스테이킹 할 때 사용하는 layer2 주소  **, Candidate.candidate() 
        - operator address : **Candidate.candidate().operator()** 
      - CandidateAddOn
        - operator (OperatorManager) address : CandidateAddOn.candidate() or Layer2Manager.operatorOfLayer(CandidateAddOn address) 
        - OperatorManager’s manager  address : OperatorManager.manager()
        - [https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/OperatorManagerV1_1.json](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/test/abi/OperatorManagerV1_1.json)
  - L2 Info  (Only exists in CandidateAddOn) 
    - **RollupConfig** address : 
      - OperatorManager.operatorInfo( OperatorManager address ).rollupConfig 
    - **L1CrossDomainMessenger** Contract: RollupConfig.l1CrossDomainMessenger()
    - **L1StandardBridge** Contract: RollupConfig.l1StandardBridge()
    - **OptimismPortal** Contract:  RollupConfig.optimismPortal()

---

- Total Staked Amount 
  - 모든 Candidate들이 스테이킹한 총 양  (**발행된 시뇨리지 포함**) 
    - **SeigManager.stakeOfTotal() **
  - 모든 Candidate들이 스테이킹한 총 양 (**정산한 시뇨리지만 포함한 양**) 
    - **SeigManager.stakeOfAllLayers()**
      - 레이어의 개수가 너무 많아지면, SeigManager.stakeOfAllLayers() 함수가 느려질 가능성이 있습니다. 이때에는  프론트에서 [_stakeOfAllLayers 함수를](https://github.com/tokamak-network/ton-staking-v2/blob/81a271d3918a98c9c536ab58ef8a09034211badc/contracts/stake/managers/SeigManagerV1_2.sol#L632-L639) 구현해서, 사용해야 합니다. 
  - 각 Candidate에 스테이킹 된 양 (정산한 시뇨리지만 포함됨) 
    - address coinage = SeigManager.coinages(layer2) 
    - coinage.totalSupply() →  layer2에 스테이킹한 총량 (정산한 시뇨리지만 포함됨) 
    - 발행된것 (SeigManager.tot()).balanceOf(layer2) 

### For L2 sequencers ( CandidateAddOn 만 해당) 

- OperatorManager 의  매니저 주소를 변경합니다.
  - L2 시퀀서에게 발행되는 시뇨리지는 OperatorManager 컨트랙에 쌓입니다.
    - OperatorManager 컨트랙이 생성될때, **RollupConfig.unsafeBlockSigner()** 주소를 manager()로 설정됩니다. 
  -  OperatorManager.manager() 는 OperatorManager 컨트랙이 보유한 토큰을 클래임할 수 있습니다. 
- **L2의 unsafeBlockSigner() 는 OperatorManager의 매니저 권한을 가질수 있습니다. **
  - 추후 RollupConfig.unsafeBlockSigner() 주소가 변경되오, RollupConfig.unsafeBlockSigner() 주소와 manager()의 주소가 다른경우, RollupConfig.unsafeBlockSigner() 계정은 **OperatorManager.acquireManager() 함수를** 호출하여, OperatorManager.manager() 주소를 RollupConfig.unsafeBlockSigner()  주소로 변경할 수 있습니다. 
- OperatorManager 매니저가 토큰(시뇨리지로 받은 톤)을  클래임합니다. 
  - OperatorManager.**claimERC20**(address token, uint256 amount)
- L2 시퀀서 주소와 OperatorManager 매니저 주소를 조회합니다. 
  - 현재 L2 시퀀서 주소 : RollupConfig.unsafeBlockSigner()  
  - 시뇨리지를 클래임할 수 있는 매니저 주소 : OperatorManager.manager()
- L2에 브릿지된 TON TVL 을 조회합니다. 
  - L2 Type 조회 : [doc](/d76ffba7cf8d428a94a250399f7b09fe#cbb4b4a8cc4c407ea61856f16783a2a7) 
  - Thanos 인 (type == 2 ) 경우 : TONContract.balanceOf(RollupConfig.optimismPortal() address)
  -  Legacy 인 (type == 1 ) 경우 : TONContract.balanceOf(RollupConfig.l1StandardBridge() address)
- SeigManager에 등록된 L2 정보를 조회합니다. 
  - SeigManager.[getLayer2RewardInfo](https://github.com/tokamak-network/ton-staking-v2/blob/81a271d3918a98c9c536ab58ef8a09034211badc/contracts/stake/managers/SeigManagerV1_2.sol#L863-L865)(CandidateAddOn address)  external view returns (Layer2Reward memory) 
    - abi: [https://github.com/tokamak-network/ton-staking-v2/blob/deploy-5th-sepolia/test/abi/SeigManagerV1.json](https://github.com/tokamak-network/ton-staking-v2/blob/deploy-5th-sepolia/test/abi/SeigManagerV1.json)

```javascript

    struct Layer2Reward {
        uint256 **layer2Tvl**;   /// 현재 등록된 L2의 TVL , 이 값은 업데이트 시뇨리지를 실행할때 갱신되므로, 현재 TVL과 다를 수 있습니다.  이 값과 현재 값의 차이에 따라 L2시퀀서가 더 이익일 수 도 있고, 스테이커가 더 이익일 수 있습니다. 
        uint256 initialDebt;
        uint256 startBlock;
    }

```
- L2 시퀀서가 받을 수 있는 시뇨리지 금액을 조회합니다. 
  - SeigManager.**claimableL2Seigniorage**( CandidateAddOn address) 

## **Install**

Install the module using NPM:

```
npm install @tokamak-network/ton-staking-sdk --save
```

## **Quick Start**

```
const tonStakingLib = require('@tokamak-network/ton-staking-sdk');
 
```

# Folder 

```json
|--src
   |- abis
   |- configs
      |- abis.ts
      |- addresses.ts
      |- chains.ts
      |- constants.ts
      |- logger.ts 
   |- models
      |- contracts.ts
      |- transaction.ts
   |- clients.ts
   |- index.ts
   |- type.ts
|--tests
	 |- client-test.ts
|--fixup.sh
|--package.json
|--tsconfig.base.json
|--tsconfig.cjs.json
|--tsconfig.esm.json
|--tsconfig.json
|--README.md
	 
```