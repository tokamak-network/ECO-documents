# Modeling

[https://docs.google.com/presentation/d/1Z75lrEYQPvqOXZ_hRMqLystM6jEbGo01aTg36VZNutU/edit#slide=id.g221d1e26ab8_0_443](https://docs.google.com/presentation/d/1Z75lrEYQPvqOXZ_hRMqLystM6jEbGo01aTg36VZNutU/edit#slide=id.g221d1e26ab8_0_443)

[https://docs.google.com/presentation/d/1yC9X9xQ_hwVoKtll-c2S3BLSpchf05kTmeCTSmWcQTw/edit#slide=id.g21241b56341_0_54](https://docs.google.com/presentation/d/1yC9X9xQ_hwVoKtll-c2S3BLSpchf05kTmeCTSmWcQTw/edit#slide=id.g21241b56341_0_54)

[https://docs.google.com/presentation/d/1SNzrypW7bgNjuZRJ9kGqAsdRV-JtkMaFq5U1PZNoC3I/edit#slide=id.g25063a2f3b1_0_20](https://docs.google.com/presentation/d/1SNzrypW7bgNjuZRJ9kGqAsdRV-JtkMaFq5U1PZNoC3I/edit#slide=id.g25063a2f3b1_0_20)

# Design Contracts

[https://app.diagrams.net/#G1ONFWgNCMvdVrH5tV7IE-e27hxrJZAGZJ](https://app.diagrams.net/#G1ONFWgNCMvdVrH5tV7IE-e27hxrJZAGZJ)

# Which tokens are staked? 

TON~~?  or WTON ? ~~ 

# How to set DAO address ?

- Admin 권한
- OnlyOwner ( = Only Admin) 현재는 다오만 권한들을 갖고 있음 (로직 변경 안됨) ⇒ (현재는 케빈 및 DAO가 권한을 가지게끔 설계할 계획)
  - ex1) 시뇨리지 분배 비율 ( DAO , sTOS holder, Staker. ) 
ex2) max ( minimum security deposit , **ratio** *TVL)
ex3) 컨트랙 로직 업그레이드 / 컨트랙 일시 중시 권한 (현재 안됨)
ex4) 블록당 시뇨리지 개수 변경 (현재 안됨)
ex5) 다오나 sTOS 홀더에게 지급하는 시뇨리지 주소 변경
ex6) maximum 레이어 2 개수 제한 (현재 안됨)
ex7) candidate minimum deposit 금액
ex8) 입/출금 할 때 시간 조정
- <u>방법1 : 다오주소에게 Owner 권한을 주는가? 다오를 제외한 다른 Owner는 없게한다</u> 
  - OnlyOwner가 여러명일수있다. 
  - 다오에게 어드민 권한을 준다.
  - 어드민 권한을 가지고 있는 사람들이 다른 사람들에게도 줄 수 있음 
- 방법2 : 다오만 OnlyOwner , 다오 변경시 → OnlyOwner권한을 위임. 
  - 절대적으로 OnlyOwner는 한명이어야함. 
- <u>방법3 : 정책적인것과 운영적인것을 분리 </u>
  - 운영은 어드민 권한 (로직 업그레이드) (운영 권한 여러명한테 줄 수 있음⇒올림푸스 다오 리서치)
    - 권한을 통째로가 아닌, 조금조금씩 이양할 수 있게끔 (뺏는 것도 가능하게끔)
  - <u>**정책은 다오권한 (1계정)**</u><u> </u><u>: 다오주소를 다오권한 계정으로 지정 (정책 권한은 위임만 가능)</u>

Do you manage DAO addresses separately? Do you set the admin as DAO?

