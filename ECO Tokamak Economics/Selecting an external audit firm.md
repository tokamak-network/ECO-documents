# Background & Purpose

We have developed the “Simple staking V2.5” feature.  Before proposing the agenda for launch on the mainnet, an external audit service provider will audit it. The external audit ensures guarantees for the developed contract code.

- Discussion: [link](https://github.com/tokamak-network/ton-staking-v2/issues/59)
- Description of DAO upgrade: [description](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md)
- Description of staking v2.5: [description](https://github.com/tokamak-network/ton-staking-v2/blob/test-mainnet/docs/en/ton-staking-v2.md)
- Related Agenda : [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)

# Candidates

ref : aa6425f1-6036-4fa4-88c4-3407e97efe2a 

| Num | Name | Nationality | Website | Featured Customers | Note | Contact Member  |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CertiK | International | [https://www.certik.com/](https://www.certik.com/) | BSC, Polygon, Terra, Aave, Pancakeswap | we have audited by CertiK | @Unknown  |
| 2 | Sherlock | International | [https://www.sherlock.xyz/](https://www.sherlock.xyz/) | Optimism (bedrock, fault proof), Gitcoin, Avail, OlympusDAO, MakerDAO | Audit [Contest](https://audits.sherlock.xyz/contests) (crowdsourced incentivized auditing) | @Unknown  |
| 3 | ImmuneFi | International | [https://immunefi.com/](https://immunefi.com/) | Scroll, ENS, The graph, Ethena, Metis, Pendle, OpenZeppelin, ALEX | Bounty platform | @Unknown  |
| 4 | Slowmist | International | [https://www.slowmist.com/](https://www.slowmist.com/) | OKX, Uniswap, Pancakeswap, Bitlayer |  | @Unknown  |
| 5 | Chainlight | Domestic | [https://chainlight.io/](https://chainlight.io/) | BLUR, Kroma, Klaytn, zkSync, TON, Perpetual Protocol | by [Theori](https://theori.io/) | @Unknown  |
| 6 | Consensys Diligence | International | [https://consensys.io/diligence/](https://consensys.io/diligence/) | Metamask, 0x, Horizon, Linea, EigenLayer |  | @Unknown  |
| 7 | Trail of Bits | Intenational | [https://www.trailofbits.com/](https://www.trailofbits.com/) | Uniswap, Scroll, Aleo | security assessments not audit ([details](https://www.trailofbits.com/services/software-assurance/blockchain/))
[published review](https://github.com/trailofbits/publications#security-reviews) | @Unknown  |
| 8 | code4rena | International | [https://code4rena.com/audits](https://code4rena.com/audits) | Optimism (Superchain), Karak, Thorchain, Renzo, Canto, Arbitrum (BoLD), Ondo Finance | crowdsourced audit
[completed audits](https://code4rena.com/audits#completed-audits) | @Unknown |
| 9 | Omniscia | international | [https://omniscia.io/](https://omniscia.io/) | Steer Protocol, Gnosis DAO, Morpho Labs, Maverick Protocol, Mitosis | The company offered to promote to Max by Tokamak Network  | @Unknown |
| 10 | Mc Hammer | Domestic |  |  |  | @Unknown |
| 11 | Carl Park | Domestic |  |  |  | @Unknown  |

# nSLOC

Consensys에서 개발한 solidity-metrics 라는 코드 분석 툴 : nSLOC

- [https://github.com/Consensys/solidity-metrics](https://github.com/Consensys/solidity-metrics)

### Contract nSLOC (v2.5-audit-request branch standard)

| Contract Name | Lines | nLine | nSLOC | Complex. Score |
| --- | --- | --- | --- | --- |
| DAOCommitteeProxy2 | 168 | 156 | 93 | 109 |
| DAOCommittee_V1 | 804 | 682 | 517 | 367 |
| DAOCommitteeOwner | 356 | 255 | 176 | 244 |
| SeigManagerV1_3 | 724 | 669 | 411 | 275 |
| DepositManagerV1_1 | 200 | 168 | 114 | 115 |
| L1BridgeRegistryV1_1 | 453 | 422 | 186 | 175 |
| Layer2ManagerV1_1 | 544 | 455 | 230 | 261 |
| OperatorManagerV1_1 | 320 | 292 | 136 | 169 |
| CandidateAddOnV1_1 | 216 | 169 | 101 | 125 |

# Progress board

[[Audit Process]]

- 결제 분할(선금 잔금), 결제 수단
  - USDT - 1옵션 - 가능하면 이쪽으로 (보통 3:7) 변동가능
  - 달러도 가능
- 