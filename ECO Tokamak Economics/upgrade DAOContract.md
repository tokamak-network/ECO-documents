repo : [https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure](https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure)

# DAO Proxy structure change

1. current structure
  1. Since the proxy can only see one logic, the Admin must change it to use other logic.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7ad244b3-33ee-4554-aeb7-5ee8048ff83a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDZ7N37Y%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL8DI%2FHH3%2BF%2B2lV6Obu8xwiPzQPWi%2F2fKQEfPpGFZeBgIhAPMWWAgmPTJiWBGzU0Vd2pfldOH8SdUp8%2BaxlWgIPLc8Kv8DCHoQABoMNjM3NDIzMTgzODA1IgwEQh0XEIOwGb8VAUwq3ANKL%2BMkgOB%2BIphjigNQNd%2BF3%2F5YaQodFiHZREHUBdQuV7LcNORP8SILDk%2FIv17t9CY5m3pwA0CMIHi0eREITOKpxYEmVGkMO%2BJn0pGFl1QbCHx2Iab7TegjxD4nlN4Ux0r573o%2FUuevMFIoh%2B1npb%2B4fF3Cwd6TzLWb%2BK8pBRmeDwkzLKy5%2FSkd23b%2FuextKo%2BzvZf2qcmp5oA8YLj642bnoIn7KBsr6DyCJM%2FdSSrkrlpm9be6lRRPY78CzDZFzEkF7jGNGBGkGObiW5lTFs94WvRv6dQWDTF9uTJ0CQo5uWlGK%2FOR1vh1sQWpMK4yeK4BX5Bt6nmyaRjcRhzYi%2FQX%2BkZulzyhxdjc1nkYOdejsfhRqAPvsriR243hcDYq6v3jCFgEbVb8VcJJN7wzd8n6rB5ZLHCbH1%2BCPGxBVuPv%2BG6KrO2d6spKx0JTsBmU85nNVFlmVucH2%2Fx4AIF7125EckbNj3pHDTVkrGk51Ujemi7YH9sQsULPVzlG%2F%2FLq%2BGV07nEmOeD2xllIJsixR3d0AqOxXiauFVp7QKYb8HIoXN6BOh5CZ5MWBjUXCWNH5J7RALC%2FAqvTX9Yz4a4IgkL0Ky3Ej34djIk%2FoEijjhmAruzn7k6BTI5feo5SoTD%2BmNvMBjqkAcZ6D1ZjzLdO4IHCGAvt%2FA%2BvpEIO8n%2BO2f9WO4eORgUdD1uOvFyPu93oScKTOiCydZbohxH8YlLGZwlqXr9RJ%2BHK3zVSNn6HoOichgjzc1ir3VhECAETiX5VHeGhrMwcBhjxI78S%2BCHAMm9OKEQroFN0l9b4wmh3al36rP0mweHQJVBhKkYi6TNIknEx2djWBAv5k8fkaWnnwoah3BNYO5kguVTI&X-Amz-Signature=08391e3697330e472dfc1f4560f90665bfbea733fcd0a4bbfe992c6c24c3f310&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. structure to change
  1. Changed the structure to one in which a proxy looks at proxy and proxy look at multiple logics.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4d05783e-33d9-4d45-a3e5-e73c929fded5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CANBJNM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHLQB%2FVyeXGTbEWfTL2NUhH9oDzPBSdc2RpXn7YoGtOEAiB4EM9AlFhggkwXGCqL0MaHFBLQ5oUol1KSOK0nWRJzHir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMoDCQt6LoGrQBQ2tbKtwDq0htjwnESlkfVHM%2FR4lhOOPDpqPcaA%2BaB7A2KUIzEu0BaF4prwapMxVo9BWeo%2Bo274oQ%2FxHgEB4cq7M7W5U1HXyqTo1LoOdtiMsRjkdpCsNSMni1TIaQm1WJuc0hAlmy9xVNZ41ot8ZVEub0h8qT6ABCbADLfAnoqbmXglpUrcDQ4wIUDXlfK8oWFQQ5zXzauA3LZyQPApeq8JMBuWzjJa2uiGuRHKMiCLaY%2B50OXTOgLEyyoABHpDD1IchKf9zslsYYRbS69cSvPJlQqWvgUHGY4kYc9Z%2BT%2F92mCoog9Dn%2BEFR%2FFT6VVFs6lOuxa4EmP6qaZjE5%2FGVI2DYu%2B37lvbmV1b9GBWaQBEpD1w41rSh990kOhmzsMkQt%2FsbU4UpTiEVSRNAEBjpO814axpfvQ6Wrk832yXJz0pAOIdg0Pct1pg3L0FfsaGV7mu9UhTR4EuzfoE5AN0GVfGk6qkg%2FuxcepHWpXcNmKsgraNsKm%2FaxXZowEqJngsmex27nn2V6RjD%2Fqh%2Fd9ZlvU5SiWTN9h%2BH%2FWf92aLKDvCzzT5ePcviF%2FaHqtQHf9mlxJvVBv1UKvYhKqsngTuWqTdxqP7s6%2FrH%2FSYawlg1Gf%2Bfi2Ux5Xg%2B0wwcY1TvcBxr78Rsw9JrbzAY6pgFTA97l4mQyjJlhDvGpI0Ca5Kbwn0yRgd5ceNhD03sxcYgUu6JcmYyi%2FSkcX2LlEe0lkld5x9nG9c%2Bkml8Y%2B6%2BciXsXHSnkHFqYJ7Cp%2FyTpY6YUVIRO4H0wmXFp2KwR9PRk90tC9PgRbN7ifEEaII6neh5Lu%2FZsP8lFXCzIDgNSKHlbtzNSjmLYKEEN%2FLrc6QGi9KK3RvA%2FpgkimMJLGWrJgeQek%2FLy&X-Amz-Signature=c8e6547140b431087d010421f82b575b039d50bd62d4bf97cba5623bbee61792&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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