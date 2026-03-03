## Seigniorage distribution

<u>**Do we have to force the sequencer collateral to be proportional to L2 growth?**</u>

(e.g.) The sequencer collateral worth 1 ETH may be too small for L2 whose TVL is 100,000 ETH) 

- We may impose the lower limit on the sequencer collateral as a proportion of L2 TVL.
- For example, if the minimum sequencer collateral is 1% of L2 TVL, a sequencer must lock the minimum 1,000 ETH as collateral in the case of TVL being 100,000 ETH.
- The hypothetical formula can be as follows:
**Minimum sequencer collateral = **max(10 ETH, 1% of L2 TVL)  
- It means we should constantly keep track of L2 TVL. (from contract point of view, infeasible)
- focus on flat amount of sequencer collateral modeling or term-based sequencer? or fixed into ETH?
- Optimism sequencer bond: should be high enough to discourage rug pull
- collateral: ETH or ETH+TON
- For now, most L2 rely on sequencers only.
- <u>goal: decide the proper amount of minimum collateral depending on quality of comprising assets</u>
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c9b4881d-e8f1-446c-8240-0eefff432ae8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XFLVS6A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG7ow6gZblavbft7x%2BeL3P64Vjm%2F63hRwygeXxqIumggIhAKFSyDZWtkPtDPdZSvE57qiEP5LPiv3Bida9FJj3X0aKKv8DCHoQABoMNjM3NDIzMTgzODA1IgzzBXZWc1IshU2Ilx8q3APNI0Thi%2BDRsm9zI%2FVWRePDB6I5uxHcABMdlrrzED3Rhg8uqmorztwLCH4bZNV1kwbMIo81DkAZjkIE7U%2F9LLslS7zJLEFu9T%2FEv9EzdZYnAU2KiUltjQAhaHCl%2BOffEP%2B32LukRuxS32IgfC%2Fe6xJ7%2FUsGCUtr7BYaXlwvo9Du7AiG6%2BpRwaBY7%2FvHBphsemcqKR18dZ7UiiCqf%2FLgiG9UPgTpK3OHhPN4TqAk4jK7GRQ%2BAMwKzz6v0PDz%2BZ5aNGJT7eRixwp6M9tYjuot30h1B1jcZ5%2FvdlSiPJHFX8UMbdejzEbpL6TybIJr2f7QT7r%2FrIlj5QOKrXd28C8kuhIAxJpXPOvsU2NUiZ8Rpte6pDY35Kv3zDl%2BkxSE42sNj4T3prFqGforpSQtBREAQwmFYaxdHPKhw6sqqagq8BcpCeqka8Koek0tPhmZAGoHJ7aNEgJkDRoDhy1DbqBHD1YQIj0h8p96wUDXQ%2FEkxwleBHeih7DWs9smnd%2BXfdIgu5ry4WYU%2BhY6EIHsw6Xv%2Bfl0AA1sre9kffqwHMnFjpgCKNSAtjeSg96%2F6rZFhGJ4ozxjWdzD6LIU8DGrZ%2Ftef9RmFIr%2BCg9VGkKO8YxFAwL6OR55hdx7JCC7LjRt4jCqmNvMBjqkAanHKamuq6qlK1IdUI9uoUHGRGNitCVXS0VGBwXBToVs8EB950xcaU%2FyVFpJSgdO9jU6QgvqbsYc50zTsFJ0Q1nK4qBaIZCRLzSgEWKLxNswPBVLWfTiTU%2B%2FzAAeOtjw9ZVvTn6LNhI%2B1XQfV05jDjfEMEJ1mUyNAl1XzvssuQgNhhDc7wUOUlno6OVepKqZmNJxcQUTNs6GVn00%2BtkOLDDw8jgU&X-Amz-Signature=45cf0771e39524f69690bb2108d8ce2aa4ad68369dc8e5329e9b47141943d911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/66c1e8b4-4267-470a-886f-672ceed3bccb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XFLVS6A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG7ow6gZblavbft7x%2BeL3P64Vjm%2F63hRwygeXxqIumggIhAKFSyDZWtkPtDPdZSvE57qiEP5LPiv3Bida9FJj3X0aKKv8DCHoQABoMNjM3NDIzMTgzODA1IgzzBXZWc1IshU2Ilx8q3APNI0Thi%2BDRsm9zI%2FVWRePDB6I5uxHcABMdlrrzED3Rhg8uqmorztwLCH4bZNV1kwbMIo81DkAZjkIE7U%2F9LLslS7zJLEFu9T%2FEv9EzdZYnAU2KiUltjQAhaHCl%2BOffEP%2B32LukRuxS32IgfC%2Fe6xJ7%2FUsGCUtr7BYaXlwvo9Du7AiG6%2BpRwaBY7%2FvHBphsemcqKR18dZ7UiiCqf%2FLgiG9UPgTpK3OHhPN4TqAk4jK7GRQ%2BAMwKzz6v0PDz%2BZ5aNGJT7eRixwp6M9tYjuot30h1B1jcZ5%2FvdlSiPJHFX8UMbdejzEbpL6TybIJr2f7QT7r%2FrIlj5QOKrXd28C8kuhIAxJpXPOvsU2NUiZ8Rpte6pDY35Kv3zDl%2BkxSE42sNj4T3prFqGforpSQtBREAQwmFYaxdHPKhw6sqqagq8BcpCeqka8Koek0tPhmZAGoHJ7aNEgJkDRoDhy1DbqBHD1YQIj0h8p96wUDXQ%2FEkxwleBHeih7DWs9smnd%2BXfdIgu5ry4WYU%2BhY6EIHsw6Xv%2Bfl0AA1sre9kffqwHMnFjpgCKNSAtjeSg96%2F6rZFhGJ4ozxjWdzD6LIU8DGrZ%2Ftef9RmFIr%2BCg9VGkKO8YxFAwL6OR55hdx7JCC7LjRt4jCqmNvMBjqkAanHKamuq6qlK1IdUI9uoUHGRGNitCVXS0VGBwXBToVs8EB950xcaU%2FyVFpJSgdO9jU6QgvqbsYc50zTsFJ0Q1nK4qBaIZCRLzSgEWKLxNswPBVLWfTiTU%2B%2FzAAeOtjw9ZVvTn6LNhI%2B1XQfV05jDjfEMEJ1mUyNAl1XzvssuQgNhhDc7wUOUlno6OVepKqZmNJxcQUTNs6GVn00%2BtkOLDDw8jgU&X-Amz-Signature=ab4a65552d8b9716dd450a45aed47853478946f046ca8d995a38b5f41ccb1d99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- centralized sequencer vs decentralized sequencer?

