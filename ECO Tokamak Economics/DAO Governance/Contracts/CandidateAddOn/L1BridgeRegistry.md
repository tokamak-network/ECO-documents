### **L1BridgeRegistry**

[*setup history*](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4)*:*

1. *upgradeTo —**` L1BridgeRegistryV1_1`*
1. *setSeigniorageCommittee — **`DAOCommitteeProxy`*
1. *AddManager — **`DAOCommitteeProxy`*
1. *SetAddresses*
  - *_layer2Manager — **`Layer2ManagerProxy`*
  - *_seigManager — **`SeigManagerProxy`*
  - *_ton — **`TON`*
1. *transferAdmin — **`DAOCommitteeProxy`*

```solidity
enum TYPE_ROLLUPCONFIG {
        NONE,
        LEGARCY,
        OPTIMISM_BEDROCK
    }
```

```solidity
struct ROLLUP_INFO {
    uint8 rollupType;
    address l2TON;
    bool rejectedSeigs;
    bool rejectedL2Deposit;
    string name;
}
```

```solidity
function _registerRollupConfig(
    address rollupConfig,
    uint8 _type,
    address _l2TON,
    string memory _name
) internal {
    if (_l2TON == address(0)) revert RegisterError(4);
    if (_type == 0 || _type > uint8(type(TYPE_ROLLUPCONFIG).max)) revert RegisterError(1);

    ROLLUP_INFO storage info = rollupInfo[rollupConfig];

    if (info.rollupType != 0) revert RegisterError(2);
    if (!_availableForRegistration(rollupConfig, _type)) revert RegisterError(3);

    if (_type == 1 || _type == 2) {
        address bridge_ = IOptimismSystemConfig(rollupConfig).l1StandardBridge();
        if (bridge_ == address(0)) revert BridgeError();
        l1Bridge[bridge_] = true;
        emit AddedBridge(rollupConfig, bridge_);
    }

    if (_type == 2) {
        address portal_ = IOptimismSystemConfig(rollupConfig).optimismPortal();
        if (portal_ == address(0)) revert PortalError();
        portal[portal_] = true;
        emit AddedPortal(rollupConfig, portal_);
    }

    info.rollupType = _type;
    info.l2TON = _l2TON;
    if (bytes(_name).length != 0) info.name = _name;
    emit RegisteredRollupConfig(rollupConfig, _type, _l2TON, _name);
}
```

RollupInfo

- *rollupType — NONE/LEGACY/OPTIMISM_BEDROCK*
—> LEGACY와 OPTIMISM_BEDROCK?
- 