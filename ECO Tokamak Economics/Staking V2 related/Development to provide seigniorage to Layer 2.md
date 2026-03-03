# Discussion on needs 

[[discussion about Layer2Manager managing L2 TVL]]

[https://docs.google.com/presentation/d/1hBDp7KL41i7dZX2bwALLymPVVByPZVfhq3hTgCP_rkY/edit#slide=id.g26bb3a29bd9_0_0](https://docs.google.com/presentation/d/1hBDp7KL41i7dZX2bwALLymPVVByPZVfhq3hTgCP_rkY/edit#slide=id.g26bb3a29bd9_0_0)

# Query  the TON TVL of Layer2x

### on Titan

We used mapping `deposits`variable in L1StandardBridge for L1 ERC token deposited. We can query it using L1 token address and L2 token address. you can test [this](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#readProxyContract)

### on Thanos, on On-demand-L2

We will provide `depositedAmount`in OptimismPortal contract for querying TON TVL. ([source](https://github.com/tokamak-network/tokamak-titan-canyon/blob/8f40245f68d861ad17165431c7c93806bcf6bda0/packages/tokamak/contracts-bedrock/src/L1/OptimismPortal.sol#L75))

# Contract Relations

[https://app.diagrams.net/#G1wKnYpwnyX4zuUlNhUlYcU2MGK4vdfZ1k#{"pageId"%3A"FWIDIvq44IJMgAup5Hyy"}](https://app.diagrams.net/#G1wKnYpwnyX4zuUlNhUlYcU2MGK4vdfZ1k#%7B%22pageId%22%3A%22FWIDIvq44IJMgAup5Hyy%22%7D)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/957a8d6a-9bde-4624-8851-9a00b86f2874/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.31.37.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7XKGK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDY1GFTgnZzPzdcMJM2HZMj4IVm81DuEP13kgoYIW9WUAiAGpDoSx60XXxHkuozZmmMRTP77NJpgo8Vk9A5bePggXCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMM4FtKBHT%2FXZ%2FEkIJKtwDpB%2BRAOBxN4LGf1b9CJiWrjGbeLCj36yAxB%2Bl%2BKLVFUR2pdWAPDpcTWgcYCIC5uz%2B8qT7bSU1C2S0jJFg7Qts2pURiIl3455wzVsDxy3OKpg5lpLZ0P9Yz3zBq%2FMnHNYlsYaoTvttZ5aldzY6HEJtOPBpZsSVCa1ZtI%2FfOHnNmKXB8Vk5FtJxl1qrwkM4oaxCYQdBH9y1%2BEz6yGafDoR4FwhGk%2BOs2GE1u%2FkREX7zybgVsEMpWpEPNE6zxAhaz2vhhuK6UAIhhlarTNDHsT0VoePXVIWNZfSZ2PrONlfg2RpejYoIcz1%2FQ78CHunksn6Win0OnJ0AUmqDYYhdbZPYSi65t4lJEr%2BsRNaS78fhtwJkKrFcrt3pCrSis0JaJ2fcToFBSl8QLtTX%2B8AJA7KVBOzf6i4DaGeyY%2BINTfCsCaKp653vInNIlayB%2BQcyNoZZcSlFDDbd9DGNrs%2B5m%2FntggzQxLreSyGBf3xBpt%2BpafI8%2BR5lwvbVPcJZjes2%2FKdUZS9D6%2B3Lm7g4l6%2BQ6f2xRwE2b8QR1mn38lP8bxEyJo0bHN22oMGRPaNCLYeMVgAqBKgY9dfavqEMK2l42XCFzcm0Qkgug6EDWVGHZdZxY1KW55tGSLpR67P0REwwwJjbzAY6pgECFkeEMPSevG0DHIWW8KmIG%2FiPn92FWobELeU0yfDRAqa6bBAlTOqy%2B6FkfBp%2BG0nlmzemCKjrZC0A%2BRUK4o2w7r4ChqVFPp1pTtPADdyByTiwCrS%2F6vsFP6Vp1QA9ZmHcusv4MDhsw0B9ZSQRctqKhp%2FE9N3zxAfTG3vjYQkvzym9NiS1NmNGngdvM3JuwSmXo%2BSVJQEURi8unl591lD9FlS%2F9E8Q&X-Amz-Signature=c6b676b88ddbed833c29c76e78820dabd591cad92243c17bfaf3c03b9f5a1c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Contracts Details 

[[L2Registry]]

[[OperatorFactory]]

[[Layer2Manager]]

[[Operator]]

[[Layer2CandidateFactory]]

[[Layer2Candidate]]

[[SeigManagerV1_3]]

# [For core-team] Interface to give seigniorage to Layer2 sequencer 

[[[for core-team] Interface to give seigniorage to Layer2 sequencer (deprecated)]]

[[[for core-team] Interface to give seigniorage to Layer2 sequencer  ]]

# [For Service] Interface for giving seigniorage to Layer2Candidate 

[[[For Service] Interface for giving seigniorage to Layer2Candidate (deprecated)]]

[[[For Service] Interface for giving seigniorage to CandidateAddOn’s OperatorManager ]]

# Model

[https://docs.google.com/spreadsheets/d/1GKi5zEhSSRLz07PtHotioeUdZlyPGBxnipBu5h9Q1qw/edit#gid=0](https://docs.google.com/spreadsheets/d/1GKi5zEhSSRLz07PtHotioeUdZlyPGBxnipBu5h9Q1qw/edit#gid=0)

# Audit 

[[Audits for Layer2Candidate ]]

# Additional considerations

[[The process for stopping seigniorage issuance to Layer2Candidate]]

# Documentation 

[[TON Staking V2 [KR] (deprecated)]]

[[TON Staking V2 [KR]]]

[[TON Staking V2 [EN] (deprecated)]]

- Korean Version : [git link ](https://github.com/tokamak-network/ton-staking-v2/blob/15-create-a-document/docs/kr/ton-staking-v2.md)
- English version : [git link](https://github.com/tokamak-network/ton-staking-v2/blob/codeReview/docs/en/ton-staking-v2.md) 

# Contract addres 

[[simple staking contract address ]]

[[dao contract addresses ]]

[[Register Layer2Candidates (titan-sepolia, thanos-sepolia) on sepolia simple staking ]] 