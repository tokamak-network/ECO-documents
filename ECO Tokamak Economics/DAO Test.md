# test page 

- Election (voting~withdrawal):   [https://dao-tokamak-network-fdny4drf6-tokamak-network.vercel.app/#/election/0x0f42d1c40b95df7a1478639918fc358b4af5298d](https://dao-tokamak-network-fdny4drf6-tokamak-network.vercel.app/#/election/0x0f42d1c40b95df7a1478639918fc358b4af5298d)
- Agenda : [https://sepolia.dao.tokamak.network/#/agenda](https://sepolia.dao.tokamak.network/#/agenda)
- page : [https://sepolia.dao.tokamak.network/#/election](https://sepolia.dao.tokamak.network/#/election)
- 공지기간 최소값 변경([tx](https://sepolia.etherscan.io/tx/0xd43e8c5d5afa603f0ee78a44818e98c864f63147bff70c1c9733a59f31d13fff)) : 16일(기존) → 5분 (변경) 
- 투표기간 최소값 변경([Tx](https://sepolia.etherscan.io/tx/0x81ac2e94f5636f3adc5aa915bdb1e068c704e1ccb332b5488e32fb6fe74ae9d9), [Tx2](https://sepolia.etherscan.io/tx/0xd86981621e0fda89a2c58679e397348be1ce3c1d3fb14b3edb0ee8940fceef97)) : 2일(기존) → 5분 (변경) → 10분(변경)
- sepolia faucet [https://faucet.chainstack.com/sepolia-testnet-faucet](https://faucet.chainstack.com/sepolia-testnet-faucet)
## swap 

  [https://tokamak-bridge-sepolia.vercel.app/](https://tokamak-bridge-sepolia.vercel.app/)

# Test 

Zena (1차 테스트 2023.12.12) 
- [x] 아젠다 등록  **setGlobalWithdrawalDelay  **
- [x] 아젠다 등록 **setMinimumAmount **
- [x] 아젠다 상세정보 정확하지 않은것 같음. 아젠다 투표시작시간과 종료시간이 정상표시 되지 않는것 같음. 

Zena (2차 테스트 2023.12.13) 
- [x] 멤버는 아니고, Candidate의 오퍼레이터인데,  우측상단에 클래임버튼이 활성화 되어서 클릭했는데, 클래임 금액이 0.00 TON 으로 표기회어 있음. 클래임 버튼 클릭시 아무 동작 없음. 
- [x] 심플 스테이킹에서 해당 레이어에 커밋시 추가되는 리워드 양과, 다오 페이지에 업데이트 리워드 버튼 클릭시 보이는 리워드 양이 다름 , 다오페이지의 업데이트 리워드 모달 페이지는 항상 0으로 나오는 것 같음. 

Harvey (1차 테스트)
- [x] DAO에서 undefined 정보가 있습니다.
- [x] vote버튼이 작동하지 않습니다. (unvote, Revote 정상작동 확인, withdraw는 테스트 하지 못함)
- [x] DAOVault의 기능에서 더 이상 TON, WTON관련 기능은 사용되지 않습니다
ERC20기능만 있으면 됩니다!
- [x] Voting시간이 지났는데 **Not Started Yet**이라고 뜹니다
- [x] isVotableStatus이 true가 되면 Voting할 수있게 변경하면 해야할 것 같습니다.

Harvey (2차 테스트 2024.01.03)
- [x] Vote에서 Vote버튼 클릭시 무반응입니다.
- [x] member였던 사람이 claim을 할려고하면 0으로 나오고 ~~claim버튼도 동작하지 않습니다.~~
- [ ] 

[[취약점 수정 + TON don’t use 테스트]]

Harvey (3차 테스트 2024.01.19)


Suah (2024.1.18)
- [ ] 

# Internal QA by Eugene + Lucas