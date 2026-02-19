Task: 

[Link](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1761656660861419)


Assess the current tokenomics situation (withdrawals, seigniorage distribution to users/DAO, etc.)

## Brainstorming    

Receive comments of members : [channel](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1762923836851959)   
  - Harvey
    - Total Withdrawal and Deposit Amount
    - Deposit and withdrawal amount for each Candidate
  - Jason 
    - We can also collect staking related data using [subgraph](https://thegraph.com/explorer/subgraphs/CJLiXNdHXJ22BzWignD62gohDRVTYXJQVgU4qKJEtNVS?view=Query&chain=arbitrum-one)
      - For 1. To get a good understanding of Token Economics at the moment, I think we'll only have to see if we have an l2 sequencer registered in the mainnet staking and how much activity there is related to staking on that side.
      - For 2. Who need those data?
  - Bernard
    - What matters most is what properties we aim to extract through statistics.
In my case, it’s the relationship with price. 

      - Any statistical indicators related to a token’s **demand, supply, and velocity **are useful.
      - For **demand**, metrics such as staking APY, the number of relevant wallets, and transaction counts are helpful. 
      - For **supply**, total issuance, circulating supply, and burned amount are important. 
      - For **velocity**, CEX/DEX trading volume, net staking amount, and net deposits across all types of liquidity pools are useful.
      - Some of these may not be directly related to Tokamak, though.
    -  If that metric is really needed, you can borrow the concept of VWAP (Volume-Weighted Average Price) from the stock market: [https://en.wikipedia.org/wiki/Volume-weighted_average_price](https://en.wikipedia.org/wiki/Volume-weighted_average_price)
      - In this case, you replace “price” with “staking duration.” For example, if A stakes 100 TON for 30 days, B stakes 50 TON for 100 days, and C stakes 200 TON for 10 days, then: ((100×30) + (50×100) + (200×10))/(100+50+200) = 28.6.All of this data can be obtained on-chain. If this isn’t what you had in mind, let me know, we can discuss further.
      - It can be called Volume-Weighted Average Stake (VWAS) or Volume-Weighted Average Staking Duration (VWASD).
  - Eugenie
    - I think distribution also matter, as it show if a small number of wallets can have great power over price. Also if we have a way to extract information about “social buzz” with respect to the token I think it could be helpful to track if the project is generating traction/interest, that could be a marker for price movement
    - I tried calculating the staking duration using simple matching logic: Match each stake with the next available unstake by the same depositor and calculate the duration between two events. I think even simple, it could still capture the “intention” of users. A more complex model would require tracking specific stake IDs or amounts & some assumptions about weighted average of each duration based on the amount, which I have not explored yet.I asked AI to generate py code for this. Please find the data file, the py script and the more detailed rationale in this folder: [https://drive.google.com/drive/folders/1sSTT7qahFA8d4NyE3D9UM0xVgeArX-yv?usp=drive_link](https://drive.google.com/drive/folders/1sSTT7qahFA8d4NyE3D9UM0xVgeArX-yv?usp=drive_link)
  - Jeongun Baek
    - Trends in Staking Volume Inflows and Outflows
By using the total staked amount at the start of the period, the staked amount at the end of the period, and the quantity of tokens distributed as rewards during that period, we can identify trends in inflows and outflows based on a set cycle.
  - Suhyeon
    - For the way to show, Dune dashboard must be most efficient and intuitive. How do you think? But, some data might not be accessible using Dune API.
    - If we decide to use Dune, we can cowork for the dashboard 
  - Zena
    - Additional staked amount during a specific period
    - Amount withdrawn during a specific period
    - Current total staked amount (as a percentage of total circulating supply)
    - Increase/decrease trend of the staked percentage of total circulating supply

### **1. Key Metrics & Data Points Proposed**

- **Basic Staking Flows:**
  - **Harvey:** Monthly withdrawal/deposit amounts and breakdowns by candidate.
  - **Zena:** Additional staked amounts, withdrawn amounts, current staked percentage relative to circulating supply, and trend analysis of that percentage.
  - **Jeongun Baek:** Trends in inflows/outflows based on start/end periods and reward distribution.
- **Price-Correlation Metrics (Bernard):**
  - **Demand:** Staking APY, wallet counts, transaction counts.
  - **Supply:** Total issuance, circulating supply, burned amount.
  - **Velocity:** CEX/DEX volume, net staking amount, net deposits in liquidity pools.
- **Behavioral & Sentiment Metrics (Eugenie):**
  - **Distribution:** Wallet concentration (to see if specific addresses hold power over price).
  - **Social Buzz:** Tracking project traction/interest.
  - **Staking Duration:** Average time tokens are held (indicator of intention to hold/sell).

### **2. Tools & Methodology**

- **Data Sources:** Jason suggested using **subgraphs** (specifically for L2 sequencer activity on mainnet).
- **Visualization:** Suhyeon and Jeongun Baek agreed to collaborate on creating a **Dune Dashboard**, noting it as the most efficient tool, though some data accessibility might need verification.

### **3. Deep Dive: Calculating "Average Staking Duration"**

- **The Challenge:** Zena questioned how to calculate the average duration when staking and unstaking amounts differ.
- **Proposed Solution 1 (Eugenie):** Created a Python script using logic that matches specific stakes to the next available unstake event by the same depositor.
- **Proposed Solution 2 (Bernard):** Suggested a statistical approach based on the financial concept of VWAP (Volume-Weighted Average Price). He coined it **VWASD (Volume-Weighted Average Staking Duration)**.
  - *Logic:* Calculate the duration weighted by the amount staked to get a precise metric using on-chain data.

# Task 

Tokamak Network DUNE Dash board : [link](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard) 

- Basic Staking Metrics  →  Zena, Jeongun Baek, Suhyeon , Bernard 
  - Monthly/Weekly withdrawal/deposit amounts (breakdowns by candidate)
  - Monthly/weekly staked amounts
  - Monthly/weekly the staked percentage relative to circulating supply 
  - Trend on the staked percentage relative to circulating supply  
- Price-Correlation Metrics → Zena, Jeongun Baek, Suhyeon , Bernard 
  - **Demand:** Staking APY, wallet counts, transaction counts.
  - **Supply:** Total issuance, circulating supply, burned amount.
  - **Velocity:** CEX/DEX volume, net staking amount, net deposits in liquidity pools.
- Behavioral & Sentiment Metrics  →   Eugenie, Zena
  - **Distribution:** Wallet concentration (to see if specific addresses hold power over price).
  - **Social Buzz:** Tracking project traction/interest.
  - **Staking Duration:** Average time tokens are held (indicator of intention to hold/sell).

[[Task Details]]

## Work Repo

Work Repo : [https://github.com/tokamak-network/tools](https://github.com/tokamak-network/tools) 

## Available tools

- DUN Dashboard 
  - [Tokamak Network Tokenomics Dashboard](https://dune.com/tokamak-network/tokamak-network-tokenomics-dashboard)
- Price Dashboard 
  - [Tokamak Network](https://www.tokamak.network/about/price)
- [Subgraph](https://thegraph.com/explorer/subgraphs/CJLiXNdHXJ22BzWignD62gohDRVTYXJQVgU4qKJEtNVS?view=Query&chain=arbitrum-one)
- [Event Logs Folder](https://github.com/tokamak-network/tools/tree/master/get_all_transactions/logs_events)

## Helpful indicators

- TON/WTON addresses : [link](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md#ton-wton) 
- TON Price 
  - Price API : [link](/ad96519ceade4a1790f7ffb32a4091b4)
- TON Total Supply (on chain) 
  - SeigManager.totalSupplyOfTon()  :  [link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F79)  (ray unit, decimals 27) 
- TON Circulating Supply
  - Circulating Supply = TotalSupply - DAO Vault - Staked - VestedThe amount of circulating TON in the market 
  -  [https://price.api.tokamak.network/circulatedcoins](https://price.api.tokamak.network/circulatedcoins)
- Candidate Addresses  :  [link](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md#layer-addresses)
- TON Staked Amount by Candidate (on chain) 
  - Total staking amount based on seigniorage issuance
tot.balances(above coinage address of candidate) : tot.balanceOf( coinage address ) 
    - tot address: 0x47e264ea9b229368aa90c331D3f4CBe0b4c0f01d

balanceOf(address)  abi
```shell
[
{
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
]
```
  - Total staking amount based on seigniorage acquisition completion
CoinAge.totalSupply()
totalSupply() abi
```shell
[
{
      "inputs": [
        {
          "internalType": "address",
          "name": "layer2",
          "type": "address"
        }
      ],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
]
```
- Subgraph on TON Staking : document 
  - [https://github.com/tokamak-network/staking-v1-subgraph](https://github.com/tokamak-network/staking-v1-subgraph)
  - 
- 

## Gathering Simple Staking events 

Repo :  [tools/get_all_transactions at master · tokamak-network/tools](https://github.com/tokamak-network/tools/tree/master/get_all_transactions#tokamak-network-simple-staking-events-collector)

1. Modify the block numbers in v1_get_all_events.py
```shell
# Using https://etherscan.io/blockdateconverter
BLOCK_NUMBER_DEPOSIT_MANAGER_CREATED = 23029214 # After the contract patch is completed, the block that runs the update seigniorage
BLOCK_NUMBER_SNAPSHOT = 23780621
```
1. command 
```shell
python v1_get_all_events.py
```

results - console 
```shell
zena@MacBook-Pro-2 get_all_transactions % python v1_get_all_events.py
📊 Total block range: 23029214 ~ 23780621 (751,408 blocks)
📦 Chunk size: 9,990 blocks
📦 Total chunks: 76
🔍 Starting multi-event search (Deposited, WithdrawalRequested, WithdrawalProcessed)...

📦 Chunk 1/76: blocks 23029214 ~ 23039203
   ✅ Found 1 events

📦 Chunk 2/76: blocks 23039204 ~ 23049193
   ✅ Found 0 events

📦 Chunk 3/76: blocks 23049194 ~ 23059183
   ✅ Found 0 events

📦 Chunk 4/76: blocks 23059184 ~ 23069173
   ✅ Found 0 events

📦 Chunk 5/76: blocks 23069174 ~ 23079163
   ✅ Found 1 events

📦 Chunk 6/76: blocks 23079164 ~ 23089153
   ✅ Found 0 events

📦 Chunk 7/76: blocks 23089154 ~ 23099143
   ✅ Found 1 events

📦 Chunk 8/76: blocks 23099144 ~ 23109133
   ✅ Found 1 events

📦 Chunk 9/76: blocks 23109134 ~ 23119123
   ✅ Found 1 events

📦 Chunk 10/76: blocks 23119124 ~ 23129113
   ✅ Found 1 events

📦 Chunk 11/76: blocks 23129114 ~ 23139103
   ✅ Found 3 events

📦 Chunk 12/76: blocks 23139104 ~ 23149093
   ✅ Found 0 events

📦 Chunk 13/76: blocks 23149094 ~ 23159083
   ✅ Found 0 events

📦 Chunk 14/76: blocks 23159084 ~ 23169073
   ✅ Found 0 events

📦 Chunk 15/76: blocks 23169074 ~ 23179063
   ✅ Found 1 events

📦 Chunk 16/76: blocks 23179064 ~ 23189053
   ✅ Found 0 events

📦 Chunk 17/76: blocks 23189054 ~ 23199043
   ✅ Found 0 events

📦 Chunk 18/76: blocks 23199044 ~ 23209033
   ✅ Found 0 events

📦 Chunk 19/76: blocks 23209034 ~ 23219023
   ✅ Found 1 events

📦 Chunk 20/76: blocks 23219024 ~ 23229013
   ✅ Found 1 events

📦 Chunk 21/76: blocks 23229014 ~ 23239003
   ✅ Found 1 events

📦 Chunk 22/76: blocks 23239004 ~ 23248993
   ✅ Found 6 events

📦 Chunk 23/76: blocks 23248994 ~ 23258983
   ✅ Found 0 events

📦 Chunk 24/76: blocks 23258984 ~ 23268973
   ✅ Found 3 events

📦 Chunk 25/76: blocks 23268974 ~ 23278963
   ✅ Found 1 events

📦 Chunk 26/76: blocks 23278964 ~ 23288953
   ✅ Found 2 events

📦 Chunk 27/76: blocks 23288954 ~ 23298943
   ✅ Found 1 events

📦 Chunk 28/76: blocks 23298944 ~ 23308933
   ✅ Found 0 events

📦 Chunk 29/76: blocks 23308934 ~ 23318923
   ✅ Found 0 events

📦 Chunk 30/76: blocks 23318924 ~ 23328913
   ✅ Found 0 events

📦 Chunk 31/76: blocks 23328914 ~ 23338903
   ✅ Found 1 events

📦 Chunk 32/76: blocks 23338904 ~ 23348893
   ✅ Found 1 events

📦 Chunk 33/76: blocks 23348894 ~ 23358883
   ✅ Found 1 events

📦 Chunk 34/76: blocks 23358884 ~ 23368873
   ✅ Found 3 events

📦 Chunk 35/76: blocks 23368874 ~ 23378863
   ✅ Found 1 events

📦 Chunk 36/76: blocks 23378864 ~ 23388853
   ✅ Found 1 events

📦 Chunk 37/76: blocks 23388854 ~ 23398843
   ✅ Found 0 events

📦 Chunk 38/76: blocks 23398844 ~ 23408833
   ✅ Found 0 events

📦 Chunk 39/76: blocks 23408834 ~ 23418823
   ✅ Found 1 events

📦 Chunk 40/76: blocks 23418824 ~ 23428813
   ✅ Found 1 events

📦 Chunk 41/76: blocks 23428814 ~ 23438803
   ✅ Found 1 events

📦 Chunk 42/76: blocks 23438804 ~ 23448793
   ✅ Found 3 events

📦 Chunk 43/76: blocks 23448794 ~ 23458783
   ✅ Found 0 events

📦 Chunk 44/76: blocks 23458784 ~ 23468773
   ✅ Found 0 events

📦 Chunk 45/76: blocks 23468774 ~ 23478763
   ✅ Found 0 events

📦 Chunk 46/76: blocks 23478764 ~ 23488753
   ✅ Found 2 events

📦 Chunk 47/76: blocks 23488754 ~ 23498743
   ✅ Found 0 events

📦 Chunk 48/76: blocks 23498744 ~ 23508733
   ✅ Found 0 events

📦 Chunk 49/76: blocks 23508734 ~ 23518723
   ✅ Found 0 events

📦 Chunk 50/76: blocks 23518724 ~ 23528713
   ✅ Found 0 events

📦 Chunk 51/76: blocks 23528714 ~ 23538703
   ✅ Found 19 events

📦 Chunk 52/76: blocks 23538704 ~ 23548693
   ✅ Found 0 events

📦 Chunk 53/76: blocks 23548694 ~ 23558683
   ✅ Found 2 events

📦 Chunk 54/76: blocks 23558684 ~ 23568673
   ✅ Found 2 events

📦 Chunk 55/76: blocks 23568674 ~ 23578663
   ✅ Found 0 events

📦 Chunk 56/76: blocks 23578664 ~ 23588653
   ✅ Found 2 events

📦 Chunk 57/76: blocks 23588654 ~ 23598643
   ✅ Found 2 events

📦 Chunk 58/76: blocks 23598644 ~ 23608633
   ✅ Found 1 events

📦 Chunk 59/76: blocks 23608634 ~ 23618623
   ✅ Found 0 events

📦 Chunk 60/76: blocks 23618624 ~ 23628613
   ✅ Found 0 events

📦 Chunk 61/76: blocks 23628614 ~ 23638603
   ✅ Found 0 events

📦 Chunk 62/76: blocks 23638604 ~ 23648593
   ✅ Found 0 events

📦 Chunk 63/76: blocks 23648594 ~ 23658583
   ✅ Found 0 events

📦 Chunk 64/76: blocks 23658584 ~ 23668573
   ✅ Found 3 events

📦 Chunk 65/76: blocks 23668574 ~ 23678563
   ✅ Found 0 events

📦 Chunk 66/76: blocks 23678564 ~ 23688553
   ✅ Found 0 events

📦 Chunk 67/76: blocks 23688554 ~ 23698543
   ✅ Found 0 events

📦 Chunk 68/76: blocks 23698544 ~ 23708533
   ✅ Found 1 events

📦 Chunk 69/76: blocks 23708534 ~ 23718523
   ✅ Found 3 events

📦 Chunk 70/76: blocks 23718524 ~ 23728513
   ✅ Found 0 events

📦 Chunk 71/76: blocks 23728514 ~ 23738503
   ✅ Found 0 events

📦 Chunk 72/76: blocks 23738504 ~ 23748493
   ✅ Found 0 events

📦 Chunk 73/76: blocks 23748494 ~ 23758483
   ✅ Found 0 events

📦 Chunk 74/76: blocks 23758484 ~ 23768473
   ✅ Found 1 events

📦 Chunk 75/76: blocks 23768474 ~ 23778463
   ✅ Found 1 events

📦 Chunk 76/76: blocks 23778464 ~ 23780621
   ✅ Found 0 events

✅ Total 79 events found
📋 Event details:
[  1/79] Block 23032275 | 2025-07-30 22:35:11 | TX: 0x5a6a5e06... | Type: Withdrawal | Depositor: 0x3bFda92F... | Amount: 2515350000000000000000000000000 |  WTON: 2515.350000000000000000000000
[  2/79] Block 23073909 | 2025-08-05 18:16:47 | TX: 0x343cb40f... | Type: Deposited | Depositor: 0xA4Cb7fb1... | Amount: 1200000000000000000000000000000 |  WTON: 1200.000000000000000000000000
[  3/79] Block 23097048 | 2025-08-08 23:50:23 | TX: 0xe88bb53e... | Type: Withdrawal | Depositor: 0xbe173736... | Amount: 50000000000000000000000000000000 |  WTON: 50000.00000000000000000000000
[  4/79] Block 23103860 | 2025-08-09 22:40:59 | TX: 0x23935069... | Type: Withdrawal | Depositor: 0xfBd46D2A... | Amount: 6643610000000000000000000000000 |  WTON: 6643.610000000000000000000000
[  5/79] Block 23116799 | 2025-08-11 18:05:47 | TX: 0xab0c6720... | Type: Withdrawal | Depositor: 0xE2AC4733... | Amount: 7328680000000000000000000000000 |  WTON: 7328.680000000000000000000000
[  6/79] Block 23129004 | 2025-08-13 11:00:11 | TX: 0xc4c57f0e... | Type: Unstaking | Depositor: 0xc3C6C353... | Amount: 11820350000000000000000000000000 |  WTON: 11820.35000000000000000000000
[  7/79] Block 23131727 | 2025-08-13 20:07:35 | TX: 0xbb449d2c... | Type: Unstaking | Depositor: 0x7F9CEdeB... | Amount: 36270160000000000000000000000000 |  WTON: 36270.16000000000000000000000
[  8/79] Block 23131765 | 2025-08-13 20:15:11 | TX: 0x1f1770ed... | Type: Deposited | Depositor: 0x7F9CEdeB... | Amount: 36270160000000000000000000000000 |  WTON: 36270.16000000000000000000000
[  9/79] Block 23139085 | 2025-08-14 20:48:11 | TX: 0x36add7b4... | Type: Unstaking | Depositor: 0x0c37eBe8... | Amount: 7459310000000000000000000000000 |  WTON: 7459.310000000000000000000000
[ 10/79] Block 23173006 | 2025-08-19 14:24:23 | TX: 0x7b997aa0... | Type: Deposited | Depositor: 0x6Dd786E7... | Amount: 498940000000000000000000000000 |  WTON: 498.9400000000000000000000000
[ 11/79] Block 23214152 | 2025-08-25 08:11:11 | TX: 0xcbac09cd... | Type: Withdrawal | Depositor: 0x9310eF04... | Amount: 1026000000000000000000000000000 |  WTON: 1026.000000000000000000000000
[ 12/79] Block 23225874 | 2025-08-26 23:26:23 | TX: 0xc8a9fb6b... | Type: Unstaking | Depositor: 0x44BFc835... | Amount: 5000000000000000000000000000000 |  WTON: 5000.000000000000000000000000
[ 13/79] Block 23238314 | 2025-08-28 17:06:35 | TX: 0xa942187f... | Type: Withdrawal | Depositor: 0x0c37eBe8... | Amount: 7459310000000000000000000000000 |  WTON: 7459.310000000000000000000000
[ 14/79] Block 23241437 | 2025-08-29 03:34:59 | TX: 0x36c90c0a... | Type: Unstaking | Depositor: 0xCC2f386a... | Amount: 1000000000000000000000 |  WTON: 0.000001000000000000000000000
[ 15/79] Block 23241450 | 2025-08-29 03:37:35 | TX: 0xd1a3c24b... | Type: Unstaking | Depositor: 0xCC2f386a... | Amount: 100000000000000000000000000000 |  WTON: 100.0000000000000000000000000
[ 16/79] Block 23242249 | 2025-08-29 06:17:59 | TX: 0xf3004ca3... | Type: Withdrawal | Depositor: 0xCC2f386a... | Amount: 104340000000000000000000000000 |  WTON: 104.3400000000000000000000000
[ 17/79] Block 23242301 | 2025-08-29 06:28:23 | TX: 0xf8fb2c89... | Type: Unstaking | Depositor: 0xCC2f386a... | Amount: 30000000000000000000000000000 |  WTON: 30.00000000000000000000000000
[ 18/79] Block 23244748 | 2025-08-29 14:39:35 | TX: 0xade92adf... | Type: Unstaking | Depositor: 0x7EE93e58... | Amount: 4260000000000000000000000000 |  WTON: 4.260000000000000000000000000
[ 19/79] Block 23245413 | 2025-08-29 16:53:11 | TX: 0x5045e79b... | Type: Withdrawal | Depositor: 0x340C4408... | Amount: 30000000000000000000000000000000 |  WTON: 30000.00000000000000000000000
[ 20/79] Block 23264937 | 2025-09-01 10:14:47 | TX: 0xc9f45f4c... | Type: Deposited | Depositor: 0x7511CA0A... | Amount: 1000000000000000000000000000 |  WTON: 1.000000000000000000000000000
[ 21/79] Block 23265485 | 2025-09-01 12:04:47 | TX: 0x0acf5a37... | Type: Deposited | Depositor: 0x7511CA0A... | Amount: 9000000000000000000000000000000 |  WTON: 9000.000000000000000000000000
[ 22/79] Block 23267727 | 2025-09-01 19:36:23 | TX: 0x569b7644... | Type: Withdrawal | Depositor: 0xc3C6C353... | Amount: 11820350000000000000000000000000 |  WTON: 11820.35000000000000000000000
[ 23/79] Block 23275347 | 2025-09-02 21:14:11 | TX: 0x17fd551b... | Type: Deposited | Depositor: 0x44BFc835... | Amount: 2015350000000000000000000000000 |  WTON: 2015.350000000000000000000000
[ 24/79] Block 23283145 | 2025-09-03 23:21:11 | TX: 0x2fc51a2d... | Type: Unstaking | Depositor: 0xbe173736... | Amount: 53987080000000000000000000000000 |  WTON: 53987.08000000000000000000000
[ 25/79] Block 23287553 | 2025-09-04 14:07:23 | TX: 0x916eeb45... | Type: Deposited | Depositor: 0xA4Cb7fb1... | Amount: 667000000000000000000000000000 |  WTON: 667.0000000000000000000000000
[ 26/79] Block 23293851 | 2025-09-05 11:13:47 | TX: 0x74315f5d... | Type: Deposited | Depositor: 0x0c4a118C... | Amount: 600000000000000000000000000000 |  WTON: 600.0000000000000000000000000
[ 27/79] Block 23330566 | 2025-09-10 14:21:11 | TX: 0x6ccf65d2... | Type: Deposited | Depositor: 0x3548ca2F... | Amount: 19713400000000000000000000000000 |  WTON: 19713.40000000000000000000000
[ 28/79] Block 23343484 | 2025-09-12 09:45:23 | TX: 0x011f7538... | Type: Deposited | Depositor: 0x4DC3f3aF... | Amount: 674250000000000000000000000000 |  WTON: 674.2500000000000000000000000
[ 29/79] Block 23352537 | 2025-09-13 16:04:47 | TX: 0x74df6136... | Type: Unstaking | Depositor: 0xA91E9464... | Amount: 30000000000000000000000000000000 |  WTON: 30000.00000000000000000000000
[ 30/79] Block 23362597 | 2025-09-15 01:44:59 | TX: 0x33ce0216... | Type: Withdrawal | Depositor: 0x44BFc835... | Amount: 5000000000000000000000000000000 |  WTON: 5000.000000000000000000000000
[ 31/79] Block 23362640 | 2025-09-15 01:53:35 | TX: 0xb3318b2c... | Type: Deposited | Depositor: 0x44BFc835... | Amount: 520000000000000000000000000000 |  WTON: 520.0000000000000000000000000
[ 32/79] Block 23366233 | 2025-09-15 13:55:59 | TX: 0x42621996... | Type: Unstaking | Depositor: 0xA4Cb7fb1... | Amount: 2000000000000000000000000000000 |  WTON: 2000.000000000000000000000000
[ 33/79] Block 23376494 | 2025-09-17 00:21:59 | TX: 0x1787334c... | Type: Withdrawal | Depositor: 0xbe173736... | Amount: 53987080000000000000000000000000 |  WTON: 53987.08000000000000000000000
[ 34/79] Block 23380110 | 2025-09-17 12:27:47 | TX: 0x6157cb1e... | Type: Unstaking | Depositor: 0x32594AeA... | Amount: 2806840000000000000000000000000 |  WTON: 2806.840000000000000000000000
[ 35/79] Block 23417093 | 2025-09-22 16:31:23 | TX: 0x14a68f4d... | Type: Deposited | Depositor: 0x44BFc835... | Amount: 2000000000000000000000000000000 |  WTON: 2000.000000000000000000000000
[ 36/79] Block 23424928 | 2025-09-23 18:47:11 | TX: 0xdf7ed6c9... | Type: Withdrawal | Depositor: 0x7EE93e58... | Amount: 4260000000000000000000000000 |  WTON: 4.260000000000000000000000000
[ 37/79] Block 23432166 | 2025-09-24 19:01:11 | TX: 0x9086af54... | Type: Unstaking | Depositor: 0xB9147b53... | Amount: 16371900000000000000000000000000 |  WTON: 16371.90000000000000000000000
[ 38/79] Block 23439179 | 2025-09-25 18:33:11 | TX: 0x981d2c73... | Type: Withdrawal | Depositor: 0xCC2f386a... | Amount: 1000000000000000000000 |  WTON: 0.000001000000000000000000000
[ 39/79] Block 23439179 | 2025-09-25 18:33:11 | TX: 0x981d2c73... | Type: Withdrawal | Depositor: 0xCC2f386a... | Amount: 100000000000000000000000000000 |  WTON: 100.0000000000000000000000000
[ 40/79] Block 23439179 | 2025-09-25 18:33:11 | TX: 0x981d2c73... | Type: Withdrawal | Depositor: 0xCC2f386a... | Amount: 30000000000000000000000000000 |  WTON: 30.00000000000000000000000000
[ 41/79] Block 23479517 | 2025-10-01 09:55:23 | TX: 0xc018ce3b... | Type: Withdrawal | Depositor: 0xA91E9464... | Amount: 30000000000000000000000000000000 |  WTON: 30000.00000000000000000000000
[ 42/79] Block 23479728 | 2025-10-01 10:37:35 | TX: 0xefc50997... | Type: Withdrawal | Depositor: 0x32594AeA... | Amount: 2806840000000000000000000000000 |  WTON: 2806.840000000000000000000000
[ 43/79] Block 23530143 | 2025-10-08 11:45:35 | TX: 0x4895ddc5... | Type: Withdrawal | Depositor: 0xB9147b53... | Amount: 16371900000000000000000000000000 |  WTON: 16371.90000000000000000000000
[ 44/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0xE62651Df... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 45/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x79dEe95f... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 46/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x13213c3C... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 47/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x72f65B94... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 48/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x29f26577... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 49/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x4F3b6d77... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 50/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x6bB4353b... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 51/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0xd4D30125... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 52/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x34514537... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 53/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x3F59C6e7... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 54/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x58E66ABF... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 55/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x10BD35F4... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 56/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x5EF7b061... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 57/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x7093Ff67... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 58/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x079D2614... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 59/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0x018561D7... | Amount: 125000000000000000000000000000 |  WTON: 125.0000000000000000000000000
[ 60/79] Block 23532218 | 2025-10-08 18:43:11 | TX: 0x379d1c1c... | Type: Deposited | Depositor: 0xb6461ff4... | Amount: 150000000000000000000000000000 |  WTON: 150.0000000000000000000000000
[ 61/79] Block 23533452 | 2025-10-08 22:53:47 | TX: 0x5fe95ae7... | Type: Withdrawal | Depositor: 0xA4Cb7fb1... | Amount: 2000000000000000000000000000000 |  WTON: 2000.000000000000000000000000
[ 62/79] Block 23557672 | 2025-10-12 08:09:59 | TX: 0x9048985a... | Type: Unstaking | Depositor: 0x79dEe95f... | Amount: 149990000000000000000000000000 |  WTON: 149.9900000000000000000000000
[ 63/79] Block 23558597 | 2025-10-12 11:15:59 | TX: 0x0ec0a131... | Type: Unstaking | Depositor: 0x7093Ff67... | Amount: 126580000000000000000000000000 |  WTON: 126.5800000000000000000000000
[ 64/79] Block 23559333 | 2025-10-12 13:44:11 | TX: 0x411291de... | Type: Unstaking | Depositor: 0x018561D7... | Amount: 126580000000000000000000000000 |  WTON: 126.5800000000000000000000000
[ 65/79] Block 23566031 | 2025-10-13 12:10:59 | TX: 0x80bf7203... | Type: Unstaking | Depositor: 0xFe995E75... | Amount: 1000000000000000000000000000 |  WTON: 1.000000000000000000000000000
[ 66/79] Block 23580695 | 2025-10-15 13:25:11 | TX: 0xb0cd39e7... | Type: Unstaking | Depositor: 0x079D2614... | Amount: 126860000000000000000000000000 |  WTON: 126.8600000000000000000000000
[ 67/79] Block 23587034 | 2025-10-16 10:43:23 | TX: 0x9ed952da... | Type: Deposited | Depositor: 0x7511CA0A... | Amount: 1000000000000000000000000000000 |  WTON: 1000.000000000000000000000000
[ 68/79] Block 23588989 | 2025-10-16 17:18:47 | TX: 0x054ce9e0... | Type: Deposited | Depositor: 0xA4Cb7fb1... | Amount: 5162890000000000000000000000000 |  WTON: 5162.890000000000000000000000
[ 69/79] Block 23590931 | 2025-10-16 23:51:11 | TX: 0x8c5d0f01... | Type: Unstaking | Depositor: 0xFe995E75... | Amount: 3351310000000000000000000000000 |  WTON: 3351.310000000000000000000000
[ 70/79] Block 23598899 | 2025-10-18 02:32:59 | TX: 0xed37466a... | Type: Deposited | Depositor: 0x44BFc835... | Amount: 2200000000000000000000000000000 |  WTON: 2200.000000000000000000000000
[ 71/79] Block 23658686 | 2025-10-26 11:35:35 | TX: 0x930027eb... | Type: Withdrawal | Depositor: 0x79dEe95f... | Amount: 149990000000000000000000000000 |  WTON: 149.9900000000000000000000000
[ 72/79] Block 23658784 | 2025-10-26 11:55:11 | TX: 0x15c50bee... | Type: Withdrawal | Depositor: 0x7093Ff67... | Amount: 126580000000000000000000000000 |  WTON: 126.5800000000000000000000000
[ 73/79] Block 23658986 | 2025-10-26 12:35:35 | TX: 0xe192189d... | Type: Withdrawal | Depositor: 0x018561D7... | Amount: 126580000000000000000000000000 |  WTON: 126.5800000000000000000000000
[ 74/79] Block 23701060 | 2025-11-01 09:58:59 | TX: 0x7a29bbaf... | Type: Deposited | Depositor: 0x0c4a118C... | Amount: 1400000000000000000000000000000 |  WTON: 1400.000000000000000000000000
[ 75/79] Block 23710096 | 2025-11-02 16:17:35 | TX: 0xd9971d6d... | Type: Withdrawal | Depositor: 0x079D2614... | Amount: 126860000000000000000000000000 |  WTON: 126.8600000000000000000000000
[ 76/79] Block 23716007 | 2025-11-03 12:06:59 | TX: 0xa6081b97... | Type: Withdrawal | Depositor: 0xFe995E75... | Amount: 1000000000000000000000000000 |  WTON: 1.000000000000000000000000000
[ 77/79] Block 23716007 | 2025-11-03 12:06:59 | TX: 0xa6081b97... | Type: Withdrawal | Depositor: 0xFe995E75... | Amount: 3351310000000000000000000000000 |  WTON: 3351.310000000000000000000000
[ 78/79] Block 23762112 | 2025-11-09 22:51:11 | TX: 0x711d17f9... | Type: Unstaking | Depositor: 0x72f65B94... | Amount: 152500000000000000000000000000 |  WTON: 152.5000000000000000000000000
[ 79/79] Block 23775627 | 2025-11-11 20:14:47 | TX: 0x30035c30... | Type: Unstaking | Depositor: 0xA91E9464... | Amount: 30000000000000000000000000000000 |  WTON: 30000.00000000000000000000000
📄 CSV file saved: v1_23029214_23780621.csv

🎉 Analysis completed!
📊 Total events processed: 79
📄 Results saved to: v1_23029214_23780621.csv

📋 Summary: 79 total events processed 
```

  - result - file : create ‘v1_StartBlock_ENdBlock.csv 
    - Move the file to [this folder](https://github.com/tokamak-network/tools/tree/master/get_all_transactions/logs_events) : You can see log files. 
1. Items to extract for the token economic situation: 
 