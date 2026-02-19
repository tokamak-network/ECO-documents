1/

```
ETH 예치자
  ↓ (32 ETH Deposit)
Activation Queue 대기
  ↓
Active Validator
```

```javascript
Active Validator
  ↓ (Voluntary Exit)
Exit Queue 대기
  ↓
Exited Validator
  ↓
Withdrawal Queue
  ↓
32 ETH + 모든 보상 출금
```

- **Exit Queue**
→ 합의 참여자 급감으로 인한 **네트워크 보안 저하 방지**
- **Withdrawal Queue**
→ 대량 출금으로 인한 **Execution Layer 혼잡 방지**

2/

slot: 12초

epoch: 32 slots ≈ 6.4분

attestation 보상 — 에폭 단위

block proposer 보상 — 슬롯 단위

penalty — 에폭 단위

3/

```
32 ETH (Initial Stake)
+ Attestation Rewards
+ Block Proposal Rewards
- Penalties (있다면)
= Validator Balance
```

- Validator Balance는 **Consensus Layer 상태**
- 출금은 **Withdrawal 메커니즘을 통해 Execution Layer로 이동**

4/

Solo staking = 내 32 ETH + 내 키 + 내 노드 + 내 책임

- Validator 키를 **직접 소유**
- Consensus 참여를 **직접 수행**
- 보상도, 패널티도 **전부 본인 몫**