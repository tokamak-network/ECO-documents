repo : [https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure](https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure)

# DAO Proxy structure change

1. current structure
  1. Since the proxy can only see one logic, the Admin must change it to use other logic.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7ad244b3-33ee-4554-aeb7-5ee8048ff83a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXOFXI3P%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGTUrT9FdAPlBUwVF89Uc1jzCcMapv5WJ8LYntzA3CS7AiEAwZ3HxKeY8qEA8C2RxEvD%2FBU8MKdvW3xR%2BzOdBDE15HIq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDO%2FpkrPakM8yt81emCrcA0%2FyqD1lnUt2Tm%2BBawOBz3JvLxClD9O2P1IBEAXy99EtwiWrrgMlmYhmhyUEL%2BCibM%2FdMqH%2FxUCujbgllJSTsgayvPDsFkCwn2l%2FjB94iDfFoKM1FoJyz%2BKFlgO8Yf%2BlV%2FSDg2T5qEfwxuB%2BPMcibc4kvmfZIouBHZ%2FqRXxF5Ab6vpEyesCshWKNwESmmWtOAFSHgpVawgMI6sjA76kuYCeEOmLybApCT6ZWGcvKPNhse7mWFWkvgxbmxVs250DerXRBgA7iDiR1z1Pym7c%2F9G0TvrDDCGx4qjauDsztTXdL%2FKkqX4oyuxXwcEQ5ygjvxMXt0IwjQa88ObBHMS7QQ5cqRuK7f8y8jkjzjoI0o%2BiYj46VeChYtzebLeRc3iaWW4PKtddYUZ4L06B1pRjM6alrBIF56TJRCIqY0ENWPYxbGWqSaVxz%2BfqNTZZn2SYBBQoHUOeoNNwLGzZTYJsnY%2Bt3u%2Fa9tiRLhzFKqv0OL7PA5e8HmVof8mkuvR40IP5DcEjU5uCEXcIdEMN%2BzjXjqRHhHwv9s76%2FFpYpp2lpf5n01QDKMMBFUi1ZdpxRoXYMko%2FUut%2BSOaO1SM%2FPVZh7C6b%2FPNsaIcw9cR%2FiLvOIrgx9wuRVvqhpdDA3%2BFBoMKvw2cwGOqUBvw7ytKOSZmE0zB5oUVkjo8VU4fLYVkuAAnD0fOW5CB4d4mb%2Fdvsg839TnzrpxgZpUVF%2FAhXm1DdJ0kEfNIJ%2FzAMZy3G2%2BQkuK0g7CcrC9oHcGkbOLin4b3Ecov%2FjIVojauR88nKnMlagPlG%2FB1rGDC7ovNPZshEdUUyvc7iu3b15JMA%2B24%2FXIP5hZqmy8sMqyzwJ6XMQK0DCo0ds%2BCb5FA61yTMT&X-Amz-Signature=7d46293d1ac9a94bbaedbfc5db7be93da4f95539d9eaa9b8223983af06115ad0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. structure to change
  1. Changed the structure to one in which a proxy looks at proxy and proxy look at multiple logics.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4d05783e-33d9-4d45-a3e5-e73c929fded5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPQX7HY%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEqiCUvMaZeNYKuAecQMyzpfrl%2FOr6Ixh6eohCzKKOixAiEAm7zbryJ69nCvTkNgpTRXfrGBl55yUodsNP5U3trFLlUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJorNPPmiSuNb3%2BxhSrcAyILKbnuo2S%2BPAVN%2BZFvER0xfpuO1vsrDU66wkG%2Bt3VlWQqX7A7IJcgs8QtkBKq3tl8%2F4%2Bks7ogzMb69hHK2dul6ZRUBMooD89SCHJYbsCvzqpqIBix8N4eKn6xNWW5CfOvgNND9hUG4d20PxQ6G8R2laPnwV6U%2BPgoxOQ71oRPehTpjBiOkK%2BClfcLmO0JDh%2FvvkrEcW837BcDf4udI1%2BSCYTxtHEv5FVmRrocUxhSG5ysljkQ8fbk5G0Rl3vJahvZp%2B4m%2BijZlzVnwblMGaWnHT%2F8XqWDZNWXbQdrec0%2FvawgD0kQr7h3QT6xONcV0pEkuip6gKClBvT5ljzOTLi7uDJMTrsuyyPlfQ3scLHl%2FoREAVTiRAkCx%2BhV956JYLEumjRrigFiQ7YZZj%2BR0GB7p3nD9YITqAJCbfGq8btay6C2rV73l8XL0Tcsm8I%2FOegKOOZ8Mfpx6PHxZxgGoa%2FUMu47f1DZ57ZeiXzS0Ax98F2e987mip7Awo81f%2BHI6jYJAb2mZdhYBCGYG7hJXw1CRXcEieznQroelZFMNUb0TQvIW1%2BmkUfcBeRS%2Bf5XX2y7bAu%2FRpmTf1OrkP0%2BH0LsUe8b%2BmhIecVhnetlYZhsraNiSONM1DcIStznzMMfv2cwGOqUBaKMYcGhX%2FRNRdn4S%2F8M9LCMPBFuhuNH2%2FzNhuv3yFmIhuO6GySUu%2BwD7PvA%2FuEVeQP5r3iR2xlSOtlhNsRbbCNxWmNdUQO8VAxvIgmw04x%2BZHqxg5VMqCcIPlc2lk2qZyMbYQ8pBvn8F9%2BAlAN96dzeVQFuzuH5VEw5j3ry8qv%2FLkO%2FGammyKC8i6Hu8OvX382qK45xaIXSBxfzIGBZqKvRYwaJy&X-Amz-Signature=a0cc6cd45fa8a356b81e53013db3b3e07b0ac1181fe62e99813192a692a2ca34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# work detail

