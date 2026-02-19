#323 **EOA Can Be Set as MultiSigWallet in DAOCommittee_V2.sol**
**Reporter: Suhyeon**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/323](https://github.com/tokamak-network/ton-staking-v2/issues/323)

Summary : Add the code after the zero address check

```bash
require(_multiSigWallet.code.length > 0, "Must be a contract");
```

Severity : **Low**

#324 **Misleading Function Name in DAOCommittee_V2.sol**
**Reporter: Suhyeon**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/324](https://github.com/tokamak-network/ton-staking-v2/issues/324)

Summary : Function named _validateSignatures (plural) but validates only one signature, causing confusion, So Change the function name **_validateSignatures** to **_validateSignature**

Severity : **Info**

#325 **Signature Length Validation Inconsistency**
**Reporter: Mehdi**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/325](https://github.com/tokamak-network/ton-staking-v2/issues/325)

Summary : Inconsistent signature length validation between `_validateSignatures` and `_recoverSigner` functions creates potential for unexpected behavior and gas waste. The initial validation allows signatures longer than 65 bytes, but the recovery function strictly requires exactly 65 bytes.

Severity : **Low**

Reason : This part wasn't a security issue, but rather an increase in gas efficiency.

#326 **Gas Inefficient Signature Parsing Implementation**
**Reporter: Mehdi**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/326](https://github.com/tokamak-network/ton-staking-v2/issues/326)

Summary : The signature parsing in `_validateSignatures` uses `BytesLib.slice()` which creates unnecessary memory allocation and copying, leading to higher gas costs.

Severity : **Low**

Reason : This part wasn't a security issue, but rather an increase in gas efficiency.

#327 **Potentially CRITICAL: Signature Replay Attack Vulnerability in ERC-1271 Implementation**
**Reporter: George**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/327](https://github.com/tokamak-network/ton-staking-v2/issues/327)

Summary : The hash value and signature value are passed repeatedly.

Severity : **High**

Reason : EIP-1271 is helpful for studying and understanding the relevant part in more depth, although the hash and signature that originally passed verification with the view function will continue to pass verification.

#329 **MultiSigWallet Integration and ERC-1271 Implementation Issues in DAOCommittee_V2**
**Reporter: Zena**

Link : [https://github.com/tokamak-network/ton-staking-v2/issues/329](https://github.com/tokamak-network/ton-staking-v2/issues/329)

Summary : There is a phenomenon in which the policy of signing in SafeWallet does not match the policy of signing in MultiSigWallet, causing the policy of MultiSigWallet to collapse.

Severity : **Medium**

Reason : Although there were no issues with the code, it was recognized that there were parts that did not comply with the DAO policy, so it was rated Medium.

| **Priority** | TOTAL | Each TON |  |
| --- | --- | --- | --- |
| HIGH | 100 | 100 | 1 (George) |
| MEDIUM | 50 | 50 | 1 (Zena) |
| LOW | 45 | 15 | 3 (2 Mehdi, 1 Suhyeon) |
| INFO | 5 | 5 | 1 (Suhyeon) |
| TOTAL REWARD | 200 |  |  |

# Reward Tx

- George : 100 TON (HIGH - 100 TON)
  - tx : [https://etherscan.io/tx/0xa71f39c36bad4989bab52ebeb0e9ea49e8cc11f6eeb1edbfec40fb52e0a34fb2](https://etherscan.io/tx/0xa71f39c36bad4989bab52ebeb0e9ea49e8cc11f6eeb1edbfec40fb52e0a34fb2)
- Zena : 50 TON (MEDIUM - 50 TON) (해당 리워드는 다시 프로젝트에 반납)
  - refund tx : [https://etherscan.io/tx/0x200898b4f78d35e2e19df94ed58a92a95186058ae4cdc17e76c499f05f4bdf8e](https://etherscan.io/tx/0x200898b4f78d35e2e19df94ed58a92a95186058ae4cdc17e76c499f05f4bdf8e)
- Mehdi : 30 TON (2 LOW - 30 TON)
  - tx : [https://etherscan.io/tx/0x884a044a0beffc153e33fa1e4031fe68de812a88d599da8186c14ab189db2efd](https://etherscan.io/tx/0x884a044a0beffc153e33fa1e4031fe68de812a88d599da8186c14ab189db2efd)
- Suhyeon : 20 TON (LOW - 15 TON, INFO - 5 TON)
  - tx : [https://etherscan.io/tx/0x14df50efe667c4fbcb5da7ae7bbf9743c748384413fd2b55c4ebaf0db6cb1eb6](https://etherscan.io/tx/0x14df50efe667c4fbcb5da7ae7bbf9743c748384413fd2b55c4ebaf0db6cb1eb6)