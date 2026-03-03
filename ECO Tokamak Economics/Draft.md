<u>*Special thanks to Kevin.J, Darren.K, Nomad.I, Jake.J, Suah.K, Praveen.S, and Jamie for the productive feedback on the posting.*</u>

## 0. Introduction

Layer 2 is a collective term for a specific set of Ethereum scaling solutions without severely sacrificing security and decentralization. While layer 2 executes heavy computations off-chain, it relies on layer 1 or Ethereum for security and decentralization.

Tokamak Network has been striving to establish an on-demand layer 2 protocol. More specifically, optimistic roll-up, adopted by platforms like Optimism or Boba Network, will be at the core of our service. Being ‘optimistic’ implies that we assume the validity of transactions unless there is a challenge. If transactions get ‘rolled-up,’ multiple transactions are collected into a batch and submitted to layer 1 at once. 

In the process, TON, the native token of Tokamak Network, must play a pivotal role in incentivizing users to act in an advantageous way for the protocol. In this context, diversifying the utilities of TON is crucial. 

Among possible utilities like governance or staking, we will exclusively discuss the way to maximize the utility of TON as a fee token in this paper.

## 1.  Trade-off around fee token utility

### **1.1. Why TON to be a fee token?**

 

If TON is a fee token, we can pay transaction fees in TON.

Why is it so important? No matter which applications or services people use on blockchains, making transactions is unavoidable. When you stake TON, it is a transaction. When you swap ETH for TON, it is a transaction as well. In other words, fee token utility guarantees the baseline demand for TON.

UX can be improved, too. Users do not necessarily have to hold many ETH just for transaction fees.

### **1.2. Fee token dilemma**

