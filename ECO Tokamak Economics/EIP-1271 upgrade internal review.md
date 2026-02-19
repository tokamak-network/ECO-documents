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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6e4d958c-f04c-45ff-b967-5373e9d3a960/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T52E73QK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEc6FD%2BKTxiLZ1WrsmIEvVu8BD%2B19p6hRY5VYKO3vceCAiB6PXhV0AeJGeObN5kjsZ8y7s2V2NHERtHxos2jcklK2ir%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIM1T8EN57Sjh1fnt3tKtwDrNn7ihS35CN4q95jF%2B6jNvr12HHkaQ9eK1myuKz028dzHKdnu1%2FFu0A763sqpooccECSq%2F7kIe4iBY2B0seoglxsCh3a%2Fd7tKJlf6E2YiY%2BdEbCJIjJSXVOxMzbok8nWy410wSDS6bB0MC7fOTfRhYWLaFoocbsaVpfT3XdI8C59etgebl6Dgl%2B%2Fq3dpNE%2BdCNyiAcjZZVTNWrP%2Br17naMGhZeuXvekjkZUmoOlBhbD%2FcP3aPHHGfK%2B2IKNEipQuUGvRndKkM8VSSNSpOnnBA%2BaYXMg4mKcmL7Ytugdyz6F74Z4wrbCElLRlD6EJXoOJgarVF7uzPIvmvbDcJWyXxWHi0cvrD3o867MqJK9aAflmjOkf2sY0cdz2F7CR7s66OhOtks5PAlucj%2BH2az6CPVy77wR9r7V7JoChACqhY%2F%2FlHDatjmyYr4vQYsaFVDYGqGMC3PVvSFm0pvZbgn0SLETgI2J%2BVsPcVuKqtdwMJOva1%2FobY2gPQw49DZc75ZhCQw%2Bh5cxVbSvVp01z%2FRYdLlwqTF3FVadFTeUvL6YlLM%2BgNtwh9f4DmfWx7biSwmZDHOL14r5XB47SuEG19pszLnQdF8pZlQDGb2IwINJiM58kVp52eZW8j7lIvCowqsTazAY6pgGrXe74nsXpqjeE0ErXhbPoPfk2DH1bvR8OKg4hTmqnZ1gDJVz0mPNBUIcS%2FcsndLJGaJo7xL3S535387P0tLaGhnfROFKTZiUEiQ2MEfjzCXzEILsnNRBn%2FKWWAhavH93dSd9lICNYYNcmX%2B6BkKrCz1C3q3IPq%2F8kEyXCuNk1BNXOkto63ld5MspZxAgV7kGkNpf8Z8UkVMIjkeA9dSLTBz3%2F10SQ&X-Amz-Signature=344452d9ac4486005647e97d3d65b75a3527ba59985104b27c27d0b7243d6489&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[[Internal Review Report]]