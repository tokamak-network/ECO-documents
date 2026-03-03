[[SafeWallet Sign Recovery Upgrade Internal Review]]

# **Basic Info**

- Project codename: ECO
- Review branch link: [GitHub - tokamak-network/ton-staking-v2 at DAO-ERC1271upgrade](https://github.com/tokamak-network/ton-staking-v2/tree/DAO-ERC1271upgrade)
- commit hash: [4a51c2ea6e4d499ca35c6cb77ba8e1a7ca5543ca](https://github.com/tokamak-network/ton-staking-v2/commit/4a51c2ea6e4d499ca35c6cb77ba8e1a7ca5543ca)
- Expected review duration (# of business days): 8 days 
- Review completion deadline (YYYY-MM-DD): 2025-08-26 ~ 2025-09-02
- Development Background Explanation
  - https://www.notion.so/tokamak/EIP-1271-feature-upgrade-to-DAO-contract-246d96a400a3803b92ded29124858fa0 

# **Audit Scope**

- Contract Scope
  - [https://github.com/tokamak-network/ton-staking-v2/blob/DAO-ERC1271upgrade/contracts/dao/DAOCommittee_V2.sol#L156-L252](https://github.com/tokamak-network/ton-staking-v2/blob/DAO-ERC1271upgrade/contracts/dao/DAOCommittee_V2.sol#L156-L252)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/DAO-ERC1271upgrade/contracts/dao/StorageStateCommitteeV3.sol#L6](https://github.com/tokamak-network/ton-staking-v2/blob/DAO-ERC1271upgrade/contracts/dao/StorageStateCommitteeV3.sol#L6)
- Function Scope
  - isValidSignature(bytes32,bytes) returns (bytes4)
  - _validateSignatures(bytes32,bytes) returns (bool)
  - _recoverSigner(bytes32,bytes) returns (address)
  - setMultiSigWallet(address)
- Storage Scope
  - address public multiSigWallet

# Implementation Development

## 1. Development Overview

Currently, in the TON Staking V2 system, the DAO Committee owns the MultiSigWallet Contract. Utilizing this structure, we plan to implement signature verification functionality compliant with the EIP-1271 standard, supporting features such as off-chain ordering, metatransactions, and delegation of authority.

## 2. Current DAO System Structure

- DAOCommittee_V1: Main DAO contract
- MultiSigWallet: Multi-Sig wallet set as the DAO owner
- Owner Structure: Structure where multiple owners submit and verify transactions

## 3. EIP-1271 Implementation Plan (MultiSigWallet-based Signature Verification )

This method verifies messages individually signed by MultiSigWallet owners by concatenating them together.

- Advantage: Leverages the existing MultiSigWallet structure
- Advantage: Owner authorization management is already handled by MultiSigWallet
- Advantage: Maintains consistency with the existing security model

## 4. Technical Implementation Details

### Signature Verification Logic

1. Extract the signature from the concatenated signature
1. Recover the signer address from the signature
1. Verify that the signer is the MultiSigWallet owner.

# Review Focus Areas

### 🔴 **High Priority**

1. ECDSA Signature Verification Security
1. MultiSigWallet authorization verification logic
1. Reentrant attack vector
1. Signature length and format verification

### 🟡 **Medium Priority**

1. DoS prevention
1. EIP-1271 standard compliance
1. State variable storage security
1. Access control consistency

### 🟢 Low Priority (Nice to Have)

1. Code readability and documentation
1. Improved error messages
1. Gas efficiency

### **Known Issues/Limitations**

1. Single-signature verification limitations
1. Ethereum Signed Message format fixed
1. MultiSigWallet contract dependency
1. Design constraints that require MultiSigWallet to have the Admin role
1. Failure to implement signature reuse prevention

# How to Test

- execute Sepolia Local Node 
```solidity
npx hardhat node --fork https://sepolia.infura.io/v3/{YOUR_INFURA_KEY}
```
- run the Test
```solidity
npx hardhat test test/erc1271-test.ts --network local
```
- Result
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6e4d958c-f04c-45ff-b967-5373e9d3a960/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LF4567Y%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBBxL6XftMGJm%2Fl7oBg3AgKXNF5x2HOoFxf2lEA2uz8uAiBzsysPBDEpXayloPj0q0PWVbefGoe5oXnANZBbIWPFoyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMQU1CXIH%2FHYOH8lvSKtwDyfqPphxFvEox6Jovkbjhb0qFKZiHUf02nvwOktutzHmUGm%2BnMY5MbbM0KooTnxTMGhAPdljkDw6H%2BAWu2j%2BuYa5nBQxJHXFtfowfIr39Uf0K8thVZXH0gkG8eAVNjZ5UOjYTcJD1RAmgOieOtHneABn4f%2FUVah0k4TcKq%2FDAWXC1vNr%2Bqzx5%2BLCtVt1%2BfyeAVuUNV0jWumgSiPjHhIygH%2FoqEgs2fPb77OQ8l5T4apfV9Og6pJVsJl7bH%2F7uW9uPgdbUNDSqGvSgryaeBOIVHGKH9ooc8w6GCsWrNVhS0juKQRSJvpMuhyZfhL6%2BVLEdiD2zWcej870gxTqTD4KdxsZKg4eBQFt%2Fyjf9b9BxdSNPnxW4ow7cGorynSYRe5nBQkw12a8rBZBndyDe%2BmTa7MEFxFRYyYrwLHQxesYN0OQ9y4K6C0B5vURbwkyhRx4QvnGNMouAj0w%2FrLdAasdkKLkhnCyZ4ngHjPQUo7waZWOwTUCnbLFfpYUc1NStxmOlG7ZkvHCSsrc2IRpTiLpTa%2FSqPy8WytCMCSrFLzGNOvd8MBu6u8u%2F4s%2BbMMNcKOFg%2FVDg8C1KMkfSTV%2BRjOalryz2oZ4JmhbSiAkvMHv9LvmLwvjGvMLFhwXGeT4wx5jbzAY6pgHuT3toCzDCtluSXQAi3gXTC%2BGHymGNKKlfbLlZOVM3%2BP5fTXbPG4wD0RLwRTHspW%2BUcaNONNazbLtJnSDr5S77wEXuW4KO1xX7q10dpeCSadYaQXe1jitIufWqSqD19xu8QHDA1kGqf%2FQP%2BO9GIXtX9sLGb3bDYmQjJef8htx9BIVNKIPK%2FcvZsnjycqW79%2Fl2Qd9GLFtF8uSPjpjb7%2Ffnsul7WngW&X-Amz-Signature=064bc0117dbd0e3c58f16188aa962fb9870d2927c82d1037ad44995a4bbcd51a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[[Internal Review Report]]