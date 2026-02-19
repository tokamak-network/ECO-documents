**Author:** Bernard Lee, Suhyeon Lee

**Date:** February 2, 2026

## 1. Experimental Results: OP Succinct ZKP Costs

We conducted tests using OP Succinct with Succinct Prover Network to measure actual ZKP costs.

### 1.1 Test Environment

| Component | Configuration |
| --- | --- |
| L1 | Kurtosis devnet (Ethereum) |
| L2 | OP Stack devnet |
| Prover | Succinct Prover Network |
| Proof Type | SP1 (Range: Compressed, Aggregation: Plonk) |

### 1.2 Test Results Summary

| Metric | 1 TX | 1000 TXs | Ratio |
| --- | --- | --- | --- |
| Range PGU | 1.68B | 11.85B | 7x |
| Range Time | 6m 22s | 10m 40s | 1.7x |
| Range Cost | ~0.2 PROVE | ~5.5 PROVE | 27x |
| Agg PGU | 1.5M | 1.5M | 1x (fixed) |
| Agg Cost | ~0.3 PROVE | ~0.3 PROVE | 1x (fixed) |
| **Total Cost** | ~0.5 PROVE | ~5.8 PROVE | 12x |
| **Cost per TX** | 0.5 PROVE | 0.0058 PROVE | **86x cheaper** |

### 1.3 Key Findings

1. **Aggregation proof is fixed cost**: ~0.3 PROVE regardless of batch size
1. **Range proof scales sublinearly**: 1000x TXs → 7x PGU (fixed overhead amortization)
1. **Batch proving efficiency**: 86x cost reduction per TX at 1000 TXs

### 1.4 Cost Model Parameters (Derived from Testing)

| Parameter | Symbol | Value | Description |
| --- | --- | --- | --- |
| Range base fee | $C_{\text{range}}^{\text{fixed}}$ | 0.2 PROVE | Fixed cost component |
| Range variable | $c_{\text{range}}$ | 0.45 PROVE/bPGU | Per-PGU cost |
| Aggregation | $C_{\text{agg}}$ | 0.3 PROVE | Fixed (Plonk proof) |

---

## 2. Motivation: Why Hybrid Approach?

### 2.1 The Batch Size Dilemma

In optimistic rollups, **batch size** creates a fundamental trade-off:

```
┌─────────────────────────────────────────────────────────────────┐
│  Normal Operation: Larger batches are better                    │
│  ─────────────────────────────────────────                      │
│                                                                  │
│  On-chain submission cost is mostly fixed (calldata overhead)   │
│  → Larger batch = lower cost per TX                             │
│                                                                  │
│  Example:                                                        │
│    - 1 TX batch: $33 per TX                                     │
│    - 1000 TX batch: $0.033 per TX (1000x cheaper)               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Dispute Resolution: Larger batches are problematic             │
│  ─────────────────────────────────────────────────              │
│                                                                  │
│  If challenged, must prove the ENTIRE batch via ZKP             │
│  → Larger batch = higher ZKP cost                               │
│                                                                  │
│  Example (from our tests):                                       │
│    - 1 TX batch: 0.5 PROVE (~$0.20)                             │
│    - 1000 TX batch: 5.8 PROVE (~$2.32)                          │
└─────────────────────────────────────────────────────────────────┘

```

### 2.2 The Solution: Bisection to Narrow ZKP Scope

**Idea**: Don't prove the entire batch—use bisection to find the disputed segment, then prove only that small segment.

```
Original batch: 1000 TXs (10B PGU)
                    │
    Bisection (d=10 rounds)
                    │
                    ▼
Disputed segment: ~1 TX (10M PGU)
                    │
         ZKP for small segment
                    │
                    ▼
Cost: ~0.5 PROVE instead of ~5.8 PROVE (10x savings)

```

### 2.3 The Problem with Interactive Bisection

Traditional bisection protocols (OP Stack Cannon, Arbitrum BOLD, Cartesi DAVE) require **interactive** rounds:

```
Round 1: Proposer commits to midpoint     → 1 TX + wait
Round 2: Challenger picks left/right      → 1 TX + wait
Round 3: Proposer commits to new midpoint → 1 TX + wait
...
Round N: Final step                       → 1 TX + wait

Total: O(log N) transactions, each with timeout periods
Time: Could take days to weeks

```

**Problems**:

- High gas costs (many transactions)
- Long delays (timeout periods add up)
- Complex game-theoretic security

