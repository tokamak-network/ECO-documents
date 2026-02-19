# **Task #1. Upgrade L1 PowerTon **

 파워톤의 톤 금액이 new titan에서 분배될 수 있도록 파워톤 로직을 업그레이드한다. 

- **파워톤 distribute 함수 실행시 파워톤이 가지고 있는 톤을  L2 의 L2PowerTon 컨트랙으로 보내서 에어드랍을 할 수 있게 한다.  ** 
- L1의 Ton을 L2 **L2PowerTon **로 deposit하면 L2의 **L2PowerTon에는 **Native TON으로 예치된다. 
- develop contract
[[PowerTONUpgrade_V1_1]]

# **Task #2.  L2 PowerTon**

L2PowerTon 은 보유하고 있는 nativeTON 또는 erc20 을  **L2DividendPoolStos 컨트랙의 distribute 함수를 호출하면서 같이 전송하여,  **L2에서 에어드랍할 수 있도록 하는 컨트랙이다.   

- develop contract
[[L2PowerTon]]

- 참고 : L2DividendPoolStos 
  - 2cebd910-a6c1-43bf-b554-9c522823143e 
  - 8aa422d7-ac91-4d6f-980e-2540c118c1f2 