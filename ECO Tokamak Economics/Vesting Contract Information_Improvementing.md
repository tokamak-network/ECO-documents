# Vesting Contract Information

- Vesting repo : [https://github.com/tokamak-network/presale-contracts](https://github.com/tokamak-network/presale-contracts)

> [!note]
> 📌 **The vesting contract outlines the how 50,000,000 TON is allocated into various vault.** Each vault has its own unique token and can be exchanged for TON at a specified swap ratio. The vault also specifies the authorized individuals who can access the tokens, as well as the unlock schedule.
> There is a special vault called MarketingTON that does not have unlock schedule and allows for swapping beyond a predetermined amount. However, it's important to note that this does not result in the creation of additional TON. Any surplus swap amount is deducted from the claimable amount in other vaults. In other words, the total claimable amount from all the vaults remains fixed at 50,000,000 TON.

## [SeedTON](https://etherscan.io/address/0x6c1e75ce98f67e15587388f633d8c7ae8f2c399f)

1. Vault parameters
| Token supply | [30,000](https://etherscan.io/tx/0x0181d388bbfb17113b5e64392a6c88d68afef974d64241b7a426c7dedbcc2e32) SeedTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x8ec31deaed9768b42e68273eb6a98f98faa1d0277fc6f494c7438398dddbac8c) TON per 1 SeedTON |
| Total locked TON | [30,000](https://etherscan.io/advanced-filter?tkn=0x6c1E75Ce98f67e15587388f633D8C7Ae8F2C399f&txntype=2&tadd=0x25c31c6f764c11fbe62b72e83a149771d6d70a61) SeedTON x [50](https://etherscan.io/tx/0x8ec31deaed9768b42e68273eb6a98f98faa1d0277fc6f494c7438398dddbac8c) TON per 1 SeedTON = 1,500,000 TON  |
| First unlock amount | [300](https://etherscan.io/tx/0x51a7fc6462587332747e364d29ea7a30292d31043c3141ebe6436a59f535f03c) SeedTON |
| Subsequent unlock amount | ([30,000](https://etherscan.io/advanced-filter?tkn=0x6c1E75Ce98f67e15587388f633D8C7Ae8F2C399f&txntype=2&tadd=0x25c31c6f764c11fbe62b72e83a149771d6d70a61)-[300](https://etherscan.io/tx/0x51a7fc6462587332747e364d29ea7a30292d31043c3141ebe6436a59f535f03c))/ 6 = 4,950 SeedTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | SeedTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2020.09.12](https://etherscan.io/tx/0x51a7fc6462587332747e364d29ea7a30292d31043c3141ebe6436a59f535f03c) | [300](https://etherscan.io/tx/0x51a7fc6462587332747e364d29ea7a30292d31043c3141ebe6436a59f535f03c) SeedTON | 15,000 TON |
| 2 | 2020.10.12  | 4,950 SeedTON | 247,500 TON |
| 3 | 2020.11.11 | 4,950 SeedTON | 247,500 TON |
| 4 | 2020.12.11 | 4,950 SeedTON | 247,500 TON |
| 5 | 2021.01.10 | 4,950 SeedTON | 247,500 TON |
| 6 | 2021.02.09 | 4,950 SeedTON | 247,500 TON |
| 7 | 2021.03.11 | 4,950 SeedTON | 247,500 TON |
| SUM |  | 247,500 SeedTON | 1,500,000 TON |

## [PrivateTON](https://etherscan.io/address/0xa4eac2a2eaff4a43e31b336406a6d618725032cc)

1. Vault parameters
| Token supply | [144,000](https://etherscan.io/tx/0x7c48628b0bcc15d43c6733ed058e370dd718f95c6fe4b2708bce55ddf0b665a5) PrivateTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0xf168931839af1ffc1fbc089293bb5fec1c915b42bfee21e4d514ec7548b6cbdb) TON per 1 PrivateTON |
| Total locked TON | [144,000](https://etherscan.io/tx/0x7c48628b0bcc15d43c6733ed058e370dd718f95c6fe4b2708bce55ddf0b665a5) PrivateTON x [50](https://etherscan.io/tx/0xf168931839af1ffc1fbc089293bb5fec1c915b42bfee21e4d514ec7548b6cbdb) TON per 1 PrivateTON = 7,200,000 TON  |
| First unlock amount | [7,200](https://etherscan.io/tx/0x573f8e324a83ba922bde42f49e4fb950d8445940aab21aecb8d14f60c3b2dc84) PrivateTON |
| Subsequent unlock amount | ([144,000](https://etherscan.io/advanced-filter?tkn=0xa4eac2a2eaff4a43e31b336406a6d618725032cc&txntype=2&tadd=0x25c31c6f764c11fbe62b72e83a149771d6d70a61)-[7,200](https://etherscan.io/tx/0x573f8e324a83ba922bde42f49e4fb950d8445940aab21aecb8d14f60c3b2dc84)) / 10 = 13,680 PrivateTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | PrivateTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | 2020.09.12   | 7,200 PrivateTON | 360,000 TON |
| 2 | 2020.10.12   | 13,680 PrivateTON | 684,000 TON |
| 3 | 2020.11.11   | 13,680 PrivateTON | 684,000 TON |
| 4 | 2020.12.11   | 13,680 PrivateTON | 684,000 TON |
| 5 | 2021.01.10   | 13,680 PrivateTON | 684,000 TON |
| 6 | 2021.02.09   | 13,680 PrivateTON | 684,000 TON |
| 7 | 2021.03.11   | 13,680 PrivateTON | 684,000 TON |
| 8 | 2021.04.10   | 13,680 PrivateTON | 684,000 TON |
| 9 | 2021.05.10   | 13,680 PrivateTON | 684,000 TON |
| 10 | 2021.06.09   | 13,680 PrivateTON | 684,000 TON |
| 11 | 2021.07.09   | 13,680 PrivateTON | 684,000 TON |
| SUM |  | 144,000 PrivateTON | 7,200,000 TON |

## [**StrategicTON**](https://etherscan.io/address/0x9ab783adc9958f578cb4b126187592e2d9072a2d)

1. Vault parameters
| Token supply | [84,000](https://etherscan.io/tx/0x379daa66fa5db83769256475843846c0ce193abe364f6ab6c7127acf1e77a15e) StrategicTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x6846601e9cbe7b4228ca485d1f56744ccd14bbe2dcdfbaebc51db2ad7756b9f7) TON per 1 StrategicTON |
| Total locked TON | [84,000](https://etherscan.io/tx/0x379daa66fa5db83769256475843846c0ce193abe364f6ab6c7127acf1e77a15e) StrategicTON x [50](https://etherscan.io/tx/0x6846601e9cbe7b4228ca485d1f56744ccd14bbe2dcdfbaebc51db2ad7756b9f7) TON per 1 StrategicTON = 4,200,000 TON  |
| First unlock amount | [7,560](https://etherscan.io/tx/0xe817927cc5ef20605f45088f4fc426e193069a30616190a96818ae38966d71d5) StrategicTON |
| Subsequent unlock amount | ([84,000](https://etherscan.io/advanced-filter?tkn=0x9aB783ADC9958f578CB4b126187592e2D9072a2D&txntype=2&tadd=0x25c31c6f764c11fbe62b72e83a149771d6d70a61)-[7,560](https://etherscan.io/tx/0xe817927cc5ef20605f45088f4fc426e193069a30616190a96818ae38966d71d5)) / 10 = 7,644 StrategicTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Unlock Date (GMT+09:00) | StrategicTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | 2020.09.12   | 7,560 StrategicTON | 378,000 TON |
| 2 | 2020.10.12   | 7,644 StrategicTON | 382,200 TON |
| 3 | 2020.11.11   | 7,644 StrategicTON | 382,200 TON |
| 4 | 2020.12.11   | 7,644 StrategicTON | 382,200 TON |
| 6 | 2021.01.10   | 7,644 StrategicTON | 382,200 TON |
| 7 | 2021.02.09   | 7,644 StrategicTON | 382,200 TON |
| 8 | 2021.03.11   | 7,644 StrategicTON | 382,200 TON |
| 9 | 2021.04.10   | 7,644 StrategicTON | 382,200 TON |
| 10 | 2021.05.10   | 7,644 StrategicTON | 382,200 TON |
| 11 | 2021.06.09   | 7,644 StrategicTON | 382,200 TON |
| 12 | 2021.07.09   | 7,644 StrategicTON | 382,200 TON |
| SUM |  | 84,000 StrategicTON | 4,200,000 TON |

## [Team](https://etherscan.io/address/0x07599893969f5a4851d149ed14dbeba886811afb)[**TON**](https://etherscan.io/address/0x07599893969f5a4851d149ed14dbeba886811afb)

1. Vault parameters
| Token supply | [150,000](https://etherscan.io/tx/0xa2f8cf7f6d5f7533e22ac755ea587589746db32711b63ed116cea01b79150f2f) TeamTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x88f3aaa35e531fd80c1f87b3d2fbebd9ee2db1fce0425f2c0f5b529dce5e3f48) TON per 1 TeamTON |
| Total locked TON | [150,000](https://etherscan.io/tx/0xa2f8cf7f6d5f7533e22ac755ea587589746db32711b63ed116cea01b79150f2f) TeamTON x [50](https://etherscan.io/tx/0x88f3aaa35e531fd80c1f87b3d2fbebd9ee2db1fce0425f2c0f5b529dce5e3f48) TON per 1 TeamTON = 7,500,000 TON  |
| Unlock amount per round | [150,000](https://etherscan.io/tx/0xa2f8cf7f6d5f7533e22ac755ea587589746db32711b63ed116cea01b79150f2f)/ 36 = 4,166 TeamTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | TeamTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2021.02.09](https://etherscan.io/tx/0x326ca34edc123e261325c0222b1fc7fa0e5a5b88035ade193fd12907af8d8df2) | 4,166 TeamTON | 208,333 TON |
| 2 | 2021.03.11   | 4,166 TeamTON | 208,333 TON |
| 3 | 2021.04.10   | 4,166 TeamTON | 208,333 TON |
| 4 | 2021.05.10   | 4,166 TeamTON | 208,333 TON |
| 5 | 2021.06.09   | 4,166 TeamTON | 208,333 TON |
| 6 | 2021.07.09   | 4,166 TeamTON | 208,333 TON |
| 7 | 2021.08.08   | 4,166 TeamTON | 208,333 TON |
| 8 | 2021.09.07   | 4,166 TeamTON | 208,333 TON |
| 9 | 2021.10.07   | 4,166 TeamTON | 208,333 TON |
| 10 | 2021.11.06   | 4,166 TeamTON | 208,333 TON |
| 11 | 2021.12.06   | 4,166 TeamTON | 208,333 TON |
| 12 | 2022.01.05   | 4,166 TeamTON | 208,333 TON |
| 13 | 2022.02.04   | 4,166 TeamTON | 208,333 TON |
| 14 | 2022.03.06   | 4,166 TeamTON | 208,333 TON |
| 15 | 2022.04.05   | 4,166 TeamTON | 208,333 TON |
| 16 | 2022.05.05   | 4,166 TeamTON | 208,333 TON |
| 17 | 2022.06.04   | 4,166 TeamTON | 208,333 TON |
| 18 | 2022.07.04   | 4,166 TeamTON | 208,333 TON |
| 19 | 2022.08.03   | 4,166 TeamTON | 208,333 TON |
| 20 | 2022.09.02   | 4,166 TeamTON | 208,333 TON |
| 21 | 2022.10.02   | 4,166 TeamTON | 208,333 TON |
| 22 | 2022.11.01   | 4,166 TeamTON | 208,333 TON |
| 23 | 2022.12.01   | 4,166 TeamTON | 208,333 TON |
| 24 | 2022.12.31   | 4,166 TeamTON | 208,333 TON |
| 25 | 2023.01.30   | 4,166 TeamTON | 208,333 TON |
| 26 | 2023.03.01   | 4,166 TeamTON | 208,333 TON |
| 27 | 2023.03.31   | 4,166 TeamTON | 208,333 TON |
| 28 | 2023.04.30   | 4,166 TeamTON | 208,333 TON |
| 29 | 2023.05.30   | 4,166 TeamTON | 208,333 TON |
| 30 | 2023.06.29   | 4,166 TeamTON | 208,333 TON |
| 31 | 2023.07.29   | 4,166 TeamTON | 208,333 TON |
| 32 | 2023.08.28   | 4,166 TeamTON | 208,333 TON |
| 33 | 2023.09.27   | 4,166 TeamTON | 208,333 TON |
| 34 | 2023.10.27   | 4,166 TeamTON | 208,333 TON |
| 35 | 2023.11.26   | 4,166 TeamTON | 208,333 TON |
| 36 | 2023.12.26   | 4,166 TeamTON | 208,333 TON |
| SUM |  | 150,000 TeamTON | 7,500,000 TON |

## [Advisor](https://etherscan.io/address/0x7c65182dd2ec55d3d91d16e2e69eebe251a5f1a2)[**TON**](https://etherscan.io/address/0x7c65182dd2ec55d3d91d16e2e69eebe251a5f1a2)

1. Vault parameters
| Token supply | [30,000](https://etherscan.io/tx/0x21c94f90294ab57cd8edc7bd9dd4c44360d0315d39f95ebd3a5f238230f179c8) AdvisorTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x8a64448be2d737d62b4e7cd07b8ead88e2618032213c7af86a950a462670d5c4) TON per 1 AdvisorTON |
| Total locked TON | [30,000](https://etherscan.io/tx/0x21c94f90294ab57cd8edc7bd9dd4c44360d0315d39f95ebd3a5f238230f179c8) AdvisorTON x [50](https://etherscan.io/tx/0x8a64448be2d737d62b4e7cd07b8ead88e2618032213c7af86a950a462670d5c4) TON per 1 AdvisorTON = 1,500,000 TON  |
| Unlock amount per round | [30,000](https://etherscan.io/tx/0x21c94f90294ab57cd8edc7bd9dd4c44360d0315d39f95ebd3a5f238230f179c8) / 18 = 1,666 AdvisorTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | AdvisorTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2021.02.09](https://etherscan.io/tx/0xa39d9fa8d622495f17a92d8a5e867fdbae0a6f0f94c6778d1f1b96f8c19107f6) | 1,666 AdvisorTON | 83,333 TON |
| 2 | 2021.03.11   | 1,666 AdvisorTON | 83,333 TON |
| 3 | 2021.04.10   | 1,666 AdvisorTON | 83,333 TON |
| 4 | 2021.05.10   | 1,666 AdvisorTON | 83,333 TON |
| 5 | 2021.06.09   | 1,666 AdvisorTON | 83,333 TON |
| 6 | 2021.07.09   | 1,666 AdvisorTON | 83,333 TON |
| 7 | 2021.08.08   | 1,666 AdvisorTON | 83,333 TON |
| 8 | 2021.09.07   | 1,666 AdvisorTON | 83,333 TON |
| 9 | 2021.10.07   | 1,666 AdvisorTON | 83,333 TON |
| 10 | 2021.11.06   | 1,666 AdvisorTON | 83,333 TON |
| 11 | 2021.12.06   | 1,666 AdvisorTON | 83,333 TON |
| 12 | 2022.01.05   | 1,666 AdvisorTON | 83,333 TON |
| 13 | 2022.02.04   | 1,666 AdvisorTON | 83,333 TON |
| 14 | 2022.03.06   | 1,666 AdvisorTON | 83,333 TON |
| 15 | 2022.04.05   | 1,666 AdvisorTON | 83,333 TON |
| 16 | 2022.05.05   | 1,666 AdvisorTON | 83,333 TON |
| 17 | 2022.06.04   | 1,666 AdvisorTON | 83,333 TON |
| 18 | 2022.07.04   | 1,666 AdvisorTON | 83,333 TON |
| SUM |  | 30,000 AdvisorTON | 1,500,000 TON |

## [Marketing](https://etherscan.io/address/0xe3a87a9343D262F5f11280058ae807B45aa34669)[**TON**](https://etherscan.io/address/0xe3a87a9343D262F5f11280058ae807B45aa34669)

1. Vault parameters
| Token supply | [2,604,259](https://etherscan.io/advanced-filter?tkn=0xe3a87a9343D262F5f11280058ae807B45aa34669&txntype=2&fadd=0x0000000000000000000000000000000000000000&p=6) MarketingTON |
| --- | --- |
| Swap ratio | [1](https://etherscan.io/tx/0x5b12fbb304d7dc265bb91230ef03321935733af352194fd82398e9242e95493c) TON per 1 MarketingTON |
| Total locked TON | [2,604,259](https://etherscan.io/advanced-filter?tkn=0xe3a87a9343D262F5f11280058ae807B45aa34669&txntype=2&fadd=0x0000000000000000000000000000000000000000&p=6) MarketingTON x [1](https://etherscan.io/tx/0x5b12fbb304d7dc265bb91230ef03321935733af352194fd82398e9242e95493c) TON per 1 MarketingTON = 2,604,259 TON  |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | MarketingTON | Equivalent TON |
| --- | --- | --- | --- |
| No unlock rounds | [No unlock rounds](https://etherscan.io/tx/0x21f889cef265534eb44a10632f213cb9c49fbf0ccccc1ac0fc8f27d80a3a5622) | 2,604,259 MarketingTON | 2,604,259 TON |
| SUM |  | 2,604,259 MarketingTON | 2,604,259 TON |

  1. Note: Actual unlock amount: [2,604,259](https://etherscan.io/advanced-filter?tkn=0xe3a87a9343D262F5f11280058ae807B45aa34669&txntype=2&fadd=0x0000000000000000000000000000000000000000&p=6) * [1](https://etherscan.io/tx/0x5b12fbb304d7dc265bb91230ef03321935733af352194fd82398e9242e95493c) =  2,604,259 TON
    1. There are no unlock restrictions for MarketingTON. It can be minted by the MarketingTON minter (or can be staked for more MarketingTON) and can be swapped to TON at any time. However, this does not imply that additional TON can be minted.
    1. If predefined unlock amount (2,600,000 MarketingTON) has been swapped to TON, the swapper contract will utilize the unclaimed TON from another vault to exchange MarketingTON for TON. This implies that the TON in the other vaults may be less than what is specified in this document. **Note: no additional TON can be generated through this process.**

## [Business](https://etherscan.io/address/0x774bb5875072dea0a41f8d4ea90adc36270cc98e)[**TON**](https://etherscan.io/address/0x774bb5875072dea0a41f8d4ea90adc36270cc98e)

1. Vault parameters
| Token supply | [100,000](https://etherscan.io/tx/0x97ac9f51fac98eee2381fad4ab14bd6f5d65b6976dacb5579220dc68d5fd8fd1) BusinessTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x8ef000a99f5612b9fd30e9e61a3a58ce4f1682e87cd5c177300f9f3d3edffffe) TON per 1 BusinessTON |
| Total locked TON | [100,000](https://etherscan.io/tx/0x97ac9f51fac98eee2381fad4ab14bd6f5d65b6976dacb5579220dc68d5fd8fd1) BusinessTON x [50](https://etherscan.io/tx/0x8ef000a99f5612b9fd30e9e61a3a58ce4f1682e87cd5c177300f9f3d3edffffe) TON per 1 BusinessTON = 5,000,000 TON |
| Unlock amount per round | [100,000](https://etherscan.io/tx/0x97ac9f51fac98eee2381fad4ab14bd6f5d65b6976dacb5579220dc68d5fd8fd1) / 20 = 5,000 BusinessTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | BusinessTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2020.09.12](https://etherscan.io/tx/0xb58eb9951574c4df42163861eeb1eb7445aa24fa5bb266bb2d1999c779302304)   | [5,000](https://etherscan.io/tx/0xb58eb9951574c4df42163861eeb1eb7445aa24fa5bb266bb2d1999c779302304) BusinessTON | 250,000 TON |
| 2 | [2020.10.12](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1)   | 5,000 BusinessTON | 250,000 TON |
| 3 | 2020.11.11   | 5,000 BusinessTON | 250,000 TON |
| 4 | 2020.12.11   | 5,000 BusinessTON | 250,000 TON |
| 5 | 2021.01.10   | 5,000 BusinessTON | 250,000 TON |
| 6 | 2021.02.09   | 5,000 BusinessTON | 250,000 TON |
| 7 | 2021.03.11   | 5,000 BusinessTON | 250,000 TON |
| 8 | 2021.04.10   | 5,000 BusinessTON | 250,000 TON |
| 9 | 2021.05.10   | 5,000 BusinessTON | 250,000 TON |
| 10 | 2021.06.09   | 5,000 BusinessTON | 250,000 TON |
| 11 | 2021.07.09   | 5,000 BusinessTON | 250,000 TON |
| 12 | 2021.08.08   | 5,000 BusinessTON | 250,000 TON |
| 13 | 2021.09.07   | 5,000 BusinessTON | 250,000 TON |
| 14 | 2021.10.07   | 5,000 BusinessTON | 250,000 TON |
| 15 | 2021.11.06   | 5,000 BusinessTON | 250,000 TON |
| 16 | 2021.12.06   | 5,000 BusinessTON | 250,000 TON |
| 17 | 2022.01.05   | 5,000 BusinessTON | 250,000 TON |
| 18 | 2022.02.04   | 5,000 BusinessTON | 250,000 TON |
| 19 | 2022.03.06   | 5,000 BusinessTON | 250,000 TON |
| 20 | 2022.04.05   | 5,000 BusinessTON | 250,000 TON |
| SUM |  | 100,000 BusinessTON | 5,000,000 TON |

## [Reserve](https://etherscan.io/address/0xd1f04aad6582f6034f4e5709f2c09b147f3376c5)[**TON**](https://etherscan.io/address/0xd1f04aad6582f6034f4e5709f2c09b147f3376c5)

1. Vault parameters
| Token supply | [60,000](https://etherscan.io/tx/0x17c667d5e9678d52f6c86cd868de9acd3584bf560140c7751da9318b1defec25) ReserveTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0xd816d0762187ae731cda26209eaa118287afe68d64cfa9881107c30f88ab918b) TON per 1 ReserveTON |
| Total locked TON | [60,000](https://etherscan.io/tx/0x17c667d5e9678d52f6c86cd868de9acd3584bf560140c7751da9318b1defec25) ReserveTON x [50](https://etherscan.io/tx/0xd816d0762187ae731cda26209eaa118287afe68d64cfa9881107c30f88ab918b) TON per 1 ReserveTON = 3,000,000 TON |
| Unlock amount per round | [60,000](https://etherscan.io/tx/0x17c667d5e9678d52f6c86cd868de9acd3584bf560140c7751da9318b1defec25) / 30 = 2,000 ReserveTON |
| Unlock round period | [2592000](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1) seconds (30 days) |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | ReserveTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2021.08.08  ](https://etherscan.io/tx/0x082dbbd3c48487c39fb3dd51cf2028d4e1540a42089c145c0475037e19dac84d) | [2,000](https://etherscan.io/tx/0x082dbbd3c48487c39fb3dd51cf2028d4e1540a42089c145c0475037e19dac84d) ReserveTON | 100,000 TON |
| 2 | [2021.09.07](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61#readContract#F1)   | 2,000 ReserveTON | 100,000 TON |
| 3 | 2021.10.07   | 2,000 ReserveTON | 100,000 TON |
| 4 | 2021.11.06   | 2,000 ReserveTON | 100,000 TON |
| 5 | 2021.12.06   | 2,000 ReserveTON | 100,000 TON |
| 6 | 2022.01.05   | 2,000 ReserveTON | 100,000 TON |
| 7 | 2022.02.04   | 2,000 ReserveTON | 100,000 TON |
| 8 | 2022.03.06   | 2,000 ReserveTON | 100,000 TON |
| 9 | 2022.04.05   | 2,000 ReserveTON | 100,000 TON |
| 10 | 2022.05.05   | 2,000 ReserveTON | 100,000 TON |
| 11 | 2022.06.04   | 2,000 ReserveTON | 100,000 TON |
| 12 | 2022.07.04   | 2,000 ReserveTON | 100,000 TON |
| 13 | 2022.08.03   | 2,000 ReserveTON | 100,000 TON |
| 14 | 2022.09.02   | 2,000 ReserveTON | 100,000 TON |
| 15 | 2022.10.02   | 2,000 ReserveTON | 100,000 TON |
| 16 | 2022.11.01   | 2,000 ReserveTON | 100,000 TON |
| 17 | 2022.12.01   | 2,000 ReserveTON | 100,000 TON |
| 18 | 2022.12.31   | 2,000 ReserveTON | 100,000 TON |
| 19 | 2023.01.30   | 2,000 ReserveTON | 100,000 TON |
| 20 | 2023.03.01   | 2,000 ReserveTON | 100,000 TON |
| 21 | 2023.03.31   | 2,000 ReserveTON | 100,000 TON |
| 22 | 2023.04.30   | 2,000 ReserveTON | 100,000 TON |
| 23 | 2023.05.30   | 2,000 ReserveTON | 100,000 TON |
| 24 | 2023.06.29   | 2,000 ReserveTON | 100,000 TON |
| 25 | 2023.07.29   | 2,000 ReserveTON | 100,000 TON |
| 26 | 2023.08.28   | 2,000 ReserveTON | 100,000 TON |
| 27 | 2023.09.27   | 2,000 ReserveTON | 100,000 TON |
| 28 | 2023.10.27   | 2,000 ReserveTON | 100,000 TON |
| 29 | 2023.11.26   | 2,000 ReserveTON | 100,000 TON |
| 30 | 2023.12.26   | 2,000 ReserveTON | 100,000 TON |
| SUM |  | 60,000 ReserveTON | 3,000,000 TON |

## [DAOTON](https://etherscan.io/address/0x08368cf6c32f5ca0ac80f7bc9da768fc775e9cd7)

1. Vault parameters
| Token supply | [350,000](https://etherscan.io/tx/0x7053a5f3864050fa6420afc990be701b55570dc850414285fdd6a50f31427bd2) DAOTON |
| --- | --- |
| Swap ratio | [50](https://etherscan.io/tx/0x86a3881caf83b7e71a9e364a893771aa61fa1864a5361f7b75284c11fdad088d) TON per 1 DAOTON |
| Total locked TON | [350,000](https://etherscan.io/tx/0x7053a5f3864050fa6420afc990be701b55570dc850414285fdd6a50f31427bd2) DAOTON x [50](https://etherscan.io/tx/0x86a3881caf83b7e71a9e364a893771aa61fa1864a5361f7b75284c11fdad088d) TON per 1 DAOTON = 17,500,000 TON |
1. Unlock Information
| Unlock Round | Date (GMT+09:00) | DAOTON | Equivalent TON |
| --- | --- | --- | --- |
| 1 | [2021.01.10](https://etherscan.io/tx/0xf9597fd1d9f7456b05c787e2bc0bcbba73b5bea603104e2c3bd2e563779c2ae2) | 350,000 DAOTON | 17,500,000 TON |
| SUM |  | [350,000](https://etherscan.io/tx/0xf9597fd1d9f7456b05c787e2bc0bcbba73b5bea603104e2c3bd2e563779c2ae2) DAOTON | [17,500,000](https://etherscan.io/tx/0x86a3881caf83b7e71a9e364a893771aa61fa1864a5361f7b75284c11fdad088d) TON |

# Swap Contracts

> [!note]
> 📌 The policy for swapping tokens in the TON (Tokamak Network Token) circulation system is stored in Ethereum network. **The token swap contract applies rules for the circulating supply, timing of coin circulation, and allocation of newly circulated coins. **Because these rules are defined in the smart contract, nobody, including the system's developers, can change the contract or its rules.

- [VestingSwapper](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61) (Seed**TON**, Private**TON**, Strategic**TON, **Marketing**TON)**
- [Swapper](https://etherscan.io/address/0x8db1fdfda8d1024f8a5b5dced5ec1918435f2fc8) (Marketing**TON, **Team**TON, **Advisor**TON, **Business**TON, **Reserve**TON, **DAO**TON)**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fc262c27-4d4e-4d76-add6-c384f76e55f8/SwapDiagram.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EMJKLIM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzKMAudFKA7drnE7DU%2Bv0R3CpjFLr%2B5xVIL7ag8P2xvgIgWKdKeQaWkTjbbkE%2BzNgNmI6VbwnIfYz60kcj7uzL%2FF0q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAB9%2FYj2ORZEGZ5FjyrcAyeInMValwRux7%2BeAPbvkvKPksiLjC%2B6yiTfuxJoRT5agyofLBlOwr2EUrYM%2BUwekenMa5lZi%2BdydwQ1ktnSNPYBPq7MlEOjV%2FQPQFowTrnZjQhx5xBQ5gMwFwdTy%2BaY9wy71ozbIx5xwoYtQ51cxwNvN4pX5fVCWGRa0aabFjVHil%2By1yv0vTOYwB0HAG88j5mIxYcbaICUTY2L4FVkmYCTjko%2FIZV%2Bn9qIKDhjf8XcAE8hRRNY%2FeUVaBZouv6GPPVbv%2BlAIjIh2ip0GYVTrWQHMDY2ld%2FNPupo5ELodWEeN0fAEdsa5vHn3L9fWR1OsxrduaibjPj%2FmQMLZVwilaNXxsuIoIiWdu46u9PSnCFhFGhyQc954R%2BPDJSNJbMfcTQgZatnTGEaw70twApAL%2BbnbOleNmWgSZx3ECAQuF%2BxF%2FnW5NIG8Q23LItM6qGdDWfSVf2UL%2BybwdCyFaNbRWCH6YVtMp5XyK0L00igfRutMXGW%2BMoOGBRA6mRnI%2FEvlB96nzfqgg84X5XAMonaz2RkGf96Ngqc7S8ys5K%2FgyTtutABag3VHWQgYl5rQVHp218VXrUXrj7KHSuQuuNh1Co2EbbRPKEPFejroNtMcRY8ZtXw1NTCtb7mw37KMP3v2swGOqUBwusE2lTYVOmQBUaFO7gJekfILD%2BGblAnEQJZagc7TywbRWXBEeZzW8Inifhc%2BiI25sTLbY8h4%2B4DBv6W0lK2bSwSXL3PQuU7cdKf1%2F6JMyuToD%2BomRGnrn%2Bpgw7Pb7RRC3dfYykodafd7gsPsZejsvq5k8oRWCERO5E6%2Fk68JArCsTGBbeY3%2FqLck0wYoEE1doVd8fohJ4sGPJaxHnwLv2O5o4fG&X-Amz-Signature=cb11388a68d80bfa979c1457415b51c4293b0ae3520c6b045cb5e9dcea2d1a4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)