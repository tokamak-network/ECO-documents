TON Staking v2 is a development to reflect the contents of the V2 white paper, so please read the [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2) first.

V2 introduces a concept called L2 sequencer, which was not present in V1, and new content has been added to distribute a portion of the newly issued TON seigniorage to the L2 sequencer. Since V2 is a reinforced system from the existing V1 contract, if there is a contract that exists in V1, it is implemented by upgrading. Therefore, readers of this article should be familiar with the V1 system. If you want to know more about TON staking V1, please refer to this [Medium article](https://medium.com/tokamak-network/looking-into-tokamak-networks-staking-contract-7d5f9fa057e7).

# Changes in V2

## Changes in Seigniorage Distribution

In V2, the seigniorage from the issued TON is paid to the L2 sequencer in proportion to the total issuance of TON and the liquidity of TON in the L2 layer. (refer to the white paper)

S: TON staking amount

T: Total TON issuance

TON seigs: Amount of TON seigniorage issued

D: Total TON liquidity of Layer2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6e2a8516-0927-4c97-8fe1-393a9582e2b1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.49.36.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=5c8dff2a0c85caaf0b9088ceb60914314f9358d869543cbe060450c05e5565b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Distribution of V1 Seigniorage

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/367faed2-b282-46f3-b4ad-0225993e226d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.50.15.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=7ed51261c050e498436456914faf3e355cb50f54702b4042deb35e131206d51e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Distribution of V2 Seigniorage

## Addition of Layer2Candidate

In V1, there was a DAOCandidate Layer2. DAOCandidate is a Layer2 that can become a committee of the DAO.

The Layer2Candidate added in V2 inherits all the functions of DAOCandidate, so it can become a committee of the DAO and at the same time, the sequencer of Layer2 can receive seigniorage.

## Staked amount can be used as Layer2 liquidity immediately.

An added feature in Layer2Candidate is the withdrawAndDepositL2 function, which combines the unique deposit function of Layer2 with the unstaking function, allowing you to deposit into L2 while withdrawing.

The withdrawAndDepositL2 function allows you to unstake while simultaneously depositing in Layer2. The advantage of this function compared to V1 is that unstaking is possible immediately without waiting time (waiting block: .. block, about 2 weeks) after requesting unstaking. You can use the funds tied up in L1 as L2 liquidity as soon as you execute the function.

## Provides a mechanism to stop providing seigniorage to the L2 sequencer of Layer2Candidate.

The function of granting seigniorage to the Layer2 sequencer is a major authority granted in the Tokamak economy. However, if it is determined that such Layer2 is not performing its appropriate role in the Tokamak economy, the Seigniorage Committee can stop the seigniorage granted to the sequencer of the Layer2Candidate.

## You can cancel the stop of providing seigniorage to the L2 sequencer of Layer2Candidate.

The recovery of the seigniorage stop of the Layer2Candidate can be cancelled again by the Seigniorage Committee if it is judged that there is a valid reason and improvement.

# TON Stake Contracts

## TON Stake V1 Contracts

The contracts of V1 are configured as follows. DAOCandidate can be created through DAOCommittee, and once the created daoCandidate is registered through Layer2Registry and registered in SeigManager, an AutoCoinage that maps with DAOCandidate is created. AutoCoinage manages the staking amount and holds the logic for paying compound interest. Therefore, a separate AutoCoinage is created for each layer (DAOCandidate).

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/441dce2f-f4da-4ee4-91bc-580afd7df8a6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.28.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=757fbcdf8ae9cb98de0be4b255184ccee3614a072c45856c2d734ea7af7d3782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## TON Stake V2 Contracts

V2 has added Layer2Candidate while maintaining the configuration of V1. The contract configuration is as shown in the figure below. Compared to V1, it looks a bit more complex. However, you can see that the contract in blue has been added and there are no changes to the existing configuration.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/070e303e-b4d5-4dbc-a889-8b1dd711c26e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.04.54.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=fea5627b85dffff6858e5c1f9f03e0fbd7b29ab56f2d523469c117e8494b7ca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

In the Contract part below, I will explain one by one about the contract in blue.

First, you need to understand how to verify Layer2 in L1. The Layer2 we are currently targeting is Optimism Rollup. We first apply the Optimism Layer2, and the contract upgrade is made so that other layers can also be applied. Optimism Layer2 has a legacy version and a bedrock version. Remember that the initial application target is limited to cases where the L2 nativeToken is TON in the Optimism legacy version and the Optimism bedrock version. In the Optimism bedrock version, the SystemConfig contract contains information and environment settings for the L1 contract. Therefore, we will use the address of SystemConfig as the address to distinguish Layer2. In the case of the legacy version, since there is no SystemConfig, a separate legacySystemConfig contract was created. In the case of the legacy Layer2, you should deploy the legacySystemConfig contract and use this address as the address to distinguish Layer2.

# Use case

## For registrant of L2Registry

Accounts with registrant authority in the L2Registry contract can register the SystemConfig that holds unique information of Layer2. Registering SystemConfig means that you have confirmed that the Layer2 is fine. Only the Layer2 of the registered SystemConfig can be registered as Layer2Candidate. Only after being registered as a Layer2Candidate, the sequencer can receive seigniorage.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/985596ab-ea70-4120-a54a-83b21d6573ac/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.07.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=e14b964d11d7641afd06b5ba13ccd80685b12c23d3d172a8d70bf6c02bf9698d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For everyone

Anyone can register Layer2Candidate for the SystemConfig registered in L2Registry. When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer, so you must also provide TON equivalent to the minimum deposit. Currently, according to the service standard, you need to provide at least 1000.1 TON. Through the 'Register Layer2Candidate' function, the Operator, Layer2Candidate, and Coinage contracts are created.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fafadd66-1b57-4f77-8a51-018f178ea306/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.41.57.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=dd9861063640d2482e81b4ed70b5cc9032b1d74a3ed6a30c1df8233c30ab34a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For staker in Layer2Candidate

Users who have staked in Layer2Candidate can perform the function of depositing in the Layer2 while withdrawing the staked amount through the WithdrawAndDepositL2 function.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/45aec071-04e4-491f-86b3-7377a85dc221/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=7f8cd9b49a8e80680b1b5adbaa3b122857e5d512f764a638ed669a6b203a1777&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For seigniorageCommittee

Simple Staking V2 designed an economy that issues TON seigniorage to the sequencer of Layer2Candidate that operates Layer2. However, there must be a function to immediately stop the issuance of TON seigniorage to the sequencer of Layer2 if it is found that it does not actually operate Layer2 or unfairly receives seigniorage.

A seigniorage committee account defined in the L2Registry contract was created. The seigniorage committee can perform the function of stopping or cancelling the issuance of seigniorage to the Layer2 sequencer.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/68a7f248-5364-44d9-9165-a9dd06fd7908/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYC4RD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDll5IyGbEbcEyA0jLBCsyt422jOuslWmwVS6WK%2FctLhQIgLU27rs6vr89Xg93CBZSVe9leysp%2F4zg3h1ld00LQb1Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDyX7MRAmkxObBcrmyrcA8vPCYRBc7GvwgZa5HL6GkcjP99gKxxjLHQosKCDf0he0VFRRChYkjgQ0MQszTaXAIFYzQ0qNUCiZC7isrm8qM%2Bvq%2FSin%2FxqwpqHDjXpYXEUfc76QEg3dF%2FayO%2Ft8DVXS3Hue1wRLTIludjbKQT0nZwJMruJ%2BeiYj%2BJLBFws8J%2FFMzzE3VtJWHOsnIzjzWGIgxW0jVHKZ9DCzG6XCPaA9aohkwQ%2FMVfsZBgw%2FYbNrmNt2NURPPBGQOrv5XaqsT%2BImAd3RTSylrJXjFFqaaV%2Brj9w8ZhJER3DHhtslhvbA%2FTYu%2FT4siRrQtvB3OD6FSx15YLdwvRHFxvi15uy9Rwso7arVCZ5i%2F26p7hJdJnM5AzN%2FkJFyManZ92cU0JJXbXjBe%2FoKJ%2BfC6H6wh%2F9V8axPbcBRcyGFTWN7Jm4ccSjAfiAq7T7Kb5BSP3xXFOhG1JZVlfOYn6rd7jDLGt1HCDjzcBXIaUq5q7%2FAVd%2FPbXmpOdZ16ZteFXQE7Zi1QyJM5geg%2Fnm%2FV57EZ8NbbSmu4cFfQB6joyw1Wn5no0Lfui5KI22N%2FC%2BZkiJ7W4dvTpaq1g25WRSf%2Bg%2B9tjCHzhmTcIl6U5CnD4uAj8lLm8V7DM%2BU4O3mTI2nL3IVSRBxz%2FvMPOY28wGOqUB6r%2BaFAI3X4Hu759eY035emIsi8VQBdZpsRCmLXXKI1f%2BIJor9LyALf1%2F6lOWlfv7n1uO0eelgg4U4PukTuLDERjdu7yvwC3bDLbeTf8A9peEy3kOZPBlL03Oxy2%2BQAQY8PT6V5yyURyEoG6j1NpkpudMgjDsGMYvphtpnkeXm9x9pKxAzsJ9%2Fie%2F8ozRnvaUYqybRS94GSAqcNKTBPH8N9Uxop7q&X-Amz-Signature=be09650e6e0d087747012416392ebec45f03950159ac6822a0ce1151bbcee693&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Sequence Diagrams

## Register Layer2Candidate

When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer.

When registering Layer2Candidate, you must provide the address of the SystemConfig contract that holds the environment setting information of Layer2. Also, the SystemConfig you enter must be registered in L2Registry before registration. (Only accounts with L2Registry's Registrant authority can register in L2Registry.)

![Screenshot 2024-06-26 AM 10.36.58.png]([https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448)
TON Staking v2 is a development to reflect the contents of the V2 white paper, so please read the white paper first.

V2 introduces a concept called L2 sequencer, which was not present in V1, and new content has been added to distribute a portion of the newly issued TON seigniorage to the L2 sequencer. Since V2 is a reinforced system from the existing V1 contract, if there is a contract that exists in V1, it is implemented by upgrading. Therefore, readers of this article should be familiar with the V1 system. If you want to know more about TON staking V1, please refer to the respective Medium article.

# Changes in V2

## Changes in Seigniorage Distribution

In V2, the seigniorage from the issued TON is paid to the L2 sequencer in proportion to the total issuance of TON and the liquidity of TON in the L2 layer.

S: TON staking amount

T: Total TON issuance

TON seigs: Amount of TON seigniorage issued

D: Total TON liquidity of Layer2

## Addition of Layer2Candidate

In V1, there was a DAOCandidate Layer2. DAOCandidate is a Layer2 that can become a committee of the DAO.

The Layer2Candidate added in V2 inherits all the functions of DAOCandidate, so it can become a committee of the DAO and at the same time, the sequencer of Layer2 can receive seigniorage.

## Staked amount can be used as Layer2 liquidity immediately.

An added feature in Layer2Candidate is the withdrawAndDepositL2 function, which combines the unique deposit function of Layer2 with the unstaking function, allowing you to deposit into L2 while withdrawing.

The withdrawAndDepositL2 function allows you to unstake while simultaneously depositing in Layer2. The advantage of this function compared to V1 is that unstaking is possible immediately without waiting time (waiting block: .. block, about 2 weeks) after requesting unstaking. You can use the funds tied up in L1 as L2 liquidity as soon as you execute the function.

## Provides a mechanism to stop providing seigniorage to the L2 sequencer of Layer2Candidate.

The function of granting seigniorage to the Layer2 sequencer is a major authority granted in the Tokamak economy. However, if it is determined that such Layer2 is not performing its appropriate role in the Tokamak economy, the Seigniorage Committee can stop the seigniorage granted to the sequencer of the Layer2Candidate.

## You can cancel the stop of providing seigniorage to the L2 sequencer of Layer2Candidate.

The recovery of the seigniorage stop of the Layer2Candidate can be cancelled again by the Seigniorage Committee if it is judged that there is a valid reason and improvement.

# TON Stake Contracts

## TON Stake V1 Contracts

The contracts of V1 are configured as follows. DAOCandidate can be created through DAOCommittee, and once the created daoCandidate is registered through Layer2Registry and registered in SeigManager, an AutoCoinage that maps with DAOCandidate is created. AutoCoinage manages the staking amount and holds the logic for paying compound interest. Therefore, a separate AutoCoinage is created for each layer (DAOCandidate).

## TON Stake V2 Contracts

V2 has added Layer2Candidate while maintaining the configuration of V1. The contract configuration is as shown in the figure below. Compared to V1, it looks a bit more complex. However, you can see that the contract in blue has been added and there are no changes to the existing configuration.

In the Contract part below, I will explain one by one about the contract in blue.

First, you need to understand how to verify Layer2 in L1. The Layer2 we are currently targeting is Optimism Rollup. We first apply the Optimism Layer2, and the contract upgrade is made so that other layers can also be applied. Optimism Layer2 has a legacy version and a bedrock version. Remember that the initial application target is limited to cases where the L2 nativeToken is TON in the Optimism legacy version and the Optimism bedrock version. In the Optimism bedrock version, the SystemConfig contract contains information and environment settings for the L1 contract. Therefore, we will use the address of SystemConfig as the address to distinguish Layer2. In the case of the legacy version, since there is no SystemConfig, a separate legacySystemConfig contract was created. In the case of the legacy Layer2, you should deploy the legacySystemConfig contract and use this address as the address to distinguish Layer2.

# Use case

## For registrant of L2Registry

Accounts with registrant authority in the L2Registry contract can register the SystemConfig that holds unique information of Layer2. Registering SystemConfig means that you have confirmed that the Layer2 is fine. Only the Layer2 of the registered SystemConfig can be registered as Layer2Candidate. Only after being registered as a Layer2Candidate, the sequencer can receive seigniorage.

## For everyone

Anyone can register Layer2Candidate for the SystemConfig registered in L2Registry. When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer, so you must also provide TON equivalent to the minimum deposit. Currently, according to the service standard, you need to provide at least 1000.1 TON. Through the 'Register Layer2Candidate' function, the Operator, Layer2Candidate, and Coinage contracts are created.

## For staker in Layer2Candidate

Users who have staked in Layer2Candidate can perform the function of depositing in the Layer2 while withdrawing the staked amount through the WithdrawAndDepositL2 function.

## For seigniorageCommittee

Simple Staking V2 designed an economy that issues TON seigniorage to the sequencer of Layer2Candidate that operates Layer2. However, there must be a function to immediately stop the issuance of TON seigniorage to the sequencer of Layer2 if it is found that it does not actually operate Layer2 or unfairly receives seigniorage.

A seigniorage committee account defined in the L2Registry contract was created. The seigniorage committee can perform the function of stopping or cancelling the issuance of seigniorage to the Layer2 sequencer.

# Sequence Diagrams

## Register Layer2Candidate

When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer.

When registering Layer2Candidate, you must provide the address of the SystemConfig contract that holds the environment setting information of Layer2. Also, the SystemConfig you enter must be registered in L2Registry before registration. (Only accounts with L2Registry's Registrant authority can register in L2Registry.)

TON Staking v2 is a development to reflect the contents of the V2 white paper.

V2 introduces a concept called L2 sequencer, which was not present in V1. This new content adds the distribution of a portion of the newly issued TON seigniorage to the L2 sequencer. V2 is a reinforced system from the existing V1 contract, so if there is a contract that exists in V1, it is implemented by upgrading.

# Changes in V2

## Changes in Seigniorage Distribution

In V2, the seigniorage from the issued TON is paid to the L2 sequencer in proportion to the total issuance of TON and the liquidity of TON in the L2 layer.

## Addition of Layer2Candidate

In V1, there was a DAOCandidate Layer2. DAOCandidate is a Layer2 that can become a committee of the DAO. The Layer2Candidate added in V2 inherits all the functions of DAOCandidate, making it possible to become a committee of the DAO and at the same time, the sequencer of Layer2 can receive seigniorage.

## Staked amount can be used as Layer2 liquidity immediately.

An added feature in Layer2Candidate is the withdrawAndDepositL2 function, which combines the unique deposit function of Layer2 with the unstaking function, allowing you to deposit into L2 while withdrawing.

## Provides a mechanism to stop providing seigniorage to the L2 sequencer of Layer2Candidate.

The function of granting seigniorage to the Layer2 sequencer is a major authority granted in the Tokamak economy. However, if it is determined that such Layer2 is not performing its appropriate role in the Tokamak economy, the Seigniorage Committee can stop the seigniorage granted to the sequencer of the Layer2Candidate.

## You can cancel the stop of providing seigniorage to the L2 sequencer of Layer2Candidate.

The recovery of the seigniorage stop of the Layer2Candidate can be cancelled again by the Seigniorage Committee if it is judged that there is a valid reason and improvement.

# TON Stake Contracts

## TON Stake V1 Contracts

The contracts of V1 are configured as follows. DAOCandidate can be created through DAOCommittee, and once the created daoCandidate is registered through Layer2Registry and registered in SeigManager, an AutoCoinage that maps with DAOCandidate is created. AutoCoinage manages the staking amount and holds the logic for paying compound interest. Therefore, a separate AutoCoinage is created for each layer (DAOCandidate).

## TON Stake V2 Contracts

V2 has added Layer2Candidate while maintaining the configuration of V1. The contract configuration is as shown in the figure below. Compared to V1, it looks a bit more complex. However, you can see that the contract in blue has been added and there are no changes to the existing configuration.

In the Contract part below, I will explain one by one about the contract in blue.

First, you need to understand how to verify Layer2 in L1. The Layer2 we are currently targeting is Optimism Rollup. We first apply the Optimism Layer2, and the contract upgrade is made so that other layers can also be applied. Optimism Layer2 has a legacy version and a bedrock version. Remember that the initial application target is limited to cases where the L2 nativeToken is TON in the Optimism legacy version and the Optimism bedrock version. In the Optimism bedrock version, the SystemConfig contract contains information and environment settings for the L1 contract. Therefore, we will use the address of SystemConfig as the address to distinguish Layer2. In the case of the legacy version, since there is no SystemConfig, a separate legacySystemConfig contract was created. In the case of the legacy Layer2, you should deploy the legacySystemConfig contract and use this address as the address to distinguish Layer2.

# Use case

## For registrant of L2Registry

Accounts with registrant authority in the L2Registry contract can register the SystemConfig that holds unique information of Layer2. Registering SystemConfig means that you have confirmed that the Layer2 is fine. Only the Layer2 of the registered SystemConfig can be registered as Layer2Candidate. Only after being registered as a Layer2Candidate, the sequencer can receive seigniorage.

## For everyone

Anyone can register Layer2Candidate for the SystemConfig registered in L2Registry. When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer, so you must also provide TON equivalent to the minimum deposit. Currently, according to the service standard, you need to provide at least 1000.1 TON. Through the 'Register Layer2Candidate' function, the Operator, Layer2Candidate, and Coinage contracts are created.

## For staker in Layer2Candidate

Users who have staked in Layer2Candidate can perform the function of depositing in the Layer2 while withdrawing the staked amount through the WithdrawAndDepositL2 function.

## For seigniorageCommittee

Simple Staking V2 designed an economy that issues TON seigniorage to the sequencer of Layer2Candidate that operates Layer2. However, there must be a function to immediately stop the issuance of TON seigniorage to the sequencer of Layer2 if it is found that it does not actually operate Layer2 or unfairly receives seigniorage.

A seigniorage committee account defined in the L2Registry contract was created. The seigniorage committee can perform the function of stopping or cancelling the issuance of seigniorage to the Layer2 sequencer.

# Sequence Diagrams

## Register Layer2Candidate

When registering Layer2Candidate, you must deposit at least the minimum deposit amount as the operator name of the layer.

When registering Layer2Candidate, you must provide the address of the SystemConfig contract that holds the environment setting information of Layer2. Also, the SystemConfig you enter must be registered in L2Registry before registration. (Only accounts with L2Registry's Registrant authority can register in L2Registry.)

TON Staking v2 는 V2 백서의 내용을 반영하기 위한 개발이므로,  [백서](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2)를 먼저 읽고 오시기 바랍니다. 

V2에는 V1에는 존재하지 않는 L2 시퀀서라는 개념이 도입되었으며,  새로 발행되는 톤 시뇨리지의 일부를 L2 시퀀서에게 분배하는 내용이 추가된 내용입니다.  V2는 기존  V1 컨트랙에서 보강된 시스템이기 때문에, V1에 존재하는 컨트랙일 경우, 업그레이드하여 구현합니다.  따라서 본 글을 읽으시는 독자는 V1 시스템을 알고 있어야 합니다.  톤스테이킹 V1에 대해서 더 자세히 알고 싶은 분은 [미디움 글](https://medium.com/tokamak-network/looking-into-tokamak-networks-staking-contract-7d5f9fa057e7)을 참고하시기 바랍니다. 

# V2에서 변경하는 사항들  

## 시뇨리지 분배의 변화 

V2에서는  발행된 시뇨리지에서 톤의 총 발행량과  L2 레이어의 톤 유동성의 비율만큼의 시뇨리지를 L2 시퀀서에게 지급합니다.  (백서 참고) 

![V1 의 시뇨리지 분배](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6e2a8516-0927-4c97-8fe1-393a9582e2b1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.49.36.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=b00df8a4826f3566a7a7520989c7a618c6feeedc2f9979f405c4feb521c8a98e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![V2의 시뇨리지 분배 ](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/367faed2-b282-46f3-b4ad-0225993e226d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.50.15.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=1935fa3cbdefe420f3a7ce876dd6feea3a4169db149c4690a54ed5d11655a651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Layer2Candidate 추가  

V1에서는 DAOCandidate Layer2 가 존재하였습니다. DAOCandidate 는 다오의 위원회가 될 수 있는 Layer2 입니다.

V2에서 추가되는 Layer2Candidate는 DAOCandidate의 모든 기능을 상속받아 다오의 위원회가 될 수 있음과 동시에 Layer2의 시퀀서가 시뇨리지를 받을 수 있습니다.    

## 스테이킹 금액을 즉시 Layer2 유동성으로 사용 가능합니다. 

Layer2Candidate 에서 추가된 기능으로, 해당 Layer2의 독자적인 예치 기능을 언스테이킹 기능과 연계하여,  인출과 동시에 L2에 예치하는(withdrawAndDepositL2) 함수를 제공합니다.   

withdrawAndDepositL2 함수는 스테이킹 금액을 언스테이킹하면서 동시에 Layer2에 예치하는 기능입니다. 이 기능이 V1과 비교했을때의 강점은 언스테이킹 요청 후 대기 시간없이(대기블록 : .. 블록, 약 2주)  바로 언스테이킹이 가능하다는데 있습니다.  함수 실행 즉시 L1에 묶인 자금을 L2  유동성으로 사용할 수 있습니다.  

## Layer2Candidate 의 L2시퀀서에게 시뇨리지 제공 중지할 수 있는 메커니즘을 제공합니다.     

레이어2 시퀀서에게 시뇨리지를 부여하는 기능은 토카막 이코노미의 큰 권한을 부여받은 것입니다. 그런데, 이러한 레이어2가 토카막 이코노미에 적절한 역할을 하지 못한다고 판단될 경우, 시뇨리지 위원회는 해당 Layer2Candidate의 시퀀서에게 부여되는 시뇨리지를 중지할 수 있습니다. 

## Layer2Candidate 의 L2시퀀서에게 시뇨리지 제공 중지 취소를 할 수 있습니다. 

 Layer2Candidate의 시뇨리지 중지의 복구는 타당한 이유 및 개선이 있다고 판단될 경우, 시뇨리지 위원회에 의해 다시 중지취소가 가능합니다. 

# TON Stake Contracts    

## TON Stake V1 Contracts

V1 의 컨트랙트는 아래와 같이 구성되어 있다. DAOCandidate는 DAOCommittee를 통해 생성을 할 수 있으며, 생성된 daoCandiate가 Layer2Registry를 통해 등록되고, SeigManager에 등록되면서, DAOCandidate와 매핑되는 AutoCoinage가 생성된다. AutoCoinage 는 스테이킹 금액을 관리하면서, 복리이자를 지급하기 위한 로직을 보유한다. 때문에 각 레이어 (DAOCandidate) 마다 별도의 AutoCoinage 가 생성된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/441dce2f-f4da-4ee4-91bc-580afd7df8a6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.28.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=5addeb32b49abced73baff89b5c4e900eb2aed4a097159ff445bfc5cc6f367d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## TON Stake V2 Contracts

V2는 V1의 구성을 유지하면서 Layer2Candidate가 추가되었다. 컨트랙트 구성은 아래 그림과 같다. V1에 비해 다소 복잡해보인다. 그러나 파란색 부분의 컨트랙이 추가되었고 기존 구성에는 전혀 변경사항이 없음을 알 수 있다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/070e303e-b4d5-4dbc-a889-8b1dd711c26e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.04.54.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=59c027e3c3670b7d496e6bf6994fd870dfa524397cdd161c88f962762f80e74f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

아래 Contract 파트에서 파란색 컨트랙에 대해 하나씩 설명하도록 하겠다. 

먼저 이해하고 넘어가야 할것은 Layer2를 L1에서 어떻게 확인할 것인가에 대한 문제이다. 우리가 현재 타켓으로 하고 있는 Layer2는 옵티미즘 롤업이다. 옵티미즘의 레이어2를 먼저 적용하고, 다른 레이어도 적용될수 있도록 컨트랙 업그레이가 가능하게 제작한다.  옵티미즘 레이어2는 legacy버전과 배드락 버전이 있다. 처음 적용 대상은 옵티미즘 레거시 버전과 옵티미즘 배드락버전 중 L2 nativeToken이 톤인경우로 제한한다는 것을 기억해주길 바란다.  옵티미즘 배드락 버전에는 SystemConfig 컨트랙에 L1컨트랙의 정보와 환경설정이 담겨있다. 따라서 SystemConfig의 주소를 Layer2를 구별할 수 있는 주소로 사용할 것이다. 레거시 버전의 경우에는 SystemConfig가 존재하지 않기 때문에, legacySystemConfig 컨트랙을 별도 만들었다. 레거시 레이어2의 경우는 legacySystemConfig 컨트랙을 배포하여, 이 주소를 해당 Layer2를 구별할 수 있는 주소록 사용해야 한다. 

# Use case 

## For registrant of L2Registry

L2Registry 컨트랙에 registrant 권한을 가진 계정은 Layer2 의 고유한 정보를 보유하고 있는 SystemConfig를 등록할 수 있다. SystemConfig를 등록한다는 것은 해당 레이어2가 문제가 없는 레이어2라는 것을 확인했다는 의미이다.  등록된 SystemConfig의 레이어2만 Layer2Candidate로 등록될 수 있다.  Layer2Candidate 로 등록이 되고 나서야 해당 시퀀서가 시뇨리지를 받을 수 있게 된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/985596ab-ea70-4120-a54a-83b21d6573ac/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.07.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=51a3e490d173fdc464fa8929975b4323adcc8ca11446ce8efa2650b8ce595e74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For everyone 

누구나 L2Registry에 등록된 SystemConfig에 대해서 Layer2Candidate를 등록할 수 있다. Layer2Candidate 등록시에는 오퍼레이터 계정으로 최소 예치금 이상을 예치하여야 하므로, 최소예치금에 해당하는 톤을 같이 제공해야 한다. 현재 서비스 기준으로는 최소 1000.1 TON을 제공해야 한다.  ‘Layer2Candidate 등록’ 기능을 통해 Operator, Layer2Candidate, Coinage 컨트랙이 생성된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fafadd66-1b57-4f77-8a51-018f178ea306/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.41.57.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=8676231ce3586116b381476dcd89f17fd5b405e13d200d4ce29705648bd3f0ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For staker in Layer2Candidate

Layer2Candidate 에 스테이킹한 사용자는 WithdrawAndDepositL2 기능을 통해 스테이킹을 금액 인출과 동시에 인출된 금액을 해당 Layer2 에 예치하는 기능을 수행할 수 있습니다. 이때 스테이킹 금액을 인출할때 대기시간없이 바로 인출 및 L2 예치가 됩니다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/45aec071-04e4-491f-86b3-7377a85dc221/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=1cdec4f6ce56c9acca9f6b96b661951a64872bef8493b1e50b6275376d7f397b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For seigniorageCommittee

심플 스테이킹 V2는 Layer2를 운영하는 Layer2Candidate의 시퀀서에게 톤 시뇨리지를 발급하는 이코노미를 설계했습니다. 그러나 Layer2를 실제로 운영하지 않거나  불합리하게 시뇨리지를 할당받는 행위 등을 발견할 즉시 해당 레이어2의 시퀀서에게 톤 시뇨리지 발급을 중지할 수 있는 기능이 있어야 합니다. 

 L2Registry 컨트랙에 정의된 시뇨리지 위원회 계정을 만들었습니다. 시뇨리지 위원회는 레이어2 시퀀서에 대한 시뇨리지 발급 중지 또는 발급 중지 취소 기능을 수행할 수 있습니다.  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/68a7f248-5364-44d9-9165-a9dd06fd7908/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=536a811f005d846d642080c1342b42ea291105da074d71a34d292b3e711ea25f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Sequence Diagrams   

## Register Layer2Candidate 

Layer2Candidate를 등록할때에는 해당 레이어의 오퍼레이터 이름으로 최소 예치금액 이상을 예치해야 합니다. 

Layer2Candidate를 등록시. Layer2의 환경설정 정보를 보유하고 있는 SystemConfig 컨트랙 주소를 제시해야 합니다. 또한 입력하는 SystemConfig는 등록 전에 L2Registry에 등록되어 있어야 합니다. ( L2Registry에 등록하는 권한은 L2Registry의 Registrant 권한을 보유한 계정만 등록이 가능합니다. ) 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/04f3c312-7fb4-438d-b3b7-fa8fbf23d939/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.36.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=068e71f60291d0912b9ca386e4bebaac8405cbb5ed68f4f1d2a7ec51139a113d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Withdraw And Deposit L2 

Layer2Candidate 에 스테이킹한 사용자는 스테이킹한 금액을 즉시 출금하면서, Layer2에 예치할 수 있습니다. 

  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c6654014-150b-4263-9ffb-4816dce85214/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.49.12.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=5cf3f74b20a034830b1886af20b1db375651c954f6705ba4bd9470ae90a8fba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Stop distributing a seigniorage to the L2 sequencer

시뇨리지 위원회는  특정 레이어2가 시뇨리지를 받기에 불합리하다고 판단될때, 해당 레이어2의 시퀀서에게 배분하는 시뇨리지 발급을 중지할 수 있습니다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e2a30ff0-83d1-4da5-ab23-9fbc2867bb08/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.10.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=0d041dac6c33fcf744825a07fc1b5d2fb6b4a62cf4aa2732a0b4d72f3d1f61ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Cancel stopping distributing a seigniorage to the L2 sequencer

시뇨리지 위원회는  특정 레이어2의 시퀀서에게 배분하는 시뇨리지 발급을 중지했던 것을 취소하여, 다시 시뇨리지를 지급할 수 있습니다.  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8df2043b-66cb-4060-94f4-4a86ab9626ea/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.11.00.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDYZAJ3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBqvjaZpOv2G5GxXai7bv3dQ9lkQJeS5%2Bu21fVjLmr8QIhAM8nmNWhqGLVFZSD7rZlS6rjkONFwMKyQki%2BCZ2lIF2gKv8DCHoQABoMNjM3NDIzMTgzODA1IgxQ4qJ24gHDHPLa0z4q3AOiH7StMbiD2KKv%2Bly%2Fx7gewHnvmTLhGFy7TowHcFYKFtxs5YXhCWiQvbYEm5L6JZTp5GFKUWzdMwN%2BWO8xEotUs3ZuC0foAeNHWZJWTKXrepqj8zrdHoKeoCqFEwd5C5kSFMrd7jwhXbgbOku5Bx%2BWxZq0asnyNY2qYHsGogXsuXOsmc6Y5Y%2BXGMfE7y9oIgeH5HARnCqKWi26CqJoXkswiP18iSwrqVuHd1Nq2PJ7l0sQq%2Fy4I%2BA3I6LyDSZGlFMuP4TAuuWpyXjyJOlOfpJGkQ%2FtB2j2lVT0MaElxrTuLl0NYqW606RlICk5AirFMNVBmUjfV7sF2xtqgBIxsXcrNlhM09QYLZ48bxey0ihUgWBwKYDIKEwQAh7SHEX7RXS%2FCdajpE%2F1mY4mTp58k0L5Qglk5RQn23YF8O4ZMr6mMk%2FBXTOLwfuby4gyhnKgahCcspcaIRPLAFypA4WDkcPGm9US0fNzp8F0PkiXsokKfvZLMHJmBMP%2FfjSsxDyWsw9r0fcfTUb9JLkSH5a0zKmcQi7xhjn5Hy6vNUI8080FYHWPprArOczqgbXB2I9RSuOs8aW53hvTPm8Dzj80QrA2R%2B68oOq1Uw9OfneH2bF9LQFbT3RLmXfl77r0YDCNmtvMBjqkARARC8IHOLV2Hw2oe9dSnAC8VRVB8dYtgZVGDETRIwirJxIXQIvWvO7dvxrrQn3Y1LMolj8g9kAwLYaezj%2FsR1bS%2Bs68Bsh17Z7%2F687OdgSMD0wvsAvnSQ7PUE49VP6urx%2BNbG9V3nqiBl4I10LGDzmEi%2BOEgnUlUuwObouPTwxAvvaWqvsicQNcgLJ3QhNhT4hG44czgScJcZh7MDMzgiwgOVZF&X-Amz-Signature=46f1a032eec37cf484640b5aebd54acd636c08ffdbf42aabcd7450d81becea3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Contract Details 

## L2Registry

- 개요
  - 토카막 네트웤에서 운영되는 레이어2의 SystemConfig 컨트랙 주소가 등록된  컨트랙입니다. 
  -  타이탄, 타노스는 어드민에 의해 수동으로 SystemConfig를 입력합니다. 
  - on-demand L2에서 생성된 컨트랙은 컨트랙 생성시 자동으로 등록됩니다.  
  - 기존에 심플스테이킹에 Layer2Registry가 존재하여 구별을 주고자 L2Registry 로 이름을 정했다. 
  - 추후 다른 레이어(ex, zk-EVM) 지원을 고려하여 프록시로 구성하여 업그레이드 가능해야 한다.  
- 권한 
  - **Owner **:  오너는 로직 업그레이드 권한을 갖으며, 매니저를 지정할 수 있다. 
  - **Manager** : 재단은 MANAGER_ROLE 을 보유하고 있고, 매니저는 오퍼레이터를 등록하거나 제거할 수 있다.  SeigniorageCommittee
  - Registrant:  on-demand-L2 오픈시, L2를 실제 배포하는 서버의 EOA에게 REGISTRANT_ROLE 을 주어야 한다. 
- 스토리지 
```javascript
address public layer2Manager;
address public seigManager;
address public ton;
address public seigniorageCommittee;
    
/// systemConfig - type (0:empty, 1: optimism legacy, 2: optimism bedrock native TON)
mapping (address => uint8) public systemConfigType;

/// For registered bridges, set to true.
mapping (address => bool) public l1Bridge;

/// For registered portals, set to true.
mapping (address => bool) public portal;

/// Set the layer where seigniorage issuance has been suspended to true.
mapping (address => bool) public rejectSystemConfig; 
```
- 이벤트 
```javascript
 event SetAddresses(address _layer2Manager, address _seigManager, address _ton);
event SetSeigniorageCommittee(address _seigniorageCommittee);

/**
 * @notice  Event occurs when registering SystemConfig
 * @param   systemConfig  the systemConfig address
 * @param   type_         0: none, 1: legacy, 2: bedrock with nativeTON
 */
event RegisteredSystemConfig(address systemConfig, uint8 type_);

/**
 * @notice  Event occurs when an account with registrant privileges changes the layer 2 type.
 * @param   systemConfig  the systemConfig address
 * @param   type_         0: none, 1: legacy, 2: bedrock with nativeTON
 */
event ChangedType(address systemConfig, uint8 type_);

/**
 * @notice  Event occurs when onlySeigniorageCommittee stops issuing seigniorage
 *          to the layer 2 sequencer of a specific systemConfig.
 * @param   _systemConfig  the systemConfig address
 */
event RejectedLayer2Candidate(address _systemConfig);

/**
 * @notice  Event occurs when onlySeigniorageCommittee cancels stoping issuing seigniorage
 *          to the layer 2 sequencer of a specific systemConfig.
 * @param   _systemConfig  the systemConfig address
 */
event RestoredLayer2Candidate(address _systemConfig);

```
- 주요 Transaction Functions 
  - function rejectLayer2Candidate(address _systemConfig)  external onlySeigniorageCommittee() 
```solidity
/**
 * @notice Stop issuing seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function rejectLayer2Candidate(
    address _systemConfig
)  external onlySeigniorageCommittee() 
```
  - function restoreLayer2Candidate(address _systemConfig)  external onlySeigniorageCommittee() 
```solidity
/**
 * Restore cancel stoping seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function restoreLayer2Candidate(
    address _systemConfig
)  external onlySeigniorageCommittee() 
```
  - function registerSystemConfigByManager(address _systemConfig, uint8 _type)  external onlyManager 
```solidity
/**
 * @notice Registers Layer2 for a specific systemConfig by the manager.
 * @param _systemConfig  the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function registerSystemConfigByManager(address _systemConfig, uint8 _type)  external  onlyManager  

```
  - function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyRegistrant
```solidity
/**
 * @notice Registers Layer2 for a specific systemConfig by Registrant.
 * @param _systemConfig the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyRegistrant  

```
  -  function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant
```solidity
/**
 * @notice Changes the Layer2 type for a specific systemConfig by Registrant.
 * @param _systemConfig the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant 
```
- 주요 View Functions 
  -  function layer2TVL(address _systemConfig) public view returns (uint256 amount)
```solidity
/**
 * @notice View the liquidity of Layer2 TON for a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function layer2TVL(address _systemConfig) public view returns (uint256 amount)
```
  - function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid)
```solidity
/**
 * @notice Check whether a specific systemConfig can be registered as a type.
 * @param _systemConfig the systemConfig address
 * @param _type         1: legacy, 2: bedrock with nativeTON
 */
function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid)
  
```

## OperatorFactory

- 개요
DAOCommittee 에 Layer2Candidate가 멤버로 등록될때 Layer2Candidate의 오퍼레이터 주소가 매핑의 키값으로 등록되기 때문에 오퍼레이터 주소가 변경되어서는 안된다.  그러나 L2레이어(SystemConfig)의 오퍼레이터는 언제든지 바뀔수 있기 때문에 Operator 컨트랙을 만들었다.  Operator 컨트랙은 SystemConfig 컨트랙에 매핑되는 컨트랙이다. 즉, SystemConfig (L2레이어) 컨트랙 주소로 Operator 컨트랙의 주소를 생성하여야 한다.    추후 로직 변경 가능성이 있으므로, 프록시로 구현하였다. 
- 권한 
  - 오너 : 오너는 배포되는 오퍼레이터의 로직을 설정할 수 있다.  
- 스토리지
```javascript
address public operatorImplementation;
address public depositManager;
address public ton;
address public wton;
address public layer2Manager;
```
- 이벤트
```javascript
/**
 * @notice Event occurs when set the addresses
 * @param depositManager    the depositManager address
 * @param ton               TON address
 * @param wton              WTON
 * @param layer2Manager     the layer2Manager address
 */
event SetAddresses(address depositManager, address ton, address wton, address layer2Manager);

/**
 * @notice Event occured when change the operator implementaion address
 * @param newOperatorImplementation the operator implementaion address
 */
event ChangedOperatorImplementaion(address newOperatorImplementation);

/**
 * @notice Event occured when create the Operator Contract
 * @param systemConfig  the systemConfig address
 * @param owner         the owner address
 * @param manager       the manager address
 * @param operator      the operator address
 */
event CreatedOperator(address systemConfig, address owner, address manager, address operator);

```
- 주요  Transaction 함수 
  - function changeOperatorImplementaion(address newOperatorImplementation) external onlyOwner 
```solidity
/**
 * @notice Change the operator implementaion address by Owner
 * @param newOperatorImplementation the operator implementaion address
 */
function changeOperatorImplementaion(address newOperatorImplementation) external onlyOwner  
```
  -  function createOperator(address systemConfig) external returns (address operator)
```solidity
/**
 * @notice  Create an Operator Contract, and return its address.
 *          return revert if the account is already deployed.
 *          Note. Only Layer2Manager Contract can be called.
 *          When creating the Layer2Candidate, create an Operator contract
 *          that is mapped to SystemConfig.
 * @param systemConfig  the systemConfig address
 */
function createOperator(address systemConfig) external returns (address operator) {
 
```
- 주요 View 함수 
  - function getAddress(address systemConfig) public view returns (address) 
```solidity
/**
 * @notice  Returns the operator contract address matching systemConfig.
 * @param systemConfig  the systemConfig address
 */
function getAddress(address systemConfig) public view returns (address) 
```

## Operator

- 개요
  - Operator 컨트랙은 추후 Layer2에서 다중 시퀀서(오퍼레이터)를 지원할 가능성이 있다는 것을 염두에 두고 설계되어야 한다.  따라서 업그레이드 가능한 구조로 설계된다. 
  - Layer2Candidate 는 DAOCandidate의 모든 기능을 상속받았다. DAOCandidate의 onlyCandidate 의 정의 
    - **Operator.isOperator(msg.sender)** 가 true은 계정을 의미하며, operator 권한을 가진 계정은 Layer2Candidate의 오퍼레이터 함수를 사용할수 있게 한다.
- 권한 
  - owner 
    - 프록시 오너로서, 로직을 업그레이드 할 수 있다.
    - 프록시 오너는 재단이 보유한다. 
    - 매니저를 변경할 수 있다. 
    - 오퍼레이터를 추가/삭제할 수 있다. 
  - manager 
    - 관리자 권한은 오퍼레이터 등록 및 제거 할 수 있다. 최초 배포시 SystemConfig의 오너를 manager 로 지정한다. 
    - 추후 SystemConfig의 오너가 변경될때, transferManager 를 이용하여 manager를 변경해야 한다. (SystemConfig.owner 가 manager를 가져갈 수 있는 인터페이스를 제공한다. )  
  - operator  (onlyCandidate)
    - 오퍼레이터 권한을 보유한다. 다오멤버의 함수를 사용할 수 있다. 
    - onlyCandidate : **Operator.isOperator(msg.sender)**  == true 인 계정이다. 
    - DAOCandidate에서 상속받은 onlyCandidate가 사용할 수 있는 함수는 오퍼페이터가 실행할 수 있다. 
      - changeMember 함수 → Operator 컨트랙이 다오의 멤버가 된다. 
      - retireMember 함수 → Operator 컨트랙이 다오 멤버에서 사임한다. 
      - castVote 함수  → Operator 컨트랙 이름으로 안건에 투표한다. 
      - claimActivityReward 함수 → 리워드는 Operator 컨트랙이 받는다.  
- 스토리지
```javascript
address public systemConfig;
address public layer2Manager;
address public depositManager;
address public ton;
address public wton;

address public manager;
mapping(address => bool) public operator;
```
- 이벤트
```javascript
/**
* @notice Event occurs when the transfer manager
* @param previousManager   the previous manager address
* @param newManager        the new manager address
*/
event TransferredManager(address previousManager, address newManager);

/**
* @notice Event occurs when adding the operator
* @param operator  the operator address
*/
event AddedOperator(address operator);

/**
* @notice Event occurs when deleting the operator
* @param operator  the operator address
*/
event DeletedOperator(address operator);

/**
* @notice Event occurs when setting the addresses
* @param _layer2Manager    the _layer2Manager address
* @param _depositManager   the _depositManager address
* @param _ton              the TON address
* @param _wton             the WTON address
*/
event SetAddresses(address _layer2Manager, address _depositManager, address _ton, address _wton);

/**
* @notice Event occurs when the claim token
* @param token     the token address, if token address is address(0), it is ETH
* @param caller    the caller address
* @param to        the address received token
* @param amount    the received token amount
*/
event Claimed(address token, address caller, address to, uint256 amount);

```
- 주요  Transaction 함수 
  - function claimETH() external onlyOwnerOrManager 
```javascript
/**
 * @notice  Give ETH to a manager through the manager(or owner) claim
 */
function claimETH() external onlyOwnerOrManager
```
  - function claimERC20(address token, uint256 amount) external onlyOwnerOrManager 
```javascript
/**
 * @notice  Give ERC20 to a manager through the manager(or owner) claim
 * @param token     the token address
 * @param amount    the amount claimed token
 */
function claimERC20(address token, uint256 amount) external onlyOwnerOrManager
```
  - function depositByLayer2Canddiate(uint256 amount) external onlyLayer2Candidate 
```javascript
/**
 * @notice Deposit wton amount to DepositManager as named Layer2
 * @param amount    the deposit wton amount (ray)
 */
function depositByLayer2Canddiate(uint256 amount) external onlyLayer2Candidate 
```
  - function claimByLayer2Candidate(uint256 amount) external onlyLayer2Candidate 
```javascript
/**
* @notice Claim WTON to a manager
* @param amount    the deposit wton amount (ray)
*/
function claimByLayer2Candidate(uint256 amount) external onlyLayer2Candidate
```
- 주요 View 함수 
  - function acquireManager() external
```javascript
/**
 * @notice acquire administrator privileges.
 */
function acquireManager() external 
```
  - function isOperator(address addr) public view returns (bool)
```javascript
/**
 * @notice Returns true if the operator has permission.
 * @param addr the address to check
 */
function isOperator(address addr) public view returns (bool)
```
  - function checkL1Bridge() public view returns (bool result, address l1Bridge, address portal, address l2Ton) 
```javascript
/**
 * @notice Returns the availability status of Layer 2, L1 bridge address, portal address, and L2TON address.
 * @return result   the availability status of Layer 2
 * @return l1Bridge the L1 bridge address
 * @return portal   the L1 portal address
 * @return l2Ton    the L2 TON address
 *                  L2TON address is 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000,
 *                  In this case, the native token of Layer 2 is TON.
 */
function checkL1Bridge() public view returns (bool result, address l1Bridge, address portal, address l2Ton) {
  
```

## Layer2Manager 

- 개요
  - Layer2 시퀀서가 시뇨리지를 받기 위해서는 SystemConfig 주소를  Layer2Manager에 등록해야 합니다. 
  - 시뇨리지 분배시, Layer2의 시퀀서들에게 지급되는 시뇨리지를 Layer2Manager에게 지급합니다. 따라서 Layer2Manager 는 Layer2Candidate 의 시뇨리지 정산 전까지 해당 시뇨리지를 보유하게 됩니다.      
- 권한 
  - Owner** **:  오너는 로직 업그레이드 권한을 갖으며, 설정값들을 설정할 수 있다.  
- 스토리지
```javascript
struct OperatorInfo {
    address systemConfig;
    address layer2Candidate;
}

struct SystemConfigInfo {
    uint8 stateIssue; // status for giving seigniorage ( 0: none, 1: registered, 2: paused )
    address operator;
}

address public l2Register;
address public operatorFactory;
address public ton;
address public wton;
address public dao;
address public depositManager;
address public seigManager;
address public swapProxy;

/// The minimum TON deposit amount required when creating a Layer2Candidate.
/// Due to calculating swton, It is recommended to set 
/// DepositManager's minimum deposit + 0.1 TON
uint256 public minimumInitialDepositAmount;  

/// systemConfig - SystemConfigInfo
mapping (address => SystemConfigInfo) public systemConfigInfo;

/// operator - OperatorInfo
mapping (address => OperatorInfo) public operatorInfo;

```
- 이벤트
```javascript
/**
 * @notice Event occurs when setting the minimum initial deposit amount
 * @param _minimumInitialDepositAmount the inimum initial deposit amount
 */
event SetMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount);

/**
 * @notice Event occurs when registering Layer2Candidate
 * @param systemConfig      the systemConfig address
 * @param wtonAmount        the wton amount depositing when registering Layer2Canddiate
 * @param memo              the name of Layer2Canddiate
 * @param operator          a opperator contract address
 * @param layer2Candidate   a layer2Candidate address
 */
event RegisteredLayer2Candidate(address systemConfig, uint256 wtonAmount, string memo, address operator, address layer2Candidate);

/**
 * @notice Event occurs when pausing the layer2 candidate
 * @param systemConfig      the systemConfig address
 * @param _layer2           the layer2 address
 */
event PausedLayer2Candidate(address systemConfig, address _layer2);

/**
 * @notice Event occurs when pausing the layer2 candidate
 * @param systemConfig      the systemConfig address
 * @param _layer2           the layer2 address
 */
event UnpausedLayer2Candidate(address systemConfig, address _layer2);
```
- 주요  Transaction 함수 
  - function registerLayer2Candidate(address systemConfig, uint256 amount, bool flagTon, string calldata memo) external
```javascript
/**
 * @notice Register the Layer2Candidate
 * @param systemConfig     systemConfig's address
 * @param amount           transfered amount
 * @param flagTon          if true, amount is ton, otherwise it it wton
 * param memo             layer's name
 */
function registerLayer2Candidate(
    address systemConfig,
    uint256 amount,
    bool flagTon,
    string calldata memo
)
    external
```
  - function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool)
```javascript
/// @notice ERC20 Approve callback
/// @param owner    Account that called approveAndCall
/// @param spender  OnApprove function contract address
/// @param amount   Approved amount
/// @param data     Data used in OnApprove contract
/// @return bool    true
function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool)
```
  - function pauseLayer2Candidate(address systemConfig) external onlyL2Register ifFree 
```javascript
/**
 * @notice Pause the layer2 candidate
 * @param systemConfig the systemConfig address
 */
function pauseLayer2Candidate(address systemConfig) external onlyL2Register ifFree 
```
  - function unpauseLayer2Cnadidate(address systemConfig) external onlyL2Register ifFree 
```solidity
/**
 * @notice Unpause the layer2 candidate
 * @param systemConfig the systemConfig address
 */
function unpauseLayer2Cnadidate(address systemConfig) external onlyL2Register ifFree 
```
  - function updateSeigniorage(address systemConfig, uint256 amount) external onlySeigManger 
```javascript
/**
* @notice When executing update seigniorage, the seigniorage is settled to the Operator of Layer 2.
* @param systemConfig the systemConfig address
* @param amount the amount to give a seigniorage
*/
function updateSeigniorage(address systemConfig, uint256 amount) external onlySeigManger 
```
  - function setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)  external  onlyOwner 
```javascript
/**
* @notice  Set the minimum TON deposit amount required when creating a Layer2Candidate.
*          Due to calculating swton, it is recommended to set DepositManager's minimum deposit + 0.1 TON
* @param   _minimumInitialDepositAmount the minimum initial deposit amount
*/
function setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)  external  onlyOwner 
```

 

- 주요 View 함수 
  - function systemConfigOfOperator(address _oper) external view returns (address) 
```javascript
/**
 * @notice View the systemConfig address of the operator address.
 * @param _oper     the operator address
 * @return          the systemConfig address
 */
function systemConfigOfOperator(address _oper) external view returns (address) 
```
  - function operatorOfSystemConfig(address _sys) external view returns (address) 
```javascript
/**
 * @notice View the operator address of the systemConfig address.
 * @param _sys      the systemConfig address
 * @return          the operator address
 */
function operatorOfSystemConfig(address _sys) external view returns (address) 
```
  - function layer2CandidateOfOperator(address _oper) external view returns (address)
```javascript
/**
 * @notice  View the layer2Candidate address of the operator address.
 * @param _oper     the operator address
 * @return          the layer2Candidate address
 */
function layer2CandidateOfOperator(address _oper) external view returns (address) 
```
  - function issueStatusLayer2(address _sys) external view returns (uint8)
```javascript
/**
 * @notice View the status of seigniorage provision for Layer 2 corresponding to SystemConfig.
 * @param _sys      the systemConfig address
 * @return          the status of seigniorage provision for Layer 2
 *                  ( 0: none , 1: registered, 2: paused )
 */
function issueStatusLayer2(address _sys) external view returns (uint8) 
```
  - function checkLayer2TVL(address _systemConfig) public view returns (bool result, uint256 amount) 
```javascript
/**
 * @notice  Check Layer 2’s TON liquidity related information
 * @param _systemConfig the syatemConfig address
 * @return result       whether layer 2 TON liquidity can be checked
 * @return amount       the layer 2's TON amount (total value liquidity)
 */
function checkLayer2TVL(address _systemConfig) public view returns (bool result, uint256 amount)
```
  - function checkL1Bridge(address _systemConfig) public view returns (bool result, address l1Bridge, address portal, address l2Ton) 
```javascript
/**
 * @notice Layer 2 related information search
 * @param _systemConfig     the systemConfig address
 * @return result           whether Layer2 information can be searched
 * @return l1Bridge         the L1 bridge address
 * @return portal           the optimism portal address
 * @return l2Ton            the L2 TON address
 */
function checkL1Bridge(address _systemConfig) public view returns (bool result, address l1Bridge, address portal, address l2Ton)

```

## Layer2ContractFactory 

- 개요
  - Layer2Candiate 를 생성하는 컨트랙입니다. 
- 권한 
  - Owner** **:  오너는 로직 업그레이드 권한을 갖으며, 설정값들을 설정할 수 있다.  
- 스토리지
```javascript
address public depositManager;
address public daoCommittee;
address public layer2CandidateImp;
address public ton;
address public wton;

address public onDemandL2Registry;
```
- 이벤트
```javascript
/**
 * @notice  Event that occurs when a Candidate is created
 * @param sender            the sender address
 * @param layer2            the layer2 address
 * @param operator          the operator address
 * @param isLayer2Candidate whether it is Layer2Candidate
 * @param name              the name of Layer2
 * @param committee         the committee address
 * @param seigManager       the seigManager address
 */
event DeployedCandidate(
    address sender,
    address layer2,
    address operator,
    bool isLayer2Candidate,
    string name,
    address committee,
    address seigManager
);
```
- 주요  Transaction 함수 
  - function deploy(address _sender, string memory _name, address _committee, address _seigManager) public onlyDAOCommittee  returns (address)
```solidity
/**
* @notice Deploy the candidate contract
* @param _sender       the sender address
* @param _name         the name of layer2
* @param _committee    the committee address
* @param _seigManager  the seigManager address
* @return              the created candidate address
*/
function deploy(
  address _sender,
  string memory _name,
  address _committee,
  address _seigManager
)
  public onlyDAOCommittee
  returns (address)
```

## Layer2Contract 

- 개요
  - 심플스테이킹(톤 스테이킹)의 기본기능(예치, 업데이트시뇨리지-이자지급, 출금 기능)을 지원한다. 
  - DAOCandidate에서 할 수 있는 다오 멤버 기능을 지원한다. 
  - 업데이트 시뇨리지 실행시, Layer2Candidate의 시퀀서(오퍼레이터)가 시뇨리지를 받을 수 있다.
- 권한 
  - Owner : 오너는 로직 업그레이드 권한을 갖으며, 설정값을 초기화 할 수 있다.
  - onlyCandidate : Layer2Candidate 에 매칭되는 Operator 컨트랙의 오퍼레이터 권한을 갖는 계정 
```javascript
 modifier onlyCandidate() {
      require(IOperateContract(candidate).isOperator(msg.sender),
      "sender is not an operator");
      _;
  }
```
- 스토리지
```solidity
    mapping(bytes4 => bool) internal _supportedInterfaces;
    bool public isLayer2Candidate;
    address public candidate;
    string public memo;

    address public committee;
    address public seigManager;
    address ton;
    address wton;
```
- 이벤트
```javascript
event Initialized(address _operateContract, string memo, address committee, address seigManager);
event SetMemo(string _memo);
```
- 주요  Transaction 함수 
  - function changeMember(uint256 _memberIndex) external  onlyCandidate   returns (bool)
```javascript
/// @notice Try to be a member
/// @param _memberIndex The index of changing member slot
/// @return Whether or not the execution succeeded
function changeMember(uint256 _memberIndex)
    external
    onlyCandidate
    returns (bool)
```
  - function retireMember() external onlyCandidate returns (bool)
```javascript
/// @notice Retire a member
/// @return Whether or not the execution succeeded
function retireMember() external onlyCandidate returns (bool) 
```
  - function castVote(uint256 _agendaID,  uint256 _vote, string calldata  _comment ) external  onlyCandidate
```javascript
/// @notice Vote on an agenda
/// @param _agendaID The agenda ID
/// @param _vote voting type
/// @param _comment voting comment
function castVote(
    uint256 _agendaID,
    uint256 _vote,
    string calldata _comment
)
    external
    onlyCandidate
```
  - function claimActivityReward() external  onlyCandidate
```javascript
/**
 * @notice Claim an activity reward
 */
function claimActivityReward()
    external
    onlyCandidate
```
  - function updateSeigniorage() external returns (bool) 
```javascript
/// @notice Call updateSeigniorage on SeigManager
/// @return Whether or not the execution succeeded
function updateSeigniorage() external returns (bool)
```
  - function updateSeigniorage(uint256 afterCall) public returns (bool) 
```javascript
/// @notice Call updateSeigniorage on SeigManager
/// @param afterCall    After running update seigniorage, option to run additional functions
///                     0: none, 1: claim, 2: staking
/// @return             Whether or not the execution succeeded
function updateSeigniorage(uint256 afterCall) public returns (bool) 
```
- 주요 View 함수
  -  function totalStaked() external  view returns (uint256 totalsupply)
```javascript
/// @notice Retrieves the total staked balance on this candidate
/// @return totalsupply Total staked amount on this candidate
function totalStaked()
    external
    view
    returns (uint256 totalsupply)
```
  - function stakedOf(address _account)  external  view returns (uint256 amount)
```javascript
/// @notice Retrieves the staked balance of the account on this candidate
/// @param _account Address being retrieved
/// @return amount The staked balance of the account on this candidate
function stakedOf(
    address _account
)
    external
    view
    returns (uint256 amount)
```

## SeigManagerV1_3 

- 개요
  - Layer2Candidate의 업데이트 시뇨리지 실행시, layer2의 TON TVL에 따라  Layer2 시퀀서에게 시뇨리지를 지급해야 하며, 지급되는 시뇨리지는 Operator 컨트랙에게 정산됩니다.  
  - Operator 컨트랙의 오퍼레이터권한을 갖는 시퀀서가 Layer2Candidate 의  업데이트 시뇨리지 실행(시뇨리지 분배시)시, 청구 및 스테이킹 옵션을 선택해서, 시뇨리지 정산과 동시에 청구 또는 스테이킹 기능을  같이 실행할 수 있습니다.  
  - L2 시퀀서에게 분배되는 시뇨리지 분배로직은 [V2 백서](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2)의 시뇨리지 배분 규칙에 따라 이루어진다. 
  - V1에서 이미 SeigManager 가 배포되어 운영되고 있으므로, 다른 기능은 변경없이 업데이트 시뇨리지 함수만  SeigManagerV1_3에 변경된 로직으로 실행되도록 한다. 
  - 업데이트 시뇨리지 함수실행시 Layer2에게 제공하는 시뇨리지를 관리하기 위한 스토리지를 추가한다. 
- 권한 
  - 
- 추가된 스토리지
```javascript
struct Layer2Reward {
    uint256 layer2Tvl;
    uint256 initialDebt;
}

/// L2Registry address
address public l2Registry;

/// Layer2Manager address
address public layer2Manager;

/// layer2 seigs start block
uint256 public layer2StartBlock;

uint256 public l2RewardPerUint;  // ray unit .1e27

/// total layer2 TON TVL
uint256 public totalLayer2TVL;

/// layer2 reward information for each layer2.
mapping (address => Layer2Reward) public layer2RewardInfo;

```
- 삭제된 이벤트 
업데이트 시뇨리지 실행시 발생하던 SeigGiven 이벤트가 삭제되었다. 

```javascript
event SeigGiven(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig);
```
- 추가된 이벤트
업데이트 시뇨리지 실행시 아래 SeigGiven2 이벤트가 추가 발생한다. 

```javascript
/**
 * Event that occurs when seigniorage is distributed when update seigniorage is executed
 * @param layer2        The layer2 address
 * @param totalSeig     Total amount of seigniorage issued
 * @param stakedSeig    Seigniorage equal to the staking ratio of ton total 
 *                      supply in total issued seigniorage
 * @param unstakedSeig  Total issued seigniorage minus stakedSeig
 * @param powertonSeig  Seigniorage distributed to powerton
 * @param daoSeig       Seigniorage distributed to dao
 * @param pseig         Seigniorage equal to relativeSeigRate ratio 
 *                      from unstakedSeig amount
 *                      Seigniorage given to stakers = stakedSeig + pseig
 * @param l2TotalSeigs  Seigniorage distributed to L2 sequencer
 * @param layer2Seigs   Seigniorage currently settled (give) 
 *                      to layer2Candidate's operator contract
 */
event SeigGiven2(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig, uint256 l2TotalSeigs, uint256 layer2Seigs);

```
- 주요  Transaction 함수 
  - function excludeFromSeigniorage (address _layer2) external returns (bool) onlyLayer2Manager
```javascript
/**
* @notice Exclude the layer2 in distributing a seigniorage
* @param _layer2     the layer2 address
*/
function excludeFromSeigniorage (address _layer2)
external
returns (bool)
```
  - function updateSeigniorageOperator() external  returns (bool)  onlyCandidate
```javascript
/**
* @notice Distribute the issuing seigniorage.
*         If caller is a Layer2Candidate, the seigniorage is settled to the L2 Operator.
*/
function updateSeigniorageOperator()
external
returns (bool)
```
  - function updateSeigniorage() external  returns (bool)  onlyCandidate
```javascript
/**
* @notice Distribute the issuing seigniorage.
*/
function updateSeigniorage()
external
returns (bool)
```
  - function updateSeigniorageLayer(address layer2) external returns (bool) 
```javascript
/**
* @notice Distribute the issuing seigniorage on layer2.
*/
function updateSeigniorageLayer(address layer2) external returns (bool) 
```
- 주요 View 함수 
  - function getOperatorAmount(address layer2) external view returns (uint256)  
```javascript
/**
* @notice Query the staking amount held by the operator
*/
function getOperatorAmount(address layer2) external view returns (uint256) 
```
  -  function estimatedDistribute(uint256 blockNumber, address layer2, bool _isSenderOperator)  external view returns (uint256 maxSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 relativeSeig, uint256 l2TotalSeigs, uint256 layer2Seigs)
```javascript
/**
* @notice Estimate the seigniorage to be distributed
* @param blockNumber         The block number
* @param layer2              The layer2 address
* @param _isSenderOperator   Whether sender is operator of layer2
* @return maxSeig            Total amount of seigniorage occurring in that block
* @return stakedSeig         the amount equals to the staking ratio in TON total supply
*                            in total issuing seigniorage
* @return unstakedSeig       MaxSeig minus stakedSeig
* @return powertonSeig       the amount calculated to be distributed to Powerton
* @return daoSeig            the amount calculated to be distributed to DAO
* @return relativeSeig       the amount equal to relativeSeigRate ratio from unstakedSeig amount
* @return l2TotalSeigs       the amount calculated to be distributed to L2 sequencer
* @return layer2Seigs        the amount currently to be settled (give)  to layer2Candidate's operator contract
*/
function estimatedDistribute(uint256 blockNumber, address layer2, bool _isSenderOperator)
external view
returns (uint256 maxSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 relativeSeig, uint256 l2TotalSeigs, uint256 layer2Seigs) 
```

## DepositManagerV1_1 

- 개요
  - Layer2Candidate 의 경우라면 톤스테이킹출금을 하면서, 동시에 해당 Layer2에 예치할 수 있는 기능 (withdrawAndDepositL2) 을 지원한다. 이 때에는 출금시 지연시간 없이 즉시 출금 후, L1에 예치된다. 
  - Layer2Candidate가 아닌 레이어에 withdrawAndDepositL2 함수를 요청할때는 에러를 발생한다. 
  -  DepositManagerProxy에 기존 로직은 그대로 두고, withdrawAndDepositL2 함수만 추가되도록 한다. 
- 스토리지
```javascript
address public ton;
uint32 public minDepositGasLimit; /// not used
```
- 이벤트
```javascript
/**
 * @notice Event that occurs when calling the withdrawAndDepositL2 function
 * @param layer2    The layer2 address
 * @param account   The account address
 * @param amount    The amount of withdrawal and deposit L2
 */
event WithdrawalAndDeposited(address indexed layer2, address account, uint256 amount);

```
- 주요  Transaction 함수 
  - function withdrawAndDepositL2(address layer2, uint256 amount) external ifFree returns (bool) 

```javascript
/**
 * @notice Withdrawal from L1 and deposit to L2
 * @param layer2    The layer2 address
 * @param amount    The amount to be withdrawal and deposit L2. ()`amount` WTON in RAY)
 */
function withdrawAndDepositL2(address layer2, uint256 amount) external ifFree returns (bool) 
```