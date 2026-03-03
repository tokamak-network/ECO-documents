> [!note]
> 💫 This is a guide for the Community Edition, which will be updated further as development progresses, keeping space for screenshots.

Since we won't be adding it to the official Tokamak Network docs, we'll write this guide in Notion first and discuss which platforms we'll publish it to after development.

# **Guide Structure (Current version)**

Intro
### **Simple staking**

**Introducing Tokamak Network's staking system.**

**1. Features**

Tokamak Network’s staking is used to select the DAO committee members that can vote on agendas. Here's how it works:

  - Users can stake their TON or WTON on DAO candidates to earn staking rewards and support the DAO candidate to become one of the DAO committee members.
  - The three DAO candidates with the highest staking can become DAO committee members, where they can vote on DAO agendas.

### **2. Page Information**

The initial screen of the staking page

![](images/105bf43c442c.jpg)

  1. **Home**
  - Click the Connect Wallet button to link your Metamask or Trezor wallet.
  - The blue graph shows the amount staked on Tokamak network by the staker each day, and the grey graph shows the actual APY each day. If you hover your mouse over the graph, you can see the total amount of daily staking and the actual APY.
  1. **Staking**
  - On the staking page, you can check information about the DAO candidates. If your wallet is connected, you can click the blue arrow on the right of each operator to see detailed information about the DAO candidate and the staking button. If your wallet is not connected, you can only see the details of the operator.
  - Once your wallet is connected, you can click the Staking button to stake your TON (or WTON) to a DAO candidate.

The information provided is as follows:

  - Total Staked: This is the total of staked TON.
  - Pending Withdrawal: This is the total amount of Unstake TON. This amount can only be withdrawn after the withdrawal delay period set by the DAO candidate (default is after 93,046 blocks, about 14 days) has passed.

### **3. Login**

You must first log in through wallet connection to access some features like staking and account information. You can select the wallet connection method by clicking the wallet connection button at the top right of the screen.

  - Log in with Metamask
    - Make sure you are connected to the Ethereum mainnet network. Then click the Connect Wallet button.
    - In the pop-up window, click the Metamask icon.
    - In the list of browser extensions, click the Metamask icon and select the account to connect to the service.
  - Log in with Trezor
    - Connect to Trezor wallet
![](images/7fc555be5780.png)

Stake
## **Stake**

**You can stake TON or WTON on DAO candidates and receive staking rewards over time.**

### **1. DAO candidate**

To stake TON in the DAO candidate list, click on the expand button on the right for more details.

![](images/1176757a5e49.jpg)

### **2. Staking information**

When the detail information window expands, check the information about the DAO candidate.

  - **Stakers**: The number of users who have staked to this DAO candidate
  - **Pending Withdrawal**: The total amount not withdrawn after executing unstake
  - **Your Staked**: The amount you have staked for the currently selected DAO candidate
  - **Unclaimed Staking Reward**: Unclaimed staking reward that has accumulated.

![](images/704300863d63.png)

### **3. Stake**

There is a simulator in the upper right corner of the staking screen. With this, you can calculate the expected return rate according to the amount and duration of staking.

![](images/923bca3d3421.jpg)

  - When you press the Simulator button, a popup appears.
  - Enter the TON to be staked.
  - Select the duration of the stake.
  - Click the Calculate button.
  - To close the popup, click the X button.
  - The expected amount of TON (or WTON) to be acquired during the selected period is displayed here.
  - USD value, APY, and KRW value of the TON amount to be obtained are displayed here.
  - When you click the Stake button, a popup window where you can stake appears.
  - To recalculate, click the Recalculate button.
  - When you click the Stake button, a popup window as below appears, and the quantity entered in the simulator is displayed identically, so you can conveniently execute staking immediately (quantity modification is also possible). You can stake TON or WTON.

![](images/56fddf43d3ff.png)

When you press the Stake button, a Metamask popup window opens in the browser's Metamask extension. Complete the staking by clicking confirm.

> [!note]
> ⚠️ If Stake button is disabled
>   - This phenomenon occurs when the DAO candidate does not stake 1,000.1 TON.

Withdraw
## **Withdraw**

**Introducing the process of withdrawing staked TON.**

There are two key points to note. First, withdrawing the staked amount requires two steps: unstaking and then withdrawing. Second, withdrawal is only possible after 93,046 blocks from unstaking (approximately 14 days).

Withdrawal delay period

  - Period: 93,046 blocks after unstaking (approximately equivalent to 14 days).

