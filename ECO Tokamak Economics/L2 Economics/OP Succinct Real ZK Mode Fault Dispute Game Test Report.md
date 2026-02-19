**Author:** Bernard Lee, Suhyeon Lee

**Date:** January 21, 2026

**Environment:** Local Devnet (op-succinct) + Succinct Prover Network

**Mode:** Real ZK Mode (actual ZK proof generation via Succinct Network)

---

## 1. Test Objective

To verify the complete ZK validity proof pipeline with **real proof generation**:

1. Can Succinct Prover Network generate actual ZK proofs for L2 state transitions?
1. Can the generated Plonk proof be verified on-chain?
1. What are the actual costs and time requirements?
1. What infrastructure setup is required for on-chain verification?

---

## 2. Test Environment

### 2.1 Network Configuration

| Component | Endpoint |
| --- | --- |
| L1 RPC | [http://127.0.0.1:50643](http://127.0.0.1:50643/) |
| L2 RPC | [http://127.0.0.1:50696](http://127.0.0.1:50696/) |
| L2 Node RPC | [http://127.0.0.1:50701](http://127.0.0.1:50701/) |
| L1 Beacon RPC | [http://127.0.0.1:50647](http://127.0.0.1:50647/) |
| L1 Chain ID | 3151908 |
| L2 Chain ID | 901 |

### 2.2 Deployed Contracts

| Contract | Address | Role |
| --- | --- | --- |
| DisputeGameFactory | `0x37d08c124B91e1663d83fb1b742677115959b726` | Game creation management |
| SP1 Verifier Gateway | `0x48266A1953D7e3a02603868528Fd51DCa1866614` | Routes proofs to correct verifier |
| SP1 Verifier (v5.0.0 Plonk) | `0x835089111509d7102bF2935f50905a89d5840AAD` | On-chain proof verification |
| Anchor State Registry | `0xfbECDA1A5CAf07b2a9E6042e6A41A85935a557cD` | L2 state anchoring |
| Access Manager | `0xB2540a4Faf97c6312677BFDcE2f11513AD31cDD4` | Proposer/Challenger permissions |

### 2.3 Accounts

| Role | Address | Purpose |
| --- | --- | --- |
| Proposer/Owner | `0x589A698b7b7dA0Bec545177D3963A2741105C7C9` | Game creation, proof submission |
| Challenger | `0x90F79bf6EB2c4f870365E785982E1f101E93b906` | Challenge submission |
| Succinct Requester | `0x6d14e0f28cc49f11613e0092773101cce2cfb0ab` | Proof requests to Succinct Network |

### 2.4 Proposer Configuration

`mock_mode=false
SP1_PROVER=network
RANGE_PROOF_STRATEGY=auction
AGG_PROOF_STRATEGY=auction
AUCTION_TIMEOUT=600              # 10 minutes
PROPOSAL_INTERVAL_IN_BLOCKS=1    # 1 block per game
RANGE_CYCLE_LIMIT=10000000000    # 10 billion cycles
RANGE_GAS_LIMIT=10000000000      # 10 billion PGUs
AGG_CYCLE_LIMIT=10000000000
AGG_GAS_LIMIT=10000000000
MAX_PRICE_PER_PGU=150000000
MIN_AUCTION_PERIOD=300           # 5 minutes`

---

## 3. Two-Stage Proof Architecture

### Why Two Proofs?

OP Succinct uses a two-stage proof system for cost efficiency:

`┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Range Proof (Compressed)                          │
│  - Proves L2 state transition correctness                   │
│  - Large proof size (several MB)                            │
│  - Cannot be verified on-chain directly (too expensive)     │
│  - Fast to generate relative to complexity                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Aggregation Proof (Plonk)                         │
│  - Proves "the Compressed proof is valid"                   │
│  - Small proof size (hundreds of bytes)                     │
│  - Can be verified on-chain efficiently                     │
│  - SNARK-based, constant verification cost                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  On-chain Verification                                      │
│  - SP1VerifierGateway routes to correct verifier            │
│  - SP1Verifier (Plonk) verifies the proof                   │
│  - Game status updated to "Proven"                          │
└─────────────────────────────────────────────────────────────┘`

---

## 4. Test Procedure and Results

### 4.1 Step 1: Infrastructure Setup

### Deploy SP1 Verifier Gateway

bash

`cd ~/Downloads/op-succinct/contracts

cat > src/SimpleVerifierGateway.sol << 'EOF'
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.15;

import {ISP1Verifier} from "@sp1-contracts/src/ISP1Verifier.sol";

contract SimpleVerifierGateway is ISP1Verifier {
    address public owner;
    mapping(bytes4 => address) public verifiers;
    
    constructor() {
        owner = msg.sender;
    }
    
    function addRoute(bytes4 selector, address verifier) external {
        require(msg.sender == owner, "not owner");
        verifiers[selector] = verifier;
    }
    
    function verifyProof(bytes32 programVKey, bytes calldata publicValues, bytes calldata proofBytes) external view {
        bytes4 selector = bytes4(proofBytes[:4]);
        address verifier = verifiers[selector];
        require(verifier != address(0), "route not found");
        ISP1Verifier(verifier).verifyProof(programVKey, publicValues, proofBytes);
    }
}
EOF

forge create src/SimpleVerifierGateway.sol:SimpleVerifierGateway \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23 \
  --broadcast
# Deployed to: 0x48266A1953D7e3a02603868528Fd51DCa1866614`

### Deploy SP1 Verifier (v5.0.0 Plonk)

bash

`cd ~/Downloads/op-succinct/contracts/lib/sp1-contracts
git checkout v5.0.0

cd contracts
forge create src/v5.0.0/SP1VerifierPlonk.sol:SP1Verifier \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23 \
  --broadcast
# Deployed to: 0x835089111509d7102bF2935f50905a89d5840AAD`

### Register Verifier Route

bash

`# Get VERIFIER_HASH (selector)
cast call 0x835089111509d7102bF2935f50905a89d5840AAD "VERIFIER_HASH()(bytes32)" --rpc-url http://127.0.0.1:50643
# 0xd4e8ecd2357dd882209800acd6abb443d231cf287d77ba62b732ce937c8b56e7

# Add route (first 4 bytes of hash)
cast send 0x48266A1953D7e3a02603868528Fd51DCa1866614 \
  "addRoute(bytes4,address)" 0xd4e8ecd2 0x835089111509d7102bF2935f50905a89d5840AAD \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23`

### Update FDG Config and Deploy

bash

`# Update verifier address in config
cd ~/Downloads/op-succinct/contracts
sed -i '' 's/0x397A5f7f3dBd538f23DE225B51f532c34448dA9B/0x48266A1953D7e3a02603868528Fd51DCa1866614/g' opsuccinctfdgconfig.json

# Deploy FDG contracts
OP_SUCCINCT_FAULT_DISPUTE_GAME_CONFIG_PATH=./opsuccinctfdgconfig.json \
forge script script/fp/DeployOPSuccinctFDG.s.sol:DeployOPSuccinctFDG \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23 \
  --broadcast`

### 4.2 Step 2: Grant Permissions

bash

`# Grant Proposer permission
cast send 0xB2540a4Faf97c6312677BFDcE2f11513AD31cDD4 \
  "setProposer(address,bool)" 0x589A698b7b7dA0Bec545177D3963A2741105C7C9 true \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23

# Grant Challenger permission
cast send 0xB2540a4Faf97c6312677BFDcE2f11513AD31cDD4 \
  "setChallenger(address,bool)" 0x90F79bf6EB2c4f870365E785982E1f101E93b906 true \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23

# Fund Challenger with ETH
cast send 0x90F79bf6EB2c4f870365E785982E1f101E93b906 \
  --value 1ether \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23`

### 4.3 Step 3: Start Proposer and Execute Challenge

bash

`# Start Proposer
cd ~/Downloads/op-succinct

L1_RPC=http://127.0.0.1:50643 \
L2_RPC=http://127.0.0.1:50696 \
L2_NODE_RPC=http://127.0.0.1:50701 \
L1_BEACON_RPC=http://127.0.0.1:50647 \
ANCHOR_STATE_REGISTRY_ADDRESS=0xfbECDA1A5CAf07b2a9E6042e6A41A85935a557cD \
FACTORY_ADDRESS=0x37d08c124B91e1663d83fb1b742677115959b726 \
GAME_TYPE=42 \
MOCK_MODE=false \
PROPOSAL_INTERVAL_IN_BLOCKS=1 \
PRIVATE_KEY=0xeaba42282ad33c8ef2524f07277c03a776d98ae19f581990ce75becb7cfa1c23 \
SP1_PROVER=network \
RANGE_PROOF_STRATEGY=auction \
AGG_PROOF_STRATEGY=auction \
AUCTION_TIMEOUT=600 \
RANGE_CYCLE_LIMIT=10000000000 \
RANGE_GAS_LIMIT=10000000000 \
AGG_CYCLE_LIMIT=10000000000 \
AGG_GAS_LIMIT=10000000000 \
MAX_PRICE_PER_PGU=150000000 \
MIN_AUCTION_PERIOD=300 \
RUST_LOG=info \
NETWORK_PRIVATE_KEY=<your_succinct_wallet_private_key> \
./target/release/proposer

# Execute Challenge (in another terminal)
cast send 0x56b2de5af86c685bdfd41315e52240ec6cc91cfc "challenge()" \
  --value 0.001ether \
  --rpc-url http://127.0.0.1:50643 \
  --private-key 0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6
```

### 4.4 Step 4: Proof Generation and Submission

#### Range Proof Request Log
```
2026-01-20T18:58:32.409859Z  INFO [[Proving]]: Generating Range Proof for blocks 2236 to 2237
2026-01-20T18:58:42.560060Z  INFO [[Proving]]: Requesting proof:
2026-01-20T18:58:42.560060Z  INFO [[Proving]]: ├─ Strategy: Auction
2026-01-20T18:58:42.560086Z  INFO [[Proving]]: ├─ Proof mode: Compressed
2026-01-20T18:58:42.560092Z  INFO [[Proving]]: ├─ Circuit version: v5.0.0
2026-01-20T18:58:42.560105Z  INFO [[Proving]]: ├─ Base fee: 0.2000 $PROVE
2026-01-20T18:58:42.560272Z  INFO [[Proving]]: ├─ Cycle limit: 10000000000 cycles
2026-01-20T18:58:42.560699Z  INFO [[Proving]]: └─ Gas limit: 10000000000 PGUs
2026-01-20T18:58:49.013186Z  INFO [[Proving]]: Range proof request submitted 
  proof_id=0x4855d8b5bda7837443b5c03df6937a5f477b489117a5b89c569437b34ed37e1c
```

#### Aggregation Proof Request Log
```
2026-01-20T19:05:17.612586Z  INFO [[Proving]]: Proof fulfilled proof_id=0x4855d8b5bd...
2026-01-20T19:05:17.631909Z  INFO [[Proving]]: Preparing Stdin for Agg Proof
2026-01-20T19:05:19.987685Z  INFO [[Proving]]: Requesting proof:
2026-01-20T19:05:19.987726Z  INFO [[Proving]]: ├─ Strategy: Auction
2026-01-20T19:05:19.988666Z  INFO [[Proving]]: ├─ Proof mode: Plonk
2026-01-20T19:05:19.988700Z  INFO [[Proving]]: ├─ Circuit version: v5.0.0
2026-01-20T19:05:19.988715Z  INFO [[Proving]]: ├─ Base fee: 0.3000 $PROVE
2026-01-20T19:05:26.459533Z  INFO [[Proving]]: Aggregation proof request submitted 
  proof_id=0x9406792f84242b5a3ce9e994191322d36b4f9532fe39bb0e62a471b1c430e34b
```

#### On-chain Submission Log
```
2026-01-20T19:12:09.094686Z  INFO Game proven successfully 
  game_address=0x56b2de5af86c685bdfd41315e52240ec6cc91cfc
  l2_block_start=2236 
  l2_block_end=2237
  tx_hash=0xc2e15ed92315cbf82ccd57eda48874f73df36f469e9918da46e52f9e74615df7
  duration_s=816.706023042`

---

## 5. Proof Details from Succinct Explorer

### 5.1 Range Proof (Compressed)

| Item | Value |
| --- | --- |
| Request ID | `0x4855d8b5bda7837443b5c03df6937a5f477b489117a5b89c569437b34ed37e1c` |
| Explorer Link | [https://explorer.succinct.xyz/request/0x4855d8b5bda7837443b5c03df6937a5f477b489117a5b89c569437b34ed37e1c](https://explorer.succinct.xyz/request/0x4855d8b5bda7837443b5c03df6937a5f477b489117a5b89c569437b34ed37e1c) |
| Status | Fulfilled |
| Mode | Compressed |
| SP1 Version | v5.0.0 |
| Time Taken | 6m 22s |
| Gas Limit | 10,000,000,000 PGUs |
| Gas Used | 1,683,173,009 PGUs |
| Base Fee | 0.2 PROVE |
| Total Fee | ~0.2 PROVE |
| Prover | `0xb3780a...b60dcf` |

### 5.2 Aggregation Proof (Plonk)

| Item | Value |
| --- | --- |
| Request ID | `0x9406792f84242b5a3ce9e994191322d36b4f9532fe39bb0e62a471b1c430e34b` |
| Explorer Link | [https://explorer.succinct.xyz/request/0x9406792f84242b5a3ce9e994191322d36b4f9532fe39bb0e62a471b1c430e34b](https://explorer.succinct.xyz/request/0x9406792f84242b5a3ce9e994191322d36b4f9532fe39bb0e62a471b1c430e34b) |
| Status | Fulfilled |
| Mode | Plonk |
| SP1 Version | v5.0.0 |
| Time Taken | 6m 21s |
| Gas Limit | 10,000,000,000 PGUs |
| Gas Used | 1,529,006 PGUs |
| Base Fee | 0.3 PROVE |
| Total Fee | ~0.3 PROVE |
| Prover | `0x3d008b...0fa125` |

---

## 6. Cost and Time Summary

### 6.1 Proof Generation Costs

| Stage | Base Fee | Gas Fee | Total |
| --- | --- | --- | --- |
| Range Proof (Compressed) | 0.2 PROVE | ~0 PROVE | ~0.2 PROVE |
| Aggregation Proof (Plonk) | 0.3 PROVE | ~0 PROVE | ~0.3 PROVE |
| **Total** |  |  | **~0.5 PROVE** |

### 6.2 Time Breakdown

| Stage | Duration |
| --- | --- |
| Range Proof Generation | 6m 22s |
| Aggregation Proof Generation | 6m 21s |
| On-chain Submission | ~1s |
| **Total End-to-End** | **~13 minutes** |

### 6.3 Comparison: Mock Mode vs Real ZK Mode

| Metric | Mock Mode | Real ZK Mode |
| --- | --- | --- |
| Total Duration | 66 seconds | ~13 minutes |
| PROVE Cost | 0 | ~0.5 PROVE |
| On-chain Verification | Skipped | Actual verification |
| Proof Generation | Simulated | Succinct Network |

---

## 7. Troubleshooting Journey

### 7.1 Issue: "route not found" Error

**Symptom:** Plonk proof generated successfully but on-chain submission failed with "route not found"

**Root Cause:** SP1 Verifier Gateway didn't have a route for the v5.0.0 Plonk verifier selector

**Solution:**

1. Deploy v5.0.0 SP1VerifierPlonk
1. Get VERIFIER_HASH and register route in Gateway

bash

`# Get selector from VERIFIER_HASH
cast call <verifier_address> "VERIFIER_HASH()(bytes32)"
# Use first 4 bytes as selector

# Add route
cast send <gateway_address> "addRoute(bytes4,address)" <selector> <verifier_address>`

### 7.2 Issue: "cycle limit exceeded" Error

**Symptom:** Proof request failed with "The request's cycle limit was exceeded"

**Root Cause:** Initial RANGE_CYCLE_LIMIT=100,000,000 (100M) was too low

**Solution:** Increase to 10,000,000,000 (10B) cycles

bash

`RANGE_CYCLE_LIMIT=10000000000
RANGE_GAS_LIMIT=10000000000`

### 7.3 Issue: "gas limit exceeded" Error

**Symptom:** After fixing cycle limit, failed with "The request's prover gas limit was exceeded"

**Root Cause:** Gas limit also needs to be increased proportionally

**Solution:** Set both cycle and gas limits to 10B

### 7.4 Issue: "no reservation found for requester"

**Symptom:** Proof request rejected with permission error

**Root Cause:** Using `Reserved` strategy without reservation on Succinct Network

**Solution:** Switch to `Auction` strategy

bash

`RANGE_PROOF_STRATEGY=auction
AGG_PROOF_STRATEGY=auction`

### 7.5 Issue: Verifier contract has no code

**Symptom:** `prove()` call reverted with empty revert data

**Root Cause:** FDG contract referenced a verifier address that had no deployed code on devnet

**Solution:**

1. Deploy SP1VerifierGateway to devnet
1. Deploy SP1Verifier (Plonk) to devnet
1. Register routes
1. Redeploy FDG contracts with correct verifier address

---

## 8. Key Findings

### 8.1 Architecture Insights

1. **Two-Stage Proof System**: Compressed → Plonk conversion is necessary for on-chain verification efficiency
1. **Verifier Version Compatibility**: Succinct Network's SP1 version (v5.0.0) must match on-chain verifier version
1. **Gateway Pattern**: SP1VerifierGateway routes proofs to correct verifier based on 4-byte selector from VERIFIER_HASH
1. **Resource Requirements**: Even 1 block transition requires ~1.7B gas units (cycles) for proof generation

### 8.2 Cost Analysis

| Metric | Value | Notes |
| --- | --- | --- |
| Per-block proof cost | ~0.5 PROVE | For minimal L2 activity |
| Gas used (Range) | 1.68B PGUs | 16.8% of 10B limit |
| Gas used (Plonk) | 1.5M PGUs | Significantly smaller |

### 8.3 Operational Considerations

1. **Auction Strategy**: More flexible than Reserved, works without pre-registration
1. **Timeout Settings**: 10-minute auction timeout provides sufficient time for prover bids
1. **Minimum Auction Period**: 5 minutes ensures competitive bidding

---

## 9. Conclusion

Successfully completed the **full ZK validity proof pipeline** with real proof generation:

### Verified Items

-  Dispute Game creation and challenge mechanism
- Range Proof (Compressed) generation via Succinct Network
- Aggregation Proof (Plonk) generation via Succinct Network
- On-chain proof verification with SP1Verifier
- Game state transition to "Proven"

### Key Metrics

- **Total Time**: ~13 minutes (vs 66s in Mock Mode)
- **Total Cost**: ~0.5 PROVE tokens
- **Blocks Proven**: 1 (L2 block 2236 → 2237)

### Production Readiness Notes

1. Verifier contracts must match Succinct Network's SP1 version
1. Cycle/Gas limits should be set conservatively high
1. Auction strategy recommended for flexibility
1. Monitor PROVE token balance for continuous operation

---

## Appendix: Key Commands Reference

bash

`# Check game status
cast call <game_address> "status()(uint8)" --rpc-url <l1_rpc>
cast call <game_address> "gameOver()(bool)" --rpc-url <l1_rpc>

# Execute challenge
cast send <game_address> "challenge()" --value 0.001ether --rpc-url <l1_rpc> --private-key <pk>

# Deploy verifier
forge create src/v5.0.0/SP1VerifierPlonk.sol:SP1Verifier --rpc-url <l1_rpc> --private-key <pk> --broadcast

# Add verifier route
cast call <verifier> "VERIFIER_HASH()(bytes32)" --rpc-url <l1_rpc>
cast send <gateway> "addRoute(bytes4,address)" <selector> <verifier> --rpc-url <l1_rpc> --private-key <pk>

# Grant permissions
cast send <access_manager> "setProposer(address,bool)" <addr> true --rpc-url <l1_rpc> --private-key <pk>
cast send <access_manager> "setChallenger(address,bool)" <addr> true --rpc-url <l1_rpc> --private-key <pk>`