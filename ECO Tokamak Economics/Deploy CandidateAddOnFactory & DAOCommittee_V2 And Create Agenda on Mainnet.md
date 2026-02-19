repo : [GitHub - tokamak-network/ton-staking-v2 at deploy-candidateAndDAO](https://github.com/tokamak-network/ton-staking-v2/tree/deploy-candidateAndDAO)

test: [doc1](/1dfd96a400a380e69602ce6b7c590782#1dfd96a400a380c39f23eb19a46d9ce2) , [doc2](/1f3d96a400a3809fb3acfb4e80a69562#1f3d96a400a3803fa715fe6618b96af2)

# Deploy CandidateAddOnFactory & DAOCommittee_V2 Contracts 

### Expected Used Gas 

[https://docs.google.com/spreadsheets/d/1W6OW0Ns-C0pIhYuShwtf2_oksC4OozcWLjYoWBVm3Nw/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1W6OW0Ns-C0pIhYuShwtf2_oksC4OozcWLjYoWBVm3Nw/edit?gid=0#gid=0)

- gasFee : 0.018 ETH & 10TON (gasPrice: Based on 2gwei)
- Deploy & Create Account : 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- ETH transfer (Jason → Harvey)
  - ETH(0.018) : [https://etherscan.io/tx/0xcd56165816e8b3d171205cd915a730c797429c323aeba4936b1de18c47fa950d](https://etherscan.io/tx/0xcd56165816e8b3d171205cd915a730c797429c323aeba4936b1de18c47fa950d)
  - TON : [https://etherscan.io/tx/0x4d302cee9add4ee41dc5c2dcf6671d9ced1a7224fd9f5a85531856582a3fb9bf](https://etherscan.io/tx/0x4d302cee9add4ee41dc5c2dcf6671d9ced1a7224fd9f5a85531856582a3fb9bf)
- ETH transfer (Harvey → Jason)
  - ETH(0.0138) : [https://etherscan.io/tx/0xdf208c98b1e1981f3f7cda460f9cf4711cacc421ed4df89a0a09011be76c54e4](https://etherscan.io/tx/0xdf208c98b1e1981f3f7cda460f9cf4711cacc421ed4df89a0a09011be76c54e4)

## Deploy CandidateAddOnFactory

- Deploy account: 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- Deploy command:

```shell
npx hardhat run scripts/layer2-mainnet/9.deploy-candidate-add-on-proxy-factory.js --network mainnet

npx hardhat verify 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22 --network mainnet
```

- tx : [https://etherscan.io/tx/0x2a206160568a018d13152224f0bc668105080640acb8610e1f5d8c19c35971ae](https://etherscan.io/tx/0x2a206160568a018d13152224f0bc668105080640acb8610e1f5d8c19c35971ae)
- Deployed CandidateAddOnFactory address: 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22

## Deploy DAOCommittee_V2

- Deploy account : 0x6E1c4a442E9B9ddA59382ee78058650F1723E0F6
- Deploy command
```solidity
npx hardhat run scripts/1.deploy_DAO.js --network mainnet

npx hardhat verify 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B --network mainnet
```
- tx : [https://etherscan.io/tx/0x08589450dbe4708ea928e3c0aa92cf5dd3aa60ecb4f43bebceb66461706471d1](https://etherscan.io/tx/0x08589450dbe4708ea928e3c0aa92cf5dd3aa60ecb4f43bebceb66461706471d1)
- Deployed DAOCommittee_V2 address: 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B

## Deployed Addresses 

```solidity
DAOCommittee_V2 : 0x9f2242B4859c2B1c2fa327245c65e785983e9F5B
CandidateAddOnFactory : 0xacf89A80F1EC7B94EA1e184f70E02fa1231cAB22
```

## Create Agenda

- The agenda performs two functions:
  - The first is the upgradeTo function for CandidateFactoryProxy.
  - The second is the upgradeTo2 function of DAOCommitteeProxy2.
- create agenda
```solidity
npx hardhat run scripts/13.upgradeToAgenda_on_Mainnet.js --network mainnet
```
- tx : [https://etherscan.io/tx/0x1cd0e5c2e4e9d499cd9e72dd86e047815ba44c8e19e8296181cb29e989b1398d](https://etherscan.io/tx/0x1cd0e5c2e4e9d499cd9e72dd86e047815ba44c8e19e8296181cb29e989b1398d)
- Agenda 15 : [https://github.com/tokamak-network/ton-staking-v2/issues/311](https://github.com/tokamak-network/ton-staking-v2/issues/311)

## After Test

- Create an agenda and then test it
- After setting blockNumber after agenda creation
```solidity
npx hardhat test test/agenda/35.AfterDeployIntegrationTest-mainnet.js 
```
- Result
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/12baa833-3199-4ab3-abf7-617549565e9f/75A2C405-A39A-48E8-B267-E3C857F0078F.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEJRJALI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd7UN%2BR0iFdWj0FdJl07kFxjzerFpcFkSS8htvFXzazAiBjkBa3PDG%2BWJ0MPxDffe%2FMIAIYNIJBCA1m7%2BYQ9u7NQSr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMVjahdqxJ%2FeuSsN9SKtwD9mXgF1gtMyHDj5Cn3Bdkjrmc7pzIvtdjR6Vm8GtDiCtw%2FYGwSyH8cpOIXAb%2FlSZLa0pIZflEIRMaOo%2B5%2FzAQfBTkorEdnLhHdIlJriJqaf1Ga7JMl%2BD41S7bkbwgKNXoEATYcp3dIH%2FeujQRHaYJDnhbYWEHd0odnE0qR3GfGxMCBsHSvhhPdjrBZ%2FB1UG6jdDleBaVLguw3q8RA3V16jDB1THSuZ%2B0iP6GSd%2BFxvd3Kz%2FYjLFDHrKScAfn0iukkun%2FLTcKwDZ8aqh22tDEOE6YZnYCBQtgXoj%2BCNFkZ19EGvjn1USJTecz%2FOC9HJvYjdSiCR7rSPSA6rzWcHMmt5ilr7RpiE3H51CMfTuVtUGgZAS%2BPKFZxhPDBmx4KVeZlaU4AKQ8Rxy6X6KkXN1SDshjjuw1MD0OoySlq9O68jICaGDHXzZ3W2ZS0KN%2Fc7D9BGcSUOnshemBULqj1EeLp3CTGnElahOciaHLNIHWAtTSJmow16ECv7%2FADe5M%2BbdiN1DIlPEFg%2Bns0Zei3eAqoGDlXfI1pad8VBEYLDIGLRT0rPqvUeSMHT6b4Yg4lfREplhb3F1PaHneXZ3svO1rchbcWg4%2BkhVKx0Cy%2BiJPjAhHNwREzTmVoPLgc9ogw%2BMTazAY6pgHdYp6veR0cPkpcyPWPqdUayYbHazUcVq8P7%2BzTtM1XRzSSP0WSr%2BB131EONQWan5jwwmMgxvqrSGplckpUTKfHCFDuZdAAsIncbEhmnavTBY5mCTg%2FaYEc%2FxnmlVFBmjMB%2Fcs3u%2FmKacbiTu%2FXPiZ311vOr3ajaImqgL1fvgFrxSsO5w1TamptDi%2B9R9TWh5jeINstZlzuOzXdBNcGTFu120oPO1dg&X-Amz-Signature=d71fa12c62ae802e88f12a3a0c7ebf3417de68e3c285acaf5b80b914a9b46263&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/60e33936-1e94-48b9-84e5-d13d91f73754/97ABCDD3-633F-4983-AE31-B6212AEF86DC.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEJRJALI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd7UN%2BR0iFdWj0FdJl07kFxjzerFpcFkSS8htvFXzazAiBjkBa3PDG%2BWJ0MPxDffe%2FMIAIYNIJBCA1m7%2BYQ9u7NQSr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMVjahdqxJ%2FeuSsN9SKtwD9mXgF1gtMyHDj5Cn3Bdkjrmc7pzIvtdjR6Vm8GtDiCtw%2FYGwSyH8cpOIXAb%2FlSZLa0pIZflEIRMaOo%2B5%2FzAQfBTkorEdnLhHdIlJriJqaf1Ga7JMl%2BD41S7bkbwgKNXoEATYcp3dIH%2FeujQRHaYJDnhbYWEHd0odnE0qR3GfGxMCBsHSvhhPdjrBZ%2FB1UG6jdDleBaVLguw3q8RA3V16jDB1THSuZ%2B0iP6GSd%2BFxvd3Kz%2FYjLFDHrKScAfn0iukkun%2FLTcKwDZ8aqh22tDEOE6YZnYCBQtgXoj%2BCNFkZ19EGvjn1USJTecz%2FOC9HJvYjdSiCR7rSPSA6rzWcHMmt5ilr7RpiE3H51CMfTuVtUGgZAS%2BPKFZxhPDBmx4KVeZlaU4AKQ8Rxy6X6KkXN1SDshjjuw1MD0OoySlq9O68jICaGDHXzZ3W2ZS0KN%2Fc7D9BGcSUOnshemBULqj1EeLp3CTGnElahOciaHLNIHWAtTSJmow16ECv7%2FADe5M%2BbdiN1DIlPEFg%2Bns0Zei3eAqoGDlXfI1pad8VBEYLDIGLRT0rPqvUeSMHT6b4Yg4lfREplhb3F1PaHneXZ3svO1rchbcWg4%2BkhVKx0Cy%2BiJPjAhHNwREzTmVoPLgc9ogw%2BMTazAY6pgHdYp6veR0cPkpcyPWPqdUayYbHazUcVq8P7%2BzTtM1XRzSSP0WSr%2BB131EONQWan5jwwmMgxvqrSGplckpUTKfHCFDuZdAAsIncbEhmnavTBY5mCTg%2FaYEc%2FxnmlVFBmjMB%2Fcs3u%2FmKacbiTu%2FXPiZ311vOr3ajaImqgL1fvgFrxSsO5w1TamptDi%2B9R9TWh5jeINstZlzuOzXdBNcGTFu120oPO1dg&X-Amz-Signature=88d08c75a420c6f3887153eebebcca80a887a31782ae06b739752573a730dd71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e44884da-edb5-4fc7-bfac-745c34044ab6/271FA56D-F04A-417F-AA08-E01CB3E589F6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEJRJALI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T054958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd7UN%2BR0iFdWj0FdJl07kFxjzerFpcFkSS8htvFXzazAiBjkBa3PDG%2BWJ0MPxDffe%2FMIAIYNIJBCA1m7%2BYQ9u7NQSr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMVjahdqxJ%2FeuSsN9SKtwD9mXgF1gtMyHDj5Cn3Bdkjrmc7pzIvtdjR6Vm8GtDiCtw%2FYGwSyH8cpOIXAb%2FlSZLa0pIZflEIRMaOo%2B5%2FzAQfBTkorEdnLhHdIlJriJqaf1Ga7JMl%2BD41S7bkbwgKNXoEATYcp3dIH%2FeujQRHaYJDnhbYWEHd0odnE0qR3GfGxMCBsHSvhhPdjrBZ%2FB1UG6jdDleBaVLguw3q8RA3V16jDB1THSuZ%2B0iP6GSd%2BFxvd3Kz%2FYjLFDHrKScAfn0iukkun%2FLTcKwDZ8aqh22tDEOE6YZnYCBQtgXoj%2BCNFkZ19EGvjn1USJTecz%2FOC9HJvYjdSiCR7rSPSA6rzWcHMmt5ilr7RpiE3H51CMfTuVtUGgZAS%2BPKFZxhPDBmx4KVeZlaU4AKQ8Rxy6X6KkXN1SDshjjuw1MD0OoySlq9O68jICaGDHXzZ3W2ZS0KN%2Fc7D9BGcSUOnshemBULqj1EeLp3CTGnElahOciaHLNIHWAtTSJmow16ECv7%2FADe5M%2BbdiN1DIlPEFg%2Bns0Zei3eAqoGDlXfI1pad8VBEYLDIGLRT0rPqvUeSMHT6b4Yg4lfREplhb3F1PaHneXZ3svO1rchbcWg4%2BkhVKx0Cy%2BiJPjAhHNwREzTmVoPLgc9ogw%2BMTazAY6pgHdYp6veR0cPkpcyPWPqdUayYbHazUcVq8P7%2BzTtM1XRzSSP0WSr%2BB131EONQWan5jwwmMgxvqrSGplckpUTKfHCFDuZdAAsIncbEhmnavTBY5mCTg%2FaYEc%2FxnmlVFBmjMB%2Fcs3u%2FmKacbiTu%2FXPiZ311vOr3ajaImqgL1fvgFrxSsO5w1TamptDi%2B9R9TWh5jeINstZlzuOzXdBNcGTFu120oPO1dg&X-Amz-Signature=1cc57c0232232d81f11c993e6756d2d4c4d988c9adb0f723f8a313f9fa63ad11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- 