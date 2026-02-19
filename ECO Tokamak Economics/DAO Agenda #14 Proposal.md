Tokamak Network DAO agenda #14 proposal

# Deploy TON staking V2 contract + upgrade DAO 

DAO agenda proposal link: [https://dao.tokamak.network/#/agenda/14](https://dao.tokamak.network/#/agenda/14)

### Simple Summary

The Tokamak Network Foundation proposes a staking V2 upgrade to strengthen the TON economy. This proposal allows for the creation of DAO candidates with L2 that can receive seigniorage based on the TON locked in the bridge(portal). To implement this proposal, the DAO contract must be upgraded to provide additional features to support staking V2.

### Motivation

[Tokamak Network L2 Cryptoeconomic](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2) outlines how L2 operator can receive sequencer seigniorage based on TON bridged to L2. This proposal puts the concept into action, enticing more L2s to join Tokamak Network's ecosystem as DAO candidates and earn sequencer seigniorage. Tokamak Network encourages developers and operators to maintain and improve Layer2s by distributing seigniorage to Layer 2 operators, which can lead to a more robust ecosystem and try to make a symbiotic relationship between the Layer1 and Layer2, promoting overall stability, security, and efficiency of the TON ecosystem.

### On-Chain Effects

1. DAO contract upgrade
- DAOCommitteeProxy upgrade ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/proxy/DAOCommitteeProxy2.sol)): This upgrade allows new logic to be added to DAOCommittee, providing greater control and flexibility over its functions.
- Added staking V2 logic and migrated existing logic to DAOCommitteeProxy2 ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommittee_V1.sol)): Added createCandidateAddOn function, which creates a DAO candidate with L2, and separated non onlyOwner functions from existing DAOCommittee.
- Set DAO parameter to DAOCommittee ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L183-L191)) : Changed so that a candidate cannot call changeMember multiple times in a short period of time.
1. Staking V2 contract setting
- SeigManagerProxy upgrade ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol)) : The logic of SeigManagerV1_2, which was previously used, has been upgraded.
- Added and set staking V2 logic to SeigManagerProxy ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_3.sol)): update seigniorage function based on staking V2
- Added and set staking V2 logic to DepositMangerProxy ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/DepositManagerV1_1.sol)): update based on staking V2
- Set staking V2 parameters to DAOCommittee ([link 1](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L195-L204), [link 2](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L208-L216)): enable staking V2 related functions.
- Set staking V2 parameter to SeigManager ([link 1](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L295-L300), [link 2](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L316-L320))
- Set staking V2 parameter to DepositManager ([link](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/DepositManagerV1_1.sol#L83-L87))

### References

- Discussion: [link](https://github.com/tokamak-network/ton-staking-v2/issues/310)
- Description of DAO upgrade: [description](https://github.com/tokamak-network/ton-staking-v2/blob/mainnet-agenda-test/doc/en/dao-upgraded-en.md)
- Description of staking V2: [description](https://github.com/tokamak-network/ton-staking-v2/blob/test-mainnet/docs/en/ton-staking-v2.md)
- Implementation
  - DAOCommittee_V1:
    - [createCandidateAddOn(string calldata _memo, address _operatorManagerAddress)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommittee_V1.sol#L235-L265)
    - [currentAgendaStatus(uint256 _agendaID)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommittee_V1.sol#L513-L558)
  - DAOCommitteeOwner:
    - [setCandidateAddOnFactory(address _candidateAddOnFactory)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L193-L204)
    - [setLayer2Manager(address _layer2Manager)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L206-L216)
    - [setCooldownTime(uint256 _cooltime)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L181-L191)
    - [daoExecuteTransaction(address _to,bytes memory _data)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/DAOCommitteeOwner.sol#L396-L411)
  - SeigManager:
    - [setLayer2Manager(address layer2Manager_)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L291-L300)
    - [setLayer2StartBlock(uint256 startBlock_)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L302-L310)
    - [setL1BridgeRegistry(address l1BridgeRegistry_)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L312-L320)
    - [updateSeigniorage()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_3.sol#L180-L186)
    - [updateSeigniorageLayer(address layer2)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_3.sol#L192-L198)
    - [estimatedDistribute(uint256 blockNumber, address layer2)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_3.sol#L238-L270)
    - [allowIssuanceLayer2Seigs(address layer2)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_2.sol#L595-L599)
    - [pause()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/SeigManagerV1_3.sol#L216-L222)
  - DepositManager:
    - [setMinDepositGasLimit(uint32 gasLimit_)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/DepositManagerV1_1.sol#L78-L81)
    - [setAddresses(address _l1BridgeRegistry, address _layer2Manager)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/DepositManagerV1_1.sol#L83-L87)
    - [withdrawAndDepositL2(address layer2, uint256 amount)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/stake/managers/DepositManagerV1_1.sol#L88-L144)
  - L1BridgeRegistry:
    - [setAddresses(address _layer2Manager, address _seigManager, address _ton)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L115-L134)
    - [setSeigniorageCommittee(address _seigniorageCommittee)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L136-L149)
    - [rejectCandidateAddOn(address rollupConfig)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L153-L168)
    - [restoreCandidateAddOn(address rollupConfig, bool rejectedL2Deposit)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L170-L187)
    - [registerRollupConfigByManager(address rollupConfig, uint8 _type, address _l2TON, string calldata _name)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L192-L205)
    - [registerRollupConfigByManager(address rollupConfig, uint8 _type, address _l2TON)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L207-L214)
    - [registerRollupConfig(address rollupConfig, uint8 _type, address _l2TON, string calldata _name)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L218-L231)
    - [registerRollupConfig(address rollupConfig, uint8 _type, address _l2TON)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/L1BridgeRegistryV1_1.sol#L233-L240)
  - Layer2Manager:
    - [setAddresses( address _l1BridgeRegistry, address _operatorManagerFactory, address _ton, address _wton, address _dao, address _depositManager, address _seigManager, address _swapProxy)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/Layer2ManagerV1_1.sol#L128-L150)
    - [setOperatorManagerFactory(address _operatorManagerFactory)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/Layer2ManagerV1_1.sol#L152-L158)
    - [setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/Layer2ManagerV1_1.sol#L160-L170)
    - [registerCandidateAddOn(address rollupConfig, uint256 amount, bool flagTon, string calldata memo)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/Layer2ManagerV1_1.sol#L232-L253)
    - [onApprove(address owner, address spender, uint256 amount, bytes calldata data)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/Layer2ManagerV1_1.sol#L256-L289)
  - OperatorManager:
    - [setAddresses(address _layer2Manager, address _depositManager, address _ton, address _wton)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L99-L119)
    - [transferManager(address newManager)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L126-L136)
    - [claimETH()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L138-L143)
    - [claimERC20(address token, uint256 amount)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L145-L152)
    - [requestWithdrawal(uint256 amount)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L154-L164)
    - [processRequest()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L166-L172)
    - [processRequests(uint256 n)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/layer2/OperatorManagerV1_1.sol#L174-L180)
  - CandidateAddOn:
    - [initialize(address _operateContract, string memory _memo, address _committee, address _seigManager, address _ton, address _wton)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L30-L59)
    - [setMemo(string calldata _memo)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L61-L66)
    - [changeMember(uint256 _memberIndex)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L71-L80)
    - [retireMember()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L82-L86)
    - [castVote( uint256 _agendaID, uint256 _vote, string calldata _comment)](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L88-L101)
    - [claimActivityReward()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L103-L111)
    - [updateSeigniorage()](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-merge/contracts/dao/CandidateAddOnV1_1.sol#L116-L122)
- Sepolia Tests: [create](https://sepolia.etherscan.io/tx/0xff454e78031bd41c15a4afe711a5657762fab742e2ef2d2863bbaa2f7f30aba9), [execute](https://sepolia.etherscan.io/tx/0x8b59c53b81ae38d7df277c495ef81b9e516ec86baf772c8fdb146b288513ec4c)

### Copyright

Copyright and related rights waived via [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).