![**Example: fee token dilemma**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/9929ddda-f00b-4ee4-a782-73277852ccd6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.16.39.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XZ2GSAC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUjqjHpEIqpTM0q9oOYGwXDVnpfvG1WLSt7UV4hK9ZHAiAF7vUd4trRlFal%2B8dJ3kE3TBM9Z189PFaG1x6obkfW7Sr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMlfS00eULgDPDmqHZKtwDEmeCyORpEuKDu1zWEQDVRekz%2BtKzfbLfTf5B%2F3ZMcqcVEoMsCiH94DxtDH%2FebVUAbh5KwMm3hYx0JzLTAXHyp41Q6q4hRvFPrYPAUM%2BwgQS87s8qUlsQ06GdcXkat2RKt9KPtNJqHVlz0XVCn4Ajge9S0aRouxkwSRHLS9La0DkqBrHpRA4yyU0RYzGOVeWc%2FAY1G3uJmecMYpuHbMu96DRmAExocNJOuxIJEmzYCxzIrYlM3mHrc5v9FP6ISpzqfqbJ%2B5yHoWCNXNcnXEpPTW3oUxT1O42ebtnK8Kbk6cPDAkkJyrw%2B6iKYN%2BTJPAd12db9d38rEygtwy0n8tX8oW4%2FTZF3%2FS84UFBsAJf2GfDBoKXtICBbdLLjeiQxha%2BwOK35VPTLN3T0be5k6oAnEI8I0roEny%2ByPYq7wPPzQ7%2B6P2jZOjNFRKXN5RGMC%2Bz6BS1HQRNT8OxR1%2BWyqsW6lvpan7HpXg0Ge9RN1me6EpquYdk090VF%2BiIlw0kPG4jwxo%2FEp329yWhSMEWbf45Bn8cTN%2F%2FcWS6StECr9CgEEAyPfpFPMKKusH67HnD7Y46CF9%2F54UPeDINRQUFjRx2I0nUxIDpFb1dAqogabTFgwlQFoH4qEV8kpYVCMGUwk5nbzAY6pgH7J0EfFHMu4ol4OZs0UPwvc9Gp7%2FF50BkS51MCKBxXXIkbW8UPAwG0qiKXSiKWVYF3kLcvcM6OwBVr3bvBbYievtyOadtCTl1ZXj6ZOf9di%2BkxIL56pLeQn1vfYLK2pVJIpgqRHfUIIRJ%2Bdv%2FISf%2BP4RskobWebXlAhOyHvSBvOV7vjp7Yb0H4pvBxvcsFyI0LWxX63Kvsv1A%2F%2F6yuykDSeVbp%2BEel&X-Amz-Signature=4cd09ab5b105a90c65579ff5aad8367b97b646dcaed7aebb95b39592f4d2bb5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Unfortunately, an extremely tricky issue has prevented many layer 2 protocols from allowing their tokens to be fee tokens: potential downward pressures on the token price.

The picture above shows how the ‘fee token dilemma’ arises. Layer 1 describes the underlying blockchain architecture responsible for the security and decentralization of layer 2 networks. Sequencers are entities entitled to produce blocks in the layer 2 environment. 

Let’s look at the bright side first. When users make transactions, they purchase TON to pay transaction fees, boosting the price of TON.

However, you should also see the other side of the picture. Sequencers send the information on a bunch of layer 2 transactions to layer 1 for security. The problem is that the security fees incur, and sequencers must pay these fees in ETH. Consequently, despite taking transaction fees in TON, sequencers swap some TON for ETH to pay layer 1 fees. Of course, it would bring down the price of TON.

## 2. Similar protocols addressing fee token dilemma

### 2.1. Optimism

OP token, the native token of Optimism, is not for paying transaction fees within the network. Instead, it only performs governance functions. 

![**Optimism Collective (Source: Optimism)**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a8c3c2df-7c83-4710-85ed-6e141dcca5fa/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-02_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.42.40.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XZ2GSAC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUjqjHpEIqpTM0q9oOYGwXDVnpfvG1WLSt7UV4hK9ZHAiAF7vUd4trRlFal%2B8dJ3kE3TBM9Z189PFaG1x6obkfW7Sr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMlfS00eULgDPDmqHZKtwDEmeCyORpEuKDu1zWEQDVRekz%2BtKzfbLfTf5B%2F3ZMcqcVEoMsCiH94DxtDH%2FebVUAbh5KwMm3hYx0JzLTAXHyp41Q6q4hRvFPrYPAUM%2BwgQS87s8qUlsQ06GdcXkat2RKt9KPtNJqHVlz0XVCn4Ajge9S0aRouxkwSRHLS9La0DkqBrHpRA4yyU0RYzGOVeWc%2FAY1G3uJmecMYpuHbMu96DRmAExocNJOuxIJEmzYCxzIrYlM3mHrc5v9FP6ISpzqfqbJ%2B5yHoWCNXNcnXEpPTW3oUxT1O42ebtnK8Kbk6cPDAkkJyrw%2B6iKYN%2BTJPAd12db9d38rEygtwy0n8tX8oW4%2FTZF3%2FS84UFBsAJf2GfDBoKXtICBbdLLjeiQxha%2BwOK35VPTLN3T0be5k6oAnEI8I0roEny%2ByPYq7wPPzQ7%2B6P2jZOjNFRKXN5RGMC%2Bz6BS1HQRNT8OxR1%2BWyqsW6lvpan7HpXg0Ge9RN1me6EpquYdk090VF%2BiIlw0kPG4jwxo%2FEp329yWhSMEWbf45Bn8cTN%2F%2FcWS6StECr9CgEEAyPfpFPMKKusH67HnD7Y46CF9%2F54UPeDINRQUFjRx2I0nUxIDpFb1dAqogabTFgwlQFoH4qEV8kpYVCMGUwk5nbzAY6pgH7J0EfFHMu4ol4OZs0UPwvc9Gp7%2FF50BkS51MCKBxXXIkbW8UPAwG0qiKXSiKWVYF3kLcvcM6OwBVr3bvBbYievtyOadtCTl1ZXj6ZOf9di%2BkxIL56pLeQn1vfYLK2pVJIpgqRHfUIIRJ%2Bdv%2FISf%2BP4RskobWebXlAhOyHvSBvOV7vjp7Yb0H4pvBxvcsFyI0LWxX63Kvsv1A%2F%2F6yuykDSeVbp%2BEel&X-Amz-Signature=e889740a11c69476db63f02f353157945cf1457ab64a6f08fdde074eb33c1441&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For example, Optimism Collective, together with Optimism Foundation, is responsible for governance in Optimism. In Token House, one of the two pillars supporting Optimism Collective, OP token holders can submit, deliberate, and vote on governance proposals, including protocol upgrades or inflation adjustment.

### 2.2. Boba Network

Unlike Optimism, Boba Network has a dual-fee token system. Although ETH is a default fee token, users can also choose to pay transaction fees in the BOBA token. If using BOBA as a fee token, users get a 25% discount.

However, Boba Network does not directly tackle the fee token dilemma. If necessary, BOBA gets swapped for ETH to cover layer 1 fees.

Instead, it tries to indirectly assuage the dilemma by combining governance with staking. If users want to participate in the decision-making process of Boba Network, they should stake BOBA. Additionally, a portion of transaction fees accrues to staked BOBA.

In other words, Boba network utilizes incentives so that more BOBA remains within the protocol.

## 3. Tokamak Network: proactive approach

Tokamak Network wants TON to be a fee token. Plus, we directly deal with the fee token dilemma by using two tools at our disposal: MEV or Maximal Extractable Value and TON seigniorage distribution.

### 3.1. MEV(Maximal Extractable Value)

The broader sense of MEV will remain intact in the long run. In addition, sequencers in each layer 2 protocol will manage to capture their share of MEV. It will help them cover layer 1 fees.

 

<u>**3.1.1. Broader definition of MEV**</u>

- **Conventional definition of MEV**
In technical terms, MEV refers to the maximum value extracted from block production in excess of the standard block reward and gas fees by including, excluding, and changing the order of transactions in a block.

DEX arbitrage is one of the most well-known MEV examples. Let’s say two exchanges put a different price tag on the same token. In this case, buying the token at a discount and immediately selling it at a premium generate profits.

Notably, MEV is not just for block producers or sequencers. Searchers, a group of users specialized in spotting MEV opportunities with advanced algorithms or bots, can also benefit from MEV. Of course, a part of profits for searchers goes to sequencers in the form of higher gas fees. Searchers should split the MEV benefits to include their transactions first in a block.
- **Redefinition of MEV**

<u>**3.1.2. MEV will not disappear**</u>

If MEV decreases significantly in the future, it cannot be a credible source of income for sequencers to deal with layer 1 fees. In this sense, the sustainability of MEV is essential.

With the steadily increasing trend, MEV is unlikely to disappear thanks to 1) centralized block production and 2) complexity in Ethereum.