### 2.4 Our Solution: Pre-committed Hybrid

**Key insight**: The proposer already knows all intermediate states. Why not reveal them all at once?

```
┌─────────────────────────────────────────────────────────────────┐
│  Pre-committed Bisection + ZKP                                  │
│  ─────────────────────────────                                  │
│                                                                  │
│  Step 1: Challenger says "Invalid!"              → 1 TX         │
│  Step 2: Proposer reveals ALL commitments        → 1 TX         │
│  Step 3: Challenger pinpoints disagreement       → 1 TX         │
│  Step 4: Proposer submits ZKP for that segment   → 1 TX         │
│                                                                  │
│  Total: 3-4 transactions (vs O(log N) for interactive)          │
│  Time: Hours instead of days/weeks                              │
└─────────────────────────────────────────────────────────────────┘

```

### 2.5 Summary: Evolution of Approach

| Stage | Approach | Problem |
| --- | --- | --- |
| 1 | Large batches for efficiency | High ZKP cost if disputed |
| 2 | Bisection to narrow scope | Too many rounds, slow |
| 3 | **Pre-committed + ZKP** | ✓ Fast, cheap, secure |

---

## 3. Existing Dispute Resolution Protocols

| Protocol | Bisection Method | Final Resolution | Key Feature |
| --- | --- | --- | --- |
| **OP Stack (Cannon)** | Interactive (per-round tx) | One-step proof (MIPS on-chain) | Standard interactive bisection |
| **Arbitrum BOLD** | Interactive + History Commitment | One-step proof | Trustless cooperation via shared history |
| **Cartesi DAVE** | Tournament + Interactive | One-step proof | Sybil-resistant, permissionless |
| **Our Proposal** | **Pre-committed (single reveal)** | **ZK Proof** | Minimal rounds + ZKP finality |

### 3.1 OP Stack (Cannon)

- Fully interactive bisection game
- Each round requires an on-chain transaction
- Final resolution: execute single MIPS instruction on-chain
- $O(\log N)$ transactions for dispute resolution

### 3.2 Arbitrum BOLD

- Proposers commit to entire execution history upfront (Merkle tree)
- Enables "trustless cooperation": honest parties with same correct history can collaborate without explicit coordination
- Bisection still interactive, but bounded delay guaranteed
- History commitment serves as **reference for cooperation**, not to reduce rounds

### 3.3 Cartesi DAVE

- Permissionless refereed tournaments
- Sybil-resistant: single honest validator can win against many attackers
- Resources scale logarithmically with number of opponents

### 3.4 Our Proposal: Pre-committed Bisection + ZKP

- Proposer reveals **all intermediate commitments in one transaction**
- Challenger pinpoints disagreement in **one transaction**
- Final resolution via **ZK proof** (not one-step on-chain execution)
- **Total: 3-4 transactions** regardless of batch size

---

## 4. Protocol Flow: Pre-committed Bisection + ZKP

### 4.1 Normal Operation (No Dispute)

```
┌─────────────────────────────────────────────────────────────────┐
│  Proposer                                                        │
│    │                                                             │
│    ├──► Submit batch root commitment to L1                       │
│    │    (Pre-state root, Post-state root, Batch root)           │
│    │                                                             │
│    └──► Cost: ~$33 (L1 calldata)                                │
│                                                                  │
│  Challenge Period: 7 days                                        │
│    │                                                             │
│    └──► No challenge → Batch finalized ✓                        │
└─────────────────────────────────────────────────────────────────┘

```

### 4.2 Dispute Resolution Flow

