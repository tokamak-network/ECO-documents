proxy : [sepolia.etherscan.io](https://sepolia.etherscan.io/address/0xb62Cff55292EC561e76B823ce126A806874a392E#readProxyContract)

gnosis safe : [sepolia.etherscan.io](https://sepolia.etherscan.io/address/0x29fcb43b46531bca003ddc8fcb67ffe91900c762#code)

[https://github.com/safe-global/safe-smart-account/blob/main/contracts/SafeL2.sol](https://github.com/safe-global/safe-smart-account/blob/main/contracts/SafeL2.sol)

[https://github.com/tokamak-network/safe-smart-account](https://github.com/tokamak-network/safe-smart-account)

# Test (on sepolia)

gnosis safe wallet [https://app.safe.global/welcome/accounts](https://app.safe.global/welcome/accounts)

: [https://app.safe.global/home?safe=sep:0xb62Cff55292EC561e76B823ce126A806874a392E](https://app.safe.global/home?safe=sep%3A0xb62Cff55292EC561e76B823ce126A806874a392E)

[https://docs.tally.xyz/knowledge-base/managing-a-dao/gnosis-safe#tally](https://docs.tally.xyz/knowledge-base/managing-a-dao/gnosis-safe#tally)

[https://docs.tally.xyz/knowledge-base/managing-a-dao/dao-settings](https://docs.tally.xyz/knowledge-base/managing-a-dao/dao-settings)

[https://docs.tally.xyz/knowledge-base/managing-a-dao/gnosis-safe#what](https://docs.tally.xyz/knowledge-base/managing-a-dao/gnosis-safe#what)

Multi sig git → DAO v1 의 멤버 변경에 따라 자동으로 멤버 변경을 요청할 수 있도록 해야 한다. 

[Link](https://github.com/gnosis/MultiSigWallet)

- 

# Tokamak DAO v2 (on sepolia)

1. Security Councils (multi-sig wallet) 만들기 
  1.  9 of 12 multi-sig 
  1.  7 of 12 multi-sig 
1. SecurityCouncilManager 에 의해서 multi-sig wallet의 signer 변경가능한지 검토한다.
  1. 타임락에 스케쥴링을 해서 실행해야 한다. (?)
  1. 