1. develop the DAOProxy2
  1. new version DAOProxy2 
1. upgrade DAOCommittee_V1
  1. apply storage DAOProxy2
  1. function summary
    1. increaseMaxMember (onlyOwner)
    1. setActivityRewardPerSecond (onlyOwner)
    1. createCandidate (anyone)
    1. createCandidate (onlyOwner)
    1. registerLayer2Candidate 
    1. registerLayer2CandidateByOwner 
    1. changeMember
    1. retireMember
    1. setMemoOnCandidate
    1. setMemoOnCandidateContract
    1. decreaseMaxMember (onlyOwner)
    1. setBurntAmountAtDAO (onlyOwner)
    1. onApprove
    1. setQuorum (onlyOwner)
    1. castVote
    1. endAgendaVoting
    1. executeAgenda
    1. setAgendaStatus (onlyOwner)
    1. updateSeigniorage
    1. claimActivityReward
    1. payCreatingAgendaFee
1. upgrade DAOCommitteeOwner
  1. apply storage DAOProxy2
  1. function summary
    1. setSeigManager
    1. setTargetSeigManager
    1. setSeigPause
    1. setSeigUnpause
    1. setTargetGlobalWithdrawalDelay
    1. setTargetAddMinter
    1. setTargetUpgradeTo
    1. setTargetSetTON
    1. setTargetSetWTON
    1. setDaoVault
    1. setLayer2Registry
    1. setAgendaManager
    1. setCandidateFactory
    1. setTon
    1. setWton
    1. setActivityRewardPerSecond
    1. setCandidatesSeigManager
    1. setCandidatesCommittee
    1. setCreateAgendaFees
    1. setMinimumNoticePeriodSeconds
    1. setMinimumVotingPeriodSeconds
    1. setExecutingPeriodSeconds
1. need add function
  1. setLayer2CandidateFactory
  1. setLayer2Manager
  1. setTargetSetLayer2Manager
  1. setTargetSetL2Registry
  1. setTargetLayer2StartBlock
  1. setTargetSetImplementation2
  1. setTargetSetSelectorImplementations2
  1. createLayer2Candidate (onlyLayer2Manager)
  1. daoCommittee 컨트랙트에서 ChangedMemo 이벤트 발생시에 이벤트 파라미터를 candidate -> candidateContract로 변경

# Work progress

1. develop the DAOProxy2 - [https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/proxy/DAOCommitteeProxy2.sol](https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/proxy/DAOCommitteeProxy2.sol)
1. upgrade DAOCommittee_V1 (blue - new upgrade function) - [https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/dao/DAOCommittee_V1.sol](https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/dao/DAOCommittee_V1.sol)
  1. createCandidate (anyone)
  1. createCandidate (Owner) → createCandidateOwner (Owner)
  1. createLayer2Candidate (onlyLayer2Manager) → createCandidateAddOn (nameChange)
  1. chagneMember (anyone)
  1. retireMember (onlyMember)
  1. setMemoOnCandidate (anyone)
  1. setMemoOnCandidateContract (anyone) 
  1. onApprove (anyone)
  1. castVote (onlyMember)
  1. endAgendaVoting (anyone)
  1. executeAgenda (anyone)
  1. setAgendaStatus (Owner)
  1. updateSeigniorage (anyone)
  1. claimActivityReward (anyone)
  1. isCandidate (view)
  1. totalSupplyOnCandidate (view)
  1. balanceOfOnCandidate (view)
  1. totalSupplyOnCandidateContract (view)
  1. balanceOfOnCandidateContract (view)
  1. candidatesLength (view)
  1. isExistCandidate (view)
  1. getClaimableActivityReward (view)
  1. getOldCandidateInfos (view)
  1. operatorAmountCheck (view)
