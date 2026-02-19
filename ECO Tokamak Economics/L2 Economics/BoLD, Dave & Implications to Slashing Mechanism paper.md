- What is the key differences in our slashing mechanism, if compare to BoLD and Dave?

| **Feature** | **Dave** | **BoLD ** | **(Im)possibility of Incentive Design** |
| --- | --- | --- | --- |
| **Core Idea** | Tournament bracket with regular state hashes | All-vs-all graph-based competition | Theoretical analysis of incentive compatibility |
| **Primary Goal** | Decentralization, security, and liveness | Delay attack resistance and bounded completion time | Analyze economic viability and incentive compatibility |
| **Challenge Structure** | Tournament bracket with multi-stage disputes | Dynamically growing graph with all-vs-all bisection | Abstract model of single-winner vs. multi-winner designs |
| **Winner Determination** | Winner of the tournament bracket | Root with the highest aggregated bottom-up timer | Not applicable (analyzes winner-take-all vs. inclusive rewards) |
| **Scalability Approach** | Dense computation hashes and poly-logarithmic scaling | Recursive refinement with a unified timer system | Winner multiplicity (non-exclusionary multi-winner design) |
| **Completion Time** | 2-5 challenge periods | Constant (≈ 2 challenge periods) | Not applicable (focuses on feasibility, not speed) |
| **Honest Party Costs** | Constant hardware, but substantial computation | Computation scales with number of adversaries (NA) | Provides cost bounds for feasibility (e.g., Dp ≥ ĉA/(1-η)) |
| **Key Advantage** | Logarithmic scaling of settlement delay | Constant and fast dispute resolution time | Provides clear, mechanism-agnostic feasibility conditions |
| **Objectives** | Cartesi optimizes for low honest-party computation cost | BoLD optimizes for completion time, | Incentivize honest party by ensuring non-negative net payoff |
| **Threat Model Focus** | General subversion of blockchain process | Delay attacks, censorship, and resource exhaustion | Colluding minorities and ordering power by proposers/builders |
| **Practicality** | Implementation-ready design | Deployed system (replaces Arbitrum Classic) | Not implemented |
| **Relationship to Prior Work** | Evolution of PRT and Cartesi | Replacement for Arbitrum Classic | Builds on general literature of rollup dispute protocols |

BoLD
**"all-versus-all"** model. Unlike previous protocols where a winner only took the stake of one specific opponent, BoLD allows a single honest party to win against *any* number of adversaries simultaneously, potentially collecting reimbursements from a pool of malicious stakes. The "edge" abstraction allows the system to treat the dispute as a single shared game rather than multiple separate ones. Instead of the honest party having to fight Challenger A, then Challenger B, then Challenger C in a row, BoLD allows the honest party to defend a single "honest edge" against all attackers at once. anyone can create a trustless smart contract to pool funds together and defend Arbitrum against invalid claims, or challenge invalid claims posted by others. 

A winner is a root node. When a root node is declared as winner, the honest edge is identified, and all stakers defending the honest edge can claim back their stake. This could be understood as “multi-winner”, but unclear how rewards are splitted


