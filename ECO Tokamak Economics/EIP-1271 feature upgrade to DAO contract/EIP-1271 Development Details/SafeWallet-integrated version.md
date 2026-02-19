repo :  [GitHub - tokamak-network/ton-staking-v2 at safeWallet-protocol](https://github.com/tokamak-network/ton-staking-v2/tree/safeWallet-protocol)

Contract : [https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/DAOCommittee_V2.sol#L164-L411](https://github.com/tokamak-network/ton-staking-v2/blob/safeWallet-protocol/contracts/dao/DAOCommittee_V2.sol#L164-L411)

- DAOContract는 SafeWallet의 Signer로 검증하였을때 signer를 복구하여서 확인하며 Hash값에 대한 Signature는 2개이상이와서 검증을 진행하여야함 
- Signature의 Hash값이 다르거나 Signature를 중복으로 넣게되면 중복은 Singer가 나오더라도 Signer로 추가되지 않음 (다른 Signer가 Sign해야함)
- 이는 EIP-1271의 표준이 아닌 SafeWallet의 형태로 된 Hash값과 서명만 검증이 가능함 (표준으로 sign하고 검증할시 에러 발생)
- 필요시 EIP-1271표준 기능도 추가가능함
- DAOContract에 isOwner함수가 추가됨 → isOwner함수는 MultiSigWallet의 Owner들 값을 리턴함 (isOwner함수가 없을 시 SafeWallet에서 검증 불가)

## Kevin’s 1st Feedback

- 정확히 어떤걸 위해서 하는 것인지 이해가 안됨 → 정리 후 다시 미팅 필요
- DAO Agenda 통과를 위해서 하는 것이니 더 배경 설명이 필요함 
- Kevin을 이해시키는 것 보다 불특정 다수 투자자들을 이해시켜야함 (DAO는 Kevin이 통과시키는 것이 아니라 다수의 TON 투자자들을 이해시켜야함)