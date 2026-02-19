Related Slack Links : [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1754358607034289?thread_ts=1753857060.873189&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1754358607034289?thread_ts=1753857060.873189&cid=C06UKCF86TE)

# 1. Reasons to upgrade

When registering an operator who deployed L2 in the Rollup hub as a DAO candidate, two of the owners of the Safe wallet with the authority to upgrade the L1 contract are used as foundation addresses (TokamakDAO, Foundation) as a device to prevent unauthorized upgrades of the bridge logic due to fraudulent actions by malicious operators. This is necessary for Tokamak DAO to verify the Sign.

Rollup hub에서 L2를 배포한 운영자를 DAO candidate로 등록할 때 악의의 운영자의 부정 행위로 브릿지의 로직을 무단 업그레이드하지 못하도록 하는 장치로 L1 컨트랙트의 업그레이드 권한을 가진 Safe wallet의 소유자 중 2명을 재단 주소 (TokamakDAO, Foundation)로 사용하는데 여기서 Tokamak DAO가 Sign에 대한 검증을 하기 위해서 필요합니다. 

# 2. Current system structure

- DAOCommittee_V2: Main DAO contract
- MultiSigWallet: A multi-sig wallet designated as the DAO's owner
- MultiSigWallet Owner Structure: A structure in which multiple owners submit and confirm transactions.
- DAOCommittee_V2: 메인 DAO 컨트랙트 (아직 아젠다 통과가 안되서 지금은 V1)
- MultiSigWallet: DAO의 owner로 설정된 멀티시그 지갑
- MultiSigWallet Owner 구조: 여러 owner들이 트랜잭션을 제출하고 확인하는 구조

# 3. EIP-1271 Implementation Plan

### MultiSigWallet-based Signature Verification 

This method connects messages individually signed by MultiSigWallet owners and verifies them with the DAO Committee.

EIP-1271 is currently required because the DAOContract cannot sign. However, MultiSigWallet, the owner of the DAOContract, cannot sign.
However, MultiSigWallet owners can sign.
Therefore, we plan to develop a method to use this to verify whether the owner of MultiSigWallet signed the contract.

### MultiSigWallet 기반 서명 검증 

MultiSigWallet의 owner들이 개별적으로 서명한 메시지를 연결하여 DAO Contract가 검증하는 방식입니다.

현재 EIP-1271이 필요한 것은 DAOContract가 서명을 하지 못하여서 필요한데 DAOContract의 Owner인 MultiSigWallet Contract도 서명을 하진 못합니다.
하지만 MultiSigWallet의 Owner들은 서명을 할 수 있습니다.
그래서 이를 이용해 MultiSigWallet의 Owner가 서명을 하였는지 확인하는 방식으로 개발할려고 합니다.

# 4. Development Phase-by-Phase Plan

- Phase 1: Basic architecture design and functional implementation (1 weeks) (25.08.07~25.08.13)
- Phase 2: Test script development and documentation (1 week) (25.08.14~25.08.20)
- Phase 3: Internal audit and feedback implementation & testing on Sepolia(1-2 weeks) (25.08.21~25.09.03)
- Phase 4: deployment
- Phase 1: 기본 구조 설계 및 기능 구현 (1주) (25.08.07~25.08.13)
- Phase 2: 테스트 스크립트 개발 및 문서화 (1주) (25.08.14~25.08.20)
- Phase 3: 내부 오딧 및 피드백 적용 & Sepolia 테스트 (1주~2주) (25.08.21~25.09.03)
- Phase 4 : 배포 

Feedback

- 사용하는 LLM 과정을 기록 (모든 사람들이 추가 개발할 수 있게) (zeroshot(한번에 할 수 있었으면 좋겠다[LLM이랑 대화하는 것을 줄이게][LLM으로 개발했을때 최대한 같은 결과물이 나올 수 있도록]))

[[EIP-1271 Development Details]]

# 5. Plan change

[[Summary of Plan changes]]

# 6. Background

[[Development Background]]