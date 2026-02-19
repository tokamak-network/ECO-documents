1. Standardize to Discord 
1. Voting token: Get a more detailed explanation (Diagram helpful)
1. Cross-chain Governance (Coming Soon)
1. Governance Examples
  1. Update the seigniorage distribution
  1. Changing the number of security council (Member count?)
  1. [https://dao.tokamak.network/#/propose](https://dao.tokamak.network/#/propose) 
1. Tally’s Governor Contract parameters 
```javascript
token: {
  name: "TOKAMAK VOTE TOKEN",   // votable token name 
  symbol: "TVT",         // votable token symbol                           
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
```
1. 