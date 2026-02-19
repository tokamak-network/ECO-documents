Seminar material [https://docs.google.com/presentation/d/1EOXKqeunAStk8X3mVcC_9PdIxOWbaN5A/edit?usp=drive_link&ouid=114240629257411445292&rtpof=true&sd=true](https://docs.google.com/presentation/d/1EOXKqeunAStk8X3mVcC_9PdIxOWbaN5A/edit?usp=drive_link&ouid=114240629257411445292&rtpof=true&sd=true)

<u>**Why should we care about a market for ZK proofs?**</u>
  1. Fraud proof relies on game theoretic incentives to deter fraud, yet it remains vulnerable to well-funded attackers since the Total Value Secured could be large enough for an attacker to justify spending hundreds of millions of dollars to potentially gain billions. (participation is unrestricted, either by imposing a permission list or demanding the deposit of expensive *bonds). *Transition to ZK is natural to ensure security.
  1. Zero Knowledge (ZK) Rollups, e.g. Starknet and ZkSync, are being used today as a scaling solution on Ethereum. Their success led to a steadily growing demand in ZK proofs. Prover markets are a natural evolution for ZK Rollups as part of their transition towards decentralization
  1. If our roll-ups become zk rollups, or zk-based fraudproof, then our sequencers will become zk sequencers. It will be their job to submit the validity proof.
  1. Validity proof is expensive to create. So, our sequencers will have the incentive to find parties with capable hardware to produce the proof, ask them to produce the proof in exchange for a fee. This is zk proving market.
  1. Especially, if we adopt the hybrid approach (zk-basee fraud proof), zk sequencer only need to submit a validity proof once challenged. As a result, there is less incentive for them to invest heavily on hardware to generate the proof. A zk proof market address this issue nicely: sequencers don’t always have to create the proof on their own; they can buy it when they need to. 

⇒ There seems to be an organic alignment of interest between parties, or in economic terms, a coincidence of wants. This is a reasonable economic foundation for a market. 

<u>**Theoretical Foundation**</u>
Based on the following post: [On Ethereum Prover Market Design](https://ethresear.ch/t/on-ethereum-prover-market-design/22916)

The central problem is: How do we create a market where block proposers (who need proofs) can efficiently and safely buy them from provers (who have the hardware to make them)?

The post compares **02** main ways to design this market: Auction vs. Lotteries

|  | **Proof Lotteries (The "Permissionless" Option)** | **Auction-liked Staked Allocations (The "Guaranteed" Option)** |
| --- | --- | --- |
| Summary | The proposer announces a "prize" (reward). Any prover can submit a proof, and the prize is split among those who do. | Provers must put up a "stake" (collateral) to be eligible. The proposer then "allocates" the job to specific provers ahead of time. |
| What it means? | Suppose you are the buyer of the proof (block proposer) looking for a seller (prover). You don't know exactly who will show up, but if you set the prize high enough, someone likely will. | Suppose you are the buyer of the proof (block proposer) looking for a seller. The sellers (provers) approach you first by staking their collateral to be eligible, then engage in a bidding process. If they are chosen but fail to deliver, their stake is slashed. |
| Matching logic | The post mentions that setting a prize of roughly ln(V) (the natural log of the block's value) is enough to ensure someone submits a proof with high probability. | There is no prize set in advance. It is a dynamic multi-round auction. |
| Trade-offs | Lack price signaling & adjustment, thus the market is considered “not efficient”: the prize is too rigid that it may fail to reflect the level of resource needed for a block (i.e: prize is too low for a difficult block, and as a result no one will bother)

Requires only 1 round of communication & fully permissionless ⇒ reduce general waste of resource | Provide a more efficient market by allowing the prize to update dynamically, but require upfront collateral from bidders ⇒ more capital intensive, thus favors wealthy provers ⇒ risk of centralization. 

Stronger guarantee that proof would be delivered (because of staked collateral)

Requires multiple rounds of communication |

Reference on Auction type: [https://pure.uva.nl/ws/files/134864661/Integration_of_Blockchain_and_Auction_Models.pdf](https://pure.uva.nl/ws/files/134864661/Integration_of_Blockchain_and_Auction_Models.pdf)

(table II)

<u>**Comparison of existing solutions**</u>
| Player | Mechanism Category | Specific Mechanism | Cost Model | Incentive Structure | Efficiency & Key Features |
| --- | --- | --- | --- | --- | --- |
| [**Succinct**](https://blog.succinct.xyz/network/introducing-the-succinct-network-architecture-and-the-prove-token/)**

** | Auction-Based | Reverse Auction with Staking | Price discovery via competitive bidding. Requesters pay the winning (lowest) bid price in `$PROVE` tokens.  | Provers are rewarded with the fee for the winning bid. Staking `$PROVE` is required to participate, with slashing for non-delivery. Future "proof contests" aim to broaden rewards. | Simple, fast, and effective for homogenous proof requests. Low latency matching. Architecture separates off-chain auctioneering from on-chain settlement. |
| [**Brevis**](https://brevis.network/whitepaper/provernet.pdf)**

**[**Brevis ProverNet**](https://blog.brevis.network/2025/11/17/brevis-provernet-the-open-marketplace-for-zero-knowledge-proofs/) | Auction-Based | Truthful Online Double Auction (TODA) | Two-sided price discovery. Both requesters and provers submit bids. Fees cover prover payments and operational costs.  | Truthful bidding is the optimal strategy. Designed to handle heterogeneous workloads, matching jobs to provers with specific capabilities. Runs on a dedicated rollup for high throughput.  | Natively supports diverse and multi-stage proof pipelines. High-performance and scalable due to its specialized "glue-and-coprocessor" architecture. Proven in production with major partners. |
| [**Boundless (RISC Zero)**](https://dev.risczero.com/api/generating-proofs/remote-proving) | Auction-Based | Reverse Dutch Auction + [Proof of Verifiable Work (PoVW)](https://www.gate.com/tr/learn/articles/what-is-boundless-zkc/12097) | Price discovery via Reverse Dutch Auction. Prover rewards are proportional to the verified computational work (PoVW).  | [Dual incentive: ](https://www.binance.com/en/research/analysis/boundless)marketplace fees from jobs and `$ZKC` token rewards based on PoVW. Staking `$ZKC` is required, with slashing for failures.  | **PoVW is a key differentiator**, enabling fair, compute-based rewards. Universal, cross-chain protocol supporting Rust & C++. Decentralized from day one. |
| [**Lagrange**](https://docs.lagrange.dev/lpn/architecture/dara) | Auction-Based
 | Combinatorial Auctions, Multi-attribute Auctions, Dynamic Programming, Approximation Algorithms | Predictable pricing models for enterprise planning, driven by a managed network rather than open real-time auctions.  | Operators stake `$LA` tokens and are rewarded for reliable service. Penalties (slashing) for delays or failures. Focus on uptime and performance guarantees. | Enterprise-grade reliability with 99.9% uptime guarantees. Modular "network of networks" architecture. Optimized for specialized hardware and specific ZK circuits.  |
| [Kalypso (by Marlin)](https://docs.kalypso.org/learn/) | Auction-Based (Orderbook with planned auction support ) | Users specify their needs in terms of proof time and cost, and Kalypso finds the best options based on these criteria. | Orderbook pricing; users prioritize cost or speed | POND token staking; slashing for missed response times | Flexible matching; supports [4 market types](https://docs.kalypso.org/user-guides/creating-a-market/determine-market-type) for different verification needs (based on whether or not inputs need to be confidential) |
| [=nil; Foundation](https://nil.foundation/blog/post/proof-market) | Orderbook-Based Market | Order book treating proofs as commodities with expiration | Market-driven pricing; expiration creates dynamic pricing | Proof generators and circuit designers earn from sales; decentralized nodes reduce front-running | Generic model handles both urgent and non-urgent requests; blockchain-agnostic |

<u>**Comparison of existing solutions: Performance & Liveness**</u>
| **Prover Network** | **zkVM** | **Benchmark Cost** | **Proof Generation Time** | **Liveness** | Live Dashboard |
| --- | --- | --- | --- | --- | --- |
| [**Succinct**](https://blog.succinct.xyz/network/introducing-the-succinct-network-architecture-and-the-prove-token/)**

** | SP1 (Hypercube) | $0.005-$0.01/tx | <12s | Mainnet
(Aug 2025) | [Succinct Explorer](https://explorer.succinct.xyz/)
(See Total Fee) |
| [**Brevis**](https://brevis.network/whitepaper/provernet.pdf)**

**[**Brevis ProverNet**](https://blog.brevis.network/2025/11/17/brevis-provernet-the-open-marketplace-for-zero-knowledge-proofs/) | RISC Zero | $0.01-$0.04/tx | Avg. 6.9s | Mainnet
(Sep 2025) | N/A |
| [**Boundless (RISC Zero)**](https://dev.risczero.com/api/generating-proofs/remote-proving) | Pico zkVM | Market-based
(PoVW-based) | Market-based | Mainnet Beta
(Dec 2025) | [Orders](https://explorer.boundless.network/orders)
(See Locked Price) |
| [**Lagrange**](https://docs.lagrange.dev/lpn/architecture/dara) | Plonky2/3 | Market-based  | Market-based | Mainnet
(2024~) | N/A |
| [Kalypso (by Marlin)](https://docs.kalypso.org/learn/) | Circuit-agnostic | Market-based | Market-based | Mainnet
(Jul 2025~) | N/A |
| [=nil; Foundation](https://nil.foundation/blog/post/proof-market) | zkLLVM | Market-based | Market-based | Testnet v1
(Oct 2024~) | N/A |

<u>**Observations: **</u>

- While the theory mentions both designs, the production market has converged almost entirely on auction-based mechanisms, with significant variations in implementation details. The absence of lottery-based systems suggests that players value the benefits of price discovery, economic security through competitive staking, and direct alignment of rewards with computational contribution
- While auctions have clearly become the dominant mechanism in production markets, there are growing concerns in academia about centralization risks. Hybrid approaches combining auctions and lotteries, such as [Prooφ (Wang et al., 2024)](https://arxiv.org/abs/2404.06495), have been proposed.
- On the other hand, Succinct currently uses a reverse auction but plans to transition to a [Proof Contest](https://resources.cryptocompare.com/asset-management/20420/1754473565450.pdf) mechanism. Proof Contest is an all-pay auction structure that distributes rewards to a broader set of provers rather than winner-take-all. By introducing probabilistic allocation, it ensures that smaller or less efficient provers still have opportunities to participate, promoting a decentralized prover set.
- In case of [Boundless](https://read.boundless.network/), rewards are distributed proportionally to actual zkVM cycles performed. Instead of meaningless hash computations in traditional PoW, provers generate useful ZK proofs. This is similar to how mining pools distribute rewards proportionally to contributed hashpower, ensuring smaller participants remain incentivized and promoting decentralization.