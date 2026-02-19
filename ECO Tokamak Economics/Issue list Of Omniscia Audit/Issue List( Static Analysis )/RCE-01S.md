[https://omniscia.io/reports/tokamak-network-ton-staking-v2-67bc7fe2ee4dd600185cd150/static-analysis/RefactorCoinageSnapshotStorage-RCE](https://omniscia.io/reports/tokamak-network-ton-staking-v2-67bc7fe2ee4dd600185cd150/static-analysis/RefactorCoinageSnapshotStorage-RCE)

RCE-01S

[Link](https://github.com/tokamak-network/ton-staking-v2/issues/235)

The RefactorCoinageSnapshotStorage contract is a contract already in use in the service and used to create a Candidate. We do not plan to upgrade the logic of the contract being serviced unless there is a critical error.