<u>**How can we implement the seigniorage distribution discussed in the economics paper?**</u>

- The seigniorage distribution formula for the unique L2 in the economics paper is as follows:
**Sequencer:** (D+C)/T * Seig 
**Stakers:** (T-D-C)/ T * Seig
- We can achieve this, without touching the original contracts, by redistributing the seigniorage for TON DAO to sequencers.
- It does not seem preferable to take the seigniorage for sTOS holders.
- current staking contract does not seem to support Optimism…?
- may reuse the existing code and redeploy it ? ⇒ which features we want to roll out first?
(e.g. staking only or staking and staking-based FW)

<u>**How can we distribute TON seigniorage when multiple L2 exists?**</u>

- It is possible to generalize the formula for the unique L2.
- For instance, the seigniorage distribution formula for the unique L2 is as follows:
**Sequencer:** (D+C)/T * Seig 
**Stakers:** (T-D-C)/ T * Seig 
- In the case of multiple L2 networks, we can modify the formula as follows:
**Sequencer i :** (D_i+C_i)/T *Seig
**Stakers:** (T-ΣD-ΣC)/T * Seig
- If we use the seigniorage for TON DAO, we can just distribute it proportionately

<u>**What if users deposit assets other than TON(e.g.) USDT, USDC)?**</u>

