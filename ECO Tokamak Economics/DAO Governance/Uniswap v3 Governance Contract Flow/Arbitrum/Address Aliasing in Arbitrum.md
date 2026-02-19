Important Takeaway : 

a. Uniswap Timelock Contract Address on L1 -  0x1a9C8182C09F50C8318d769245beA52c32BE35BC

b. **Uniswap Timelock Contract Address on Arbitrum after address aliasing** - 

0x2BAD8182C09F50c8318d769245beA52C32Be46CD

1. [https://gov.uniswap.org/t/consensus-check-fix-the-cross-chain-messaging-bridge-on-arbitrum/18547](https://gov.uniswap.org/t/consensus-check-fix-the-cross-chain-messaging-bridge-on-arbitrum/18547) 
1. **Arbitrum Address Aliasing** - [https://docs.arbitrum.io/how-arbitrum-works/arbos/l1-l2-messaging#address-aliasing](https://docs.arbitrum.io/how-arbitrum-works/arbos/l1-l2-messaging#address-aliasing) 

### Background

1. **Uniswap Governance:**
  - Uniswap uses a suite of smart contracts on Ethereum (L1) for its governance. UNI token holders can propose and vote on changes to the protocol.
1. **Cross-Chain Deployment:**
  - Uniswap is deployed not only on Ethereum but also on other chains like Polygon, Optimism, Celo, and Arbitrum. These deployments are managed through governance proposals passed on Ethereum.
1. **Cross-Chain Governance:**
  - For these deployments to receive governance instructions from Ethereum, there needs to be a way to pass decisions from Ethereum's L1 to the other chains (L2s).

### Problem on Arbitrum

1. **Address Aliasing:**
  - Arbitrum initially planned to let Ethereum addresses directly control contracts on Arbitrum with their L1 identity preserved. However, they switched to using "address aliasing" for security. This changes how L1 addresses appear on L2.
1. **Misconfiguration:**
  - When Uniswap deployed its contracts on Arbitrum, it set the owner of the Uniswap V3 Factory to the L1 Uniswap Timelock address without considering the address aliasing.
1. **Ownership Issue:**
  - The unaliased address on Arbitrum, supposed to be the L1 Timelock, is actually an externally owned account (EOA) without a private key. This means no one can control the governance of Uniswap's contracts on Arbitrum.
1. **Deployment Error:**
  - The governance deployer on Arbitrum burned the nonce for deploying a contract to that address, which means it’s impossible to deploy a new contract to take control of the address.

### Solution

1. **Disable Aliasing Temporarily:**
  - Arbitrum will temporarily disable address aliasing for the L1 Timelock address (`0x1a9c8182c09f50c8318d769245bea52c32be35bc`) to allow a governance action to be correctly executed on Arbitrum.
1. **Ownership Transfer:**
  - Once aliasing is disabled, Uniswap’s governance will send a cross-chain message from the L1 Timelock to the L2 Uniswap Factory to set its owner to the correct aliased address (`0x2BAD8182C09F50c8318d769245beA52C32Be46CD`).
1. **Address Alias Calculation:**
  - The new owner address is calculated by adding a specific offset (0x111) to the original L1 address. This means the aliased address will have control over the contract.
1. **Re-enable Aliasing:**
  - After the ownership transfer is completed, Arbitrum will re-enable aliasing, ensuring the governance flow is secure and operational.

### Conclusion

- **Functional Governance:** Once this fix is implemented, Uniswap will be able to manage its Arbitrum deployment through its governance process on Ethereum, allowing for decentralized control over protocol changes.

### Learning Points

- **Technical Adaptation:** Projects must adapt to changes in blockchain infrastructure and coordinate with teams managing these infrastructures to ensure functional deployments.
- **Importance of Security:** Address aliasing was implemented for security, demonstrating the need to balance functionality with security measures in cross-chain deployments.