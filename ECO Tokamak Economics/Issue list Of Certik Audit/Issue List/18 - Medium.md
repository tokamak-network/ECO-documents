# **SMV-06 | Incorrect Reward Allocation After Unpause**

| **카테고리** | **심각도** | **위치** | **상태** |
| --- | --- | --- | --- |
| **Logical-issue** | **중간** | **SeigManagerV1_3.sol#L659-L659: L659-L659** | **Pending** |

### **Description**

The `_increaseTot()` function is responsible for distributing rewards to various roles. At line 661, the function calculates the reward tokens for layer2. When rewards for layer2 are paused and later resumed, the variable `initialDebt` is set to 0. As a result, layer2 is incorrectly allowed to claim rewards for the paused period, leading to undesired reward distribution.

```solidity
    function excludeFromSeigniorage(address _layer2) external returns (bool) {
        _onlyLayer2Manager();
        Layer2Reward storage reward = layer2RewardInfo[_layer2];
        // require (totalLayer2TVL >= reward.layer2Tvl, "check layer2Tvl");
        if (totalLayer2TVL < reward.layer2Tvl) revert Layer2TvlError();

        emit ExcludedFromSeigniorage(_layer2, reward.layer2Tvl, reward.initialDebt);

        if (reward.layer2Tvl != 0) {
            totalLayer2TVL -= reward.layer2Tvl;
            reward.layer2Tvl = 0;
            reward.initialDebt = 0;
        }

        return true;
    }

```

```solidity
    function unSettledReward(address layer2) public view returns (uint256 amount) {
        Layer2Reward memory layer2Info = layer2RewardInfo[layer2];
        if (layer2Info.layer2Tvl != 0)
            amount = l2RewardPerUint * (layer2Info.layer2Tvl / 1e18) - layer2Info.initialDebt;
    }

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

Ensure that initialDebt is correctly set when resuming rewards after a pause. The function should include checks to prevent layer2 from claiming rewards for the paused period unless explicitly intended.

## Feedback

**Branch : SMV-06**

The issuance of a specific L2 sequencer seigniorage can be stopped by the onlySeigniorageCommittee(DAO). It can be issued again, but if there is an error in setting the initial value, the code is modified.

- If L2 seigniorage is stopped, L2 seigniorage that has not yet been settled will be locked in the contract.
- When L2 issuance is resumed, seigniorage issuance begins anew.

 

 commit : **2287604**

[https://github.com/tokamak-network/ton-staking-v2/commit/2287604fd2f1575ff96852f9b16a79a51f80700c](https://github.com/tokamak-network/ton-staking-v2/commit/2287604fd2f1575ff96852f9b16a79a51f80700c)

Merge SMV-05 to SMV-06

- [commits](https://github.com/tokamak-network/ton-staking-v2/commits/SMV-06/) 

[Link](https://github.com/tokamak-network/ton-staking-v2/blob/27e4f2642c9f39c14eb8e4ac56e14d8bbdc3981d/contracts/stake/managers/SeigManagerV1_3.sol#L198-L232)

[Link](https://github.com/tokamak-network/ton-staking-v2/blob/27e4f2642c9f39c14eb8e4ac56e14d8bbdc3981d/contracts/stake/managers/SeigManagerV1_3.sol#L683-L704)

—

There was an error in the previous code and it has been fixed.


- branch : [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-certik](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-certik)commit: 
- commit: [7c0b859db3906d18a1b59cc60d8d8fc396f302bf](https://github.com/tokamak-network/ton-staking-v2/commit/7c0b859db3906d18a1b59cc60d8d8fc396f302bf)
- test 
npx hardhat clean

npx hardhat compile

npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts