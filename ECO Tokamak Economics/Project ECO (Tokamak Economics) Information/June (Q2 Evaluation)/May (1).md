## 1. Roadmap

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4fb296e7-e9af-4d36-a68a-4b7762fc5f45/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QTM3R66%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe%2BDZ3Ko9P80YdL%2B3PECv1EhroycwjU%2BCnkr9BtmQuuAiAKNbTvVmAhCZ29%2FxhhwnTlmWh3KJWQzqgzbTPcE%2BOW3yr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMGTCWK%2B6PyI%2Fa%2BZwAKtwDohXSTBDqYwq7ZUSPwOicbluykAR73pgUQLE2YFnJbq999MAk5idvA83vPwAcBJwk6cIVHa9RpMN0GQnl6kXo%2BU%2F%2B974EK1P%2BCvYVq5tW1rLDiNKFvacbvF%2F3VBhIUW%2FBnHWc0I%2FM4ZOfL%2BFmOQxJlOJ6fLK9XnHn%2BY3tnRb7gFpc9Lq%2BILhBRg72%2FfL78QtpoRgPuJ4ritMChqTvayRS1AMU5MlpuD3pgf1yN1U21ByYp4zg3z4hUmxbWXjk7baf8VXqsc7hX9R2POys9YQbw3qo%2Buhf22dX0udeCdqwUk9s9mF1Kmy6e%2BbGvQZb4oNPGfYI3YPQ6X0R8crjoMq2%2BpuyWS73%2BzqG5t6IInOL0oSTu59qHXN%2FuLnJENuMbL2z%2B20ZXDosi%2Bfp0CwLicjeLaFKe4VhHU2cv6rK%2FgoGNocD0NkJT3U9eJ3nej%2Bi%2BuKLpyizO8yWAzHBZdB2Cwpg2e5sPWnKkDx3SmkpCrDaIhlZzPq7VYyto%2FfbvZRWvRDcH%2Bf0Hdaqm1Jdfg9IW5SdcbjtXD31MIPxGJqkLefQvIsITY13gKEF7RpBambg2%2BdPEnGd4ySzWcSruD0zg0DIg2Oct%2FwbAbRzmj5G13oM4tzzAK%2Bb2ExOn8TlLfYwp5nbzAY6pgG8ZDG%2BKzmTTt0q3SCxSnV%2BGOZ2S1RR9rETOeo84ohatj0GRVCyjcHraAMaKiQNkVG6kD5o6EYymom3zpOsKuUE5jG%2Ft2atoeI0RuhaRCbcd5afSeZMGA4WF2dhCcWElRkTU84e91J7qXE8MTyBDlDxWGRxGrYooMMbjeL%2BPcXih0%2BS1YjwVELduEV9uyHpueKCfGKY4Us4VweOvLre8XHPiCIyfahk&X-Amz-Signature=02f07a46cdb3e3d32ea005384a809c51fa6a048bd36ca76776f362e73cf3f23d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**<modified roadmap>**

 There is a change in schedule due to changes to the design. Due to the issue of the distribution of seigniorage between V1 and V2, additional modeling is needed and further development of the contract is expected accordingly, so the external audit schedule has been postponed. Accordingly, the development schedule is adjusted

There are two major developments during May:

1. <u>**Integrated UI (Bridge + Tokamak Swap + Pool)**</u>

Based on our priority, Unified UI is under develop. And we can show demo of deposit & withdraw in Bridge part until next week.
1. <u>**Discussion about seigniorage distribution**</u>

## 2. Developments in May

### Research unit

**Motivation**

- Provide feedback to contract and design unit 
- Define a path for TON Governance

**Goals**

- Write the Governance Article series, and discuss the possible paths for progressive decentralization of TON Governance

**Progress**

- Governance Article Part 1([Draft](https://docs.google.com/document/d/1xIhrq4_Zkw6-a9WxgOSC7R53yHuXUakbIyQxMtoHXTw/edit?usp=sharing)), Part 2 ([WIP](https://docs.google.com/document/d/1hhwE3kgajOMRziEp0qH65njkQzcGT_BUOUYKnpVIBZM/edit?usp=sharing))

### Contract unit

**Motivation**

- Make the TON staking v2 contracts and finish to preparing the audit.
- Make the DAO V2 contract and how to preparing migration

**Goals**

- Finish developing TON Staking V2 contracts
- Go through internal audits of TONStakingV2 Contracts
- Finish developing DAO V2 contracts

**Progress**

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

### Plan/Design unit

**Motivation**

- Prepare for TON staking v2 phase 1 storyboard & design
- Design for Integrated UI - Swap/Bridge


**Goals**

- Finish Staking storyboard
- Finish Staking UI Design-TON Staking v1/v2, Tokamak Fast Withdraw 
- Integrated UI Design - Swap/Bridge

**Progress**

- [Staking storyboard0.2](https://www.figma.com/file/SQWkrz1nwjszjtZ23ar8id/Tokamak-L2-Storyboard?type=design&node-id=554-12514&t=grT27iUwfsjGMDzP-4)
- [Staking UI Design-TON Staking v1/v2](https://onther.slack.com/archives/C01G5GYKJ03/p1683712821522599)
- [Integrated UI Design -Swap/Bridge](https://www.figma.com/file/DSe0jpvapjNmM9m7UynelD/Tokamak-Uniswap-V3?type=design&node-id=743-6371&t=88GyAO3UqV0fLiUx-4)

### Front-end unit

**Motivation**

- Prepare implementation for 3 types of service
- There are too short time for implement service, so service team need to prepare  for it.


**Goals**

- Embark on developing the service page for bridge

**Progress**

- deposit, withdraw part in unified bridge ([commit](https://github.com/tokamak-network/Unified-interface/commit/535802cf79abd7891fdd7164e9f6b8b5ba48d43d)) - 80%
- Staking subgraph architecture v0.2([doc](/9f7cd5c147bd407cbaa37d85e3e87691)) - 70%
- Fw fee server ([commit](https://github.com/tokamak-network/fw-fee-server/commit/a07a308b5382fb5baefd8b7652e05ede24da2498)) - 30%
- Staking v2 subgraph ([commit](https://github.com/tokamak-network/staking-v2-subgraph/commit/4dc5c212383f2e641233b0b6d653a38fb4136346)) - 10%

## 3. Goals in June

### Research unit

- Finish Governance Article Series
- Design a gradual decentralization path for TON Governance

### Contract unit

-  Develop the DAO Contract
  - Develop the Logic(V1 and V2 can be used together)
  - make the Documentation of DAO V1 & V2 Contracts
- Develop TONStakingV2 Contracts 
  -  Documentation of TONStaking V2 Contracts 

### Plan/Design unit

- Finish Staking UI Design-Tokamak Fast Withdraw 
- Finish Integrated UI Design - Swap/Bridge

### Front-end unit

- Implement Staking v2 subgraph & fw fee server
- Start to implement staking fw

## 4. Others

- How we manage tokamak layer2 economics & uniswap v3 design?
- Contract team(zena & harvey) will support L2 team for documentation part @

## 5. Comments from Tokamak Network