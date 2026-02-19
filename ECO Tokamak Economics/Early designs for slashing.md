Meeting Record : [https://drive.google.com/file/d/1Xi0MLwIswg09Eiq0toWVE2rb-8nUWAOm/view](https://drive.google.com/file/d/1Xi0MLwIswg09Eiq0toWVE2rb-8nUWAOm/view)

Gemini record : [https://docs.google.com/document/d/1irGWBrmCW3TH1fxtC7pc8VUoVa2_uC8yVMbuL4tUW3o/edit?tab=t.pd0df2g0ooxn](https://docs.google.com/document/d/1irGWBrmCW3TH1fxtC7pc8VUoVa2_uC8yVMbuL4tUW3o/edit?tab=t.pd0df2g0ooxn)

# EN Version

- In the current optimistic rollup designs,
  - There's a single winner "effectively"
    - It means there can be more than a single winner but the first winner takes all the reward so the other winners are not actually winners.
  - The single winner takes all the winning reward by slashing the loser's deposit (malicious block sequencer/proposer)
- This brings a security issue not fixable without strict fairness which is impossible in the most of blockchain
  - The malicious block proposer can be a Sybil challenger at the same time. Then, we can't guarantee
    - that an honest challenger wins the game
    - that the malicious actor will get financial damage
- So the slashing mechanism should include the below rules:
  - A part of the winning reward should be burned
  - Multiple effective winners should be allowed
    - To implement this, we should store challengers' challenge timining and the reward should be escrowed to distribute to effective winners after the first winner decision.

## Harvey’s opinion

- If we want to proceed with the slashing mechanism by December, it should be simple.
- Slashing should be done in the form of stealing the TON deposited by the sequencer in the event of an attack by someone, i.e. when the sequencer presents an incorrect stateRoot value.
- Burning the operator's collateral (how much to burn can be decided by the DAO?)

## Suhyeon’s opinion

- If the L2 deposit is greater than a certain amount, the sequencer must also stake a corresponding portion.
- Paying roll-up seigniorage separately to operators (sequencers) every quarter?
- If the challenger wins, some of the tokens will be burned → Operator's Tone Staking + Reward both
- Multi-winner → The operator can decide who will lose → The challengers save the time they spent on the challenge and distribute it to everyone who has a close time → This part is better to be developed later (time-wise).

## Conclusion

- If the challenger wins, some of the tokens will be burned → The operator's TON staking ratio will be burned → Burning will be done at the TON staking ratio, but currently it is 100% → It would be better to allow the DAO or someone else to adjust the ratio.
- It should be easy to tell when the challenger wins in DisputeGame.
- How can we easily understand the outcome of a DisputeGame and who won? This feature should be easily accessible.
- Starting from the fourth quarter of this year(2025), we will continue to upgrade the slashing mechanism.

# KR Version

- 승리 보상의 일부는 소각되어야 한다
- 여러 명의 유효 승자가 허용되어야 합니다.
- 이를 구현하려면 도전자의 도전 타이밍을 저장하고, 첫 번째 승자 결정 후 유효 승자에게 보상을 분배하기 위해 에스크로를 설정해야 합니다.

- 현재의 낙관적 롤업 설계에서는
"실질적으로" 단일 승자가 존재합니다.
즉, 승자가 여러 명일 수 있지만, 첫 번째 승자가 모든 보상을 가져가므로 다른 승자는 실제 승자가 아닙니다.
단일 승자는 패배자의 예치금을 삭감하여 모든 승리 보상을 가져갑니다(악의적인 블록 시퀀서/제안자).
이로 인해 대부분의 블록체인에서는 불가능한 엄격한 공정성 없이는 해결할 수 없는 보안 문제가 발생합니다.
악의적인 블록 제안자는 동시에 시빌 도전자일 수 있습니다. 따라서
정직한 도전자가 게임에서 승리한다는 보장이 없으며,
악의적인 행위자가 재정적 피해를 입는다는 보장도 없습니다.
따라서 슬래싱 메커니즘에는 다음 규칙이 포함되어야 합니다.
승리 보상의 일부는 소각되어야 합니다.
여러 명의 유효 승자가 허용되어야 합니다.
이를 구현하려면 도전자의 도전 타이밍을 저장하고, 첫 번째 승자 결정 후 유효 승자에게 보상을 분배하기 위해 에스크로를 설정해야 합니다.
이 글이 개념을 이해하는 데 도움이 되기를 바랍니다.

## Harvey’s 의견

- 12월까지 Slashing mechanism을 진행할려면 간단히 진행되야함
- Slashing은 누군가의 공격이 일어났을때 즉 시퀀서가 잘못된 stateRoot 값을 제시했을때 시퀀서에게 책임을 묻는 형태로 시퀀서의 Deposit한 TON을 탈취하는 형태가 되어야함
- 오퍼레이터의 담보금 소각 (얼마를 소각할지는 DAO에서 정할 수 있도록?)

## Suhyeon’s 의견

- L2의 Deposit이 얼마 이상이면 시퀀서도 그에 상응하는 비율을 Staking해야함
- 분기별로 운영자(시퀀서)에게 롤업 시뇨리지를 따로 지급?
- 챌린져가 이기게 되면 일부 소각 → 오퍼레이터의 톤 스테이킹 + Reward를 둘다 
- 멀티 위너 → 운영자가 누구에게 질지 정할 수 있음 → 챌린져들이 챌린지를 한 시간을 다 저장하고 가까운 시간에게 모두에게 분배 → 이 부분은 추후에 개발하는게 좋음 (시간상)

## 결론 정리 

- 챌린저가 이기게 되면 일부 소각 → 오퍼레이터의 톤 스테이킹 비율을 소각 → 톤 스테이킹 비율로 소각하는 데 현재는 100%로 소각 → 해당 비율은 DAO나 누군가 조정할 수 있게 하는게 좋음
- DisputeGame에서 챌린저가 이겼다는 것을 쉽게 알 수 있게 해야함
- 어떻게 하면 쉽게 DisputeGame 결과가 일어났는지? 어떻게 누가 이겼는지 쉽게 알아서 이 기능을 활용할 수 있도록 해야함
- 이번 25년 4분기를 시작해서 Slashing mechanism을 계속해서 업그레이드 시키는 방향으로 진행