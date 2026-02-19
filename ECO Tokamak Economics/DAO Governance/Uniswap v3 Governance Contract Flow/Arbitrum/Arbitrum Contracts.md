### Deployment and Initial Setup

1. **Deployment by Deployer:**
  - The Uniswap V3 contracts were initially deployed on Arbitrum by a deployer contract.
  - Deployer Address: [Link](https://arbiscan.io/address/0x6c9fc64a53c1b71fb3f9af64d1ae3a4931a5f4e9).

### Factory Contract Deployment and Ownership Challenges

1. **Deployment of Uniswap V3 Factory Contract:**
  - The deployer deployed the Uniswap V3 Factory contract.
  - Factory deployment transaction: [Link](https://arbiscan.io/tx/0xa2a1257ad6c87282cf939494e4daae37b78c372b5de25d44c7d4018265c7b0f6).
1. **Miscommunication and Address Aliasing:**
  - The Uniswap team transferred the ownership to the original L1 Timelock address without considering Arbitrum’s address aliasing mechanism.
    - The deployer transferred ownership of Uniswap V3 to the Uniswap V3 Proxy Admin.
    - Transaction for ownership transfer: [Link](https://arbiscan.io/tx/0x5636bbb6e385bfb1f30ca45ff61285e9db2bd6e05580440ac778e7df4ee7d77e).
  - This resulted in the Timelock address being unclaimed, as there was no private key available.
1. **Nonce Burn and Deployment Restriction:**
  - The [deployer had burned the nonce](https://gov.uniswap.org/t/consensus-check-fix-the-cross-chain-messaging-bridge-on-arbitrum/18547#:~:text=The%20governance%20deployer%20key%20on%20Arbitrum%20has%20burned%20the%20nonce%20that%20could%20deploy%20a%20contract%20to%20this%20address%2C%20verifiable%20here), preventing any contract deployment on the L2 Timelock address.

### Solution and Ownership Update

1. **Temporary Pause on Address Aliasing:**
  - Arbitrum paused address aliasing to allow the Uniswap team to set the correct owner.
1. **Ownership Change  to Aliased Address Using ****`setOwner`****:**
  - Eventually, the ownership was set to the correct aliased address on Arbitrum.
  - Final ownership transaction: [Link](https://arbiscan.io/tx/0x7d42d3755ada7791d93dec1649d2aabc4a9dbb3abde46c04ae89d8983be55ee4).

### Summary

- **Deployment and Ownership:** Initially, the Uniswap V3 contracts on Arbitrum were deployed and transferred to a proxy admin(L1 Timelock address).
- **Address Aliasing Issue:** Due to a misunderstanding of Arbitrum’s address aliasing, the Timelock address was not usable for governance actions.
- **Resolution:** Arbitrum temporarily disabled aliasing, allowing the Uniswap team to correct the ownership to the aliased Timelock address, ensuring proper governance functionality.