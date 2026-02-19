Temperature Check vs SC voting

# **Who can vote?**

- **TON token availability**: TON token is available on **Ethereum.**
- **Eligibility criteria**:
  1. **Staked TON Holders on Ethereum**:
    - Users must hold staked TON([Simple Staking Service](https://simple.staking.tokamak.network/staking)) to become eligible to vote.
  1. **Steps to Participate**:
    - **Stake TON**: Holders must stake their TON to begin the voting process.
    - **Mint Vote Tokens**: After staking, vote tokens are minted in a 1:1 ratio to the staked TON.
    - **Delegate Voting Power**: **Vote token** must be delegated to a **specific address** to assign voting power. This address can either be your own or that of a trusted party who will act in the best interests of the Tokamak Ecosystem.
    - Minting vote tokens and delegating voting power is typically a one-time process. However, if any remaining amount is available for minting, you can mint additional tokens and delegate them as needed.
  1. **Guide** - https://www.notion.so/tokamak/Tokamak-Tally-s-DAO-on-sepolia-142d96a400a381c8981ec50344ac7375#142d96a400a3815bb9f3cfc67eb0f5e8 
- **Key Reminder**:
  - Delegation must occur **before the voting period begins** for the account to be eligible. This is similar to voter registration, where preparation is essential to ensure your vote is counted for any proposal of interest.
  - Vote tokens are minted at a 1:1 ratio to the amount of staked TON.

# Token Supply Information

### **Supply Details**

- **Supply Dashboard**: [View Dashboard](https://price.tokamak.network/#/)
- **Total Supply**: 88,116,248 TON
- **Circulating Supply**:
  - General: 49,381,422 TON
  - Upbit Standard: 70,658,266 TON

---

### **Staking and Voting Rights**

### **Staked TON**

- **Check Staked Amount**:
  - Contract: `SeigManager`
  - Function: `stakeOf(address account)`

### **Minting and Delegation**

1. **Get Mintable Voting Rights**:
  - Contract: `TokamakVoteERC20`
  - Function: `mintableAmount(address my_account)`
1. **Mint Voting Rights**:
  - Contract: `TokamakVoteERC20`
  - Function: `mint(uint256 amount)`
1. **Delegate Voting Rights**:
  - Contract: `TokamakVoteERC20`
  - Function: `delegate(address to_delegatee)`
1. **Read Voting Weight**:
  - Contract: `Governor`
  - Function: `getVotes(my_account, snapshot_clock)`
    - **my_account**: Address of the account
    - **snapshot_clock**: A snapshot block number (must be less than the current block number).

Example Code:

```javascript
javascript
Copy code
let snapshot_clock = await governor.clock(); // Fetch snapshot block number
let voting_weight = await governor.getVotes(user_address, snapshot_clock);


```

---

### **Total Votable Tokens**

- **Contract**: `TokamakVoteERC20`
- **Function**: `totalSupply()`

### **Additional Voting Tokens**

- **(A) Currently Staked Total**:
  - Contract: `SeigManager`
  - Function: `stakeOfTotal()` ([Link](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#readProxyContract#F59))
- **(B) Number of Votes (Vote Token minted so far)**:
  - Contract: `TokamakVoteERC20`
  - Function: `totalSupply()`
- **(C) Additional Mintable Votes**:
  - Formula: `(A) - (B)`