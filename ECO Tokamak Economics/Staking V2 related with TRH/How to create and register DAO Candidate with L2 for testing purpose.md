> [!important]
> ❗ In staking v2.5, TON Staking contract issues seigniorage to DAO candidates who are operating L2, based on amount of TON deposit, according to [the latest version of white paper](https://github.com/tokamak-network/papers/pull/23).
> - Although we have confirmed with the foundation about the latest change (where we requested to not change the definition of DAO candidate collateral, they want to have additional conversation about the change)
> - It is possible that there may be further change on this topic.

Simple staking v2.5 frontend will support DAO Candidate with L2 (who has registered their L2 information) and give them sequencer seigniorage based on bridged TON amount. This document explains how to make a fake rollupConfig address (contract info for portal, bridge, native token address, etc) that can be use to register DAO candidate with L2 for **testing purpose**. 

## Step 1. Prepare a fake rollupConfig address

> [!tip]
> 💡 Note: Instead of creating a fake one, you can deploy an actual L2 based on Tokamak Thanos on Sepolia, and use [SystemConfig](https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol) address as rollupConfig address. **Make sure to deploy using TON as L2 native token**, as any other ERC20 or ETH are not supported right now**. **

> [!important]
> ❗ We are updating the contract right now, we will announce on the tokamak-dev channel when the update is finished.

rollupConfig defines the essential information about the L2, and based on rollupConfig, which is used as basis for sequencer seigniorage that is distributed to the L2 operator. 

Create the fake rollupConfig contract through the create function of MockSystemConfigFactory.

- To create MockSystemConfig, click the [createMockSystemConfig's write ](https://sepolia.etherscan.io/address/0x5f4c9422b13dDae3B909dd96F3BB713c6eEe65Ff#writeContract#F1)button (_name is not currently supported, you can put anything right now).
  - _name: abc

![](images/c32b41df9704.png)
- You can find “mockSystemConfig” address on ‘Logs’ tab page.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/058b51f1-736c-48ec-90ba-436f963328a9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-10-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.32.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U64WZAOF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC96KzLBU8pqEHy8iGGmj%2FQ6zvyngQmcgSjRFo6FwMGXgIgbk%2B3pUPfkQLC%2F8DE1HR5iHPQro7dv5MOjf2g%2B3zky70q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGdALuUVatbniMQrBSrcA%2F9kI%2B7XApC59QXKAkHO4xUtKee2pnTnd9ZJvFx46xSSXJWG0pmdqOT6deutEucqgjkwNIBcza3sz%2BnNIk%2F%2FZyeIyEqgaroCdjQ5zKYXLhWkGzCoILYvZOGsYTUlCu4TtxP9YJsukObtEO3pYy7oqPs%2BFditm5xxQxWOQVfZ38nmdIt%2FVxR2uC5O6Y0UaY72hzxd%2BIV%2FJCYN6WVjTiutJXBHiqKcVTeKHLfAPlxijcFTy43LvLlDfKM1EUQoMMsd%2F6Fv29p%2FD4Sc62iOv2Rzh2TICSCv6CYhxoRHvyMXvHIkqKN81vpmE06WWyTg7rhitWtihGFAL99ZBcFi7FHJp1b6KOs4if%2F1xvPj7lGPmOwzmAKre5PSJbeDnP9kA5OklerBJvU%2FM1RTQL6ocQWNfxtfWeg8M5P5AsI3VKHMC6q%2FaSmQTFY9aHKyrAOa2eGEF5htvEGtME%2Bk%2B8OqJ%2BSWbloGg6dXOjB6RPMEwmtUM2%2F2A5I8zo61Gsj5W9YJZ5Ubc4jvzDxXvastMnuVtoceYC2rxxETQNeBbgKCyQxFGXLFQlSISEJyjSTHCYahoyorXsnZlpES%2FX4ET%2FCgZe4%2FkkF1DRa0AFqvH3Rx7iz6aslTaeYL5CX3SkP43InFMI%2Fv2cwGOqUBVIFoaSV0DpdoJIle%2F5TCmJqk24R2okjlbqxJ6i6Vk9bHE0XY43Q6Az1WvEmoXPNkUXH4w25SiWgkderjXvG4g6bV6FfCZIfdR6mz15gQjKo6lDnP1TnkGUaIMT0JdbJyKgxyXiubFYGPrBo%2BSSXhtM6uHoEJFvaNcoOCUP9XnUDDzrlDuasR9fcvOSq8w51polE%2BkkXrFc7MmEUrZ07Fmk7LRbre&X-Amz-Signature=bab22c3969fbe1686c00153c9fbcd55f04fb45028b3a56abd760500466aafc1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Step 2. Register rollupConfig 

rollupConfig** **address** **needs to be registered to L1BridgeRegistry using [**registerRollupConfigByManager**](https://sepolia.etherscan.io/address/0x58813D18b019F670d43be0D80Af968C99cc82c05#writeProxyContract) function (onlyOwner function). This is a permissioned function to prevent abusing sequencer seigniorage.

> [!note]
> ✔️ **R****equest rollupConfig registration to L1BridgeRegistry through “tokamak-dev” slack channel (tag @Zena).**
> Example message to send:*
> @Zena ***Request rollupConfig registration to L1BridgeRegistry**
> 
> *candidate name (this is the name that will show up on staking page): Demo stakingv2 *
> 
> *rollupConfig address: 0x95d8AA4C202D469b1A75dc1294D92e0002FD0c1b*

> [!tip]
> 💡 
> - Duplicate Candidate names are not allowed. 
> - Cannot register rollupConfig that has the same information with existing DAO Candidate with L2 (example: Titan Sepolia, Thanos Sepolia)

## Step 3. Create and register DAO Candidate with L2

> [!important]
> ❗ Make sure Step 2. is completed before doing this step.

After completing Step 2, you can create and register as a DAO Candidate with L2 ton Layer2Manager. This will create CandidateAddOn contract with rollupConfig. (You need 1000.1 TON to create and register Candidate with L2)

1. Make sure you have at least 1000.1 TON. You can use faucet to get [TON for testing on Sepolia](/0ef21581cb544875b2c919593dbc8325#17a4544ca9d04d5591188eeae10d429f).
1. [Approve TON ](https://sepolia.etherscan.io/address/0xa30fe40285b8f5c0457dbc3b7c8a280373c40044#writeContract#F2)for use by Layer2Manager
  - spender: 0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b 
  - amount: 1000100000000000000000

![](images/1b61f39409a7.png)
1. [C](https://sepolia.etherscan.io/address/0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b#writeProxyContract#F5)[reate and register as a Candidate with L2](https://sepolia.etherscan.io/address/0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b#writeProxyContract#F5) to Layer2Manager
- rollupConfig: *(*[*rollupConfig*](/10ad96a400a38051a8c4f9755c62f179#113d96a400a380429e9ec6d33ccccf97)* used during step 2)*
- amount: 1000100000000000000000
- flagTon: true
- memo: * (*[*candidate name*](/10ad96a400a38051a8c4f9755c62f179#111d96a400a380b7a62dfbaba8d19a9b)* used during step 2)*
![](images/2e0365453c6f.png)

## **Step 4. Check that registered Candidate with L2 shows up as DAO candidate**

After completing this procedure, check that the Candidate with L2 you registered appears on the

1. [Sepolia version of Simple Staking v2.5 webpage](https://simple-staking-v2-one.vercel.app/staking) 
1. [Sepolia version of Tokamak DAO](https://sepolia.dao.tokamak.network/#/election).
- If it is not shown within 30 minutes, please contact Jason 
- Please note that “Withdraw to L2” feature is not fully supported right now for newly added DAO candidate with L2