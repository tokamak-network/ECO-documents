## Motivation: <u>Why do we develop in this project?</u>

The Tokamak Network has announced plans to launch a layer 2 (L2) protocol based on Optimism in the second quarter of 2023. However, the current infrastructure, including Simple Staking, is not suitable for the L2 environment. Additionally, with competitors such as Arbitrum, Optimism, and Boba Network already in the market, merely creating a layer 2 platform may not be enough to attract users.

To overcome these challenges, Tokamak Layer2 Economics team will provide infrastructure for the Tokamak Network’s L2 environment. So, our team’s plan is convert current TON ecosystem to layer2 friendly such as Staking & DAO. And provide unified interface contains bridge, swap & pool functions.

## Goals: <u>What do we want to achieve with this project?</u>

TON Staking & DAO v2 aims to achieve the following goals:

- Foster organic growth of the Tokamak Network
- Enhance the user experience of the Tokamak Network
- Reinforce the security of the Tokamak Network
- Alleviate the capital inefficiency of staked TON
- For support both v1 & v2 update TON seigniorage distribution model

Unified interface aims to achieve the following goals:

- Support multiple functions in the similar UI
- Support Uniswap V3 like functions in L2 

## Roadmap: <u>How did we plan and what has changed?</u>

<Original roadmap(in May)>

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b11790d0-455d-4993-a8bb-3bc27b772957/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBFRM4X%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1lc4nMpCEj1pv0dJYSQQyYQyDv02wXEK6fZaUIWmP4AiEA1M3A8guwdJPTL1Dnv0NYHBtuEiNh%2FZDVMBQBn4vYET0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDHtNsNZfNV2doMm00CrcAxzTyinwJicLgxG2idtvmWHAic4L7REmEqjbCwGwnmn4R%2BZKPfuREDL97lzHctLrL8ymyPlDiTrsJVQtokiwqLDXwjkxbETXqGnA2GiU%2BdZ2dGBNs9KQ19%2FFOG9zgY6LzVH92Y0MjPk78xvo9cGmwyEXF2%2B9k5Ml5w5Ea4LZjZMwyMOiRl08q8SjaZT4ojFyLuR4Oy%2FBInSyFudIJZkjSWgBaRJU04itXklEoMrjHDifhA9%2F52QrDyKXThI%2BzthIxQ4whEhdcbYqt5JGbnB%2BH9UGcWWhkz1%2FBTQaX22gFWyytxh7YXeyoiY7OStE5r3KdzpRbIRxFtWFGvB%2BSsBoxZdzfxO0y2PyKPBcqo9zrI4YsylIy5t6h8L8zd67hv5u6Va4k4VaywM3JUMHRlrnrAd%2B6S%2FNyWgcxiWcXaiUs%2Bpw%2BLTxuy6XIUZXVhi45zTbpgAEzFhPfIR%2FHvYqFmUZXRVTGrZfA15EomLZDPklxG6BnUxs%2Ba69vGHGsphFWFu6Sab9S5MYoHl%2FW9hvpTFoBMnGlkUExPW7xhQkxvBXpBJNxpC3COIn5GnzohTW3drgUcJE%2BNrmEq4DMRkYCVa0Zvk7PKHTw6DbOd7EFpjPVFVu0cpl40tlobKNzJs4MK6a28wGOqUBh07vBWx3K36DkFEfc1Y8PgD%2Fo3wQR39sAq4I51hPdrTe48zfEdbKZ9VVM2ekdFxp%2BBdUB14fLkfwZjn8jR9DFSOymor0puGuOh0ELBkweafO1K1HjZ6BW5OGnji7g763BQCR%2FPucugvL67rZSRqJK%2BhAK5vBNMNLA4xX%2FmcPyqR0QBhigbTMJ%2Bzru8mE266cSV89YcYacOv77SBFxtjNtjOTwB0W&X-Amz-Signature=90243d1228700b183744633996df4f4ad7460efac731e71196dbee9dfb3ffbef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Major changes

### 1. Bridge is upgraded to unified bridge

