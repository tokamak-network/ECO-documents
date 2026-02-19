Related Issue: [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)

### Repo (Branch)

- [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request)
- the latest commit hash:  **01e198130b178757dd194bd8726a1ab678fca167**

### Expected review duration 

- 30 days 

### Development specifications: 

- **Here's a description of the contract being audited (what changed in v2.5).**
  - Description of staking v2.5: [description](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/docs/en/ton-staking-v2.md)
  - Description of DAO upgrade: [description](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md)
- Reference for understanding contracts
  - The ton-staking contracts readme: [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-request](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-request?tab=readme-ov-file#the-ton-staking-contract-distributes-seigniorage-to-stakers-that-stake-ton)
  - The tokamakDAO Contract readme : [tokamak-dao-contracts/README.md at guide-document-for-user · tokamak-network/tokamak-dao-contracts](https://github.com/tokamak-network/tokamak-dao-contracts/blob/guide-document-for-user/README.md#tokamak-dao-contracts)

### Contract scope  

- DAOCommitteeProxy2.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/proxy/DAOCommitteeProxy2.sol)
- DAOCommittee_V1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommittee_V1.sol) 
- DAOCommitteeOwner.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/DAOCommitteeOwner.sol)
- SeigManagerV1_3.sol : [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/SeigManagerV1_3.sol) 
- DepositManagerV1_1.sol: [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/stake/managers/DepositManagerV1_1.sol)
- L1BridgeRegistryV1_1.sol  [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/L1BridgeRegistryV1_1.sol)
- Layer2ManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/Layer2ManagerV1_1.sol)
- OperatorManagerV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/layer2/OperatorManagerV1_1.sol)
- CandidateAddOnV1_1.sol [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-request/contracts/dao/CandidateAddOnV1_1.sol)

## Test

### Download the code and configure it

```json
git clone https://github.com/tokamak-network/ton-staking-v2.git
cd ton-staking-v2
git checkout v2.5-audit-request

nvm use v20.10.0
npm install --force

cp .env.sample .env
chmod 777 .env
vi .env     // edit .env with your data 

npx hardhat compile 
```

### Test on Sepolia forking node

- Copy all of the content of the `hardhat.config.sepolia.ts` file to `hardhat.config.ts`.
- Test on blockNumber: 5859537 
  - Currently, sepolia has already deployed the contract, so we test at 5859537 block number forking node.
  - Set blockNumber in the forking section of the hardhat network in the hardhat.config.ts file to 5859537.

```json
npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts
```
- Test on blockNumber: 7551570
  - Currently, sepolia has already deployed the contract, so reset the existing data and redeploy it to test.
  - Set blockNumber in the forking section of the hardhat network in the hardhat.config.ts file to 7551570.

```json
npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts
```

### Test on Mainnet forking node

- Copy all of the content of the `hardhat.config.mainnet.ts` file to `hardhat.config.ts`.
- Test on blockNumber: 21077756  
  - Since Titan is currently closed, we will test based on block number 21077756 when Titan is not closed.

```json
npx hardhat test test/layer2/units/2.all.test.mainnet.test.ts

npx hardhat test test/layer2/units/6.dao-staking-v2.5.mainnet.test.ts

npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts
```