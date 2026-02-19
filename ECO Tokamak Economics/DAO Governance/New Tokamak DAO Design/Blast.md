L1 측

1. 사용자가 ETH를 Blast Bridge에 예치
1. Bridge 컨트랙트가 ETH를 Lido에 스테이킹 —> stETH 수령
1. stETH에서 발생하는 수익을 축적 (L1에서 계속 증가)

L2 측

1. 사용자는 L2에서 리베이스 ETH를 받음 (브릿지 완료)
1. 일반 ETH처럼 보이지만 내부적으로 리베이스 매커니즘이 적용된다.

L1 → L2 수익 전달

1. L1의 stETH 수익이 주기적으로 측정된다.
1. Blast Operator가 L2의 총 ETH 공급량을 업데이트한다.
1. L2의 모든 리베이스 ETH 잔액이 자동으로 증가한다. —> 노드 수준에서 address.balance를 업데이트한다.

L1 Side

1. User deposits ETH into Blast Bridge
1. Bridge contract stakes ETH into Lido → receives stETH
1. Accumulates yield generated from stETH (continuously increases on L1)

L2 Side

1. User receives rebasing ETH on L2 (bridge completed)
1. Looks like regular ETH but internally applies a rebasing mechanism.

L1 → L2 Yield Transfer

1. stETH yield on L1 is measured periodically.
1. Blast Operator updates the total ETH supply on L2.
1. All rebasing ETH balances on L2 automatically increase. → Updates address.balance at the node level

Stakers deposit into L2 to increase that L2's TVL. 동시에 L2의 유틸리티를 사용하기도 한다.

Stakers deposit into L2 to increase that L2's TVL. At the same time, they also utilize the L2's utilities.


Staker는 이를 위해 L1StandardBridge에 TON을 예치를 한다. 그리고 해당 staker가 얼만큼 예치했는지 기록한다.

For this purpose, stakers deposit TON into L1StandardBridge. The system then records how much each staker has deposited.

가스비

타노스에서 TON을 가스비로 사용할 수 있습니다. TON은 Native 코인 형태로 사용되나요, 아니면 ERC20 가스 토큰 형태로 사용되나요?

질문이 하나 있습니다.

I have a question.

TON can be used for gas fees in Thanos deployed by the TRH platform. Is it used as a native coin or as an ERC20 gas token?

1. Staker #1이 L1StandardBridge에 1000 TON 예치 —> 기록됨
1. L2에서 Staker #1이 TON을 다른 지갑으로 전송
1. Staker #1의 L2 잔액은 0이 됨
1. 하지만 L1StandardBridge 기록은 여전히 1000 TON
1. Staker #1은 계속 시뇨리지 + vTON 수령
1. Staker #1이 다른 지갑으로 TON 전송
1. 해당 지갑이 L1으로 withdraw
1. 다시 L1StandardBridge에 deposit
1. 같은 TON으로 두 번 시뇨리지 + vTON 수령
1. Staker #1 deposits 1000 TON into L1StandardBridge → recorded
1. On L2, Staker #1 transfers TON to another wallet
1. Staker #1's L2 balance becomes 0
1. However, the L1StandardBridge record still shows 1000 TON
1. Staker #1 continues to receive seigniorage + vTON
1. Staker #1 transfers TON to another wallet
1. That wallet withdraws to L1
1. Deposits again into L1StandardBridge
1. Receives seigniorage + vTON twice with the same TON
- 결국 문제의 핵심은 L1과 L2에 기록된 잔액 정보가 일치하지 않는다는 점이다.
- 따라서 L1StandardBridge의 기록이 아닌 L2의 실제 TON 잔액을 기준으로 시뇨리지와 vTON을 지급한다.
- Ultimately, the core issue is that the balance information recorded on L1 and L2 does not match.
- Therefore, seigniorage and vTON are distributed based on the actual TON balance on L2, not the records in L1StandardBridge.
- vTON은 DAO 투표에 사용되며, DAO는 L1에서 운영됩니다.
- L2에서 발행할 경우 L2→L1 브릿지가 필요하여 복잡성이 증가합니다.
- L1에서 발행하면 바로 사용할 수 있습니다.
- vTON is used for DAO voting, and the DAO operates on L1.
- If issued on L2, it would require an L2→L1 bridge, increasing complexity.
- If issued on L1, it can be used immediately.

시뇨리지는 L2에서 지급해도 문제없지만, vTON은 L2에서 발행되면 복잡해진다.

Seigniorage can be distributed on L2 without issues, but issuing vTON on L2 becomes complicated.

Seigniorage can be distributed on L2 without issues, but issuing vTON on L2 becomes complicated.

Stakers can earn both seigniorage and vTON, but issuing vTON on L2 becomes complicated.