```
┌─────────────────────────────────────────────────────────────────┐
│  Step 1: Challenge                                               │
│  ─────────────────                                               │
│  Challenger: "This batch is invalid!"                           │
│    │                                                             │
│    └──► 1 transaction                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 2: Reveal Intermediate Commitments                         │
│  ───────────────────────────────────────                         │
│  Proposer reveals d levels of commitments in ONE transaction:   │
│                                                                  │
│    Level 0: [root]                     (1 commitment)           │
│    Level 1: [c₀, c₁]                   (2 commitments)          │
│    Level 2: [c₀₀, c₀₁, c₁₀, c₁₁]       (4 commitments)          │
│    ...                                                           │
│    Level d: [c₀...₀, ..., c₁...₁]      (2^d commitments)        │
│                                                                  │
│    Total: 2^(d+1) - 1 commitments                               │
│    │                                                             │
│    └──► 1 transaction (calldata only, ~$0.02-0.03)              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 3: Pinpoint Disagreement                                   │
│  ────────────────────────────                                    │
│  Challenger examines commitments and identifies which segment   │
│  (at level d) contains the error:                               │
│                                                                  │
│    "I disagree with segment #42 (TXs 4200-4299)"                │
│    │                                                             │
│    └──► 1 transaction                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 4: ZK Proof for Narrowed Range                            │
│  ───────────────────────────────────                            │
│  Proposer generates ZK proof for ONLY the disputed segment:     │
│                                                                  │
│    Original batch: G PGU (e.g., 10 billion)                     │
│    Disputed segment: G/2^d PGU (e.g., 10 million at d=10)       │
│                                                                  │
│    ZK Proof proves: preState --[execute segment]--> postState   │
│    │                                                             │
│    └──► 1 transaction (submit proof)                            │
│                                                                  │
│  Verifier checks proof on-chain → Dispute resolved              │
└─────────────────────────────────────────────────────────────────┘

```

### 4.3 Cost Comparison

| Approach | Transactions | Estimated Cost |
| --- | --- | --- |
| Interactive Bisection (Cannon) | $O(\log N)$ ~20-30 tx | ~$50-100 |
| Full Batch ZKP | 1 tx | ~$2.00 (5 PROVE) |
| **Pre-committed + ZKP (ours)** | 3-4 tx | **~$0.25** (0.5 PROVE) |

---

## 5. Problem Statement

**Given**: A batch with total Prover Gas Units $= G$

**Decision**: Bisection depth $d$ (number of levels to reveal before generating ZKP)

**Objective**: Minimize total dispute resolution cost

---

## 6. Cost Model

### 6.1 Two-Stage ZKP Architecture (OP Succinct)


$C_{\text{zkp}}(G) = \underbrace{C_{\text{range}}^{\text{fixed}} + c_{\text{range}} \cdot G}{\text{Range Proof}} + \underbrace{C{\text{agg}}}_{\text{Aggregation}}$

### 6.2 Reveal Cost

Each commitment requires 32 bytes of calldata:


$\text{Gas per commitment} = 32 \text{ bytes} \times 16 \text{ gas/byte} = 512 \text{ gas}$


**Current market conditions** (January 2026):

| Parameter | Value |
| --- | --- |
| Gas price | ~0.5 gwei |
| ETH price | ~$2,700 |
| PROVE price | ~$0.40 |

**Cost per commitment**:


$c_r = \frac{512 \times 0.5 \times 10^{-9} \times 2700}{0.40} \approx 0.002 \text{ PROVE}$


### 6.3 Total Dispute Cost Function


$C(d) = C_{\text{reveal}}(d) + C_{\text{zkp}}\left(\frac{G}{2^d}\right)$


Expanding:


$\boxed{C(d) = c_r \cdot d + c_{\text{range}} \cdot G \cdot 2^{-d} + C_0}$

where $C_0 = C_{\text{range}}^{\text{fixed}} + C_{\text{agg}} = 0.5$ PROVE (total fixed cost).

---

## 7. Optimization

### 7.1 First-Order Condition


$\frac{dC}{dd} = c_r - c_{\text{range}} \cdot G \cdot \ln(2) \cdot 2^{-d} = 0$

### 7.2 Analytic Solution

**Optimal bisection depth**:


$\boxed{d^* = \log_2(\lambda G)}$


where the **cost ratio parameter**:


$\lambda = \frac{c_{\text{range}} \cdot \ln(2)}{c_r} = \frac{0.45 \times 0.693}{c_r} = \frac{0.312}{c_r}$


### 7.3 Optimal Remaining PGU


$\boxed{G^* = \frac{G}{2^{d^*}} = \frac{c_r}{c_{\text{range}} \cdot \ln(2)} = \text{constant}}$


**Key insight**: The optimal remaining PGU is a **constant**, independent of the initial batch size $G$.

### 7.4 Minimum Cost


$\boxed{C^*(G) = c_r \cdot \log_2(e\lambda G) + C_0}$


This shows **logarithmic scaling** with batch size $G$.

---

## 8. Floor Effect Analysis

### 8.1 The Problem

The range proof cost has a floor at $C_{\text{range}}^{\text{fixed}} = 0.2$ PROVE.

As $d$ increases, $c_{\text{range}} \cdot G/2^d \to 0$, but total cost cannot go below $C_0 = 0.5$ PROVE.

