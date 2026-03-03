**index**

## V1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/210c13c5-4995-4eac-b2a4-bc7e9e6eb009/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7XXJAH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTiyQ6hKjaLFL99D8Umi1JyksZmZmmdnHx3fmOWzlCqwIgdzcsYUPsKA6Uzp1TgfAi33YmLrNoLl%2B8ARz%2BYXdOdxIq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDOxjzeUe%2FEpXFRJ90CrcA33juyto2aRYOgT3XIzYCiBakZ2r2XhG5SZmpUvIszR4X3YuWux%2FXiRBR%2B%2F0XJ8APT2Y2xJQXL71MhzMSMS3f5Khk88wgmcKbAF0XqCIzC41rEcSJxp3MMVqLfmFCe9SvOwGi4gDLpp7gfSiB6Hq0o5tAeY7kU4uhaVT0x0KQ3mC6TbYjBFeOdmw2L8%2FaTgzrtIGgbZkk1qcz5XdAvwhmCL3CspDyXoXUFDdfGAE%2BDFjRYpVXTdbWy93moljwgRWNgW%2BoT09jsVO2TQSeGJRqqmmpw366n4wvNRHw0ZWuJ2LrxImesAmhkM3eaTgi4mT%2Fe9XteiF6dQFsvx9Y7Fm0LChrT2tFBc3b4O0fvGj31Mv1ZqOTxoG2Uo1bErF%2FqoCDHycZbYbcIG7USoMxuEKA8PXdAQb3tq8zl1Y7HMRrT%2BS44QPswqjIMkd%2BAKVJOOel7ObKdsWovsoSrBrK0sVouH5WUtGs7fozX6U50jKy9t3R54jSlUjQLQ8SWK%2FVoqw3QrJraW%2FTVVURWRlUYY8VrMgze6m%2FY4UJ3PqRf9aRscsNwmc2%2FHvrl%2F%2B8W7ZzoXXp0QVkRuW%2Bo1G47Cz8co4bZpQnYQ6uhty%2BQDpWCxpCjBkweNZiOu%2FS%2BPHQhUVMIiZ28wGOqUB7kKE%2BznizB4YC7GuMd4L6qA1f0GYPrD7tp5Se5E%2Ffbhew7JOPqCmG7n8NrFUNN58rJ%2B7fDLMkpVNYc9neEJep3ioE%2F8wsFwaMJYp97CcbvgCDYYbwJx0q85YEzMWsQa%2FVqabhBtr00dSurqoFY6WgEzFfrnMNfIFGWEI8QL7Z2tH3GuA4pmhMOaPrsu9gdh6zzeCUYTWNcpTyrKmr6p9VsK2q2IM&X-Amz-Signature=8b500e26acf8210ee356c11ad51141461ea1fbfa03a8fc913efd46bf31a94d3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

***DAOCommitteeProxy:**** *[*0xDD9f0cCc044B0781289Ee318e5971b0139602C26*](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)

