## seigManagerV2 

- ton address
  -  [0x2be5e8c109e2197D077D13A82dAead6a9b3433C5](https://etherscan.io/address/0x2be5e8c109e2197D077D13A82dAead6a9b3433C5)
- wton address
  - [0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2](https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2)
- tot  
  - [0x6FC20Ca22E67aAb397Adb977F092245525f7AeEf](https://etherscan.io/address/0x6FC20Ca22E67aAb397Adb977F092245525f7AeEf)
- seigManagerV1 
  - [0x710936500aC59e8551331871Cbad3D33d5e0D909](https://etherscan.io/address/0x710936500aC59e8551331871Cbad3D33d5e0D909)
- layer2ManagerProxy 배포한후 사용
- optimismSequencerProxy 배포한후 사용
- candidateProxy 배포한후 사용
- seigPerBlock : the amount of seigniorage issued per block 
  - [3920000000000000000](https://etherscan.io/unitconverter?wei=3920000000000000000000000000)
- minimumBlocksForUpdateSeig : ( unused now, if you want to use, you can use) you can execute “update seigniorage” only once during  this blocks. 
  - **2400**
- ratesTonStakers : Give seigniorage as much as the staked percentage and give the remaining seigniorage to TonStakers what percentage
  - 0.4 → 4000 ( current V1 ) 
- ratesDao : Give seigniorage as much as the staked percentage and give the remaining seigniorage to DAO what percentage
  - 0.[5](https://etherscan.io/unitconverter?wei=500000000000000000000000000) → 5000 ( current V1 ) 
- ratesStosHolders : Give seigniorage as much as the staked percentage and give the remaining seigniorage to stos holders what percentage
  - 0.1 → 1000  ( current V1 ) 
- ratesUnits : 10000 
- dao address
  -  [0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303](https://etherscan.io/address/0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303)
- sTosHolders (powerTon address)
  -  [0x970298189050aBd4dc4F119ccae14ee145ad9371](https://etherscan.io/address/0x970298189050aBd4dc4F119ccae14ee145ad9371)
- lastSeigBlock : Change to v2, and specify the block that starts seignorage issued in v2.
  - 

## Layer2Manager 

- minimumDepositForSequencer : minimum security deposit amount of sequencer. [ref link](/6708d576446c430483cfad093c100398)
  - 
- **`ratioOfDeposit`**** : **What percentage of Layer 2's TON TVL will be determined as the minimum security deposit. [ref link](/6708d576446c430483cfad093c100398)
  - 0
- minimumDepositForCandidate : minimum staking  amount of candidate
  - 
- delayBlocksForWithdraw : the number of delay blocks to withdrawal after unstaking
  - 93046  ( current V1 ) 
- maxLayer2Count : How many layer 2 can be registered
  -  