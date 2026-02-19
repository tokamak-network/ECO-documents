# 논의1. 백서의 시퀀서 담보금과 시퀀서 스테이킹 

[Link](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1766540376341699)

- 제나 
  - 백서에서는 시퀀서의 역할 및 조건에 담보와 스테이킹 이라는 용어가 혼용되어 있습니다. 
    - 최소 담보 : Dsequencer = Hmax·Cmax + ∆sequencer
    - 시뇨리지 지급 자격조건 : T_i ≥ θ · B_i (**T_i : L1에 스테이킹한 양,** B_i  브릿지된 양 ) 
  - 질문1 : 아래 버나드님 답변에 의하면 담보 따로 스테이킹 따로 해야 한다고 말씀하신것인가요? **서비스에서 담보볼트와 스테이킹 볼트를 별도로 개발하고, 서비스 인터페이스가 담보 따로 스테이킹 따로 구현을 해야 하나요?  **
  - (버나드) 질문1에 대한 답변: 제가 백서의 용어 정리와 별개로 개발에 대한 지침을 따로 안드렸군요. 제 생각은 두 메커니즘이 결국 동일하고 볼트를 각각 개발할 경우 구현 난이도만 올라가므로 따로 구현할 필요는 없다고 봅니다.
  - **담보를 스테이킹한다. **→ 담보 볼트 , 잔액  지급자격조건,  **max( Hmax·Cmax + ∆sequencer, θ · B_i") **
    - 원래 의도는 담보와 스테이킹이 별개임. 
      - 담보 따로 : 필요성에 대해 논의하자. → 경제적 보안때문에 만들었음. 필수가 아닌것으로 완화었다. → 강제조치를 하기보다는 이러한 지표가 있으니 참고해도 된다. 이렇게 되었을때 잃는것은. 담보금이 없으면 경제적 보안이 취약할수있다. 잘못해도 손해보는 금액이 없다. 
        - 경제적 보안 취약해지는 이유 : 잘못을 해도 손해보는 부분이 없다. 
        - 슬래싱 : 담보금을 슬래싱?  스테이킹 금액을 슬래싱? 오퍼레이터가 슬래싱되면 스테이킹금액이 적으면, 잃는것이 적으니까 담보금을 추가로 걸었다. 백서에서 본드 ( 
          - 구현 : 최소 스테이킹 ( θ · B_i" ) 을 못맞추면 시뇨리지가 안생김. 담보금은 스테이킹과 같은 것이다. 
      - **일반 스테이커들이  바로 검증자가 될수있게. 기존 스테이킹 컨트랙을 활용하자.. → 유저 경험이 더 편하게… max(Hmax·Cmax + ∆sequencer, θ · B_i)   **
        - **Hmax·Cmax + ∆sequencer**
        - ** θ · B_i **
        - **슬래싱 (이건 경제적인 제약으로 봐야함.) **
          - 시뇨리지 지급안됨 
          - 스테이킹 금액이 모두 몰수됨 
          - **`시퀀서의 자격요건이 취소된다. → L2 블록을 못 올림 ? 누가 관리하나? ⇒ 이 내용은 백서에서 삭제하자. `**` `@Theo Lee 확인하시면 좋을것 같습니다. 
      - **시퀀서도 담보금 , 스테이킹 금액 모두 기존 톤스테이킹을 사용하게…**

- 버나드 
  - 화폐 발행 이익 자격 확보를 위한 스테이킹과 채권 분할 상환을 위한 보증금은 원래 같은 금고에 보관하도록 설계된 것이 아닙니다. 두 항목을 통합하는 방안을 논의하겠습니다. 
  - In Section 3.3.1, “the model distributes staking rewards in proportion to each L2's measured performance” → “**the model distributes rewards in proportion to each L2's measured performanc**e”
  - In the same section, “and TiT_i Ti as the amount of TON staked by the L2 sequencer on the L1 TON staking contract.” → “and** TiT_i Ti as the amount of TON staked by the L2 sequencer on the L1 contract.**”
  - 본 노션에 정리된 결과에 따라 백서 내용을 수정하였습니다.
    - **담보금 요건 통합**: fraud proof coverage와 seigniorage eligibility를 하나의 공식으로 통합

$D_{sequencer} = max(H_{max} · C_{max} + Δ_{sequencer}, θ · B_i)$

    - 슬래싱 처리 변경
      - 기존: 시퀀싱 중단 가능 → 시뇨리지 자격 중단
      - 시퀀싱 자격 취소 관련 내용은 삭제됨

 

# 논의2. 검증자 최소 담보금 계산 공식 

https://www.notion.so/tokamak/Implementation-Operational-Discussion-of-the-Validator-Minimum-Collateral-Calculation-2d8d96a400a380a794f2c18b218b51a0

[Link](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1766549466594079)

- 버나드 
  - Adding these two items to the whitepaper would address your concerns: **“validation is enforced at the time of registration”** and **“grace period is given when collateral falls below D_min.”**
However, since the current whitepaper does not contain specific requirements as such, I don’t expect the conflicts you’re concerned about.
I believe, if detailed requirements are documented separately in a yellowpaper, we can keep consistency and this should not cause issues later. I think we could add **a disclaimer to the whitepaper stating that “not everything will be implemented immediately and that implementation may proceed in phases through beta/soft-open stages (also, to address what Kevin mentioned)**“.
  - **등록시점에 등록조건을 충족해야 한다. **
  - **담보금이 최소 담보금 조건 밑으로 떨어지면 유예기간이 주어진다 .**
  - 면책조항(모든 기능이 즉시 구현되는 것은 아니며, 베타/소프트 오픈 단계를 거쳐 단계적으로 구현될 수 있습니다) 
- 케빈 
  -  That part is too much of trxtbook, no l2 will survive or not practical design for layer2 operating
  - It is not matter of disclaimer, matter of practicality of idea. Some parts need to be modified or eliminated, especially the "minimum collateral" policy.
  - 예전에도 비슷한 얘기를 했었는데, 이건 운영상에 심각한 차질을 빚을 수 있는 정책이니 신중하게 결정해야 되고,  초기에는 사실상 없는것과 같이 무력화된 수준 정도의 파라미터를 사용할거다라고 코멘트 했던 기억이 있어요. 그런데 구현 및 실제 운영상에 무력화된 파라미터를 사용할 수 없다면, 없는게 나아요.
- **결론은?**  **아래 내용인가요?? 케빈 요구사항에 맞는것인가요? **
  - **등록시점에 등록조건을 충족해야 한다. **
  - **담보금이 최소 담보금 조건 밑으로 떨어지면 유예기간이 주어진다 .**
- (버나드) 답변: 업데이트된 백서 최신버전에는 해당 요건들이 운용의 유연성을 위해 모두 필수가 아닌 상태로 완화되어 있습니다(사실상 대부분 무력화). grace period는 존재할 수 있지만, D_min이 요구되는 경우에만(기본적으로 요구되지 않을 수 있기에) 존재하도록 설정되어 있습니다. 표로 정리하면 다음과 같습니다:

| 위치 | 표현 |
| --- | --- |
| Economic Security for Sequencers | "may be introduced or adjusted according to operational needs" |
| Sequencer Deposits | "may require" |
| Sequencer Slashing | "may be introduced as follows" |
| Economic Security for Validators | "may be introduced or adjusted based on operational needs” |
| Validator Deposits | "may be required" |
| Validator Slashing | "In cases where slashing is introduced" |
| D_min | "If a minimum threshold is introduced" |

- **최소 담보금은 현재 없고, 나중에 적용될수있게 : 초기에는 최소담보금이 0이되게. → 도입 여부에 대한 플래그 추가. **