**index**

## Contract

### Storage Layout

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/404d719a-47c4-49dc-a5c0-623acc742e3c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVIVBVE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpa%2BePhHEDYO3foO9jlKr1LTv2bWaCOXWY4ZECuIKkbQIgAkrX8xu8Q1ScDNfYaMAVQKTpgAmczCEEKHr3MFLtNsgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDA16gh074mLGx%2Fa1uyrcA4orDvylosWJqou0NJ3ufQaQ0643XC3dJLw8nROPZhzi3vFKu9fVB%2BcHgW6BCzlsi6bJMtFxr5sSPblTGSb8qDuudDIUhxkjtu5EXFlls0U4oe3%2B1FJhV3SfePtkWas9GU6Qm45bkuE%2BYCtM4xmPcfJno6LGmTlQJY7fEMfghQ%2FBW828tvDUE6%2FjcAnu1YHEmoBESq98f%2F8EhDUWKntocict%2BMbcR9gNJYQ5kBzNakojJc9NM1vdu9b6tVzTej5GVQQ2q%2B6gxsFMuNTIPyk8njlWYCuQCeXncQYRCr%2BzjRkxRQQFKsx7D9GlZp5BBQEWqQCQcmZlGBajyVpmPELaqHAtLf1RsuFaC2%2B4GiYPrDXMQOld7qbHZN0BDHESe5JODBcMQtFa43M0jPFDVoD6WyNzm1ukk2HmRS5ertQ5foqhvz47DdNFFI83R0JU%2F3cBy2jE07vNPo4oP0CFIUaTynHzDJ5sy4xniH8zToh5B9NLLNR%2BQ0pyygdPKXTjstOQdytipDP9wbYXZlL3WeOh4NXnocNOA2bgL1CfciUc04rTHsz7%2BfekNQKAFYYH1kFW6k%2FNtcEUbTBZQSmRGwUdBhcNqPavh%2FrCiI%2Fj3%2FtCTfUXlzWPJW%2BJMyqLFKCMMMqY28wGOqUBYsoDEmdzePqd5LMRHxQcbQhUrvkpEwxeRB32vBGHPa42qTmGhuh%2Bo0kJmo7bwJSo%2B9x%2F%2FcNnzgmeHe3OnBpI1Is9dhwUmckNKWKAyg6fHYCpuDEDT1xyBGZQT9KMTsenTKpSv4BNYsr5sSMptFaWCcJLQLz51zPeN%2FsLmyKc9KwmplDToD0zaR950cgf4jRvg6QnaC9qLLMqEmswaj1z1iu6EH4R&X-Amz-Signature=2c340df8d19576462bc9d38d379e23447ae0b80c7bddfc5247ea21f578339218&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Setup

