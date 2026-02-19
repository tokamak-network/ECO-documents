# Logic Design

- The concept of slashing
  - If the Challenger wins the DisputeGame, the staked amount in the Operator's Layer2 will be confiscated.
  - Layer2 operators are subject to a rule that does not provide seigniorage unless they deposit more than 1000.1 TON in their Layer2.
- How
  - Confiscate the Operator's amount from the amount managed by Coinage 
- Slashing Check Logic
  - Regardless of game type, if the GameStatus status is CHALLENGER_WINS, the game is eligible for slashing. (GameStatus is shared across all games)
- Slashing Logic
  1. **Burn the Operator's amount by the BurnRatio.**
    - BurnRatio : The rate at which the Operator's coinage amount is burned
    - (A) : Amount staked by the operator (seigManager.stakedOf(layer2, operator))
    - (B) : Amount staked by the challenger (seigManager.stakedOf(layer2, challenger))
    - Amount burned : (A) * BurnRatio
      - The operator's staking amount is reduced by the amount burned.
    - RewardRatio : Reward ratio given to challengers
    - Reward Amount : (A) * BurnRatio * RewardRatio (New Mint[To implement transfer indirectly)
      - A portion of the amount burned by the Operator is given to the Challenger as compensation.
    - **verification**
      - Total staking amount of tot : - ((A)*BurnRatio) + ((A)*BurnRatio*RewardRatio)
      - tot.balanceOf(layer2) : - ((A)*BurnRatio) + ((A)*BurnRatio*RewardRatio)
      - Operator's staking amount : (A) - ((A)*BurnRatio)
      - Challenger's staking amount : (B) + ((A)*BurnRatio*RewardRatio)
      - Total staking amount in Layer2 : - ((A)*BurnRatio) + ((A)*BurnRatio*RewardRatio)
      - **What happens if it exceeds 1000 TON even after slashing with BurnRatio?**
      - After burning, it is impossible to update the Seigniorage.
  1. **Burn all of the Operator's amount. (이 방향)**
    - (A) : Amount staked by the operator (seigManager.stakedOf(layer2, operator))
    - (B) : Amount staked by the challenger (seigManager.stakedOf(layer2, challenger))
    - Amount burned : (A) 
    - RewardRatio : Reward ratio given to challengers
    - Reward Amount : (A) * RewardRatio (New Mint[To implement transfer indirectly])
      - A portion of the amount burned by the Operator is given to the Challenger as compensation.
    - **verification**
      - Total staking amount of tot : - (A) + ((A)*RewardRatio) =  -(A)(1-RewardRatio)
      - tot.balanceOf(layer2) : - (A) + ((A)*RewardRatio)
      - Operator's staking amount : 0
      - Challenger's staking amount : (B) + ((A)*RewardRatio)
      - Total staking amount in Layer2 : - (A) + ((A)*RewardRatio)
      - After burning, it is impossible to update the Seigniorage.

## Additional decisions to be made

1. 1번 로직과 2번로직 둘중 결정하기
Comment: In the 2nd way, the reward comes from the burned deposit. The burned deposit can’t be transferred. Isn’t it? 
1. Currently, candidates created with TRH-SDK do not have the ability to slash, so is it right to give seigniorage to those candidates? (challenge 기능이 없는 롤업에게 시뇨리지를 주는 것이 맞는 것인지에 대한 논의 필요)
Suhyeon’s Comment: Can you elaborate this case? I don’t understand what the case is.
Harvey’s Comment : 케빈과 의논 후 다시 이야기를 한다.
1. Will the slashing rate be changeable in the future, or will it be fixed to slash all of the Operator's Staked Amount?(추후에 Slashing되는 비율을 변경할 수 있도록 할 것인지? 아니면 고정으로 Operator의 모든금액을 Slashing할 것인지?)
Comment: I think all the amount should be slashed. I don’t find a reason to leave a part of it.
공통적으로 쓸 수 있는 파라미터를 할 수 있을 것 같다.(Layer2별로 파라미터 필요X) 
1. How to handle WTON in actual DepositManager after slashing in coinage? (coinage에서 슬래싱 후 실제 DepositManager에 있는 WTON은 어떻게 처리할 것인지?)
Comment: need to discuss
원래의 소각목표인 address(1)로 보낸다. (Need Kevin’s Comment)
1. ~~How much will be burned and how much will be given to the challenger? (얼만큼 소각하고 얼만큼 challenger에게 줄것인지?)~~
~~Comment: This ratio can be calculated later. Let’s go with a simple parameter first. For example, burn half and the other half as reward.~~
1. Should the burn rate be different depending on the L2 TVL? (L2 TVL에 따라서 소각 비율을 달리 할 것인지?)
Comment: I don’t think so. The parameter boundary for security differs relying on a L2 environment. But, there should be a commont boundary exists.

Need Kevin’s Comment
1. 챌린저가 승리를 해도 상위레벨에서 승자도 있고 하위레벨에서 승자도 있지만 최초로 rootClaim이 잘못됬다는 것을 발견하고 반박에 성공한 사람에게 Challenger보상을 지급해도 되는지? (모든 승자들에게 보상을 주는게 제일 좋아보입니다. 하지만 이건 가스비가 엄청나게 많이 들기 때문에 온체인에서 하기는 현실적으로 어렵습니다.)
Comment: need to discuss
Harvey’s Commnet : 현재 분기에서는 12월만 남아서 최초 발견자에게 보상 지급, 추후 26년 1분기에 Window 시스템 도입 테스트