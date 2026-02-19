Tokamak layer 2(L2) Cryptoeconomics

[https://tokamak-network.github.io/papers/tokamak-cryptoeconomics-en.pdf](https://tokamak-network.github.io/papers/tokamak-cryptoeconomics-en.pdf)

### Recent Whitepaper

[Link](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md)

[Link](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md)

## **Part 1. Current Design (per Tokamak whitepaper)**

- **Sequencer role**
  - Orders L2 transactions, produces blocks, and submits them to L1.
  - Must lock **collateral (C)**, slashed if invalid blocks are posted.
  - Earns **transaction fees + seigniorage**, where seigniorage share is proportional to:


$$








\frac{D + C}{T} \cdot Seig
$$

where D = user deposits, T = total TON supply.

- **Challenge mechanism**
  - 7–14 day dispute window. Fraud proofs can be submitted; slashing applies to sequencers, challengers, and even passive stakers.
- **Fast withdrawals**
  - Provided by **independent liquidity providers** (not necessarily sequencers).
  - They earn **fast withdrawal fees** for fronting liquidity.
  - Sequencers *could* act as FW providers, but this is optional.

---

## **Part 2. Critical Perspective**

- Compared to other L2s (Optimism, Arbitrum), Tokamak sequencers face a **heavier burden**:
  1. Collateral slashing risk.
  1. Dependence on TVL growth to maximize seigniorage.
  1. (Optional) FW liquidity provision, adding capital risk.
- **Profit model (simplified):**

$$








Profit = \Big(\tfrac{D+C}{T} \cdot Seig + Fees \Big) - \Big(Cost_{L1} + p_{inv}\alpha C + p_{nc}C \Big)
$$

-  **Limit behavior (moral hazard):**

$$








\lim_{D \to \infty} Profit = \infty
$$

→ Once sequencer earnings far exceed C, even losing the full collateral is not a deterrent. This creates **moral hazard**: sequencers may act dishonestly once “they’ve already made enough.”

- **If also providing FW liquidity:**

$$








Profit = \dots - r_{liq} \cdot L_{fw}
$$

→ Capital burden grows further.


- **Implication**
  - Current model discourages **permissionless sequencers**, since only large, well-capitalized actors can manage this burden.
  - Other L2s aim for simpler “fees + MEV – costs” structures, which keep entry easier.
  - A safer model would:
    - Decouple seigniorage from pure deposit size.
    - Tie **collateral dynamically to sequencer earnings** (e.g., “once revenue > threshold ⇒ collateral rises”).
    - Align risk with profit to reduce moral hazard and centralization pressure.

Minute of 9/21 Meeting

1. Modular Approach - Validator Set Support - Additional Security Layer - RAT
1. Hybrid Approach - zk vs OP
1. Section 5 → Validity Proof - Discuss with zk Team
1. Section 4 → Utilities of TON
1. 