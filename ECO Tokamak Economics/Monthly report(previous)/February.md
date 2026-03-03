## 1. Developments in February

- In this quarter L2 Economics team will be working on 3 types of task

### Service maintenance 

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - Staking service maintenance
  - DAO service re-open
  - Price dashboard maintenance
- **Progress**
  - **Staking:** 
    - simple staking UI [update](https://www.figma.com/file/mjiyy4ImRFKlH8rzEtXN0h/2024.1.22-Simple-Staking-Page-Update?type=design&node-id=0-1&mode=design&t=F6aHZpXE3HIERueh-0) , [Desktop](https://tokamak-network.slack.com/archives/C0416F1TNE5/p1707267152171089?thread_ts=1707105885.396839&cid=C0416F1TNE5) & [Mobile](/468f5805a332473d96412b5cc5bffc53) - 1st week
    - modify simple stake to check operator's minimum collateral when stake. ( [doc](/607fc9970b5f48d6ba7dd0fc21764809), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/SeigManagerV1_2/) ) - 1st week
    - update staking page([commit](https://github.com/tokamak-network/simple-staking-v2/commit/cb03db90609420c4cb439ab50b46243dab2e2e72)) - 2nd week
    - set wallet page in staking ([commit](https://github.com/tokamak-network/simple-staking-v2/commit/732d136f038750f8fc07a99d31186f6b2a555237)) - 3rd week
  - **DAO**: 
    - modify DAO logic to strengthening DAO Committee qualifications through checking minimum collateral ([doc](/607fc9970b5f48d6ba7dd0fc21764809), [commits](https://github.com/tokamak-network/ton-staking-v2/commits/Agenda_Audit/)) 
    - deploy DAOCommitte_V1, SeigManagerV1_2 on mainnet and reopen DAO  ([doc](/b77464f38a7a4174a4173e6c5ae8dd59), [commits1](https://github.com/tokamak-network/ton-staking-v2/commits/SeigManagerV1_2/) ) 
    - prepare DAO re-open ([design](/ae0da156b2f346658aff622c60ef25bf), [front](https://github.com/tokamak-network/dao.tokamak.network/commit/5cf07ce49654abd55d1d151eed7580643ad450fa))
  - **Price Dashboard**
    - update link to dune dashboard([commit](https://github.com/tokamak-network/pricedashboard-v2/commit/b7ba6ff75c36166f8048b7d8658f07c62b5cce4b))
    - Dune Dashboard weekly update
    - Dune Dashboard mobile view update

### Staking V2 & FW (35%)

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
- **Goals**
  - Finalize FW model design
  - Seminar about research competitors
  - Determine overall UX for L2 registry and communicate with Core team
- **Progress**
  - **FW Modeling**
    - FW modeling: [mechanism design](/328d03ce7b30420cadc99ba6e5c73e02)
    - FW modeling and Game theory seminar
    - Current FW model analysis (WIP): [slides](https://docs.google.com/presentation/d/1bcXhBlm5uboiUvcbDIT9PhbN0RzFAVphtxFnnwKatPg/edit#slide=id.p)
    - Work on FW storyboard design with Monica
  - **Contract**
    - Building and testing FW development environment (tokamak-titan-canyon) ([doc](/1ea7e4c6b31a43f5aa74c0dba8dae620))
    - develop contracts that manages the L2 TVL to provide seigniorage, (20% , [contract design](/20b2ca5fe08e4986959d890fb2fb1d82), [L2Registry](/f7f2a0f242fa4171b45434810d6a32f4)**, **[Operator](/c3ef429695944ab5a67a8eb8b3df97c2), [OperatorFactory](/8e0abb3092ff4348997c87b07b0f8391), ** **[commits](https://github.com/tokamak-network/ton-staking-v2/commits/Layer2Manager/)** **)
  - **L2 Registry & Simple staking page **
    -  [Seminar_L2 On Demand Competitors](https://docs.google.com/presentation/d/161K61NwWdJNdZXfXOGPGUSyaS0vFzFX0JmPcr_QsRx0/edit?usp=sharing)
    - Rollup Deployment Demo: Caldera ([Slides](https://docs.google.com/presentation/d/1AlV80kW2UxmcYQ6Sz1wNws9H2xP_3FG0tTm8YkPTjBs/edit?usp=sharing))
    - L2 On Demand Storyboard :[ Initial version](https://www.figma.com/file/PUXcCtb9O0w5DMqc8cBNQ3/L2On-demand-Rollup-Storyboard?type=design&node-id=0-1&mode=design)
    - Seignorage simulation based on current white paper ([spreadsheet](https://docs.google.com/spreadsheets/d/1GKi5zEhSSRLz07PtHotioeUdZlyPGBxnipBu5h9Q1qw/edit#gid=0))

### Tokamak DAO V2 (18%)

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to improve DAO and communication with external parties
- **Goals**
  - write a draft policy framework for the DAO 
- **Progress**
  - **Model**
    - No progress
  - **Contract**
    - research & deploy the Contract about Tally use Token on Sepolia ([doc](/17fb45703ea549adbd9c9b58513f64e7), [commits](https://github.com/tokamak-network/tally-erc20/commits/main/))

## 2. Goals in March

### System maintenance

- **Motivation**
  - To maintain & update Tokamak Network’s service except for Tonstarter and Bridge
- **Goals**
  - re-open DAO

### Staking V2 & FW

- **Motivation**
  - To provide liquidity for the fast withdrawal request and make enable FW from Tokamak L2
  - Upgrade existing simple staking service to support registration and display of L2 reference chain (Titan, Thanos) information
- **Goals**
  - Make Staking V2 & FW storyboard
  - Improve existing idea to improve UX for the liquidity providers
  - Writing a manuscript (draft) about the FW model
  - PoC implementation on the FW model
  - Submitting a proposal of FW model research to Ethereum Academic Grant
  - develop & test the FW Contract 

### Tokamak DAO V2

- **Motivation**
  - Provide better UX/UI about price dashboard and use it to new DAO model
  - Using Tally for managing the new DAO.
- **Goals**
  - deploy tally DAO contract to test on sepolia
  - Test the tally interface with the deployed contracts of our token
  - Determine the further steps for integrating our DAO with Tally

## 3. Others

- 

## 4. Comments from Tokamak Network