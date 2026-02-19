[https://github.com/tokamak-network/ton-staking-v2/tree/codeReview_apply](https://github.com/tokamak-network/ton-staking-v2/tree/codeReview_apply)

https://www.notion.so/tokamak/Contract-review-request-form-ton-staking-v2-81ef6a68bdb24aa3b171e25d53f76b72

- Contract scope (Contract subject to code review) 
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/L2RegistryProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/L2RegistryProxy.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/L2RegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/L2RegistryV1_1.sol)
  - 
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/Layer2ManagerV1_1.sol)
  - 
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/factory/OperatorFactory.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/factory/OperatorFactory.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/OperatorV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/layer2/OperatorV1_1.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/Layer2CandidateProxy.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/Layer2CandidateProxy.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/Layer2CandidateV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/Layer2CandidateV1_1.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/DAOCommitteeAddV1_1.sol#L109](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/dao/DAOCommitteeAddV1_1.sol#L109)
    - Only the createLayer2Candidate function is subject to code review.
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/stake/managers/SeigManagerV1_3.sol)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/stake/managers/DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/contracts/stake/managers/DepositManagerV1_1.sol)

# Changes in Staking V2.5  

- change contract name ‘L2Registry’ to **L1BridgeRegistry** 
- change name ‘**systemConfig**’ to **l2Config**
- change name ‘**systemConfigType**’ to **rollupType**
- change name **ISystemConfig to ****IOptimismSystemConfig**
- change **registerL2Config to ‘registerL2Config**(address _l2Config, uint8 _type, address _l2TON )  external  onlyRegistrant’
- change struct OperatorInfo in L2Manager
```javascript
struct OperatorInfo {
      address systemConfig; **// l2Config**
      address layer2Candidate; // candidateAddOn 
  }
->

struct OperatorInfo {
      address **l2Config**; ** **
      address candidateAddOn;  
  }
```
- change struct SystemConfigInfo in L2Manager
```javascript
struct SystemConfigInfo {
      uint8 stateIssue;  // status for giving seigniorage ( 0: none , 1: registered, 2: paused )
      address operator; 
  }
->

struct SeqSeigStatus {  
      uint8 status; // status for giving seigniorage ( 0: none , 1: registered, 2: paused )
      address operatorManager;  
  }
```
- change contract name ‘Layer2CandidateFactory’ to candiateAddOnFactory
- change function name ‘createLayer2Candidate’ to createCandidateAddOn 
- change contract name ‘Operator’ to OperatorManager
- delete operator in Operator contract : ~~**mapping(address => bool) public operator;**~~~~ ~~
- **change function isOperator():  if msg.sender is **manager, returns** true. 
**

# Repo 

[https://github.com/tokamak-network/ton-staking-v2/issues/35](https://github.com/tokamak-network/ton-staking-v2/issues/35)

[https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5](https://github.com/tokamak-network/ton-staking-v2/tree/staking-v2.5)