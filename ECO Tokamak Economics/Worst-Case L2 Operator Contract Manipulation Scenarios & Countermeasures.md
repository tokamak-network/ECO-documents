Here are several worst-case scenario examples of Layer 2 (L2) operators manipulating L2 contracts, (along with simplified hypothetical code snippets to illustrate the concept and) potential user-verifiable countermeasures.

**Important Disclaimer:** The following code examples are highly simplified for illustrative purposes and **not representative of production-ready L2 contracts.** Real-world L2 systems are significantly more complex and employ numerous security mechanisms. These examples aim to demonstrate potential manipulation vectors in a basic way. Similarly, the "tests" are conceptual and not actual implemented test suites.

## Example Scenario # . When the public L2 RPC is forged

**Manipulation**: 

**Hypothetical L2 Contract Snippet (Illustrative)**:

**Conceptual "Test" of Manipulation**:

**User-Verifiable Countermeasures**:

## Scenario 1 . When the public L2 RPC is forged

**Manipulation**: 

**Hypothetical L2 Contract Snippet (Illustrative)**:

**Conceptual "Test" of Manipulation**:

**User-Verifiable Countermeasures**:

## Scenario 2 . When the L2 withdrawal request TON is not burned and is stolen by the L2 operator

**Manipulation**: 

Malicious L2 operator manipulates Burn.nativeToken(uint256 _amount) function to send to a specific account without burning and withdraw this stolen TON to L1.

**Hypothetical L2 Contract Snippet (Illustrative)**:

 The /libraries/Burn.sol contract is manipulated by a malicious operator as follows:

```shell
// SPDX-License-Identifier: MIT
pragma solidity 0.8.15;

/// @title Burn
/// @notice Utilities for burning stuff.
library Burn {
		
    /// @notice Burns a given amount of the native token.
    /// @param _amount Amount of the native token to burn.
    function nativeToken(uint256 _amount) internal {
		  **  address payable operaor = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
		    operaor.trnasfer(_amount); **
    }

    /// @notice Burns a given amount of gas.
    /// @param _amount Amount of gas to burn.
    function gas(uint256 _amount) internal view {
        uint256 i = 0;
        uint256 initialGas = gasleft();
        while (initialGas - gasleft() < _amount) {
            ++i;
        }
    }
}

/// @title Burner
/// @notice Burner self-destructs on creation and sends all native tokens to itself, removing all native tokens given to
///         the contract from the circulating supply. Self-destructing is the only way to remove native tokens
///         from the circulating supply.
contract Burner {
    constructor() payable {
        selfdestruct(payable(address(this)));
    }
}
```

**Conceptual "Test" of Manipulation**:

1. A user submits a withdrawal transaction for a native ton.
1. The requested native ton is transferred in the L2ToL1MessagePasser contract. 
1. <u>When the L2ToL1MessagePasser.burn() function is called, the native ton held by L2ToL1MessagePasser should be burned, but </u><u>the malicious sequencer manipulates this code to transfer the native ton to another account without burning it</u><u>.</u>
1. The malicious sequencer withdraws the received native ton to L1.
1. <u>Some users may not be able to withdraw because there are not enough TON locked to L1.</u>

**User-Verifiable Countermeasures**: 

1. (Countermeasure 1): We can provide a page to verify that the L2 contract has not been manipulated with. -> (not a complete solution) Since it only checks the current state, if it is manipulated, maliciously performed, and then restored to its original state, it may not be detected.
1. (Countermeasure 2): Develop an L2 DAO contract, and have L2 DAO hold the authority to upgrade the L2 contract. L2 DAO executes the agenda from the contract existing in L1 and executes the command to L2. (It takes time to design and develop.)
1. (Countermeasure 3): If we can verify that the TON locked in the L1 bridge is equal to the total TON held in L2 (excluding the TON to be burned), we can verify that the TON has not been stolen. The information required for verification is as follows:
  - The amount of TON locked in L1 that is scheduled to be withdrawn
  - The amount of TON locked in L1 that is not scheduled to be withdrawn
  - The amount of TON held in L2 that is scheduled to be burned
  - The amount of TON held in L2 excluding the TON to be burned