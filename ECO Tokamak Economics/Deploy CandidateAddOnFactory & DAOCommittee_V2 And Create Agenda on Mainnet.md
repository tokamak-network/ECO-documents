repo : [GitHub - tokamak-network/ton-staking-v2 at deploy-candidateAndDAO](https://github.com/tokamak-network/ton-staking-v2/tree/deploy-candidateAndDAO)

test: [doc1](/1dfd96a400a380e69602ce6b7c590782#1dfd96a400a380c39f23eb19a46d9ce2) , [doc2](/1f3d96a400a3809fb3acfb4e80a69562#1f3d96a400a3803fa715fe6618b96af2)

# Deploy CandidateAddOnFactory & DAOCommittee_V2 Contracts 

### Expected Used Gas 

[https://docs.google.com/spreadsheets/d/1W6OW0Ns-C0pIhYuShwtf2_oksC4OozcWLjYoWBVm3Nw/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1W6OW0Ns-C0pIhYuShwtf2_oksC4OozcWLjYoWBVm3Nw/edit?gid=0#gid=0)

- gasFee : 0.018 ETH & 10TON (gasPrice: Based on 2gwei)
- Deploy & Create Account : 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- ETH transfer (Jason → Harvey)
  - ETH(0.018) : [https://etherscan.io/tx/0xcd56165816e8b3d171205cd915a730c797429c323aeba4936b1de18c47fa950d](https://etherscan.io/tx/0xcd56165816e8b3d171205cd915a730c797429c323aeba4936b1de18c47fa950d)
  - TON : [https://etherscan.io/tx/0x4d302cee9add4ee41dc5c2dcf6671d9ced1a7224fd9f5a85531856582a3fb9bf](https://etherscan.io/tx/0x4d302cee9add4ee41dc5c2dcf6671d9ced1a7224fd9f5a85531856582a3fb9bf)
- ETH transfer (Harvey → Jason)
  - ETH(0.0138) : [https://etherscan.io/tx/0xdf208c98b1e1981f3f7cda460f9cf4711cacc421ed4df89a0a09011be76c54e4](https://etherscan.io/tx/0xdf208c98b1e1981f3f7cda460f9cf4711cacc421ed4df89a0a09011be76c54e4)

## Deploy CandidateAddOnFactory

- Deploy account: 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- Deploy command:

```shell
npx hardhat run scripts/layer2-mainnet/9.deploy-candidate-add-on-proxy-factory.js --network mainnet

npx hardhat verify 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22 --network mainnet
```

- tx : [https://etherscan.io/tx/0x2a206160568a018d13152224f0bc668105080640acb8610e1f5d8c19c35971ae](https://etherscan.io/tx/0x2a206160568a018d13152224f0bc668105080640acb8610e1f5d8c19c35971ae)
- Deployed CandidateAddOnFactory address: 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22

## Deploy DAOCommittee_V2

- Deploy account : 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- Deploy command
```solidity
npx hardhat run scripts/1.deploy_DAO.js --network mainnet

npx hardhat verify 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B --network mainnet
```
- tx : [https://etherscan.io/tx/0x08589450dbe4708ea928e3c0aa92cf5dd3aa60ecb4f43bebceb66461706471d1](https://etherscan.io/tx/0x08589450dbe4708ea928e3c0aa92cf5dd3aa60ecb4f43bebceb66461706471d1)
- Deployed DAOCommittee_V2 address: 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B

## Deployed Addresses 

```solidity
DAOCommittee_V2 : 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B
CandidateAddOnFactory : 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22
```

## Create Agenda

- The agenda performs two functions:
  - The first is the upgradeTo function for CandidateFactoryProxy.
  - The second is the upgradeTo2 function of DAOCommitteeProxy2.
- create agenda
```solidity
npx hardhat run scripts/13.upgradeToAgenda_on_Mainnet.js --network mainnet
```
- tx : [https://etherscan.io/tx/0x1cd0e5c2e4e9d499cd9e72dd86e047815ba44c8e19e8296181cb29e989b1398d](https://etherscan.io/tx/0x1cd0e5c2e4e9d499cd9e72dd86e047815ba44c8e19e8296181cb29e989b1398d)
- Agenda 15 : [https://github.com/tokamak-network/ton-staking-v2/issues/311](https://github.com/tokamak-network/ton-staking-v2/issues/311)

## After Test

- Create an agenda and then test it
- After setting blockNumber after agenda creation
```solidity
npx hardhat test test/agenda/35.AfterDeployIntegrationTest-mainnet.js 
```
- Result
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/12baa833-3199-4ab3-abf7-617549565e9f/75A2C405-A39A-48E8-B267-E3C857F0078F.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656A5KLUE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqlN5Baezpm7JoA9PtXo0QATIOvdKLfkCJhpy3kNYBGAiA%2FM8FdgHI%2FoxFC2t35poLmoD8ynr081MBcM1wzu6OAsyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMgUXFN%2Fnen3%2FTIYmtKtwD4YcOq%2BpmFu48X%2BIXajPg%2F2P8%2BB9LQqWzXvGYpixu6%2BzJYjThwkkQpDY5mcjSrj2fBs3u%2BvYeXTykTc2QAamK6z1ajjwvXByKsas%2BG1E6xs4uaeDC9h%2FLsajTiEqSUTw74JVhjuKqP8xi1gfsU%2FUdMueUH%2Bog6cD2d1sgzLEd6VqGORDVpHB4Ev%2BODTsoDG6MVJyW7MKjM%2FU0wm6gdpVqVtqSO25uZIhb2xQDSZLNRc6KkFG9esQzJw8OT%2BuTU4JgmNVNi7DpbNRSeFF6lu%2FvKUdvoaWmbsur3b8tDDpomdtPidI3qpA0yogwHj2hdF7Y8%2BTeQ62Mz%2FVBt1aDD5AUKmgKl3eKK2H8Z4rzhaErg2O5KER2Qzbi2uxQlFSGTuBUyODGeOujrXinXrS6P8amgbG1dRKlTazik%2F7RyciaEcIgdEaRTi%2Bz4FmIiKXOQCR2iMvzi0kJW0jkNqrtUJLNTDzWOxCT%2FjgIt6lu540phMD0NcNQk2RZLIbgFSqlBMe4L7u7xTp3YSIAkkra0%2BScijWp87E0Abewl642ZMFeWYEFF9TWdgC8NzOLmw0uF7FBv%2Bzb8XzNefEZrr7gJXQcJRu2%2BDa1CVgpblDZ%2FC4F8pHIaDNEf3TsonhZGZQw0JrbzAY6pgG5FF82V%2FN4YNMmJvig%2BZfUk5IKjcLc1AIOXHsgJ4hm1V1G3bMsOK0%2BRidUAgveqdvt%2Fj1Ktzt%2F7qKesmYx%2Fioc%2Fr2HmMWrfp4MxChFQOhFTBQT8fSe7AJZ%2BFU%2BW80CpVp6h9B2E397fYlrA4RYssrPEGAkFF36UdQAKwNFkK0PGk%2FFy9OR5MTcJv4H0CsnpEQ2tbkS6nkcC8e3t%2FMWJICKaeIpQ9kA&X-Amz-Signature=812d90a5ff3361aa72494b7e689175a24942b8680fa73aa67f19e56fc68153c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/60e33936-1e94-48b9-84e5-d13d91f73754/97ABCDD3-633F-4983-AE31-B6212AEF86DC.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656A5KLUE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqlN5Baezpm7JoA9PtXo0QATIOvdKLfkCJhpy3kNYBGAiA%2FM8FdgHI%2FoxFC2t35poLmoD8ynr081MBcM1wzu6OAsyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMgUXFN%2Fnen3%2FTIYmtKtwD4YcOq%2BpmFu48X%2BIXajPg%2F2P8%2BB9LQqWzXvGYpixu6%2BzJYjThwkkQpDY5mcjSrj2fBs3u%2BvYeXTykTc2QAamK6z1ajjwvXByKsas%2BG1E6xs4uaeDC9h%2FLsajTiEqSUTw74JVhjuKqP8xi1gfsU%2FUdMueUH%2Bog6cD2d1sgzLEd6VqGORDVpHB4Ev%2BODTsoDG6MVJyW7MKjM%2FU0wm6gdpVqVtqSO25uZIhb2xQDSZLNRc6KkFG9esQzJw8OT%2BuTU4JgmNVNi7DpbNRSeFF6lu%2FvKUdvoaWmbsur3b8tDDpomdtPidI3qpA0yogwHj2hdF7Y8%2BTeQ62Mz%2FVBt1aDD5AUKmgKl3eKK2H8Z4rzhaErg2O5KER2Qzbi2uxQlFSGTuBUyODGeOujrXinXrS6P8amgbG1dRKlTazik%2F7RyciaEcIgdEaRTi%2Bz4FmIiKXOQCR2iMvzi0kJW0jkNqrtUJLNTDzWOxCT%2FjgIt6lu540phMD0NcNQk2RZLIbgFSqlBMe4L7u7xTp3YSIAkkra0%2BScijWp87E0Abewl642ZMFeWYEFF9TWdgC8NzOLmw0uF7FBv%2Bzb8XzNefEZrr7gJXQcJRu2%2BDa1CVgpblDZ%2FC4F8pHIaDNEf3TsonhZGZQw0JrbzAY6pgG5FF82V%2FN4YNMmJvig%2BZfUk5IKjcLc1AIOXHsgJ4hm1V1G3bMsOK0%2BRidUAgveqdvt%2Fj1Ktzt%2F7qKesmYx%2Fioc%2Fr2HmMWrfp4MxChFQOhFTBQT8fSe7AJZ%2BFU%2BW80CpVp6h9B2E397fYlrA4RYssrPEGAkFF36UdQAKwNFkK0PGk%2FFy9OR5MTcJv4H0CsnpEQ2tbkS6nkcC8e3t%2FMWJICKaeIpQ9kA&X-Amz-Signature=3e4743f8dbe3eb4b8943e9e18d8f77ad57f6ef7c82f8ca05c0f40216dd0aca11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e44884da-edb5-4fc7-bfac-745c34044ab6/271FA56D-F04A-417F-AA08-E01CB3E589F6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656A5KLUE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqlN5Baezpm7JoA9PtXo0QATIOvdKLfkCJhpy3kNYBGAiA%2FM8FdgHI%2FoxFC2t35poLmoD8ynr081MBcM1wzu6OAsyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMgUXFN%2Fnen3%2FTIYmtKtwD4YcOq%2BpmFu48X%2BIXajPg%2F2P8%2BB9LQqWzXvGYpixu6%2BzJYjThwkkQpDY5mcjSrj2fBs3u%2BvYeXTykTc2QAamK6z1ajjwvXByKsas%2BG1E6xs4uaeDC9h%2FLsajTiEqSUTw74JVhjuKqP8xi1gfsU%2FUdMueUH%2Bog6cD2d1sgzLEd6VqGORDVpHB4Ev%2BODTsoDG6MVJyW7MKjM%2FU0wm6gdpVqVtqSO25uZIhb2xQDSZLNRc6KkFG9esQzJw8OT%2BuTU4JgmNVNi7DpbNRSeFF6lu%2FvKUdvoaWmbsur3b8tDDpomdtPidI3qpA0yogwHj2hdF7Y8%2BTeQ62Mz%2FVBt1aDD5AUKmgKl3eKK2H8Z4rzhaErg2O5KER2Qzbi2uxQlFSGTuBUyODGeOujrXinXrS6P8amgbG1dRKlTazik%2F7RyciaEcIgdEaRTi%2Bz4FmIiKXOQCR2iMvzi0kJW0jkNqrtUJLNTDzWOxCT%2FjgIt6lu540phMD0NcNQk2RZLIbgFSqlBMe4L7u7xTp3YSIAkkra0%2BScijWp87E0Abewl642ZMFeWYEFF9TWdgC8NzOLmw0uF7FBv%2Bzb8XzNefEZrr7gJXQcJRu2%2BDa1CVgpblDZ%2FC4F8pHIaDNEf3TsonhZGZQw0JrbzAY6pgG5FF82V%2FN4YNMmJvig%2BZfUk5IKjcLc1AIOXHsgJ4hm1V1G3bMsOK0%2BRidUAgveqdvt%2Fj1Ktzt%2F7qKesmYx%2Fioc%2Fr2HmMWrfp4MxChFQOhFTBQT8fSe7AJZ%2BFU%2BW80CpVp6h9B2E397fYlrA4RYssrPEGAkFF36UdQAKwNFkK0PGk%2FFy9OR5MTcJv4H0CsnpEQ2tbkS6nkcC8e3t%2FMWJICKaeIpQ9kA&X-Amz-Signature=8efaf1d317c1631c39e9c6c51da60f543f1c796be335653512ae58cfd703b3dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- 