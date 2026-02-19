**index**

### Storage Layout

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/28fa6a65-bf01-4a15-ab77-4084fb5f7983/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOKTTBFN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnJ1%2FSJI4%2Bn1JA%2FO%2FG0kH2a62XKy%2Btbwa7Si2x56bW5AiBbGB55poa1EhdrL7369t65XP0dNRMTkNnprWDvOKlDuir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMGD03rsqS3UPClK47KtwDRX2LTvLRqv6RPixEhhkrBwrHGHOyCH5W%2FmCsNpmS3MM2Y8i5mNDAvgvjbEECgCDY6XFCRn52tCjNnJOlalRUetpuG%2FqdA92NOq%2F517VLkTnLzEm0xol5a%2FPUTsSlccazLcB0qlFLSh3L45fbZTUgP3wfDHZ3G7twhHvvkK%2FbcHHEeooqnl39s3750oFVz9fPMIo%2BaInvqysYkgdH%2F3CSD4TfpwxEd66fbgc1ogIWruUzpyxwGpJ9UZm6Xw1aS0KeGqjQ2NB4y8gXh854IVHJIxoYzsppCEv57elPhUvKuzvSlsuf9S8coN5EIslhmMYYN36ph7BG7gn%2BwWJdxzoasrsscSHh5%2BsFxakbwYr5mcJSfZicFXt9aqyiKGV6DdsnWmxlwXlP4vuLvN%2F7U2OjKxQ%2Bhzt0h4rXTPaYByUwjMIkK3MaItVffhVDfbM1Ry4L%2BkWsIh3w%2B9DDIrxCQ0p6d%2FWxU3K4D%2FUotNCUxxfe5FmnTMENwg6tDgwX1RWhs0SI%2BHRbDinFN7apAKYR2Mkx9CS3HWZBNvA8hNMLHhJaCDz%2BsuMuonDA11UF0K6vNCg9Yeq0qL1DJ%2FP4fu4PdmER9mwc%2Fgq0tsOF4gI8069GYFI1%2FhkUgHCE3Fxwo5Ywuu7ZzAY6pgEKVa%2B9enfVx4q0pAR1T5NTEGRmrBaZU4OSGKEpdwwEZfggAN%2Bv%2FauwbrJovkyH1YWRrVNsbIK4KJsZ8s4dyiffKT8tyBOKQe%2BdgM0MTVH%2Fm4fWSzsBGbWwUTPYN9z3IXl8Y6dq9zaqSsaCZE2lIQXtuqWWQrCgjETTipOKTkCQ3R6SuEl9o3eLNQ4uqgJ4zP7vJPSvNv7brewTKDuOz2xdMiFfC4YZ&X-Amz-Signature=cd2414b74c37eac19deb1fbcdc69213fa71711d372ddf5e8d2b0054259740058&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> ***DAOCommitteeProxy2, DAOCommitteeOwner, 그리고 DAOCommittee_V1 컨트랙트의 storage layout은 모두 동일하다.***

1. *`ton`*
1. *`daoVault`*
1. *`agendaManager`*
1. *`candidateFactory`**: *
1. *`layer2Registry`*
1. *`seigManager`*
1. *candidates*
1. *members*
1. *maxMember*
1. *_candidateInfos*
1. *quorum*
1. *activityRewardPerSecond*
1. *_roles*
1. *_supportedInterfaces*
1. *`_implementation`*
1. *_oldCandidateInfos*
1. *`wton`*
1. *`layer2Manager`*
1. *`candidateAddOnFactory`*
1. *`proxyImplementation`*
1. *`aliveImplementation`*
1. *`selectorImplementation`*
1. *blacklist*
1. *privateLayer2*
1. *cooldown*
1. *cooldownTime*

> *주소는 **`address`**로 표시한다.*

### Functions

1. `removeFromBlacklist`:
1. `createCandidate`: 

[[DAOCommittee Upgrade History]]

[[DAOCommitteeProxy & DAOCommitteeProxy2]]