- **Present**
- **Future**
![**Homogeneous system**](images/bb8d554948f4.png)

![**Heterogeneous system**](images/f1635e2e31bc.png)

If the block production gets centralized, a small number of sequencers, if not only, handle transactions. Unlike decentralized sequencers, since there is less competition and uncertainties in becoming a block producer, it would be much easier to pursue MEV.

Then, how does block production get centralized? It is closely related to the future layer 2 landscape proposed by Vitalik Buterin. The figure above illustrates the two possibilities discussed in his famous article ‘Endgame’: 1) a homogenous system where a small number of similar chains handle most of the Ethereum activities or 2) a heterogeneous system where multiple different chains cater to diverse needs. 

Interestingly, both scenarios can lead to the same conclusion: centralized block production. In the case of a homogeneous world, the larger computational capacity for higher TPS would render the block production centralized. As for a heterogeneous ecosystem, potential cross-domain MEV may make centralized block production more likely.

![**Defi TVL (Source: DefiLlama)**](images/8ec9bb86b74c.png)

The complicated nature of Ethereum can also feed MEV. For example, it is hard to reap profits from only sending or receiving tokens. However, it is a different story if you engage in diverse financial activities like trading spots or derivatives. Lucrative MEV transactions such as arbitrages or liquidations will frequently arise. Sequencers will benefit from either directly capitalizing on such opportunities or receiving higher gas fees from searchers.

What demonstrates the complexity of Ethereum well is Defi. In the graph above, despite taking a hit from the recent crypto crash, Defi TVL has grown about 500% since September 2020. If you lengthen the time horizon a bit more, the current size of the Defi ecosystem is approximately 120 times larger than that in September 2019. As long as the crypto industry grows continuously in the long run, the Defi ecosystem will also expand, offering more MEV chances.

<u>**3.1.3. Layer 2 protocols take their own share of MEV**</u>

From now on, we assume there exists only one sequencer in each layer 2 protocol based on the premise of centralized block production.

