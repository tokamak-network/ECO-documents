[[-]]

L2 Operator와 Validator의 deposit 수량은 withdraw 시 항상 불변이므로, mint된 veTON을 withdraw한 만큼 burn할 수 있습니다.

반면 User의 deposit 수량은 L2에서의 활동에 따라 변경될 수 있어 withdraw 시 수량이 달라질 수 있습니다. withdraw 시 veTON을 소각하지 않으면 infinite minting 공격에 취약해집니다.

Tradeable; burned when used for voting

[https://docs.google.com/presentation/d/1zr9x-QrRHMESa9T93aMCai5crx33yG7p3lI7KYN8aew/edit?usp=drive_link](https://docs.google.com/presentation/d/1zr9x-QrRHMESa9T93aMCai5crx33yG7p3lI7KYN8aew/edit?usp=drive_link)

[[Draft]]

[[feedback]]

1. vTON
  1. Who should receive vTON?
    1. ~~TON holders~~
    1. Bridged TON holders
    1. L2 operators who stake TON
    1. Validators who stake TON
  1. 

feedback:

1. ~~현재는 deposit을 하면 voting power가 L2 operator에게 자동으로 위임된다. 그러나 해당 L2의 utility만 사용하고 싶고 voting power까지 L2 operator에게 위임하고 싶지 않은 경우가 있을 수 있다.~~
1. L2에 staking을 하면 vTON을 주는 것으로 논의가 이루어지고 있다. 하지만 여기에는 다양한 한계들이 존재한다.
  1. Infinite Minting —> Streaming Granting
  1. vTON on L1 Based on L2 data
1. 이를 위해 CRV와 같이 VestingEscrow처럼 별도로 TON을 stake를 하고 vTON을 얻을 수 있도록 한다.
1. L2 운영자는 네트워크 운영으로 바쁘다. 만약 투표에 참여하지 않으면 손해를 볼 수 있다. 따라서 L2 운영자는 직접 TON을 스테이킹해 vTON을 확보하거나 vTON을 매수해야 한다.
1. 고래의 입장에서 직접 투표를 하고 싶을 수 있다. **자신의 Voting Power를 꼭 Operator를 통해서 행사해야 한다는 부분만 변경되면 될 것 같다.**
1. L2 Operator와 Validator에게 voting power를 강제로 부여하기보다는, 원하는 경우 스스로 Voting Power를 확보할 수 있도록 하는 것이 더 합리적이다.
1. Voting Layer를 별도로 둔다.
1. 이사회 — 내부 관계자가 아닌 외부인 또한 delegator가 될 수도 있으며, 즉 누구나 delegator로 나설 수 있다. 선거 활동하듯이 말이다. 그러면 자신의 vTON을 그들에게 준다.
  1. 정리하면 TON —> veTON —> veTON을 갖고 있으면 vTON이 생성된다. veTON을 delegate를 한다.
1. 챌린지 —> vTON이 사용된 10%만큼을 사용해서 챌린지를 걸 수 있다. Security Council
1. 시뇨리지만큼 vTON을 준다. 전송가능한 형태로? 투표를 하면 날아가고… 범용의…
  1. 시뇨리지를 받는 대상은 Operator와 Validator이다. 기존의 Staker는…?
1. 악의적 대응을 어떻게 할 것인가?
1. (개인에게 Voting Power를 주게 되면) 꼭 Penalty를 주지 않아도 된다.

Stake한 수량은 변경되지 않습니다. Unstake를 하면 동일한 수량을 받습니다.

Deposit한 수량은 변경될 수 있습니다. Withdraw를 하면 다른 수량을 받을 수 있습니다.

The staked amount does not change. When you unstake, you receive the same amount.

The deposited amount can change. When you withdraw, you may receive a different amount.

1. 현재 v1 모델에서는 어디에 deposit을 해도 상관이 없는 구조이다. 그래서 거버넌스를 operator에게 제공한다. 모두 동일한 구조이기 때문이다. V2 모델에서는 유틸리티가 다르기 때문에 
1. 현재는 기본형이 위임이다.
1. Utility를 이용하기 위해 L2에 들어갔는데 거버넌스 참여권을 주는 것이 맞을까?

vTON

- deposit 대신에 stake 즉, 묶여 있는 자산을 기준으로 한다. 일반 유저는 DAO에 참여하기 위해서는
1. 투표를 위해서는 별도의 vTON 토큰 발행이 필요하다. vTON은 L1에 배포된다.
1. vTON은 L2 Operator와 Validator뿐만 아니라 모든 참여자에게 지급하여 투표권을 부여한다.

현실 세계 vs. 블록체인 세계

Cybil Attack 가능성이 존재하지 않는다. Cybil Attack 가능성이 존재한다.

1인 1표, 기여 기반 투표 (새로운 실험)

의도적으로 Voting Power를 획득한다 vs. Voting Power를 부여받는다

1. $vTON$
1. vTON
  1. 모든 유저에게 action에 따라 vTON을 제공한다. 단, vTON 거래는 불가능하다. — 현실세계에서 모든 시민이 투표권을 기본으로 받는 것과 같다.
  1. TON을 담보로 맡기면 vTON을 받을 수 있다. 이 vTON은 거래가 가능하다. — 경제적 토큰을 담보로 제공하여 거버넌스에 참여하는 방식이다.

[[-]]

changelogs:

1. **vTON**
  1. vTON burns when used for voting and can be traded. Price fluctuations could cause governance paralysis or enable attacks.
    1. Price up: Governance becomes expensive, reducing participation. Users hold vTON instead of voting to preserve its value.
    1. Price down: Governance becomes vulnerable to attacks. An attacker could cheaply acquire large amounts of vTON from the market to control voting outcomes.
  1. **Vote Rewards:** Users who participate in voting (burning) are provided with DAO rewards (e.g., protocol fee distribution) equivalent to the value of the burned $vTON$ to compensate for the opportunity cost of burning.
  1. **Security Council**: The Security Council serves as the "last line of defense" when market dynamics ($vTON$ trading) threaten the survival of the ecosystem. Its core purpose is to respond to "plutocracy" or "malicious attacks" that may arise from the tradability of $vTON$.
  1. **Separation of utility and voting**: L2 users can deposit tokens to Layer 2 to use utility of Layer 2. L2 users can choose to lock their TON to 
1. **Governance participants**: [~~only L2 operators and validators~~](/2d9d96a400a3804eada9db5b07c5d797) → ~~TON holders~~ → Complete separation of utility usage and governance participation
  1. ~~vTON is not provided to all TON holders, but only to users who have performed ~~~~specific actions~~~~.~~
    1. ~~Bridged TON holders: ~~~~Deposit TON to L2.~~
    1. ~~L2 operators: ~~~~Deposit TON to become an L2 operator.~~
    1. ~~Validators: ~~~~Deposit TON to become a validator.~~
  1. 
1. **Method of providing vTON**
  1. **Immediate granting**: $vTON$ is granted at the moment of deposit.
    1. Infinite Minting: Users can mint $vTON$ infinitely by selling it on the market or voting on specific agendas, withdrawing their original $TON$, and depositing it again into a different account.
    1. To prevent Infinite Minting, a lock-up is imposed so that users cannot withdraw an amount of $TON$ unless they have an equivalent amount of $vTON$. However, this approach causes inconvenience to users.
  1. **Streaming granting**: vTON accumulates in the user's wallet in real-time as time passes.
    1.  $vTON = \int (\text{Action Value}) \times R \, dt$
    1. Since it is a time-based reward, $TON$ can be withdrawn immediately without any lockup based on the amount of $vTON$ when withdrawing $TON$.
    1. The deposit amounts of L2 operators and Validators are locked in the L1 contract. On the other hand, while L2 users' deposits are tied to L1, they can be freely used on L2. Therefore, the amount of vTON for L2 users must be calculated based on their current balance on L2. For this reason, vTON should be granted based on the current TON holdings on L2, not on Bridged TON.
1. **Delegating vTON**
  1. 

**L1 Governance**

**L2 Governance**

1. Quorum
1. Delegation
1. Voting power can be exercised in the form of Voting TON tokens.
1. Voting power is provided to TON Holders, not to L2 Operators and Validators.
  - TON Holders, **Bridged TON Holders**, Voting TON Holder, ~~L2 Operators,~~ ~~Validators~~
  - TON Holders에게만 주면 생태계 기여 없이 Voting Power를 갖게 된다. 반면 Bridged TON Holder는 L2를 사용함으로써 생태계에 기여한다고 볼 수 있다. 그렇다면 Bridged TON Holder에게 Voting TON을 주는 방식이 더 적절한 것은 아닐까?
  - Bridged TON Holders —> Voting TON
  - Governance Hijacking

Bridged TON Holder에게 Bridged TON 수량만큼 vTON을 주고 이것을 거래할 수 있게 하는 것도 하나의 아이디어입니다. 또 다른 아이디어로는 안건별로 vTON을 주는 것은 어떻게 생각하시나요?

- In the current model, voting power is generated proportional to the amount of TON deposited in L2, and this is automatically transferred to the L2 operator. However, L2 users may have deposited TON to use the service, not necessarily to delegate voting rights. Therefore, we separate L2 usage from voting power delegation, so that voting power does not automatically transfer to operators just because users utilize L2.
1. Voting Layer를 별도로 둔다.
1. Voting Power는 톤 홀더라면 누구나…
1. Agenda — for App Chain, for Tokamak Ecosystem
  1. Voting layer for Tokamak, for Layer 2
1. voting power: L2 operators, validators —> stakers
  1. utility vs. voting power

⎿  · vTON은 양도 가능한 토큰인가요, 아니면 비양도성(Soul-bound)인가요? →
양도 가능 (시장에서 자유롭게 거래 가능)
· TON → vTON 교환 비율은 어떻게 되나요? → 1:1 (1 TON deposit = 1
vTON)
· 누가 TON을 deposit하여 vTON을 받을 수 있나요? → 누구나 (스테이커가
아니어도 가능)

 · 소각된 TON은 어떻게 처리되나요? → 영구 소각 (총 공급량 감소)


- voting power vs. app utility
- Tokamak Agenda, App Agenda
- vTON?
- Voting Layer