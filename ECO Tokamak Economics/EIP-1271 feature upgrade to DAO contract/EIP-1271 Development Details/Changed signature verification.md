issues : [https://github.com/tokamak-network/ton-staking-v2/issues/329](https://github.com/tokamak-network/ton-staking-v2/issues/329)

# Background to the change

다음 이슈에서 서명 검증 정책이 MultiSigWallet 정책과 맞지 않다는 의견이 나왔고 해당 의견이 맞다고 판단되어서 서명 검증 로직을 변경하였습니다.

그래서 기존 MultiSigWallet의 Owner 중 한명이 Sign을 하여도 검증 통과에서 MultiSigWallet의 정족수인 numConfirmationsRequired값 이상의 Owner가 Sign을 하여야 통과되도록 변경하였습니다.

(1명의 Owner가 Sign하면 검증 통과 → 2명이상의 Owner가 Sign해야 검증 통과)

In the following issue, it was suggested that the signature verification policy did not align with the MultiSigWallet policy. This opinion was confirmed, and the signature verification logic was modified.

Therefore, even if just one owner of the existing MultiSigWallet signs, verification will only pass if more than the numConfirmationsRequired number of owners sign.

(Verification passes if 1 owner signs → Verification passes if 2 or more owners sign)

# How to change

LLM 프롬프트를 변경하여서 변경하였습니다.

I changed it by changing the LLM prompt.

commit : [https://github.com/tokamak-network/ton-staking-v2/commit/6a49801408d97fca3d4a64aa71826a4696723f7b](https://github.com/tokamak-network/ton-staking-v2/commit/6a49801408d97fca3d4a64aa71826a4696723f7b)

LLM프롬프트로 변경 시 Contract로직은 잘 변경해주나 Test코드 작성 시 부족한 점이 있었음

When changing to the LLM prompt, the contract logic was changed properly, but there were some shortcomings when writing the test code.

# How to Test

```solidity
npx hardhat test test/EIP1271.upgrade.test.ts --network hardhat 
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/327e6d60-2e47-47e0-ae91-1456b47b52bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS5F3YH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCi1jM%2BqFUyvywBZLuO8%2FYoSc8F86psmbGYyj95Son4cgIhAOmqcUtuxlWq%2Bx0Blx1bk%2FEpP1ikQQkKWVAfKUAOoXewKv8DCHQQABoMNjM3NDIzMTgzODA1IgwRhUwE65iaXQc5WLgq3AMFeryIOEUEg9F4zRNH%2FM%2FaTXeoBh6UVE6F3NYbc3i0OXX8XcOvtRoOFQil4cNFKhVIHygeYQKCwrlzydDEPkzPYSA68ofqN1Xb36NoBTdGbBOLkx2jgZWzBzEbMdI7O6NLi083TemHtX6fxUCYRKur0OnawJcJpDX3UpCOFP9pOb7nJApQweV2YLpK7p0szjgUza2DBLL8uEhZdn8mQ%2BP4BEQrsaRCNq071%2FVnilJDt2Nd2NARfLpfqA32w5pz8eKTtZmvSeJJGGMTrt%2BFXu8yQwYMwDesTxv242PszATGKshgniw%2F%2B4Us6wGPMIiMFW00uDCepH5ZmHDE0YUkra2d38lJgFiqUBbxHQjlm8NMtgwPS5vtpsJwqZ8wvX0JuH3LnE4ofqmvALNce%2F4%2FXXs1wwq5qsUPrBDV8lUWabeAbgNHUwe6HRgG1cB%2FoDH3XodM7ygMJLZcl7JsY20vsZ0oZYub9JFGraYSQnrkS9y1F7izW07U9qnkLtZUaT%2FzCZt5bmxQh6jVXXMyRGX0TrahQ%2F%2B2EShbPCxlGI1PIxDXUnCsgv%2F9n3QC7xAvIHyO44qJVmZPltpjryUwg463MGsggrpmz1De%2BhfWagOdpcHcHpETfEgeIRuiamGmODCr8NnMBjqkATV1aBuqOfrP0ddjpUGn2Wa67OA98iKcbe4sRijKMu4Ty2%2BMcoSyUo6UkzJxcpwMwcvhzRfIBNdPru9Y7KVKypJjgfDAExDHCholHzfkvWCH28aq8zepFitnwG%2F90TSZmfGaG%2Bzag4SdV1qkVT2t0sV7BvabhXe6HnGuJ50MfAnlJS30BxOxUzF5dRMMgTt%2BHeziGcbPkBfjod7WqCjp%2FvV0m4JG&X-Amz-Signature=3fdcaad19169f5632dc0b90cf1ea674c8cc3af921c878b83716148f90e4f2456&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Deployed & Setting on Sepolia

contract : [https://sepolia.etherscan.io/address/0x4c20f793bD3F4106819c9a705670D30E18bdB983#code](https://sepolia.etherscan.io/address/0x4c20f793bD3F4106819c9a705670D30E18bdB983#code)

DAOCommitteeProxy2 upgradeTo2 DAOCommittee_V2 : [https://sepolia.etherscan.io/tx/0xbbcfa89afead496e59c84289dc2f06dfde841a9fb3dd313377af78399a3f5603](https://sepolia.etherscan.io/tx/0xbbcfa89afead496e59c84289dc2f06dfde841a9fb3dd313377af78399a3f5603)

# Develop the SafeWallet-Protocol

Repo : [https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/main](https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/main)

branch1 : [https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/firstKIRO](https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/firstKIRO)

branch2 : [https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/gemini](https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/gemini)

branch3 : [https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/cursor](https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/cursor)

branch4 : [https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/Self-development](https://github.com/tokamak-network/safeWallet-ProtocolKit/tree/Self-development)

I ran several tests to find out what the problem was.

## (1) Test1 (Fail)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit5DAO.ts
```
- If DAOContract is one of SafeWallets, the owner of DAOContract is MultiSigWallet, and two of the owners of MultiSigWallet sign.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6ed7b684-3069-45b6-80b0-3103639c9726/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS5F3YH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCi1jM%2BqFUyvywBZLuO8%2FYoSc8F86psmbGYyj95Son4cgIhAOmqcUtuxlWq%2Bx0Blx1bk%2FEpP1ikQQkKWVAfKUAOoXewKv8DCHQQABoMNjM3NDIzMTgzODA1IgwRhUwE65iaXQc5WLgq3AMFeryIOEUEg9F4zRNH%2FM%2FaTXeoBh6UVE6F3NYbc3i0OXX8XcOvtRoOFQil4cNFKhVIHygeYQKCwrlzydDEPkzPYSA68ofqN1Xb36NoBTdGbBOLkx2jgZWzBzEbMdI7O6NLi083TemHtX6fxUCYRKur0OnawJcJpDX3UpCOFP9pOb7nJApQweV2YLpK7p0szjgUza2DBLL8uEhZdn8mQ%2BP4BEQrsaRCNq071%2FVnilJDt2Nd2NARfLpfqA32w5pz8eKTtZmvSeJJGGMTrt%2BFXu8yQwYMwDesTxv242PszATGKshgniw%2F%2B4Us6wGPMIiMFW00uDCepH5ZmHDE0YUkra2d38lJgFiqUBbxHQjlm8NMtgwPS5vtpsJwqZ8wvX0JuH3LnE4ofqmvALNce%2F4%2FXXs1wwq5qsUPrBDV8lUWabeAbgNHUwe6HRgG1cB%2FoDH3XodM7ygMJLZcl7JsY20vsZ0oZYub9JFGraYSQnrkS9y1F7izW07U9qnkLtZUaT%2FzCZt5bmxQh6jVXXMyRGX0TrahQ%2F%2B2EShbPCxlGI1PIxDXUnCsgv%2F9n3QC7xAvIHyO44qJVmZPltpjryUwg463MGsggrpmz1De%2BhfWagOdpcHcHpETfEgeIRuiamGmODCr8NnMBjqkATV1aBuqOfrP0ddjpUGn2Wa67OA98iKcbe4sRijKMu4Ty2%2BMcoSyUo6UkzJxcpwMwcvhzRfIBNdPru9Y7KVKypJjgfDAExDHCholHzfkvWCH28aq8zepFitnwG%2F90TSZmfGaG%2Bzag4SdV1qkVT2t0sV7BvabhXe6HnGuJ50MfAnlJS30BxOxUzF5dRMMgTt%2BHeziGcbPkBfjod7WqCjp%2FvV0m4JG&X-Amz-Signature=65c62ee76dc3605b80cd2e908717164e5fc21b5a0ff3f78b905b9576d8fe9c6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (2) Test2 (Fail)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit3.ts
```
- If one of the candidates for SafeWallet is MultiSigWallet

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/00298342-e0f8-4e31-90a4-243603662b2a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS5F3YH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCi1jM%2BqFUyvywBZLuO8%2FYoSc8F86psmbGYyj95Son4cgIhAOmqcUtuxlWq%2Bx0Blx1bk%2FEpP1ikQQkKWVAfKUAOoXewKv8DCHQQABoMNjM3NDIzMTgzODA1IgwRhUwE65iaXQc5WLgq3AMFeryIOEUEg9F4zRNH%2FM%2FaTXeoBh6UVE6F3NYbc3i0OXX8XcOvtRoOFQil4cNFKhVIHygeYQKCwrlzydDEPkzPYSA68ofqN1Xb36NoBTdGbBOLkx2jgZWzBzEbMdI7O6NLi083TemHtX6fxUCYRKur0OnawJcJpDX3UpCOFP9pOb7nJApQweV2YLpK7p0szjgUza2DBLL8uEhZdn8mQ%2BP4BEQrsaRCNq071%2FVnilJDt2Nd2NARfLpfqA32w5pz8eKTtZmvSeJJGGMTrt%2BFXu8yQwYMwDesTxv242PszATGKshgniw%2F%2B4Us6wGPMIiMFW00uDCepH5ZmHDE0YUkra2d38lJgFiqUBbxHQjlm8NMtgwPS5vtpsJwqZ8wvX0JuH3LnE4ofqmvALNce%2F4%2FXXs1wwq5qsUPrBDV8lUWabeAbgNHUwe6HRgG1cB%2FoDH3XodM7ygMJLZcl7JsY20vsZ0oZYub9JFGraYSQnrkS9y1F7izW07U9qnkLtZUaT%2FzCZt5bmxQh6jVXXMyRGX0TrahQ%2F%2B2EShbPCxlGI1PIxDXUnCsgv%2F9n3QC7xAvIHyO44qJVmZPltpjryUwg463MGsggrpmz1De%2BhfWagOdpcHcHpETfEgeIRuiamGmODCr8NnMBjqkATV1aBuqOfrP0ddjpUGn2Wa67OA98iKcbe4sRijKMu4Ty2%2BMcoSyUo6UkzJxcpwMwcvhzRfIBNdPru9Y7KVKypJjgfDAExDHCholHzfkvWCH28aq8zepFitnwG%2F90TSZmfGaG%2Bzag4SdV1qkVT2t0sV7BvabhXe6HnGuJ50MfAnlJS30BxOxUzF5dRMMgTt%2BHeziGcbPkBfjod7WqCjp%2FvV0m4JG&X-Amz-Signature=bc0795b816f9e7c14fc105e8e759c71b568a9d4b9defacf0b386f92fbbd1b427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (3) Test3 (Success)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit4SafeWallet.ts
```
- Retest with SafeWallet configuration

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f8759a52-c159-4c6b-8e93-7d50e8b08d41/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS5F3YH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCi1jM%2BqFUyvywBZLuO8%2FYoSc8F86psmbGYyj95Son4cgIhAOmqcUtuxlWq%2Bx0Blx1bk%2FEpP1ikQQkKWVAfKUAOoXewKv8DCHQQABoMNjM3NDIzMTgzODA1IgwRhUwE65iaXQc5WLgq3AMFeryIOEUEg9F4zRNH%2FM%2FaTXeoBh6UVE6F3NYbc3i0OXX8XcOvtRoOFQil4cNFKhVIHygeYQKCwrlzydDEPkzPYSA68ofqN1Xb36NoBTdGbBOLkx2jgZWzBzEbMdI7O6NLi083TemHtX6fxUCYRKur0OnawJcJpDX3UpCOFP9pOb7nJApQweV2YLpK7p0szjgUza2DBLL8uEhZdn8mQ%2BP4BEQrsaRCNq071%2FVnilJDt2Nd2NARfLpfqA32w5pz8eKTtZmvSeJJGGMTrt%2BFXu8yQwYMwDesTxv242PszATGKshgniw%2F%2B4Us6wGPMIiMFW00uDCepH5ZmHDE0YUkra2d38lJgFiqUBbxHQjlm8NMtgwPS5vtpsJwqZ8wvX0JuH3LnE4ofqmvALNce%2F4%2FXXs1wwq5qsUPrBDV8lUWabeAbgNHUwe6HRgG1cB%2FoDH3XodM7ygMJLZcl7JsY20vsZ0oZYub9JFGraYSQnrkS9y1F7izW07U9qnkLtZUaT%2FzCZt5bmxQh6jVXXMyRGX0TrahQ%2F%2B2EShbPCxlGI1PIxDXUnCsgv%2F9n3QC7xAvIHyO44qJVmZPltpjryUwg463MGsggrpmz1De%2BhfWagOdpcHcHpETfEgeIRuiamGmODCr8NnMBjqkATV1aBuqOfrP0ddjpUGn2Wa67OA98iKcbe4sRijKMu4Ty2%2BMcoSyUo6UkzJxcpwMwcvhzRfIBNdPru9Y7KVKypJjgfDAExDHCholHzfkvWCH28aq8zepFitnwG%2F90TSZmfGaG%2Bzag4SdV1qkVT2t0sV7BvabhXe6HnGuJ50MfAnlJS30BxOxUzF5dRMMgTt%2BHeziGcbPkBfjod7WqCjp%2FvV0m4JG&X-Amz-Signature=177def92c4c02110aa307bd5f1c9d55e959020733db0626caea334106db7ab21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (4) Test4 (Success)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit2-singleOwnerPass.ts
```
- Version composed by Singer

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/317ce4b3-dd2f-422f-97d3-65fba2ff7b26/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS5F3YH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCi1jM%2BqFUyvywBZLuO8%2FYoSc8F86psmbGYyj95Son4cgIhAOmqcUtuxlWq%2Bx0Blx1bk%2FEpP1ikQQkKWVAfKUAOoXewKv8DCHQQABoMNjM3NDIzMTgzODA1IgwRhUwE65iaXQc5WLgq3AMFeryIOEUEg9F4zRNH%2FM%2FaTXeoBh6UVE6F3NYbc3i0OXX8XcOvtRoOFQil4cNFKhVIHygeYQKCwrlzydDEPkzPYSA68ofqN1Xb36NoBTdGbBOLkx2jgZWzBzEbMdI7O6NLi083TemHtX6fxUCYRKur0OnawJcJpDX3UpCOFP9pOb7nJApQweV2YLpK7p0szjgUza2DBLL8uEhZdn8mQ%2BP4BEQrsaRCNq071%2FVnilJDt2Nd2NARfLpfqA32w5pz8eKTtZmvSeJJGGMTrt%2BFXu8yQwYMwDesTxv242PszATGKshgniw%2F%2B4Us6wGPMIiMFW00uDCepH5ZmHDE0YUkra2d38lJgFiqUBbxHQjlm8NMtgwPS5vtpsJwqZ8wvX0JuH3LnE4ofqmvALNce%2F4%2FXXs1wwq5qsUPrBDV8lUWabeAbgNHUwe6HRgG1cB%2FoDH3XodM7ygMJLZcl7JsY20vsZ0oZYub9JFGraYSQnrkS9y1F7izW07U9qnkLtZUaT%2FzCZt5bmxQh6jVXXMyRGX0TrahQ%2F%2B2EShbPCxlGI1PIxDXUnCsgv%2F9n3QC7xAvIHyO44qJVmZPltpjryUwg463MGsggrpmz1De%2BhfWagOdpcHcHpETfEgeIRuiamGmODCr8NnMBjqkATV1aBuqOfrP0ddjpUGn2Wa67OA98iKcbe4sRijKMu4Ty2%2BMcoSyUo6UkzJxcpwMwcvhzRfIBNdPru9Y7KVKypJjgfDAExDHCholHzfkvWCH28aq8zepFitnwG%2F90TSZmfGaG%2Bzag4SdV1qkVT2t0sV7BvabhXe6HnGuJ50MfAnlJS30BxOxUzF5dRMMgTt%2BHeziGcbPkBfjod7WqCjp%2FvV0m4JG&X-Amz-Signature=2f3198ffcea82cab2d08aac570f046c68391116e1b7c7daa74734d8e0fe412c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Remain issue : [https://github.com/safe-global/safe-core-sdk/issues/1264](https://github.com/safe-global/safe-core-sdk/issues/1264)