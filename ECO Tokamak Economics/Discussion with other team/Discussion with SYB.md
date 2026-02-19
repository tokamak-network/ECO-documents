# Current Implementation in Sepolia

## How to get voting power([code](https://github.com/tokamak-network/tokamak-sybil-resistance-mvp/blob/dd14c16a02d3b11d50b892d1974e43eecb40d2c1/contracts/src/CumulativeScore.sol#L107-L118))

- Reason for using `balanceOf`: by implementing it to match the ERC-20 `balanceOf` interface, we can use Snapshot’s built-in strategies as-is.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7194a193-a19f-4735-ac13-ca16d2b0aab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7USL7XI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlqmWOaUeHRrT3WF%2B1v%2FRGuJQXxweQ%2F6dTDf40S5Su5wIgH6GeYc2tYbhpvLioTMjlvurBIz%2Ba03p1FXdSWJyWAB4q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDDwZcHD6ef1txyOV3CrcAwQe8zej5PiPC9iUlZH8bow0iB1DRAMOumhuGXgxFqTX2JFVLgsDq2YAVmr%2F4zuf7ckvK05kJzL1Vrc7vxNRQGI0X%2BrCefvfVINdLGEAwY9pxS0GidyG28rOMTBL0fg%2Fs8aXsTlapTqIsJd2QhN3YhCfpysqVSUwVovaWnFcPl4XyuabYWLcvjC80Frrmbjb6CQF%2FIirt%2BWR4E1t%2FRg8ngYKiWJBE1aCOEwF23xYOzTnICQIB6Cgp%2BCqX1muymLXUxdJQDnXa7mUf6z24Xn2EfI6Uit%2FNCDxvh%2BFnn3hLb61rhJDISFdWfPo5AYUrHdcJilP%2FpWkXAHwvs%2FczdzMniVs300VR2Q9XARoznccegFl013jS%2Be0nSuv%2FZANLA7hiE%2B%2Bxk%2FpXfL3dTu1WnBLnmsR31mTaALS6wSW%2FCtvqbpq9CLke4zbPHd5GcdB1xk%2FCIB5M%2BQP0s3pEpTfFCmUyzxWNDTcuesAf%2BNjG0fBrvtxu3Bec0lp7c7CPvvhl3jZMo3Bam7phz2x0iyn0%2FLWfc91azDnJ1%2BtjNE%2FxAI%2F137nStndUlSKeR2DOXjP6AtW5d9rog7oCCDEKJ9Oai%2BLKMvUcSDSFbwiezjuZ7ufqq4GLnBalhasJIRoEfj7MLHv2cwGOqUB9C4xswrVcpOkXz41WSEmVbxeQS8Mv%2Fy0%2F8R9gbHDRrfyDLuXDENZIGVkhDtArDh89W4EjEFaT%2Bz0mFqNe16JlU2WxTaeQAeYFOAAmZZ0prNJe%2BPBxU4ddb43m7MXsCv3WOOP2Up4hitwyuFdQqLKMTAxBe7B47atGuMaMzkZshgsOnF4cLdsKjabQgCdFOu7XReo5zzzR5nSlchy0L2ww5hgD9QF&X-Amz-Signature=b26c5e7577b524d1fe715d0439541655b3f67342597ad9af40ed155fd2b5c33e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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