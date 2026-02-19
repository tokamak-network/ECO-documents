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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c9b4881d-e8f1-446c-8240-0eefff432ae8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW2AC2W5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiwLPK1H%2FOmBtVlR0acwCczy%2BFYWc3BAJKkvMyiJ1sKgIgUZpwaRywcfKsxgZwR4bVPPm5jcaIG1rIKQ7vh7mrbWoq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDANK6KdujGzqxZjIUCrcA%2F0Bs5Om1pZh4TNtYjd62dsv%2Bhy%2FuojfnIjvF0Tg2hG4%2BpIsC6Cm4A88tvOQp6SadOt8j25VFbYYK6%2FzXHIh%2FONN%2BCcnDEtSkLRs87PsbsdcnFhlKGTSXBLI7Eo3lY53%2FOKLosliIFqTQUae7Qp%2FalQoi9z4%2B48CusN32qBqNKX1EUnp296K8wDdSmVAWt%2FvpOcENifU2c2k2DXZWT1AvR%2F9kNNupZwVbW7h6zrnVcMqUsCCoEsr2hIlq5no8nhD%2BJYD9xtk5SCcOMI5XzDIFom39uX412FXfKRYq%2FywGg32BZlaxdUQ2AjwZZ%2FpE1ZtyUTcCges9fXex1AwRrxCtlTNm7%2B0NsFXzCcsiKnEA%2Fq3kpXBT6UuxweB0qX0Sg22%2FoKguxNejvsKpDcpEzjU8HHfjERodjnseQXiDdBC0YoirPVMbqz7OAnyscalX5rMEPeKFhDXkZ0feBfqyTni39QsvBAM8RPBsM50QEC33I8edGQNTVLa0V3wulwmgPiFE20bRLpMeouJVlNc9hZyTvjwsXDDYRILarT7hpMNkgqAKzk%2BsW7ivlyM3BbgXPEaaXmbdyTii3FDfUSt8cTmIxZuLuZpXuyBDYqrI3mwyl78kR6Td5kfKutKCWk%2FMLzv2cwGOqUBJFw4smYuwzy8czGMQUccGw3nXlW6PlFVwK1Ot0gjKqRDSIMASXPw9iC1GFLzQN6nOmYBfc5jYIv7Wlq0MaAKvT55fLQeIKk5LXOKlj%2Bwp0oyiP8c06IsgoTjSkTFt8MjHujbinQr1T82iEx%2Bq5CYT26eUXl54FonHHThea4L6rCxHoQhPXAmmhGAQpvoeSko%2FlR39Kgr0hq%2BV4b44iblj3v6jItW&X-Amz-Signature=bd5904181e2a8337de5f0b0773f8a0e9f09e572dc83e7700ef5ce1be1ca52248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/66c1e8b4-4267-470a-886f-672ceed3bccb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW2AC2W5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiwLPK1H%2FOmBtVlR0acwCczy%2BFYWc3BAJKkvMyiJ1sKgIgUZpwaRywcfKsxgZwR4bVPPm5jcaIG1rIKQ7vh7mrbWoq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDANK6KdujGzqxZjIUCrcA%2F0Bs5Om1pZh4TNtYjd62dsv%2Bhy%2FuojfnIjvF0Tg2hG4%2BpIsC6Cm4A88tvOQp6SadOt8j25VFbYYK6%2FzXHIh%2FONN%2BCcnDEtSkLRs87PsbsdcnFhlKGTSXBLI7Eo3lY53%2FOKLosliIFqTQUae7Qp%2FalQoi9z4%2B48CusN32qBqNKX1EUnp296K8wDdSmVAWt%2FvpOcENifU2c2k2DXZWT1AvR%2F9kNNupZwVbW7h6zrnVcMqUsCCoEsr2hIlq5no8nhD%2BJYD9xtk5SCcOMI5XzDIFom39uX412FXfKRYq%2FywGg32BZlaxdUQ2AjwZZ%2FpE1ZtyUTcCges9fXex1AwRrxCtlTNm7%2B0NsFXzCcsiKnEA%2Fq3kpXBT6UuxweB0qX0Sg22%2FoKguxNejvsKpDcpEzjU8HHfjERodjnseQXiDdBC0YoirPVMbqz7OAnyscalX5rMEPeKFhDXkZ0feBfqyTni39QsvBAM8RPBsM50QEC33I8edGQNTVLa0V3wulwmgPiFE20bRLpMeouJVlNc9hZyTvjwsXDDYRILarT7hpMNkgqAKzk%2BsW7ivlyM3BbgXPEaaXmbdyTii3FDfUSt8cTmIxZuLuZpXuyBDYqrI3mwyl78kR6Td5kfKutKCWk%2FMLzv2cwGOqUBJFw4smYuwzy8czGMQUccGw3nXlW6PlFVwK1Ot0gjKqRDSIMASXPw9iC1GFLzQN6nOmYBfc5jYIv7Wlq0MaAKvT55fLQeIKk5LXOKlj%2Bwp0oyiP8c06IsgoTjSkTFt8MjHujbinQr1T82iEx%2Bq5CYT26eUXl54FonHHThea4L6rCxHoQhPXAmmhGAQpvoeSko%2FlR39Kgr0hq%2BV4b44iblj3v6jItW&X-Amz-Signature=ddbc9b5c010ed417f0b43d52978047abd6e5a0f51d4491b121020d4d821b3d06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f217882c-64c3-46cc-8f45-efe53daccc2d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7S6JONO%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T035915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAf2sjyOLW0jalrUL5tV%2BQyKU2LcjYJMWENQ3%2FW5v5%2FwAiBsmZrjp9kVt%2FFXdNE5qMAkyQnTTfcIMkoZTd2l2WSkwSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMY0HpQrnlhPzn65EWKtwDs7XWafEAsLST0%2Fys3fmsmMNIaKTo65h1Aq1ZEZfinH4SRuj%2BcUkQ1AR2J3l4xIqqy%2B9yNwVKz8TIk5%2B7%2F%2Ft%2BiuCjqE1%2FAXmgmB8R398dBTgWXJB5pr5GroE4cVXjnNbi3gvnJVoqQnh2oxoYffwoC4Ae%2Bj8KHrHM%2F8msrxPZwyy6C47lzWsk0T8rLI7Y7Ax%2BNvQvC4vnF7fWrxg2BpknjtXcxq8qWk52pbiEtCtsYpcRqWvTLylr2SgxKxZW%2BZ8DYrFIgKhpR3CQGnRWpPZOZFV%2BLMWErdid2U6cqAxonZPtTvHfzg2YAWn2nh3A8RRZoFO8HPdhvtqV8gFNT7P2L7EA1nFSjAAkj2VVAZsHBFTQ47h37RGa5Yb7izuQ7RfxaJe7cLJu0DoYFrRGUSGfMkrKjgL7QMMq9tyMNPYsjY8Ts%2Fy%2B6mYbM4YiJ%2FLwuiw1%2FjYaxgLuh1m4Nei2hANN0jd7yj6DEg%2FaTQp3PYf7sdXnDJNxzEOXBH%2BuEoSVNw90Kn6YcHjyVW6i0XAmB7e7pasLGh8dpnt1iC8B8hE67N%2FAVUvRv%2FXulQeHkZn1zomTgWAWvsTVHif7ZH0oc1VH9f%2BizxmV%2BZA6AQpgCet04m%2BHz5LWgxhW4e%2Fgv48wjfHZzAY6pgGcC%2B%2FzZHIyfuW%2BeQVVTvIOzFl5qNdDETeg3w824HxZmsvyGPQE2%2FU4tqefffOQkNaEkUhuDdjg2VcAf%2Fub4JDPIt4G4fh7ukfLp6TgfqjZuXe4nVcdMEXFLtm4VKDPgAlx2fxxD3y3BsbbNXG%2BJ%2FlrH2jAuV%2F5E0GgzkTcEZApDqOjMYt9WJsJFRKM2XdHtokDNxio3fjAFZOQNoQVxcoKQivkYs8R&X-Amz-Signature=9be98a557ceef13f0b35e6132393fbf3b1909c56b34738efc7bce38c1424d134&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)