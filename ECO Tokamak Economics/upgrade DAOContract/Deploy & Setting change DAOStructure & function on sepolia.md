Repo : [https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure](https://github.com/tokamak-network/ton-staking-v2/tree/NewDAOStructure)

# ~~Deploy process~~

DAOCommitteeProxy2 : [https://sepolia.etherscan.io/tx/0x47e1b9a50146af4c3e667231a4a960e61761c19968183ff12098ff0a2e13013e](https://sepolia.etherscan.io/tx/0x47e1b9a50146af4c3e667231a4a960e61761c19968183ff12098ff0a2e13013e)

DAOCommittee_V1 : 

[https://sepolia.etherscan.io/tx/0xf9119ecbc293f48311c570197ea927e8e8dbc35dce21f5cf347d5eedd734123a](https://sepolia.etherscan.io/tx/0xf9119ecbc293f48311c570197ea927e8e8dbc35dce21f5cf347d5eedd734123a)

DAOCommitteeOwner :

[https://sepolia.etherscan.io/tx/0x3ba06437343a11887c844304f65bb305decdfc8b770a2aced8c6485acfcdfb27](https://sepolia.etherscan.io/tx/0x3ba06437343a11887c844304f65bb305decdfc8b770a2aced8c6485acfcdfb27)

# ~~Setting Process~~

1. upgradeTo : DAOCommitteeProxy → DAOCommitteeProxy2 ([https://sepolia.etherscan.io/tx/0xe4235755cd9cdf8b63284322313794f9e7f1f4d00a8e336667f534f3314a2048](https://sepolia.etherscan.io/tx/0xe4235755cd9cdf8b63284322313794f9e7f1f4d00a8e336667f534f3314a2048))
1. upgradeTo2 : DAOCommitteeProxy2 → DAOCommittee_V1 ([https://sepolia.etherscan.io/tx/0x0983001ef5abc3429556885eb9f83955dd7adb0b5e9a7ccb4a250b4bf1bea93d](https://sepolia.etherscan.io/tx/0x0983001ef5abc3429556885eb9f83955dd7adb0b5e9a7ccb4a250b4bf1bea93d))
1. setAliveImplementation2 to DAOCommittee_V1 ([https://sepolia.etherscan.io/tx/0x68ff7347e8acbb7ce9d3e9e87f5ced68f6150a7744a3353f8fa3df33781850a4](https://sepolia.etherscan.io/tx/0x68ff7347e8acbb7ce9d3e9e87f5ced68f6150a7744a3353f8fa3df33781850a4)) (안해도 되는 과정?)
1. setImplementation2 to DAOCommittee_V1 ([https://sepolia.etherscan.io/tx/0xa90c81bf432324b1b46c7fcc41ccd971aabe13de4a902745b2ce494133451e59](https://sepolia.etherscan.io/tx/0xa90c81bf432324b1b46c7fcc41ccd971aabe13de4a902745b2ce494133451e59)) (안해도 되는 과정?)
1. setAliveImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0x2f6bf4848f43f2e6bca3f8fd8fa841e371ed05fb77f1f453caf41ef024c57e54](https://sepolia.etherscan.io/tx/0x2f6bf4848f43f2e6bca3f8fd8fa841e371ed05fb77f1f453caf41ef024c57e54))
1. setImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0x02b2bcf3d2c50ca2b4d3a60eff80a532d4a9c7d002e6163b483f30de1be72297](https://sepolia.etherscan.io/tx/0x02b2bcf3d2c50ca2b4d3a60eff80a532d4a9c7d002e6163b483f30de1be72297))
1. setSelectorImplementations2 DAOCommitteeOwner functions ([https://sepolia.etherscan.io/tx/0x2647f34470fc58a159c624a590fa38309e8e27fdee2e2a12a088b3dc53eaac4e](https://sepolia.etherscan.io/tx/0x2647f34470fc58a159c624a590fa38309e8e27fdee2e2a12a088b3dc53eaac4e))
1. setLayer2CandidateFactory, setLayer2Manager 필요?

# ~~Deploy Address~~

```javascript
DAOCommitteeProxy : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386
DAOCommitteeProxy2 : 0x5FBb951E7B7a3E2e947AF7E8565b15AA11e670fE
DAOCommittee_V1 : 0x324715873db4fc19057acE49eD17dA0a93Ae2310
DAOCommitteeOwner : 0xaF23260F74806641e3307Eb567C57a4640861080
```

# Deploy process

DAOCommitteeProxy2 : [https://sepolia.etherscan.io/tx/0x24d09ee948c7ec34efc59b398ff8787664cd0483566dbec58ae47af6db84be67](https://sepolia.etherscan.io/tx/0x24d09ee948c7ec34efc59b398ff8787664cd0483566dbec58ae47af6db84be67)

DAOCommittee_V1 : 

[https://sepolia.etherscan.io/tx/0x405bea29151cccb0437ad6d07e481f5a51deb3b0776eff7ed8e9a31638c15bdf](https://sepolia.etherscan.io/tx/0x405bea29151cccb0437ad6d07e481f5a51deb3b0776eff7ed8e9a31638c15bdf)

DAOCommitteeOwner :

[https://sepolia.etherscan.io/tx/0x967195325117e0b69370485dc974a3f3834a10d2788fe4d627e829eda3d233c5](https://sepolia.etherscan.io/tx/0x967195325117e0b69370485dc974a3f3834a10d2788fe4d627e829eda3d233c5)

# Setting Process

1. upgradeTo : DAOCommitteeProxy → DAOCommitteeProxy2 ([https://sepolia.etherscan.io/tx/0x47cb932528ab1e9cb0b9e0b54f1c7c20c2409c5802d4d07ee8ae0b69a03394d9](https://sepolia.etherscan.io/tx/0x47cb932528ab1e9cb0b9e0b54f1c7c20c2409c5802d4d07ee8ae0b69a03394d9))
1. upgradeTo2 : DAOCommitteeProxy2 → DAOCommittee_V1 ([https://sepolia.etherscan.io/tx/0x248c7bb883e8f7f4417bcd001d3800dcaacb56cbe32ce857ac8b3291362c7fa0](https://sepolia.etherscan.io/tx/0x248c7bb883e8f7f4417bcd001d3800dcaacb56cbe32ce857ac8b3291362c7fa0))
1. setAliveImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0x5c5a623c289b10476af93f445faa3d980fa9894f4e477dfb6afcba76cb027e32](https://sepolia.etherscan.io/tx/0x5c5a623c289b10476af93f445faa3d980fa9894f4e477dfb6afcba76cb027e32))
1. setImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0xb6858fc6a545109bff05b705fb8c80896d39a8ef8bbd88f0dd01f2bbdab70abb](https://sepolia.etherscan.io/tx/0xb6858fc6a545109bff05b705fb8c80896d39a8ef8bbd88f0dd01f2bbdab70abb))
1. setSelectorImplementations2 DAOCommitteeOwner functions ([https://sepolia.etherscan.io/tx/0x5cd457d2edbf193b1e2bbed230ec3ed61391774a6f8b2dc9c5632efaba3fa4c6](https://sepolia.etherscan.io/tx/0x5cd457d2edbf193b1e2bbed230ec3ed61391774a6f8b2dc9c5632efaba3fa4c6))
1. setLayer2CandidateFactory ([https://sepolia.etherscan.io/tx/0xe673a57a9b71b8993317d9c708745c5a40fabde2068bdb2ed0b8ca9cf5b36a43](https://sepolia.etherscan.io/tx/0xe673a57a9b71b8993317d9c708745c5a40fabde2068bdb2ed0b8ca9cf5b36a43))
1. setLayer2Manager ([https://sepolia.etherscan.io/tx/0x48d9451caed05e522a0b42c3f8fe766314c4b1e8477004bbb62eaf0f18a41e82](https://sepolia.etherscan.io/tx/0x48d9451caed05e522a0b42c3f8fe766314c4b1e8477004bbb62eaf0f18a41e82))

# Deploy Address

```javascript
DAOCommitteeProxy : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386
DAOCommitteeProxy2 : 0x0cb4E974302864D1059028de86757Ca55D121Cb8
DAOCommittee_V1 : 0xB800a42D9A8e5036B75246aeDA578DCe58f85B18
DAOCommitteeOwner : 0x34B6e334D88436Fbbb9c316865A1BA454769C090
Layer2CandidateFactory: 0x770739A468D9262960ee0669f9Eaf0db6E21F81A
Layer2Manager: 0x0237839A14194085B5145D1d1e1E77dc92aCAF06
```

# Deploy process (24.09.19)

DAOCommitteeProxy2 : [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0xc1d1aca1122c6a36dd2525ea62aeb8de8029e4ddef1129cde41300212d4d3db9)

DAOCommittee_V1 : [Contract Address 0xaDf24e3885D4c8DB092514dF364b09f314F1e794 | Etherscan](https://sepolia.etherscan.io/address/0xaDf24e3885D4c8DB092514dF364b09f314F1e794)

DAOCommitteeOwner :[sepolia.etherscan.io](https://sepolia.etherscan.io/address/0x63f116823B6Ed37271B0204A51e8ea4Eaa09c9a6)

# Setting Process

```bash
SelectorBytes :  [
  '0x401e23e6', '0xbaa12536', '0x4e24ce49',
  '0xe93d3a1d', '0xe9152a33', '0x4a15efa7',
  '0x342478c2', '0x7657f20a', '0xa1f3ac2a',
  '0xefd57979', '0x81bfe42c', '0x38d1b17c',
  '0x9d65b531', '0xebf97be6', '0x0ef646ad',
  '0x0c536c52', '0x4b799db1', '0x2af60ff4',
  '0x49c39f14', '0x047f52f2', '0x4d288fec',
  '0xaef2c585', '0x6da8f3ce', '0xc1ba4e59',
  '0x50e8f17d', '0x74d58f48', '0x5ebe7622',
  '0x69154295', '0x5c43030f', '0xb4f69b6a',
  '0x23d09fdf', '0xc0bc5304', '0x69b1227a'
]
```

1. upgradeTo : DAOCommitteeProxy → DAOCommitteeProxy2 ([https://sepolia.etherscan.io/tx/0xc9aea1578414a3d3436077ac32c5c71a9a486cd7627433e9ff1f4dbfe0fbf91f](https://sepolia.etherscan.io/tx/0xc9aea1578414a3d3436077ac32c5c71a9a486cd7627433e9ff1f4dbfe0fbf91f))
1. upgradeTo2 : DAOCommitteeProxy2 → DAOCommittee_V1 ([https://sepolia.etherscan.io/tx/0xc03f8a479fc668379e017dd1672d7192d86872944ade3f2a9fe4e9a6e7ad9f15](https://sepolia.etherscan.io/tx/0xc03f8a479fc668379e017dd1672d7192d86872944ade3f2a9fe4e9a6e7ad9f15))
1. setAliveImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0x656cd3f7d67d32d66dedcfbb3876c106563853bd497ee5d681822c8cc7674efb](https://sepolia.etherscan.io/tx/0x656cd3f7d67d32d66dedcfbb3876c106563853bd497ee5d681822c8cc7674efb))
1. setImplementation2 to DAOCommitteeOwner ([https://sepolia.etherscan.io/tx/0xff87f9b47a4aba0beb5a0df6bcb09aaf7433ad0f874a07734ddab392129d3fd6](https://sepolia.etherscan.io/tx/0xff87f9b47a4aba0beb5a0df6bcb09aaf7433ad0f874a07734ddab392129d3fd6))
1. setSelectorImplementations2 DAOCommitteeOwner functions ([https://sepolia.etherscan.io/tx/0x803c5b2b8cc28d5e40b7942af534c7f8dda41e415630fa8ae99ce44bbf030714](https://sepolia.etherscan.io/tx/0x803c5b2b8cc28d5e40b7942af534c7f8dda41e415630fa8ae99ce44bbf030714))
1. setCandidateAddOnFactory ([https://sepolia.etherscan.io/tx/0xb1f40baea8c5b7890f849f73cb3072e1c04cdd8072c0c908d6aa52ac9dc840a4](https://sepolia.etherscan.io/tx/0xb1f40baea8c5b7890f849f73cb3072e1c04cdd8072c0c908d6aa52ac9dc840a4))
1. setLayer2Manager ([https://sepolia.etherscan.io/tx/0x3970a44e468acdf97b733f048edc741fd30666ad0dd2cd69d984eec4b79f5ff8](https://sepolia.etherscan.io/tx/0x3970a44e468acdf97b733f048edc741fd30666ad0dd2cd69d984eec4b79f5ff8))
1. setTargetSetL1BridgeRegistry () [SeigManager확인결과 주소 일치하여서 수정안함]

# Deploy Address

```javascript
DAOCommitteeProxy : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386
DAOCommitteeProxy2 : 0x399A7Aa3BF8da93319494CdFC495Ab20541eC1D4
DAOCommittee_V1 : 0xaDf24e3885D4c8DB092514dF364b09f314F1e794
DAOCommitteeOwner : 0x63f116823B6Ed37271B0204A51e8ea4Eaa09c9a6
Layer2ManagerProxy: 0xffb690feeFb2225394ad84594C4a270c04be0b55
CandidateAddOnFactory: 0x63c95fbA722613Cb4385687E609840Ed10262434
```