Even if MEV will not disappear as a whole, it does not guarantee a certain amount of MEV for individual layer 2 protocols. What if one or two dominant protocols take the whole pie? What if the competition among services is so fierce that the share for each platform is too small?

We believe each layer 2 protocol will retain MEV with monopoly power from the heterogeneous layer 2 environments. At the same time, the partial homogeneity all the layer 2 services share will put a cap on monopoly power and thus MEV they can extract.

![**Heterogeneous system with some homogeneity**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7bbd797e-07a9-4d8e-a570-12c5e2dc3919/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-27_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_12.52.34.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XZ2GSAC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUjqjHpEIqpTM0q9oOYGwXDVnpfvG1WLSt7UV4hK9ZHAiAF7vUd4trRlFal%2B8dJ3kE3TBM9Z189PFaG1x6obkfW7Sr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMlfS00eULgDPDmqHZKtwDEmeCyORpEuKDu1zWEQDVRekz%2BtKzfbLfTf5B%2F3ZMcqcVEoMsCiH94DxtDH%2FebVUAbh5KwMm3hYx0JzLTAXHyp41Q6q4hRvFPrYPAUM%2BwgQS87s8qUlsQ06GdcXkat2RKt9KPtNJqHVlz0XVCn4Ajge9S0aRouxkwSRHLS9La0DkqBrHpRA4yyU0RYzGOVeWc%2FAY1G3uJmecMYpuHbMu96DRmAExocNJOuxIJEmzYCxzIrYlM3mHrc5v9FP6ISpzqfqbJ%2B5yHoWCNXNcnXEpPTW3oUxT1O42ebtnK8Kbk6cPDAkkJyrw%2B6iKYN%2BTJPAd12db9d38rEygtwy0n8tX8oW4%2FTZF3%2FS84UFBsAJf2GfDBoKXtICBbdLLjeiQxha%2BwOK35VPTLN3T0be5k6oAnEI8I0roEny%2ByPYq7wPPzQ7%2B6P2jZOjNFRKXN5RGMC%2Bz6BS1HQRNT8OxR1%2BWyqsW6lvpan7HpXg0Ge9RN1me6EpquYdk090VF%2BiIlw0kPG4jwxo%2FEp329yWhSMEWbf45Bn8cTN%2F%2FcWS6StECr9CgEEAyPfpFPMKKusH67HnD7Y46CF9%2F54UPeDINRQUFjRx2I0nUxIDpFb1dAqogabTFgwlQFoH4qEV8kpYVCMGUwk5nbzAY6pgH7J0EfFHMu4ol4OZs0UPwvc9Gp7%2FF50BkS51MCKBxXXIkbW8UPAwG0qiKXSiKWVYF3kLcvcM6OwBVr3bvBbYievtyOadtCTl1ZXj6ZOf9di%2BkxIL56pLeQn1vfYLK2pVJIpgqRHfUIIRJ%2Bdv%2FISf%2BP4RskobWebXlAhOyHvSBvOV7vjp7Yb0H4pvBxvcsFyI0LWxX63Kvsv1A%2F%2F6yuykDSeVbp%2BEel&X-Amz-Signature=6fe0a6c059a55ad2c6a4e4c8749e7dbabc572e1eb9ffb9878ccf4729f9ef3e50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Tokamak Network expects a variety of layer 2 services to coexist, meeting diverse needs.  Regarding block production, it will get centralized due to cross-domain MEV.

Since each protocol caters to specific needs, such as trading NFT or hedging risks with derivatives, layer 2 platforms can exert monopoly power over users. 

We should also note that users rarely go to other networks once they get used to a specific platform.

However, at the same time, all layer 2 protocols share some similarities in that they focus on scalability and rely on native token incentives.

It implies that the monopoly power mentioned above is not limitless due to some competition among layer 2 services.

![**Example: How far a sequencer can go in terms of pursuing MEV**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3913c5d8-fea7-4532-9450-2965bf5745a0/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-05_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_12.41.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XZ2GSAC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUjqjHpEIqpTM0q9oOYGwXDVnpfvG1WLSt7UV4hK9ZHAiAF7vUd4trRlFal%2B8dJ3kE3TBM9Z189PFaG1x6obkfW7Sr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMlfS00eULgDPDmqHZKtwDEmeCyORpEuKDu1zWEQDVRekz%2BtKzfbLfTf5B%2F3ZMcqcVEoMsCiH94DxtDH%2FebVUAbh5KwMm3hYx0JzLTAXHyp41Q6q4hRvFPrYPAUM%2BwgQS87s8qUlsQ06GdcXkat2RKt9KPtNJqHVlz0XVCn4Ajge9S0aRouxkwSRHLS9La0DkqBrHpRA4yyU0RYzGOVeWc%2FAY1G3uJmecMYpuHbMu96DRmAExocNJOuxIJEmzYCxzIrYlM3mHrc5v9FP6ISpzqfqbJ%2B5yHoWCNXNcnXEpPTW3oUxT1O42ebtnK8Kbk6cPDAkkJyrw%2B6iKYN%2BTJPAd12db9d38rEygtwy0n8tX8oW4%2FTZF3%2FS84UFBsAJf2GfDBoKXtICBbdLLjeiQxha%2BwOK35VPTLN3T0be5k6oAnEI8I0roEny%2ByPYq7wPPzQ7%2B6P2jZOjNFRKXN5RGMC%2Bz6BS1HQRNT8OxR1%2BWyqsW6lvpan7HpXg0Ge9RN1me6EpquYdk090VF%2BiIlw0kPG4jwxo%2FEp329yWhSMEWbf45Bn8cTN%2F%2FcWS6StECr9CgEEAyPfpFPMKKusH67HnD7Y46CF9%2F54UPeDINRQUFjRx2I0nUxIDpFb1dAqogabTFgwlQFoH4qEV8kpYVCMGUwk5nbzAY6pgH7J0EfFHMu4ol4OZs0UPwvc9Gp7%2FF50BkS51MCKBxXXIkbW8UPAwG0qiKXSiKWVYF3kLcvcM6OwBVr3bvBbYievtyOadtCTl1ZXj6ZOf9di%2BkxIL56pLeQn1vfYLK2pVJIpgqRHfUIIRJ%2Bdv%2FISf%2BP4RskobWebXlAhOyHvSBvOV7vjp7Yb0H4pvBxvcsFyI0LWxX63Kvsv1A%2F%2F6yuykDSeVbp%2BEel&X-Amz-Signature=7883e7622b33fade5ad109f673ae9c0cecd5e97abb99c98d57d2addcf3b55214&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The limited monopoly power affects the aggressiveness of sequencers in pursuing MEV chances.

Based on the figure above, at first, MEV is zero because there are no users. As the popularity of the layer 2 protocols grows, more people come to networks, which leads to more MEV opportunities. Interestingly, MEV increases very fast until it reaches roll-up fees. It is because sequencers can actively pursue MEV transactions with monopoly power.

However, once MEV exceeds roll-up fees, the deceleration begins. Sequencers start to worry about whether MEV activity seriously erodes the common goods. Crossing the ‘red-line’ would mean users’ departure from protocols. The competition based on partial homogeneity works this time.

<u>**3.1.4. Numeric MEV modeling **</u>

We have reasoned that MEV will remain in place, and each layer 2 protocol will have a part of MEV. It is finally time to check whether the actual data supports our argument. 

While doing numeric modeling, we will refer to Boba Network for two reasons.

First, Boba Network is an appropriate example of a relatively small protocol in a heterogeneous system. According to L2Beat, its current market share is approximately 0.59% as of October 5th, KST.

Second, Boba Network is a good proxy for Tokamak Network. Both services utilize the optimistic roll-up technology. The size of networks, in terms of TVL, is quite similar, too.

- **Layer 1 fees (roll-up fees)**
- **Estimated MEV a sequencer earns**
According to Flashbots, as of October 5th, KST, the extracted MEV during the last 30 days is about 795K USD. Therefore, we can infer that MEV worth approximately 27K USD gets materialized daily.

However, it is more like the lower bound for the actual MEV due to the omission of certain types of transactions, including CEX-DEX arbitrages and sandwich transactions. Moreover, it is the extracted MEV on Ethereum, not layer 2 networks.

Therefore, adapting the original data for our modeling is crucial.

![**Cumulative Extracted MEV split by the type of transactions (Source: Flashbots)**](images/88f5a58832ba.png)

![**DEX to CEX Spot Trade Volume(%) (Source: The Block)**](images/385ed95b7127.png)

First, the extracted MEV in the Flashbots Dashboard mostly comes from arbitrages. Considering liquidations are generally not more profitable than arbitrages, it is safe to assume all the extracted MEV comes from arbitrages.

Plus, arbitrages in the Flashbots data are through swap transactions in DEX. Since swap transactions are equivalent to spot transactions, we can complement the extracted MEV by reflecting the spot transactions in CEX:

27K USD + 27K USD / 0.1134 = 265K USD

![**Ethereum TVL as of October 5th, KST (Source: DefiLlama)**](images/c095dfbeff08.png)

![**Uniswap TVL as of October 5th, KST (Source: DefiLlama)**](images/3a5d0843e82a.png)

![**Cumulative Sandwich Profits in Uniswap(USD) (Source: Dune)**](images/0dc264950efe.png)

Sandwich transactions cannot be ignored, too. Given the TVL difference, the cumulative sandwich profits in Ethereum are estimated as follows:

310,000 USD * 31.9 / 5.03 = 1.97M USD

Of course, since the number is in annualized terms, we can further update the extracted MEV as follows:

265K USD + 1.97M USD / 365 days = 270.4K USD

![**Extracted MEV Split by Role (Source: Flashbots)**](images/bc87b073ee00.png)

Unfortunately, MEV is not only for block producers or sequencers. Searchers can also capture MEV. If we only consider the share for miners or sequencers:

270.4K USD * 0.357 = 97K USD

![**Ethereum TVL as of October 5th, KST (Source: DefiLlama)**](images/d1631acc0613.png)

![**Layer 2 TVL (Source: L2Beat)**](images/ebc0c4d563c7.png)

Finally, we have to interpret this layer 1 number in the context of layer 2. Assuming MEV is generally proportional to the size of financial activities within networks, the following calculation holds:

97K USD * (4.71/31.9) = 14K USD
- **Conclusion**
![](images/4cf95af09f44.png)

Boba Network now expends daily roll-up fees worth 0.086 ~ 0.258 ETH or 115 ~ 346 USD.

The current market share of Boba Network is 0.59%. The estimated MEV a sequencer earns in Boba Network every day is 0.59% * 14K USD = 82.6 USD.

Therefore, Boba Network is expected to cover 24%~72% of layer 1 fees with MEV.

Considering the thin user base of Boba Network, the result of modeling is aligned with our argument. For example, according to ETHTPS.info, its TPS is 0.03, much inferior to Ethereum.

### 3.2. TON seigniorage

The distribution of TON seigniorage will be proportional to 1) the amount of TON deposited in layer 2 ecosystems and 2) the amount of TON locked for layer 2 security.

