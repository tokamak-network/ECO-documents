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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/94cbeef9-bed4-4483-b8db-8c46ca981dc2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-03-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.28.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BCZV2YR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHmL%2FOdeL%2BYDmlPXIu%2BDIdvly%2FX3W6c4MfCkWODENOCQAiBdz9DVuXxRWFu8wtHNyl94r2iOP%2BIoYD2Nh93RjDoK6Cr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMRtIs4JhL3kOXH3E7KtwDQ4%2F76tIuTvNsvoE24%2F3vJW27pXwh0fmaBjVNALrJJhe8ndmcwt2LhnG%2FzNKpUUWBPG0SIE1xBxMSB37bG6b6b0tMZHQsTPQsJd%2FjLiMg7f5coShCiI2A%2BfYti6cLHrXcMpYSR%2B3ZId6pUc2Nk3VmG41JUECf01GVPGHmYsrQ08rX%2BHVGLscDSff0QRi4Nz%2FdyiHkJE5s9R3q6CMrG4tTNjCBL5k8SR9zmOFWwL4%2Fdeziojz%2BrfVUxX7Wq7d%2FoJK2J0D7THlD0efk5F%2BTQvpP%2BK%2FtvcXTh5HakdvNrUx5JINaXxlQiTl3T4MZFOs5lbohlLA9SHDzxcCvt5UkgBRtt%2FjZxcxn033Hrr7SHGCLUNA4PwO6yOf4C3o%2BknmpCcKDroRBxcPt8NvG3o6y9jjwt94dvY8lD68IDjpJP3RoBqcvGvW7O%2BhWG3LclL2e141YVN%2Beqdwqb6SphiQfX6rTR%2FWA132ZNW4Xf8Kmh6dp3UaHTbq%2BUGqN6ZogLn0R%2FS6l1TBJTI%2FXrS7m6RZs1b%2BsEljhO9JZtrpsGIlT0BRlZ6Zszsd9rOiEsxrAi8Rdm5ROt4SBgUX4Td%2BHvBHycWQZ4s51N483S4A73c90B2IqMYOCSdWvfQkAvilzC7AwsMTazAY6pgH8T%2Fe10K7slz7ycaLFZvvi%2B00UDKQZwjB4x2lqHEVH6OKec2pM0iTa3Cr2w1Q%2BX20%2Bs7Rqm4aZJEtIxhq5PNkMgb%2Fbsk11mB5fAEkiVK4IEamSd5%2BkEJBvoT3OyMkMTxquYQMoDEV7pgS%2FAFDYl7xvt6EfCfPmRbJmYDuVeKvP6TUVQcGYyDFrb6B9LaZenGBQYW%2Bdzj0KhnYwK5Di4jrffVFTANeI&X-Amz-Signature=3609996601784e12ebff024a923092bf45305157a940fc48f34cbd1a5a341b1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1c3752ab-652f-4355-8e99-15aa5a170ea7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNLI5VBW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWfPeMNdS9whDP4qSfvFfOTkTcgNrwH9CYhPwXepr2ZAiEAj4p6%2FIEcDwyx9%2BAlEXCXSKQtAsJkfGUZikV0Tn4aBqYq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDCZtTq0asgd%2FgAP0GSrcA%2B4xVn6CFa%2Fz6dX0oLMVBomMU9ivQD4lZoyw4sHQ16%2B9viUcDknRJ70UuwiKLxly6H2xNaGsY%2FZE4ufQXKoUpctGl9GheEAH7GRWFS%2BFdaezpIR3O6K3zAI7xm8e%2F2doeXSiOz9HVhsYXrtBd0xIPBVckwSSBaxwoztp%2FH7oPkNdoGWfX3FHxBAsEVfkUlIJ3n0WoLRStC9zlYUztm5yGZNT9CWgWs02gS%2BC7sXGAhq845XlE3DmIoVoYGCfYp8rqqI3zODQfj570s3J%2FEZbIBywz2vMGAIaYuZyCM%2BcwCjY4jTS5Lp3ARRZiionsGfdLMzMc2vcGJwQC16W%2FZI5MDteLvmfrXUnm6Oy1sNx5v9M6THahKuYaTzzq1L03%2FPPcbJ%2BpPO%2BhrDzzDo9G%2Fbb3IzQzT77dB%2Bx%2BD10F1iVQLdQTcC%2BUQNtfFy4bpw6RY10E6%2Ftcu2HvoOYPVSrMl5V3o%2FXBWRM%2F8c7aOX1d66WLQKjXynbsHlebDm47CYbVS%2FCZb5xI5JFx%2FpTGd2PSZRgVceZenuK4i%2Bbtz5jtpXZaIP%2F39dKQJfZUw%2BjLKDS2p0LquZ9LAyX4cwk%2BFToaLEtEO0oL1IS6w6bmR14YnacyU9d%2FlfByJ5P%2FSgVwLvyMNLE2swGOqUB4R7W7DA%2FoqCjtovQdnGjaMV87wffIObCjHnh4WylcvhnFzf6E7uDx0trRib%2FSRNQBiQJDbxFkvAig%2BJCajaVnbenxwyAIcRwz%2FJkxV%2BGV14ff4iXC%2B4eGYbqFc6fXgZzCi1w6UgaQnu36s%2FB7nRGdBQqVcQOvdxvyrpjWM9v43wOXczcCXQDwv8EijLlUSi81mszmb28lOn7N9Oz%2FpTu27WK8%2Fs9&X-Amz-Signature=3275ef552cef540bc45dc168a9bdfe338a8f0e53a9e111bfd8669eedf3752c17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Suah
- [x] change menu titles:

