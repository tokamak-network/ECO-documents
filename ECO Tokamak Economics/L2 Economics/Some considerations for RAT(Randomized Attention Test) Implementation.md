## (1) op-validator vs op-challenger

- **op-validator**: Verifies **L1 contract deployment** (at deployment/upgrade time)
- **op-challenger**: Verifies **L2 block execution results** (real-time monitoring)
- Reference Link : [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/optimism-challenger-systems.md#%EF%B8%8F-%EA%B8%B0%EC%A1%B4-%EC%98%B5%ED%8B%B0%EB%AF%B8%EC%A6%98-%EC%B1%8C%EB%A6%B0%EC%A0%80-%EC%8B%9C%EC%8A%A4%ED%85%9C)  

## **(2) Why does the L2 Proposer create a DisputeGame every time it uploads a batch?**

- The Proposer's Role
  - L2 State Monitoring: Continuously monitors new blocks on the L2 chain.
  - Output Root Generation: Generates an output root by calculating the state root of the L2 block.
  - Dispute Game Generation: Submits a Dispute Game creation transaction for the new output root.
  - Periodic Submission: Automatically submits at set intervals (ProposalInterval).
- Reference Link1 : [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/optimism-security-model.md#2-%EC%99%9C-%EB%91%90-%EA%B0%80%EC%A7%80-%EC%A0%9C%EC%B6%9C%EC%9D%B4-%EB%AA%A8%EB%91%90-%ED%95%84%EC%9A%94%ED%95%9C%EA%B0%80)  
- Reference Link2 : [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/op-challenger-analysis.md#q5-l1%EC%97%90-dispute-game-%EC%83%9D%EC%84%B1-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98%EC%9D%84-%EC%A0%9C%EC%B6%9C%ED%95%98%EB%8A%94-%EC%A3%BC%EC%B2%B4%EB%8A%94-%EB%88%84%EA%B5%AC%EC%9D%B8%EA%B0%80%EC%9A%94)

## (3) Current Optimism GameType Values and the GameType Required by the RAT

 

- Optimism currently uses **GameType 1**: PERMISSIONED_CANNON (PermissionedDisputeGame).
  - **Current Optimism System Features:**
    - **Restricted Participation**: Only designated PROPOSER and CHALLENGER addresses can participate in the game.
    - **Single Challenger**: Only one designated challenger can participate in the game.
    - **Permission-Based**: Access Control with the OnlyAuthorized modifier.
- Tokamak-thanos' **GameType 0**: In the deployment settings, set `respectedGameType` to `0` → This is a general type that allows anyone to create a dispute game without permission.

**For the RAT system to function properly, it must be switched to GameType 0 (Permissionless).**

**→ 누구나 챌린지를 할수있으면서, 의무를 가지는 챌린저 집합이 존재를 해야 한다. 그 주소의 집합만 챌린지를 하게 하는건 아니다.  누군가 들은 최소한의 자원을 통해 관리가 되어야 한다. 컨트랙트에 관리 할수있께 하고, 그 주소에 대해서만 랜덤하게 테스트를 수행하게 하는 메커니즘이 필요하다. **

**L1 ⇒ 게임팩토리 컨트랙을 수정해서 구현하고자 한다. 챌린저 관리 하는 식으로 : 챌린저 스테이킹 , **

- **이벤트 → 어텐션 테스트 트리거 → 응답에 따라 디파짓을 차감하는 식으로 **
1. **비용확인 , 등록, 해지도 필요.**
1. **주소리스트가 등록이 되었다고 가정하고, 작업해도 된다.   **
- Reference Link1 [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/tasks/phase1/p2p-challenger-basic/dispute-game.md#-%ED%98%84%EC%9E%AC-optimism-dispute-game-%EC%84%A4%EC%A0%95) 
- Reference Link2 [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/tokamka-thanos-qna.md#2-%EB%B0%B0%ED%8F%AC%EC%97%90%EC%84%9C-%EC%84%A4%EC%A0%95%ED%95%98%EB%8A%94-respected-game-type)

## (4) Challenger Reward Mechanism  

For P2P challengers  (my proposed), the challenger's results are regularly reported to **the L2 reward management contract**.  

Designate the reward management contract as the recipient (l1FeeVaultRecipient) of the **L1FeeVault** contract on the L2 chain being monitored.

If the amount held by the L1FeeVault contract exceeds the actual batcher cost, the excess amount is sent to the recipient (reward management contract).

Currently, there is no mechanism for proposers to receive separate compensation for the dispute game creation fee. Let's provide a mechanism for them to receive compensation through the reward management contract above. (Proposers receive a separate reward for winning a game, including the game deposit.)

- Reference link for Tokamak-thanos's reward system : [link](https://github.com/Zena-park/optimism/blob/feature/p2p-challenger-attention-test/sequencer-docs/tokamka-thanos-qna.md#l2-%EC%9A%B4%EC%98%81%EB%B9%84-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98)