> [!note]
> 5️⃣ **How to set DAO address? **
> - Admin Permissions?
> - OnlyOwner (=Only Admin) Currently, only DAO has permissions (no change in logic) ⇒ (plans to design it so that Kevin and DAO to have permissions)
>   - ex1) Distribution ratio of seignorage (DAO, sTOS holder, Staker. )
> ex2) max (minimum security deposit, **ratio** * TVL)
> ex3) Contract logic upgrade/contract temporary emergency authority (currently not possible)
> ex4) Change the number of seignorage per block (currently not possible)
> ex5) Change the seignorage address to be paid to DAO or sTOS holders
> ex6) Limit maximum number of layer 2s (currently not possible)
> ex7) Candidate minimum deposit amount
> ex8) Adjusting the time when deposit/withdrawal occurs
> - Method 1: Give Owner permissions to DAO address? No other Owner except DAO
>   - There can be multiple OnlyOwners.
>   - Give admin permissions to DAO.
>   - People with admin permissions can also give them to others
> - Method 2: Only DAO is OnlyOwner, if DAO is changed → Delegating OnlyOwner permissions.
>   - OnlyOwner must be one person.
> - Method 3: Separate policy and operation
>   - Operation has admin permissions (logic upgrade) (can be given to multiple people ⇒ OlympusDAO research)
>     - Permissions can be transferred a little at a time, not all at once (can also be taken away)
>   - **Policy has DAO permissions (1 account)**: Designate DAO address as DAO permission account (policy permissions can only be delegated)

# **Where are assets stored? **

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/cbf38ce6-007f-48b5-a0b3-2b320e274bc2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-03-29_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.11.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPTHXQEM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMEIgoqh3Z%2FwzsNkOQqsd9omhuz5yT8MJbPBbmT3CloAIhAJ44E9kUsM4FSOKD4c9kRbs3iRZjWYaaNgi33Nth7vB%2FKv8DCHoQABoMNjM3NDIzMTgzODA1IgyEmdDK73QziFYHt6Aq3AN6BkrtI%2BJsEti4xRe9cNa0hoAGh%2B1PZ3XbePpPEQywEjXw%2FW%2BRLoytEFzcu6PwmND37GL5kXEgwlsD48e3iKhmWZWMKXK0iNp7J4pInE6%2Fhs1PDeQWKFspbk2doFtljP8kat8bpxoLSNuxpPo7CvVAG%2FtcZaL9g65GFmGhNvn8rFXCjdsrQyq9A%2BLj5mwWj6RdjMVeRJzDQGGJOYxltm9F%2BMMWxAOpSA3cZb8DO1COFKdjILwl3MPFWxZ0d4TwzOiVCmSvNcsZCQW5DhZYrq1YoC3QM7eHei0SbgVv%2BlOUgb22UxCcN4XD7XGkXMhcEtOuo4befezw4%2BDQhBt9ZCuYluIY6gsWHKobhhg%2FdSVPgHn6XXivFT%2FX5K45y4uXYYIPRwI21KMHYwoOmZpr5RzhonHo%2F9Y1Xw79B7s9H7ST1L3djEh%2BlM9cX9PaPVpdOb0NnY0gSvYX%2F%2BHiejWGxIBeDJO%2F%2Fm2HpEB4FeH78svu3Q%2B2V701iwkRtTweko1MgDZzxb78zumZdpliH1W50IXoTLcT3oRpeD3%2FPWKuDhx7X%2BgnVFbK4BHTHK4PqJeVIZZNipUiPaWkNLJlMtc4IsZsDlZsXJyAFFyrk90zTLshPIxKiviO2%2FxWIPdzwjCfmdvMBjqkAaXXmFomlPbYEkWbdyC8TiFncJG1hJHD0OhjLYAacecYg3oGgluiAnGeKPnEyNBHhiT6Qa62ih5wcbG6HHv5BxiJM3IKxfhzug1Wq1u32onaPeDFkmiiNRq5sT8DSdM66i%2FxEX0WNJBdgVx0aHXO5Tzx0eL1iDkNlsAWFc6ZcTgvDmmgQ0ld7CO7XDK4TWkkFGlWusn8LphqTF4ua52z7xF0CKnC&X-Amz-Signature=5119e02a3d99508f43a806329c5dc7a45d7730aff6ddbb2c3a058c49c175a1cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Seigniorage  : **SeigManagerV2**
  - The seigniorage update contract is SeigManagerV2
- Security deposits of sequencers : **Layer2Manager** 
  - The contract that manages information of all sequencers and candidates is Layer2Manager.
  - The subject that creates sequencers and candidates is Layer2Manager.
-  TON staked to ~~sequencer~~Operator : ~~**Sequencer**~~ Operator
  - Users use Operator contracts when staking on Operator.
  - If staked TON in operator contract is insufficient when user withdraw amount, operator contract send user's claimed TON to user through it claim the insufficient TON amount to SeigManagerV2.
