## Flow of Proposal

## Proposal Action :

1. Using [getActions](https://etherscan.io/address/0x408ed6354d4973f66138c91495f2f2fcbd8724c3#readProxyContract#F10) method we get the below information :
```javascript
targets address[], values uint256[], signatures string[], calldatas bytes[]

[ getActions(uint256) method Response ]
  targets   address[] :  
[[0x4Dbd4fc535Ac27206064B68FfCf827b0A60BAB3f]]
  values   uint256[] :  1000000000000000
  signatures   string[] :  
  calldatas   bytes[] :  0x679b6ded0000000000000000000000001f98431c8ad98523631ae4a59f267346ea31f9840000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110d9316ec0000000000000000000000000001a9c8182c09f50c8318d769245bea52c32be35bc0000000000000000000000001a9c8182c09f50c8318d769245bea52c32be35bc0000000000000000000000000000000000000000000000000000000000030d40000000000000000000000000000000000000000000000000000000003b9aca00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000448a7c195f0000000000000000000000000000000000000000000000000000000000000064000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000
```

### ***What does it mean to “queue” a proposal?***

**Queue** prepares a proposal for execution. The queue action sends the proposal to the Timelock contract, which starts the countdown until the proposal can be executed.

Someone needs to call the `queue()` function because the EVM (Ethereum Virtual Machine) does not support scheduled or automatic calls. Every call must be kicked off by a user.

If a Governor does not have a Timelock, then proposals don’t need to be queued. They can be executed as soon as the proposal passes.