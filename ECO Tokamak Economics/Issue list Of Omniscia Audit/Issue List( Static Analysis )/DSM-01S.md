[https://omniscia.io/reports/tokamak-network-ton-staking-v2-67bc7fe2ee4dd600185cd150/static-analysis/DSMath-DSM](https://omniscia.io/reports/tokamak-network-ton-staking-v2-67bc7fe2ee4dd600185cd150/static-analysis/DSMath-DSM)

[Link](https://github.com/tokamak-network/ton-staking-v2/issues/216)

It is used in the RefactorCoinageSnapshot contract.

However, this RefactorCoinageSnapshot contract is a contract already in use in the service and is used to manage the seigniorage of each layer. We do not plan to upgrade the logic of the contract being serviced unless there is a critical error. In the same context, if the newly distributed code of Coinage is distributed differently from the existing one, there will be management issues, so we will maintain the current code.