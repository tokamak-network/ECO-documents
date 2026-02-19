Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-03-07

The original whitepaper and the highlighted revised whitepaper are as follows:

[original.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/40d38a60-cd88-41a4-b31b-17d4a544d62c/original.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D5SBY6U%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAddLLXW0PBAbdNLmTxwvOeAhgp0Jco5O2njSbK9bUVgIgfgBayuO9lMthk3ru%2BGkRWliDy3ZF7TTQ%2FU9Vfl4OG9oq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDIUR4HrwfWtT9LSnRircA7Zd0ELELZM8n5SFDMJ9Eq51X3z0%2FHwBx3AyLeeI4C4R5DaDSV8zBNhJ9euWedi%2FRkqPer91fve1eGLux1W3T0mYY%2B1sP%2FBuuQf781HY9rg%2FzLbN%2BRReGxFzMOzXaancCh4jJB63NemWMgGDkDAT7tQbK07y2Lb1J%2FTUmiCoI158%2BxbMj7fZ2HO5DQQHwS7ifNQ63Ugyds5un75zl1utQ%2F1x8FQqTdSfpU%2FluNQUTfEIb5xsvp6IQTQNO16%2FYJsOgBuITeDoXChFPAATkpdUKmPqTfla3khWXcZ6x%2FyjFXU75j2dRHtcwtCQjJH6plDbLK9iurNrlFFmQLzrgtkvsyyO6%2Bc4e%2FJru3JiHu%2BSH9WXg9Saj4hY7gy%2FdCQFZpQe2yyvyjOLsv80ukfzFYv83l4Jj2KACV%2F8CO2%2Fwz%2FXGOWQU73P59gEslGK05y1%2F97jc5Zlv7dp2o3i4Z75VU%2B99qj%2BjKcgfrvb73SBHZTAxOc1ggpIpsSW%2F%2FqTT8agyr8gBmTdiJOxdlBlsjJD0qp1yLko%2BcUcWEhTJ7XcgewzJDHA6HRNFDingHGRJccYd%2B3wVdT6RcFO1DCqogq9512PQLIjgb21s%2BiFMGYM6wO3ocN16OHCX6bb06MJlnYEMI%2Fx2cwGOqUBW6ckzHh%2Flg1aox2hL78C9NFjfbskV6HzCBill7CNkmowahryGjFOlUhTk1rBBKdkNHburYaP0jcaN7302U35azGmqxv609P4e0qew4J8CQuCbWhtcYOEOufursBTdFeVP9yhVUq5jj%2FLAlXb0kSRipGWdLKgnZXj5QK9m87Fd6FBjzXBSh93E7GUKcKHsJ4rczEYO0UJCtMcEcgWnEJfZFu8jzev&X-Amz-Signature=06eb4f94fd438cbeec335b6de3cd5adb28e6dc627531bdf5a5211d162b5aebeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[revised.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/77905a7e-9485-40a6-b701-840b8d4bec03/revised.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D5SBY6U%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAddLLXW0PBAbdNLmTxwvOeAhgp0Jco5O2njSbK9bUVgIgfgBayuO9lMthk3ru%2BGkRWliDy3ZF7TTQ%2FU9Vfl4OG9oq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDIUR4HrwfWtT9LSnRircA7Zd0ELELZM8n5SFDMJ9Eq51X3z0%2FHwBx3AyLeeI4C4R5DaDSV8zBNhJ9euWedi%2FRkqPer91fve1eGLux1W3T0mYY%2B1sP%2FBuuQf781HY9rg%2FzLbN%2BRReGxFzMOzXaancCh4jJB63NemWMgGDkDAT7tQbK07y2Lb1J%2FTUmiCoI158%2BxbMj7fZ2HO5DQQHwS7ifNQ63Ugyds5un75zl1utQ%2F1x8FQqTdSfpU%2FluNQUTfEIb5xsvp6IQTQNO16%2FYJsOgBuITeDoXChFPAATkpdUKmPqTfla3khWXcZ6x%2FyjFXU75j2dRHtcwtCQjJH6plDbLK9iurNrlFFmQLzrgtkvsyyO6%2Bc4e%2FJru3JiHu%2BSH9WXg9Saj4hY7gy%2FdCQFZpQe2yyvyjOLsv80ukfzFYv83l4Jj2KACV%2F8CO2%2Fwz%2FXGOWQU73P59gEslGK05y1%2F97jc5Zlv7dp2o3i4Z75VU%2B99qj%2BjKcgfrvb73SBHZTAxOc1ggpIpsSW%2F%2FqTT8agyr8gBmTdiJOxdlBlsjJD0qp1yLko%2BcUcWEhTJ7XcgewzJDHA6HRNFDingHGRJccYd%2B3wVdT6RcFO1DCqogq9512PQLIjgb21s%2BiFMGYM6wO3ocN16OHCX6bb06MJlnYEMI%2Fx2cwGOqUBW6ckzHh%2Flg1aox2hL78C9NFjfbskV6HzCBill7CNkmowahryGjFOlUhTk1rBBKdkNHburYaP0jcaN7302U35azGmqxv609P4e0qew4J8CQuCbWhtcYOEOufursBTdFeVP9yhVUq5jj%2FLAlXb0kSRipGWdLKgnZXj5QK9m87Fd6FBjzXBSh93E7GUKcKHsJ4rczEYO0UJCtMcEcgWnEJfZFu8jzev&X-Amz-Signature=98e845f618cd4686a3bb5df49bb69d5d5d3e35c7a1ff620c5e836221f0021b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
- $T_{\Phi}$: Effective TON supply for seigniorage
  - The staked amount and the L2 amount mainly affects to the seigniorage distribution
  - $T_{\Phi} = S+T_{L2}$
- $\Phi_{L1}$: seigniorage for L1 staking Users
  - $\Phi_{L1} = W_S \cdot \frac{S}{T_\Phi}\Phi$ where $W_S \leq 1$
- $\Phi_{L2}$: seigniorage for L2 seqeuncers based on the TON amounts in L2
  - $\Phi_{L2} = W_{L2} \cdot \frac{T_{L2}}{T_\Phi} \Phi$ where $W_{L2} \leq 1$
- $\Phi_{DAO}$: seigniorage for Tokamak Network DAO
  - $\Phi_{DAO} = \Phi - \Phi_{L1} - \Phi_{L2} = \frac{T_\Phi-W_S \cdot S - W_{L2} \cdot T_{L2}}{T_\Phi} \cdot \Phi \geq 0$ 

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