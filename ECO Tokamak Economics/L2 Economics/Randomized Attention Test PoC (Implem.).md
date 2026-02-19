## Test Plan

- Scenarios:
  1. **Baseline:** Gas cost of a standard create call in the original DisputeGameFactory.
  1. **RAT-Triggered Creation:** Gas cost of a create call that probabilistically triggers an Attention Test in the modified DisputeGameFactoryRAT.
  1. **RAT-Solution Submission:** Gas cost for a challenged validator to submit their solution via the new submitAttentionSolution function.
- Methodology
  1. **Environment Setup:**
    - Initialize a Foundry project and configure dependencies for Optimism contracts.
    - Run a local Anvil node.
  1. **Contract Implementation:**
    - Create DisputeGameFactoryRAT.sol by modifying the original contract to include RAT logic (probabilistic trigger, state variables, events).
    - Develop a simple MockDisputeGame.sol for the game implementation to isolate factory costs.
  1. **Test Script (RATCost.t.sol):**
    - Write a Foundry test suite to deploy both original and RAT-enabled factories.
    - Set the RAT probability to 100% to ensure consistent triggering for testing purposes.
    - Create separate test functions for each scenario, using vm.prank to simulate actions from the proposer and validator.
  1. **Execution & Analysis:**
    - Run the test suite using the forge test --gas-report command.
    - Analyze the generated gas report to compare the mean gas costs of each function call, calculating the overhead of the RAT mechanism in both the creation and solution submission phases.

### Optimism Mainnet StateRoot Commitment & Tx Example

```javascript
    /// @notice Creates a new DisputeGame proxy contract.
    /// @param _gameType The type of the DisputeGame - used to decide the proxy implementation.
    /// @param _rootClaim The root claim of the DisputeGame.
    /// @param _extraData Any extra data that should be provided to the created dispute game.
    /// @return proxy_ The address of the created DisputeGame proxy.
    function create(
        GameType _gameType,
        Claim _rootClaim,
        bytes calldata _extraData /// L2BlockNumber!!!
    )
        external
        payable
        returns (IDisputeGame proxy_);
```

Docs

[https://specs.optimism.io/fault-proof/stage-one/dispute-game-interface.html](https://specs.optimism.io/fault-proof/stage-one/dispute-game-interface.html)

Tx Example

[https://etherscan.io/tx/0xbba9caa804ac5666992db72014a3b1ad5515054f2d2057598aac872be9272106](https://etherscan.io/tx/0xbba9caa804ac5666992db72014a3b1ad5515054f2d2057598aac872be9272106)

- Why did they change `postL2State` to `create` ?
  - Major difference: `create` starts a dispute game right away. Therefore, anyone can dispute the state commitment by sending a transaction without creating a smart contract. 
  - Also, we can consider the dipute time window starts with the commitment.
  - This interface provides a modular architecture

## Target Contracts to Modify

DisputeGameFactory.sol

[Link](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol)

FaultDisputeGame.sol

[Link](https://github.com/ethereum-optimism/optimism/blob/develop/packages/contracts-bedrock/src/dispute/DisputeGameFactory.sol)

### Old Version for Testing

[https://specs.optimism.io/protocol/proposals.html#l2-output-root-proposals-specification](https://specs.optimism.io/protocol/proposals.html#l2-output-root-proposals-specification)

[https://docs.optimism.io/stack/transactions/transaction-flow](https://docs.optimism.io/stack/transactions/transaction-flow)

[Link](https://github.com/ethereum-optimism/optimism/blob/233ede59d16cb01bdd8e7ff662a153a4c3178bdd/packages/contracts-bedrock/contracts/L1/L2OutputOracle.sol)

## References

[https://optimistic.etherscan.io/](https://optimistic.etherscan.io/)

[https://l2beat.com/scaling/projects/op-mainnet](https://l2beat.com/scaling/projects/op-mainnet)