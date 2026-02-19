## What is Upgraded

When creating an agenda, a memo field was added and the currentAgendaStatus function was added.

For more information, please refer to the following [link](/203d96a400a3805e92dcc97c46aa2eeb).

## Upgraded functions front usage example

ABI 

[DAOCommittee_V2.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8e6e8b4c-e0af-4668-ae96-3ede8d891d88/DAOCommittee_V2.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YMOYESN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T040445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCV9YQy97dFSb6PGoUWLrqH6PkPs1SmvSSJwVAXXmeAKQIhAOsuUCPxmbvVUYBYvkd1Mni3HATleDnOVne4IUQr9X8qKv8DCHQQABoMNjM3NDIzMTgzODA1Igx90KhMN%2BQpPUq2Qswq3AOTzotx5zuxUwkmmhKrtlNjqyOmGOG4eHLgUYBFh8RmnDz9tuyl02fOEAd48iYolMjY3pOOj0k%2BiiKem7cS6lNQH2WtcrJ2BsaJITM%2FlQdldmo9naeQh4llforwTKoIUE1U9xG5lNDF42FuXWQI0AR9wmcUueGYG7Ajfs6tg3ttszujsxr4NPkeBI15IlLrnEyDMgE30JyLuu4qJCkPEn9R2li0wX%2BMCHx9JIwK2W7lvwD6GcEapxjt5E64%2BvH%2FhXkhsJkTnuXSS5OikhX1fsH7OBVGDk64F4Sxru3Nukexwu0P8APHSL8GekqcIsl%2F%2BHNjtEVeSlHSspByGJPDQ9mVznS%2FoGibroQ6LSYIz444Y4J9O50B9Q%2BjLBH1nzk8Y6FPjJF%2FyIMmh5Hk2XVzxL3ea0TjXQ6SJncUM8gxp4Sl6sSeN1Px6UjKnb3d5Zc9bOHjX90MT%2FXo7iwztqYQdwZW5e0y9d5HeMbXagaJYx8b%2B24th%2BWmPAi727ET%2BPquYF5VmPja2UXafzUkmnnHq2E5Rn8k%2FZO3jjJRGP795g0VHEzn2wHiW354TyrKwL9CHyCQu%2FsJptypVwHMkxS%2Fv9yrYsH15nzHYedVxq8i%2B3gbsGD4QYZZwOpHszoEDTDA7tnMBjqkASmEZs%2FpNpkouJ61c010kZWSBkKXMYSCIMB2yefvLk%2B6GLRhHDJgTTl5TjaAImvKV2yEkrIQvOOeaYp9w%2FNwmgazRUckE%2BpTTbya0EC%2FsljWMVwhzw6t6PeqrUSE9N4Ky2E%2FGSgixZNSyVHWjqxKh6N5oOnHeDRMk6SgRasUbppv4syVeg4YCx11qPp%2BfuxXCORSgwzSrWryXrK7o40%2B8YiXE7Zo&X-Amz-Signature=761eea2aa1f962eeced29f94088fb4786e12609d4f8a14bd9b8ea53b1912c814&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ApproveAndCall call

```solidity
const noticePeriod = await daoagendaManager.minimumNoticePeriodSeconds();
const votingPeriod = await daoagendaManager.minimumVotingPeriodSeconds();

const selector = Web3EthAbi.encodeFunctionSignature("setMinimumNoticePeriodSeconds(uint256)");

const newMinimumNoticePeriod = 40;
const data = padLeft(newMinimumNoticePeriod.toString(16), 64);
const functionBytecode = selector.concat(data);

//Memo can be in string format.
memo = ""
memo = "memo"
memo = "https://snapshot.box/#/explore3"

const param = Web3EthAbi.encodeParameters(
    ["address[]", "uint128", "uint128", "bool", "bytes[]", "string"],
    [
        [daoagendaManager.address], 
        noticePeriod.toString(), 
        votingPeriod.toString(), 
        true, 
        [functionBytecode],
        memo
    ]
);

const agendaFee = await daoagendaManager.createAgendaFees();

// create agenda
await ton.connect(user1).approveAndCall(
    daoCommitteeProxy.address,
    agendaFee,
    param
);
```

currentAgendaStatus Call 

```solidity
agendaID = (await daoagendaManager.numAgendas()).sub(1);

let result = await daoCommittee_V2_Contract.currentAgendaStatus(agendaID)
//result.currentResult
//result.cureentStatus
```

agendaMemo Call

```solidity
let daoMemo = await daoCommittee_V2_Contract.agendaMemo(agendaID)
```

version Call

```solidity
await daoCommittee_V2_Contract.version()

version = 2.0.0
```

## Q&A

(1) What has changed in agenda transmission is that a memo field has been added. What item is used as a memo field?

(2) How can I check the version of the contract? Is this a contract that supports memo fields?

(3) Which functions from the contract should I check on the front?