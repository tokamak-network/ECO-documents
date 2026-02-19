**index**

## Contract

### Storage Layout

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/404d719a-47c4-49dc-a5c0-623acc742e3c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O24JR6C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGUJojbSzmk9cK1JdPUHiSSNyTR5YzYz2tOkQ1HsyskAiEAxlwOjIGFFSfUh85qhOIfGmdp%2FlrnSi2T4g7mtVLEEuwq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDtiS%2BRhlexs67rKQSrcA%2B7I7%2BwRZN3maH6uMpUooFB6iURHJ1WERh7hi8xRqNC2SbM8Hs6%2F5i5gSJpl%2FJ1%2FvJGwe%2B55KBDBnX4HB7n0yFFCQy%2FofAfJC2FxXrLPkHGpq%2FkfiZ9jSG%2B%2FN7Ey5ACRDAXMwSSgG04F4ApQNFF2Wz353Bdt4uuA46%2BrpndgbTV8Yby2MLMeoMcJBfKZrmt4ssb3uXU65Nzr2o7RXje0X3E0oyGIt%2BMCYnJgqLhNIBFr3l%2F3Skqi2KWQPvpv8E1yBLZpFURcJkESRNjrjjvO%2FzGKt0w5sGSt2lsbS79w2YfJqHIaAYY0uUEGVWXJpVGpxHkXSMsVKmBuyvIdoOVQ5UkM%2FpYnQ1Y9qAal4K5Oe%2FcX7q7kcaZric7chBweJkszi%2BJtaiuDo5tD8AAXR5vel5mGnouBFTZaC9indKA848AB2X3JJuSCxxMJn0GK3plPCjNgNfpZx%2BCdCqEwkRcXdzYvLhT1NdFqOHin01Ng0BaC0iozSTIz%2FASCWqo1q0S5HFTbWGa%2Bd53I5o3uuqtCkcRcfGHMhTzeteQ3k8IwCzWPUGHCvaB4W2cSFMNEhWyjNnBijWvg0Qf17mo214a8srUUVN4F3Gg%2BwF%2FsglAv5KofnxKCQ7SnLFJ4OGmkMK602swGOqUBjG4ttjD2u67Ae%2B2AwE5L9NPlBEekoyetVBYjwGVp9ihbUqbBc8tFfsJi54xEbN231qZyHWxXDQMLWH4tcbjGpWIvH%2Fyd7%2FqHVQns1ey22uMYYKyD%2FW7uQCVmLJsTBeVptKcbdb8FC%2BY68pYHmBhkXdi197%2FOUQn%2FqjNp3y5NbJRXKY%2Byf1GwHU1wTwjrCEYcd3leYfFfmGys1ZIuQILl6xInIV7l&X-Amz-Signature=7b02e46afdc79b0da10750ddc8ab5cd5095cfce32d6c79767e915a3184e88a5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Setup

