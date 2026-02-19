RFC#13 : [Added signature verification function to DAO contracts · tokamak-network tokamak-dao-contracts · Discussion #13](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/13)

The contract that manages the contracts created using TRH-SDK will be handled by the SafeWallet Contract, and one of the responsible persons will be updated to enable the DAO Contract to do so.

The TRH team is currently targeting the mainnet testing run of the TRH-SDK between January 19th and 23rd, 2025. Therefore, request that create an agenda to support this feature in line with this schedule.

(The current agenda has a 16-day Notice period and a 2-day voting period, so it takes a total of 18 days from the time the agenda is created to the time it is approved.)

## SafeWallet Execute Test

- The test is a process in which 3 candidates must agree to pass.
- 3 candidates will proceed with 2 EOAs and 1 Contract. (3 of 3은 risky하다, 2 of 3을 할 수 있게?)
- Test contents
  - ETH transfer
    - tx : [https://sepolia.etherscan.io/tx/0x96b5180d0f864ec847470903c491bf893826320e51850037b0adb0cdc5f0d039](https://sepolia.etherscan.io/tx/0x96b5180d0f864ec847470903c491bf893826320e51850037b0adb0cdc5f0d039)
  - MockContract administrator function Execute
    - tx : [https://sepolia.etherscan.io/tx/0x47d8f29242c0117784dce651fc4bdc58caac6a9c7c065b6c4508144f1ea73dd4](https://sepolia.etherscan.io/tx/0x47d8f29242c0117784dce651fc4bdc58caac6a9c7c065b6c4508144f1ea73dd4)
  - TRH-SDK administrator function execute
    - tx : [https://sepolia.etherscan.io/tx/0x72907ce5898d73a1c6c4e2c01ddc1acd8b887995e0fef163ddc46d4a7bf437a7](https://sepolia.etherscan.io/tx/0x72907ce5898d73a1c6c4e2c01ddc1acd8b887995e0fef163ddc46d4a7bf437a7)

## Create Agenda Process

1. DAOCommittee_V2 Contract Deploy
  1. script : [https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/1.deploy_DAO.js](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/1.deploy_DAO.js)
  1. command : npx hardhat run scripts/1.deploy_DAO.js --network mainnet
1. Create Agenda
  1. script : [https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/14.createAgendaAboutRFC13_Mainnet.js](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/scripts/14.createAgendaAboutRFC13_Mainnet.js)
  1. Need to input Data the New DAOCommittee_V2
  1. command : npx hardhat run scripts/14.createAgendaAboutRFC13_Mainnet.js --network mainnet 
1. Total Cost
  1. [https://docs.google.com/spreadsheets/d/1wLUnD2V7yzzJb3jtG5hevYDt57PCcTve7aWhnwcYFL8/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1wLUnD2V7yzzJb3jtG5hevYDt57PCcTve7aWhnwcYFL8/edit?gid=0#gid=0)
  1. 0.006 ETH & 10 TON (1 Gwei standard)
1. Precautions
  1. Approval must be completed starting from Agenda 15, which is listed in [RFC#12](https://github.com/tokamak-network/tokamak-dao-contracts/discussions/12).
  1. If you do not wish to approve agenda15, we may proceed again by creating a new agenda. (In this case, please let me know in advance.)

## Feedback

- 하드코드되어서 변경될 수 없는 부분(시뇨리지 로직과 관련된 부분은 건드릴 수 없게)과 운영중에 변경할 수 있는 부분은 나누어서 관리되어야한다. (혹시 하드코드된 부분이 변경된다고 하더라도 DAO에서 일관적으로 변경할 수 있도록 해야한다)
- 분리되는게 가능한지 파악
- 옵티미즘과 우리는 나아가는 방향이 다르다 (큰줄기 하나, 작은 줄기 여러개)
- 이렇게 DAO업그레이드를 진행하지 않더라도 할 수 있는 방법이 있을 것.
- TRH도 나중에 업그레이드로 Challenger를 붙일 수 있도록 개발해야한다. (마이그레이션을 감안하고 개발을 진행해야함)

## EN

- The hardcoded parts (those related to segregation logic) and the parts that can be modified during operation should be managed separately. (Even if the hardcoded parts are changed, the DAO must be able to handle the changes consistently.)
- Find out if separation is possible
- There must be a way to do this without having to upgrade the DAO.
- TRH should also be developed to accommodate Challenger upgrades later. (Development should be conducted with migration in mind.)