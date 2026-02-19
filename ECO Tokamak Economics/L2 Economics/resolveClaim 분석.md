[https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/L1/RAT.sol](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/L1/RAT.sol)

**resolveClaim(uint256 _claimIndex, uint256 _numToResolve)**

- Prerequisites
  - This function must be resolved sequentially, starting with the lowest claim index. It will [not execute until all sub-indices are resolved](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L815-L816).
- Action. State Change Details
  - If no claim is refuted, the deposit provided by [the claimant is recovered](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L791).
  - If a claim is refuted,
    - (1) [Find the leftmost claim](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L826) among the sub-claims that refuted the claim.
    - (2) [Set counteredBy = claimant of the leftmost claim](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L827) among the sub-claims.
    - (3) [Pay the deposit to counteredBy](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L858-L859).
  - resolvedSubgames[_claimIndex] = true; => [Set to resolved](https://github.com/tokamak-network/optimism/blob/f6a9eb93347817bbe8145f1008f7b2f8ee8f6203/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol#L837).

**Conclusion**,

If your claim isn’t refuted, your deposit will be recovered.

If your claim is refuted, the leftmost claim (the claim refuted first) will receive the deposit.

## 예시 구조:

claimIndex 0: “상태 X가 맞다” (프로포저)

└── claimIndex 1: “상태 X가 틀렸다” (도전자1)

├── claimIndex 2: “1이 틀렸다” (도전자2)

│   └── claimIndex 3: “2가 틀렸다” (도전자3)

└── claimIndex 4: “1이 틀렸다” (도전자4)

└─── claimIndex 5: “4가 틀렸다” (도전자5)

### 해결 과정 (bottom-up):

1. claimIndex 5 (leaf): counteredBy = null → 도전자5가 bond 유지

2. claimIndex 3 (leaf): counteredBy = null → 도전자3이 bond 유지

3. claimIndex 4: 자식 5 (성공) → countered = 도전자5 → 도전자5가 도전자4의 bond 가져감

4. claimIndex 2: 자식 3 (성공) → countered = 도전자3 → 도전자3이 도전자2의 bond 가져감

5. claimIndex 1: 자식들 2(패배), 4(패배) → 성공한 자식 없음 → countered = address(0) → 도전자1이 자신의 bond 유지

6. claimIndex 0: 자식 1 (성공) → countered = 도전자1 → 도전자1이 프로포저의 bond 가져감

최종 Bond 분배:

- 프로포저 bond → 도전자1

- 도전자1 bond → 도전자1 유지

- 도전자2 bond → 도전자3

- 도전자3 bond → 도전자3 유지

- 도전자4 bond → 도전자5

- 도전자5 bond → 도전자5 유지

### resolveClaim 호출 순서와 Bond 분배:

```shell
// 1단계: Leaf 노드들 (bottom-up)
resolveClaim(5, 1)  // claimIndex 5 해결
→ Bond 받는 사람: 도전자5 (자신의 bond 유지 - 반박당하지 않음)

resolveClaim(3, 1)  // claimIndex 3 해결
→ Bond 받는 사람: 도전자3 (자신의 bond 유지 - 반박당하지 않음)

// 2단계: 다음 레벨
resolveClaim(4, 1)  // claimIndex 4 해결
→ Bond 받는 사람: 도전자5 (claimIndex 5가 4를 성공적으로 반박)

resolveClaim(2, 1)  // claimIndex 2 해결
→ Bond 받는 사람: 도전자3 (claimIndex 3이 2를 성공적으로 반박)

// 3단계: 상위 레벨
resolveClaim(1, 1)  // claimIndex 1 해결
→ Bond 받는 사람: 도전자1 (자식들 2,4 모두 패배 → 반박 실패)

// 4단계: Root
resolveClaim(0, 1)  // claimIndex 0 해결
→ Bond 받는 사람: 도전자1 (claimIndex 1이 0을 성공적으로 반박)
```

최종 Bond 분배 결과:

- 도전자5: 자신의 bond + 도전자4의 bond
- 도전자3: 자신의 bond + 도전자2의 bond
- 도전자1: 자신의 bond + 프로포저의 bond
- 도전자2: bond 잃음 (도전자3에게)
- 도전자4: bond 잃음 (도전자5에게)
- 프로포저: bond 잃음 (도전자1에게)

승자: 도전자1, 도전자3, 도전자5가 각각 2개씩의 bond를 획득!