[https://sepolia.etherscan.io/txs?a=0xe18a97CD99056A790E5153d554C58a32c5D596Ce&p=3](https://sepolia.etherscan.io/txs?a=0xe18a97CD99056A790E5153d554C58a32c5D596Ce&p=3)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/31423412-6cc8-4398-9484-a7dace31ea45/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O24JR6C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGUJojbSzmk9cK1JdPUHiSSNyTR5YzYz2tOkQ1HsyskAiEAxlwOjIGFFSfUh85qhOIfGmdp%2FlrnSi2T4g7mtVLEEuwq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDtiS%2BRhlexs67rKQSrcA%2B7I7%2BwRZN3maH6uMpUooFB6iURHJ1WERh7hi8xRqNC2SbM8Hs6%2F5i5gSJpl%2FJ1%2FvJGwe%2B55KBDBnX4HB7n0yFFCQy%2FofAfJC2FxXrLPkHGpq%2FkfiZ9jSG%2B%2FN7Ey5ACRDAXMwSSgG04F4ApQNFF2Wz353Bdt4uuA46%2BrpndgbTV8Yby2MLMeoMcJBfKZrmt4ssb3uXU65Nzr2o7RXje0X3E0oyGIt%2BMCYnJgqLhNIBFr3l%2F3Skqi2KWQPvpv8E1yBLZpFURcJkESRNjrjjvO%2FzGKt0w5sGSt2lsbS79w2YfJqHIaAYY0uUEGVWXJpVGpxHkXSMsVKmBuyvIdoOVQ5UkM%2FpYnQ1Y9qAal4K5Oe%2FcX7q7kcaZric7chBweJkszi%2BJtaiuDo5tD8AAXR5vel5mGnouBFTZaC9indKA848AB2X3JJuSCxxMJn0GK3plPCjNgNfpZx%2BCdCqEwkRcXdzYvLhT1NdFqOHin01Ng0BaC0iozSTIz%2FASCWqo1q0S5HFTbWGa%2Bd53I5o3uuqtCkcRcfGHMhTzeteQ3k8IwCzWPUGHCvaB4W2cSFMNEhWyjNnBijWvg0Qf17mo214a8srUUVN4F3Gg%2BwF%2FsglAv5KofnxKCQ7SnLFJ4OGmkMK602swGOqUBjG4ttjD2u67Ae%2B2AwE5L9NPlBEekoyetVBYjwGVp9ihbUqbBc8tFfsJi54xEbN231qZyHWxXDQMLWH4tcbjGpWIvH%2Fyd7%2FqHVQns1ey22uMYYKyD%2FW7uQCVmLJsTBeVptKcbdb8FC%2BY68pYHmBhkXdi197%2FOUQn%2FqjNp3y5NbJRXKY%2Byf1GwHU1wTwjrCEYcd3leYfFfmGys1ZIuQILl6xInIV7l&X-Amz-Signature=ed6818dc2ccfe70f775faf42417a4e2e0eb839c9f454a8bdea64ebd552a750bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### setLogicContractInfo

[https://sepolia.etherscan.io/tx/0x9fb24ba440afbe6f1c635c2cc6e910a6a46fc6b61b98a9de9163ee44f6c800ac](https://sepolia.etherscan.io/tx/0x9fb24ba440afbe6f1c635c2cc6e910a6a46fc6b61b98a9de9163ee44f6c800ac)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/76e2db4c-e4dc-4177-846d-61bdf1602276/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O24JR6C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGUJojbSzmk9cK1JdPUHiSSNyTR5YzYz2tOkQ1HsyskAiEAxlwOjIGFFSfUh85qhOIfGmdp%2FlrnSi2T4g7mtVLEEuwq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDtiS%2BRhlexs67rKQSrcA%2B7I7%2BwRZN3maH6uMpUooFB6iURHJ1WERh7hi8xRqNC2SbM8Hs6%2F5i5gSJpl%2FJ1%2FvJGwe%2B55KBDBnX4HB7n0yFFCQy%2FofAfJC2FxXrLPkHGpq%2FkfiZ9jSG%2B%2FN7Ey5ACRDAXMwSSgG04F4ApQNFF2Wz353Bdt4uuA46%2BrpndgbTV8Yby2MLMeoMcJBfKZrmt4ssb3uXU65Nzr2o7RXje0X3E0oyGIt%2BMCYnJgqLhNIBFr3l%2F3Skqi2KWQPvpv8E1yBLZpFURcJkESRNjrjjvO%2FzGKt0w5sGSt2lsbS79w2YfJqHIaAYY0uUEGVWXJpVGpxHkXSMsVKmBuyvIdoOVQ5UkM%2FpYnQ1Y9qAal4K5Oe%2FcX7q7kcaZric7chBweJkszi%2BJtaiuDo5tD8AAXR5vel5mGnouBFTZaC9indKA848AB2X3JJuSCxxMJn0GK3plPCjNgNfpZx%2BCdCqEwkRcXdzYvLhT1NdFqOHin01Ng0BaC0iozSTIz%2FASCWqo1q0S5HFTbWGa%2Bd53I5o3uuqtCkcRcfGHMhTzeteQ3k8IwCzWPUGHCvaB4W2cSFMNEhWyjNnBijWvg0Qf17mo214a8srUUVN4F3Gg%2BwF%2FsglAv5KofnxKCQ7SnLFJ4OGmkMK602swGOqUBjG4ttjD2u67Ae%2B2AwE5L9NPlBEekoyetVBYjwGVp9ihbUqbBc8tFfsJi54xEbN231qZyHWxXDQMLWH4tcbjGpWIvH%2Fyd7%2FqHVQns1ey22uMYYKyD%2FW7uQCVmLJsTBeVptKcbdb8FC%2BY68pYHmBhkXdi197%2FOUQn%2FqjNp3y5NbJRXKY%2Byf1GwHU1wTwjrCEYcd3leYfFfmGys1ZIuQILl6xInIV7l&X-Amz-Signature=23b501bb903e683e976be5b87d8992397708071db98203a3b7f59d773dac2d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- *_systemConfigProxy: *[*0x3098F8D753ebbD341F472C0aD7f291c81D28dc71*](https://sepolia.etherscan.io/address/0x3098F8D753ebbD341F472C0aD7f291c81D28dc71)
- *_proxyAdmin: *[*0x42BE6e434d98D8b09bBd8a459e3d0e032f780453*](https://sepolia.etherscan.io/address/0x42BE6e434d98D8b09bBd8a459e3d0e032f780453)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/692ed99d-9cbf-464d-af59-4df9d57e091f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O24JR6C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGUJojbSzmk9cK1JdPUHiSSNyTR5YzYz2tOkQ1HsyskAiEAxlwOjIGFFSfUh85qhOIfGmdp%2FlrnSi2T4g7mtVLEEuwq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDtiS%2BRhlexs67rKQSrcA%2B7I7%2BwRZN3maH6uMpUooFB6iURHJ1WERh7hi8xRqNC2SbM8Hs6%2F5i5gSJpl%2FJ1%2FvJGwe%2B55KBDBnX4HB7n0yFFCQy%2FofAfJC2FxXrLPkHGpq%2FkfiZ9jSG%2B%2FN7Ey5ACRDAXMwSSgG04F4ApQNFF2Wz353Bdt4uuA46%2BrpndgbTV8Yby2MLMeoMcJBfKZrmt4ssb3uXU65Nzr2o7RXje0X3E0oyGIt%2BMCYnJgqLhNIBFr3l%2F3Skqi2KWQPvpv8E1yBLZpFURcJkESRNjrjjvO%2FzGKt0w5sGSt2lsbS79w2YfJqHIaAYY0uUEGVWXJpVGpxHkXSMsVKmBuyvIdoOVQ5UkM%2FpYnQ1Y9qAal4K5Oe%2FcX7q7kcaZric7chBweJkszi%2BJtaiuDo5tD8AAXR5vel5mGnouBFTZaC9indKA848AB2X3JJuSCxxMJn0GK3plPCjNgNfpZx%2BCdCqEwkRcXdzYvLhT1NdFqOHin01Ng0BaC0iozSTIz%2FASCWqo1q0S5HFTbWGa%2Bd53I5o3uuqtCkcRcfGHMhTzeteQ3k8IwCzWPUGHCvaB4W2cSFMNEhWyjNnBijWvg0Qf17mo214a8srUUVN4F3Gg%2BwF%2FsglAv5KofnxKCQ7SnLFJ4OGmkMK602swGOqUBjG4ttjD2u67Ae%2B2AwE5L9NPlBEekoyetVBYjwGVp9ihbUqbBc8tFfsJi54xEbN231qZyHWxXDQMLWH4tcbjGpWIvH%2Fyd7%2FqHVQns1ey22uMYYKyD%2FW7uQCVmLJsTBeVptKcbdb8FC%2BY68pYHmBhkXdi197%2FOUQn%2FqjNp3y5NbJRXKY%2Byf1GwHU1wTwjrCEYcd3leYfFfmGys1ZIuQILl6xInIV7l&X-Amz-Signature=f1d4b1b38703a7a1827c17eb08ebc6da0635426f268f72fc008c9733e786f911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*ProxyAdmin 컨트랙트는 L1의 Proxy 컨트랙트를 관리하는 Admin 컨트랙트이다. SystemConfig, L1StandardBridge, L1CrossDomainMessenger, OptimismPortal 컨트랙트는 모두 Proxy 컨트랙트이다. 이 함수는 ProxyAdmin 컨트랙트의 codehash를 저장하고, 나머지 Proxy 컨트랙트들은 Implementation 주소(logicAddress)와 proxyCodehash를 저장한다.*

### setSafeConfig

[https://sepolia.etherscan.io/tx/0x9c914d20e4f7436961dc45eae946581e3d33f69e6d081344468547cc50e70445](https://sepolia.etherscan.io/tx/0x9c914d20e4f7436961dc45eae946581e3d33f69e6d081344468547cc50e70445)

*SystemOwnerSafe?*

![](images/1e5fedc67197.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3cc17968-f1db-4ab2-bfbc-6070a6e23776/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O24JR6C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGUJojbSzmk9cK1JdPUHiSSNyTR5YzYz2tOkQ1HsyskAiEAxlwOjIGFFSfUh85qhOIfGmdp%2FlrnSi2T4g7mtVLEEuwq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDtiS%2BRhlexs67rKQSrcA%2B7I7%2BwRZN3maH6uMpUooFB6iURHJ1WERh7hi8xRqNC2SbM8Hs6%2F5i5gSJpl%2FJ1%2FvJGwe%2B55KBDBnX4HB7n0yFFCQy%2FofAfJC2FxXrLPkHGpq%2FkfiZ9jSG%2B%2FN7Ey5ACRDAXMwSSgG04F4ApQNFF2Wz353Bdt4uuA46%2BrpndgbTV8Yby2MLMeoMcJBfKZrmt4ssb3uXU65Nzr2o7RXje0X3E0oyGIt%2BMCYnJgqLhNIBFr3l%2F3Skqi2KWQPvpv8E1yBLZpFURcJkESRNjrjjvO%2FzGKt0w5sGSt2lsbS79w2YfJqHIaAYY0uUEGVWXJpVGpxHkXSMsVKmBuyvIdoOVQ5UkM%2FpYnQ1Y9qAal4K5Oe%2FcX7q7kcaZric7chBweJkszi%2BJtaiuDo5tD8AAXR5vel5mGnouBFTZaC9indKA848AB2X3JJuSCxxMJn0GK3plPCjNgNfpZx%2BCdCqEwkRcXdzYvLhT1NdFqOHin01Ng0BaC0iozSTIz%2FASCWqo1q0S5HFTbWGa%2Bd53I5o3uuqtCkcRcfGHMhTzeteQ3k8IwCzWPUGHCvaB4W2cSFMNEhWyjNnBijWvg0Qf17mo214a8srUUVN4F3Gg%2BwF%2FsglAv5KofnxKCQ7SnLFJ4OGmkMK602swGOqUBjG4ttjD2u67Ae%2B2AwE5L9NPlBEekoyetVBYjwGVp9ihbUqbBc8tFfsJi54xEbN231qZyHWxXDQMLWH4tcbjGpWIvH%2Fyd7%2FqHVQns1ey22uMYYKyD%2FW7uQCVmLJsTBeVptKcbdb8FC%2BY68pYHmBhkXdi197%2FOUQn%2FqjNp3y5NbJRXKY%2Byf1GwHU1wTwjrCEYcd3leYfFfmGys1ZIuQILl6xInIV7l&X-Amz-Signature=138d22edd48a7fcbfb33feee7a8675bf228120af5c384793301deea15c5c031a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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