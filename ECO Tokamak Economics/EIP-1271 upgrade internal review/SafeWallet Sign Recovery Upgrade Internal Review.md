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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f87033dd-7ef0-4ccb-b751-f299368339d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AHISH5I%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCds%2BlZqPUOx52wgpi5NeOLsKwkkIrcpRxLOD0WNYX%2BVQIhAJ%2B701yHoKD59%2FIEpK521J5KtIcntP09DTHFRX6ceeD6Kv8DCHoQABoMNjM3NDIzMTgzODA1IgzK%2FDMD9MDAYn7MUCsq3AOodtI2sf1q93lhz5d%2FPKejo8uAcBG2BxEjl5FzTOp%2BBPVnLAM4r5oLU4SL6mvVKo8FtAeWC52TZf0KQu81z5z5ab8mwq8NwN6jJ6J%2BxgF50l0HNsn73HlFt3e6qufD75VZd7HicSdqxbTbhsPmMvc8lIu3W46pl62h3irjHVQqmoENMxqXMhrni315RIYRKJra6Hpl%2FnS0wc0xKcy%2FXZ2xbH7tireC7neLHpFh%2BtJHRpuou4GxXXOX%2FjYoPdOvJka8wodxTD0MWFzB5MbDL6mDP4iwpq9jzTeGIo%2BPLF3HJyeALLjKVMuwqbblnxo45YquQTJktw3G9sekLuJqgLDY2rA1sDmOKyMVB%2FZGvYnwed3C9ioHDsUd4r3d6yblKdpkAvtWeqOEnnVsqEsuAuMZUUkGu4uSfJpckAymYrYt9jRUVqG7noBqDFqUgEiKCRzFFtWVtgIyi4aGjZnmHPkGv3lj2U%2B%2FncU9z4GCnXS0RgbLWEYutqMRLAQTPuz8O732vCvZkxgTXP503Fo9r65ivw0uDMWK3AF5zfxAa7b066bNcVdVOzX%2FiCj2uSceEE8VO3mCqtJ%2FQfSnJjuJSRNnUT9VIezje9Wzb2mCJv5IWYSRZv1VjuWpPgfkqTCnmdvMBjqkAYsAliaq2R7ysCc4n7l8ZqLYtCIa2R0iRw4nlDB5Iks%2BWUf1eo62nrikrOALzJFvW%2BK27C0fW6XRA6njpG%2BVrfyRPXEu0GaiiygH%2BgsiKXS3h0scBiTwel61YMpHPHWt2wFQgDfdcrP%2FUhj2W9fwr5xYq6kKfkNO0Tcd%2F1%2FzSwtc%2BZ9XLgFqegzSta4ods5tIvOjX5mtYjmkagyqVyTqFOfinf0z&X-Amz-Signature=b431fcdc78234f523bcff625988a17981754567a86928f2084742ae7eefd96d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](images/401594786146.png)