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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/957a8d6a-9bde-4624-8851-9a00b86f2874/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-02-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.31.37.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K4VH2KS%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDQ6WdcR6Lnl4nkmRvGCjXN0VnWQ4jGeRh7%2Ftx9f%2BRzQIhAOfqhTRCG%2FKPS3Bp%2FQV2vtsAKan2ppxgZuQGpkraX09PKv8DCHQQABoMNjM3NDIzMTgzODA1IgxRNn%2FMmDQeaa1R3BMq3AMHK4TUvIMjIhDyP2NbFXO%2B%2FUCe%2FSKax%2BmGPCKDYGE1ItKVt35oWiwXfZb1V5NP0rA1woRjwPBSXYQYY2ljnFP7OclpJ%2BwCIr47IcWCaCHyO8s20mOTMJ3lVWJkj%2FVHw6PxBgs7IJJ3zoGLBqKz6hR4PKlvaC%2BhRL4F3Gugg%2FuVNzdVOcvZ3zn%2BG%2BLJuHu7HC%2FuYmvy995CCNs8HHoo%2By0k%2FkIvqs1SKdXlUAxsB68ekBQl9kK7e6svFZGuoKLCjeHWaVgn3P51%2FXIT2VdlwriMbo4z1bWk5QdiliGtM1XLzQAcDPq0dOC8NpE8fTVbLFkrFpGOwmiJbYIu2Yf08Ez%2BNo3JKD9ylVOvMRMW0ruezkVM3sy6zJp44ZQgpLJp57aHqhFuqGIGpAHrxM%2Fsd02xEtA8QsRuz7sAVIW%2Fr6zVu2kls%2FbeQWA5jlbg6zX7t8xK23x%2BQunmbchqSCjR%2BK6eRPftk401tK5TEVfK7sQP%2FDr3dfg%2BuAaadi%2Bo6MOn%2BRQhrtGBWg%2BRqnimkkmfKPScfSKXlEWAOgZL%2FpG6HsSWegvqaVf52mZ8KvLyAnQIVs628sIRAFxAIt78RMfQRYLW6taZmPheKfMNibii0XtTjCx55mQXVNnvrpL46jCy8dnMBjqkAfoBn%2FcpQLRhHtdqK49ljp5Zcu4oX8Eoib3nK5pvQD8SDdo9hu5Ulilet9jJW8gtES7yEhvF7IWQ90vqedlEvqkvFT7oiJq1AH1WTuoBq%2F2XA1UGDI8QizMPF%2F3UABswr4ojiwglg97rEqHys9P%2FzmftAFr6n6dBDZRdUtxWScgTXRywRC3ETMw9zZ3L%2BcuyTkRfbfx6iISBhFE6axSdzmL2HdUg&X-Amz-Signature=8d79cd6e9f425fe60a2cb250ffeec3933b4b4129fe94e82b7a043b0ad43b22ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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