***DAOCommittee:**** *[*0xd1a3fddccd09cebcfcc7845ddba666b7b8e6d1fb*](https://etherscan.io/address/0xd1a3fddccd09cebcfcc7845ddba666b7b8e6d1fb#code)

> ***실제로 V1이 배포된 주소는 ****[https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L13-L14](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L13-L14)****에서 확인할 수 있다.***

## V2

### upgradeTo

*V1에서 V2로 업그레이드하려면 *[*Proxy 컨트랙트의 upgradeTo 함수*](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOCommitteeProxy.sol#L62-L69)*를 호출해야 한다.*

![[*https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26?mtd=0x3659cfe6~Upgrade To*](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26?mtd=0x3659cfe6~Upgrade%20To)](images/d1b4fdaa811c.png)

1. ***DAOCommittee —> DAOCommitteeExtend ****(0x4B4b52c7042Ae24f74c5C42C09bc925FeFaFA49E)*
1. ***DAOCommittee —> DAOCommitteeExtend  ****(0x72655449e82211624D5F4D2ABb235bB6Fe2fe989)*
1. ***DAOCommittee —> DAOCommitteeExtend  ****(0x4B4b52c7042Ae24f74c5C42C09bc925FeFaFA49E)*
1. ***DAOCommitteeExtend —> DAOCommitteeOwner ****(0xe070fFD0E25801392108076ed5291fA9524c3f44)*
1. ***DAOCommitteeOwner —> DAOCommitteeVault ****(0xba5634e0c432Af80060CF19E0940B59b2DC31173)*
1. ***DAOCommitteeVault —> DAOCommitteeOwner ****(0xe070fFD0E25801392108076ed5291fA9524c3f44) — ****rollback!***
1. ***DAOCommitteeOwner —> *****DAOCommittee_V1 ***(0xdF2eCda32970DB7dB3428FC12Bc1697098418815)* — ***current logic contract***

### **setTargetUpgradeTo**

*DAOCommitteeOwner 컨트랙트에는 setTargetUpgradeTo 함수가 있다. 이 함수를 통해 특정 target 컨트랙트를 강제로 업그레이드할 수 있다.*

```solidity
function setTargetUpgradeTo(address target, address logic) external onlyOwner {
    ITarget(target).upgradeTo(logic);
}
```

![](images/73f2fa46f080.png)

1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManager`******  — ***[https://etherscan.io/tx/0xaaa7e6494b270a4a1a5a9eee36d207013e894c418836e1990dc71d4ae77d4eac](https://etherscan.io/tx/0xaaa7e6494b270a4a1a5a9eee36d207013e894c418836e1990dc71d4ae77d4eac)
1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManagerV1_1`****** — ***[*https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3*](https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3)** **
1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManagerV1_2`****** — ***[https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46](https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46)

### Execute Agenda

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0aa629f7-413f-4556-a5bf-90932763dabd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7XXJAH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTiyQ6hKjaLFL99D8Umi1JyksZmZmmdnHx3fmOWzlCqwIgdzcsYUPsKA6Uzp1TgfAi33YmLrNoLl%2B8ARz%2BYXdOdxIq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDOxjzeUe%2FEpXFRJ90CrcA33juyto2aRYOgT3XIzYCiBakZ2r2XhG5SZmpUvIszR4X3YuWux%2FXiRBR%2B%2F0XJ8APT2Y2xJQXL71MhzMSMS3f5Khk88wgmcKbAF0XqCIzC41rEcSJxp3MMVqLfmFCe9SvOwGi4gDLpp7gfSiB6Hq0o5tAeY7kU4uhaVT0x0KQ3mC6TbYjBFeOdmw2L8%2FaTgzrtIGgbZkk1qcz5XdAvwhmCL3CspDyXoXUFDdfGAE%2BDFjRYpVXTdbWy93moljwgRWNgW%2BoT09jsVO2TQSeGJRqqmmpw366n4wvNRHw0ZWuJ2LrxImesAmhkM3eaTgi4mT%2Fe9XteiF6dQFsvx9Y7Fm0LChrT2tFBc3b4O0fvGj31Mv1ZqOTxoG2Uo1bErF%2FqoCDHycZbYbcIG7USoMxuEKA8PXdAQb3tq8zl1Y7HMRrT%2BS44QPswqjIMkd%2BAKVJOOel7ObKdsWovsoSrBrK0sVouH5WUtGs7fozX6U50jKy9t3R54jSlUjQLQ8SWK%2FVoqw3QrJraW%2FTVVURWRlUYY8VrMgze6m%2FY4UJ3PqRf9aRscsNwmc2%2FHvrl%2F%2B8W7ZzoXXp0QVkRuW%2Bo1G47Cz8co4bZpQnYQ6uhty%2BQDpWCxpCjBkweNZiOu%2FS%2BPHQhUVMIiZ28wGOqUB7kKE%2BznizB4YC7GuMd4L6qA1f0GYPrD7tp5Se5E%2Ffbhew7JOPqCmG7n8NrFUNN58rJ%2B7fDLMkpVNYc9neEJep3ioE%2F8wsFwaMJYp97CcbvgCDYYbwJx0q85YEzMWsQa%2FVqabhBtr00dSurqoFY6WgEzFfrnMNfIFGWEI8QL7Z2tH3GuA4pmhMOaPrsu9gdh6zzeCUYTWNcpTyrKmr6p9VsK2q2IM&X-Amz-Signature=d83671fa3844c07e5af67371ed526f99f9e05b0b37df316695c348ba772bed07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[*이 트랜잭션*](https://etherscan.io/tx/0x4b51009dbba5e17e6f956618ce24d323a1864e12c7cd2d7b46a44ecf56723f31)*은 Agenda #14를 실행한다. 트랜잭션의 이벤트를 확인하면 Upgraded 로그(DAOCommitteeProxy —> DAOCommitteeProxy2)가 기록되어 있다. 어젠다의 상세 내용과 트랜잭션은 **에서 확인할 수 있다.*

![](images/575c76263e55.png)

![](images/16eaa1439529.png)