Sometimes, users say that even after waiting about two weeks (Withdrawal delay period), they haven't received their tokens. This problem usually happens when they forget to click the withdraw button after the unstaking period is over.

### **1. Unstake**

  - When you press the Unstake button, a pop-up appears.

![](images/5265bfd28840.png)

  - When the pop-up window appears, enter the amount of TON to be unstaked.
  - Click the Unstake button.

![](images/bf92cff7dcb3.png)

  - Click the confirm button in the Metamask popup that opens in the Metamask extension of the browser.

> [!note]
> ⚠️ Before unstaking, check if there are any unclaimed staking rewards
>   - After unstaking, any unclaimed staking rewards will be burned.
>   - If there are unclaimed rewards, claim them to Your Staked first

### **2. Withdraw**

  - You can withdraw after 93,046 blocks (~14 days) from unstaking. When you press the Withdraw button, a pop-up window appears.

![](images/41b48036c38a.png)

  - The amount ready for withdrawal is shown in the Withdrawable Balance. This is the amount that has undergone the two-week delay period after unstaking.
  - If you press the Withdraw button, the whole amount available for withdrawal is taken out. Partial withdrawal is not an option.

![](images/de321d31c767.png)

  - Click the confirm button on the Metamask popup to complete the transaction.

### **3. Restake**

After unstaking, you can restake at any time, provided you haven't made the withdrawal. The pending withdrawal amount will be displayed as 'Restakable Amount' in the pop-up window when you click the Restake button.

![](images/2b69c9a8fd08.png)

  - When you click the Restake button, a popup will appear.
  - The amount that can be restaked is displayed under the Restakable Amount. You can apply Restake to this entire amount at once, but not to just a portion of it.
  - Clicking the Restake button will open a Metamask popup window in your browser's Metamask extension. Confirm the action by pressing the confirm button.

Staking reward
## **Staking reward**

**Earn rewards through staking.**

To receive unclaimed staking rewards, move them to "Your Staked" by following these steps:

  - "Unclaimed Staking Reward" area displays the staking rewards you haven't received yet (referred to as number 1 in the image below).
  - To claim these rewards, first click on the "Add to Your Staked" section (number 2 in the image below).

![](images/cf0477f83571.png)

  - The corresponding amount is now added to your staking amount, i.e., Your Staked amount (number 3 in the picture below).
  - The Unclaimed Staking Reward area remains with a balance of 0.

![](images/29cbd0f77a8a.png)