1. L2에서 시뇨리지와 vTON을 분배하는 모델을 설계했다. L2 TON Balance 기준으로 시뇨리지를 분배하고, 시뇨리지를 받은 만큼 vTON도 함께 지급한다. —> 그런데 vTON은 L1 DAO 투표에 사용된다. L2에서 vTON을 발행하면 투표할 때마다 L1으로 브릿지해야 한다. 복잡성이 증가한다.
1. vTON은 L1에서 발행하는 것이 좋다. —> 그런데 L1에서 vTON을 발행하려면 "누가 얼마나 받을 자격이 있는지" L1에서 알아야 한다. 기존 방식인 L1 Bridge 기록 기준으로 하면, Staker가 L2에서 TON을 다른 지갑으로 transfer하고 그 지갑이 withdraw 후 다시 deposit하면 같은 TON으로 이중 수령이 가능하다.
1. 그래서 시뇨리지 + vTON을 받으려면 L2에서 TON을 Lock하도록 한다. Lock된 TON은 L2에서 transfer가 불가능하고, unlock하려면 반드시 L1으로 withdraw해야 한다. 이렇게 하면 L1에서 "누가 얼마나 Lock했는지" 정확히 추적할 수 있고, vTON을 L1에서 발행할 수 있다. —> 그런데 Lock한 사용자는 L2 utility를 사용하지 못하면서 시뇨리지 + vTON만 받는다. 아무런 기여 없이 보상만 받는 것이다.
1. 그래서 Lock한 TON은 L2 보안 담보 역할을 하게 한다. L2 Operator가 fraud를 저지르면 Lock한 Staker도 함께 일부 슬래싱된다. Lock한 Staker는 리스크를 감수하는 대가로 vTON을 받는 것이다. —> 결과적으로 Bridged TON과 Locked TON 두 가지 유형으로 구분된다. 두 유형 간의 시뇨리지 분배 비율은 DAO에서 결정한다.
1. 처음에는 L2에서 TON 잔액을 기준으로 시뇨리지와 vTON을 나눠주는 방식을 생각했다. 하지만 vTON은 L1에서 DAO 투표에 쓰인다. —> L2에서 vTON을 만들면 투표할 때마다 L1으로 옮겨야 해서 너무 복잡해진다.
1. 그래서 vTON은 L1에서 만드는 게 낫다. 그런데 L1에서 vTON을 만들려면 누가 얼마나 받아야 하는지 L1에서 알아야 한다. 기존 방식대로 L1 브릿지 기록을 보면 문제가 생긴다. 사용자가 L2에서 TON을 다른 지갑으로 보내고, 그 지갑이 L1으로 출금한 뒤 다시 예치하면 같은 TON으로 두 번 보상을 받을 수 있다.
1. 그래서 시뇨리지와 vTON을 받으려면 L2에서 TON을 잠궈야 한다. 잠긴 TON은 L2에서 다른 곳으로 보낼 수 없고, 잠금을 풀려면 반드시 L1으로 출금해야 한다. 이렇게 하면 L1에서 누가 얼마나 잠갔는지 정확히 알 수 있고, vTON을 L1에서 만들 수 있다. 그런데 이 방식은 문제가 있다. TON을 잠근 사용자는 L2 기능을 못 쓰면서 보상만 받는다. 아무것도 기여하지 않고 보상만 받는 셈이다.
1. 그래서 잠긴 TON이 L2 보안을 지키는 역할을 하게 만들었다. L2 운영자가 문제를 일으키면 TON을 잠근 사용자도 일부 손해를 본다(슬래싱). 잠근 사용자는 이런 위험을 감수하는 대신 vTON을 받는다. 결과적으로 브릿지된 TON과 잠긴 TON, 두 가지로 나뉜다. 두 종류 간의 시뇨리지 분배 비율은 DAO에서 정한다.
1. L2 TON 잔액 기준으로 시뇨리지와 vTON 지급 → 문제: vTON은 L1 DAO 투표에 사용되므로 L2→L1 브릿지가 필요해 복잡성 증가
1. vTON을 L1에서 발행 → L1 데이터를 기준으로 발행해야 함
1. TON을 lock하면 시뇨리지와 vTON 수령, L2에서 transfer 불가 → 문제: L2 유틸리티를 활용하지 않으면서 기여 없이 보상만 수령
1. Lock된 TON을 L2 보안 담보로 활용 → Operator가 fraud 시 함께 슬래싱됨. 이 리스크의 대가로 vTON 수령
1. Distribute seigniorage and vTON based on L2 TON balance → Problem: Since vTON is used for L1 DAO voting, an L2→L1 bridge is required, increasing complexity
1. Issue vTON on L1 → Must be issued based on L1 data
1. Locking TON receives seigniorage and vTON, transfer disabled on L2 → Problem: Receives rewards without contributing while not utilizing L2 utility
1. Utilize locked TON as L2 security collateral → Slashed together when Operator commits fraud. Receives vTON as compensation for this risk
- Locked TON은 L2에서 사용할 수 없으므로 Bridge 컨트랙트를 통해 deposit할 필요가 없다.
- 따라서 Lock 전용 L1 컨트랙트를 별도로 만들어 슬래싱 발생 시 개입할 수 있도록 한다.
- TVL 기준으로 시뇨리지를 분배하되, 일정 비율은 Locked TON 보유자에게 배분한다. 이 비율은 DAO 또는 자체적으로 결정한다.
- Locked TON cannot be used on L2, so there is no need to deposit it through the Bridge contract.
- Therefore, a separate L1 contract dedicated to locking is created to enable intervention when slashing occurs.
- Seigniorage is distributed based on TVL, but a certain percentage is allocated to Locked TON holders. This ratio is determined by the DAO or internally.