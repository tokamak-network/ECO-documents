**index**

Summary:

- Candidate는 세 가지 종류로 나뉜다: 일반 Candidate, Layer 2 Candidate, CandidateAddOn
  - Layer 2 Candidate는 Layer 2 등록 이후 Candidate를 별도로 등록하는 과정으로 분리되어 있다. 반면 CandidateAddOn은 trh-sdk가 L1BridgeRegistry 컨트랙트에 등록할 때 동시에 CandidateAddOn으로 등록된다.

[[trh-sdk deploy-contracts, deploy, verify-register-candidate]]

[[L1ContractVerification]]

[[L1BridgeRegistry]]

[[Layer2Manager]]

[[OperatorManager]]

[[SeigManagerV1_3.sol]]

L1ContractVerification에서 검증을 한다. L1ContractVerification가 L1BridgeRegistry 컨트랙트에 등록을 완료한다.

> ***The tokamak rollup hub SDK(TRH-SDK) allows anyone to quickly deploy customized and autonomous Layer 2 Rollups on the Ethereum network.***

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d5b53cca-127e-4a85-a309-38b0acc0be72/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656FAZROC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDDyLCuDQDktwKCYLaBgPp9gOmQsnRmkN5tkb0zymfYgIgdv%2Bl%2F5nyOaKm9GACCuMV%2FWy%2Bwn553HjZeYcGS7r%2B42Eq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDK%2BnaZn7ycx6QY8EpircA9OcVVFXFSfoq80mCdFB6e4KHNFxdepzFW5wKuxC99DhQZApED1ZeZeWxDijZRYqnrAbTwR1bQ9n5yjT9yiRX7rcjCB5yRzLG5QA7K%2B0ellG3uSaODvFoqYt9Ztc0tZqiKolKZ3jqscl0zrVTeVBbbTlbwX2K87PUtAzNrxm1ct1%2BJOkzvpaRwYFIAjK%2BSXoG5HyA%2BY4uwI2gZxXUZksg8Zu5EJDO7KLYRjjbsk94aIhX02VNpVmeMmJYvnlA1NM5Tbzo%2BwTXVU%2BRfHl5adIxVsCDyvDak7FV%2FwFyG6weycD6Q6jKUbgXQRSOdnOfUQkvfXY%2FF8LCfb7u%2BviWdPnD2h9YzQeOTiR42%2FS3fagnwZ3%2FqszjmEN3c%2FF1ItBXenzF%2FYUwaWS1729k0FKNY%2FhtnCZ0y0S2F41bveoObfoH7Kr32H4YCKlmmPsdAR3t9%2FCtnnSei0LrGiEBqGNi9jqStPPPZoXw8Ju4Pm7NEVSiszbf5nrVSOvbUiUHW6pSNFpH%2F%2FUu3w6WAyC%2Bbyt%2BitsylJAt1RZ0JEI6Pkid0NOteA0%2Bu3SF40bU%2FY2qGBXWOMuHRLT8DbC6%2BQ7%2FyqHXFzFP%2F1OcvfyJIjrHyu7qFE5nt1eb%2FxkxYIkQHdrU76BMLaY28wGOqUBsyGgtQrFRaP7tkSjwWkhX5IDYnyVQsmFxKMA93dIk8SKCACraOsw7WxaDSYAu%2FC5KdK%2FOzdNAHSWW9ExplGxtVM2qih9NFnD1mM8J5yAgJ%2Ft0GgyVnXbQ7lE0%2FYy%2BtJlhnPiqQN%2FqQEyPtdfrXy%2Bt7B7j7GTv8gg37aVZh2XU1eojwH9Cu5Ng1Mb4ZbLKFSRn1LWfPvni%2BboUvLVnxxtVKOPcSyz&X-Amz-Signature=e1846441d803b89dfa5fbc3cb268b0f0ab2f519d8e978895cc80d5d30c0d2f73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Setup

- [*Layer2ManagerProxy*](https://etherscan.io/address/0xD6Bf6B2b7553c8064Ba763AD6989829060FdFC1D#code)
  - *`upgradeTo`** — Layer2ManagerV1_1*
  - `setAddresses`
    - *_l1BridgeRegisry — *[*0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4*](https://etherscan.io/address/0x39d43281A4A5e922AB0DCf89825D73273D8C5BA4)*, _operatorManagerFactory — *[*0xAf86b21edDdC78ea27E23A7F2151d60d4e069450*](https://etherscan.io/address/0xAf86b21edDdC78ea27E23A7F2151d60d4e069450)*, _ton, _wton, _dao, _depositManager, _seigManager, _swapProxy — *[*0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d*](https://etherscan.io/address/0x30e65B3A6e6868F044944Aa0e9C5d52F8dcb138d)
  - *`setMinimumInitialDepositAmount`** — 1000100000000000000000*
  - *`transferOwnership`** — DAOCommitteeProxy*
- [*Layer2ManagerV1_1*](https://etherscan.io/address/0x2EB7f500125f11544392B83B87cDEb9456f3509f#code)

### Storage Layout

> 2b6d96a4-00a3-80bc-9889-ee9d186639a9***와 마찬가지로, Proxy 컨트랙트와 Logic 컨트랙트의 storage layout이 동일하다.***

![*Layer2ManagerProxy.sol*](images/2204710456f8.png)

![*Layer2ManagerV1_1.sol*](images/0ba5018c6e01.png)

***storage slots:***

1. *pauseProxy*
1. *proxyImplementation*
1. *aliveImplementation*
1. *selectorImplementation*
1. *_supportedInterfaces*
1. *_roles*

1. *l1BridgeRegistry*
1. *operatorManagerFactory*
1. *ton*
1. *wton*
1. *dao*
1. *depositManager*
1. *seigManager*
1. *swapProxy*
1. *minimumInitialDepositAmount*
1. *rollupConfigInfo*
1. *operatorInfo*
1. *operatorOfLayer*
1. *_lock*