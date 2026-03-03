# 1. Performance in August

## Deliverables

- Shutting down simple staking & community version
  - X post([1](https://x.com/Tokamak_Network/status/1957362665850016009), [2](https://x.com/Tokamak_Network/status/1954801446777483757), [3](https://x.com/Tokamak_Network/status/1952257662927913167))

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c6a80804-1820-46c3-98c6-4a9791a7ab24/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA6NSGXN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFberZW7Ev40Td57kIgU6MSe6W95mfinU8VAcFyK6pocAiA4WOm9Zus3VrwZr%2BQ7bwGnY0BpQbovZAeL%2FC5N0GCBcCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMRbjT3qnsWjeaMvr%2FKtwD9NiYFsz2VWVNkqNtFOfYtyb3HeDyZHdrprAOou%2BWVI3cyIuVnF5xTQ5JEDCY6eYxrN400KpmibWsu9U7CMixpO3dF4MyhAAUJbyawias2WaWpgmeNEonhbhGfozoyaSFu5lyGsuiEBPPtfDHQUrV1zX80eM651JJYxMWInkB46mLttxFFG93zvEmZ8ku0Sbs2J5IhEjO5TO197%2FYZ%2BTVyLRhYg%2FlQQLT8KPlLBX1JDM52Qk7cJI3vQQY9pFLioLvcNMdJ0c0MKTCdEOV82Kyo6DZZjDeCzStSKLYjCm9bl%2B1pE6Mbez549yudD6WVb0xlNzNSBWcSnS1TFzbu7udG2cHfIQcqxP4UKl7lRnZ5q5Buy2or05NZlPnm0wzzP7hZztr8iS7HAZCQofamyugeFGdKukMhNOXBR44abxp2j7xFO0Z3IloKbgINZpMAj8rTvbzx5FaiHjTU3EbJR2cEvRPqugD8CZrbq%2FFEbBa50xyaY%2FGQSmYXfOWK1nQWyPvo9kEm39IibEdEY9gESJnE48A8FFi%2Fls913uvO1hHtX0dZ3O1b8WuCxHJ%2FYoy1h2Bq%2BrsVsOU71S%2B4CAffbaiLGXS4VYOi2eguJ3PWN%2BotzTsOW7w%2Ff0RDJgxUNsw7pnbzAY6pgFoi7FbOYgwxjKsTHHALfzaIeBTTEzB1%2FgKzJLHJAZYguM7X%2F13lHkCXcANBFp6Ovz21%2FbQvqGc%2BGePZw2cRUrhSYqKiHNMQVMPpwSTbVAQkUiutmWuoOyY0WilAD47wpyqark%2B3G6OoCLma23GmOB4%2F%2BLdVjI7zpL3jcqfKvcStlhfd%2B8E1OigREzdK6b1%2FFgwqKDe5HTRZypwYs%2BuAiOXMKYPC037&X-Amz-Signature=ddaf45b9a69d6ca045f51c9f04d65f024b579afd325a1e4e1bcfa83dd9a4c036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Staking 

- **Goals for this quarter**
  - Shutdown the Staking service & conversion to the community version
- **Progress**
  - Community version
    - 
  - Staking V2
    - 
  - Staking**:** 
    - [TON-total-supply data sheet](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004)  is updated ( 2025.7.31 data )
- **Change(compared with Q2 goals)**
**Tokamak Network Terminal**

  - Goals
    - Multi-device / Multi-wallet support
    - Configuring an LLM-Driven Development Environment
  - **Progress**
    - Implemented Staking tools(stake, unstake, withdrawal, …)
    - Implemented [DAO tools](https://github.com/hooki/tokamak-network-terminal/pull/12)
    - Added `/commit`, `/build` commands
    - Added Cursor / Claude Code contexts

### Tokamak DAO  

- **Goals for this quarter**
  - Completed the internal test for DAO Community version web application ([notice](https://tokamak-network.slack.com/archives/C07JU4P56MR/p1754542580637609?thread_ts=1752724118.411619&cid=C07JU4P56MR))
  - Open the community version for DAO V1 ( [medium](https://medium.com/tokamak-network/empowering-communities-announcing-the-dao-community-web-application-fa190133d7f7), [X](https://tokamak-network.slack.com/archives/C07JU42NK9R/p1755506608440329?thread_ts=1755502872.672329&cid=C07JU42NK9R) ) 
  - Shutdown the DAO frontend and backend
  - Publish DAO V2.0 policy document: add information about snapshot and forum
- **Progress**
  -  Develop the llm-prompts for DAO Agenda apps ([link](https://github.com/tokamak-network/dao-community-version/tree/main/prompts-for-llm/prompts))
  - Adding EIP-1271 functionality to the DAO Contract
    - DAO Contract EIP-1271 Development Purpose and Plan ([doc](/246d96a400a3803b92ded29124858fa0))
    - Basic architecture design and functional implementation ([doc](/255d96a400a38039a686dd044d4d6663))
    - Test script development and documentation ([doc](/255d96a400a38039a686dd044d4d6663#255d96a400a3809f853dc60d4757603c), [readme](https://github.com/tokamak-network/ton-staking-v2/blob/DAO-ERC1271upgrade/doc/en/erc1271-implementation.md))
    - Internal Review in progress ([doc](/25bd96a400a3808e8bf0ceaee46c1ca4), [slack](https://tokamak-network.slack.com/archives/C07JU4P56MR/p1756195760617419))
  - Organize DAO Agenda issues for the DAO Community version
    - issues ([1](https://github.com/tokamak-network/ton-staking-v2/issues/316), [2](https://github.com/tokamak-network/ton-staking-v2/issues/317), [3](https://github.com/tokamak-network/ton-staking-v2/issues/318), [4](https://github.com/tokamak-network/ton-staking-v2/issues/319), [5](https://github.com/tokamak-network/ton-staking-v2/issues/313), [6](https://github.com/tokamak-network/ton-staking-v2/issues/320), [7](https://github.com/tokamak-network/ton-staking-v2/issues/321), [8](https://github.com/tokamak-network/ton-staking-v2/issues/322), [9](https://github.com/tokamak-network/ton-staking-v2/issues/315), [10](https://github.com/tokamak-network/ton-staking-v2/issues/314), [11](https://github.com/tokamak-network/ton-staking-v2/issues/33#issuecomment-3209501844), [12](https://github.com/tokamak-network/ton-staking-v2/issues/312))
- **Change(compared with Q2 goals)**
  - Adding EIP1271 functionality to the DAO Contract

### Tokamak Economics

- **Progress**
  - Analyzed a theoretical foundation for the slashing mechanism ([pdf](https://drive.google.com/file/d/1SCESKKF-smd0RP-sbzypoHfKuQsOoD-B/view?usp=sharing))
  - Develop the Randomized Attention Test PoC ( [readme](https://github.com/tokamak-network/optimism/tree/feature/op-challenger-with-rat/op-challenger/rat/prompts#randomized-attention-test-rat-poc-with-llm), [commits](https://github.com/tokamak-network/optimism/commits/feature/op-challenger-with-rat/), prompts: [contract](https://github.com/tokamak-network/optimism/blob/feature/op-challenger-with-rat/op-challenger/rat/prompts/build_contracts.md), [ game](https://github.com/tokamak-network/optimism/blob/feature/op-challenger-with-rat/op-challenger/rat/prompts/spec_game.md) )
  - DisputeGame Analysis and Develop for Slashing
    - Develop & Deploy & Test the TONDisputeGameFactory, TONDisputeGame Contract ([doc](/245d96a400a380e8a26ed3fc04c942ae))

# 2. Goals in September

### Tokamak Staking Terminal  

- Multi-device / Multi-wallet support
- Configuring an LLM-Driven Development Environment

### Tokamak DAO

- Release of llm-prompts for DAO Agenda apps   
- Development of LLM prompts for DAO contract upgrades
- Submitting the DAO EIP-1271 Upgrade Agenda
- Developing EIP-1271 Upgrade Contracts Using AI Coding Assistants: Medium Post 

### Tokamak Economics

- Layer 2 ecosystem survey
- Publish the research paper of the slashing mechanism
- Update the RAT research paper
- The Randomized Attention Test PoC completed
- Development of LLM prompts for slashing

## 3. Others

- 

## 4. Comments from Tokamak Network

- 