- Sequencer seigniorage is based on TON only. (incentivizes sequencers to attract more TON)
- Only TON seigniorage distribution can affect the quality of L2 TVL.
- 

<u>**Should we allow sequencers to use assets other than TON as collaterals?**</u>

## Verification economics

<u>**What is the appropriate minimum challenge costs?**</u>

- Which one is better: flat bond vs proportional bond
- How can stakers actually do validation? ⇒ delegation (⇒ may ask Zena)

<u>**What is the appropriate slashing rate?**</u>

<u>**What if valid FW requests do not get processed?**</u>

- We can model the FW fee function so that it can flexibly reflect supply and demand.

<u>**What if sequencer is down for prolonged period (e.g.) 1 day)? **</u>

- do we have to impose penalties? (e.g.) slashing mechanism) centralized sequencer
- punishments not just on attacks but laziness
- exit mechanism for users is needed (⇒ can ask Optimism team)

## Others

<u>**We may need to clarify what type of MEV we are thinking about.**</u>

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f217882c-64c3-46cc-8f45-efe53daccc2d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVYREFD7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMdSetv6voqvZx3y8F1%2FbQH%2BfZdYFUWLKPRp%2BXBJ3lEAiEAzf%2F%2BqCPKFckSvkIrD1H1owJcmS7M8FHY8mpYRm51pyEq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPR0IkZZembMv5IxNSrcA7Nbx7Wqi%2B8Q%2Bpn9cj%2BnywwPgZ%2FBi8J%2B7h7vcsOU8F4py4WIVusZ%2BcstpQ9hSDXl%2Fj9CJl9yAm9GW6TlNkVWyTujqMPoaHACIP0OoD11bLAxSgnumJ8XOiINWxnHaHg8nQ1RVPe4TVyYa1%2FmJCx%2F6sSzbemJCNx6x4FYtuYJ9UmlcHIHeJwI%2BuzSPRlf6HO%2B0TpHeNxpzkv7ps0Y8VM%2BgpK1IXavXh2%2FdOVmxF%2BtwJf0rzl4brLwfM0AMzyaSxoHPxSZaZ%2FDUMbklu2dJtRxxcBBEgNr4GLMVO6iZihiFNyIxJ9GjB%2F%2BLY2EYB7Z%2BzNmHNew26zMEDRghFSU6aAnM9%2Bwz7AIG1phgFtF%2FFXdIi5VKScKxh74lEirP1FQsW%2Fls8caDVUHgvQmsZuYahr43%2B0Z2h11fENOA4kQKYrYeBCLR7LRE2J1j%2Fikugv3SFM1GPdHoTTCS%2Fns%2FfIFdtUlJhKdn5x8pkGhdQ%2FtKoiH4nCaJzeISN9Xutx%2BVQNIR6rVsam0DO3ZPxrpqLoLzFJIUJ9piu1O36%2FKqM0pICOjHK9ZpXpcN43wF3Owqu81vPV5l0ROa8xThj%2B2v2nwULDfmWezaF%2FrDM7eZa7ohFxvBujNNVFZcwpuBW08PIDCMM%2Fv2swGOqUBgbJBfLmlDGLF%2BN%2F64PmopVxYeY39hkmyOpwiAGyWD3CtDNSdAYX0Xta3XOo0t5B8Io6y7%2BklYGItdRNvQE8boWafve%2B0zc%2B5i54AlcgI8sEt6W0ZiTYsMl0Dlie73iJenjDZHB%2BpBiZPtGqk%2Bl3EPrw39IWziagakqTULQh3OK0az678AHwV8dGPoIHCfBXhs2%2B5emsRsb%2FCj4WWMWsEnqruwaBN&X-Amz-Signature=d6379a639b1b2faf9f3d060b8a69b01f9e6167cf11cc5f5deb8baff03ba76e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)