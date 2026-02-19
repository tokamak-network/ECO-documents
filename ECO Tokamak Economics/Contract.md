## What we are doing NOW

- function description except bond and fast withdraw ([doc](/6708d576446c430483cfad093c100398))
- develop TONStakingV2, Layer2Manager contracts except bond and fast withdraw ([doc](/d5e44476c3c24f40aeb16272460bf420) , [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_1_stakingLayer2) ) 
- Make the contract usages guide for frontend ( except fast withdraw )  
  - [[(1st) Contract Usage Guide   ]]

## Previous outputs

### Jan

- study & QnA (A [note](https://hackmd.io/ledLT2qfRqO2FudJho-ZZQ?both=) on Tokamak L2 Cryptoeconomics  ) 
- Build the local optimism environment on mac for development.([commit](https://github.com/Onther-Tech/tokamak-optimism-test), doc)

### Feb

- TONStakingV2 Contracts 
  - How to ceasing the seigniorage distribution in the existing contract? ([doc](/08df84961e61418dbf064a5145266d0e))  
  - Study the updated the seigniorage distribution formula ([doc](/38a110408e0f40d3bf26fcfaac7618cc))  
  - contract function specifications ([doc](https://docs.google.com/spreadsheets/d/1GfdGprl-r4MXonwG_QBPzfApRvaWDaYe9fyAOVFUkIQ/edit#gid=0)) 
- L2 interface  
  - Building L1 and L2 test environments by forking mainnet and goerli ([doc](/1abe6cae1254419084c7455dc18b8e00))
  - L1/L2 contract Usage : ERC20 L1, L2 deploy & deposit, withdraw ([doc](/0d2c3aaeb83e49d0b1ad2d995223da1f), [commits](https://github.com/Onther-Tech/tokamak-optimism-test/commits/main))  
  - Study the fastWithdraw ([doc](/b346cb4f44ee4d69bff48fbdc47eb823))  

### Mar 

- TONStakingV2 Contracts (by @Zena)
  - [Contract-specific features](https://docs.google.com/spreadsheets/d/1GfdGprl-r4MXonwG_QBPzfApRvaWDaYe9fyAOVFUkIQ/edit#gid=0) 
  - [Function description ](/6708d576446c430483cfad093c100398)except fast withdraw.
  - 1st develop version
    - [Contract 1st design](/38a110408e0f40d3bf26fcfaac7618cc)  
    - develop TONStakingV2, Layer2Manager contracts except fast withdraw 
      - branch : [TSV2_1_stakingLayer2](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_1_stakingLayer2)
      - contract [test](/2e7a284037474c36bd7adb6cdd963e25), [commits ](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_1_stakingLayer2) 
      - [[(1st) Contract Usage Guide   ]]
  - 2nd develop version
    - [Contract 2nd Design](/48826d84d2b9440f93e49bb477302043) 
    - develop TONStakingV2, Layer2Manager contracts except fast withdraw
      - 2nd_dev: branch :  [TSV2_2_dao_committee](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_2_dao_committee) 
      - contract [test](/a14c2667a2384db8aea0db4e93374ad6), [commits](https://github.com/tokamak-network/tokamak-staking-v2/commits/TSV2_2_dao_committee) 
      - [[(2nd) Contract Usage Guide ]] 
- DAO 
  - analysis DAO Contract ([doc](/76de9c1b7f3f4d84bb3681c2416cd79f))