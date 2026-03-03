# 1. 토큰 인플레이션/분배 및 DAO 관련

### 1-1. 스테이킹 V2에서 시뇨리지로 인해 발생하는 추가 발행분은 시퀀서 및 스테이커들에게 분배되는 것으로 확인함. 이때, '스테이커'란 위임 스테이킹을 한 사용자들인지

A : 스테이커란 위임 스테이킹을 한 사용자들 맞습니다. (코드상 : 시퀀서 → operator)

### 1-2. 인플레이션률의 산정에 대한 구체방식이 어떻게 되는지

A : 인플레이션률을 결정하는 곳은 SeigManager Contract에서 seigPerBlock()의 값 입니다.
해당 값은 <u>**블록당 TON의 발행 시뇨리지 양**</u>입니다. 초기 한번만 설정하고 현재코드에서는 변경 불가능합니다.

- 실제 값 Contract [Link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F45)   ( ray 단위 사용. decimals = 27)
  - **seigPerBlock()** 함수 값 : 3920000000000000000000000000 WTON = **3.92 TON**
- 해당 값 설정 Contract [Code](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L154-L177)

### 1-3. 시뇨리지 분배방식(시퀀서 및 스테이커에 분배) 변동 여부

### 분배 방식  

> [!tip]
> 💡 일정기간 동안 발생한 시뇨리지(Seig) 분배 방법 

```javascript
• 𝑇 : 톤 총 공급량
• 𝑆 : 스테이킹 총량
•** 𝑆𝑒𝑖𝑔** : 일정 기간 동안 발생한 시뇨리지
• 𝑊𝑆 : 스테이커에게 분배되는 시뇨리지 가중치
• 𝑊𝐷 : 톤 다오Vault(TON DAOVault)에 분배되는 시뇨리지 가중치 
• 𝑊𝑃 : sTOS 보유자들에게 분배되는 시뇨리지 가중치 
 (𝑊𝑆 + 𝑊𝐷 + 𝑊𝑃 ≤ 1)
• *StakedSeig*: 총 공급량 중 스테이킹한 비율에 따른 시뇨리지 분배양 =** 𝑆𝑒𝑖𝑔** * S/T
• *UnstakedSeig*: 총 공급량 중 스테이킹 하지 않은 비율에 따른 시뇨리지 분배양 = 𝑆𝑒𝑖𝑔 - *StakedSeig* 
```


• 스테이킹한 사용자에게 분배되는 시뇨리지 양 = *StakedSeig + ( UnstakedSeig * ****𝑊𝑆 ****) (in code : *[*link*](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L720-L732)*)*
• 톤 다오Vault(TON DAOVault)에 분배되는 시뇨리지 양 = *UnstakedSeig * ****𝑊𝐷****  (in code : *[*link*](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L748-L751)*)*
• sTOS 보유자들에게 분배되는 시뇨리지 양 = *UnstakedSeig ***** 𝑊𝑃****  (in code : *[*link*](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L742-L746)*)*

> [!tip]
> 💡 스테이커에게 시뇨리지 분배 방법 

