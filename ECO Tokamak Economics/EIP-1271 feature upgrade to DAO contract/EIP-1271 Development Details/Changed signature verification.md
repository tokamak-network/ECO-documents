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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/327e6d60-2e47-47e0-ae91-1456b47b52bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI6FWP7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPmP%2BuIcUfS0Sa1HpD%2Fpt9S%2BqqWjRqv%2FxMI3UjnAAgwwIgNZ2KxASxDNrcnmqwQtl5VfQGLLOXFC4bvQ9rGOgFfkwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDByUOKam00jaFoGyQCrcAwWuA7Az%2FfamgYbXS0zQWMKB8tSJAeIphNZHONPY7sIaAYVw7I7BMh6fgToxdgO9WHCDirU6JdjgTcPt4eSVig%2BjpMf96EAVCLDb8YDmS0AEw%2BVyPV%2BmWZ7ELhpIBMnf9xHYXuwkAmHqx4DCcciG9xykr9Ldpv9GxIjRiy7OAY4T14zPnmtvLepIPRtLNKXJmytJnGhsFpnLBZgkqucK0HQcUqoheeP51GRUKkJaC8L8jSRJZdez%2Bts%2FLAvekIYaIU4yDZUXg4QhdccD84rgaKlvcbPeGUTlvv2ajFGel6KVB4PTIfGmzVLoxp0cNpbMWVKpP5IhoIB2CKv%2FTMucHLPP%2B2LJems1u7Jv%2F5RECUBsz1CMkcR%2FK6LjDgqmRK2GeC3oLR%2FeqV7v0HM%2FO7pwgRknSd26dPAd%2FkjSlgj43KRzLpEeg56rz8ReNEDD6wEdtwbGPZxXmdEzwvjk1Djfk%2FCUySRXyyjk45eVkLik%2Bi24L2%2F0Xm3V%2BSlvRF2fFRW3TELGf%2BXW9KVvN%2FLJLGvffY%2B6QQWuqeh31MKp75jXtqIUC4kOH%2Bi1urbK7ts%2F8mUImUYIznW5jO1s6Hg6xTOodaPcxzw0yGqvGjOLNp29zxl%2FEA3tAoZXGdwZ%2B8NXMPOa28wGOqUB%2FlbT9xyhF12yLgQetE305iFSpM5OIcR9yXC%2F5l1Hnfa7Hdy2gdg8f1bBH4Xi9YEuMhCiiY6cI1bYb2EeOVONbLP%2B%2BE0mGibCyoceAtiMf0V%2FJOkBLLJ44sucehFoPFtp2wPibA2B1DpxmQZWgLw%2BYm74ENjUrodP8PEp4Nh2nAxup%2F8lEc%2B%2Flh%2FSWRsEwFoNp0D%2Fx0P4Yx5%2FmdOJJMEjJMIP1mzy&X-Amz-Signature=ea2bac88dbf94ec81e2b8aaf7341751cd56a1a5e5acf135af6aaaebc41b640f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6ed7b684-3069-45b6-80b0-3103639c9726/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI6FWP7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPmP%2BuIcUfS0Sa1HpD%2Fpt9S%2BqqWjRqv%2FxMI3UjnAAgwwIgNZ2KxASxDNrcnmqwQtl5VfQGLLOXFC4bvQ9rGOgFfkwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDByUOKam00jaFoGyQCrcAwWuA7Az%2FfamgYbXS0zQWMKB8tSJAeIphNZHONPY7sIaAYVw7I7BMh6fgToxdgO9WHCDirU6JdjgTcPt4eSVig%2BjpMf96EAVCLDb8YDmS0AEw%2BVyPV%2BmWZ7ELhpIBMnf9xHYXuwkAmHqx4DCcciG9xykr9Ldpv9GxIjRiy7OAY4T14zPnmtvLepIPRtLNKXJmytJnGhsFpnLBZgkqucK0HQcUqoheeP51GRUKkJaC8L8jSRJZdez%2Bts%2FLAvekIYaIU4yDZUXg4QhdccD84rgaKlvcbPeGUTlvv2ajFGel6KVB4PTIfGmzVLoxp0cNpbMWVKpP5IhoIB2CKv%2FTMucHLPP%2B2LJems1u7Jv%2F5RECUBsz1CMkcR%2FK6LjDgqmRK2GeC3oLR%2FeqV7v0HM%2FO7pwgRknSd26dPAd%2FkjSlgj43KRzLpEeg56rz8ReNEDD6wEdtwbGPZxXmdEzwvjk1Djfk%2FCUySRXyyjk45eVkLik%2Bi24L2%2F0Xm3V%2BSlvRF2fFRW3TELGf%2BXW9KVvN%2FLJLGvffY%2B6QQWuqeh31MKp75jXtqIUC4kOH%2Bi1urbK7ts%2F8mUImUYIznW5jO1s6Hg6xTOodaPcxzw0yGqvGjOLNp29zxl%2FEA3tAoZXGdwZ%2B8NXMPOa28wGOqUB%2FlbT9xyhF12yLgQetE305iFSpM5OIcR9yXC%2F5l1Hnfa7Hdy2gdg8f1bBH4Xi9YEuMhCiiY6cI1bYb2EeOVONbLP%2B%2BE0mGibCyoceAtiMf0V%2FJOkBLLJ44sucehFoPFtp2wPibA2B1DpxmQZWgLw%2BYm74ENjUrodP8PEp4Nh2nAxup%2F8lEc%2B%2Flh%2FSWRsEwFoNp0D%2Fx0P4Yx5%2FmdOJJMEjJMIP1mzy&X-Amz-Signature=91f1aac36265afb3ef8d95843747548d89b5f4587b2585115a4d922471f1b413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (2) Test2 (Fail)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit3.ts
```
- If one of the candidates for SafeWallet is MultiSigWallet

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/00298342-e0f8-4e31-90a4-243603662b2a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI6FWP7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPmP%2BuIcUfS0Sa1HpD%2Fpt9S%2BqqWjRqv%2FxMI3UjnAAgwwIgNZ2KxASxDNrcnmqwQtl5VfQGLLOXFC4bvQ9rGOgFfkwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDByUOKam00jaFoGyQCrcAwWuA7Az%2FfamgYbXS0zQWMKB8tSJAeIphNZHONPY7sIaAYVw7I7BMh6fgToxdgO9WHCDirU6JdjgTcPt4eSVig%2BjpMf96EAVCLDb8YDmS0AEw%2BVyPV%2BmWZ7ELhpIBMnf9xHYXuwkAmHqx4DCcciG9xykr9Ldpv9GxIjRiy7OAY4T14zPnmtvLepIPRtLNKXJmytJnGhsFpnLBZgkqucK0HQcUqoheeP51GRUKkJaC8L8jSRJZdez%2Bts%2FLAvekIYaIU4yDZUXg4QhdccD84rgaKlvcbPeGUTlvv2ajFGel6KVB4PTIfGmzVLoxp0cNpbMWVKpP5IhoIB2CKv%2FTMucHLPP%2B2LJems1u7Jv%2F5RECUBsz1CMkcR%2FK6LjDgqmRK2GeC3oLR%2FeqV7v0HM%2FO7pwgRknSd26dPAd%2FkjSlgj43KRzLpEeg56rz8ReNEDD6wEdtwbGPZxXmdEzwvjk1Djfk%2FCUySRXyyjk45eVkLik%2Bi24L2%2F0Xm3V%2BSlvRF2fFRW3TELGf%2BXW9KVvN%2FLJLGvffY%2B6QQWuqeh31MKp75jXtqIUC4kOH%2Bi1urbK7ts%2F8mUImUYIznW5jO1s6Hg6xTOodaPcxzw0yGqvGjOLNp29zxl%2FEA3tAoZXGdwZ%2B8NXMPOa28wGOqUB%2FlbT9xyhF12yLgQetE305iFSpM5OIcR9yXC%2F5l1Hnfa7Hdy2gdg8f1bBH4Xi9YEuMhCiiY6cI1bYb2EeOVONbLP%2B%2BE0mGibCyoceAtiMf0V%2FJOkBLLJ44sucehFoPFtp2wPibA2B1DpxmQZWgLw%2BYm74ENjUrodP8PEp4Nh2nAxup%2F8lEc%2B%2Flh%2FSWRsEwFoNp0D%2Fx0P4Yx5%2FmdOJJMEjJMIP1mzy&X-Amz-Signature=6808b597cc286aec47a6603a08367f125ecd7ca9339456998a8b245e70071188&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (3) Test3 (Success)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit4SafeWallet.ts
```
- Retest with SafeWallet configuration

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f8759a52-c159-4c6b-8e93-7d50e8b08d41/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI6FWP7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPmP%2BuIcUfS0Sa1HpD%2Fpt9S%2BqqWjRqv%2FxMI3UjnAAgwwIgNZ2KxASxDNrcnmqwQtl5VfQGLLOXFC4bvQ9rGOgFfkwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDByUOKam00jaFoGyQCrcAwWuA7Az%2FfamgYbXS0zQWMKB8tSJAeIphNZHONPY7sIaAYVw7I7BMh6fgToxdgO9WHCDirU6JdjgTcPt4eSVig%2BjpMf96EAVCLDb8YDmS0AEw%2BVyPV%2BmWZ7ELhpIBMnf9xHYXuwkAmHqx4DCcciG9xykr9Ldpv9GxIjRiy7OAY4T14zPnmtvLepIPRtLNKXJmytJnGhsFpnLBZgkqucK0HQcUqoheeP51GRUKkJaC8L8jSRJZdez%2Bts%2FLAvekIYaIU4yDZUXg4QhdccD84rgaKlvcbPeGUTlvv2ajFGel6KVB4PTIfGmzVLoxp0cNpbMWVKpP5IhoIB2CKv%2FTMucHLPP%2B2LJems1u7Jv%2F5RECUBsz1CMkcR%2FK6LjDgqmRK2GeC3oLR%2FeqV7v0HM%2FO7pwgRknSd26dPAd%2FkjSlgj43KRzLpEeg56rz8ReNEDD6wEdtwbGPZxXmdEzwvjk1Djfk%2FCUySRXyyjk45eVkLik%2Bi24L2%2F0Xm3V%2BSlvRF2fFRW3TELGf%2BXW9KVvN%2FLJLGvffY%2B6QQWuqeh31MKp75jXtqIUC4kOH%2Bi1urbK7ts%2F8mUImUYIznW5jO1s6Hg6xTOodaPcxzw0yGqvGjOLNp29zxl%2FEA3tAoZXGdwZ%2B8NXMPOa28wGOqUB%2FlbT9xyhF12yLgQetE305iFSpM5OIcR9yXC%2F5l1Hnfa7Hdy2gdg8f1bBH4Xi9YEuMhCiiY6cI1bYb2EeOVONbLP%2B%2BE0mGibCyoceAtiMf0V%2FJOkBLLJ44sucehFoPFtp2wPibA2B1DpxmQZWgLw%2BYm74ENjUrodP8PEp4Nh2nAxup%2F8lEc%2B%2Flh%2FSWRsEwFoNp0D%2Fx0P4Yx5%2FmdOJJMEjJMIP1mzy&X-Amz-Signature=4116e345f20fcc1b479967a62c8ff2f041dc644b6b4e0552e3d687663701ee6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## (4) Test4 (Success)