[https://sepolia.etherscan.io/txs?a=0xe18a97CD99056A790E5153d554C58a32c5D596Ce&p=3](https://sepolia.etherscan.io/txs?a=0xe18a97CD99056A790E5153d554C58a32c5D596Ce&p=3)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/31423412-6cc8-4398-9484-a7dace31ea45/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVIVBVE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpa%2BePhHEDYO3foO9jlKr1LTv2bWaCOXWY4ZECuIKkbQIgAkrX8xu8Q1ScDNfYaMAVQKTpgAmczCEEKHr3MFLtNsgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDA16gh074mLGx%2Fa1uyrcA4orDvylosWJqou0NJ3ufQaQ0643XC3dJLw8nROPZhzi3vFKu9fVB%2BcHgW6BCzlsi6bJMtFxr5sSPblTGSb8qDuudDIUhxkjtu5EXFlls0U4oe3%2B1FJhV3SfePtkWas9GU6Qm45bkuE%2BYCtM4xmPcfJno6LGmTlQJY7fEMfghQ%2FBW828tvDUE6%2FjcAnu1YHEmoBESq98f%2F8EhDUWKntocict%2BMbcR9gNJYQ5kBzNakojJc9NM1vdu9b6tVzTej5GVQQ2q%2B6gxsFMuNTIPyk8njlWYCuQCeXncQYRCr%2BzjRkxRQQFKsx7D9GlZp5BBQEWqQCQcmZlGBajyVpmPELaqHAtLf1RsuFaC2%2B4GiYPrDXMQOld7qbHZN0BDHESe5JODBcMQtFa43M0jPFDVoD6WyNzm1ukk2HmRS5ertQ5foqhvz47DdNFFI83R0JU%2F3cBy2jE07vNPo4oP0CFIUaTynHzDJ5sy4xniH8zToh5B9NLLNR%2BQ0pyygdPKXTjstOQdytipDP9wbYXZlL3WeOh4NXnocNOA2bgL1CfciUc04rTHsz7%2BfekNQKAFYYH1kFW6k%2FNtcEUbTBZQSmRGwUdBhcNqPavh%2FrCiI%2Fj3%2FtCTfUXlzWPJW%2BJMyqLFKCMMMqY28wGOqUBYsoDEmdzePqd5LMRHxQcbQhUrvkpEwxeRB32vBGHPa42qTmGhuh%2Bo0kJmo7bwJSo%2B9x%2F%2FcNnzgmeHe3OnBpI1Is9dhwUmckNKWKAyg6fHYCpuDEDT1xyBGZQT9KMTsenTKpSv4BNYsr5sSMptFaWCcJLQLz51zPeN%2FsLmyKc9KwmplDToD0zaR950cgf4jRvg6QnaC9qLLMqEmswaj1z1iu6EH4R&X-Amz-Signature=94fa24ae9febd17cb8dcfcb59ff3abf4ea632621aebca4a9428c1343ffa573d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### setLogicContractInfo

[https://sepolia.etherscan.io/tx/0x9fb24ba440afbe6f1c635c2cc6e910a6a46fc6b61b98a9de9163ee44f6c800ac](https://sepolia.etherscan.io/tx/0x9fb24ba440afbe6f1c635c2cc6e910a6a46fc6b61b98a9de9163ee44f6c800ac)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/76e2db4c-e4dc-4177-846d-61bdf1602276/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVIVBVE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpa%2BePhHEDYO3foO9jlKr1LTv2bWaCOXWY4ZECuIKkbQIgAkrX8xu8Q1ScDNfYaMAVQKTpgAmczCEEKHr3MFLtNsgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDA16gh074mLGx%2Fa1uyrcA4orDvylosWJqou0NJ3ufQaQ0643XC3dJLw8nROPZhzi3vFKu9fVB%2BcHgW6BCzlsi6bJMtFxr5sSPblTGSb8qDuudDIUhxkjtu5EXFlls0U4oe3%2B1FJhV3SfePtkWas9GU6Qm45bkuE%2BYCtM4xmPcfJno6LGmTlQJY7fEMfghQ%2FBW828tvDUE6%2FjcAnu1YHEmoBESq98f%2F8EhDUWKntocict%2BMbcR9gNJYQ5kBzNakojJc9NM1vdu9b6tVzTej5GVQQ2q%2B6gxsFMuNTIPyk8njlWYCuQCeXncQYRCr%2BzjRkxRQQFKsx7D9GlZp5BBQEWqQCQcmZlGBajyVpmPELaqHAtLf1RsuFaC2%2B4GiYPrDXMQOld7qbHZN0BDHESe5JODBcMQtFa43M0jPFDVoD6WyNzm1ukk2HmRS5ertQ5foqhvz47DdNFFI83R0JU%2F3cBy2jE07vNPo4oP0CFIUaTynHzDJ5sy4xniH8zToh5B9NLLNR%2BQ0pyygdPKXTjstOQdytipDP9wbYXZlL3WeOh4NXnocNOA2bgL1CfciUc04rTHsz7%2BfekNQKAFYYH1kFW6k%2FNtcEUbTBZQSmRGwUdBhcNqPavh%2FrCiI%2Fj3%2FtCTfUXlzWPJW%2BJMyqLFKCMMMqY28wGOqUBYsoDEmdzePqd5LMRHxQcbQhUrvkpEwxeRB32vBGHPa42qTmGhuh%2Bo0kJmo7bwJSo%2B9x%2F%2FcNnzgmeHe3OnBpI1Is9dhwUmckNKWKAyg6fHYCpuDEDT1xyBGZQT9KMTsenTKpSv4BNYsr5sSMptFaWCcJLQLz51zPeN%2FsLmyKc9KwmplDToD0zaR950cgf4jRvg6QnaC9qLLMqEmswaj1z1iu6EH4R&X-Amz-Signature=6c7f582e5e0ab4c23de012a27a59da0565c8fc04a5d20814cf0f0b5c83313e4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- *_systemConfigProxy: *[*0x3098F8D753ebbD341F472C0aD7f291c81D28dc71*](https://sepolia.etherscan.io/address/0x3098F8D753ebbD341F472C0aD7f291c81D28dc71)
- *_proxyAdmin: *[*0x42BE6e434d98D8b09bBd8a459e3d0e032f780453*](https://sepolia.etherscan.io/address/0x42BE6e434d98D8b09bBd8a459e3d0e032f780453)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/692ed99d-9cbf-464d-af59-4df9d57e091f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVIVBVE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpa%2BePhHEDYO3foO9jlKr1LTv2bWaCOXWY4ZECuIKkbQIgAkrX8xu8Q1ScDNfYaMAVQKTpgAmczCEEKHr3MFLtNsgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDA16gh074mLGx%2Fa1uyrcA4orDvylosWJqou0NJ3ufQaQ0643XC3dJLw8nROPZhzi3vFKu9fVB%2BcHgW6BCzlsi6bJMtFxr5sSPblTGSb8qDuudDIUhxkjtu5EXFlls0U4oe3%2B1FJhV3SfePtkWas9GU6Qm45bkuE%2BYCtM4xmPcfJno6LGmTlQJY7fEMfghQ%2FBW828tvDUE6%2FjcAnu1YHEmoBESq98f%2F8EhDUWKntocict%2BMbcR9gNJYQ5kBzNakojJc9NM1vdu9b6tVzTej5GVQQ2q%2B6gxsFMuNTIPyk8njlWYCuQCeXncQYRCr%2BzjRkxRQQFKsx7D9GlZp5BBQEWqQCQcmZlGBajyVpmPELaqHAtLf1RsuFaC2%2B4GiYPrDXMQOld7qbHZN0BDHESe5JODBcMQtFa43M0jPFDVoD6WyNzm1ukk2HmRS5ertQ5foqhvz47DdNFFI83R0JU%2F3cBy2jE07vNPo4oP0CFIUaTynHzDJ5sy4xniH8zToh5B9NLLNR%2BQ0pyygdPKXTjstOQdytipDP9wbYXZlL3WeOh4NXnocNOA2bgL1CfciUc04rTHsz7%2BfekNQKAFYYH1kFW6k%2FNtcEUbTBZQSmRGwUdBhcNqPavh%2FrCiI%2Fj3%2FtCTfUXlzWPJW%2BJMyqLFKCMMMqY28wGOqUBYsoDEmdzePqd5LMRHxQcbQhUrvkpEwxeRB32vBGHPa42qTmGhuh%2Bo0kJmo7bwJSo%2B9x%2F%2FcNnzgmeHe3OnBpI1Is9dhwUmckNKWKAyg6fHYCpuDEDT1xyBGZQT9KMTsenTKpSv4BNYsr5sSMptFaWCcJLQLz51zPeN%2FsLmyKc9KwmplDToD0zaR950cgf4jRvg6QnaC9qLLMqEmswaj1z1iu6EH4R&X-Amz-Signature=ab28d3108874f99b23ec4fbc65e0e05b931ceba37c2b7d97355df1b9eaaa790e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*ProxyAdmin 컨트랙트는 L1의 Proxy 컨트랙트를 관리하는 Admin 컨트랙트이다. SystemConfig, L1StandardBridge, L1CrossDomainMessenger, OptimismPortal 컨트랙트는 모두 Proxy 컨트랙트이다. 이 함수는 ProxyAdmin 컨트랙트의 codehash를 저장하고, 나머지 Proxy 컨트랙트들은 Implementation 주소(logicAddress)와 proxyCodehash를 저장한다.*

### setSafeConfig

[https://sepolia.etherscan.io/tx/0x9c914d20e4f7436961dc45eae946581e3d33f69e6d081344468547cc50e70445](https://sepolia.etherscan.io/tx/0x9c914d20e4f7436961dc45eae946581e3d33f69e6d081344468547cc50e70445)

*SystemOwnerSafe?*

![](images/3dc39958ca79.png)

```solidity
*// Get the safe wallet address from the proxy admin
IProxyAdmin proxyAdminContract = IProxyAdmin(_l1ProxyAdmin);
address safeWalletAddress = proxyAdminContract.owner();

console.log("Safe wallet address:", safeWalletAddress);
// Get the implementation address of the safe wallet using masterCopy function
address implementation = **IGnosisSafe**(safeWalletAddress).masterCopy();

// Set Safe wallet info with the implementation address and codehash
verifier.setSafeConfig(
    _tokamakDAO, _foundation, _SAFE_THRESHOLD, implementation.codehash, safeWalletAddress.codehash
);*
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3cc17968-f1db-4ab2-bfbc-6070a6e23776/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVIVBVE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpa%2BePhHEDYO3foO9jlKr1LTv2bWaCOXWY4ZECuIKkbQIgAkrX8xu8Q1ScDNfYaMAVQKTpgAmczCEEKHr3MFLtNsgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDA16gh074mLGx%2Fa1uyrcA4orDvylosWJqou0NJ3ufQaQ0643XC3dJLw8nROPZhzi3vFKu9fVB%2BcHgW6BCzlsi6bJMtFxr5sSPblTGSb8qDuudDIUhxkjtu5EXFlls0U4oe3%2B1FJhV3SfePtkWas9GU6Qm45bkuE%2BYCtM4xmPcfJno6LGmTlQJY7fEMfghQ%2FBW828tvDUE6%2FjcAnu1YHEmoBESq98f%2F8EhDUWKntocict%2BMbcR9gNJYQ5kBzNakojJc9NM1vdu9b6tVzTej5GVQQ2q%2B6gxsFMuNTIPyk8njlWYCuQCeXncQYRCr%2BzjRkxRQQFKsx7D9GlZp5BBQEWqQCQcmZlGBajyVpmPELaqHAtLf1RsuFaC2%2B4GiYPrDXMQOld7qbHZN0BDHESe5JODBcMQtFa43M0jPFDVoD6WyNzm1ukk2HmRS5ertQ5foqhvz47DdNFFI83R0JU%2F3cBy2jE07vNPo4oP0CFIUaTynHzDJ5sy4xniH8zToh5B9NLLNR%2BQ0pyygdPKXTjstOQdytipDP9wbYXZlL3WeOh4NXnocNOA2bgL1CfciUc04rTHsz7%2BfekNQKAFYYH1kFW6k%2FNtcEUbTBZQSmRGwUdBhcNqPavh%2FrCiI%2Fj3%2FtCTfUXlzWPJW%2BJMyqLFKCMMMqY28wGOqUBYsoDEmdzePqd5LMRHxQcbQhUrvkpEwxeRB32vBGHPa42qTmGhuh%2Bo0kJmo7bwJSo%2B9x%2F%2FcNnzgmeHe3OnBpI1Is9dhwUmckNKWKAyg6fHYCpuDEDT1xyBGZQT9KMTsenTKpSv4BNYsr5sSMptFaWCcJLQLz51zPeN%2FsLmyKc9KwmplDToD0zaR950cgf4jRvg6QnaC9qLLMqEmswaj1z1iu6EH4R&X-Amz-Signature=2e1f57d263a08dfe75572def6ecf5c56041f1d78bf753fd686e299a509afb048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. *tokamakDAO 그리고 **foundation에 주소**를 지정한다.*
1. *ProxyAdmin은 L1 프록시 컨트랙트를 관리하는 컨트랙트이며, 해당 컨트랙트의 owner는 SafeWallet 주소이다. implementationCodehash는 SafeWallet의 Implementation 컨트랙트 codehash이고, proxyCodehash는 SafeWallet의 Proxy 컨트랙트 codehash이다.*
1. *requiredThreshold는 3 그리고 **ownersCount**도 3으로 지정한다.*

### setBridgeRegistryAddress

*—> L1BridgeRegistryProxy*

### setVerificationPossible

*—> true*

### grantRole

## verifyAndRegisterRollupConfig

**TODO:**

- *Research **[https://github.com/safe-fndn/safe-smart-account/blob/main/contracts/Safe.sol](https://github.com/safe-fndn/safe-smart-account/blob/main/contracts/Safe.sol)*

### _verifySafe

### _verifyProxyAdmin

### _verifyL1Contracts

### registerRollupConfig

[[L1BridgeRegistry]] 

```solidity
*function _registerRollupConfig(
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
}*
```