Meeting Record : [https://drive.google.com/file/d/1GMtSgBhVyn-mrDK8btlGwLa1bP0eTWlR/view](https://drive.google.com/file/d/1GMtSgBhVyn-mrDK8btlGwLa1bP0eTWlR/view)

Gemini : [https://docs.google.com/document/d/1J2jFZiJp-oYDtbyo4FAX-FJhMpL1GItJ68D6skDR62Y/edit?tab=t.xv5of56sl22c](https://docs.google.com/document/d/1J2jFZiJp-oYDtbyo4FAX-FJhMpL1GItJ68D6skDR62Y/edit?tab=t.xv5of56sl22c)

rollupConfig

- Titan이면 [LegacySystemConfig](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/contracts/layer2/LegacySystemConfig.sol)
  - 이 경우 disputeGame을 진행하지 못함
    - 그럼 이 경우에는 잘못된 부분이 나오더라도 Slashing하지 못하는데 어떻게 진행해야하나?
  - **논의 필요**
    - Slashing을 할 수 없는 해당 후보자에게 시뇨리지를 주는 것이 맞는 것인지에 대한 논의 필요
      - Kevin과 회의 후 최종 결정
- Thanos이면 [SystemConfig ](https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol)
  - 이 경우 해당 System의 disputeGameFactory주소를 가져올 수 있음 ([https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol#L265-L268](https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol#L265-L268))
    - DisputeGameFactory를 통해서 생성된 DisputeGame주소를 받고 DisputeGame주소를 체크
    - DisputeGame주소를 이용하여서 해당 게임의 결과를 가져와 챌린져가 이긴 게임이면 Slashing 시킴
- Slashing을 하는 비중()은 어떤식으로 결정하게 되는가?
  - 누가 결정하는가? (ex : DAO에서 비율로 결정?)
    - DAO에서 Agenda를 통해서 결정 → Kevin의 결정이 Slashing비율을 변경하지 않는다로 되면 따로 결정하지 않고 Storage로 저장하지 않아도됨 (Kevin과 회의 후 최종 결정)
  - 어느곳 Contract에서 해당 Storage를 저장할 것인지?
- ~~Slashing을 한 금액을 다시 원복할 수 있는 방법이 필요한지?~~
- DepositManager에서 _accStaked, _accStakedLayer2, _accStakedAccount 이 값을 조정해야하는지?
  - requestWithdrawal을 할때 해당 Storage값을 뺴지 않아서 그렇게 유의미한 데이터가 아니라고 판단되는데 조정해야하면 조정을 진행하고 안해도되면 가스비도 아낄 수 있으니 다음 과정을 건너뛸려고 합니다.
- Slashing을 burn하는것이 목표인지 challenger에게 주는것이 목표인지?
- Slashing이란
  - Operator의 Layer2에 스테이킹된 금액을 몰수 시키는 것
    - 이 몰수 시킨 금액을 어떤식으로 처리할 것 인지?
    - Challenger에게 아니면 DAO에게? 아니면 address(1)로 보낼 것 인지?
- Slashing의 개념
  - Operator가 스테이킹한 금액 (A): seigManager.stakedOf(layer2, operator)  (coinage가 관리하는 금액)
  - 슬래싱 비율 :  ‘Operator가 스테이킹한 금액’ 전체 (?) → 확인필요
    - 결론 최소 스테이킹 금액보다 작아야한다. 
  - 로직 
    - 슬래싱을 한다!! 결정을 하는 로직 (**이 부분을 좀 더 정확하게 정리하기**)
      - 게임타입에 다른 로직  
      - 
    - 소각 (burn)
      - 소각의 비율 ( BurnRatio ) 
      - Burn: (A) * BurnRatio 양만큼 ⇒ 오퍼레이터의 스테이킹금액이 줄어든다. 스테이킹금액 소각 tot.burnFrom() 
      - 추가적으로 소각 비율만큼 WTON을 어떻게 할지를 결정해야한다
        - 이 부분은 burn하거나 이런식으로 진행하게 되면  
    - 챌린저에게 준다 
      - 비율 : 1-BurnRatio 
      - 준다? : 챌린저의 스테이킹 금액이 A*(1-BurnRatio) 만큼 늘어난다. 
    - ⇒ 로직: 오퍼레이터의 스테이킹금액 전체를 번하고, A*(1-BurnRatio) 금액을 챌린저에게 민트한다. 
    - 검증
      - tot 의 총 스테이킹 물량은 :  -((A) * BurnRatio)
      - tot.balanceOf(layer2) :  -((A) * BurnRatio) (시뇨리지를 발급하는 기준의 Balance) (**이 부분 확인해보기**) 
      - 오퍼레이터의 스테이킹 금액 : 0 
      - 챌린저의 스테이킹 금액: + A*(1-BurnRatio) 
      - 레이어2의 총 스테이킹 금액 : -((A) * BurnRatio)
      - 레이어2에 스테이킹하고 있는 다른 유저의 커밋시 예상 스테이킹 금액이 변경됨( 받을 시뇨리지가 늘어나게 된다. ) 
      - 

현재 Contract 구조인데 어떻게 업그레이드 시킬 것인지?

- SeigMangerProxy ([https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#code](https://etherscan.io/address/0x0b55a0f463b6defb81c6063973763951712d0e5f#code))
  - proxyImplementation[0] : [**SeigManagerV1_2**](https://etherscan.io/address/0xb1958719b3Af9B4d85D93EFC5e317C97cCe9aBc4#code)
  - proxyImplementation[1] : [**SeigManagerV1_3**](https://etherscan.io/address/0xce18C6F84F10881eA47A43AF7311A29bb116F628#code)
- DepositManagerProxy ([https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#readProxyContract](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#readProxyContract))
  - proxyImplementation[0] : [DepositManager](https://etherscan.io/address/0x76C01207959DF1242C2824B4445CdE48eb55D2f1#code)
  - proxyImplementation[1] : [DepositManager_setWithdrawalDelay](https://etherscan.io/address/0xAB9231f3081B5C3C27d34Ed4CEFc1280f89ff687#code)
  - proxyImplementation[2] : [DepositManagerV1_1](https://etherscan.io/address/0x74bC3031b9369e6b898e82784106257D4D37Eac5#code)
- Layer2MangerProxy ([https://etherscan.io/address/0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D#code](https://etherscan.io/address/0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D#code))
  - proxyImplementation[0] : [Layer2ManagerV1_1](https://etherscan.io/address/0x2EB7f500125f11544392B83B87cDEb9456f3509f#code)