Contract Address
Github (contract): [https://github.com/tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2)

| Contract | Ethereum Network |
| --- | --- |
| DAOCommitteeExtend | [0x72655449e82211624D5F4D2ABb235bB6Fe2fe989](https://etherscan.io/address/0x72655449e82211624d5f4d2abb235bb6fe2fe989) |
| PowerTONUpgrade | [0x0aa0191e9cc7be9b7228d4d3e3dd65749c93551f](https://etherscan.io/address/0x0aa0191e9cc7be9b7228d4d3e3dd65749c93551f) |
| SeigManager | [0x3B1e59C2Ff4b850d78AB50cb13a4A482101681b6](https://etherscan.io/address/0x3b1e59c2ff4b850d78ab50cb13a4a482101681b6) |
| SeigManagerMigration | [0x19bc9bf93e1abeb169c923da689ffd6a14582593](https://etherscan.io/address/) |
| SeigManagerProxy | [0x0b55a0f463b6DEFb81c6063973763951712D0E5F](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f) |
| DepositManager | [0x76C01207959DF1242C2824B4445CdE48eb55D2f1](https://etherscan.io/address/0x76c01207959df1242c2824b4445cde48eb55d2f1) |
| DepositManagerForMigration | [0xEA729c4e532c17CbdAd9149a1A7a645AECBc524C](https://etherscan.io/address/0xea729c4e532c17cbdad9149a1a7a645aecbc524c) |
| DepositManagerProxy | [0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e) |
| Layer2Registry | [0x296EF64487ECfddcDd03EaB35C81c9262dAB88Ba](https://etherscan.io/address/0x296ef64487ecfddcdd03eab35c81c9262dab88ba) |
| Layer2RegistryProxy | [0x7846c2248A7B4dE77E9C2Bae7FBB93bfC286837B](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b) |
| Candidate | [0x1A8F59017E0434EFc27e89640AC4b7D7d194C0a3](https://etherscan.io/address/0x1a8f59017e0434efc27e89640ac4b7d7d194c0a3) |
| CandidateFactory | [0xC5eb1c5Ce7196BdB49Ea7500CA18a1B9f1fA3fFB](https://etherscan.io/address/0xc5eb1c5ce7196bdb49ea7500ca18a1b9f1fa3ffb) |
| CandidateFactoryProxy | [0x9FC7100a16407eE24a79C834A56E6ECA555A5D7c](https://etherscan.io/address/0x9fc7100a16407ee24a79c834a56e6eca555a5d7c) |
| RefactorCoinageSnapshot | [0xef12310ff8A6e96357B7D2c4A759b19ce94f7DFB](https://etherscan.io/address/0xef12310ff8a6e96357b7d2c4a759b19ce94f7dfb) |
| CoinageFactory | [0xe8fAe91B80dd515c3D8B9FC02CB5B2ecFDDABf43](https://etherscan.io/address/0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43) |
| PowerTONSwapperProxy | [0x970298189050aBd4dc4F119ccae14ee145ad9371](https://etherscan.io/address/0x970298189050aBd4dc4F119ccae14ee145ad9371) |

# **Guide Structure (Community Edition version)**

1. Intro

   1.1. Detail

2. Stake

   2.1. Staking Information

   2.2. Stake

   2.3. Staking Calculator

3. Withdraw

   3.1. Unstake

   3.2. Restake

   3.3. Withdraw

4. L2 Operator

5. Contract Address

## 1. Intro

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/71573f82-bc59-49bf-a135-3601be6eadf7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=2574967ed2f3f1071f745f6d4f847c20a0681eafc663f211a934223281d50446&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When you first enter the Simple Staking Community Edition, you'll see a screen like the one above. On the left side of the main screen, you can see Staking APY, Total Staked amount, and seigniorage emission, and on the right side, you can see DAO Candidates. Please note that the Staking APY and Total Staked amount are different for each DAO Candidate, and if your staked amount is in a specific DAO Candidate, it will be displayed together.

### 1.1. Detail 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/63bac281-3261-4c5d-bc91-0b3a69d26e5d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=995c9e8af4864e41d52cf9bc1bad5bba1eb1b80610c400e615ab2ef0690202f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Clicking on a DAO Candidate will take you to its detail page. On the details page, you can see the Staking APY, Total Staked amount, and Commission rate for the selected DAO Candidate.
On this page, you can stake, unstake, and withdraw, and before you stake, you can use the staking calculator to see how much reward amount can be expected. You can check your balance in both TON/WTON, check your unclaimed staking rewards, and update your seigniorage.

## 2. Stake

### 2.1. Staking Information

When the detail information window expands, check the information about the DAO candidate.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/35f3c841-c343-483e-87b1-6cae1e14e8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=61fe10e75bfd1b3cd5b45ee5911c595ed654100ce0b1255c2c780f0c59495c04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Staking APY**: Expected annual percentage yield when you stake TON/WTON
- **Total Staked**: The total amount not withdrawn after executing unstake
- **Commission rate**: This type of commission allows the selected DAO Candidate to pay a portion of the reward to the DAO Candidate based on a preset percentage.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7897f62d-fff0-44b3-a317-674284ede4db/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=5f59e5ee72080d5e070a5d994131491390188c4f8a40b25dab7ab096c432674c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Your Staked amount**: The amount you have staked for the currently selected DAO candidate
- **Unclaimed Staking Reward**: The amount of Staking rewards you have not yet claimed. 

### 2.2. Stake

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f92e2912-d810-4d9a-b2b1-d4bce95c9e58/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=5b5686b6837a762b8b238b2c60f1df754a063f7119a688165cd8de205e74ed58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When you press the Stake button, a Metamask popup window opens in the browser's Metamask extension. Complete the staking by clicking confirm.

> [!warning]
> ⚠️ If Stake button is disabled
> - This phenomenon occurs when the DAO candidate does not stake 1,000.1 TON.

### 2.3. Staking Calculator

Press the Staking Calculator link and a popup will appear. Enter the TON you want to bet, select the time period and click the Calculate button to see the estimated profit (TON or WTON), along with the USD, APY and KRW value of the estimated profit. To proceed with staking, click the Stake button and a staking popup will open to reflect that, and you can also modify the quantity if necessary. To recalculate, you can use the Recalculate button. To close the popup, click the X button.

## 3. Withdraw

Introducing the process of withdrawing staked TON.

There are two key points to note. 

- First, withdrawing the staked amount requires two steps: unstaking and then withdrawing.
- Second, withdrawal is only possible after 93,046 blocks from unstaking (approximately 14 days).


Withdrawal delay period

- Period: 93,046 blocks after unstaking (approximately equivalent to 14 days).


> [!warning]
> ⚠️ Sometimes, users say that even after waiting about two weeks (Withdrawal delay period), they haven't received their tokens. This problem usually happens when they forget to click the withdraw button after the unstaking period is over.

### 3.1. Unstake

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/eb1bfde2-15ba-4aab-80e4-80cff3168754/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=8f4fbe8206873ad6a3e2f5b4b97a5eabeb203f56593a7f4f31013bc83fe34e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When you press the Unstake button, a Metamask popup window opens in the browser’s Metamask extension. Complete the unstaking by clicking confirm.

Enter the amount of TON to be unstaked.

- Click the Unstake button.
- Click the confirm button in the Metamask popup that opens in the Metamask extension of the browser.



### 3.2. Restake

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1cbcb365-d76b-42f1-a4d1-4e9dcb840750/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=1c101737419b24157f6adcd8ac9092f9aa9128ae38bba9e15e3f1f0cebebe4bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you unstaked and have not yet made a Withdraw, you can Restake to receive staking rewards again. If Restake is available, the Restake feature will be enabled next to Withdraw. Restake works in the same process as Stake. Restake is valid for Unstake amounts that you have not Withdrawn.

### 3.3. Withdraw

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/96497d43-5ae0-4fb0-9f7d-8583854cd218/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=96b6d5943e1a143555b8043c2eb71c18ffc5d51d19b99d7471985715124f80a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The amount ready for withdrawal is shown in the Withdrawable Balance. This is the amount that has undergone the two-week delay period after unstaking.

If you press the Withdraw button, the whole amount available for withdrawal is taken out. Partial withdrawal is not an option.

- Click the confirm button on the Metamask popup to complete the transaction.

## 4. L2 Operator

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e63df3b1-50cb-4fbe-8cb5-14f44b473fd5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=a47422e035b9aa4815e6fbaf0cfe6e158c5edec48c6f6f64958e3c67476ee3cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If the DAO Candidate you want to stake is L2, you will additionally be provided with Sequencer seigniorage information.

> [!warning]
> ⚠️ Note that DAO Candidates that are Layer2 are labeled L2 for easy identification.

- If you are a User - TON Bridged to L2 information and a link to it

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b2475c59-46a7-4581-8eab-cc6c049b91b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=66cdadf226546cccfe4ac09d9f0747024de6e4046c80a23317c75dc27a788dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- If you are an Operator - TON Bridged to L2 information and link, Claimable seigniorage quantity and Claim, Stake function

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e1b81cb4-0a43-4d6c-9d5b-58c4c54bacd7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZI7LQD2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BWJW0MkSh2LRU5UlwCxobZ3VSRmSqt3ulOmIcnZmWiAiBuyzdKlPMQJzj5Uwqe98z4c2o5JVUTOqzCVgr1LIiEqyr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMxkWYse0xW1bemlJaKtwDUBvXoB%2F4HiiFTdY9L9i1%2FGlxaTkp1lOQgaG2TTSjRiurtZhGwLwZZ2%2FqnTa36A3S3ruO6AOSmgdlezjfaCbo0xo8%2BK%2FPuXeCOsofWd9L0B%2FcP4uHYpC3j32rMCcw6bMP8hdIShtBeKc%2Fn9K5RzP4f6oQFK2VTx5WuLNNXKkfUhVBpKqj7Tf8eulU9esQsR1OTcMvov%2Fb8bm4W6WpvPP9YaBsbbvAuaRWxxcfAnDnjB43FZzw5zT63GZ7JZsSXy2BVqy9LZtG0Hk7fa46p6kVTDY5ayL%2BxmB6ZOvD0oicThncoJCwz%2BUAa8Z4BZ6wlcQ0Jm7aX6hu290RUNN7lgi47PMhKWjI9RnDfHTfM1530td5wJy4hvWiqpTHtKEldxhOXGmFrUZBPLVTj5KsxNzYsQHJ%2BO8u%2BvZZ%2BE3HmCW8OxSVL58%2Fhf0ZIQ7NA%2ByUkU2oaImWp5XSW5tL1A%2Bu6FRQWmOfA%2FRWFsiZUmphL5GmHKBCeH7QuTgF9y7DYyCvDsGNX%2FOONqT67IWybJ%2Ffa%2F34CcMcRkWFIE8za1oLd4o7lbPj52CQHCGmGWN3BfORTDb5T1WDCZd3iv8Qkvqh1xqeM8N7FSS58oHl%2BqDR%2B5C2oftyRUp2TcZY0Ve4o8Ewqu%2FazAY6pgHl4aEjMVYkpvnWB5lVmxUJN9vsilyFz3N%2FBnuvF5lvWOFsA39txEocAKhgIhyCjEBBbgp1kAXsJl%2BoNPZVHZH3odRKQz3RuyAm5zGWMVtQMkrXtxCXOHAANWzBWGxgkeCx6ZEXP4PBzIrmIQr3LPi0KNKEskXfAH3LKc%2BkWhg7kupn71h0TQD8LBMgOgVx4Ht50f%2BKN4ibCSv%2FD%2FvrDhMIFQi1F8V2&X-Amz-Signature=2f9a65d9441b2a6ea5e88d0b2692bf0bb3f4e5f6533309fbca6bff920d8ab8e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 5. Contract Address

Github (contract): [https://github.com/tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2)

| Contract | Ethereum Network |
| --- | --- |
| DAOCommitteeExtend | [0x72655449e82211624D5F4D2ABb235bB6Fe2fe989](https://etherscan.io/address/0x72655449e82211624d5f4d2abb235bb6fe2fe989) |
| PowerTONUpgrade | [0x0aa0191e9cc7be9b7228d4d3e3dd65749c93551f](https://etherscan.io/address/0x0aa0191e9cc7be9b7228d4d3e3dd65749c93551f) |
| SeigManager | [0x3B1e59C2Ff4b850d78AB50cb13a4A482101681b6](https://etherscan.io/address/0x3b1e59c2ff4b850d78ab50cb13a4a482101681b6) |
| SeigManagerMigration | [0x19bc9bf93e1abeb169c923da689ffd6a14582593](https://etherscan.io/address/) |
| SeigManagerProxy | [0x0b55a0f463b6DEFb81c6063973763951712D0E5F](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f) |
| DepositManager | [0x76C01207959DF1242C2824B4445CdE48eb55D2f1](https://etherscan.io/address/0x76c01207959df1242c2824b4445cde48eb55d2f1) |
| DepositManagerForMigration | [0xEA729c4e532c17CbdAd9149a1A7a645AECBc524C](https://etherscan.io/address/0xea729c4e532c17cbdad9149a1a7a645aecbc524c) |
| DepositManagerProxy | [0x0b58ca72b12F01FC05F8f252e226f3E2089BD00E](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e) |
| Layer2Registry | [0x296EF64487ECfddcDd03EaB35C81c9262dAB88Ba](https://etherscan.io/address/0x296ef64487ecfddcdd03eab35c81c9262dab88ba) |
| Layer2RegistryProxy | [0x7846c2248A7B4dE77E9C2Bae7FBB93bfC286837B](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b) |
| Candidate | [0x1A8F59017E0434EFc27e89640AC4b7D7d194C0a3](https://etherscan.io/address/0x1a8f59017e0434efc27e89640ac4b7d7d194c0a3) |
| CandidateFactory | [0xC5eb1c5Ce7196BdB49Ea7500CA18a1B9f1fA3fFB](https://etherscan.io/address/0xc5eb1c5ce7196bdb49ea7500ca18a1b9f1fa3ffb) |
| CandidateFactoryProxy | [0x9FC7100a16407eE24a79C834A56E6ECA555A5D7c](https://etherscan.io/address/0x9fc7100a16407ee24a79c834a56e6eca555a5d7c) |
| RefactorCoinageSnapshot | [0xef12310ff8A6e96357B7D2c4A759b19ce94f7DFB](https://etherscan.io/address/0xef12310ff8a6e96357b7d2c4a759b19ce94f7dfb) |
| CoinageFactory | [0xe8fAe91B80dd515c3D8B9FC02CB5B2ecFDDABf43](https://etherscan.io/address/0xe8fae91b80dd515c3d8b9fc02cb5b2ecfddabf43) |
| PowerTONSwapperProxy | [0x970298189050aBd4dc4F119ccae14ee145ad9371](https://etherscan.io/address/0x970298189050aBd4dc4F119ccae14ee145ad9371) |