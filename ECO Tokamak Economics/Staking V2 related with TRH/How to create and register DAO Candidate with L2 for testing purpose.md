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

![](images/8430e06c6c23.png)
- You can find “mockSystemConfig” address on ‘Logs’ tab page.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/058b51f1-736c-48ec-90ba-436f963328a9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-10-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.32.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVBWSNOG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqCHHcIo4hIgtwL83GuiZ0CJiQh0Wy%2BiiTI%2F%2BSw75eVgIgfvBs9b%2FjSG9CU1zS70nP3jhjJ9oBic%2FiQo%2B5Bz17mqwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDPkTdlX6%2FOeREveGfircAyo212dMNLhA3Sm3EDNnSeXLwEUox3z%2FCd3xCNwKNlcWHjK03BmCepB5nbsJhPcSTlBG6LJDOCex%2Fl3joyAXL8thSRkTzL4dQdnSQNsvs%2FVsW3HJsR1a7gHoXllP1bakk%2FwQlnrwnIQZ6ULZy4tAcLSyoyFJvLFmd2ydU2zIShLXtGX5lYK93fXJy%2BBQMAR%2FXHEGP02RibkFTzZyjkY2RsVao1%2BudbRfD51PRVG1rdQHJ9%2BT0z%2B%2F7VQz%2FIdU5x60rMe2kH57l4Dd3FTonlRXFoKiv29bRm6Ju7JWBDimu1ezBthM137gBKJ0K%2BagALkoayigQ8r8BpPSwM8HpafNWMX19mXfP0f7D3ciFObTmQr%2BDK6wZIYnuGSIgFd52s2ohZUc2ES40bt228jOodjuwo56Fv7do0HRFD07u%2BUbYtD9ASX6%2BWSpcoE9RFkksWRQHQPwdNNIGbJ5ry7FKIi3OMgc3W36QxtqVmQk8x5pgnkoPcstmMkVSuwZ%2BO9JzCgvcaNdf1Bj%2BupcNwjX%2BjS5k4v5kvq%2FraeqiKvKQA1Lb3cOoeU8TY%2BlIz4sYkfucrn4ETKjoXG9r8r7HdL3NLTeO%2B%2BIYsbh%2FooMul4%2BMfwCFlaAfba2UY%2BfCjbPG3%2BBMNyZ28wGOqUBQRtzGuXWaHFHgBi%2FAmYh8SQXoQw6iDF1O2p%2F6TvpowMrQZbEOc3GaEMZOlC4ry9pTq%2FWmxBOr0NE0avtTIfPYPKaSndUdcOiq%2Ff0axLaDC08DS3vW%2BfteBH6sNTarcHXdcfgfnUsP2QJEHlbm2QJrofT%2BQ5pMoiAswPKzd5O4eV%2Fzv0CLLCY%2F%2FoRJiy3UMDntawrolZUOIPzLQJiNeSMDYRDl43l&X-Amz-Signature=30faae242d31baa3fb03346491d8f671eff579b4f4dcc87a2bd6e03bdc79f223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](images/4a7d2b6af748.png)
1. [C](https://sepolia.etherscan.io/address/0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b#writeProxyContract#F5)[reate and register as a Candidate with L2](https://sepolia.etherscan.io/address/0x0fDb12aF5Fece558d17237E2D252EC5dbA25396b#writeProxyContract#F5) to Layer2Manager
- rollupConfig: *(*[*rollupConfig*](/10ad96a400a38051a8c4f9755c62f179#113d96a400a380429e9ec6d33ccccf97)* used during step 2)*
- amount: 1000100000000000000000
- flagTon: true
- memo: * (*[*candidate name*](/10ad96a400a38051a8c4f9755c62f179#111d96a400a380b7a62dfbaba8d19a9b)* used during step 2)*
![](images/251b474a1a5c.png)

## **Step 4. Check that registered Candidate with L2 shows up as DAO candidate**

After completing this procedure, check that the Candidate with L2 you registered appears on the

1. [Sepolia version of Simple Staking v2.5 webpage](https://simple-staking-v2-one.vercel.app/staking) 
1. [Sepolia version of Tokamak DAO](https://sepolia.dao.tokamak.network/#/election).
- If it is not shown within 30 minutes, please contact Jason 
- Please note that “Withdraw to L2” feature is not fully supported right now for newly added DAO candidate with L2