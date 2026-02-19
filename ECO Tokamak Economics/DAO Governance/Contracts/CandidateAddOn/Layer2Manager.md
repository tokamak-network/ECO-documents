*l2ManagerContract.RegisterCandidateAddOn*

***TODO:***

- *rollupConfig —> systemConfig*

*(1) registerCandidateAddOn*

```solidity
*function registerCandidateAddOn(
    address rollupConfig,
    uint256 amount,
    bool flagTon,
    string calldata memo
) external {
    _nonZeroAddress(rollupConfig);
    if (bytes(memo).length == 0) revert ZeroBytesError();
    if (rollupConfigInfo[rollupConfig].operatorManager != address(0)) revert RegisterError(4);

    if (!_availableRegister(rollupConfig)) revert RegisterError(5);
    _transferDepositAmount(msg.sender, rollupConfig, amount, flagTon, memo);
}*
```

*(2) _transferDepositAmount*

*(3) _registerCandidateAddOn*