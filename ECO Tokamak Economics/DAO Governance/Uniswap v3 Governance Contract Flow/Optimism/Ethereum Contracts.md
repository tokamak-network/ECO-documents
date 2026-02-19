## Flow of Proposal

[https://etherscan.io/txs?a=0x408ed6354d4973f66138c91495f2f2fcbd8724c3&p=853](https://etherscan.io/txs?a=0x408ed6354d4973f66138c91495f2f2fcbd8724c3&p=853) 

[https://etherscan.io/tx/0x6dc60fc7d8a8a948f62baefe299b691f4683313669db0dddee178c1dfe955824](https://etherscan.io/tx/0x6dc60fc7d8a8a948f62baefe299b691f4683313669db0dddee178c1dfe955824)

[https://etherscan.io/tx/0x6dc60fc7d8a8a948f62baefe299b691f4683313669db0dddee178c1dfe955824#eventlog#285](https://etherscan.io/tx/0x6dc60fc7d8a8a948f62baefe299b691f4683313669db0dddee178c1dfe955824#eventlog#285)

## Proposal Action :

1. Using [getActions](https://etherscan.io/address/0x408ed6354d4973f66138c91495f2f2fcbd8724c3#readProxyContract#F10) method we get the below information :
```javascript
targets address[], values uint256[], signatures string[], calldatas bytes[]

[ getActions(uint256) method Response ]
  targets   address[] :  
[[0x25ace71c97B33Cc4729CF772ae268934F7ab5fA1]]
  values   uint256[] :  0
  signatures   string[] :  
  calldatas   bytes[] :  0x3dbb202b000000000000000000000000a1dd330d602c32622aa270ea73d078b803cb3518000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000002dc6c000000000000000000000000000000000000000000000000000000000000000c46fadcf720000000000000000000000001f98431c8ad98523631ae4a59f267346ea31f984000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000448a7c195f000000000000000000000000000000000000000000000000000000000000006400000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

### ***What does it mean to “queue” a proposal?***

**Queue** prepares a proposal for execution. The queue action sends the proposal to the Timelock contract, which starts the countdown until the proposal can be executed.

Someone needs to call the `queue()` function because the EVM (Ethereum Virtual Machine) does not support scheduled or automatic calls. Every call must be kicked off by a user.

If a Governor does not have a Timelock, then proposals don’t need to be queued. They can be executed as soon as the proposal passes.