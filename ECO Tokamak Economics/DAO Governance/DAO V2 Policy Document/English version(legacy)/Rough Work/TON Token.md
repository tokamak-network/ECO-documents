- Supply Dashboard: [https://price.tokamak.network/#/](https://price.tokamak.network/#/) 
- Total Supply: 88,116,248 TON
- Circulating Supply: 49,381,422 TON 
- Circulating Supply (Upbit Standard):  70,658,266 TON
- Staked TON: Check the amount staked by the account.
  - Contract: SeigManager
  - Function: stakeOf(address account)
- As a user, how can I get the number of minting-able voting rights?
  - Contract: TokamakVoteERC20
  - Function: mintableAmount(address my_account)
- As a user, how can I get my voting rights?
  - Contract: TokamakVoteERC20
  - Function: mint(uint256 amount)
- As a user, how can I delegate my voting rights to a delegatee?
  - Contract: TokamakVoteERC20
  - Function: delegate(address to_delegatee)
- As a user, how can I read the voting weight?
  - Contract: Governor
  - Function: getVotes(my_account, snapshot_clock) 
    - my_account: Address of the account you wish to view
    - snapshot_clock: A snapshot block number, It must be a smaller block than the current block number.

```javascript
 // Read the voting weight from the token's built in snapshot mechanism (see {Governor-_getVotes}).
 
 let snapshot_clock  = await governor.clock(); // a snapshot block number
 let getVotes_a = await governor.getVotes(user_address, snapshot_clock) 
```
- How do I know the total number of additional voting tokens that can be minted?
  - (A) Currently Staked Total
    - Contract: SeigManager
    - Function: stakeOfTotal()
  - (B) Number of Votes 
    - Contract: TokamakVoteERC20
    - Function: totalSupply()
  - (C) Total number of votes that can be minted
    - (C) = (A) - (B)
-   How to know the total count of votable tokens?
  - Contract: TokamakVoteERC20
  - Function: totalSupply()

# How to Get Votable Token?

# Who can vote?

- **Token Presence**: Available in Ethereum and Titan 
- **Voting Eligibility**: 
  - TON holders on Ethereum can participate in voting since they need to utilize the simple staking service for governance participation
  - To use TON for voting, the owner must first stake their TON and complete the delegation process. Delegating staked TON assigns the voting power of your tokens to a **specific address**, enabling it to participate in voting. This address can either be your own or that of a trusted party whom you believe will act in the best interest of the Tokamak Ecosystem.
  - An important note: Similar to voter registration in a broader democracy, staked TON must be delegated before the voting period to be eligible for use in a vote. This means if you want your vote to count, you must delegate it in anticipation of any proposal you may be interested in.