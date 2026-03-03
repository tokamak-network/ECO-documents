**업데이트 시뇨리지 실행시, L2  TVL에 따라 L2 시퀀서에게 시뇨리지를 배분해야 한다.**  

- **업데이트 시뇨리지 실행  **
  - **사용자가 업데이트 시뇨리지를 실행할때 L2 시퀀서에게 제공하는 시뇨리지 분배가 같이 이루어진다. **
  - [draw](https://app.diagrams.net/#G1wKnYpwnyX4zuUlNhUlYcU2MGK4vdfZ1k#%7B%22pageId%22%3A%22WHy0HBHsAwfnHHUYGA3b%22%7D)

![](images/2bbcf62b5e94.png)

  - **확인 1:  시뇨리지 부여 시작 시점 . **
 현재 블록 >  layer2StartBlock (레이어2 시뇨리지 발행 시작 블록) 

    - 1 이면, 중지 
    - 1 이 아니면, 특정 블록이후 실행한다. 

![](images/b6db0edf31e6.png)
  - **확인 2:  현재 레이어 layer2의 업데이트 시뇨리지 실행시,  시뇨리지 발행한 블록 이후부터 layer2 갱신 금액이 반영되어야 한다. **
    - 즉, 위에서 첫번째 A 레이어 업데이트 시뇨리지 시점이후, A레이어의 TVL이 반영되기 시작하는 시점은 T2부터 반영되기 시작해야 한다. 
  - **로직 1: L2 전체 시퀀서에게 발행하는 금액 계산 **
    - L2 전체 시퀀서에게 발행하는 금액 (l2TotalSeigs) 계산시,   **현재 레이어 layer2 의 상태가 이전 데이타로 반영되도록 한다. **
      - **l2TotalSeigs** = rdiv(rmul(maxSeig, oldTotalLayer2TVL*1e9),**tos**);
      - oldTotalLayer2TVL 의 갱신없이 l2TotalSeigs 을 반영한뒤, 
      - layer2Manager에게 민트한다. IWTON(_wton).mint(layer2Manager, l2TotalSeigs); 
      - newTotalLayer2TVL = oldTotalLayer2TVL - oldLayer2Tvl + curLayer2Tvl 모든 업데이트 로직이 실행된후, 종료되기 바로 직전에 갱신한다.  
  - **로직2 : 해당 Layer2에게 발급되어야 하는 리워드 계산  **
    - 변수 정의 
      - l2RewardPerUint** : layer2TON 하나당 지급되는 시뇨리지 양 **
**l2RewardPerUint += l2TotalSeigs / oldTotalLayer2TVL; **
      - **struct LayerReward **
        - **layer2TVL** : 해당 레이어의 TON TVL  
        - **initialDebt : 최초 리워드 시작시 이전에 반영되지 않아야 하는 시뇨리지 양을 계산 , 빚으로 인지하여, 받아야 하는 시뇨리지 계산시 빼주어야 한다. **
          - initialDebt =** curLayer2Tvl * l2RewardPerUint **
      - **reward amount of Layer2 = l2RewardPerUint * layer2TVL - initialDebt **
      - **oldLayer2TVL  : 업데이트 시뇨리지 실행 시점에 이전에 저장된 layer2TVL **
      - **curLayer2TVL : 업데이트 시뇨리지 실행 시점에  조회한 layer2TVL **
    - 로직** 절차 **
      1. **l2RewardPerUint**  업데이트한다. 
        1. **l2RewardPerUint += l2TotalSeigs / totalLayer2TVL;**
      1. 이전 TVL보다 줄었거나, 오퍼레이터가 직접 업데이트 시뇨리지를 실행한 경우라면,  현재 시점의 리워드 계산하여, 정산한다. **Layer2Manager 에서 보관하고 있는 시뇨리지를 오퍼레이터 컨트랙으로 보낸다. **
        1. **reward  = l2RewardPerUint * layer2TVL - initialDebt **
        1. **transfer (reward)  from Layer2Manager to OperatorContract**
        1. initialDebt = curLayer2Tvl * l2RewardPerUint
      1. layer2TVL 현행화 = curLayer2Tvl
      1. 최초 로직실행시 (initialDebt == 0) 
        1. initialDebt = layer2TVL * l2RewardPerUint
      1. totalLayer2TVL 현행화 
        1. totalLayer2TVL = totalLayer2TVL - oldLayer2TVL+ curLayer2TVL; 
      1. **실행자가 오퍼레이터이면서, 스테이킹 또는 클래임 옵션을 선택한 경우 **
        1. 스테이킹을 하는 것으로 선택했을 경우:  DepositManager 에 OperatorContract 계정으로  OperatorContract 이 보유한 wton 을 스테이킹한다. 
        1. 클래임을 선택한 경우 :  OperatorContract 컨트랙의 manager에게 ** **OperatorContract 이 보유하고 있는 wton을  보낸다. (톤으로 바꿔야 하는가?) 

2. 추가 스토리지 

1. 특정 Layer2가 유효한지 확인
  1. L2Registry에 유효한 Layer2인지 조회 
1. 특정 Layer2가 유효하지 않을때, 
  1. layer2TVL ≠ 0 
    1. totalTVL = totalTVL - layer2TVL  
    1. layer2TVL = 0

##  

# SeigManager 함수

| 함수이름 | 권한 | 로직번호 |
| --- | --- | --- |
| pause | onlyPauser |  |
| unpause | onlyPauser |  |
| setData | onlyOwner |  |
| setLayer2Manager | onlyOwner |  |
| setPowerTON | onlyOwner |  |
| setDao | onlyOwner |  |
| setPowerTONSeigRate | onlyOwner |  |
| setDaoSeigRate | onlyOwner |  |
| setPseigRate | onlyOwner |  |
| setCoinageFactory | onlyOwner |  |
| transferCoinageOwnership | onlyOwner |  |
| renounceWTONMinter | onlyOwner |  |
| setAdjustDelay | onlyOwner |  |
| setMinimumAmount | onlyOwner |  |
| setSeigStartBlock | onlyOwner |  |
| setInitialTotalSupply | onlyOwner |  |
| setBurntAmountAtDAO | onlyOwner |  |
| renounceMinter(address target) | onlyOwner |  |
| renouncePauser(address target) | onlyOwner |  |
| renounceOwnership(address target) | onlyOwner |  |
| transferOwnership(address target, address newOwner) | onlyOwner |  |
| deployCoinage | onlyRegistry |  |
| setCommissionRate | onlyRegistryOrOperator(layer2) |  |
| slash | onlyChallenger |  |
| onDeposit | onlyDepositManager |  |
| onWithdraw | onlyDepositManager |  |
| **updateSeigniorage** | anyone |  |
| onTransfer | anyone |   |
| updateSeigniorageLayer(address layer2) | anyone |   |
| additionalTotBurnAmount |  | view |
| uncommittedStakeOf
(address layer2, address account) |  | view |
| uncommittedStakeOf
(address account) |  | view |
| unallocatedSeigniorage |  | view |
| unallocatedSeigniorageAt |  | view |
| stakeOf
(address layer2, address account)  |  | view |
| stakeOfAt
(address layer2, address account, uint256 snapshotId) |  | view |
| stakeOf(address account) |  | view |
| stakeOfAt(address account, uint256 snapshotId) |  | view |
| stakeOfTotal |  | view |
| stakeOfTotalAt(uint256 snapshotId) |  | view |
| stakeOfAllLayers |  | view |
| stakeOfAllLayersAt(uint256 snapshotId)  |  | view |
| registry() |  | view |
| depositManager() |  | view |
| ton() |  | view |
| wton() |  | view |
| powerton() |  | view |
| tot() |  | view |
| coinages(address layer2) |  | view |
| commissionRates(address layer2) |  | view |
| isCommissionRateNegative(address layer2) |  | view |
| lastCommitBlock(address layer2) |  | view |
| seigPerBlock() |  | view |
| lastSeigBlock() |  | view |
| pausedBlock() |  | view |
| unpausedBlock() |  | view |
| DEFAULT_FACTOR() |  | view |
| progressSnapshotId() |  | view |
| totalSupplyOfTon() |  | view |
| totalSupplyOfTon_2() |  | view |

# Test 1 

repo : [https://github.com/tokamak-network/ton-staking-v2/tree/L2Seigniorage](https://github.com/tokamak-network/ton-staking-v2/tree/L2Seigniorage) 

[code](https://github.com/tokamak-network/ton-staking-v2/blob/L2Seigniorage/test/layer2/units/2.Layer2Manager.mainnet.test.ts) 

`npx hardhat test test/layer2/units/2.Layer2Manager.mainnet.test.ts`

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/33230744-fa04-4191-97d9-b9b6a7648897/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.12.04.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=acfa0eba18edc048d7706cfe26bd484d8dda3c52043cb3af005d93b35784eb86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a5627154-a579-4e3f-be45-3528a095c2cb/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.12.18.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=9be3bdd2c2a6f467eb328f9a143b7880b4a7367a9dc9037845ab3a3184afe572&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c24fca22-c604-4545-8de0-f66108b9585a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.13.08.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=654437b478a05434ee46451419f87ca3f758414abf4185c087adb9d4ec5f37f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ba8f588f-ad6d-441f-b264-177e8b3d1c23/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.13.14.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=d1152de8bba9c48179af87a39c82ae3374d3f83e6035e42ae1a3d319df7e6043&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/08bc39ed-0591-4907-8ffa-257caacfa80a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.13.25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=d5a7bb1ff3f283e56212df3c871d643fb5a02d45876a401b7fadfff0e54307bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/5f0cf07f-13fd-4074-bb4e-c443d739c8e9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-04-10_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.13.33.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PPDCFL3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE3rhTcWs9HGzty0tYy%2Bp%2BB9NuzoC03W59rJezEQIdOgIgOVfPsPZR%2FZZUCttCLE7vP0DAZetWAPAxOXUfRn0XMUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAekC60TQ2OlimqTXCrcA8Qq8n87hyvEuOZLqEklep8nuq3kr6ndGm%2FhmI5zlANzpQ6BG99sPrw%2Fyl3wyix0AIWUV%2FI%2BMOBM0xrY%2F3SSJgUFfNE0C8hEy6CabsRZXGrAUiY1RUihpE89DquZs8b4r%2Fs6kpjmAMRRB95M9hWYA1mrwzGz7bWqh0zoJXuOOQ9Syzo2fjtC5aTg67Zh0jjajDK%2BOtmyJauvlwK5dk0cboc9qTRwAmPKT7pWc%2B5%2BIRbeNteDyCJAvCP%2BA4ziWxS23JZnSYPcHvEN9lYIPvV4OaaFNje5icXdQiZHXDch7%2B0gFQ51uc2mrzYsK8Q21wACpFvSX5vPA%2BTfs1YPMqa%2BwBZWgarO%2F88V1mjF%2BsqwFLwMDxEx6rfzLE%2BniCFiVLnJSa3gwISk1q88yvIzolM0GVu9Wa%2FVSKVagd1sy7LTCiZB%2BfZpZIGmz6TveBfCkaUaaVg4iqGM1aGNkPer%2FIS%2FBeHL4CYGQfP8jAlit%2FNb%2BtTi7Yp3D0Vj%2FE6kXREis2oSoskoS0QrhDwBbuQ9925m7f2xbY%2Bs4Jbv%2BryNoq%2Fwi%2F4O4Tsfz07HtAjXYLflP8LDi4FaB%2FfcYdcahvzy5ZYP6Sa9ttSLxsBMPYexxX4v1NGcCmFTL0mt4%2BLTyB8FMKeZ28wGOqUBMjydbcfKtPR5ak2Dr8yXGVUcJaEyjbLC6wm8eP2fMN0rz3bpVGqr%2F1Ctnt%2Ba5ay4fiEs1lKVic89iCHrzGYcWNFMtqAwU2icvrQDU0DnhknGjB3wkdWEJcQK67lkfc6rM1Nme1dQuA4PM5Q1YrlOUcqo5uxegAOw3B09wTpRBeWCTP3synljwgfXSPJE%2FY2NfMLLgB3vbQXrHUN%2BRRHdKeJQGncf&X-Amz-Signature=b7943e32fe761224655e5a43374b3a10bd0fd0d9d5aec64486b86e5491adbc13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)