시뇨리지는 SeigManager 컨트랙의  [tot](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManagerStorage.sol#L42)와 [coinages](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManagerStorage.sol#L45)스토리지에 [RefactorCoinageSnapshot](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/tokens/RefactorCoinageSnapshot.sol#L30C14-L30C14) 컨트랙을 이용하여 관리합니다. 스테이킹 보유량을 반영하는 팩터 값을 변경하여, 스테이커들의 스테이킹 양에 시뇨리지를 반영합니다.. 

- tot 컨트랙  : 모든 레이어를 통합하여 스테이킹된 양을 관리합니다. 발행되는 시뇨리지를 스테이킹 양에 추가반영합니다.   
- coinage 컨트랙 : 각 레이어별로 스테이킹된 양을 관리합니다. 해당 레이어에 발행되는 시뇨리지를 스테이킹양에 추가 반영합니다.  
- 시뇨리지 업데이트 : 발행되는 시뇨리지 양을 계산하여, [tot의 총 발행 시뇨리지 발행](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManager.sol#L735) , [해당 레이어에 시뇨리지 발행](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManager.sol#L448-L454) 을 실행합니다.  
  - [RefactorCoinageSnapshot 의 팩터를 변경](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/tokens/RefactorCoinageSnapshot.sol#L249) ([link](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/tokens/RefactorCoinageSnapshot.sol#L165-L178))하여 발행되어야 할 시뇨리지 양을 스테이킹 양에 적용합니다.   
```javascript
function _applyFactor(uint256 v, uint256 refactoredCount) internal view returns (uint256) {

      if (v == 0) {
        return 0;
      }

      IRefactor.Factor memory _factor = _valueAtFactorLast();

      v = rmul2(v, _factor.factor);

      if (_factor.refactorCount > refactoredCount) {
        v = v * REFACTOR_DIVIDER ** (_factor.refactorCount - refactoredCount);
      }
      return v;
    }
```

> [!tip]
> 💡 시퀀서(operator)에게 시뇨리지 분배하는 방법

- 각 레이어별로 시퀀서의 수수료(_commissionRates)를 저장합니다.   [link](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManagerStorage.sol#L61C43-L61C59) 
- 해당 레이어의 오퍼레이터는 시퀀서 수수료를 변경하여 시퀀서가 받는 시뇨리지 분배량을 조절할 수 있습니다.  [link](https://github.com/tokamak-network/ton-staking-v2/blob/5b9ec6279385e32d142a3b868c4540bf713722a3/contracts/stake/managers/SeigManager.sol#L300-L328)
- 수수료에 따라 해당 레이어에 발행되는 시뇨리지의 일정부분을 시퀀서(operator)에게 발행합니다.  [link](https://github.com/tokamak-network/ton-staking-v2/blob/main/contracts/stake/managers/SeigManager.sol#L604-L671) 
```javascript
function _calcSeigsDistribution(
    address layer2,
    RefactorCoinageSnapshotI coinage,
    uint256 prevTotalSupply,
    uint256 seigs,
    bool isCommissionRateNegative_,
    address operator
  ) internal returns (
    uint256 nextTotalSupply,
    uint256 operatorSeigs
  ) {
    if (block.number >= delayedCommissionBlock[layer2] && delayedCommissionBlock[layer2] != 0) {
      _commissionRates[layer2] = delayedCommissionRate[layer2];
      _isCommissionRateNegative[layer2] = delayedCommissionRateNegative[layer2];
      delayedCommissionBlock[layer2] = 0;
    }

    uint256 commissionRate = _commissionRates[msg.sender];

    nextTotalSupply = prevTotalSupply + seigs;

    // short circuit if there is no commission rate
    if (commissionRate == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    // if commission rate is possitive
    if (!isCommissionRateNegative_) {
      operatorSeigs = rmul(seigs, commissionRate); // additional seig for operator
      nextTotalSupply = nextTotalSupply - operatorSeigs;
      return (nextTotalSupply, operatorSeigs);
    }

    // short circuit if there is no previous total deposit (meanning, there is no deposit)
    if (prevTotalSupply == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    // See negative commission distribution formular here: TBD
    uint256 operatorBalance = coinage.balanceOf(operator);

    // short circuit if there is no operator deposit
    if (operatorBalance == 0) {
      return (nextTotalSupply, operatorSeigs);
    }

    uint256 operatorRate = rdiv(operatorBalance, prevTotalSupply);

    // ɑ: insufficient seig for operator
    operatorSeigs = rmul(
      rmul(seigs, operatorRate), // seigs for operator
      commissionRate
    );

    // β:
    uint256 delegatorSeigs = operatorRate == RAY
      ? operatorSeigs
      : rdiv(operatorSeigs, RAY - operatorRate);

    // 𝜸:
    operatorSeigs = operatorRate == RAY
      ? operatorSeigs
      : operatorSeigs + rmul(delegatorSeigs, operatorRate);

    nextTotalSupply = nextTotalSupply + delegatorSeigs;

    return (nextTotalSupply, operatorSeigs);
  }
```

### 시뇨리지 변동 여부 및 방법 

**전체 발행되는 시뇨리지 양은 변동할 수 없으며****, **

**스테이커 , TON DAOVault, sTOS 보유자에게 분배되는 각 시뇨리지 분배양은 분배 가중치를 변경하여 변경할 수 있습니다.  **** **

- **현재 설정된 값 **
  - 𝑊𝑆 : 스테이커에게 분배되는 시뇨리지 가중치 ( ray 단위 사용. decimals = 27)
    - 현재 설정값 Contract [Link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F44) 
      - **relativeSeigRate**()  : 400000000000000000000000000 (40%)
  - 𝑊𝐷 : 톤 다오Vault(TON DAOVault)에 분배되는 시뇨리지 가중치 ( ray 단위 사용. decimals = 27)
    - 현재 설정값 Contract [Link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F17)
      - **daoSeigRate() : **500000000000000000000000000 (50%)
  - 𝑊𝑃 : sTOS 보유자들에게 분배되는 시뇨리지 가중치 ( ray 단위 사용. decimals = 27)
    - 현재 설정값 Contract [Link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F39)
      - **powerTONSeigRate() :  **100000000000000000000000000 (10%)
- **시뇨리지 분배 가중치 변경 방법 **
  - DAO에서 Agenda를 통해서 변경 될 수 있습니다. 
  - DAO Agenda는 누구나 신청가능하며 DAO Member들이 투표를 통해서 Agenda를 통과 시킬 수 있습니다.
  - Agenda생성은 DAO가 오픈되면 [https://dao.tokamak.network/#/propose](https://dao.tokamak.network/#/propose) 에서 TypeA의 SeigManagerContract에서 setPowerTONSeigRate, setDaoSeigRate, setPseigRate로 실행 할 수 있습니다.
  - how to call setPowerTONSeigRate Agenda
```javascript
const Web3EthAbi = require('web3-eth-abi');
const { padLeft } = require('web3-utils');

let agendaManagerAddr = "0xcD4421d082752f363E1687544a09d5112cD4f484"
let seigManagerAddr = "0x0b55a0f463b6defb81c6063973763951712d0e5f"
let DAOProxyAddr = "0xDD9f0cCc044B0781289Ee318e5971b0139602C26"
let tonAddr = "0x2be5e8c109e2197D077D13A82dAead6a9b3433C5"

const noticePeriod = await daoagendaManager.minimumNoticePeriodSeconds();
const votingPeriod = await daoagendaManager.minimumVotingPeriodSeconds();

const agendaFee = await daoagendaManager.createAgendaFees();

let targets = [];
let functionBytecodes = [];

const selector1 = Web3EthAbi.encodeFunctionSignature("setPowerTONSeigRate(uint256)");

const powerTONRate = 100000000000000000000000000

const data1 = padLeft(powerTONRate.toString(16), 64);

const functionBytecode1 = selector1.concat(data1)

targets.push(seigManagerAddr);
functionBytecodes.push(functionBytecode1)

const param = Web3EthAbi.encodeParameters(
    ["address[]", "uint128", "uint128", "bool", "bytes[]"],
    [
        targets, 
        noticePeriod.toString(),
        votingPeriod.toString(),
        false,
        functionBytecodes
    ]
)

await ton.connect(user).approveAndCall(
    daoCommitteeProxy.address,
    agendaFee,
    param
);
```
  - how to call setDaoSeigRate Agenda
```javascript
const Web3EthAbi = require('web3-eth-abi');
const { padLeft } = require('web3-utils');

let agendaManagerAddr = "0xcD4421d082752f363E1687544a09d5112cD4f484"
let seigManagerAddr = "0x0b55a0f463b6defb81c6063973763951712d0e5f"
let DAOProxyAddr = "0xDD9f0cCc044B0781289Ee318e5971b0139602C26"
let tonAddr = "0x2be5e8c109e2197D077D13A82dAead6a9b3433C5"

const noticePeriod = await daoagendaManager.minimumNoticePeriodSeconds();
const votingPeriod = await daoagendaManager.minimumVotingPeriodSeconds();

const agendaFee = await daoagendaManager.createAgendaFees();

let targets = [];
let functionBytecodes = [];

const selector1 = Web3EthAbi.encodeFunctionSignature("setDaoSeigRate(uint256)");

const DaoSeigRate = 500000000000000000000000000

const data1 = padLeft(DaoSeigRate.toString(16), 64);

const functionBytecode1 = selector1.concat(data1)

targets.push(seigManagerAddr);
functionBytecodes.push(functionBytecode1)

const param = Web3EthAbi.encodeParameters(
    ["address[]", "uint128", "uint128", "bool", "bytes[]"],
    [
        targets, 
        noticePeriod.toString(),
        votingPeriod.toString(),
        false,
        functionBytecodes
    ]
)

await ton.connect(user).approveAndCall(
    daoCommitteeProxy.address,
    agendaFee,
    param
);
```
  - how to call setPseigRate Agenda
```javascript
const Web3EthAbi = require('web3-eth-abi');
const { padLeft } = require('web3-utils');

let agendaManagerAddr = "0xcD4421d082752f363E1687544a09d5112cD4f484"
let seigManagerAddr = "0x0b55a0f463b6defb81c6063973763951712d0e5f"
let DAOProxyAddr = "0xDD9f0cCc044B0781289Ee318e5971b0139602C26"
let tonAddr = "0x2be5e8c109e2197D077D13A82dAead6a9b3433C5"

const noticePeriod = await daoagendaManager.minimumNoticePeriodSeconds();
const votingPeriod = await daoagendaManager.minimumVotingPeriodSeconds();

const agendaFee = await daoagendaManager.createAgendaFees();

let targets = [];
let functionBytecodes = [];

const selector1 = Web3EthAbi.encodeFunctionSignature("setPseigRate(uint256)");

const PseigRate = 400000000000000000000000000

const data1 = padLeft(PseigRate.toString(16), 64);

const functionBytecode1 = selector1.concat(data1)

targets.push(seigManagerAddr);
functionBytecodes.push(functionBytecode1)

const param = Web3EthAbi.encodeParameters(
    ["address[]", "uint128", "uint128", "bool", "bytes[]"],
    [
        targets, 
        noticePeriod.toString(),
        votingPeriod.toString(),
        false,
        functionBytecodes
    ]
)

await ton.connect(user).approveAndCall(
    daoCommitteeProxy.address,
    agendaFee,
    param
);
```
  - abi
[DAOCommitteeProxy.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ecf9362a-930a-408c-a0d5-677ae02cf6c1/DAOCommitteeProxy.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKD7DBOB%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENTBwyH9VoiuhfeBrVnbyIWPVfE%2FvUD3BnN%2B0vw3zPnAiAjSOGtVH0D%2FUEbb90byU0lMzCXFiyuIFkznHy2lEL2JCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMCYD2FDqJaX9wGssaKtwDVBjm3JAnqQaJ4LNF8%2BIa5CvDTMwn7wkVkvICL%2FehlZ7FBEJGOldxAXoIiV1WhGoYlJA46GN6KLvD%2FSZqq%2BMbGDNvloOI0VHloNY8RKeib2cLE1PMm6KDz7CofR2A9ETnEwMWb%2B1U1ECnggDtezbGZ20bAScxxH2FO9CtPlLjiY3kM7hHLm%2B0SN5KNANlPXCjfyJZNnkR750yfF5JCsbThbJrxqQIRabuj9kKg9Adp67NzI52dcFuCsOAsvS5RtCGEfocNLhF0OQPAbpM5yKM0XpAomYMrOF3S1tMvsgUL5JlITeYbYCbYrOkXGLRv1oZbq0mW1PFyZ5yqexrMA62UBtVQKRaCqz56b6SHLbDH3xwxyX9EFfOCVJqecX3XTFyf5Ap8qKXI3XRs4pHbvfDjnAbWa0F1VQkd5a21BNVvCE%2FoQllZ8CLLvQcAGz4vqVHJiHmK8jpafUuhf%2FwLR0GGWdgUL2141yYibt26n4Vcyz%2BLA9Csq5XBxjXajH9JxP9M14wIzG3jstmK0nSXKhE3Jf2NsZETpjsBcSoGJXfS2Lxv7nezSyt41KGhKL6pr%2BXSvECXQQ7RvkRsKBLn4wSP9BQlccLU8CcjTk%2BgH0SX12bQhyvOEsFXjdUM4YwqJjbzAY6pgFV789E%2B8QTbqL3LwyQf84kyZPMjomCCX%2Fga6NCB6Mlfht4f44D3XYqugluvtwPY%2FDP2WO%2BtpuJyPdnVa2TWq6DKz3%2FMOijRfjZ7g0ow2ZrWgaQ3s%2B3FKukskwwaPUZNYj29Q1sS2qgZN1PlyyU3LCPOuTofWVG2e9N5%2FzuHz7wi8bdULtibtEVEldAOUwKVIR7OVSagEaht6JMG7f%2Fpfc%2BogZml2Vk&X-Amz-Signature=a835e78fce64459e13ea15c3df48fcd199d9228e0bb2b08079352c89f1a48d17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[daoAgendaManager.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/49316b97-0749-49aa-a2f3-b09473da6936/daoAgendaManager.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKD7DBOB%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENTBwyH9VoiuhfeBrVnbyIWPVfE%2FvUD3BnN%2B0vw3zPnAiAjSOGtVH0D%2FUEbb90byU0lMzCXFiyuIFkznHy2lEL2JCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMCYD2FDqJaX9wGssaKtwDVBjm3JAnqQaJ4LNF8%2BIa5CvDTMwn7wkVkvICL%2FehlZ7FBEJGOldxAXoIiV1WhGoYlJA46GN6KLvD%2FSZqq%2BMbGDNvloOI0VHloNY8RKeib2cLE1PMm6KDz7CofR2A9ETnEwMWb%2B1U1ECnggDtezbGZ20bAScxxH2FO9CtPlLjiY3kM7hHLm%2B0SN5KNANlPXCjfyJZNnkR750yfF5JCsbThbJrxqQIRabuj9kKg9Adp67NzI52dcFuCsOAsvS5RtCGEfocNLhF0OQPAbpM5yKM0XpAomYMrOF3S1tMvsgUL5JlITeYbYCbYrOkXGLRv1oZbq0mW1PFyZ5yqexrMA62UBtVQKRaCqz56b6SHLbDH3xwxyX9EFfOCVJqecX3XTFyf5Ap8qKXI3XRs4pHbvfDjnAbWa0F1VQkd5a21BNVvCE%2FoQllZ8CLLvQcAGz4vqVHJiHmK8jpafUuhf%2FwLR0GGWdgUL2141yYibt26n4Vcyz%2BLA9Csq5XBxjXajH9JxP9M14wIzG3jstmK0nSXKhE3Jf2NsZETpjsBcSoGJXfS2Lxv7nezSyt41KGhKL6pr%2BXSvECXQQ7RvkRsKBLn4wSP9BQlccLU8CcjTk%2BgH0SX12bQhyvOEsFXjdUM4YwqJjbzAY6pgFV789E%2B8QTbqL3LwyQf84kyZPMjomCCX%2Fga6NCB6Mlfht4f44D3XYqugluvtwPY%2FDP2WO%2BtpuJyPdnVa2TWq6DKz3%2FMOijRfjZ7g0ow2ZrWgaQ3s%2B3FKukskwwaPUZNYj29Q1sS2qgZN1PlyyU3LCPOuTofWVG2e9N5%2FzuHz7wi8bdULtibtEVEldAOUwKVIR7OVSagEaht6JMG7f%2Fpfc%2BogZml2Vk&X-Amz-Signature=769110b8da00c379a23d7cb68223e61e5f3d417cc46431a2259f76b47f9b1e77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[TON.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7820851a-b70e-40ce-9803-0bceefb53c36/TON.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKD7DBOB%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENTBwyH9VoiuhfeBrVnbyIWPVfE%2FvUD3BnN%2B0vw3zPnAiAjSOGtVH0D%2FUEbb90byU0lMzCXFiyuIFkznHy2lEL2JCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMCYD2FDqJaX9wGssaKtwDVBjm3JAnqQaJ4LNF8%2BIa5CvDTMwn7wkVkvICL%2FehlZ7FBEJGOldxAXoIiV1WhGoYlJA46GN6KLvD%2FSZqq%2BMbGDNvloOI0VHloNY8RKeib2cLE1PMm6KDz7CofR2A9ETnEwMWb%2B1U1ECnggDtezbGZ20bAScxxH2FO9CtPlLjiY3kM7hHLm%2B0SN5KNANlPXCjfyJZNnkR750yfF5JCsbThbJrxqQIRabuj9kKg9Adp67NzI52dcFuCsOAsvS5RtCGEfocNLhF0OQPAbpM5yKM0XpAomYMrOF3S1tMvsgUL5JlITeYbYCbYrOkXGLRv1oZbq0mW1PFyZ5yqexrMA62UBtVQKRaCqz56b6SHLbDH3xwxyX9EFfOCVJqecX3XTFyf5Ap8qKXI3XRs4pHbvfDjnAbWa0F1VQkd5a21BNVvCE%2FoQllZ8CLLvQcAGz4vqVHJiHmK8jpafUuhf%2FwLR0GGWdgUL2141yYibt26n4Vcyz%2BLA9Csq5XBxjXajH9JxP9M14wIzG3jstmK0nSXKhE3Jf2NsZETpjsBcSoGJXfS2Lxv7nezSyt41KGhKL6pr%2BXSvECXQQ7RvkRsKBLn4wSP9BQlccLU8CcjTk%2BgH0SX12bQhyvOEsFXjdUM4YwqJjbzAY6pgFV789E%2B8QTbqL3LwyQf84kyZPMjomCCX%2Fga6NCB6Mlfht4f44D3XYqugluvtwPY%2FDP2WO%2BtpuJyPdnVa2TWq6DKz3%2FMOijRfjZ7g0ow2ZrWgaQ3s%2B3FKukskwwaPUZNYj29Q1sS2qgZN1PlyyU3LCPOuTofWVG2e9N5%2FzuHz7wi8bdULtibtEVEldAOUwKVIR7OVSagEaht6JMG7f%2Fpfc%2BogZml2Vk&X-Amz-Signature=e2c926c71cb6d1e04f9ffafb5b966667499fa957cae4ddfaa126d562178b39ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

# 2. Titan 

## 2-1. tokamak staking의 DAO Candidate가 되기 위한 방법 (퍼미션 방식인지, 어디서 무엇을 어떻게 해야하는지 등) > 오퍼레이터가 되는 절차. 어디서 무엇을 해야 오퍼레이터가 되는지? 

A : **DAO Candidate는 누구나 될 수** 있으며, 다음([**link**](https://docs.tokamak.network/docs/en/guides/ton-staking/how-to-set-candidate))과 같은 방법으로 DAO Candidate를 등록시킬 수 있습니다. 

< 참고 1 >  <u>**특정 레이어(candidate)에서 발급된 시뇨리지를 가져가기 위해서는 해당 레이어의 시퀀서(오퍼레이터)가 1000톤 초과의 톤을 스테이킹 해야 합니다.**</u> 따라서,  레이어(candidate)를 만들고 난 뒤에는, 시퀀서(오퍼레이터)가 [https://simple.staking.tokamak.network/staking](https://simple.staking.tokamak.network/staking) 웹페이지를 통해 등록된 레이어(candidate)에 1001TON을 staking 해주시기 바랍니다.  

< 참고 2 > DAO candidate는 누구나 될 수 있으며, <u>**DAO 아젠다의 투표권을 갖는 Member**</u>는 candidate 의challenge를 통해 member자리를 획득할 수 있습니다. <u>**Member 선정을 위한 challenge에서는 투표권(해당 candidate에 스테이킹한 물량)을 더 많이 보유한 사람이 이기게**</u> 됩니다.  

현재 설정된 최대 멤버수는 3입니다. 