1. Deploying Uniswap v3 in Arbitrum by the deployer
  1. [https://arbiscan.io/address/0x6c9fc64a53c1b71fb3f9af64d1ae3a4931a5f4e9](https://arbiscan.io/address/0x6c9fc64a53c1b71fb3f9af64d1ae3a4931a5f4e9) 
  1. Transfer ownership: Uniswap v3 deployer on Uniswap v3 proxy admin - [https://arbiscan.io/tx/0x5636bbb6e385bfb1f30ca45ff61285e9db2bd6e05580440ac778e7df4ee7d77e](https://arbiscan.io/tx/0x5636bbb6e385bfb1f30ca45ff61285e9db2bd6e05580440ac778e7df4ee7d77e) 
  1. New Owner (**This is the aliased address of Uniswap v3 Timelock contract in L1**): [https://arbiscan.io/address/0x2BAD8182C09F50c8318d769245beA52C32Be46CD](https://arbiscan.io/address/0x2BAD8182C09F50c8318d769245beA52C32Be46CD)
1. Deployer deployed Uniswap v3 factory contract
  1. [https://arbiscan.io/tx/0xa2a1257ad6c87282cf939494e4daae37b78c372b5de25d44c7d4018265c7b0f6](https://arbiscan.io/tx/0xa2a1257ad6c87282cf939494e4daae37b78c372b5de25d44c7d4018265c7b0f6) 
1.  Uniswap used the original L1 Timelock contract address in Arbitrum without considering Arbitrum address aliasing (Miscommunication).
1. No private key for the Timelock address is available and the deployer burned the nonce, and they couldn’t deploy a contract on L1 Timelock address 
1. So, Arbitrum paused the address aliasing for a while for Uniswap to set the owner in Arbitrum
1. Change owner of Uniswap v3 factory using [setowner](https://github.com/Uniswap/v3-core/blob/d8b1c635c275d2a9450bd6a78f3fa2484fef73eb/contracts/UniswapV3Factory.sol#L54) function
  1. [https://arbiscan.io/tx/0x348d4ad88f433586dc4ce288534989f34a2ec2d95f0339ebdad9cca0eeb61a37](https://arbiscan.io/tx/0x348d4ad88f433586dc4ce288534989f34a2ec2d95f0339ebdad9cca0eeb61a37) 
  1. The new owner is 0x1a9C8182C09F50C8318d769245beA52c32BE35BC 
  1. It is the Uniswap V2: Timelock Contract address in L1 - [https://etherscan.io/address/0x1a9C8182C09F50C8318d769245beA52c32BE35BC](https://etherscan.io/address/0x1a9C8182C09F50C8318d769245beA52c32BE35BC) 
  1. So the owner of the v3 factory changed from deployer to Uniswap v2 timelock contract address
  1. A new owner has been set at a later date. Address of  the owner - [0x2BAD8182C09F50c8318d769245beA52C32Be46CD](https://arbiscan.io/address/0x2BAD8182C09F50c8318d769245beA52C32Be46CD) 
  1. New owner transaction - [https://arbiscan.io/tx/0x7d42d3755ada7791d93dec1649d2aabc4a9dbb3abde46c04ae89d8983be55ee4](https://arbiscan.io/tx/0x7d42d3755ada7791d93dec1649d2aabc4a9dbb3abde46c04ae89d8983be55ee4) 

Proposal Approved —>  Timelock —>   Timelock contract initiate the retryable ticket —> Ticket mentions the details of v3 factory contract, and call data. 

V3 factory contract has an owner set by the timelock address in arbitrum

Uniswap timelock in Ethereum - [https://etherscan.io/address/0x1a9c8182c09f50c8318d769245bea52c32be35bc](https://etherscan.io/address/0x1a9c8182c09f50c8318d769245bea52c32be35bc) 

[https://arbiscan.io/tx/0x7d42d3755ada7791d93dec1649d2aabc4a9dbb3abde46c04ae89d8983be55ee4](https://arbiscan.io/tx/0x7d42d3755ada7791d93dec1649d2aabc4a9dbb3abde46c04ae89d8983be55ee4)  - Setting new owner

Execute proposal in ethereum - [https://etherscan.io/tx/0x199b729dd7871efd63e38de5139471cf3194f3306168589d4a685b1a99538728](https://etherscan.io/tx/0x199b729dd7871efd63e38de5139471cf3194f3306168589d4a685b1a99538728)

[https://arbiscan.io/tx/0x39722d69370c7332a0ba49c30ed834399933c118a6296a60c31c62b69e29dbcc](https://arbiscan.io/tx/0x39722d69370c7332a0ba49c30ed834399933c118a6296a60c31c62b69e29dbcc) Enable fee amount

Uniswapv3 deployer in arbitrum - [https://arbiscan.io/address/0x6c9fc64a53c1b71fb3f9af64d1ae3a4931a5f4e9](https://arbiscan.io/address/0x6c9fc64a53c1b71fb3f9af64d1ae3a4931a5f4e9) 

Transferring Ownership to Proxy Admin - [https://arbiscan.io/tx/0x5636bbb6e385bfb1f30ca45ff61285e9db2bd6e05580440ac778e7df4ee7d77e](https://arbiscan.io/tx/0x5636bbb6e385bfb1f30ca45ff61285e9db2bd6e05580440ac778e7df4ee7d77e) 