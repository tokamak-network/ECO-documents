## Reason for writing document

Contracts analysis for using Tally

## What contracts are needed to use Tally?

- Token Contract : EIP-5805 compatible ERC20 or NFT (Simplily, ERC20 or NFT with delegation and voting checkpoint functions.)
- Governor Contract : A contract that has proposal writing and voting functions and is linked to token contracts and time contracts.
  - how voting power is determined
  - how many votes are needed for quorum
  - what options people have when casting a vote and how those votes are counted
  - what type of token should be used to vote
- TimeLock Contract : There is a function to delay the proposal before execution when the proposal is successful.

## Contract composition

1. TestToken.sol - When deploying, an owner address is required to execute the mint function.
  - Essential feature to become a Tally token
    - ERC20
    - ERC20Votes
    - ERC20Permit
  - Not a required feature, but an added feature
    - ERC20Burnable
    - Ownable
    - add mint function
1. TestTimelockController.sol - When deploying, you can set minDelay, proposers, executors, and admin, and it is okay to disable values except minDelay. Administrators can make initial configuration of a role and must relinquish the role of administrator after assisting with configuration.
  - Essential feature to become a Tally token
    - TimelockController
1. TestGovernance.sol - When distributing, the token address and TimelockController address are required. Setting values include the Governance name, votingDelay, VotingPeriod, ProposalThreshold, and Quorum number.
  - Governor
  - GovernorSettings
  - GovernorCountingSimple
  - GovernorVotes
  - GovernorVotesQuorumFraction
  - GovernorTimelockControl

## Deploy the Contract on Sepolia

- TestToken : [0x378ab8A2aC543EE02F9AA3d5Bac6fD66095B7b72](https://sepolia.etherscan.io/address/0x378ab8A2aC543EE02F9AA3d5Bac6fD66095B7b72)
- TestTimelockController : [0x01FABA905f875fEE44fB283cde00D718377Bd568](https://sepolia.etherscan.io/address/0x01FABA905f875fEE44fB283cde00D718377Bd568)
  - minDelay : 60 seconds
  - admin : 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea
- TestGovernance : [0x373e7ED1D1d435c303aA9e31EdC3d3F13D5473bD](https://sepolia.etherscan.io/address/0x373e7ED1D1d435c303aA9e31EdC3d3F13D5473bD)
  - name : TestGovernance
  - voingDelay : 25 → 5 minutes (25의 값은 블록이다. 1블록에 12초로 생각하여서 총 300초(5분)이다. )
  - voindPeriod : 300 → 1 hour (위의 계산식과 동일)
  - ProposalThreshold : 10e18 (몇개의 토큰이 있어야지 proposal을 제안할 수 있는지 결정)
  - QuorumNumerator : 5 (5%의 토큰이 투표하면 제안이 수락된다, 토큰 갯수로도 지정할 수 있음)

## Related information

Test Site : [https://www.tally.xyz/gov/testgovernance](https://www.tally.xyz/gov/testgovernance)

repo : [https://github.com/tokamak-network/tally-erc20](https://github.com/tokamak-network/tally-erc20)

deploy script : npx hardhat run scripts/tally_deploy.ts --network sepolia

## Deploy the Contract on Sepolia (2024-03-12)

- TestToken : 0x4675ad31045488Ed942D4e206ac15Fbae329Bce9
- TestTimelockController : 0x78B5e3A3a463bf3DCff7Cfb4b8D48A607838C453
  - minDelay : 60 seconds
  - admin : 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea
- TestGovernance : 0x323c7cbB5C7c825d3Af02417942D78BE7FDEa2a1
  - name : TestGovernance
  - voingDelay : 25 → 5 minutes 
  - voindPeriod : 300 → 1 hour
  - ProposalThreshold : 10e18 (Determine how many tokens are required to propose a proposal)
  - QuorumNumerator : 5 (A proposal is accepted when 5% of tokens vote, which can also be specified by the number of tokens.)

**Test DAO URL** : [https://www.tally.xyz/gov/tokamak-network-dao-sepolia-ii](https://www.tally.xyz/gov/tokamak-network-dao-sepolia-ii) 

## Deploy the Contract on Sepolia2 (2024-03-12)

- TestToken : 0x1Db3fa6Dc5563C5d3eFeB342db85C2D240F670B0
- TestTimelockController : 0x1276a8940b5845EC5696B7E251b199f9F8E09781
  - minDelay : 60 seconds
  - admin : 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea
- TestGovernance : 0x213EC877913F3283b918E4650e309Ff867d044d8
  - name : TestGovernance
  - voingDelay : 25 → 5 minutes 
  - voindPeriod : 300 → 1 hour
  - ProposalThreshold : 10e18 (Determine how many tokens are required to propose a proposal)
  - QuorumNumerator : 5 (A proposal is accepted when 5% of tokens vote, which can also be specified by the number of tokens.)