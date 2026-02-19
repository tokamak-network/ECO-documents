Reference [link](/2f886f9a09bf40ce9dafa2c130361a92)

## Pre

- Graph QL 
  - event collector
  - call 함수는 별도로

## Graph schema

schema
  - sequencer

```graphql
type Sequencer @entity {
  # sequencer address
  id: ID!
  # sequencer name
  name: String!
	# owner of sequencer
	owner: Bytes!
	# address manager address
	addressManager: Bytes!
	# l1 messenger address
	l1Messenger: Bytes!
	# l1bridge address
	l1Bridge: Bytes!
	# ton adress deployed in this l2
	l2ton: Bytes!
	# commision rate
	commission: BigDecimal!
	# sequencer index
	sequencerIndex: BigDecimal!
	# deposited amount of this operator
	depositAmount: BigDeciamal!
	# deposited amount of this operator in usd
	depositAmountUSD: BigDeciamal!
  # user info who are staking to this candidate
	user: User!
  # derived values
  staked: [Stake]! @derivedFrom(field: "transaction")
  unstaked: [Unstake]! @derivedFrom(field: "transaction")
  restaked: [Restake]! @derivedFrom(field: "transaction")
	withdrawal: [Withdraw]! @derivedFrom(field: "transaction")
	deposited: [Deposit]! @derivedFrom(field: "transaction")
}
```

  - candidate

```graphql
type Candidate @entity {
  # candidate address
  id: ID!
  # sequencer name
  name: String!
	# owner of sequencer
	owner: Bytes!
	# mapping for sequencer
	sequencerIndex: BigDecimal!
	# deposited amount of this operator
	depositAmount: BigInt!
	# deposited amount of this operator in usd
	depositAmountUSD: BigDeciamal!
	# sequencer or candidate
	type: String!
  # user info who are staking to this candidate
	user: User!
  # derived values
  staked: [Stake]! @derivedFrom(field: "transaction")
  unstaked: [Unstake]! @derivedFrom(field: "transaction")
  restaked: [Restake]! @derivedFrom(field: "transaction")
	withdrawal: [Withdraw]! @derivedFrom(field: "transaction")
	deposited: [Deposit]! @derivedFrom(field: "transaction")
}
```

  - User

```graphql
type User @entity {
	# user address
  id: ID!
	# candidate or sequencer
	sequencer: Sequencer!
	# deposited amount of this user
	amount: BigInt!
	# deposited amount of this user
	depositAmount: BigInt!
	# deposited amount of this user
	depositAmountUSD: BigInt!
	# derived values
  staked: [Stake]! @derivedFrom(field: "transaction")
  unstaked: [Unstake]! @derivedFrom(field: "transaction")
	# list of provided fast withdraw
	fastWithdrawal: [FastWithdraw]! @derivedFrom(field: "transaction")
}
```

  - Agenda(after DAO contract implemented)

```graphql
type Agenda @entity {

}
```

  - Transactions

```graphql
type Transaction @entity {
  # txn hash
  id: ID!
  # block txn was included in
  blockNumber: BigInt!
  # timestamp txn was confirmed
  timestamp: BigInt!
  # gas used during txn execution
  gasUsed: BigInt!
  gasPrice: BigInt!
  # derived values
  staked: [Stake]! @derivedFrom(field: "transaction")
  unstaked: [Unstake]! @derivedFrom(field: "transaction")
  restaked: [Restake]! @derivedFrom(field: "transaction")
	withdrawal: [Withdraw]! @derivedFrom(field: "transaction")
	deposited: [Deposit]! @derivedFrom(field: "transaction")
	fastWithdrawal: [FastWithdraw]! @derivedFrom(field: "transaction")
}
```

  - Staked

```graphql
# transaction hash + "#" + index in staked Transaction array
  id: ID!
  # which txn the stake was included in
  transaction: Transaction!
  # time of txn
  timestamp: BigInt!
	# owner of sequencer or candidate where staking occured to
  sender: Bytes
  # txn origin
  origin: Bytes! # the EOA that initiated the txn
  # amount of staked
  amount: BigInt!
	# position within the transactions
  logIndex: BigInt
```

  - Unstake

```graphql
# transaction hash + "#" + index in staked Transaction array
  id: ID!
  # which txn the stake was included in
  transaction: Transaction!
  # time of txn
  timestamp: BigInt!
	# owner of sequencer or candidate where unstake occured to
  owner: Bytes!
  # txn origin
  origin: Bytes! # the EOA that initiated the txn
  # amount of staked
  amount: BigInt!
	# position within the transactions
  logIndex: BigInt
```

  - Restake

```graphql
# transaction hash + "#" + index in staked Transaction array
  id: ID!
  # which txn the stake was included in
  transaction: Transaction!
  # time of txn
  timestamp: BigInt!
	# owner of sequencer or candidate where restake occured to
  owner: Bytes!
  # txn origin
  origin: Bytes! # the EOA that initiated the txn
  # amount of staked
  amount: BigInt!
	# position within the transactions
  logIndex: BigInt
```

  - Withdraw

```graphql
# transaction hash + "#" + index in staked Transaction array
  id: ID!
  # which txn the stake was included in
  transaction: Transaction!
  # time of txn
  timestamp: BigInt!
	# owner of sequencer or candidate where withdraw occured to
  sender: Bytes
  # txn origin
  origin: Bytes! # the EOA that initiated the txn
  # amount of staked
  amount: BigInt!
	# position within the transactions
  logIndex: BigInt
```

  - FastWithdraw

```graphql
# transaction hash + "#" + index in staked Transaction array
  id: ID!
  # which txn the stake was included in
  transaction: Transaction!
  # time of txn
  timestamp: BigInt!
	# owner of sequencer or candidate where FW occured to
  owner: Bytes!
  # the address that sta
  sender: Bytes
  # txn origin
  origin: Bytes! # the EOA that initiated the txn
  # amount of FW
  amount: BigInt!
	# fee of FW
  fee: BigInt!
	# position within the transactions
  logIndex: BigInt
```

  - day data
    - 총 스테이킹량
  - hour data

## Question

- L1? L2 - fw request 관련된 컨트랙은 l2에 배포될 수 있음(Not decided yet)?
- different between sequencer & candidate
  - sequencer ↔ candidate 는 불가
  - sequencer - 운영하는 l2 필요 
  - candidate는 없음, 어떤 시퀀서에 소속됐는지, 
    - 수수료 있음
- different between deposit & staking
  - staking - simple staking: candidate or sequencer 
  - deposit - sequencer가 디파짓할때, ⇒ l2 manager  담보금,  / candidate의 deposit == staking
  - 레이어간 이동은 Transfer

## Feedback

## SeigManagerV2

### Event

```javascript
event UpdatedSeigniorage(
                uint256 lastSeigBlock_,
                uint256 increaseSeig_,
                uint256 totalSupplyOfTon_,
                uint256[4] amount_,
                uint256 prevIndex_,
                uint256 index_
                );

** amount[4] -> [amountOfstaker, amountOfsequencer, amountOfDao, amountOfStosHolders]

event Claimed(address caller, address to, uint256 amount);
```

## Subgraph

handleUpdatedSeigniorage

handleClaimed