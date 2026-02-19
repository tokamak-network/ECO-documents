Author: Bernard Lee

**Date:** January 16, 2026

**Environment:** Local Devnet (op-succinct)

**Mode:** Mock Mode (simulated ZK proof generation)

---

## 1. Test Objective

To verify how OP Succinct's **Fault Dispute Game** mechanism works:

1. Does the Proposer create a Dispute Game when submitting L2 state roots?
1. Can a Challenger submit a challenge to the game?
1. Does the Proposer automatically generate a ZK Proof to defend when challenged?
1. Does the entire flow complete successfully?

---

## 2. What is OP Succinct Fault Dispute Game?

### Traditional Optimistic Rollup

`Proposer: "Block 100's state is 0xABC"
         ↓
    7-day wait (challenge window)
         ↓
No challenge → Finalized
Challenge → Bisection Game (dozens of interactive rounds)`

### OP Succinct Approach

`Proposer: "Block 100's state is 0xABC" + Creates Dispute Game
         ↓
Challenger: "That's wrong!" + Deposits Bond
         ↓
Proposer: Generates single ZK Proof (non-interactive)
         ↓
On-chain verification → DEFENDER_WINS or CHALLENGER_WINS`

**Key Difference:** Single **ZK Proof** instead of interactive Bisection game

---

## 3. Test Environment

### 3.1 Network Configuration

