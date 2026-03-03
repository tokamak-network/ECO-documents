# Repo

[https://github.com/tokamak-network/tokamak-staking-v2](https://github.com/tokamak-network/tokamak-staking-v2)

# Branch 

 [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_5_audit_v1](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_5_audit_v1)

# Function Description 

[https://docs.google.com/presentation/d/1B1tmpdY_CT09dLsWOKXx6DGDxFo6XUcUoMK7F42fRuE/edit](https://docs.google.com/presentation/d/1B1tmpdY_CT09dLsWOKXx6DGDxFo6XUcUoMK7F42fRuE/edit)

[[Function description of TON Staking V2 (deprecated) ]] 

# Test 

[[(4th) test tokamak-staking-v2 contracts ]] 

# Usages Guide 

[[(4th) Contract Usage Guide ( included fast withdraw, snapshot)  ]] 

 

# Contracts 

[link](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_5_audit_v1/contracts)

- SeigManagerV2.sol
- Layer2Manager.sol
- OptimismSequencer.sol
- Candidate.sol
- FwReceipt.sol

# Jason 

- [x] [JS_1]  It is necessary to distinguish between sequencer and candidate for staked events.
- [ ] [JS_2] createOptimismSequencer할때 TON의 allowance 양을 체크해야할것 같습니다. 
- [ ] [JS_3] staking 할때 TON의 allowance 양 체크
- [ ] [JS_4] createCandidate할때 `MinterRole: caller does not have the Minter role` 에러가 발생해서 리버트 됩니다
- [ ] [JS_5] OptimismSequencer → L2Operator로 변경: Contract내 Sequencer라는 명칭을 L2Operator로 변경 필요, change OVM_Sequencer to **“****OVM_TONStakingManager****”**

# Suah 

- [ ] S_1. update seigniorage formula. [https://docs.google.com/presentation/d/1SNzrypW7bgNjuZRJ9kGqAsdRV-JtkMaFq5U1PZNoC3I/edit#slide=id.g25063a2f3b1_0_8](https://docs.google.com/presentation/d/1SNzrypW7bgNjuZRJ9kGqAsdRV-JtkMaFq5U1PZNoC3I/edit#slide=id.g25063a2f3b1_0_8)

# Harvey 



# Justin 



# Theo

- [ ] provideLiquidity() 에서의 유동성 공급 조건 수정

# Zena 

- [x] add ‘return index’ at create function in Layer2Manager
- [x] Z_2. delete unused storage : l1CrossDomainMessenger of FwReceiptStorage
- [x]  change license to MIT
- [x] Z_4. modified **Staked** event parameters  ***from commission to commissionLton***
- [ ] 