- branch : Self-development
```bash
node --loader ts-node/esm src/protocolKit2-singleOwnerPass.ts
```
- Version composed by Singer

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/317ce4b3-dd2f-422f-97d3-65fba2ff7b26/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI6FWP7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPmP%2BuIcUfS0Sa1HpD%2Fpt9S%2BqqWjRqv%2FxMI3UjnAAgwwIgNZ2KxASxDNrcnmqwQtl5VfQGLLOXFC4bvQ9rGOgFfkwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDByUOKam00jaFoGyQCrcAwWuA7Az%2FfamgYbXS0zQWMKB8tSJAeIphNZHONPY7sIaAYVw7I7BMh6fgToxdgO9WHCDirU6JdjgTcPt4eSVig%2BjpMf96EAVCLDb8YDmS0AEw%2BVyPV%2BmWZ7ELhpIBMnf9xHYXuwkAmHqx4DCcciG9xykr9Ldpv9GxIjRiy7OAY4T14zPnmtvLepIPRtLNKXJmytJnGhsFpnLBZgkqucK0HQcUqoheeP51GRUKkJaC8L8jSRJZdez%2Bts%2FLAvekIYaIU4yDZUXg4QhdccD84rgaKlvcbPeGUTlvv2ajFGel6KVB4PTIfGmzVLoxp0cNpbMWVKpP5IhoIB2CKv%2FTMucHLPP%2B2LJems1u7Jv%2F5RECUBsz1CMkcR%2FK6LjDgqmRK2GeC3oLR%2FeqV7v0HM%2FO7pwgRknSd26dPAd%2FkjSlgj43KRzLpEeg56rz8ReNEDD6wEdtwbGPZxXmdEzwvjk1Djfk%2FCUySRXyyjk45eVkLik%2Bi24L2%2F0Xm3V%2BSlvRF2fFRW3TELGf%2BXW9KVvN%2FLJLGvffY%2B6QQWuqeh31MKp75jXtqIUC4kOH%2Bi1urbK7ts%2F8mUImUYIznW5jO1s6Hg6xTOodaPcxzw0yGqvGjOLNp29zxl%2FEA3tAoZXGdwZ%2B8NXMPOa28wGOqUB%2FlbT9xyhF12yLgQetE305iFSpM5OIcR9yXC%2F5l1Hnfa7Hdy2gdg8f1bBH4Xi9YEuMhCiiY6cI1bYb2EeOVONbLP%2B%2BE0mGibCyoceAtiMf0V%2FJOkBLLJ44sucehFoPFtp2wPibA2B1DpxmQZWgLw%2BYm74ENjUrodP8PEp4Nh2nAxup%2F8lEc%2B%2Flh%2FSWRsEwFoNp0D%2Fx0P4Yx5%2FmdOJJMEjJMIP1mzy&X-Amz-Signature=859b809252b9feba9dc0484301f9b2261e0e1131c66a42d643476654184c5387&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Remain issue : [https://github.com/safe-global/safe-core-sdk/issues/1264](https://github.com/safe-global/safe-core-sdk/issues/1264)