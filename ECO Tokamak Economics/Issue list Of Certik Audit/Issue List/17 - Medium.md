# **SMV-07 | Inconsistent Reward Calculation for Layer2**

| **카테고리** | **심각도** | **위치** | **상태** |
| --- | --- | --- | --- |
| **Logical-issue** | **중간** | **SeigManagerV1_3.sol#L659-L659: L659-L659** | **Pending** |

### **Description**

The `_increaseTot()` function is used to distribute rewards to various roles. At line 659, the reward calculation for layer2 is inconsistent. If it's the first time layer2 is calling _increaseTot, and the check at line 660 returns true, the reward calculation starts with `initialDebt` equal to 0. If the check returns false, the calculation starts with initialDebt equal to `(l2RewardPerUint * oldLayer2Info.layer2Tvl) / 1e18`. This inconsistency may lead to unexpected reward distribution.

```
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

```

### **Recommendation**

Ensure that the logic for `initialDebt` is consistently handled for all layer2 calculations.

## Feedback

~~Branch :  SMV-07~~

[~~commit~~](https://github.com/tokamak-network/ton-staking-v2/commit/49433fc2c00524474d01a4375e12a7c958a53d36)~~
 fix: Consistency in setting the initial initialDebt value~~

~~When layer2 first calls _increaseTot,
modify initialDebt to be set to (l2RewardPerUint * curLayer2Tvl) / 1e18.~~

**SMV-07 branch is deprecated.
→ This issue was finally reflected in the SMV-06 branch.**

[Link](https://github.com/tokamak-network/ton-staking-v2/blob/27e4f2642c9f39c14eb8e4ac56e14d8bbdc3981d/contracts/stake/managers/SeigManagerV1_3.sol#L683-L703)

—

There was an error in the previous code and it has been fixed.


- branch : [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-certik](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-certik)commit: 
- commit: [72751b6fcbeed85c35f410af117d70bf7736aeb2](https://github.com/tokamak-network/ton-staking-v2/commit/72751b6fcbeed85c35f410af117d70bf7736aeb2)
- test 
npx hardhat clean

npx hardhat compile

npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts