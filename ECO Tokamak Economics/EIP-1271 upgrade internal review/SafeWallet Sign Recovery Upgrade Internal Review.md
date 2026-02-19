# **Basic Info**

- Project codename: ECO
- Review branch link: [https://github.com/tokamak-network/ton-staking-v2/tree/safeWallet-protocol](https://github.com/tokamak-network/ton-staking-v2/tree/safeWallet-protocol)
- commit hash: [b4649418d487ded0343a5f3ae3721852985a12eb](https://github.com/tokamak-network/ton-staking-v2/commit/b4649418d487ded0343a5f3ae3721852985a12eb)
- Expected review duration : 7 days 
- Review completion deadline (YYYY-MM-DD): 2025-09-24 ~ 2025-09-30
- Development Background Explanation
  - https://www.notion.so/tokamak/Development-Background-276d96a400a3806fa6cadd466b246890

# **Audit Scope**

- Contract Scope
  - [https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/DAOCommittee_V2.sol#L156-L319](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/DAOCommittee_V2.sol#L156-L319)
  - [https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/StorageStateCommitteeV3.sol#L8](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/StorageStateCommitteeV3.sol#L8)
- Function Scope
  - isValidSignature(bytes,bytes) returns (bytes4)
  - _validateSignatures(bytes32,bytes) returns (bool)
  - _recoverSigner(bytes32,bytes) returns (address)
  - encodeMessageDataForSafe(bytes) returns (bytes)
  - domainSeparator() returns (bytes32)
  - getChainId() returns (uint256)
  - _isDuplicate(address[], address, uint256) returns (bool)
  - isOwner(address) returns (bool)
  - setMultiSigWallet(address)
- Storage Scope
  - address public multiSigWallet

# Implementation Development

## 1. Development Overview

In the current TON Staking V2 system, the DAO committee owns the MultiSigWallet contract. Leveraging this structure, we plan to implement signature verification functionality that allows one of the SafeWallet owners to be assigned to the DAO contract, supporting features such as off-chain ordering, meta-transactions, and delegation of authority.

## 2. Current DAO System Structure

- DAOCommitteeProxy : Main DAO Proxy Contract
- DAOCommittee_V1: Main DAO logic Contract
- MultiSigWallet: MultiSigwalletContract set as the DAO owner

## 3. MultiSigWallet-based Signature Verification Implementation Plan 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f87033dd-7ef0-4ccb-b751-f299368339d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ATWB2LW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FBzxG4zUtr3aRMYC872fkuik4p2o%2BG1OXO4qsd%2BiljwIhAJcfVJPwGPqU%2F%2FTkKaFt2Uhuk0iGkreVCMeQ7sAQ8TYfKv8DCHQQABoMNjM3NDIzMTgzODA1IgySb02xN0JdsYnDuEMq3AN0wi1oORWUQcmcuf%2Bg%2BIYSL8e868RHJ0NSzK%2FSO9OP7jmlqxVPk1ilKafBTAuOkp%2Fr6v0TJDoCrPdg0qg%2Fnzlvj%2FqESpu%2FEBXzk4w4TQda2TFr3GF4aKThYSgtbZBlK4hTB2mFDZp6cepVPHyhpEDQiC%2BOvh1f6eQo4Y6ulW4zaSyKSqjU7Jm8kfLKcGo7rPeuzyqNQ2l%2FWeXNPG5oOmOT4kFzDYMmKqzVtNuHyAGxCkuEN3a8cvlVJsLHgRsV46dQfwchBSPiODs2LVrgLEItfOPNIGlW8yVDtoiR8aZSJKPjkxh3DpL0dldWMRwK1lJaoVPuwdpOXI0aivwwAXl7WKAPpMxRKkJdLJ6s9gT5qjTrAUYy6Y%2FKQdZ4H7r8LM6ugF9WLWzwbYwGyg9snPfmVx%2FYjcFe7AYfmlyavg0cQLdx0DksoZ2N%2F61kE9mAbuybbY0bWPoH9F9VXl8r9PhUBFqm5uxKzupR1fbCqiStIpszfpt30DXptEAulSUdCVbNLziW8yvjquY9GZ0%2Fi4M7hQYWCCRg%2BfFtq8UEsLZuOzhM6zveaJ80U%2FWXYamLNa%2F36HPsmWYTbXj68UQnRYTUveMpDb7B4rBeHjmEEcVARN4N%2FHKwKkqDXBJDdTDP8dnMBjqkAc9YpCKQPjcHwvH2rhOioSSurSokaTElyvs4DZmrpnFer1fm%2FIgQCrQWz%2FyDHQwM%2F%2FdmZvrZJTle1MwfEGdEbtIffox8XS7nkNL1sIguO7P7HNShsPyaNMQWOmCP2HCQfZt0MvZM%2FoEnXeD3q1gdy9zcOw8f8V706CaAc%2BYdByzhEMcdjM8Ev1u3RxMTxoThj3fpQ0qW8XmQO8%2F9%2B6SopiktXcIW&X-Amz-Signature=0b293d37f6ed35bdd0fb4fbed77504cd4f3712e9ce1489334fcdb59e7426a32c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- One of the Owners of SafeWallet is the DAO Contract.
- The owner of the DAO Contract is the MultiSigWallet Contract.
- There are three owners of the MultiSigWallet Contract.
- The verification can be performed in the DAO Contract by having at least two out of three Owners of the MultiSigWallet Contract sign the signature of SafeWallet.

## 4. Technical Implementation Details

### Signature Verification Logic

1. Extract the signature from the concatenated signature
1. Verify that the signature was created in SafeWallet by checking the "v" value in the signature.
1. Recover the signer from the signature.
1. Verify that the signer is the MultiSigWallet owner.
1. Make sure there are at least two unique signer.
1. If there are two or more non-duplicate signers, returns MAGICVALUE or INVALID_SIGNATURE.

# Review Focus Areas

### 🔴 **High Priority**

1. ECDSA Signature Verification Security
1. MultiSigWallet authorization verification logic
1. Reentrant attack vector
1. Signature length and format verification
1. SafeWallet signature verification failed
1. Single signature pass
1. Recognize duplicate signatures as valid signatures

### 🟡 **Medium Priority**

1. DoS prevention
1. State variable storage security
1. Access control consistency

### 🟢 Low Priority (Nice to Have)

1. Code readability and documentation
1. Improved error messages
1. Gas efficiency

### **Known Issues/Limitations**

1. The valid number of signatures must pass the current MultiSigWallet policy.
1. Hash values and signatures can be reused
1. MultiSigWallet contract dependency
1. Design constraints that require MultiSigWallet to have the Admin role
1. The signer recovery method follows the SafeWallet standard, not the EIP-1271 standard.

# How to Test

- Setting ENV Value
  - Please enter the values below as Test input. (.env file)
```bash
OWNER_PRIVATE_KEY=14b80e98c2490b8224bc0e401eef8967c3fc995b6310af2ca0960e0677ae4b4a
OWNER_PRIVATE_KEY2=9a3bcbb711100af102c30d6b64b5ddedc1537c7c2ce817c5e2d00dd8aecf41e1
SAFE_SIGNER1_PRIVATE_KEY=8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba
ETH_NODE_URI_sepolia=SEPOLIA_RPC_URL
```
  - If you set only the values above and run it, an error will occur. 
  - You can comment out unnecessary parts in the hardhat.config.ts file or enter duplicate values.
- run the Test
```bash
npx hardhat test test/SafeWallet.test3.ts --network hardhat
```
- Result 
![](images/f82d2820003d.png)