### 8.2 Practical Depth Limit


$d_{\text{floor}} = \log_2\left(\frac{G \cdot c_{\text{range}}}{C_{\text{range}}^{\text{fixed}}}\right) = \log_2\left(\frac{G}{0.444}\right)$

Beyond this depth, further bisection provides diminishing returns.

---

## 9. Numerical Analysis

### 9.1 Parameters

| Parameter | Symbol | Value |
| --- | --- | --- |
| Batch size | $G$ | 10 bPGU |
| Cost ratio | $\lambda$ | 156 |
| Reveal cost | $c_r$ | 0.002 PROVE |

### 9.2 Cost Table by Depth

| $d$ | $G_{\text{remaining}}$(bPGU) | $C_{\text{reveal}}$ | $C_{\text{range}}$ | $C_{\text{agg}}$ | $C_{\text{total}}$ |
| --- | --- | --- | --- | --- | --- |
| 0 | 10.000000 | 0.000 | 4.700 | 0.3 | 5.000 |
| 1 | 5.000000 | 0.002 | 2.450 | 0.3 | 2.752 |
| 2 | 2.500000 | 0.004 | 1.325 | 0.3 | 1.629 |
| 3 | 1.250000 | 0.006 | 0.763 | 0.3 | 1.069 |
| 4 | 0.625000 | 0.008 | 0.481 | 0.3 | 0.789 |
| 5 | 0.312500 | 0.010 | 0.341 | 0.3 | 0.651 |
| 6 | 0.156250 | 0.012 | 0.270 | 0.3 | 0.582 |
| 7 | 0.078125 | 0.014 | 0.235 | 0.3 | 0.549 |
| 8 | 0.039063 | 0.016 | 0.218 | 0.3 | 0.534 |
| 9 | 0.019531 | 0.018 | 0.209 | 0.3 | 0.527 |
| 10 | 0.009766 | 0.020 | 0.204 | 0.3 | 0.524 |
| 11 | 0.004883 | 0.022 | 0.202 | 0.3 | **0.524** |
| 12 | 0.002441 | 0.024 | 0.201 | 0.3 | 0.525 |
| 13 | 0.001221 | 0.026 | 0.201 | 0.3 | 0.527 |
| 14 | 0.000610 | 0.028 | 0.200 | 0.3 | 0.528 |
| 15 | 0.000305 | 0.030 | 0.200 | 0.3 | 0.530 |

**Optimal depth**: $d \approx 10\text{-}11$ (minimum at ~0.524 PROVE)

---

## 10. Comparison Summary

### 10.1 Cost Comparison ($G = 10$ bPGU)

| Approach | Dispute Cost | Transactions | Scaling |
| --- | --- | --- | --- |
| Pure ZKP (no bisection) | 5.00 PROVE | 1 | $O(G)$ |
| Interactive Bisection | ~0.5 PROVE + gas | ~20 tx | $O(\log G)$ |
| **Hybrid (optimal $d$)** | **0.52 PROVE** | **3-4 tx** | $O(\log G)$ |

### 10.2 Key Advantages of Hybrid Approach

1. **10x cost reduction** vs pure ZKP
1. **Minimal transactions** (3-4 vs ~20 for interactive)
1. **Logarithmic scaling** with batch size
1. **ZKP finality** (cryptographic guarantee, not game-theoretic)

---

## 11. Smart Contract Design

### 11.1 Contract Interface

```solidity
interface IPrecommittedDisputeGame {
    // Step 1: Proposer submits batch
    function proposeBatch(
        bytes32 preStateRoot,
        bytes32 postStateRoot,
        bytes32 rootCommitment,
        uint256 batchSize
    ) external returns (bytes32 batchId);

    // Step 2: Challenger initiates dispute
    function challenge(bytes32 batchId) external;

    // Step 3: Proposer reveals all intermediate commitments
    function revealCommitments(
        bytes32 batchId,
        bytes32[] calldata commitments,  // 2^d - 1 commitments
        uint256 depth
    ) external;

    // Step 4: Challenger pinpoints disagreement
    function pinpointDisagreement(
        bytes32 batchId,
        uint256 segmentIndex,           // Which leaf segment (0 to 2^d - 1)
        bytes32 expectedCommitment      // What challenger believes is correct
    ) external;

    // Step 5: Proposer submits ZK proof
    function submitZKProof(
        bytes32 batchId,
        bytes calldata proof,
        bytes calldata publicInputs
    ) external;
}

```

