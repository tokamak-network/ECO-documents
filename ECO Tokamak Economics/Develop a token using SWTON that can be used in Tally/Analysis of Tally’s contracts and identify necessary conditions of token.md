![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/19092f00-c3e2-4de0-9ba1-1aef74e17537/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-07-12_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.15.16.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DETVBHI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICdJWcMGZUo6ORh83x7twJinV3Ceo%2BHoazcszvjk7iyHAiA15OF9DoD8sz2cYqVYLp0NJVVllTMkwIB50EnauZ86XCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMl1X08Ylg%2FiryzyBIKtwDTQTE5nKK34ulAAlT2x8FTHcQuBbXzgFIhPtov9X31uSL2H12PUSt49IdRTzy8UlbNrsY6KyTHt3PWWlQBbjPHzeCp91bsxBfc9A2zDWtP71bAVEx30WO8bmOpwqaqrL1w3NCIl%2BkaS5fMjnwgIyyvUbe%2BV5dNRJ2Hd0NUhti2YgewY4qn1Y%2BMiJ32cX%2BTYnz7V%2BmY6r%2Fio2u2skLCOUMhgeSSK5AE0XwsIlbZVkVbHgzVWYzwWNz4sh1hCP%2FCoIMdb6bZORnvU4UqGlAAfvo51zmD%2B%2F8mt62jA6GaXXLo0DCrFmQbAdj5WFgrpfpOPP8C%2FPIuix46hrKed%2B%2BjdyoC9rZjiTrOFAZTMCnGOCmqI4h5grs6gtxR%2BIewhGbRAbBgVB%2FFkRywSTBXnPCQPdEXmuVmyGFIBCj%2B8%2FHrRLfuvmswJqARvKpCU%2FlXMoTYVVDMWxm68d3MltxP%2Bj9MJxDzh8iPPobpww%2Bl1VaAVxUX2YHdVagc1XEzjZpWwVpuY0AnuwP4gO%2BrVkvKbFsq5kCxlxSE9VUhEY6N2u3SDUcbPpkE%2F%2BuYXgE92TpvEumFM23I%2F80jTZHhK%2FJefOx8hRvlIplMDWJSYKbceL9m1vIdagdaVJlw7XzNWHEoRgwjZrbzAY6pgGDUvYpFjNekL3trbEkwKE3kYJCDUDPtlV9sMd7I%2BohTKdwXrPhccZvuIt7yQczbfPmFo3jCqkbPz6YGr7Uo8%2FbUOQEaYp0SHrezZT8fhnkIX4%2Fp2fsS1H9UxdV%2FR9I1eKo1QXaBZl2P7RyeNthjopIMdyiUrZn%2FF23rT9nsde0pDWwOGC1fUVR7Sa8%2FSaWG6ABw1LJukvh6brlAF8WtmwkVfuhur%2B9&X-Amz-Signature=5cafff1013db7da8565709710bea767210b538acea2d8f52663687aa2436b92a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Token (ERC20 or ERC721)  

- tracks token balances
  - It traces the balance  
  - SeigManager’s stakeOf(address account): the staked ton amount of account 
- tracks delegations & voting power 
  -  it includes  [ERC20Wrapper](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20#ERC20Wrapper).
    - [`constructor(underlyingToken)`](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20#ERC20Wrapper-constructor-contract-IERC20-)
    -  decimals()   
    - underlying()  
    - depositFor(address account, uint256 amount)  
    - withdrawTo(address account, uint256 amount)  
  - It requires a token contract that implements the [ERC20Votes interface](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20#ERC20Votes), so inherits  the [ERC20Votes](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20#ERC20Votes).
    - [https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/utils/Votes.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/utils/Votes.sol)
    - tracks delegations & voting power
    - clock() : Clock used for flagging checkpoints.
    - CLOCK_MODE() : Description of the clock
    - checkpoints(address account, uint32 pos):  Get the `pos`-th checkpoint for `account`. return Checkpoints.Checkpoint208
```javascript
struct Checkpoint208 {
    uint48 _key;
    uint208 _value;
}
```
    - numCheckpoints(address account) 
    - <u>**delegates**</u><u>(address account): Get the address </u><u>`account`</u><u> is currently delegating to.</u>
      -  *In fact, voting units must be delegated in order to count as actual votes, and *<u>*an account has to delegate those votes to itself if it wishes to participate in decisions and does not have a trusted representative.*</u>
    - getVotes(address account): Gets the current votes balance for `account`
    - getPastVotes(address account, uint256 timepoint) Retrieve the number of votes for `account` at the end of `timepoint`.
    - getPastTotalSupply(uint256 timepoint) Retrieve the `totalSupply` at the end of `timepoint`. Note, this value is the sum of all balances. It is NOT the sum of all the delegated votes!
    - **delegate**(address delegatee): Delegate votes from the sender to `delegatee`
    - **delegateBySig**(address delegatee, uint256 nonce, uint256 expiry, uint8 v, bytes32 r, bytes32 s): Delegates votes from signer to `delegatee`
- 
  - 

```javascript

 * - A counting module must implement {quorum}, {_quorumReached}, {_voteSucceeded} and {_countVote}
 * - A voting module must implement {_getVotes}
 * - Additionally, {votingPeriod} must also be implemented
```
- **UX tradeoffs**
  - Users will have to wrap their tokens to vote, and then unwrap them to use them in places that expect the unwrapped version. 
⇒ <u>They may also be confused </u>about where their token went after wrapping if their wallet doesn’t know about the wrapped version. In our case, on the Simple Staking screen, there is a staking amount, but it can be confusing if unstaking is not done. 
  - Token holders have to delegate their votes – even to themselves – before voting. The wrapping step could be combined with delegation to keep the process simpler for tokenholders.

# Governor 

[https://docs.openzeppelin.com/contracts/5.x/api/governance](https://docs.openzeppelin.com/contracts/5.x/api/governance)

- manage proposals (the entire proposal lifecycle)  and votes for your DAO
- Hold the parameters of the DAO (Quorum, proposal threshold) 
  - Quorum : the number of YES votes a proposal requires to be considered valid.
- Sends successful proposals to the TimeLock for execution
- summary of what it needs from token 
  - Token contract needs a **delegate()**, **delegateBySig()**, and **delegates()** functions** **to delegate votes from one user to another.
  - Token contract needs to have a clear definition of how to calculate the voting power of each token holder. Usually, one token = one vote, but you can also customize a formula based on the token supply. It needs to have these function definitions **getVotes()**, **getPastVotes() **and **getPastTotalSupply().**
  - Last but not least, your token contract needs to emit event logs for vote changes, token transfers, and delegation changes. It needs to have these specific events definitions **DelegateChanged**, **DelegateVotesChanged**, and **Transfer**.
[https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/utils/IVotes.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/utils/IVotes.sol)
- Governor Contract’s ProposalId 
  - [How to set up on-chain governance - OpenZeppelin Docs](https://docs.openzeppelin.com/contracts/5.x/governance#governor_governorstorage)
  - <u>Governor uses the hash of the proposal parameters </u><u>with the purpose of keeping its data off-chain by event indexing</u>.
  - Proposal's calldata didn't stored on-chain but are only emitted as events.
  - The proposal ID has a hash of everything, including calldata.
  - <u>**So, you need to decide whether to store the call data on-chain before developing a contract.**</u>
- COUNTING_MODE 
[Governance - OpenZeppelin Docs](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)

  - 현재설정 
• `quorum=for,abstain` means that both For and Abstain votes are counted towards quorum.
```javascript
function COUNTING_MODE() public pure virtual override returns (string memory) {
        return "support=bravo&quorum=for,abstain";
    }

```
- CLOCK_MODE
  - [OpenZeppelin Governor | Tally Docs](https://docs.tally.xyz/user-guides/tally-contract-compatibility/openzeppelin-governor#clock-mode)
  - `clock() → uint48`external
Clock used for flagging checkpoints. Can be overridden to implement timestamp based checkpoints (and voting).

Tally checks the contract lock using the [IERC-6372](https://eips.ethereum.org/EIPS/eip-6372) standard. We accept `blocknumber` and `timestamp` clock modes.

CLOCK_MODE() ⇒ mode=blocknumber&from=default

# TimelockController 

[Governance - OpenZeppelin Docs](https://docs.openzeppelin.com/contracts/4.x/api/governance#TimelockController)

[https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/TimelockController.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/governance/TimelockController.sol)

- Is the root of authority in a protocol. When a smart contract requires the DAO as an admin, it is the TimeLock controller address which is used. 
- Delays the execution of proposals to allow user to exit the system before a proposal is enacted. 
- Customizable Permissions for DAO designs where rolls such as PROPOSE, CANCEL, EXECUTE are not necessarily all controlled by the Governor (such as a security council for cancelling malicious proposals ) 
- 

# Fee

[Tally Fees | Tally Docs](https://docs.tally.xyz/knowledge-base/tally-fees)

Tally activated a **0.25% fee **for all executed transfer proposals as of July 1, 2024.

# Set parameters 

### Vote token

- vote token name
- vote token symbol
- vote token decimal

### Governor

- clockMode ( true for timestamp mode, false for block number mode) :
- governor name
- governor  votingDelay (A proposal is proposed and voting is possible after a votingDelay. )
- governor voting period
- governor quorumNumerator  ( Quorum numerator to denominator of 100 )
- proposalThreshold  ( Threshold to be able to propose. Set a non-zero value to prevent proposal spam. )
- voteExtension (if a late quorum is reached, how long should it be extended?)

### Timelock

-  minDelay ( Once a proposal is submitted to a timelock, the task can be executed after  minDelay )