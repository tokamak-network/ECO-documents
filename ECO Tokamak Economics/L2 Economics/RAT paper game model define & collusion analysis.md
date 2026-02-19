Game model define (current paper)
  - non-cooperative (without coalition/ collusion)
  - normal-form (players choose strategy simultaneously)
  - Complete information - each player knows their type and the other player’s type (proposer or validator) and thus the utility function. Players choose the strategy (online or offline, honest or fraudulent) 

Collusion Analysis
Why need this?

the RAT paper's analysis focuses on a symmetric Nash Equilibrium (NE) among homogeneous validators in a non-cooperative game, which, while effective against individual "lazy validators," does not explicitly model the strategic incentives for a coordinated deviation by a sub-group

Taking the reverse approach to the thought process in the paper; instead of finding conditions so that ISE is NE, this analysis would analyze the consequences if players choose to play their best strategy with the presence of collusion. Then argue if such cases are possible with sufficient probability/ if it is possible in case the conditions for NE hold. Consider this a red-team perspective: will weakness of the RAT be successfully exploited by colluded actors?

The analysis on collusion can be built on the existing discussion in **6.3.1 -  Motivation to Exploit Weak Randomness. **In this case both Deliberately causing a trigger and Deliberately surppressing trigger could be strategies for **Malicious collusion between proposer and validator(s)**

Case 1:  Smoke-screen - Deliberately causing a trigger
    - Actions (collusion as a cooperative game with transferable utility)
      - At least there must be 02 colluded validators: V01 and V02
      - Assume allowance for selection bias & ability to manipulate selection
      - The fraudulent proposer trigger the test & target V01 - who is offline. V01 payoff = fv - cv - coff
      - The online & colluded V02 stamp the fraudulent state root as valid. V02 payoff = fv - cv + r*v
      - Fraudulent proposer payoff = fp +Rfraud (if other validators in the network fail to detect fraud, or if they are slower than V02)
      - Collective payoff = 2fv - 2cv - coff + r*v + fp+ Rfraud. The collective payoff could then be divided between 3 players due to transferable utility. 
        - This could be tempting if Rfraud is significantly larger than cv and coff - which very likely to be the case especially if we are arguing for low penalty (coff under $1000 as mentioned in the paper)
    - The argument should somehow prove that this kind of attack is impossible / possible with a very small success rate and thus the payoff for fraudulent proposer is -Cfraud in most cases. ⇒ key to solve the collusion of this kind is to maintain the integrity of the random selection function (which is easy in theory?)

Case 2:   Restore the verifier’s dilemma -  Deliberately suppressing a trigger
    - Actions
      - If validators choose to be offline, surppressing trigger would work in their benefit
      - Surppressing trigger also works in fraudulent proposer’s benefit
      - So the offline validators and the fraudulent proposer have incentive to collude & surppress the RAT
      - Only honest validators do the work ⇒ classic verifier’s dillemma again
    - We have an extensive section analyzing trigger-suppression. We can loop this into collusion analysis by saying that in case the condition for ISE to be pure strategy NE holds, even if proposer could successfully evade the RAT while submitting a fraudulent state-root, individual validators still have the incentive to choose online as the preferred strategy and break the collusion?

Case 3: Diligent Collusion referring to Proof of Diligence ([pdf](https://drops.dagstuhl.de/storage/00lipics/lipics-vol316-aft2024/LIPIcs.AFT.2024.5/LIPIcs.AFT.2024.5.pdf))

  - PoD provides analysis on two collusion scenarios: 
    - (1) lazy collusion 
    - (2) diligent collusion
      - In RAT, we need to refer (2) diligent collusion in which validators collude to provide an answer from single validator executing 
      - In this case, pure Nash equilibrium for the collusion does not exist as the leader who provides the solution can always cheat and take bounty.
      - It will work samely to RAT in my opinion. 
→ Even if a validator notices the solution doesn’t match to the state transition, the validator cannot distinguish whether it’s a wrong state transition or it’s a wrong solution.

Formalization of Case 3
A notable case of collusion is when validators remain attentive and diligent while at the same time form collusion to share the execution cost. In this scenario, an attentive validator will execute the validation and share the proof Lv and Rv to a coalition of k member in exchange for fee fc from each member. 

        - fc<cv, otherwise other validators will not have the incentive to buy the proof from the coalition leader

Other member of the coalition can choose to be lazy to save the operating cost cv while still having access to Lv and Rv, which they can submit if being targeted by RAT. 

Since all other coalition member has the incentive to be lazy and rely on the coalition leader to generate and distribute the proof, our analysis focus on the action chosen by the leader.

        - Leader choose to be attentive & not betray coalition
          - payoff for leader = fv - cv + fc(k-1) 
          - payoff for member = fv - fc
        - Leader choose to be lazy
          - payoff for leader
            - if  no AT = fv + fc(k-1)
            - if selected for AT = fv + fc(k-1) - coff
          - payoff for member
            - if no AT = fv - fc
            - if selected for AT = fv - fc - coff

The coalition leader will choose to be attentive if fv - cv + fc(k-1) > fv + fc(k-1) - coff, which implies that cv < coff

### Future plan:

- [x] Revising the game definition in the paper (Section 5. Game Model)
- [x] Adding the analysis on diligent collusion (Add a section before **6.3.1 **to discuss this)
- [x] Revising the motivation to weak randomness (Case 1, case 2 as extended analysis on section **6.3.1 **)