- TON staked on candidates : **Candidate** 
  - When users stake candidates, they use the candidate contract.
  - If staked TON in candidate contract is insufficient when user withdraw amount, Candidate contract send user's claimed TON to user through it claim the insufficient TON amount to SeigManagerV2.

# Who can become a DAO committee

[link](https://docs.google.com/presentation/d/1Z75lrEYQPvqOXZ_hRMqLystM6jEbGo01aTg36VZNutU/edit#slide=id.g221d1e26ab8_0_450)

- ~~Sequencer~~ operator
- Candidate

## operator (optimismL2Operator)

**“****OVM_TONStakingManager****”**

** **

- Operate the actual layer 2.
- Required information of layer 2 operating contract address .
- Layer 2 type (Currently supports only Optimism. ) => (optimismL2Operator)
- Supports staking function. (It can be used as liquidity for fast withdraw.)
- Supports layer 2 fast withdrawal. ( in case of optimism type ) 
- The ~~sequencer~~ operator must deposit the minimum security deposit according to the TVL of Layer 2 
  - If the minimum security deposit is not deposited, operator can’t be provided the seignorage.
  - **`Amount of minimum security deposit = max ( fixed minimum security deposit, TVL * ratioOfDeposit ) `**
⇒ ratioOfDeposit is determined by DAO. Initial setting is 0%  

 

## Candidate

- Supports staking function. (It can be used as liquidity for fast withdraw.)
- Supports layer 2 fast withdrawal. ( in case of optimism type ) 
- candidate staking over minimum stake amount when creating. 
  - This minimum stake amount can not be un-staked.  
- Commission for staking can be set. default is 0. If there is a commission, the commission is collected when staking.

# Create OptimismL2Operator

- Registering a Optimism Layer2 . 
  - Layer 2's operator can create optimism layer2.
  - input data 
    - name <string>
    - **addressManager** <address>
    - ~~L1Messanger <address> (⇒ 필요 없음, 대런)~~
      - ~~addressManager.getAddress(”Proxy__OVM_L1CrossDomainMessenger”)~~
    - L1Bridge <address> : fw 로직에서 사용하려고 저장해둠 
    - L2Bridge <address> : fw 로직에서 사용하려고 저장해둠 
    - L2Ton <address> 
    - security deposit  : This must be greater than the minimum  security deposit.
  - security deposit 

# Create Candidate

- Registering a Candidate of a special layer2 . 
- input data 
  - name <string>
  - Layer 2 (OptimismL2Operator’s index) 
  - commission 
- Caller becomes an operator of candidate. 
- minimum deposit (staking)  

# Update Seigniorage 

## The timing of ‘seigniorage update’ execution.

### minimumBlocksForUpdateSeig (unused now)

The block period for seigniorage execution is set in advance. (minimumBlocksForUpdateSeig)

### ~~automatically executed ~~

~~During a user's transaction (staking, unstaking), if the minimumBlocksForUpdateSeig block has passed since the latest seigniorage issuance, the seigniorage update is automatically executed.~~

### Ready to run if you want

minimumBlocksForUpdateSeig If you want to run seigniorage update immediately regardless of the period, you can run **SeigManagerV2.runUpdateSeigniorage()** function.

## The amount of issuing seigniorage

The amount of seigniorage issued when all seigniorage is executed is calculated as 

***= The seigniorage issuance per block  * The number of blocks that have passed since the last minting issue***

## Distribute seigniorage. 

1. Update indexLton. (Reflects seigniorage for stakers )
1. Provides seigniorage for operators.
1. ~~Provide seigniorage for DAO.~~
1. ~~Provide seigniorage for sTOS holders.~~
 [link](https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_2_dao_committee/contracts/SeigManagerV2.sol#L206-L246)

### The sum of (ratesDao, ratesStosHolders, ratesStakers) 

- **`It must be One`****. **   

### Definition of item D when calculating the seignorage provided to the operator

1. update Seig : D → ** total security deposit **of operators 
When updating the seigniorage, it seems good to base it on the total operator collateral (the amount specified here as D or Deposit).
This is because there doesn't seem to be much practical benefit to be gained by updating while going through the process of checking whether the minimum operator deposit amount is met.
1. distribute :  
  - **`distributed amount of special `**`operator = (security deposit + TVL of special layer) / sum (security deposit + TVL)`**` `**
  - **Conditions** of layers that can receive seigniorage :    
    - The operator's security deposit must be greater than **`the minimum security deposit`**.
  - **`minimum security deposit`**` = `**`max ( fixed minumum security deposit, TVL * ratio ) `**

# Seigniorage for operators.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f94dd22f-fd54-429a-a4b0-e88ec5b875c0/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-03-17_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.15.37.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPTHXQEM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMEIgoqh3Z%2FwzsNkOQqsd9omhuz5yT8MJbPBbmT3CloAIhAJ44E9kUsM4FSOKD4c9kRbs3iRZjWYaaNgi33Nth7vB%2FKv8DCHoQABoMNjM3NDIzMTgzODA1IgyEmdDK73QziFYHt6Aq3AN6BkrtI%2BJsEti4xRe9cNa0hoAGh%2B1PZ3XbePpPEQywEjXw%2FW%2BRLoytEFzcu6PwmND37GL5kXEgwlsD48e3iKhmWZWMKXK0iNp7J4pInE6%2Fhs1PDeQWKFspbk2doFtljP8kat8bpxoLSNuxpPo7CvVAG%2FtcZaL9g65GFmGhNvn8rFXCjdsrQyq9A%2BLj5mwWj6RdjMVeRJzDQGGJOYxltm9F%2BMMWxAOpSA3cZb8DO1COFKdjILwl3MPFWxZ0d4TwzOiVCmSvNcsZCQW5DhZYrq1YoC3QM7eHei0SbgVv%2BlOUgb22UxCcN4XD7XGkXMhcEtOuo4befezw4%2BDQhBt9ZCuYluIY6gsWHKobhhg%2FdSVPgHn6XXivFT%2FX5K45y4uXYYIPRwI21KMHYwoOmZpr5RzhonHo%2F9Y1Xw79B7s9H7ST1L3djEh%2BlM9cX9PaPVpdOb0NnY0gSvYX%2F%2BHiejWGxIBeDJO%2F%2Fm2HpEB4FeH78svu3Q%2B2V701iwkRtTweko1MgDZzxb78zumZdpliH1W50IXoTLcT3oRpeD3%2FPWKuDhx7X%2BgnVFbK4BHTHK4PqJeVIZZNipUiPaWkNLJlMtc4IsZsDlZsXJyAFFyrk90zTLshPIxKiviO2%2FxWIPdzwjCfmdvMBjqkAaXXmFomlPbYEkWbdyC8TiFncJG1hJHD0OhjLYAacecYg3oGgluiAnGeKPnEyNBHhiT6Qa62ih5wcbG6HHv5BxiJM3IKxfhzug1Wq1u32onaPeDFkmiiNRq5sT8DSdM66i%2FxEX0WNJBdgVx0aHXO5Tzx0eL1iDkNlsAWFc6ZcTgvDmmgQ0ld7CO7XDK4TWkkFGlWusn8LphqTF4ua52z7xF0CKnC&X-Amz-Signature=c3d1429b72f508d564a3cff7a21d8d74dbfc8382c761eb46e58e20c56f48b05a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### STEP 1. If we execute “update seigniorage”,

The seigniorage amount added to the totalSeig storage of Layer2Manager is reflected.

- **The more layers there are, the higher the gas cost. This is because the TVL of all layers 2 is retrieved.**
- [link](https://github.com/tokamak-network/tokamak-staking-v2/blob/274f0b3c7fc66eb04dc62022be6e42c20cd8dd1e/contracts/SeigManagerV2.sol#L111-L164) 

### STEP2. **Layer2Manager.distribute() **

Execute the **Layer2Manager.distribute() **function to distribute the seigniorage to each sequencer.

- The amount distributed varies depending on the time of distribution. operator can try to use this. However, if operator deposits in L2, it takes 2 weeks to withdraw,
If operator make it impossible to withdraw the deposit even if you add a deposit, it will be difficult to abuse.
- **The more layers there are, the higher the gas cost.** This is because seignorage is distributed to all layers 2 one by one. At the time of distribution, query the holding amount of layer 2 because Layer 2 holdings are not separately managed.
- [link](https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_2_dao_committee/contracts/Layer2Manager.sol#L219-L250)

### STEP2. **Layer2Manager.claim(layerKey)**

When the claim function is called by specifying a specific layer, the allocated seigniorage is transferred to the operator of the layer.

# Minimum security deposit of operator

- Formula 
  - Fixed at first. `fixed minimum security deposit  amount` ex) 1000 TON 
    - DAO can change  the `fixed minimum security deposit`.
  - DAO manages `minimumSDRatio`.  
    - DAO can change to at least a minimum percent of TVL  (`minimumSDRatio`) (ex) 0.01 (1 %) 
    -  **default 0% ** 
  - `minimum security deposit` = max ( `fixed minimum security deposit`, `TVL of layer * minimumSDRatio` ) 
- **the penalty when **operator** fails to provide the ****`minimum security deposit amount`**** **
  - **Update seigniorage not receiving seigniorage to **operator

# stake 

User can stake by selecting a specific layer2.
If user stakes, user receives the lton that divide the staked amount into indexLton. 

As user receive seigniorage, indexLton increases, so we can know the user's staked amount applied seigniorage.

# unstake

When user runs the unstake, the requested amount **will be available for withdrawal after the delayBlocksForWithdraw block.**

# restake

This is a function that allows you to re-stake requests that have not yet been withdrawn.

It can be seen as a concept of canceling the unstake. This is to cancel unstake with unstake requests count not unstake amount.

# withdraw 

When user executes a withdrawal, all withdrawable amounts are withdrawn immediately.

# Fast Withdraw 

 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/904facb8-bd00-4a32-af87-338b4b6682b8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-02_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.14.57.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEQTK72Z%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXv2U6UyC1w2itHo0JVWZTH8WrHumx9rur2wsIR1dCMAiEAruWeT4VTQ6lo4yGfJF58BpkkpLtmHfFvXhjcipaoV0Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDPhdJx8K7i1%2FOcGu1ircA8n%2FX2LVhHZX9GxMrJZKCvdsOvzkRTccGpNS%2BY0F8jgecdnCvJ6wfGjYy9TU9M7vv5EEKW6IWVfunNZh%2FDe0avRjaUHejKi5DKpf%2B3FwH4o5GjLNcqeboylEm2Qiv5iELtVwWQD2IEPdMwfgbwcuDgupZBbPfEpwcFPiWqbCcnN9IS6LiZIP2jt%2BFccJA5VekTfP2%2BoFPWfbc37z8WnnsgR221oxCYJr9YNHbZXBnFFHhwAs8tAM3r0U2ug1AYb79pjSNjH9%2FmOxWuldTwKGXmAk3L1zJUUIuRRDShJKhF3kaNL8ObpUXMsHSx261EsWF%2BO8mjYX167rrHcn3LtEzebkDdJzTskS8%2BE%2Bej9eu0Ho54itfwR%2Bk7RiRI3Jt8NeJX62ebbEDeGNkLdnoMJfjVE5%2FGtjtgqISTx4fVnNjG%2FF6rYqnOteQLSP%2B65qyCCYC%2B360XD9spBB%2FXTZzeQjHbz9DeCWzXn5TGPyooU3PbBoom7zow0Sf9riI4fFuF2pAOlpKABY655SLx70Rf0kOq5AmosnGFAuXsvwKjeQftX1Xnhqhc3%2FaaKydt7CyjbL9rbNl51wvf6IgY%2B5VptPT5gRT5JpQpO3kImaPukwqG83oKDGCYgsyYs%2Bl8LnMPCY28wGOqUBEBSubu%2FdPaz%2FnqQS9%2F%2BNErxykYS9SLkvMB7%2Bp3gJD7XnupmE%2BZnuC2vzNibwB9EOE0trx2asu8WzsjnJ10aI9z6OoHgdfBsArIdTd%2B%2BB4CtMuL7w%2F6WIkiIgxyFwgwrFE0JPJRYrUHQuhtvO6Mv%2Beh6ZqHClZ9%2FvmErhoLflm30WFBFI3uCRsxoLXmf5FFSBVzyb4cey3DEyDUzsAb%2B9LY6GR24C&X-Amz-Signature=8a014c826fc83292fbc0f258f474a1dd84f37b23022a35c889ce95732648f934&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

repo : [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_3_fast_withdraw/contracts](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_3_fast_withdraw/contracts) 

## Process  

1 → 2 → 3  

## Step1. Execute Fast Withdrawal (on L2) 

-  L2 TON 보유자는 보유금액만큼 빠른 출금 요청할 수 있다. 
- ~~추후 relayer가 step 5을 실행하기 위해서는 많은 가스비가 필요할수있다. 이 실행 가스비를 relayer가 청구받아야 할텐데..이 가스비를 어떻게 지불하는가?  ⇒ 빠른 출금 가스비 정책 필요 (대런님과 논의) → 이미 가스비를 받으므로, 그냥 사용하면 됨 ~~
- 실행할때 deadline 을 입력한다.  step 2는 deadline 시간내에만 실행가능하다. 
- fee 

## Step2. Provide Liquidity (on L1)

- The L1 liquidity provider must check that the L2 withdrawal execution transaction has been submitted to L1, and must approve the fast withdrawal of (withdrawal amount-fee) to the L2 requestor.
  - If you do not approve, it will not be withdrawn.
  - The approved amount must be the same as the withdrawal amount  (withdrawal amount-fee) submitted to L1.
- L2에서 전송한 메세지(xDomainCalldata) 와 key
  - xDomainCalldata  데이타가 필요하나, 데이타 사이즈가 매우커서, 가스비가 많이 나오므로, 필요한 데이타만 파라미터로 받도록 한다. 
```javascript
function provideLiquidity(
        address requestor,  요청자 주소
        uint256 requestAmount,  요청자의 fw 금액
        uint256 provideAmount,  유동성 제공자가 제공하고자 하는 금액 
        uint32 deadline,        유동성 제공마감 시간 
        bool isCandidate,       candidate 인지 여부 
        uint32 indexNo,         유동성을 제공하는 시퀀서또는 candidate의 인덱스번호
        uint16 feeRate,         수수료 비율 ( 10000 곱해서 사용) 
        uint32 layerIndex,      빠른 출금 요청 대상의 시퀀서 번호 
        uint256 messageNonce,   L2에서 빠른 출금요청시 사용된 메세지 넌스
        bytes32 hashMessage     L2에서 빠른 출금 요청한 메세지 해쉬값 
        )
```
  - ** **hashMessage   
```javascript
encodedRelayMessage = abi.encodeWithSignature(
                "relayMessage(address,address,bytes,uint256)",
                _target,  // L1 브릿지 주소 
                _sender,  // L2 브릿지 주소 
                _message,  // 메세지 
                _messageNonce  // 메세지 넌스 
            )

hashMessage = keccak256(encodedRelayMessage) 

_message = abi.encodeWithSignature(
                "finalizeERC20Withdrawal(address,address,address,address,uint256,bytes)",
                ton,     // L1 톤주소
                _layerInfo.l2ton, // L2 톤주소
                requestor,   // 요청자 주소 
                FwReceiptContractAddress, // FwReceiptContract 주소
                amount,  // 요청금액 
                abi.encodePacked(feeRate, deadline, layerIndex)
            )
```
- 유동성을 제공→유동성제공자가 제공하려는 만큼의 톤을 L2요청자에게 (제공금액-수수료) 만큼 보내줌. 
  - **(스테이킹 금액-이미 유동성제공한 금액) ≥ **(제공금액-수수료) ** 이 있는 계정만이 유동성을 제공할 수 있습니다.  **
  - 유동성 제공을 한 후에는 key에 대한 status = PROVIDED_LIQUIDTY 로 저장. 
  - status 가 0 이거나, status = PROVIDED_LIQUIDTY 일때는 (요청금액-유동성제공된금액) > 0 일때 유동성 제공가능 
- fw수수료는 승인시 사용하는 가스비보다 많게 책정되어야 한다. 어떻게 책정이 될것인가? 비율로 정하게 되면, 출금수수료가 가스비보다 적게 될 수도 있지 않는가?  (⇒ 프론트 단에서 체크해야 할 듯.. 스테이킹 UI)
  - fw 수수료 > 승인시 사용되는 가스비  
- STEP2 : Provide Liquidity 를 실행할 수 있는 상태
  - 참고 
    - [https://github.com/tokamak-network/tokamak-optimism-v2/blob/main/packages/sdk/src/interfaces/types.ts#L126](https://github.com/tokamak-network/tokamak-optimism-v2/blob/main/packages/sdk/src/interfaces/types.ts#L126)
    - [https://github.com/tokamak-network/tokamak-optimism-v2/blob/feature/batch-relayer/packages/tokamak/sdk/src/interfaces/types.ts](https://github.com/tokamak-network/tokamak-optimism-v2/blob/feature/batch-relayer/packages/tokamak/sdk/src/interfaces/types.ts)
      - 변경된 내용: RELAYED_FAILED 타입 추가
  - 상태를 확인하는 자세한 스펙은 코어팀의 가이드에 따른다. 
3af3288c-6d3d-4d71-92ea-4814445a190b 

## Status Transitions 

- Key 별로 Status 를 저장한다. 
- 초기상태
  - NONE  
- L2 요청자가 요청했을때
  - NONE  (L1에서는 사용자가 요청한 액션을 바로 알 수 없다. ) 
- L1 유동성 제공자가 유동성 제공했을때, 
  - PROVIDE_LIQUIDITY
- L1에 요청자가 요청을 취소시켰을때, 
  - CANCEL 
- DTD 이후, L2 메세지를 실행시, 유동성 제공자가 아무도 없었을때, 
  - NORMAL_WITHDRAWAL
- DTD 이후, L2 메세지를 실행시, 취소시킨 요청이었을때,  
  - CANCEL_WITHDRAWAL
- DTD 이후, L2 메세지를 실행시, 정상적으로 정산이 되었을때,
  - FINALIZE_WITHDRAWAL
- DTD 이후, L2 메세지를 실행시,  정산이 실패 되었을 때
  - FAIL_FINISH_FW
- DTD 이후, L2 메세지를 실행시, 보낸 계정이 L1Bridge가 아닐때,
  - NOT_L1_BRIDGE
- DTD 이후, L2 메세지를 실행시, 메세지가 문제가 있을때,  
  - ZERO_AMOUNT  : 금액 데이타 0
  - ZERO_REQUESTOR : 요청자 주소 0 
  - WRONG_MESSAGE : 길이가 맞지 않을때, 
- 

## Step3. Finalize Fast Withdrawal (on L1)

- After the DTD period, check if the L1 liquidity provider has granted an expedited withdrawal.
  - If approved, the amount withdrawn is staked to the account of the L1 liquidity provider.
-  L2에서 전송한 메세지(xDomainCalldata) 를 전달받은 후, 해당 메세지로 key를 생성함. 해당 key에 대한 상태(status)가 있는지 체크해서, 유동성 제공이 되었는지, 이미 제공된 것인지 등을 확인하여 처리함. 
- 누구나 DTD가 지나. 자산이 L2→L1이 이동된 뒤에는 “Finalize Fast Withdrawal “ 기능을 실행해서, 빠른 출금의 마지막 정산 작업을 할 수 있다. 
```javascript
function finalizeFastWithdraw(
        address requestor,  요청자 주소
        uint256 requestAmount,  요청자의 fw 금액 
        uint32 deadline,        유동성 제공마감 시간  
        uint16 feeRate,         수수료 비율 ( 10000 곱해서 사용) 
        uint32 layerIndex,      빠른 출금 요청 대상의 시퀀서 번호 
        uint256 messageNonce,   L2에서 빠른 출금요청시 사용된 메세지 넌스
        bytes32 hashMessage     L2에서 빠른 출금 요청한 메세지 해쉬값 
        )

hashMessage = keccak256(encodedRelayMessage) 

_message = abi.encodeWithSignature(
                "finalizeERC20Withdrawal(address,address,address,address,uint256,bytes)",
                ton,     // L1 톤주소
                _layerInfo.l2ton, // L2 톤주소
                requestor,   // 요청자 주소 
                FwReceiptContractAddress, // FwReceiptContract 주소
                amount,  // 요청금액 
                abi.encodePacked(feeRate, deadline, layerIndex)
            ) 
```
- STEP 3: Finalize Fast Withdrawal  를 실행할 수 있는 상태 체크에 대한 자세한 스펙은 코어팀의 가이드에 따른다. 
- Status 별 처리 , (fwAmount , feeAmount = fwAmount*feeRate)
  - NONE : 0
    - message 가 등록되지 않은 경우 : 유동성이 제공되지 않은경우 
    - L2 요청자에게 fwAmount 금액을 일반 출금한다. ⇒ NORMAL_WITHDRAWAL 
  - CANCELED  : 1
    - message 에 대해 L2요청자가 취소한 경우 
    - L2 요청자에게 fwAmount 금액을 일반 출금한다. ⇒ CANCEL_WITHDRAWAL 
  - PROVIDE_LIQUIDITY : 2
    - message 에 대해 유동성을 한번이라도 제공한 경우(L2요청자에게 출금됨) 
    - PROVIDE_WITHDRAWAL: sequencer 컨트랙에 fwAmount 을 보내고,  유동성 제공자의 스테이크 금액에 feeAmount 을 증가시킨다. 
  - NORMAL_WITHDRAWAL : 3 
    - status가 NONE  인 경우, 일반 출금을 실행함. 
    - l1Bridge → FwRecipt → L2 Requestor 로 톤을 보낸다.   
    - **이벤트 : NormalWithdrawal **
  - CANCEL_WITHDRAWAL : 4
    - status가  CANCELED 인 경우, 일반 출금을 실행함.
    -  l1Bridge → FwRecipt → L2 Requestor 로 톤을 보낸다.  
    - **이벤트 : NormalWithdrawal **
  - FINALIZE_WITHDRAWAL : 5
    - DTD기간후, 체크시, PROVIDE_LIQUIDITY 상태였다면,  빠른 출금 정산을 한다. 
    - fwAmount 금액을 Sequencer 컨트랙 또는 Candidate 컨트랙으로 보내고, 유동성제공자의 스테이크 금액에 feeAmount를 추가한다. 
    - **이벤트: FinalizedFastWithdrawal**
  - NOT_L1_BRIDGE : 6
    - 호출한 주소가 L1Bridge 컨트랙이 아닌경우, 
    - NOT_L1_BRIDGE 리턴한다. 메세지는 저장하지 않는다. 
    - 금액을 받았는지 확실하지 않다. 금액에 대한 처리를 하지 못함. 
    - **이벤트: InvalidMessageFastWithdrawal**
  - ZERO_AMOUNT: 7 
    - 전송된 메세지에 금액이 0 일때,
    - ZERO_AMOUNT 리턴한다. 메세지는 저장하지 않는다
    - 금액을 받았는지 확실하지 않다. 금액에 대한 처리를 하지 못함. 
    - **이벤트: InvalidMessageFastWithdrawal**
  - ZERO_REQUESTOR: 8
    - 전송된 메세지에 요청자 주소가 없음때, 
    - ZERO_REQUESTOR 리턴한다. 메세지는 저장하지 않는다. 
    - 금액을 받았는지 확실하지 않다. 금액에 대한 처리를 하지 못함. 
    - **이벤트: InvalidMessageFastWithdrawal**
  - WRONG_MESSAGE: 9 
    - 저장된 메세지의 유동성 제공자 주소가 0 이거나, 파라미터의 금액과 전송된 메세지의 금액이 같지 않을때  
    - WRONG_MESSAGE 리턴한다. 메세지는 저장하지 않는다. 
    - 금액을 받았는지 확실하지 않다. 금액에 대한 처리를 하지 못함. 
    - **이벤트: InvalidMessageFastWithdrawal**
  - FAIL_FINISH_FW : 10 
    - DTD기간후, 체크시, PROVIDE_LIQUIDITY 상태였고, 빠른 출금 정산을 실행했는데, 빠른 출금 정산 로직을 실패한 경우임.  
    -  **fwAmount 금액을 정산하지 못한채로 종료되었음. 추후 처리 확인 후, 처리가 필요함. **
    - **이벤트: FailFinishFastWithdrawal**
  - ETC: 11
    - 알수없는 상태주소 
    - 금액을 받았는지 확실하지 않다. 금액에 대한 처리를 하지 못함. 
    - **이벤트: InvalidMessageFastWithdrawal**
- 리스크
  - 시퀀서가 다운 혹은 잘못됐을 때 ⇒ 시뇨리지를 계속 부여하게 되는 오류
  - L1 bug (프런트 쪽 오류) ⇒ L2 요청 금액 * (1-수수료) ≠ L1 금액 

# Initialize parameters 

[[Initialize parameters on mainnet]] 

[[Initialize parameters on goerli]] 