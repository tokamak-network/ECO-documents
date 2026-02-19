## Problem

When using `evm_increaseTime` to skip time on a local Anvil node, proposals remain in Pending state and never transition to Active.

## Cause

DAOGovernor uses `block.number`—not `block.timestamp`—to determine voting state:

if (block.number < proposal.voteStart) return ProposalState.Pending;
if (block.number <= proposal.voteEnd) return ProposalState.Active;

`evm_increaseTime` only advances the timestamp. The block number stays the same, so the contract never sees enough blocks to start voting.

## Solution

Use `anvil_mine(blocks, interval)` instead. This advances both block number and timestamp together.

*Example: Skip 1 day (7,200 blocks × 12s)*

```
cast rpc anvil_mine 7200 12 --rpc-url [http://127.0.0.1:8545](http://127.0.0.1:8545/)
```