| Component | Endpoint |
| --- | --- |
| L1 RPC | [http://127.0.0.1:49698](http://127.0.0.1:49698/) |
| L2 RPC | [http://127.0.0.1:49711](http://127.0.0.1:49711/) |
| L1 Chain ID | 3151908 |
| L2 Chain ID | 2151908 |

### 3.2 Core Contracts

| Contract | Address | Role |
| --- | --- | --- |
| DisputeGameFactory | `0x07B436adB8044f54A8A31Bbf24343A1197c43845` | Game creation management |
| AccessManager | `0xd88603ff781670D1e5289D4B2E826AEe4eB75Dbc` | Proposer/Challenger permissions |
| FaultDisputeGame (tested) | `0x454fa2b848e122af95f239d25bb7f7c5cad74824` | Game Index 5, L2 Block 260 |

### 3.3 Accounts

| Role | Address | Purpose |
| --- | --- | --- |
| Proposer/Owner | `0x589A698b7b7dA0Bec545177D3963A2741105C7C9` | Game creation, permission grants |
| Challenger | `0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC` | Challenge submission |

### 3.4 Proposer Configuration

`mock_mode=true              # Skip actual ZK circuit execution
fast_finality_mode=false    # Generate proof only when challenged
game_type=42                # OPSuccinctFaultDisputeGame
proposal_interval_in_blocks=10`

---

## 4. Test Procedure and Results

### 4.1 Step 1: Proposer Execution and Game Creation

The Proposer automatically creates Dispute Games for each L2 block range.

**Log Evidence:**

`[[Proposing]]: Game created successfully 
  game_index=5 
  game_address=0x454fa2b848e122af95f239d25bb7f7c5cad74824
  l2_block_number=260`

**On-chain Verification:**

bash

`$ cast call $GAME "status()(uint8)"
0  # IN_PROGRESS

$ cast call $GAME "l2BlockNumber()(uint256)"
260`

---

### 4.2 Step 2: Challenger Permission Grant

OP Succinct uses a permissioned system requiring Challenger registration.

**Commands Executed:**

bash

`# Send ETH to Challenger (for bond and gas)
$ cast send 0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC \
  --value 5ether \
  --private-key 0xeaba42...

# Grant Challenger permission via AccessManager
$ cast send 0xd88603ff781670D1e5289D4B2E826AEe4eB75Dbc \
  "setChallenger(address,bool)" \
  0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC true \
  --private-key 0xeaba42...`

**Transaction Evidence:**

- ETH Transfer: `0xdc919523489732f8943a8f4a4f8662acefecd84be8a50670ee06a2296e0d2955`
- Permission Grant: `0xe76de101f2d2551a56e9832f769ab3d1803bc4be09713be1331959d0f3d01a30`

---

### 4.3 Step 3: Challenge Execution

**Command Executed:**

bash

`$ cast send 0x454fa2b848e122af95f239d25bb7f7c5cad74824 \
  "challenge()" \
  --private-key $CHALLENGER_PK \
  --value 0.001ether  # Challenger Bond`

**Transaction Evidence:**

- Challenge TX: `0x3219cc33e0729e1fa139a1c06cdc5034aa58263dd44ecd4697d64e47d3d3c8c9`
- Block: 337
- Gas Used: 70,095

**Bond Amount:** 0.001 ETH (1e15 wei)

bash

`$ cast call $GAME "challengerBond()(uint256)"
1000000000000000`

---

### 4.4 Step 4: Proposer's Automatic Defense (ZK Proof Generation)

Upon detecting the challenge, the Proposer automatically initiates the defense process.

**Log Evidence:**

`[[Defending]]: Spawning defense for challenged game 
  game_address=0x454fa2b848e122af95f239d25bb7f7c5cad74824

[[Proving]]: Generating Range Proof for blocks 250 to 260
[[Proving]]: Generating range proof in mock mode

[[Proving]]: Captured execution stats for range proof 
  total_instruction_cycles=888355119 
  total_sp1_gas=1575568599

[[Proving]]: Generating aggregation proof in mock mode

Game proven successfully 
  game_address=0x454fa2b848e122af95f239d25bb7f7c5cad74824
  l2_block_start=250 
  l2_block_end=260
  tx_hash=0x469fd2cbfb6de46817d89832a473075106873b0f286031d6cfd60d0d29d0a852
  duration_s=66.024126708`

**On-chain Verification:**

bash

`# proposalStatus = 4 (Proven)
$ cast call $GAME "claimData()"
# First value: 4

# gameOver = true
$ cast call $GAME "gameOver()(bool)"
true`

---

## 5. Performance Measurements

### 5.1 Time Measurements (Mock Mode)

| Stage | Duration |
| --- | --- |
| Challenge Detection | Immediate (~30s in next loop) |
| Range Proof Generation | ~47 seconds |
| Aggregation Proof Generation | ~19 seconds |
| On-chain Submission | Immediate |
| **Total Duration** | **66 seconds** |

### 5.2 Computation Costs (Mock Mode Estimates)

| Metric | Value |
| --- | --- |
| Total Instruction Cycles | 888,355,119 |
| Total SP1 Gas | 1,575,568,599 |

> Note: Mock Mode skips actual ZK circuit execution, only performing witness generation. Real ZK Mode proof generation may take several minutes to tens of minutes.

---

## 6. State Transition Summary

### Game Status Flow

`┌─────────────────────────────────────────────────────────────┐
│  status()=0 (IN_PROGRESS)                                   │
│  proposalStatus=0 (Unchallenged)                            │
│                    │                                        │
│                    ▼ challenge() called                     │
│                                                             │
│  status()=0 (IN_PROGRESS)                                   │
│  proposalStatus=1 (Challenged)                              │
│                    │                                        │
│                    ▼ Proposer submits ZK Proof              │
│                                                             │
│  status()=0 (IN_PROGRESS)                                   │
│  proposalStatus=4 (Proven)                                  │
│  gameOver()=true                                            │
│                    │                                        │
│                    ▼ resolve() after parent game resolved   │
│                                                             │
│  status()=1 (DEFENDER_WINS) ← Final State                   │
└─────────────────────────────────────────────────────────────┘`

### Current State

| Item | Value | Meaning |
| --- | --- | --- |
| status() | 0 | IN_PROGRESS (awaiting parent resolve) |
| proposalStatus | 4 | Proven (proof completed) |
| gameOver() | true | Game end condition met |

> Note: To call resolve(), parent games must be resolved first. Parent games can only be resolved after MAX_CHALLENGE_DURATION (~4 hours) passes.

---

## 7. Key Findings

### 7.1 Technical Discoveries

1. **Permissioned System**: Challenge requires permission grant via AccessManager
1. **Bond Mechanism**: Challenger must deposit 0.001 ETH bond
1. **Game Chain**: Each game has a parent; sequential resolution required
1. **Automatic Defense**: Proposer automatically generates ZK Proof upon challenge detection

### 7.2 OP Succinct vs Traditional Fraud Proof

| Aspect | Traditional Bisection | OP Succinct |
| --- | --- | --- |
| Dispute Resolution | Interactive (dozens of rounds) | Non-interactive (single proof) |
| Proof Time | Several days | Minutes to hours |
| On-chain Cost | High (multiple TXs) | Low (single TX) |
| Complexity | High | Low |

---

## 8. Conclusion

The complete **Challenge → ZK Proof Generation → Defense** flow was successfully completed in **66 seconds** using OP Succinct Mock Mode.

### Verified Items

- Dispute Game creation and management
- Permissioned Challenger system
-  Challenge submission mechanism
-  Automatic ZK Proof generation (Mock Mode)
- On-chain Proof submission
- Game state transitions (Unchallenged → Challenged → Proven)

### Future Test Plans

1. **Real ZK Mode Test**: Integration with Succinct Prover Network
1. **Cost Measurement**: Measure PROVE token consumption
1. **Failure Scenario**: Verify CHALLENGER_WINS with incorrect state root

---

## Appendix: Commands Reference

bash

`# Environment Variables
GAME=0x454fa2b848e122af95f239d25bb7f7c5cad74824
ACCESS_MANAGER=0xd88603ff781670D1e5289D4B2E826AEe4eB75Dbc
CHALLENGER=0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC
CHALLENGER_PK=0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a

# Check Game Status
cast call $GAME "status()(uint8)" --rpc-url http://127.0.0.1:49698
cast call $GAME "gameOver()(bool)" --rpc-url http://127.0.0.1:49698
cast call $GAME "claimData()" --rpc-url http://127.0.0.1:49698
cast call $GAME "l2BlockNumber()(uint256)" --rpc-url http://127.0.0.1:49698
cast call $GAME "challengerBond()(uint256)" --rpc-url http://127.0.0.1:49698

# Execute Challenge
cast send $GAME "challenge()" \
  --rpc-url http://127.0.0.1:49698 \
  --private-key $CHALLENGER_PK \
  --value 0.001ether`

---

## Next Steps: Real ZK Mode with PROVE Token

To test with actual ZK proof generation via Succinct Prover Network:

1. **Acquire PROVE tokens** on Ethereum mainnet
1. **Configure network mode**: `SP1_PROVER=network`
1. **Set up wallet**: Fund with PROVE for proof generation fees
1. **Run proposer** with real proving enabled
1. **Measure**: Actual proof generation time and token costs