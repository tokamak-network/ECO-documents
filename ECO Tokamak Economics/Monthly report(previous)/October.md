## 1. Developments in October

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO maintenance
  - Price dashboard maintenance
- **Achievement**
  - **Staking:** 
    - no progress
  - **DAO**: 
    - Add new contract & new function to existing contracts([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/959af1e8b48ef0a324f271f35b8f8ad65914d071))
    - resolve event monitor issue on Sepolia([commit](https://github.com/tokamak-network/tokamak-dao-server/commit/3c0b625a4d9688155b85f5101be12eba12b7fd2f))
    - update dao front-end to resolve on-chain effect related issues ([commit](https://github.com/tokamak-network/dao.tokamak.network/commit/b974cb6871398856de30b3e749ab034a4b143582))
  - **Price Dashboard**
    - Update price dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/6b0e589f51bed55b52470bb7752592f937dd73e3))

### Staking V2

- **Motivation**
  - To provide seigniorage to L2 Sequencer
- **Goals**
  - (service) Update UX/UI simple staking page 
  - (contract) internal audit, deployment staking v2.5 contracts on mainnet, propose an agenda for upgrading staking v2.5
  - (design) Finalize storyboard and design for staking V2
- **Achievement**
**Contract**

  - updated staking v2.5 contracts based on demo feedback and tested using mainnet fork ([github](https://github.com/tokamak-network/ton-staking-v2/issues?q=is%3Aissue%20is%3Aclosed))
  - Make scripts to test the staking v2.5 deployment using the agenda ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/test-mainnet/))
  - Rehearsal of upgrading staking v2.5 on the sepolia [#57 ](https://github.com/tokamak-network/ton-staking-v2/issues/57)doc
  - Test agenda with script on Mainnet Forking ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/mainnet-agenda-test/))
  - wrote a draft about the DAO agenda (doc)
  - create an agenda about upgrade Contract and Titan DAO registration on mainnet ([commits](https://github.com/tokamak-network/ton-staking-v2/commits/deploy-ton-staking-v2.5/), [commits2](https://github.com/tokamak-network/dao.tokamak.network/commits/fea/upgrade-DAOProxy-DAOlogic/))
  - Seminar for request code review about DAOContract for CodeReview ([doc](https://docs.google.com/presentation/d/1qFaCIWRjSEiPrK9VVp5XkQkzZ0nIioOkVG8LlxG_h4E/edit#slide=id.g2893ae05661_0_309), [seminar](https://drive.google.com/file/d/1RlvTvKh0ELAR-HguBAij-Oj9jD84AJBU/view))
  - Creating an English version of upgradedDAO readme ([github](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md))
  - Gas fee calculation required for deployment/setup and agenda submission [doc](https://docs.google.com/spreadsheets/d/1xxjDkQFRBJU8Lqbt5A3gB2tiZ6wl2rm7iV1wGiRUaxg/edit?gid=0#gid=0)
  - Preparing/Deploy staking v2.5 contracts on mainnet [#54, ](https://github.com/tokamak-network/ton-staking-v2/issues/54)doc

**Service**

  - Designed additional fixes for the [mobile version](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=14-8925&node-type=section&t=rpndbXf1xdnxhcuQ-11) of Simple Staking version 2.5
  - Designed additional modifications for Simple Stakingv2.5
  - Reflect feedback from the internal test to frontend([commit](https://github.com/tokamak-network/simple-staking-v2/commit/00fcbd8893c85b3ad9817b28ca17c649a74d6c5f))

**Design**

  - UX/UI design improvements for Simple Staking version 2.5 ([figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=82-240&node-type=frame&t=LjMYZN66Zk995F3d-11), [figma2](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=14-2740&node-type=frame&t=sCBPXgIjjH1zIKfa-11))
  - Designed additional fixes for Simple Staking Version 2.5 UX/UI ([Notion](/118d96a400a380cb950ac66fa311857f#118d96a400a380d7a3ffff13706867f6))
  - Reflected the github ux/ui feedback design after simple staking v2.5 internal testing. ([Notion](/118d96a400a380cb950ac66fa311857f#128d96a400a380edb745ce6f56d64246), [Figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=14-8924&node-type=section&t=teeXiewUsvE0Pxbm-11))
- **Progress(compared with Q3 goals)**
  - The service opening schedule was delayed because we needed to use the DAO agenda to upgrade smart contract. (expected opening date: Nov 20)

### Tokamak DAO V2 

- **Motivation**
  - Provide better UX/UI about the price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - Determine a voting style suitable for DAOv2
  - Research and identify how cross-chain governance can be implemented in DAOv2
- **Achievement**
  - Research on [Quadratic Voting in Gitcoin](https://docs.google.com/presentation/d/1-j9ElorDROxieqaZH67GjTXH8QlgOKnVkGcZn_DAXm0/edit#slide=id.g3071e1d25e4_0_0) and noted some observations. 
  - Quadratic voting seminar([Video](https://drive.google.com/file/d/11c7Pj_xhQKHv6MEDGHVuVbfc_o2oaTHX/view?usp=sharing))
  - shared QV research to get Kevin's comments([link](https://w1724828219-i4h810456.slack.com/archives/C07JU6K4KDY/p1729167410529389))
  - Research on Cross chain Governance ([Link](https://docs.google.com/presentation/d/1FpWxLS7gQZCLiI7jDNK3NFnW-5oA-iCkOZY90xIyCVY/edit?usp=sharing)) (40%)
- **Progress(compared with Q3 goals)**
  - Discussed the QV voting method with the team and made some conclusions
  - Researching Cross chain governance (40% completed)

## 2. Goals in November

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - **Service** - Set DAO infra on Holesky
  - **Design** **- **Simple staking UX/UI usability improvement

### Staking V2 

- **Motivation**
  - To give incentives to the L2 sequencer & improve UX / UI
- **Goals** 
  - Open TON Staking V2.5 
  - Register the 'Titan DAO' candidate on simple staking service 
  - Deploy & upgrade the TON Staking V2.5 Contracts on Holesky
  - Simple staking v2.5 UX/UI design finish.

### Tokamak DAO V2

- **Motivation**
  - Define the Policy document for DAO v2, which can be used as a reference for DAO v2 operations 
- **Goals**
  - Finalize policy document(It includes Proposal flow, Voting style, Security council, Quorum & threshold numbers)
  - Research the L2 DAO (Cross-chain Governance)
  - Research and design The Security Council Contracts 

## 3. Others

- We will research how we respond to when sequencer failure situation.
- 1 member can be joined to ECO(not confirmed)

## 4. Comments from Tokamak Network

- 