# gas required to deploy

28815795 

[https://docs.google.com/spreadsheets/d/11-tOFwaEV8moowMfIXYTELHlYh6HzCx3CRn8VJq8aPU/edit#gid=0](https://docs.google.com/spreadsheets/d/11-tOFwaEV8moowMfIXYTELHlYh6HzCx3CRn8VJq8aPU/edit#gid=0)

# deploy on goerli

npx hardhat deploy —network goerli 

[code link](https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_5_audit_v1/deploy/deploy.ts)

```json
deploying "LibOptimism" (tx: 0x8c0b200941c3cbe4371d9715d4d3a419e65c9e69c5164805c6e6df5c0639bc17)...: deployed at 0x47bEb41c710c91e2f32A730fd233692BCd9a443f with 287193 gas
deploying "LibOperator" (tx: 0x1045c690d18de82b74239fd9eadf475b1d9135497439741897811fa9f0c11b40)...: deployed at 0x7113E111B583df38DC53C3CC3Ea3a52142DFb1a0 with 338351 gas
deploying "LibFastWithdraw" (tx: 0x93522412cf920e6a27236bbb73bae9673437caebd35d6acf4def737297e5e675)...: deployed at 0x7fe5e6406812cb9622Ba84e4026Ecd9684151fF1 with 755107 gas
deploying "SeigManagerV2" (tx: 0x0dc179244584736ef0860a5482a3d9cf1f6b90d71d82b9dcdcb07eb61d1cd6bf)...: deployed at 0x37b9512de4176dF4dA2E8c742813eA844722Ad5E with 2458768 gas
deploying "SeigManagerV2Proxy" (tx: 0xad17b5e12d9cfc7ca5aec3b52b648e17e7fb7902dddaf05fdf8cd3a62188c7fc)...: deployed at 0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3 with 2001216 gas
deploying "Layer2Manager" (tx: 0x5d619e36e4eaccbd86cf298ae9e44b208f9ba1783d0271e32a906c0483c9d10c)...: deployed at 0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211 with 3608529 gas
deploying "Layer2ManagerProxy" (tx: 0x3e524c3101853d91e4c2708d47f3547b215010bc1f0fba4c1e2161f4d4c7ddb6)...: deployed at 0x1d73ce5dBF41DD7feb5C861DE4d6FbBA74717445 with 1882111 gas
deploying "OptimismSequencer" (tx: 0x1b57f40159a909a809aab584e413499395d029ec505091c49325b128dd1de4b5)...: deployed at 0xccbB97CC6346A77F060129B928051C24F7cd68BE with 4402376 gas
deploying "OptimismSequencerProxy" (tx: 0xc371d4b81bc28762e3ac449b2a6dfd152c19f15b749531c63cc5b28adb5b407b)...: deployed at 0xE289b80D5c6Cb68C5CB36C48C9556e4Cb224c1Ae with 1971136 gas
deploying "Candidate" (tx: 0xcd276dd04fa591873718480964ab2ca2c89bcffd134456c15aea1baeb51b4ab4)...: deployed at 0x19989EBb0af66AAf2D619f75e663b8C489b7fef8 with 4456184 gas
deploying "CandidateProxy" (tx: 0xaebfe4e49c79fc9135201b42a3ad411cfb7ca147ec236b9c99456feded6cc536)...: deployed at 0x60154C996C7899d7Da8120f9E428a1E7749dc091 with 1994973 gas
deploying "FwReceipt" (tx: 0xddab299d854b7b717dcea8abd061151f17ff5e24a154986cbc7c7454fa63c80a)...: deployed at 0x00C12146166b39f529590AA214b5652BA7Dc4925 with 2913916 gas
deploying "FwReceiptProxy" (tx: 0x54696aacd6f412c9e8edc016ed152c3fbad72a8c7f22cca7b0d8544abf21cfea)...: deployed at 0x1a1Ab68E91A7E0265f4C1CF0BF1BC35f866128B2 with 1754131 gas
```

- 2023. 5.11 deployed 

```json
 "LibOptimism" at 0x47bEb41c710c91e2f32A730fd233692BCd9a443f
 "LibOperator" at 0x7113E111B583df38DC53C3CC3Ea3a52142DFb1a0
 "LibFastWithdraw" at 0x7fe5e6406812cb9622Ba84e4026Ecd9684151fF1
 "SeigManagerV2" at 0x37b9512de4176dF4dA2E8c742813eA844722Ad5E
 "SeigManagerV2Proxy" at 0xf62a322adfb5dAa81251BBEE6650D836779A3Cd3
 "Layer2Manager" at 0x7759d8b6d356c5Bd09Aa9211316Ae69b8002d211
 "Layer2ManagerProxy" at 0x1d73ce5dBF41DD7feb5C861DE4d6FbBA74717445
 "OptimismSequencer" at 0xccbB97CC6346A77F060129B928051C24F7cd68BE
 "OptimismSequencerProxy" at 0xE289b80D5c6Cb68C5CB36C48C9556e4Cb224c1Ae
 "Candidate" at 0x19989EBb0af66AAf2D619f75e663b8C489b7fef8
 "CandidateProxy" at 0x60154C996C7899d7Da8120f9E428a1E7749dc091
 "FwReceipt" at 0x00C12146166b39f529590AA214b5652BA7Dc4925
 "FwReceiptProxy" at 0x1a1Ab68E91A7E0265f4C1CF0BF1BC35f866128B2
```