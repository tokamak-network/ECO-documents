## What is Upgraded

When creating an agenda, a memo field was added and the currentAgendaStatus function was added.

For more information, please refer to the following [link](/203d96a400a3805e92dcc97c46aa2eeb).

## Upgraded functions front usage example

ABI 

[DAOCommittee_V2.json](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8e6e8b4c-e0af-4668-ae96-3ede8d891d88/DAOCommittee_V2.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D4HRWHH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0xvoh0qGqnv0bZjb6oAGp0k9fjajq%2FCw6%2BnV4qJGbdAIgbq%2FCDmY08YHKnjz85jZFBHdOw2FrlSCdNdFiTt3Zhjcq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDDO4wuksrmov0NSCyircA%2FrWhPM2Pve39gCy2tlaW8J6lPjVsP9mN6GcsUribA%2B3KHtgh0p8nFTUKQZWvyFHgLTVMfVn%2BYdWtPZ3YbvEOn5PfcvrTyPlJ2fVgA4MVgiTImvh6pcA0cNIHzmyEE5EV0XBziSkkJOO6isFW1oakuouPVAt05%2BaqQnj%2FMTa3h%2FEmUu0ooqqtkx0lg%2FlyTfBJSNFH79d2e%2BKHerDjZM%2Fv63wzRA8Kv0DjIWqY9nBfHVPbHbsTS8ZnM3pRpEdxmQ52e%2FU2%2FiMmV7OSKREbDGVH6pBk8qyDnSHKwVf%2F0TeP1F2ORIDj7tQnDaKuMabSaJphYxWj7rDBqbRxpZBNiusYws2Sjet9Zs2YBa72VI7OlaRisO20tMcATmADOR7Io4BLBYYOCe9st%2BVlf5JBxBCfC0x4gqzNxwJIk9Zqb5uBRLzLDgoOpunOzepmSG26lbnfoz8svk%2FHS5pkwubR%2Fve5%2FcguKfODIMSh23zUSh7RFQeO3cB2%2BMo0GPjZkUhoJET02bK4Cq%2BoSPdfp97xVOO7sac%2Bz%2FaI103RIhc%2FNa7DMyWMmUyZI%2BL65%2F7t0ufEDK%2FSHCJzUL0%2FlG9XkFHaHBSI6ILevRHeUdpIwBI2qaXNx%2BJacp43v7zddy1Z5F7MLPv2swGOqUBpmrNk53ggVUWiLxEUEUIh0gXnIKab0bl2SJwEXvb%2FRiB8DuEmGW6vlC4i4o5ifo8fxcb1mSsMixZLi5XE9zCywgTOMayHfehTrpGviK%2Bco1QgKku7M8ujL7SPZ025BSjKxFU4SgYLxadutWbw5%2BmG2q8q5xFB%2Fqc82Q%2BcSewWLXnXn49xtOqlks7g1Y1L%2FnPTC3ODzIdyDUp542JxftwMiHh7Y9u&X-Amz-Signature=1168035a2696060246b3bf94d1e4789b2638bcac777023f88d15cf7f09534b99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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