The original plan was to utilize the existing design of the bridge. but there are changes about it. so, we developed based on unified design. In Unified-interface we can support many functions to users. In current version, we only provide bridge & swap and pool functions are under developed.

### 2. Implement Staking V2 & DAO is delayed

Due to lack of front-end resource, we have to consider priority of service development. So, Staking & DAO service development is postponed because priority of these service is low. Many of the L2 Economics team’s resource will be move to Fee Token project.

## Member change

| Q1 | Wyatt | Suah | Praveen | Zena | Harvey | Jason | Lakmi | Ryan | Monica |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q2 | Jason | Suah | Praveen | Zena | Harvey | Justin | Ale | Ryan | Monica |

- **PM:** Wyatt → Jason(PM & Service)
- **Contract:** + Justin
  - support front-end & develop uniswap v3 contract for unified bridge
- **Service:** Lakmi → Ale
  - Unified Bridge implementation

## Budget Usage in Q1

|  | Income (TONs) | Outcome (TONs) | Total |
| --- | --- | --- | --- |
| Initial endowment | 20,300 | 18,900 (incentive) |  |
| Q1 Budget | 24,000 | 23,000 (incentive) |  |
| BOE |  | 1,136 |  |
| Total | 44,300 | **43036** | **1264** |

## Q2 2023: What did we do?

## output link: 

## Details

### Research: Suah, Praveen

**Motivation**

- Complete TON Staking v2 phase 2 modeling
- Update the TON governance fitting the L2 environment

**Goals**

- Do TON Staking v2 phase 2 modeling
  - TON staker-centric verification economics
- Design possible alternative TON DAO structures based on proof-of-uniqueness

**Progress**

**Apr**

- Finalized legal opinion 