1. upgrade DAOCommitteeOwner (red - DAOCommittee_V1 → DAOCommitteeOwner, blue - new upgrade function) - [https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/dao/DAOCommitteeOwner.sol](https://github.com/tokamak-network/ton-staking-v2/blob/NewDAOStructure/contracts/dao/DAOCommitteeOwner.sol)
  1. setLayer2CandidateFactory → setCandidateAddOnFactory
  1. setLayer2Manager
  1. setTargetSetLayer2Manager 
  1. setTargetSetL2Registry → setTargetSetL1BridgeRegistry
  1. setTargetLayer2StartBlock
  1. setTargetSetImplementation2
  1. setTargetSetSelectorImplementations2
  1. setSeigManager
  1. setTargetSeigManager
  1. setSeigPause → 메인넷에 Pause 권한을 지닌 사람은 누구인가? Proxy로 바뀌면서 setProxyPause 이것도 생김
  1. setSeigUnpause → 메인넷에 Pause 권한을 지닌 사람은 누구인가? Proxy로 바뀌면서 setProxyPause 이것도 생김
  1. setTargetGlobalWithdrawalDelay → DepositManager에 던졌으나 에러가남
  1. setTargetAddMinter
  1. setTargetUpgradeTo
  1. setTargetSetTON
  1. setTargetSetWTON
  1. setDaoVault
  1. setLayer2Registry
  1. setAgendaManager
  1. setCandidateFactory
  1. setTon
  1. setWton
  1. increaseMaxMember
  1. setQuorum
  1. decreaseMaxMember
  1. setBurntAmountAtDAO
  1. setCandidatesSeigManager
  1. setCandidatesCommittee
  1. setCreateAgendaFees
  1. setMinimumNoticePeriodSeconds
  1. setMinimumVotingPeriodSeconds
  1. setExecutingPeriodSeconds
1. delete function
  1. registerLayer2Candidate 
  1. registerLayer2CandidateByOwner 

| add function | role |
| --- | --- |
| createCandidateAddOn | A function that can create a Candidate in Layer2Manager. |
| setCandidateAddOnFactory | Setting the address of candidateAddOnFactory |
| setLayer2Manager | Setting the address of Layer2Manager |
| setTargetSetLayer2Manager | Setting the address of Layer2Manager |
| setTargetSetL1BridgeRegistry | Setting the address of L1BridgeRegistry |
| setTargetLayer2StartBlock | Sets the StartBlock of the target. |
| setTargetSetImplementation2 | Change the address of the target's logic |
| setTargetSetSelectorImplementations2 | Set the selector of the target |

| function | role |
| --- | --- |
| createCandidateOwner | A function that can create a Candidate in Layer2Manager. |
| registerLayer2CandidateByOwner | Setting the address of candidateAddOnFactory |
| setAgendaStatus | Setting the address of Layer2Manager |
| setTargetSetLayer2Manager | Setting the address of Layer2Manager |
| setTargetSetL1BridgeRegistry | Setting the address of L1BridgeRegistry |
| setTargetLayer2StartBlock | Sets the StartBlock of the target. |
| setTargetSetImplementation2 | Change the address of the target's logic |
| setTargetSetSelectorImplementations2 | Set the selector of the target |

# How to Test

1. forking the mainnet or sepolia on your local
```javascript
npx hardhat node --fork ~
```
1. setting the .env.example and name change .env
1. if you mainnet forking
```javascript
npx hardhat test test/agenda/12.UpgradeDAOProxy-test-mainnet.js --network local
```
1. if you sepolia forking
```javascript
npx hardhat test test/agenda/13.UpgradeDAOProxy-test-sepolia.js --network local
```

[[Deploy & Setting change DAOStructure & function on sepolia]]

[[How to setting change DAOStructure & function on mainnet]]