- “Election” → DAO Candidates

-“Committee” → Agenda

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4d8507fc-f6df-46ba-98bb-e502c357d9c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZXSUXA3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCW2DWWIztbdJfv7lAAFAmvpsNrRwrEOCSecCPNuoH6LwIgUmUn%2FWZ2NyRhc2AsOIKeXhHezAOFQ2iUn3k1pU5x6KMq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDH2r4ex0HlnJj5MHHSrcA8B6FnMQAsLV%2FHoU0ZAJIX6RzB1RwZxS%2BhgcZ5CmbIab6PxLtUPzJIZ%2BFOyL81%2FMkrtze12KOGiqTwXaDawBpSd1RUXfiU4lZc76fcTIjYZoMXHQhtsGtMuIKYBmINdJLcB3SeuZ8PdHZCpcnrn3Nv1Ez79c8JZSz9LySFOWs6NWxYijghUlVI7vx9%2B3%2BVxLM8OQDeG3OyKC0BZQAfvc3jXjA1VvhrNj92Ae4RfQySCVrg83U2BlKQYmIqgSd9lZobgQ1VEXYC2CbAi9qiAA4GguhA3OdBCJpVsT8WWoSkbh4Yna1EiCKfrbiaVbM0v8pg8P8zbz%2Bqbj6iR%2FOYu276EMnD9B1faEIBiTBWQelUaw7fOKt4Uu3fD69%2BZDn0oPIII%2BlxvJrh6GgWnvsvJ1LHVFABYr8R%2Bxtqi1BRSkd6sei2gamoqWTft%2BjiuQR39z71zFe9eDVM%2FM2s%2Byflhbp0aThKQraVcjT12Y0eedJpL6tQrvGK53EGVBdpRZQQQjUhFuwf%2FpnORl7Px6XKQHBon8m%2BwsfrO6th4WiML%2Bbc%2BTWP%2FDbxaqstxpp4pBYuHfz9Ie0YO4CYonjMR%2BWc26ux2kc3xEF6yr3dxgZ81a6LiN%2BI7ZxMY0rPvwALDOMM3D2swGOqUBr3SgFXGIHX3wM7ic%2Bq%2Fvd7pFaW5jgkBwXQh3uH7jjYabX2w2MAXNeJ9PBpJpEJNPObK7Rj1UTSRa0AwqWxBFkzyn6qeNtAUYupA8OzOEzoz3gcQ%2BlWjwz4oZ84nX%2FzdXWpOmhcFMxhYNc9lPgdLWo3zD5eHMupUPuOOcj4MqQOH5clxkr5TGHNQVz5qjhZArhR2em5jEy%2BiIHdRh1ySZs9mnxapI&X-Amz-Signature=529f8b8c2321f68214c10ed031ae2c02c3c2115712336a9d553e347b8ddd990a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] Change menu name “Agendas” ⇒ “Statistics”  + modify filter placement