The first standard encourages sequencers to attract more users, consolidating the ground for generating more MEV opportunities.

The second standard incentivizes sequencers to utilize MEV to pay layer 1 fees instead of swapping TON from transaction fees for ETH.

<u>**3.2.1. Terminologies**</u>

- **TON seigniorage**
- **Deposit / lock or stake TON**

<u>**3.2.2. TON seigniorage distribution based on the amount of TON deposited**</u>

![**Example: TON seigniorage proportional to the amount of TON deposited**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b6f94b8b-b5a5-451f-b737-b4094ded877e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.20.49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=8fd0b6ef2832f1a34758fb83fc7ce0cb90acde889e5a9cadff0d024e718d6867&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

As discussed in the previous sections, MEV mitigates the fee token dilemma by allowing extra income for sequencers to handle layer 1 costs. Of course, more MEV chances will arise only if more users join networks.

TON seigniorage based on the amount of TON deposited can facilitate such a process. Sequencers will strive to lure users because more users deposit more TON, leading to a higher portion of TON seigniorage for sequencers.

<u>**3.2.3. TON seigniorage distribution based on the amount of TON locked**</u>

![**Example: TON seigniorage proportional to the amount of TON locked**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/94a035a5-3b41-4026-951b-eb6b5d0fd17a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-05_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.15.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=ede75735072b950b8f93a0b16f6beedc87244a3c29aea29de190b7f114db48cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

However, we have a problem. What if people sell deposited TON all at once within layer 2? It is technically possible because deposited TON is open to all transactions, including selling.

The issue is also crucial to our scheme. When sequencers take transaction fees in TON, they must decide whether to 1) use MEV profits or 2) swap TON for ETH to pay layer 1 fees. Of course, the former option contributes to tackling the fee token dilemma.

