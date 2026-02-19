Repo: [https://github.com/tokamak-network/ton-staking-tally-contract/tree/7-use-voting-weight-as-a-quadratic-voting](https://github.com/tokamak-network/ton-staking-tally-contract/tree/7-use-voting-weight-as-a-quadratic-voting)

# Reference 

-  [https://docs.openzeppelin.com/contracts/4.x/governance](https://docs.openzeppelin.com/contracts/4.x/governance)

# Config 

[https://github.com/tokamak-network/ton-staking-tally-contract/blob/7-use-voting-weight-as-a-quadratic-voting/deploy.tokamak.tally.config.ts](https://github.com/tokamak-network/ton-staking-tally-contract/blob/7-use-voting-weight-as-a-quadratic-voting/deploy.tokamak.tally.config.ts)

```javascript
token: {
    name: "TOKAMAK VOTE TOKEN",
    symbol: "TVT",
  },
  // Timelock
  timelock: {
    minDelay: 86400, // 12 days (assuming 12 seconds per block)
  },
  // Set clockMode to true for timestamp mode, false for block number mode
  clockMode: false,
  // Governor
  governor: {
    name: "Tokamak Governor DAO",
    // 7200 is 24 hours (assuming 12 seconds per block)
    votingDelay: 7200,
    // 50400 is 7 days (assuming 12 seconds per block)
    votingPeriod: 50400,
    // Quorum numerator to denominator of 100
    quorumNumerator: 4,
    // Threshold to be able to propose
    // getVotes(proposer): QV must be greater than ProposalThreshold.
    proposalThreshold: 10000000000n, // Set a non-zero value to prevent proposal spam.
    // Vote extension: if a late quorum is reached, how long should it be extended?
    voteExtension: 7200, // 7200 is 24 hours (assuming 12 seconds per block)
  },
  // First Mint is used to mint the initial tokens for this governance
  // It must be higher than the proposalThreshold
  // so there are enough tokens for the governance to be able to propose
  //
  // ATTENTION:
  // If the amount is not higher than 0, it will not mint any tokens and will also maintain roles for the deployer.
  // Keep it as ZERO if you plan on doing manual changes and mints, before locking it up to be controlled by governor contracts.
  //
  // After the first mint, the deployer will lose the minter and admin role and give it to the timelock, which is the executor.
  firstMint: {
    amount: 0, // If set higher than zero, it will mint the specified amount of tokens to the address below
    // 'to' is an Ethereum Address. If empty, it will default to the deployer. If incorrect, it will also default to the deployer (a warning will be issued when deploying).
    to: "",
  }
```

# Contracts 

## TokamakVoteERC20

- Unsupported ERC20 functions
  - function transfer(address to, uint256 value) public override returns (bool)
  - function allowance(address owner, address spender) public pure override returns (uint256)
  -  function approve(address spender, uint256 value) public override returns (bool) 
  - function transferFrom(address from, address to, uint256 value) public override returns (bool)
- Mint TokamakVoteERC20  
  - The number of tokens that can be minted is determined by the amount of staked TON holdings.

```javascript
 function mint(uint256 amount) public 
```
- Burn
```javascript
 function burn(uint256 amount) public  
```
- View the TokamakVoteERC20 balance of the account.
```javascript
function balanceOf(address account) public view virtual returns (uint256) {
        ERC20Storage storage $ = _getERC20Storage();
```
- View the total supply of TokamakVoteERC20.
```javascript
function totalSupply() public view virtual returns (uint256)
```
- View the voting rights balance of the account.
```solidity
function getVotes(address account) public view virtual returns (uint256) 
    
```
- View the voting rights balance of the account at timepoint.
```javascript
function getPastVotes(address account, uint256 timepoint) public view returns (uint256)
    
```
- View the total voting rights counts at timepoint.
```javascript
function getPastVoteTotal(uint256 timepoint) public view returns (uint256) {
     
```
- View the total voting rights counts currently.
```javascript
function getPastTotalSupply() public view returns (uint256) {
     
```
- delegate
  - Returns the delegate that `account` has chosen.

```javascript
function delegate(address delegatee) public 
```
- delegates
  - Returns the delegate that `account` has chosen.

```javascript
function delegates(address account) public view virtual returns (address) {
     
```

## TokamakGovernor

-  votingDelay()
- votingPeriod()
- function clock() public view virtual returns (uint48);
-  function CLOCK_MODE() public view virtual returns (string memory);
-     function quorum(uint256 timepoint) public view virtual returns (uint256);
- state(uint256 proposalId)
- proposalNeedsQueuing(uint256 proposalId)
- proposalThreshold()
- proposalDeadline(uint256 proposalId)
- 

```javascript
function hashProposal(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) 
```

- 

```javascript
function propose(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        string memory description
    ) public virtual returns (uint256) 
```

- 

```javascript
function queue(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) public virtual returns (uint256)
```

- 

```javascript
function execute(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) public payable virtual returns (uint256) {
```

- 

```javascript
function cancel(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) public virtual returns (uint256) {
```

- 

```javascript
function getVotes(address account, uint256 timepoint) public view virtual returns (uint256) {
     
```

- 

```javascript
function getVotesWithParams(
        address account,
        uint256 timepoint,
        bytes memory params
    ) public view virtual returns (uint256) {
```

- 

```javascript
function castVote(uint256 proposalId, uint8 support) public virtual returns (uint256) {
        address voter = _msgSender();
     
```

## TokamakTimelockController

# TokamakVoteERC20

# Deployed Contracts On Sepolia 

# Applied Tally 

문서정리. 세폴리아에 배포 및 탈리에 적용 