### 11.2 Data Structures

```solidity
struct Batch {
    bytes32 rootCommitment;
    bytes32 preStateRoot;
    bytes32 postStateRoot;
    uint256 batchSize;
    uint256 proposedAt;
    address proposer;
    GameStatus status;
}

struct Dispute {
    address challenger;
    bytes32[] intermediateCommitments;  // Revealed by proposer
    uint256 revealDepth;
    uint256 disagreementIndex;          // Pinpointed by challenger
    bool zkProofValid;
}

enum GameStatus {
    None,
    Proposed,       // Waiting for challenges
    Challenged,     // Waiting for proposer reveal
    Revealed,       // Waiting for challenger pinpoint
    Pinpointed,     // Waiting for ZK proof
    ProverWins,
    ChallengerWins
}

```

### 11.3 Commitment Tree Structure

For depth $d$, the proposer reveals a complete binary tree:

```
         Level 0:           root
                           /    \
         Level 1:        c₀      c₁
                        /  \    /  \
         Level 2:     c₀₀ c₀₁ c₁₀ c₁₁
                       ...
         Level d:    [2^d leaf commitments]

```

Each leaf commitment covers $G/2^d$ PGU of the original batch.

**Storage**: Commitments stored in array form (BFS order):

- Index 0: root
- Index 1-2: level 1
- Index 3-6: level 2
- Index $2^d - 1$ to $2^{d+1} - 2$: level $d$ (leaves)

### 11.4 Verification Logic

```solidity
function _verifyCommitmentTree(
    bytes32[] calldata commitments,
    bytes32 expectedRoot
) internal pure returns (bool) {
    // Verify each parent = hash(leftChild, rightChild)
    for (uint i = 0; i < (commitments.length - 1) / 2; i++) {
        bytes32 expected = keccak256(abi.encodePacked(
            commitments[2*i + 1],
            commitments[2*i + 2]
        ));
        if (commitments[i] != expected) return false;
    }
    return commitments[0] == expectedRoot;
}

```

---

## 12. Practical Recommendations

### 12.1 Optimal Depth Selection

For current market conditions (January 2026):


$d^* \approx 10\text{-}11 \text{ for typical batches}$


**Rule of thumb**: Bisect until remaining PGU reaches ~5-10M PGU.

### 12.2 Protocol Parameters

| Parameter | Recommended Value |
| --- | --- |
| Max depth | 15 |
| Challenge period | 7 days |
| Response timeout (reveal) | 2 hours |
| Response timeout (pinpoint) | 4 hours |
| Response timeout (ZK proof) | 6 hours |
| Target remaining PGU | 5-10M |

### 12.3 Expected Costs

| Scenario | Cost |
| --- | --- |
| Normal operation | ~$33 (L1 submission) |
| Dispute (total) | ~$0.25 (0.5 PROVE) |
| - Reveal cost | ~$0.01 |
| - ZK proof cost | ~$0.20 |
| - Gas costs | ~$0.04 |

---

## 13. Future Work: Optimal Batch Size

### 13.1 The Batch Size Optimization Problem

While this document focuses on optimal **bisection depth** given a fixed batch size, a natural extension is to optimize the **batch size itself**.

The key trade-off:


$\text{E}[\text{Cost}] = (1-p) \cdot C_{\text{normal}}(B) + p \cdot C_{\text{dispute}}(B)$


where:

- $B$ = batch size (number of TXs)
- $p$ = dispute probability
- $C_{\text{normal}}(B)$ = cost when no dispute (decreases with larger $B$)
- $C_{\text{dispute}}(B)$ = cost when disputed (increases with larger $B$, but only logarithmically with hybrid approach)

### 13.2 Preliminary Analysis

**Normal operation cost** (per TX):

$C_{\text{normal}}(B) / B \approx \frac{C_{\text{fixed}}^{\text{L1}}}{B}$

Decreases as $B$ increases (fixed L1 costs amortized).

**Dispute cost** (with hybrid approach):

$C_{\text{dispute}}(B) = c_r \cdot \log_2(\lambda B) + C_0$

Increases logarithmically with $B$.

### 13.3 Key Insight

With the hybrid approach, dispute costs scale as $O(\log B)$ rather than $O(B)$.

This means **larger batches are much more favorable** than in pure ZKP systems:

| Dispute Probability $p$ | Optimal Strategy |
| --- | --- |
| Very low ($p < 0.01%$) | Maximize batch size |
| Low ($p \approx 0.1%$) | Large batches still optimal |
| Moderate ($p \approx 1%$) | Balance needed, but still favor large batches |
| High ($p > 5%$) | Consider smaller batches |

### 13.4 Research Directions

1. **Empirical dispute probability estimation**
  - Historical data from existing rollups
  - Security model assumptions
1. **Dynamic batch sizing**
  - Adjust batch size based on observed dispute rates
  - Market conditions (gas prices, prover costs)
1. **Game-theoretic analysis**
  - Rational challenger behavior
  - Optimal bonding mechanisms
1. **Multi-prover market integration**
  - How prover competition affects optimal parameters
  - Auction mechanisms for proof generation
1. **Formal security analysis**
  - Formally model the existing OP Stack dispute game (Cannon)
  - Formally model our pre-committed bisection + ZKP protocol
  - Prove equivalence or improved security guarantees:
    - **Soundness**: A dishonest proposer cannot convince the protocol of an invalid state
    - **Completeness**: An honest proposer can always defend a valid state
    - **Liveness**: The protocol terminates within bounded time
  - Analyze attack vectors: censorship, griefing, delay attacks
  - Compare economic security assumptions between models

---

## 14. Summary

| Formula | Expression |
| --- | --- |
| Optimal depth | $d^* = \log_2\left(\frac{c_{\text{range}} \cdot G \cdot \ln(2)}{c_r}\right)$ |
| Optimal remaining PGU | $G^* = \frac{c_r}{c_{\text{range}} \cdot \ln(2)}$ |
| Minimum cost | $C^* = c_r \cdot \log_2(e\lambda G) + C_0$ |
| Cost scaling | $O(\log G)$ |

### 14.1 Key Formulas

### 14.2 Key Insights

1. **Constant optimal remainder**: The optimal PGU to prove via ZKP is independent of batch size
1. **Logarithmic scaling**: Total dispute cost scales as $O(\log G)$
1. **Pre-committed efficiency**: Reduces interactive rounds from $O(\log N)$ to 3-4 transactions
1. **ZKP finality**: Cryptographic guarantee vs game-theoretic security
1. **Current optimum**: $d \approx 10\text{-}11$, cost ~0.5 PROVE (~$0.20)

---

## Appendix A: Notation Reference

| Symbol | Description | Unit |
| --- | --- | --- |
| $G$ | Batch size | bPGU |
| $d$ | Bisection depth | rounds |
| $d^*$ | Optimal depth | rounds |
| $c_r$ | Reveal cost per commitment | PROVE |
| $c_{\text{range}}$ | Range proof variable cost | PROVE/bPGU |
| $C_{\text{range}}^{\text{fixed}}$ | Range proof base fee | PROVE |
| $C_{\text{agg}}$ | Aggregation cost | PROVE |
| $\lambda$ | Cost ratio parameter | - |

## Appendix B: Full Contract Implementation

See attached `PrecommittedDisputeGame.sol` for complete Solidity implementation.

## Appendix C: Derivation Details

### C.1 FOC Derivation

Starting from:

$C(d) = c_r \cdot d + c_{\text{range}} \cdot G \cdot 2^{-d} + C_0$


Taking derivative:

$\frac{dC}{dd} = c_r - c_{\text{range}} \cdot G \cdot \ln(2) \cdot 2^{-d}$


Setting to zero:

$c_r = c_{\text{range}} \cdot G \cdot \ln(2) \cdot 2^{-d}$

$2^{d} = \frac{c_{\text{range}} \cdot G \cdot \ln(2)}{c_r}$

$d^* = \log_2\left(\frac{c_{\text{range}} \cdot G \cdot \ln(2)}{c_r}\right) = \log_2(\lambda G)
$

### C.2 Minimum Cost Derivation

At $d^*$*:
*$2^{-d^*} = \frac{c_r}{c_{\text{range}} \cdot G \cdot \ln(2)}$


Substituting:

$C(d^*) = c_r \cdot d^* + c_{\text{range}} \cdot G \cdot \frac{c_r}{c_{\text{range}} \cdot G \cdot \ln(2)} + C_0$


$= c_r \cdot d^* + \frac{c_r}{\ln(2)} + C_0$


=$ c_r \cdot \left(d^* + \log_2 e\right) + C_0$


$= c_r \cdot \log_2(e \cdot 2^{d^*}) + C_0$


$= c_r \cdot \log_2(e\lambda G) + C_0$