TON seigniorage distribution proportional to the amount of TON locked can guide sequencers as we want. TON from transaction fees will be locked for seigniorage. Of course, MEV revenue will cover layer 1 costs. If sequencers still stick to swapping TON for ETH, sacrificing the potential seigniorage revenue is inevitable.

<u>**3.2.4. Game-theoretic interpretation**</u>

We can illustrate how the behaviors of sequencers change with TON seigniorage distribution in a game-theoretic structure.

For this discussion, you first have to understand the payoff matrix. Payoff matrices show the benefits corresponding to specific actions by each entity. Notably, numbers in payoff matrices are in relative terms. For example, when the benefits of entity 1 and entity 2 are -2 and -1, respectively, absolute values of numbers do not matter. Instead, it just means that the loss of entity 1 is more than that of entity 2.

The payoff matrices below are not different. The first column and first row are the possible behaviors by sequencers 1 and 2, respectively. The payoff of two sequencers is denoted as (payoff of sequencer 1, payoff of sequencer 2).

![**Example: payoff matrix without TON seigniorage distribution**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/33ac545d-142d-4c48-84cc-8a9bcfc8823f/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-29_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_2.26.37.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=4fab3eca4e32674b9032e59a7a3727e75e32c4aee42ed9aa7dc8ac467eca95ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Without TON seigniorage distribution, the advantageous action for both sequencers is to swap TON for ETH, regardless of the decision by the counterpart. The reason is quite simple. You earn nothing for locking TON. Worse, if one sequencer locks TON and the other swaps TON for ETH, locked TON will suffer from declining prices due to selling pressures.

Therefore, both sequencers will sell TON from transaction fees to pay layer 1 fees and invest their assets, including MEV, in services offering higher returns.

![**Example: payoff matrix with TON seigniorage distribution**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/53cae9ac-5033-4efb-bc43-5e7f2c6286f9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-29_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_2.26.51.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=121d2396e941eeeff26d573e7060ea00e55d27c82798805a1a5c70025a47551d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

However, the whole narrative takes a 180-degree turn with TON seigniorage distribution. If you swap TON for ETH, it is the same as giving up rewards for locking TON. In other words, it will increase both the benefits of locking TON and the opportunity costs of swapping TON for ETH if we provide sufficient compensation for locked TON.

Consequently, with TON seigniorage distribution, both sequencers lock TON from transaction fees and cover layer 1 fees with their money, including MEV.

### 3.3. Tokamak Network: Freedom to choose

It is finally time to incorporate all the ideas discussed into the concrete model. Within the Tokamak Network, each layer 2 protocol can establish tailored transaction fee policies. In this section, we will propose several possible combinations of institutions sequencers can introduce.

**3**<u>**.3.1. Nascent protocols**</u>

- **TON seigniorage distribution**
![**Example: zero transaction fees**](images/1107942a1f48.png)

While competing with other dominant incumbents, it will be hard to attract users as nascent followers. Thus, we can introduce zero transaction fees in the early phase of the protocol. One step further, each transaction may be rewarded with a certain amount of TON.

As you can see, sequencers are likely to invest their money in the early stage of protocols. Therefore, the incentive mechanism is necessary to ensure that sequencers get credit for their performances. Here comes the TON seigniorage distribution proportional to the amount of TON deposited. As sequencers convince users of their merits, more TON will be deposited to make transactions, leading to more TON seigniorage for sequencers.

The TON seigniorage distribution proportional to the amount of TON locked can also work in that way. If sequencers lock a large amount of TON for seigniorage, they have big stakes to lose for their malicious behaviors. Users will interpret it as a sincere commitment to layer 2 security.
- **MEV**
Now that TON incentives laid the ground for MEV by bringing more people into platforms, we should delve into concrete ways to extract MEV.

![**Example: two-tier transaction fees**](images/2a9f097fe255.png)

For instance, we can implement the ‘paid service’ in processing transactions. In this case, the default transaction fees are zero. However, ‘paid users’ choose to pay fees and earn some benefits. Such benefits can be either prioritizing their transactions or sharing the MEV of a sequencer in the future. If possible, even paid users may be divided into multiple tiers.

Establishing exchanges is also on the table. Potential arbitrage opportunities will add to MEV. Additionally, sequencers can also expect commissions from trading activities.

**3**<u>**.3.2. Mature protocols**</u>

<!-- Unsupported block type: unsupported -->

- **TON seigniorage distribution**
![**Example: TON as a fee token**](images/226b7c86547d.png)

TON seigniorage performs a similar role in mature protocols: encourage sequencers to maintain loyal users and capture new users.

However, we must not miss one additional function: discourage sequencers from swapping TON for ETH. There is no way to force sequencers to use MEV to cover security fees. Despite making an adequate amount of MEV, they can still swap TON from transaction fees for ETH to pay layer 1 fees. TON seigniorage distribution based on the amount of TON locked raises the opportunity costs of such actions. If sequencers decide to sell TON from transaction fees, they give up potential benefits from TON seigniorage.
- **MEV**

## 4. Implications

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/aee79cb6-9bab-4ddf-8d4d-d89dc4adddab/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-05_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.13.27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=71c19311cdb8ee5f7e06ae1374eb157248b92a54427a2b1f7f36ce138f7c962f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

We can summarize the whole discussion with the diagram above.

In conclusion, implications of our model are as follows:

- **Improved UX**
Users can reduce their dependence on ETH to pay transaction fees because TON is also a fee token.
- **Centralized but censorship-resistant block production**

![**Centralized but censorship-resistant block production**](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/751b5bac-1225-4893-8e99-32e073930ff7/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.37.38.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRI5DLZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgODTUCvYkVQphuvCT9fZ88clELAh%2FlL4cW7YuYque4AiEA%2BvgRONvmB0et3oCg002YBGOLmZYFnGiFIKOMk74%2Bymoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBFuqaosYYqZ1YefnircA9bGgg%2BzcNfUX7aJE3Ba1e%2FJ7kj7jneWr8eDu9WrTYYsEVJVHvpxdz%2FkGNtyznqp3LlLZ4zI53XQbseBLUKOpyzO1da55B%2FI0xr06eiO9d%2FYBPmz02KseFJq9zPMxLSFyIK04t71%2BInItAkBbgzSBY%2F5nFeu7dahAXsOmeq17ZFG34xYnP97q%2B4XLO1bxPj6aecbz7GADTK0cCVJZj1ESsVV2c%2BJ8pa8cT9N0suPWHx6bR63mHCRNzzVmGJyYb3MGZWe9cH3SPUvJCq35dpF5yPibjuP60gxWdD%2B%2Fq8w0SHRZNa2d%2BslxNV1UHGAVrxAlke8Bb%2BXGAhpDdnNNVXNRy7DrfQGIcCtCN1e0g9eNCbQQ9sDwJs9Vh4m48vxI%2FlvxzqCJMTr60QyJG0vr8V70R4z5vJaLtbpxECINa6vWelsaRypkprgQRpT8ueUJZZDqblhJGUgA1tq9ae2E9oqkMPQ2UNjQiM4j4OIfBxRSlQ77Sy%2BzEsafJs9RKlpPzuk6C4AMBQfTcRL3zvaoq86gFRMh1pAKyTHJg7SXZVPX7qDPBHfpks5TQPKbkvlopxsQuiWlYK%2FE3OYF%2B20G4AhXcNZQAkCUNxVTzA3bin6w2%2Bv%2Bml%2F%2B%2F5ZHgYxrW6iMNyZ28wGOqUB8Or6LHhnSEvR5gr0HcaO7JtF%2FU6Mcgc%2FGQiByOJ0R1NLX8K0f6wCHstYcPpTBFKtPB%2BzAlSdCivNtZvzEOXIp0U9pkj87pnYC7CoiO8lp0jrKQAhk8%2BGGzbHm%2BDky4Zw3j8pDeSWW5phnN0cJK0RuEs6WTY5QSkk5PISXxwAX2V4YdkfTNgX95v9tNWlUX%2B6VNw%2Fs7KjKEgo%2B1ojmCrZAQeMFP1D&X-Amz-Signature=e23812b9489a6bc91bef72fe68abeee0b17e1e57da943e37c2da3dad08ae42a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Curtailed negative externalities of MEV**