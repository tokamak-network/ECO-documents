# Deploy and Setting the DAO & TONStakingV2.5 Contract 

### Simple Summary

TONStaking has been updated to V2.5.
With this update, a Layer2 Candidate has been created and a new Staking service for that Candidate has been created.
With the new Candidate, the DAOContract has also been updated.

This proposal is proposed for the following purposes:

### Motivation

The Tokamak Network currently serves Titan, Layer 2, and will continue to serve new Layer 2s in the future.
Currently, TONStaking service does not provide services for Layer 2, but with this TONStakingV2.5 update, we plan to provide services for Layer 2, including Titan.
With the TONStakingV2.5 update, DAO Candidate has also been upgraded to be able to be created for Layer 2.

### On-Chian Effects

1. The structure of DAOContract is changed and the logic is updated.
1. The logic of SeigManager is updated.
1. The logic of DepositManager is updated.
1. Set the candidateAddOnFactory and layer2Manager values ​​of TokamakDAO Contract.
1. Set the layer2Manager and l1BridgeRegistry values ​​of SeigManger Contract.
1. Set the layer2Manager and l1BridgeRegistry values ​​of DepositManager Contract.
1. Register the Titan Layer in l1BridgeRegistry Contract.

### References

- upgraded DAO desciption : [repo](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md)
- TONStakingV2.5 description : [repo](https://github.com/tokamak-network/ton-staking-v2/blob/test-mainnet/docs/en/ton-staking-v2.md)
- Agenda Tests : [Create](https://sepolia.etherscan.io/tx/0xd7e84b1e00628219de08ddee400e528f36f9192cf0e9f41a3575f5fae4232301), [execute](https://sepolia.etherscan.io/tx/0xd8b5898807a7b21386a9d632aed14b5243a5cf9854fd97f5f678c82d2aaa4ff7)

### Copyright

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).