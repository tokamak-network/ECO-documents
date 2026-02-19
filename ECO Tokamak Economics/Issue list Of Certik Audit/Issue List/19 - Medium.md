# **SMV-05 | Unused Minted Tokens in `layer2Manager` Contract**

| **카테고리** | **심각도** | **위치** | **상태** |
| --- | --- | --- | --- |
| **Logical-issue** | **중간** | **SeigManagerV1_3.sol#L636-L636: L636-L636** | **Pending** |

### **Description**

The `_increaseTot()` function is designed to distribute rewards to multiple entities, including the user, powerton, and the dao. However, a critical issue arises at line 636, where the function mints wton tokens to the layer2Manager contract. When the layer2Allowed variable is set to false, the minted tokens remain trapped in the layer2Manager contract, as it lacks the functionality to withdraw them. This results in an unallocated mint of tokens, creating a potential loss of funds or unintended token distribution.

```
   (rollupConfig, layer2Allowed) = allowIssuanceLayer2Seigs(msg.sender);

```

Additionally, if the layer2 address associated with each call to `_increaseTot()` is not permitted to receive rewards (as determined by the allowIssuanceLayer2Seigs function at line 614), the layer2Allowed variable will be set to false. In this case, the l2RewardPerUint value will not accrue, and other allowable rewards will also fail to be distributed. This behavior is problematic as it disrupts the intended reward distribution mechanism.

**SeigManagerV1_3.sol**

```solidity
     if (l2TotalSeigs != 0) IWTON(wton_).mint(_layer2Manager, l2TotalSeigs);

```

```solidity
        if (layer2Allowed) {
            if (l2TotalSeigs != 0) l2RewardPerUint += ((l2TotalSeigs * 1e18) / totalLayer2TVL);

            Layer2Reward storage newLayer2Info = layer2RewardInfo[msg.sender];

            if (l2RewardPerUint != 0) {
                if (_isSenderOperator || oldLayer2Info.layer2Tvl > curLayer2Tvl) {
                    layer2Seigs = unSettledReward(msg.sender);

                    if (layer2Seigs != 0) {
                        ILayer2Manager(_layer2Manager).updateSeigniorage(rollupConfig, layer2Seigs);
                        newLayer2Info.initialDebt += layer2Seigs;
                    }
                } else if (_lastCommitBlock[msg.sender] == 0) {
                    newLayer2Info.initialDebt = (l2RewardPerUint * oldLayer2Info.layer2Tvl) / 1e18;
                }
            }

            newLayer2Info.layer2Tvl = curLayer2Tvl;
            totalLayer2TVL = totalLayer2TVL + curLayer2Tvl - oldLayer2Info.layer2Tvl;
        }

```

### **Recommendation**

Add proper checks and conditions to prevent tokens from being minted unnecessarily or being locked in the contract.

## Feedback

### Commits

 [https://github.com/tokamak-network/ton-staking-v2/commit/8bebb4fe6c6238156bf42b2bb087e26a1f6b7384#diff-ebf4fe30d63d89ae85fba937fd947ef9a7099fc1d046c21bb301a8c3c03679ac](https://github.com/tokamak-network/ton-staking-v2/commit/8bebb4fe6c6238156bf42b2bb087e26a1f6b7384#diff-ebf4fe30d63d89ae85fba937fd947ef9a7099fc1d046c21bb301a8c3c03679ac)

### Related Functions

- Add startBlock in Layer2Reward struct

[Link](https://github.com/tokamak-network/ton-staking-v2/blob/27e4f2642c9f39c14eb8e4ac56e14d8bbdc3981d/contracts/stake/managers/SeigManagerV1_3Storage.sol#L8-L12)

- l2RewardPerUint is modified to be calculated based on l2TotalSeigs regardless of the state of the layer.
- Fix initialDebt at the first time 

[Link](https://github.com/tokamak-network/ton-staking-v2/blob/27e4f2642c9f39c14eb8e4ac56e14d8bbdc3981d/contracts/stake/managers/SeigManagerV1_3.sol#L683-L703)

—

This was fixed along with the commit reported in SMV-07.

- branch : [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-certik](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-certik)commit: 
- commit: [72751b6fcbeed85c35f410af117d70bf7736aeb2](https://github.com/tokamak-network/ton-staking-v2/commit/72751b6fcbeed85c35f410af117d70bf7736aeb2)
- test 
npx hardhat clean

npx hardhat compile

npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts