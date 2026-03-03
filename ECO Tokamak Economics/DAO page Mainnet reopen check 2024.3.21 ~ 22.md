> [!note]
> 🛠 Test date: 2024.3.21 ~ 22
> - test page: [https://dao-tokamak-network.vercel.app/#/](https://dao-tokamak-network.vercel.app/#/)
> 
> check list:
> 
> - DAO main page
> - Election page 
> - Propose page (contract team, please focus here)
> - Committee page (contract team, please focus here) 
> 
> 
> Check call: 
> - 3.22 16:00 ~ 17:00 

- design: [https://zpl.io/257KYk3](https://zpl.io/257KYk3) (if you need access, please ask Lucas)
- QA team: please make sure that all of your feedback is reflected

**Feedback **

Harvey
- [x] Top 100 Stakers 화면에서 %가 낮은 경우 숫자가 잘보이지 않습니다.
- [ ] Summary의 Number of Stakers의 값이 정확하지 않은 것 같습니다.
- [x] Plasma EVM으로 만드는 경우가 존재하나요?
- [x] DAOVault Contract에서 claimTON, claimWTON기능을 막아서 더 이상 사용하지 못합니다.
- [x] DAOVault Contract에서 정책상 TON, WTON을 사용하지 말자고 하여서 정책이 변경되기 전까지 setTON, setWTON을 변경하지않아야합니다.
- [x] 이번에 DAOCommitteLogic을 업데이트하면서 over codesize가 되어서 로직을 2개로 나누었습니다. [로직사용, Owner세팅] 이렇게 되면서 현재 로직사용이 세팅되어있어서 사용불가한 function들이 있습니다. (이는 추후 Proxy구조 업그레이드를 통해서 로직을 2개다 사용할 수 있도록 해결할려고 합니다.)
현재 사용불가 function : setActivityRewardPerSecond, setCreateAgendaFees, setMinimumNoticePeriodSeconds, setMinimumVotingPeriodSeconds
- [x] 위와 같은 이유로 사용할수 없는 function들이 있습니다.
사용불가 function : setSeigManager, setCandidatesSeigManager, setCandidatesCommittee, setDaoVault, setLayer2Registry, setAgendaManager, setCandidateFactory, setTon 

Zena
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/94cbeef9-bed4-4483-b8db-8c46ca981dc2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.28.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PHSEAR6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICjogpU%2BNVP5W8aE8MUJNcQwtLNk0qfNcm6KAzdWSfvXAiA7rj4OE8gblHI6CXbWTIGujKh5FGxMFvZYN%2F7IXghr0Sr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM9PGtQQk99hTmGaODKtwDbbILbDaOqqOeHNzeeWeXM36uITXQlOdLzawRkwaafrV2nzpTB94VJ1ZbWh%2FXUglLmapi5T9x9B5z5015A6kH3L3hOF%2FrJEzvPB9C7rL%2FLXuLhJjpkDzX6M%2BFTTVldqk3vsi86Ta9dazhWwSh%2FNmAwwT%2B%2BjqV8Ru6XUSWn3pnzpWP1CHM2DC2BfK3S1pX66wJX9%2BLvMDXyG6DcuFTuNMZUTy56Bq55B4PTVLlGeCeg1bl02lq8XVm%2Bs6D8q10lDmU6QrUqN8cdG2%2FgoTx%2FwsFL%2FVHCGWqVx513jNsPT%2B1wSjbrHedeidFwA%2FJQSTSsiZeZ2s7nl7lMCEpth3nT%2Buzo7lLXDZpQssnIR%2BFB4t%2FgueCWKAwgUDznM5AH%2BQv5Fdsv5JHR3vFRkkh9ZdoeVBLHNxOs8XDeYnvKNKajaErIU51RZqGW%2Bz6NXtq8pFGCC2WzYxyAs0AqUgDrrJyzSjyO5SoUQVlSgTzVP7NAA54zW6q36eWekmfNH1MaB5JWq4jc9CbB9AdbSIKL3uBoCcb43ckMoIAsA%2BHAlc06%2BrsU5G9j%2Fp1NmRDekUUZa5VXQMnpCKovYYxOGzNT2TgM0blTdrFJV9WOWItxZms6TV0ohyCD4Dbuk4uWAiqQN4ws5jbzAY6pgGD8e0g5ZKiR6s6VWu0hdL6AJcM%2FPaxl4kdJj7c8PlgCaavR1rWNCywUB7aoH7UqZXpBTK0IoGHMk%2F5q88kezqeLblPApyG%2Fqpb97lG%2F%2F%2BJ9ciYEOMRw8OKUrxI7ISwhFwhUbzZxGI3lewwd73pWay56qGtE34jCfzM0%2BYdlT%2B02D2WtUzzF%2FoJeOMDwJ0zpr8AYPMAkEnZieC9UHO5Ovn0QoEq6WWn&X-Amz-Signature=7c95980f445b3f2fda9cf179831fd0319068afab800e754d29a4d62265f40b3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] 위에서 퍼센티지와 스테이킹 양은 보이는데, 주소가 안보여지는것은 의도한 것인가요? 
- [x]  update Reward 버튼을 클릭하면 0 개로 한참보이다가 한 몇 초 뒤에 계산 값이 나타납니다. 처음 0으로 보이는것이 오해가 될 수 있으므로, … 와 같이 계산중임을 인지할 수 있는 표시를 하는 것이 어떨가요? 
- [x] 하단에 토카막 네트웤 말고 온더와 관련된 링크드인 등이 있는데, 안 빼도 되는지 여쭤봅니다. 
- [ ] 우측 리소스에서 Candidate Registration 링크가 이제 없어질 doc 링크인것 같습니다. 오픈전에  링크 수정해야 할것 같습니다. 
- [x] candidate 상세보기 화면의 우측 상단 페이지 네비게이션에서 제일 첫번째것은 < Previous 버튼이 활성화되면 안되고, 가장 마지막 candidate것은 Next > 버튼이 활성화 되면 안됩니다. 
- [x] candidate 상세보기 화면에서 Description 항목에 설명이 있는 candidate는 하나도 없는것 같습니다. description 항목은 삭제하는 것이 나은것 같습니다. 
- [x] 타이틀이 Committee Stats 인데, 내용으로는 Agenda Stats 인것 같습니다. 
- [x] 아젠다 상세보기에서 제일 오래된것은 Next> 버튼이 가장 최근것은 <Previous버튼이 활성화되면 안됩니다. 

Eugene
- [x] simple staking page: 아래 그림에서 1, 980 TON / 1,010 WTON 에서,  / 을 사용하니까 분자/분모처럼 느껴지더라구요. 
1, 980 TON & 1,010 WTON 처럼 &을 사용하여 표현하면 어떨까 생각해봅니다.
- [x] simple staking page: Warning의 의미는 이자(시뇨리지)를 받기전에 unstake를 하면 이자를 받을 수 없다는 문구인 것 같습니다. 다만 표현이 명확하지 않아서 좀 헛깔립니다. 문구변경을 하면 좋을 것 같아요.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1c3752ab-652f-4355-8e99-15aa5a170ea7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7XMQCYK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrOlS1jo6ZqX1KVpdQrxrdQmkAgfJz%2BPRurttcn6O82AiEAplLu%2BPxIQ56MinXjj%2BsiU4Fs4%2FrlqUYPNa0Mrh%2FyzIUq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLayJS6sk1Kee%2BOJHircA5iUc44nWKktnpaeHS4soYV%2BaLYtEnRRZLaDi8g%2BYvhZ6kiXMCVcnukdGG%2FrnjQjl4Wo1myp67XsMY5YYI6Ab%2FdMuvQcEgyh%2F7n8xY%2FCqYx8cedJNV8HIl0UMsiSIc3hZGHQbn7q82QGwMwb8GFpLNmntcifIFcYlnSBTO03UtOz2W%2BI6vm10T4KxEiW0xpKltPm3TzY3QqHORBt2%2BdoJajle6c3GxW76GHoD1htNPokMPD9jmkFOzPENHi1EApImTi5F%2FGlXJ4prbEcmq%2FvAXWk3wfxEz8Z0A7OLV9t2Gjs5qQnM7%2BiCKD3Tjp6BLNqO46%2FwZzVWcqGi0Dii4JOB8PYg3LWAMyLIuY45WHZEYBbBeInPoOc9kF%2F1juVBD2DCAhQR5jExw9prYoKmvVl410eApLZHloEBTnEsX3t5I%2FsO5tXyzhOuztGe1HibNQRNcvKmGZ2Dt%2FwzOv73Gk765r6xQFthGvgAi2QxAbzOQkT9HashkQkV7CIFuhOk%2FzOm6E71PwZOoTLRCYBrW21WxWtTjDlTQNZa98IMW3JT%2FkIMZtRXfAUyvQzXmqIa4k6fWszBJPDMEXaFewPECZBRvoea6wNy24DkQ6f%2FGPLPpSHasSaj%2BENSzn%2F%2Fo09MK%2BY28wGOqUBSuRPFbb9SDGEofrftt3zt2HmM%2F%2FtKKgU2j7J2f8oUNAhrnHY3K15quQrg461tUkw21wfGlN4ojWp8dVv%2FhoqrLw%2FhmkO9vpwZzkGw%2FA1f9plEos1R0eacLbdUeq2M%2BR3GJEXZzPZoHAHt6Cw8YO%2BoXvG9zKXc0ORV%2Bt0KXJOP97KVTQXYzFM64gXfXFtqdDESgAkgOs%2F42eAiYD4wiY4LdBvavrj&X-Amz-Signature=c6dbd60b4c9a59e014cb3c995378b68d07c5ed4dc8d820c8966827a8d72571c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Suah
- [x] change menu titles:

- “Election” → DAO Candidates

-“Committee” → Agenda

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4d8507fc-f6df-46ba-98bb-e502c357d9c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PZZ77N7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRMk99fdRm%2BfUZZwL7FiIhLBdpXNpw1%2B6f1o1FFO3llAIgCdsg2t3v7D5Vlq%2BDQ5zm5JSYWvLpNEHqNo%2BKpYvtL6Uq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMO1HtSI%2FbQpT6mDwircA48ASKp6JwfIo2kNCAAMyMDibXU1xjRlKRdh85sVxY56nKGpQP0IIlNqBWqTDGFr15k3aLO1CApqhevDep1irMcO%2BsubdmVThjrHZA7qB%2F0ZOUHiRO9lVes3QGvnRAkDNlIu613E090RhEOi6d9ftrBUAFT7gfPUJHQA5bTmlBa%2BETkIPw4Tb97%2BUld3yg8SOBa7jnPV90AtkVRlQCgcT5ibWz4FKp7UVUhLShOg9g%2FJvUV0Ey8gK0CxYDExEyLq8y2f0UL1FWI7MGgJ2xvFHt%2BRAn1HsIlLSMGWPPmTaxOOrDPx%2BF0WzfQ2hJj8j8mj%2B%2Fj4J8wGvQeQBW4zOLpNjvgETF4e1bTudwLWT4uONVY6LjjgeKaefxHSDKckqPigPbRx0DcZgdWwhRmdKYXQBVlCmjXKZTpVpS53Wh1ipB7upI0abIQKMqLrGs%2Bj3HRaC8VgP0HgPmfw%2Bt9L7VoKdKdjBbIJhhueFRRqUtrHlhwkiupYwHV4QlgBqhEORG8pyX7Ay0USaV9SRMGW%2FR%2FAl%2FLu8Zvy1s8rYG0CK5OdWN%2FQSxFQDchE2eojHD815ESEdK2aOYqm0whNFsOEmu3%2B89WwsjoCak3nbytv3DtITL0pqlRfQjU9HVHa9Ky4MLKZ28wGOqUBQlJbSazYlEVQvjk%2Bg3gEan5Px0OwdFBDr6w43VUbqqE41ZUMN14EI%2B2syu7aMx56e8fPKdWAEho9qIxoQeMwMaxgONdgKlAJtvc8NRSWjMHnZMCM34ZrJUo%2FUpU1jb3bwo4CoFVtQ5VxlDMqRZdYLB6IqJfg0IbafbHWIuk4jqIhla1TpQz6myAx8QugsW7g3Pgd2RzEmGC78tqREp8KokXUZt0L&X-Amz-Signature=2b773f7e6429b5092abe742c2e766c3f795a973219656b9fad8ecef7c9ac70b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] Change menu name “Agendas” ⇒ “Statistics”  + modify filter placement
