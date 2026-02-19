Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2024-02-18

## Error and Critial Issues in the Economics Paper

Basic notation for understanding to start:

- $D$: Total deposit by L2 sequencers
- $T$: Total TON supply
- $S$: Total staking amount

The following notation definitions don’t match to the seiniorage explaination

- $T_{L2} \triangleq D + C$
  - Total TON supply in L2
  - Where is C’s definition?
- $T_{L1} \triangleq T-D-C=T-T_{L2}$
  - Total TON supply in L1

Senioriage examples:

- Sequencers : $\frac{D}{T}Seig = \frac{T_{L2}}{T}Seig$
  - Where is C? $\frac{D}{T}Seig \not = \frac{T_{L2}}{T}Seig = \frac{D+C}{T}Seig$
- Stakers: $\frac{T-D}{T}Seig = \frac{T-T_{L2}}{T}Seig = \frac{T_{L1}}{T}Seig$
  - Why stakers get seiniorage proportional to the total L1 supply, not the total L1 staking?

## Correction

My assumption is that the authors intended:

- The sum of seinioriage of the sequencers and the stakers is the total seinioriage
  - Here I introduce new notations for convenience
    - Total seiniorage: $\Phi$
    - Total seiniorage for sequencers: $\Phi_{seq}$
    - Total seiniorage for stakers: $\Phi_{stk}$
  - Then, $\Phi = \Phi_{seq} + \Phi_{stk}$
- $T=T_{L1} + T_{L2}$
  - Here has two issues:
    - $C$ is not cleary defined
    - Stakers don’t need to get seinioriage proportional to the total L1 supply, not the staking amount
  - I propose to solve this issue by defining $C$ clearly into two notations:
    - $C$: The total circulating supply (easily, not staked TON)
    - $C_{L1}$: The circulating supply in L1
    - $C_{L2}$: The circulating supply in L2
    - That is, $C=C_{L1}+C_{L2}$
  - Then, we can have the following relationship:
    - $T_{L1} = S+C_{L1}, T_{L2} = D+C_{L2}$

Finally, using the above correction, we can notate the seinioriages as:

- Let $T_{\Phi} \triangleq  T_{L2} + S$
  - The total supply related to sienioriage
  - This is to exclude the not staked supply in L2 for seiniorage
- $\Phi_{seq}=\frac{D+C_{L2}}{T_\Phi}$
- $\Phi_{seq}=\frac{S}{T_\Phi}$


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