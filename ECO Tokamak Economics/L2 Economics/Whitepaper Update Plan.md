## 목차

- [Disccusion](/2a0d96a400a38058be92f9443850a228#2a0d96a400a38056ab49ed0707287231)
- [Old structure](/2a0d96a400a38058be92f9443850a228#2a0d96a400a380f3b685dd6255c40017)
- [New structure](/2a0d96a400a38058be92f9443850a228#2a0d96a400a380d896d8f5ca54b5db0c)

## (Discussion) Existing Structure Review & Comment

### Background summary → Summary or Executive Summary

### TL;DR → Summary 가 있다면 넣지 않는게 whitepaper 레벨에서는 자연스러움

### 1. Terminology

- 주요의견: 새 버전에는 이 섹션이 없어지는게 자연스러움. 많은 용어들은 현재 롤업과 코인이 메이저 솔루션으로 부상하며 이해하는데 크게 어려움이 없고 본문에서 명확하게 맥락을 정의하여 용어에 대한 오해를 충분히 피할 수 있음
  - Operator-Sequencer-Proposer 정의
  - inflation 대소문자, 정의가 완전히 다름
  - DTD → Dispute window
  - Deposit → Bridged Deposit to L2 등으로 구체화
  - Withdraw → 정의 안하고 맥락에 따라 판단되는게 더 맞음
  - Bridging ? L2 → L1 / L1 → L2
  - Fraud proof / Validity proof → 제거해도 문제 없음
- **다만, Seigniorage 는 생소하기 소개해야 혹은 각주로 **

### 2. Seigniorage

- 새로운 Tokenomics 명세로 전반적으로 재작성
- 새로운 Tokenomics 명세는 TON staking V3 로 소개
- TON staking V1, V2 는 이전버전의 링크 혹은 Appendix 로 분리 (흐름이 부자연스러움)
- 2.3 Sustainable growth of L2 는 디자인의 의도에 가깝기 TON Staking 명세 이후에 나오는게 부자연스럽고 현재 매우 추상적인 레벨. 때문에 TON staking V3 명세 이전에 새로운 토크노믹스 디자인 의도에 대한 먼저 설명을 하면서 그 안에서 기존 2.3 의 의도를 반영. 

### 3. Verification economics

- 기존: 챌린지 시스템 소개 → FW → Verifier’s dilemma
- 새로운: Optimistic rollup 과 검증자 문제 (verifier’s dilemma, 탈중앙화, 검증자 인센티브 ) → 시스템 기본구조: 보안 목표에 부합하는 챌린지 시스템과 공유 벨리데이터 → 검증자 문제 완화 메커니즘 (RAT, FW 등)
- **추상적으로 validity proof 에서의 경제 가능성? → 이 부분이 들어가지 않으면 validity proof 로 전환시 TON 의 유틸리티가 0으로 수렴**
  - 지금 dispute window 가 상당한 기간인 경우를 가정하고 있다. 이게 상당히 적은 기간으로 줄어들 경우에, → 고민 필요 (중요)

### 4. Utilities of TON

- L2 deposit (security) → L2 fee → DAO

### ~~5. Validity Proof → Privacy support~~

- Ooo project 관련 내용 (zk state channel 을 통한 privacy transaction)

### 6. Examples → 제거 → 블로그 글 같은걸로 별도 보충

## Old Structure

1. Terminology
1. Seigniorage
  1. Sieg. generation
  1. Seig. distribution
    1. TON staking V1
    1. TON staking V2
  1. Sustainable growth of L2
    1. Quantitative/Qualitative growth of L2
    1. Alleviation of L2 fee token dilemma
1. Verification economics (하위단 대소문자 주의)
  1. Challenge
  1. Fast withdrawal
  1. Verifier’s dilemma
1. Utilities of TON
  1. Sustainable growth of L2
  1. Enhanced L2 security
1. Validity Proof
1. Examples
1. References
1. Appendix

## New Structure

1. Siegniorage
  1. Sustainable growth of L2
  1. Seigniorage generation
  1. Seigniorage distribution: TON staking V3
1. Verification economics
  1. Optimistic protocol and verification concerns
  1. Economics structure
  1. Risk mitigation mechanisms
    1. RAT (Randomized Attention Test)
    1. FW (Fast Withdrawal)
1. Utilities of TON → 첫번째 섹션이 자연스러워보임
  1. L2 Security
  1. L2 Gas
  1. TON DAO
1. ~~Privacy Support~~
  1. ZK state channel 에 관한 내용
1. Reference
1. Appendix
  1. Terminology (if needed)
  1. TON staking v1, v2

## “Verification economics → Demand → Supply” 

## Revised Structure

Summary

1. Verification economics (Landscape) → Suhyeon
  1. Optimistic protocol and verification concerns
  1. TON rollup ecosystem
  1. Risk mitigation mechanisms
    1. RAT (Randomized Attention Test)
    1. FW (Fast Withdrawal)
1. Utilities of TON (Demand) → Bernard
  1. L2 Security
  1. L2 Gas
  1. TON DAO
1. Siegniorage (Supply) → Bernard
  1. Sustainable growth of L2
  1. Seigniorage generation
  1. Seigniorage distribution: TON staking V3
1. Reference
1. Appendix