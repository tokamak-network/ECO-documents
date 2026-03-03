# Current Implementation in Sepolia

## How to get voting power([code](https://github.com/tokamak-network/tokamak-sybil-resistance-mvp/blob/dd14c16a02d3b11d50b892d1974e43eecb40d2c1/contracts/src/CumulativeScore.sol#L107-L118))

- Reason for using `balanceOf`: by implementing it to match the ERC-20 `balanceOf` interface, we can use Snapshot’s built-in strategies as-is.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7194a193-a19f-4735-ac13-ca16d2b0aab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGOEXDWI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYCwW07GFrfhvaoARIDgdoOUTotrRGp6YmEcwOxeHoVwIgTPC5q%2FJ8n0EulbgFB%2FOpamz3eJ7sIz9hnMz5B4VkzzIq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDGtGF3lErVfvsBo3hircA10PyfW07KIzXo3eotOtTGw3TWppK5Oc0sAM%2BN7D6NJyE%2BLbEw6evCFtHZZh5y8XVXLAtldLORC4A2D3jITzYoT2gHYJRUR0hPmGZvQ7ZpqVnJgzHTtnzmw7BwRyzXjmH7mnHm8VdA9iUcliEOjV8BB1TYC3d1eqlOLOU3HRcl79tMTguco051mpiwR8rTG%2F0xdRzwnon1u5%2BKTIo%2BOwrYksNUtFqNdvmjQlhYAkpKhKv5KcIPYUSWrRHAEPyjmn9yyq9jdICFhDUfP5%2F97lZj3uhMVqe9fHt%2FecU2ebuToesu5q6ipA0QvPdksE45jIGyIaTkM1k%2FGbx5vK7SHtK9gBJJ0ofn0nfXn4i%2BmXR%2BOGPtGRzfgXzpM6rumbVYdZiJjz8GHWDuC5xZtBHyBon39CJUMncshgUIGYixM8hylzzTtldmTu3tJU71gcRSWirpfPKMWzlSEPaefQZL31FhspbHZxaxCEl4fxiUCbDgjurTf6%2F6F0vskt6%2BsBuv6tLJ%2FJ9S%2Ba%2F%2BqkxWH5BOS%2BY23ScaHIGaPiFDFmYjEhdY3k057MKiGQa2pMNPLg683u%2BQ0%2BKEAO%2FoCmxP00mZsvMtssfn7bI4IZYLAFuhzJwfyaY5jyAeW32o7E7yQCMLOY28wGOqUB%2BsTn%2Fft9PVZavS5vGZq%2F03ILi1oLT5be7pjgcK2pYfqVloGGL5r3LWVwVBa4odi261U1tLHMjDHn%2Fa1vIjSwtCy5bMYrqPFyl%2BAbnBWqwn9q0w97bld6nUE9684NUn1nZZlkjrIO3FVslfzclv0w8aAEjs%2Bkcp%2FLb2la1Q%2FaOfxA0QQRnwITgX60tm%2BAYWjxrFmRQmo1I52zcY2dqc%2F0YAW4loAg&X-Amz-Signature=ae0e6ac37528ec4022c7d034aebac60dd7bbb100888ed1b05a2e13ba1d6cc2b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- The current formula obtained via `balanceOf` is **Sybil score + ****`seigManager.stakeOf(account)`**.
- In other words, we sum the Sybil score and the user’s total staked amount.
  - Only a relatively small number of people will have a Sybil score, so granting voting power via `seigManager.stakeOf(account)` alone would not be very different from the current “sum” approach.
- Under this setup, using **SYB** may effectively be meaningless:
  - And if we use `stakeOf` as-is, voting outcomes are likely to be overly swayed by whales.

# Request and Question from ECO

## 1. Include staking in **SYB**’s scoring algorithm

- Proposal: grant **additional weighting** to SYB registrants.
- In the current SYB algorithm, staking increases the Sybil score **only for the operator**.
  - Example: when user **A** stakes to operator **B**, only **B** receives Sybil score.

## 2. **Attribution of points for Vouch/Staking**: can both **A (user)** and **B (operator)** receive points?

- **Vouch (A→B)**: it is correct that **only B**’s score increases; **A** does not increase.
- **Staking (A→B)**: **both sides can technically receive points**, but **A** can split their stake across many accounts (A1…A100), which creates a **Sybil-attack risk**.
→ Therefore, if this is allowed, **separate safeguards/mitigations are required**, and the discussion should assume that.

# Jamie’s opinion

Using QV in DAO:

Pros: A smaller group with strong preferences can overcome a larger but indifferent majority.

Cons: Requires sybil resistance mechanism.

Some thoughts:

Tokamak staking allows users to stake to operators. This can be used to get a sybil resistance measure for the operators but it doesn't really put and constraints on the user. To provide sybil resistance for users to we need some sort of vouching/staking on users too.

Answers to questions:

I think giving A uniqueness points just for staking to operator B is vulnerable to sybil attack. There should be some sort of vouch in the other way too. This could be a stake or it could just be a measure of activity on that L2.

Yes, Tokamak Staking can be used to calculate the operator score. But I think we need users to be able to get vouched in some way.

Answer question 1: Yes, if the DAO is using QV to get more voice from smaller holders, then it needs some Sybil-Resistance mechanism. Yes, I think that makes a lot of sense, and is better than just adding the points together.

Answer question 2: SYB points aren't just calculated based on the vouch from A to B, it looks at a neighborhood of the network around A and B to calculate the SYB points ( including data about other vouchers that have occurred). Yes the syb algorithm can protect against sybil attacks using a network of vouches/stakes.

# Jason’s conclusion

- If we want to use voting power with **QV** applied for **off-chain voting**, at this stage, it seems difficult for **SYB** to prevent **Sybil attacks** against QV.

# Considerations when applying Sybil to the Tokamak DAO

### Method 1: Applying Sybil to the Tokamak DAO based on the TON Staking deposit.

(1) a user deposits ETH into the main smart contract 

(2) vouches for any other Ethereum address in SYB

(3) Use the vouch point as a voting right in Tokamak DAO.

### Method 2: Applying Sybil to the Tokamak DAO without changing the currently developed Sybil.  

(1)  a user deposits ETH into the main smart contract 

(2) vouches for any other Ethereum address in SYB 

(3) The vouch point and ton staking amounts are used as Tokamak DAO voting rights.

### Currently applying  Method 2 >  3-1 above.

-  Question 1: Why are Sybil Points used for DAO voting rights? To prevent Sybil attacks?
Then, how about setting the weight to 1 if there are no Sybil Points, assigning the weight to Sybil Points if there are, and using the weight * TON staking amount as voting rights ( using the 3-2 method ) ?
-  Question 2: Couldn't malicious users exploit Sybil points to increase their voting power? Ordinary users wouldn't deposit Ether to generate Sybil points.  Can Sybil Points really defend against Sybil Attacks? 