Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-03-04

## Major Changes

- In general, removed ambiguous notations and ensured consistency
- Replaced the abbreviation "$Seig$" for seigniorage with $\Phi$ to make it more concise and visually distinct
- Removed the weight constant for STOS which is not used anymore
- The seigniorage weight constant for the DAO has been removed, as the DAO's seigniorage can be simply expressed as the total seigniorage minus the amounts allocated to staking and L2

## Notations for Supply

- $T$: Total TON supply
  - $T=T_{L1}+T_{L2}$
- $T_{L1}$: TON L1 Native Supply
  - TON existing or staked in L1, excluding the amount bridged to L2
- $T_{L2}$: TON L2 Bridged Liquidity
  - Previously, named $D$
  - TON L2 supply is only TON bridged to L2 from L1

## Notations for Staking & Seiniorage

- $S$: Total staking amount in L1
  - $S \subset T_{L1}$

## Notations for seigniorage and Its Distribution

- $\Phi$: Total seigniorage
  - $\Phi = \Phi_{L1} + \Phi_{L2} + \Phi_{DAO}$
- $T_{\Phi}$: Effective TON supply for seiniorage
  - The staked amount and the L2 amount mainly affects to the seigniorage distribution
  - $T_{\Phi} = S+T_{L2}$
- $\Phi_{L1}$: seigniorage for L1 staking Users
  - $\Phi_{L1} = W_S \cdot \frac{S}{T}\Phi$ where $W_S \leq 1$
- $\Phi_{L2}$: seigniorage for L2 seqeuncers based on the TON amounts in L2
  - $\Phi_{L2} = W_{L2} \cdot \frac{T_{L2}}{T} \Phi$ where $W_{L2} \leq 1$
- $\Phi_{DAO}$: seigniorage for Tokamak Network DAO
  - $\Phi_{DAO} = \Phi - \Phi_{L1} - \Phi_{L2} = \frac{T-W_S \cdot S - W_{L2} \cdot T_{L2}}{T} \cdot \Phi \geq 0$ 

## Notations for Multiple L2 Environment

- Let’s assume there’re mutliple rollups $1,2,...,k$
- Each rollups gets proportional seigniorage to the TON amount in their rollup
  - $\Phi_{L2,m} = \big( T_{L2,m} / \sum_{i} T_{L2,i} \big) \cdot \Phi_{L2}$ 

## References

- Tokamak Docs
[Link](https://github.com/tokamak-network/papers/blob/ae9bf27c631d3363bf03f492b3468c1f20b7e1b3/cryptoeconomics/tokamak-cryptoeconomics-en.md)

[https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics)
- Research Posts
[https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup](https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup)

[https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a](https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a)

[https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html](https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html)
- Research Papers
[https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf](https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf)

[https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3](https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3)

[https://arxiv.org/pdf/2308.02880](https://arxiv.org/pdf/2308.02880)