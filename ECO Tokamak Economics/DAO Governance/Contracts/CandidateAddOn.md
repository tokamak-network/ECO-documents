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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d5b53cca-127e-4a85-a309-38b0acc0be72/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4OVJAYG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGpVq0mpC5N2j0CDPOgn3QBPhcnUqRQAT6LVoV4fZphnAiEA0u1Q5r2RSn40m6IywF228OMaJV1KdWqMsj1mk2cE3ZIq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDIQ%2BbsEysNr0I%2BmLISrcA1WQ31F8RhkU4%2BwtSPsu8G4b%2Bu8que%2F0zoDiVuG2wTEwC%2BCloVofVnmIOexL%2FcRqjUq431As9vS2jlupZSVXlmWtrReW4vDb8EUlcdqU6x7j5ndgJtSHBaS%2FkUqP1N97voA%2Fol9v6JayPk2uwURGtVYCd0HBBSHVbQkJyK8KPwwcqG0z6jYp7hMB9p9JmHuxvbHgWeKdafEqjg%2BY4trpCDLjxcy6cmQ3f44P%2B6qtBUK2u04ATy%2F6JJtmaKDInZOIC3wpsIFDni0hqdkwX%2BCMzbvWkKv5esVWOuzSIXVE04vUpd0Ec6ul7zaPGhb4S8q9%2B4nBywWTFfMLwLRf8OEdTRSL%2BOePflQjzO41xFc50uTKlF7vR4ThGFwaUhd%2Bhy2hWBHVQtsqQ1V9g6ZCkIPeBIk5v5I%2FSFhl%2FVYyBSS6XJ2HgIR2lLkTEqJuFZMnX9ju%2Fvl29l7C3QduCUwxgUC82CeaX4LMzihj7X8siWMqDFDUjX2EPtTNBE3DYZ7oVD%2FpitCOZed9a8xlkkrmMRKk%2BIBy2GRFFrClBU%2Bxwhkhw274rStFWFtUfRhSewmKkAqGPq0mKQIg7OuzqpITNWwr0G6bhcuNuAaogwLLffv8FCevisAs%2FAGIxcS32PhvMKbx2cwGOqUBG%2BsoKcr4YtO6cHhBxQDWDTJuDRU8%2BwRHiLYxi2Ka56dj3sxFyU2mIJhX4OeIWI4xXUEUJL4gqqQ9L3zdzl1CdqjtK4HWSY9ytiVLe2Xwo3ybu5MWKTkPUl4RZA6lS9Eas7PrmL7oERMiPGNfxXCxCVQEXBbSlU0CPccWHkqNOwWTpFuZZ2w6Po6oxFT2JwadJdYfI4z04WCaAabtD5JFKYZ3dSmA&X-Amz-Signature=23dea57bb20d419dacc1bfb5c7c98e3550454fb09704b15ae99463678c4815c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![*Layer2ManagerProxy.sol*](images/b70ccc009fc4.png)

![*Layer2ManagerV1_1.sol*](images/21f56b98d8a3.png)

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