[Tokamak - Legal Opinion (19 April 2023).pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/364ece05-825a-4160-9eb4-0aa2dd80fc98/Tokamak_-_Legal_Opinion_%2819_April_2023%29.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6KSWXRG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T104344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk9WEL8gf0E7CUVcuTfloc%2BIqyMoKHLLTIp1XVMUDWVAIgXkssePNzQYl8lXvrlzqVrq5R%2BSZg1A%2BZISVSW21nEoQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDB1vzXRX2pJ7%2BM712SrcA0lQbdLNYoStCc2z7SmnoLMjiWWBQbrNDs0xItcOAz1M3coTTrbQA7q0AvULGxoAD4JcoeeDPBhcEi04qQM7P6zhILoq2Qq6aAwJml5%2F2fvPB2q4aAPRnKnlTdpozWN%2Fa5ogPJ%2BeGg6L8%2FHSVLWofNjfjC29CWZ8%2BehRlIU4xNoQBysBTKteJhmCaMXWGXyDP7AKgnl1W9Mx%2F5AQYktqdBXtrOOceZrpSa6BGM6KCptD7fKCqvrqMnKg2LhbVncPGiywTlToSDgL%2FRCmG1Pnqdb2bYkf%2Be74p%2BeaWTtTTiJLm0g0WzUmF4TMVWrBAnwbJCpSbyHeVoxdZTnD2z4kDFAEv32bnuPw1BUeYzEgO%2BEQN9S1%2FciVriI5Sjzx%2F%2BpEEsNRiFMSAuA7fegZn7O9V8VKb5hVttwt0MYewQ%2FnHxfHQEMaUEtNpZFxCjTWzYvCMu%2BNCFjZqJkEeDGf%2BZgmL%2FEZZekN1GYN21eEb0RGkIS3bVnk3F3rXY2%2BFY0srC%2FywMFC0mI%2BaA4J5S%2Fbv8FGImziPZ3X2wrUDC7MrIa8qePCfjrFrMnU%2BYh6BDhApTi4PdIAjkfG5ZlM%2FJluaawxXESOx8CzAhbX5wf6r2FvVxj1k9OfUQcDRm6%2BuoQQMPTL28wGOqUBpfOEIT9FaQMVfS6gkSTCJefP3XxKMKpUnkGNZqv%2Brit1RrZ%2FG4B5DFSGMEF%2FILKBJJ5jLTIh1CX%2FjbFXTuhiu1CMEzrcLY%2BHSRVhswzQgbWyD9bvWC2GwSuStoJsEzMcFGAMUEafqVHBuVcdHhk2xOKBGPYN2EQyTZiPO6XtZbZQeFgLIkc2jlMQ2dvmoFZF7wn2PFA5cy3wT6ATLcy9g1MLd9SD&X-Amz-Signature=67e9285e041501c01409dc62a091216966593b1a1dea5461ae02fe1154f8ff44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [Bridge storyboard guidelines](https://docs.google.com/presentation/d/1wlekH_W6jooANOKtY1hDy_f97nC3F1xVlvSvM23e10U/edit#slide=id.g22a0544c3ae_0_54)
- [Staking storyboard guidelines](https://docs.google.com/presentation/d/1dAK8670YsrFmYACPLzL6xlIqSCWMnyc0IGzj_GwGDUo/edit)
- [Gradual decentralization of TON governance](https://docs.google.com/presentation/d/1Iqtg3NWUj3-HelintCnzrb2uxkvHFHTpWYRWKt6Bhs0/edit#slide=id.g21d80f23f21_0_54)

**May**

- Governance Article Part 1([Draft](https://docs.google.com/document/d/1xIhrq4_Zkw6-a9WxgOSC7R53yHuXUakbIyQxMtoHXTw/edit?usp=sharing)), Part 2 ([WIP](https://docs.google.com/document/d/1hhwE3kgajOMRziEp0qH65njkQzcGT_BUOUYKnpVIBZM/edit?usp=sharing))

**Jun**

- Updated Seignorage distribution (v1+v2) model ([link](https://docs.google.com/presentation/d/1SNzrypW7bgNjuZRJ9kGqAsdRV-JtkMaFq5U1PZNoC3I/edit#slide=id.g21de84e49b9_0_54))
- Updated Seignorage distribution demo + simulation ([link](https://docs.google.com/spreadsheets/d/19SEEVLMazPdkdqNJ5dr1dyVhzqT1V71jcNRlhjRuvGY/edit#gid=0))

### Contract: Zena, Harvey, Justin

**Motivation**

- Develop TON staking v2 phase 1 contracts in a technically efficient way 
(i.e.) lower gas costs)
- Develop the DAO Contract V2 for using TONStakingV2
- Develop the  TON Staking V2 contracts 

**Goals**

- Finalize the general structure of TON Staking v2 phase 1
- Develop TON staking v2 phase 1 contracts
  - Simple (Normal)/FW staking
  - TON DAO
  - Migration
- Develop the DAO Contract V2

**Progress**

**Apr**

- TONStaking V2
  - [Function Description](/6708d576446c430483cfad093c100398) 
    - Develop TONStaking V2 Contracts  ([doc](/d5e44476c3c24f40aeb16272460bf420), [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_4_snapshot))  
  - Test Contracts  
    - [v0.3 ](/053f361866c54258a612d9861ba44b0c) (included fast withdraw) 
    -  [v0.4](/577d8dfa79804406b21467510653547d) (included fast withdraw & snapshot) 
  - Guide contracts usages ([doc](/ed92dcfb9aaf4ce993de47ba9b404750)) 
- DAOContract
  - Analyze the DAOContract ([doc](/76de9c1b7f3f4d84bb3681c2416cd79f))
  - Make the checklist what needs to be corrected ([doc](/59084b605b724674904e107aada970c3))
  - Develop the DAOContract ([commits](https://github.com/tokamak-network/tokamak-daoV2-contracts/commits/main))
  - Clean up what has changed ([doc](/3118434110ee48a2bbd8a029c339b0d0))

**May**

- Develop the DAO Contract
  - Specification of requirements ([doc](/3118434110ee48a2bbd8a029c339b0d0))
  - Develop the Contract ([commits](https://github.com/tokamak-network/tokamak-daoV2-contracts/commits/2.typescript-style))
    - Develop the new ProxyV2 & new LogicV2 (~5/11)
    - Develop the original Proxy & new LogicV2 (5/12~5/17)
    - Develop the test scripts (5/18~5/26)
- Develop TONStakingV2 Contracts 
  - [Function description  ](/6708d576446c430483cfad093c100398)   
  - Develop the version 0.4 for snapshot function
    - Make [test scripts](/577d8dfa79804406b21467510653547d) & set test environment  for snapshot function (v0.4) 
    - [Develop the snapshot functionality](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_4_snapshot) for TON staker (v0.4) : 100%
    - [Guide contracts usages](/ed92dcfb9aaf4ce993de47ba9b404750) (v0.4) : 100%
  - [Seminar of TON Staking V2](https://docs.google.com/presentation/d/1B1tmpdY_CT09dLsWOKXx6DGDxFo6XUcUoMK7F42fRuE/edit#slide=id.p)[KR] : 100%
  - [Request internal audit](/509c645558ac4b2e89502e9ecc45a0f8) of TON staking V2 
  - check 'pause' function of Simple Stake V1 ([doc](/bb2be3368e734bf7a549aed70d0d928c), [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_6_pause_simpleStakeV1))
  - Testing the use of WTON in the bridge ([doc](/84076a9babbb4821ae0b8b9037122bc6), [commit](https://github.com/tokamak-network/layer2-interface-test/blob/main/scripts/use-wton-in-bridge.js))
  - As we decided to use the assets(token) of staking v2 as WTON instead of TON, we will modify the code and all documentation  TON to WTON.  ⇒ Re-decided to use TON in L2  
    - change TON to WTON v0.5 ([commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_7_TONtoWTON))
    - test WTON v0.5 ([doc](/2519d8b8820e4635985580d4eff1afb3))
    - the contract usage guide v0.5([doc](/b437c3d81a0344b5b075d1741827b9ec))
  - Commenting in contracts ([commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_5_audit_v1)) 
  - Internal audit of TON staking V2 ([doc](/509c645558ac4b2e89502e9ecc45a0f8)) (on progressing)
  - Set initialize parameters ( [mainnet](/9bc875dd731543d49911c6e5385c2315) , [goerli](/58dbd5bf5c1642d09aa788b2dcf2c491) )
  - Discuss how to operate V2 together without closing simple staking
- Develop Tokamak-Uniswap-V3-deploy
  - add weth9Address, ncl option to task
  - [commits](https://github.com/tokamak-network/tokamak-uniswap-v3-deploy/commits/master), [doc](/d6c9c08c81d84f88a7f4c3c70170c7bf), [npmPackage](https://www.npmjs.com/package/@tokamak-network/tokamak-uniswap-v3-deploy)
- Develop Tokamak-Uniswap Contracts Deploys
  - test POOL_INIT_CODE_HASH
    - [doc](/59da8a344b0749c2931bcc85fdc0d5c5), 
  - test scripts
    - [doc](/7da8cc07c7a647f298ea1fdd16732696)
  - verify [doc](/c6c767119d0140ada53d001e1ac0324d)
  - about Deterministic Deployment Proxy [doc](/3cf525ad71b14762a2b343f3b1e5a513)

Jun

- Develop the DAO Contract for V2
  - finish Develop the Contract about V2 ([commits](https://github.com/tokamak-network/tokamak-daoV2-contracts/commits/2.typescript-style)) (100%) (5%)
- Develop the BridgeSwapTest ([doc](/315d42b626914045b5d7791006b4f15b), [commits](https://github.com/tokamak-network/bridgeSwapTest/commits/main))
- Develop TONStakingV2 Contracts 
  - Discuss how to operate V1 and V2 together without closing simple staking
  - internal audit 
    - change the event parameter and function interface ( [doc](/509c645558ac4b2e89502e9ecc45a0f8), [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_5_audit_v1) ) 
  - feedback the audit (check allowance, grant minter role : JS_2, JS_3, JS_4) ([doc](/509c645558ac4b2e89502e9ecc45a0f8), [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_5_audit_v1))
  - feedback audit  ([doc](/509c645558ac4b2e89502e9ecc45a0f8)) 
    - JS_5 : change name from `Sequencer` to `L2operator`, change “`OVM_Sequencer`” to “`OVM_TONStakingManager`” : [commit](https://github.com/tokamak-network/tokamak-staking-v2/commit/05e318434fe9ad482a16eb66bb817e590dc96a32) V0.6 : 100%(100%) 
    - S_1: update the seigniorage formula  [commit](https://github.com/tokamak-network/tokamak-staking-v2/commit/333580baff205c8f6c22a8bdda123ab29a42a318) : 5%
  - create the contract usage guide **V0.6** ([doc](/f3b340156ff0473c97942e6c209a83b8))
  - update the seigniorage formula, dao interface ([contract logic check](/2d7a3567409144029e049296f39b9106), [doc](/509c645558ac4b2e89502e9ecc45a0f8)2, [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_10_changeUpdateSeig))  
- Develop the DAO Contract
  - Develop the Contract Logic (Used together with V1 and V2) ([drawio](https://app.diagrams.net/#G1uGIhLtm2joDOnGdtTipGjYpfyfizneQh), [commits](https://github.com/tokamak-network/tokamak-daoV2-contracts/commit/4f1906b14355b6da9543aa06418db4263e06494f), [commits](https://github.com/tokamak-network/tokamak-daoV2-contracts/commits/6.updateForV1)2) - 15% 
- Develop the bridgeSwap Contract ([doc](/3c24540c7025402384c26e6f45e5c608), [commits](https://github.com/tokamak-network/bridgeSwapTest/commits/main)) - 100% 
  - finish internal audit ([doc](/66683ac03790445093b674426d288444), [commits](https://github.com/tokamak-network/bridgeSwapTest/commits/main)) 
  - prepare deploy ([doc](/b0104058f4634b0cb94ea61aa5984413), [gasFee](https://docs.google.com/spreadsheets/d/12rz6J0gTC2UD1rSIdyZ7tP3De1Xv1jl_nrL_IpkWCEM/edit#gid=0)) 
  - Error code cleanup ([doc](/604833631ed04eeb8392d5a4ae0fe259))
  - Deploy the bridgeSwap Contract on mainnet ([doc](/b0104058f4634b0cb94ea61aa5984413), [commits](https://github.com/tokamak-network/bridgeSwapTest/commits/main))
  - bridgeSwap interface for front ([doc](/66683ac03790445093b674426d288444))
- Uniswap V3 Contracts ([notion](/d545dd0344194b5faaae606e809c80b9)) 
  - Deployed and Verified Permit2, Universal Router ([notion](/54aea99937124da2b0f77a3b1409246b), [github](https://github.com/usgeeus/universal-router/commit/d7a465028872c3aa3fbead378de9ea9d95a17e1c))
  - Deployed, Initialized, added liquidity to a pool TON/TOS ([notion](/d545dd0344194b5faaae606e809c80b9), [github](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3)) 
  - [doc ](https://excalidraw.com/#json=-6IP2yAG3oeJdIX1Bp6c4,PcqHV8OX8WzfObBV5HsmPA)about ticks
- Prepare  the uniswap v3 contracts deployment 
  - refactoring and test scripts
    - create_pools, initialize_pools, add_liquidity ([github](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/tree/deployWeth9_testCollect/scripts/v3/mainnet)) 100%
      - create_pools, initialize pools ⇒ createAndInitializePoolIfNecessary  (combine create_pools and initialize_pools to save gas) (**100**%)
  - add create pools and initialize, add_liquidity scripts on usdt, usdc(100%)
  - Swap Test (100%)
  - simulation1 [doc](/476effabd9104325bb516312ba37c966), simulation 2 [doc](/8cea096cad6f4f23a846c8d65a51eb48), titan goerli [info](/26f3cea3c3a74f0cbc65cb0d21f985d6)
- Deploy  the uniswap v3 contracts on titan mainnet 
  - deployed uniswap v3 contracts and token on titan ([doc](/b0104058f4634b0cb94ea61aa5984413), [deployed addresses](/0f691cabf28f4643b26efb31a88a370d))
    - upgrade tokamak-smart-order-router  v0.1.0 (applied titan address) ([commits](https://github.com/tokamak-network/tokamak-smart-order-router/commits/add.tokamak-goerli))
  - SwapRouter02 test scripts [doc](/18f1cb418cd94724b14d87b8b97edf7c)
- Deploy tokamak-smart-order-router for titan ([commits](https://github.com/tokamak-network/tokamak-smart-order-router/commits/titan)) 

### Service: Jason

**Motivation**

- Develop layer2 related service.

**Goals**

- Implement 3 types of service
  - Bridge 
  - Staking
  - TON DAO

**Progress**

**Apr**

- DAO election tab ([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/99da1809336dfb17cdeb2425618f234e4ae3bf37)) - 100%
- DAO detail page in election tab ([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/cebf2823d0492f9a8c22127756c8ed392e900b83)) - 50%
- DAO agenda tab ([commit](https://github.com/tokamak-network/tokamak-dao-v2-interface/commit/4e60424d094cb1649ed3272c876e4ab604150070)) - 20%
- Staking/DAO architecture subgraph 0.1 ([doc](/b504ecbaad304dada6fc0b636dd74306)) - 30%

**May**

- deposit, withdraw part in unified bridge ([commit](https://github.com/tokamak-network/Unified-interface/commit/535802cf79abd7891fdd7164e9f6b8b5ba48d43d)) - 80%
- Staking subgraph architecture v0.2([doc](/9f7cd5c147bd407cbaa37d85e3e87691)) - 70%
- Fw fee server ([commit](https://github.com/tokamak-network/fw-fee-server/commit/a07a308b5382fb5baefd8b7652e05ede24da2498)) - 30%
- Staking v2 subgraph ([commit](https://github.com/tokamak-network/staking-v2-subgraph/commit/4dc5c212383f2e641233b0b6d653a38fb4136346)) - 10%

**Jun**

- setup routing api for swap([commit](https://github.com/tokamak-network/tokamak-routing-api/commit/884205e98eda7d11c58472855d449804523e0c4f))
- deploy subgraph to titan([commit](https://github.com/tokamak-network/tokamak-uniswap-subgraph/commit/c6df6728e47f97fee56897c50d80f1116ae6bb9f))
- bridge interface ([commit](https://github.com/tokamak-network/Unified-interface/commit/322558f9bd361e40cbee3ff1bf86f53bf2e8f9f6)) 

### Plan & Design: Ryan, Monica

**Motivation**

- Design TON staking v2 phase 1 in a more user-friendly way

**Goals**

- Do storyboard / design works of TON staking v2 phase 1
  - Bridge 
  - Staking
  - TON DAO
  - Migration

**Progress**

**Apr**

- [Staking Storyboard v0.1](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?node-id=265-8916&t=lXeaxSa2xSuxUjCd-4) (FW management)
- [Bridge Storyboard v0.3](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?node-id=353-12829&t=lXeaxSa2xSuxUjCd-4)
- [Bridge Storyboard 0.4ridge Storyboard 0.4](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?node-id=524-24902&t=GV3IarAaLKyov7ZL-4)
- [Seminar on the bridge storyboard](https://www.figma.com/file/yfPYsy29oqEpr5b4V1kw2P/Seminar-on-bridge-storyboard?node-id=0%3A1&t=dzar2f6dAj7dz32P-1)
- [Bridge UI Design](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=648-2906&t=IeItjdsixysn2taF-4)

**May**

- [Staking storyboard0.2](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?type=design&node-id=554-12514&t=grT27iUwfsjGMDzP-4)
- [Staking UI Design-TON Staking v1/v2](https://onther.slack.com/archives/C01G5GYKJ03/p1683712821522599)
- [Integrated UI Design -Swap/Bridge](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=743-6371&t=88GyAO3UqV0fLiUx-4)

**Jun**

- [Service Name / Logo](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=1413-23187&t=uTdyNaMBdEmf59Xc-4)
- [UI kit update](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=743-6219&t=8orb8gP06gZ39yWZ-4)
- [confirm modal](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=2101-34818&mode=design&t=guTN76TTAJfFrDeB-4)
- [Write User Guide (Swap/Bridge)](https://tokamaknetwork.gitbook.io/home/02-service-guide/tokamak-bridge)
- test([link1](/7458d57beb4945769ac0b6c182219304#7b3efd4830154cee8fcdaed642590462), [link2](/7458d57beb4945769ac0b6c182219304#c7ece4ee294e46afafe758fae611f138))
- [UI Update](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=743%3A3474&mode=design&t=1zOzgw7NkBelMe8b-1)

## Summary of Outputs

---

### Research & Modeling outputs

|  | Legal Opinion | Storyboard | Article | Internal discussions | New modeling |
| --- | --- | --- | --- | --- | --- |
| Quantity | 1 | 2 | 2 + 1 | 2 | 1 |

List of outputs
  - Internal discussion
    - How to migrate TON DAO v0.1 ([link](https://docs.google.com/presentation/d/1QpZlX6HiBSRKl9nf8pdRDkLVYaRd1XShUAgY16VBHdU/edit?usp=drive_link))
    - How to migrate TON DAO v0.2 ([link](https://docs.google.com/presentation/d/16MrQwQsyBDhWyI-aWSQQ0A5KasSc4ZuoktV78RO0gBk/edit#slide=id.g1f6029690e0_0_54)) 
  - Storyboard
    - [Bridge storyboard guidelines](https://docs.google.com/presentation/d/1wlekH_W6jooANOKtY1hDy_f97nC3F1xVlvSvM23e10U/edit#slide=id.g22a0544c3ae_0_54)
    - [Staking storyboard guidelines](https://docs.google.com/presentation/d/1dAK8670YsrFmYACPLzL6xlIqSCWMnyc0IGzj_GwGDUo/edit)
  - Legal Opinion
    - [Legal opinion from Duane Morris](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/364ece05-825a-4160-9eb4-0aa2dd80fc98/Tokamak_-_Legal_Opinion_(19_April_2023).pdf)
  - Updated Seigniorage Model
    - update seigniorage model for support v1 & v2 ([link](https://docs.google.com/spreadsheets/d/19SEEVLMazPdkdqNJ5dr1dyVhzqT1V71jcNRlhjRuvGY/edit#gid=0))
  - Governance Article
    - part1 ([link](https://docs.google.com/document/d/1xIhrq4_Zkw6-a9WxgOSC7R53yHuXUakbIyQxMtoHXTw/edit#heading=h.8iaug3ydf42v))
    - part2 ([link](https://docs.google.com/document/d/1hhwE3kgajOMRziEp0qH65njkQzcGT_BUOUYKnpVIBZM/edit)) - WIP

---

### Development outputs 

|  | progress | note |
| --- | --- | --- |
| Staking V2 Contract | 100%(15%) | Initial development is finished but, it needs to be re-developed based on new model |
| DAO Contract | 100% | DAO development of new V2 DAO Members has been completed, but development is needed to enable V1+V2 members to mix and use together. |
| BridgeSwap Contract | 100% | created a contract to deposit with TON, WTON, and WETH at once. In addition to the basic Deposit, the DepositTo function has also been added. And TON and WTON can perform Deposit and DepositTo with approveAndCall. |
| Uniswap & Token Contract Deploy on Titan goerli, Titan | 100% | 1. Deploy deterministic deployment proxy on Titan Goerli, Titan
2. Deploy UniswapV3 Contract on Titan Goerli, Titan(upgraded solidity v0.8.0)
3. 0.01Fee Activation, set owner to Tokamak address on Titan Goerli, Titan
4. Deploy Permit2, Universal Router, Unsupported contracts on Titan Goerli, Titan
5. Deploy TON, TOS, USDC, USDT on Titan Goerli, Titan.
6. Create WETH/TON, TON/TOS, WETH/TOS, WETH/USDC, WETH/USDT pools on Titan Goerli, Titan.
7. Add Liquidity to pools on Titan Goerli, Titan
8. Test quote and swap on Titan Goerli, Titan. |
| Unified Interface (Swap & Bridge) | 100% | Pool will be developed in July. |
| Staking v2 subgraph | 30% | It can be continued after staking v2 contract development is finished |

---

### Design outputs 

|  | FW design | DAO design | Bridge design |
| --- | --- | --- | --- |
| Progres | 20% | 0% | 100% |
| Note | Staking 2 and FW storyboards were completed, but the design was not completed due to low priority. Storyboards will be updated and designed with Suah in July |  |  |

## Q3 Roadmap

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e265411a-fe4e-480e-a1a3-5eb38d20630c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBFRM4X%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1lc4nMpCEj1pv0dJYSQQyYQyDv02wXEK6fZaUIWmP4AiEA1M3A8guwdJPTL1Dnv0NYHBtuEiNh%2FZDVMBQBn4vYET0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDHtNsNZfNV2doMm00CrcAxzTyinwJicLgxG2idtvmWHAic4L7REmEqjbCwGwnmn4R%2BZKPfuREDL97lzHctLrL8ymyPlDiTrsJVQtokiwqLDXwjkxbETXqGnA2GiU%2BdZ2dGBNs9KQ19%2FFOG9zgY6LzVH92Y0MjPk78xvo9cGmwyEXF2%2B9k5Ml5w5Ea4LZjZMwyMOiRl08q8SjaZT4ojFyLuR4Oy%2FBInSyFudIJZkjSWgBaRJU04itXklEoMrjHDifhA9%2F52QrDyKXThI%2BzthIxQ4whEhdcbYqt5JGbnB%2BH9UGcWWhkz1%2FBTQaX22gFWyytxh7YXeyoiY7OStE5r3KdzpRbIRxFtWFGvB%2BSsBoxZdzfxO0y2PyKPBcqo9zrI4YsylIy5t6h8L8zd67hv5u6Va4k4VaywM3JUMHRlrnrAd%2B6S%2FNyWgcxiWcXaiUs%2Bpw%2BLTxuy6XIUZXVhi45zTbpgAEzFhPfIR%2FHvYqFmUZXRVTGrZfA15EomLZDPklxG6BnUxs%2Ba69vGHGsphFWFu6Sab9S5MYoHl%2FW9hvpTFoBMnGlkUExPW7xhQkxvBXpBJNxpC3COIn5GnzohTW3drgUcJE%2BNrmEq4DMRkYCVa0Zvk7PKHTw6DbOd7EFpjPVFVu0cpl40tlobKNzJs4MK6a28wGOqUBh07vBWx3K36DkFEfc1Y8PgD%2Fo3wQR39sAq4I51hPdrTe48zfEdbKZ9VVM2ekdFxp%2BBdUB14fLkfwZjn8jR9DFSOymor0puGuOh0ELBkweafO1K1HjZ6BW5OGnji7g763BQCR%2FPucugvL67rZSRqJK%2BhAK5vBNMNLA4xX%2FmcPyqR0QBhigbTMJ%2Bzru8mE266cSV89YcYacOv77SBFxtjNtjOTwB0W&X-Amz-Signature=6797ef8e11e4b7d065d0655836430b134d138b38247d15ef09c70f5aba19a8a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Q3 2023: What will we do?

## Details

### Research: Suah, Praveen

**Motivation**

- For the layer2 environment, research about l2 specified governance
- Support migration about Staking & DAO contract. 

**Goals**

- Writing DAO governance article
- Solve update seignorage v1 +v2 problem with contract team
- Research on how bedrock upgrade affects Fast Withdrawal

### Contract: Zena, Harvey

**Motivation**

- DAO development that V1+V2 committee can use together

**Goals**

- Develop & test DAO Contract
- Implement Staking V2 contract based on new model

### Service: Jason

**Motivation**

- Support all the functions related with bridge
- develop staking v2 subgraph

**Goals**

- Finalize Staking v2 subgraph

### Plan & Design: Ryan, Monica

**Motivation**

- Design TON staking v2 landing page & FW page

**Goals**

- Do storyboard / design works of TON staking v2 phase 2
  - Staking 2
  - Fast Withdraw
  - Landing Page

## Budget Request

|  | request |
| --- | --- |
| endowment | 20,300 |
| Q1 | 24,000 |
| Q2 | **24,000 + 3283** |

## Changes

- 

## Comments from Tokamak Network

[[May (1)]]