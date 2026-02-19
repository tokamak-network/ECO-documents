Repo : [https://github.com/tokamak-network/ton-staking-v2/tree/11-refactoring-to-reduce-gas-costs](https://github.com/tokamak-network/ton-staking-v2/tree/11-refactoring-to-reduce-gas-costs)

`npx hardhat test test/layer2/units/5.stake-v2-gas.sepolia.test.ts`

It extracts the used gas log by functions into ‘outputFile/log-used-gas.xlsx’

# Aggregation of gas usage by function 

집계된 사용가스를 보면 registerLayer2Candidate 함수가 가장 많은 가스를 사용하고 있다. 

그 다음으로 updateSeigniorage with staking , updateSeigniorage with claim   and withdrawAndDepositL2 순으로 많은 가스를 사용한다.  

따라서, registerLayer2Candidate , updateSeigniorage with staking , updateSeigniorage with claim   , withdrawAndDepositL2 함수의 코드를 중점적으로 리팩토링하는 데 초점을 두도록 한다. 

| Contract | Name | Description | GasUsed | GasUsed (ETH) |
| --- | --- | --- | --- | --- |
| Layer2Manager | registerLayer2Candidate |  | 4885371 | 0.04885371 |
| SeigManagerV1_3 | updateSeigniorage(2) | the forth updateSeigniorage of operator with staking | 592072 | 0.00592072 |
| SeigManagerV1_3 | updateSeigniorage(1) | the third updateSeigniorage of operator with claiming | 484395 | 0.00484395 |
| DepositManager | withdrawAndDepositL2 |  | 474176 | 0.00474176 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | the second updateSeigniorage : not operator | 436149 | 0.00436149 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | the first updateSeigniorage : no give seigniorage to l2 | 428081 | 0.00428081 |
| DepositManager | approveAndCall | deposit TON to Titan Candidate | 374814 | 0.00374814 |
| DepositManager | approveAndCall | deposit TON to Titan Layer2 Candidate | 357714 | 0.00357714 |
| DepositManager | approveAndCall | deposit TON to DAOCandidate | 356170 | 0.0035617 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | updateSeigniorage to DAOCandidate | 343950 | 0.0034395 |
| DepositManager | requestWithdrawal |  | 340683 | 0.00340683 |
| DepositManager | approveAndCall | deposit TON to DAO Candidate | 322941 | 0.00322941 |
| DepositManager | approveAndCall | deposit TON to DAOCandidate | 315110 | 0.0031511 |
| DepositManager | deposit(address,uint256) | deposit WTON to Titan Candidate | 303991 | 0.00303991 |
| DepositManager | deposit(address,address,uint256) | deposit WTON to DAOCandidate | 290666 | 0.00290666 |
| DepositManager | requestWithdrawal(address,uint256) |  | 278176 | 0.00278176 |
| DepositManager | deposit(address,address,uint256) | deposit WTON to Titan Candidate | 254169 | 0.00254169 |
| DepositManager | deposit(address,uint256) | deposit WTON to DAOCandidate | 249099 | 0.00249099 |
| Layer2Manager | setAddresses |  | 218605 | 0.00218605 |
| DepositManager | processRequest |  | 197362 | 0.00197362 |
| L2Registry | setAddresses |  | 146750 | 0.0014675 |
| SystemConfig | setAddresses |  | 146738 | 0.00146738 |
| DepositManager | processRequests(address,uint256,bool) |  | 145889 | 0.00145889 |
| OperatorFactory | setAddresses |  | 92668 | 0.00092668 |
| L2Registry | registerSystemConfigByManager |  | 87131 | 0.00087131 |
| Layer2Manager | setMinimumInitialDepositAmount |  | 57280 | 0.0005728 |
| SeigManagerV1_3 | setLayer2StartBlock |  | 56891 | 0.00056891 |
| L2Registry | addManager |  | 50991 | 0.00050991 |

## After refactoring 

 

| Contract | Name | Description | GasUsed |
| --- | --- | --- | --- |
| L2Registry | addManager |  | 50991 |
| OperatorFactory | setAddresses |  | 115592 |
| Layer2Manager | setAddresses |  | 217793 |
| Layer2Manager | setMinimumInitialDepositAmount |  | 57293 |
| SystemConfig | setAddresses |  | 146738 |
| L2Registry | registerSystemConfigByManager |  | 89648 |
| L2Registry | setAddresses |  | 146750 |
| L2Registry | registerSystemConfigByManager | Thanos SystemConfig | 98997 |
| Layer2Manager | registerLayer2Candidate | using registerLayer2Candidate function | 4862471 |
| SeigManagerV1_3 | setLayer2StartBlock |  | 56913 |
| DepositManager | approveAndCall | deposit TON to Titan Candidate | 374814 |
| DepositManager | deposit(address,uint256) | deposit WTON to Titan Candidate | 303991 |
| DepositManager | deposit(address,address,uint256) | deposit WTON to Titan Candidate | 254169 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | the first updateSeigniorage : no give seigniorage to l2 | 429640 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | the second updateSeigniorage : not operator | 437487 |
| SeigManagerV1_3 | updateSeigniorage(1) | the third updateSeigniorage of operator with claiming | 480766 |
| SeigManagerV1_3 | updateSeigniorage(2) | the forth updateSeigniorage of operator with staking | 588263 |
| DepositManager | requestWithdrawal |  | 341275 |
| DepositManager | processRequest |  | 197362 |
| DepositManager | approveAndCall | deposit TON to DAOCandidate | 315110 |
| DepositManager | approveAndCall | deposit TON to DAOCandidate | 356170 |
| DepositManager | deposit(address,uint256) | deposit WTON to DAOCandidate | 249099 |
| DepositManager | deposit(address,address,uint256) | deposit WTON to DAOCandidate | 290666 |
| SeigManagerV1_3 | updateSeigniorageLayer(layerAddress) | updateSeigniorage to DAOCandidate | 347933 |
| DepositManager | requestWithdrawal(address,uint256) |  | 278176 |
| DepositManager | processRequests(address,uint256,bool) |  | 145889 |
| DepositManager | approveAndCall | deposit TON to Titan Layer2 Candidate | 357714 |
| DepositManager | approveAndCall | deposit TON to DAO Candidate | 322941 |
| DepositManager | withdrawAndDepositL2 |  | 476145 |
| L2Registry | rejectLayer2Candidate | legacySystemConfig | 115789 |
| L2Registry | registerLayer2Candidate | thanos SystemConfig | 4823637 |
| SeigManager | updateSeigniorageLayer | titanLayerAddress | 355902 |
| titanLayerContract | updateSeigniorage | with claim | 355815 |
| titanLayerContract | updateSeigniorage | with staking | 355815 |
| DepositManager | deposit(address,uint256) |  | 286891 |
| SeigManager | updateSeigniorageLayer | no give seigniorage to l2 | 435106 |
| DepositManager | deposit(address,address,uint256) |  | 254169 |
| SeigManager | updateSeigniorageLayer | give seigniorage to l2 | 408491 |
| SeigManager | updateSeigniorageLayer | not operator | 408491 |
| Layer2Contract | updateSeigniorage | operator | 485970 |
| Layer2Contract | updateSeigniorage | with operator's staking | 593467 |
| DepositManager | requestWithdrawal |  | 341275 |
| DepositManager | processRequest |  | 180262 |
| L2Registry | restoreLayer2Candidate |  | 72294 |
| SeigManager | updateSeigniorageLayer |  | 425987 |
| SeigManager | updateSeigniorageLayer |  | 403287 |
| SeigManager | updateSeigniorageLayer |  | 403287 |
| Layer2Contract | updateSeigniorage | with operator's claim | 463666 |
| Layer2Contract | updateSeigniorage | with operator's staking | 567880 |
| DepositManager | requestWithdrawal |  | 323583 |
| DepositManager | processRequest |  | 128962 |
| TonContract | approveAndCall | DepositManager.onApprove | 322929 |
| DepositManager | deposit(address,uint256) |  | 249099 |
| DepositManager | deposit(address,address,uint256) |  | 257425 |
| SeigManager | updateSeigniorageLayer |  | 354699 |
| DepositManager | requestWithdrawal |  | 326832 |
| DepositManager | processRequests |  | 109935 |