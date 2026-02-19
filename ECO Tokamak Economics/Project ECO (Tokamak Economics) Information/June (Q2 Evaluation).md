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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b11790d0-455d-4993-a8bb-3bc27b772957/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EJMIQHI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T043618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE7ZjlqytgbcGqtu1UkDM2EHatnPWX1ZJ7hLTUNhPigbAiBkAiG5q6ejxvQoKW5qWWXWalqq2NN%2BbUwvqrQLVeI0PSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMfkBbOHVEsMg6DqC0KtwDCdW89ByFAZkY%2F3AXQFSysiGgkZ0kfh4vHRmkBlprBSRCHKeDpLJRx8k7l3Dz4GRUOrr%2FI%2Bhzd6J3z3yRfEV53xwX6th8oTK1Dt0smO0A9Qo0VgflzicOp%2BrtQfd2X72MqoqOOgzcERCqsyFOHEBXFzbnGU5kLKJSPKSLzpGxTCL%2BK%2BGj7YkTbPiGs4CezxRToKzNrdxnCLva3hQoUfwsL7QQihb2fpUeOXsvVr2lomwc3%2FFOnYCNL1sxVQ9x74MGJyaWCkpi7isc%2FQvZz0aonC2h71ko6lBuunALfvOCiK6TWW3IMVbN2DT2LAtmY2ipZRtzjc3IsIQOS6z2rOQ2dmk638gJRl%2BtsWpl5vpQf%2F6lV23P10ljUG9LX%2F9Nh9W06vFSHSdX33zd%2FkFk17bg6w3RMEB%2Fs2kbCPc%2FtH9jTAd7H7gv8Svq%2FlHj8%2BmcKdoeFi8tWzBMFJeVgdeGOsUGffo8mDslH53aJhZjSGlqZbYIIn14mWGcrJr7kA1bYcCJkrascXtUEunYY%2BQ2pAsl1Pt34W%2F6y5EJtqKHaqgaH4hr8fzT%2FOwEHMWLK63qVGYlXEyGQ33S%2FOXm2UqBqYox98ymg8YDxm0EzWFocR6QwVQF1LJaRfKVzk3W0%2BUw5e%2FZzAY6pgF2Y0yhmyP8ZxNPoNoHbqaRrqH3liSWCDY2S7fdizLe089572M%2BvfcCockYRS4ntlXfsNp2K0ZyVxXUGwnYrxTgzI9ehvi0seLV6VtaSGQ8Y2bJyElc6xk0QVwKJ3zoK%2BAf2dWuNBFcJJSNzX%2BWrlbSS2PRS7nr7ZYK%2FiZaW28buEjCeDfbmqSTkoDMTV2GFpsZKkKV%2BK7SyHST1M5DkR%2Bciz8NsI9Y&X-Amz-Signature=6a89940790fc5a42a250a89ea0af62270303b95f3bac701d61a8011beda53a85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

### Contract: Zena, Harvey, Justin

### Service: Jason

### Plan & Design: Ryan, Monica

## Summary of Outputs

## Q3 Roadmap

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e265411a-fe4e-480e-a1a3-5eb38d20630c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EJMIQHI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T043619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE7ZjlqytgbcGqtu1UkDM2EHatnPWX1ZJ7hLTUNhPigbAiBkAiG5q6ejxvQoKW5qWWXWalqq2NN%2BbUwvqrQLVeI0PSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMfkBbOHVEsMg6DqC0KtwDCdW89ByFAZkY%2F3AXQFSysiGgkZ0kfh4vHRmkBlprBSRCHKeDpLJRx8k7l3Dz4GRUOrr%2FI%2Bhzd6J3z3yRfEV53xwX6th8oTK1Dt0smO0A9Qo0VgflzicOp%2BrtQfd2X72MqoqOOgzcERCqsyFOHEBXFzbnGU5kLKJSPKSLzpGxTCL%2BK%2BGj7YkTbPiGs4CezxRToKzNrdxnCLva3hQoUfwsL7QQihb2fpUeOXsvVr2lomwc3%2FFOnYCNL1sxVQ9x74MGJyaWCkpi7isc%2FQvZz0aonC2h71ko6lBuunALfvOCiK6TWW3IMVbN2DT2LAtmY2ipZRtzjc3IsIQOS6z2rOQ2dmk638gJRl%2BtsWpl5vpQf%2F6lV23P10ljUG9LX%2F9Nh9W06vFSHSdX33zd%2FkFk17bg6w3RMEB%2Fs2kbCPc%2FtH9jTAd7H7gv8Svq%2FlHj8%2BmcKdoeFi8tWzBMFJeVgdeGOsUGffo8mDslH53aJhZjSGlqZbYIIn14mWGcrJr7kA1bYcCJkrascXtUEunYY%2BQ2pAsl1Pt34W%2F6y5EJtqKHaqgaH4hr8fzT%2FOwEHMWLK63qVGYlXEyGQ33S%2FOXm2UqBqYox98ymg8YDxm0EzWFocR6QwVQF1LJaRfKVzk3W0%2BUw5e%2FZzAY6pgF2Y0yhmyP8ZxNPoNoHbqaRrqH3liSWCDY2S7fdizLe089572M%2BvfcCockYRS4ntlXfsNp2K0ZyVxXUGwnYrxTgzI9ehvi0seLV6VtaSGQ8Y2bJyElc6xk0QVwKJ3zoK%2BAf2dWuNBFcJJSNzX%2BWrlbSS2PRS7nr7ZYK%2FiZaW28buEjCeDfbmqSTkoDMTV2GFpsZKkKV%2BK7SyHST1M5DkR%2Bciz8NsI9Y&X-Amz-Signature=88abf04953c71d8b0dd07160407355169feb3f40c628c14a4d8a2b9ecff4717f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Q3 2023: What will we do?

## Details

### Research: Suah, Praveen

### Contract: Zena, Harvey

### Service: Jason

### Plan & Design: Ryan, Monica

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