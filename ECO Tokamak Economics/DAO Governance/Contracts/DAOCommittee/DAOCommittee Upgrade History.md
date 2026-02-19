**index**

## V1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/210c13c5-4995-4eac-b2a4-bc7e9e6eb009/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XRRYN43%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfn2PocquEQdhltx9l50qL5V8LGwdFh1XNKiKDIeC6hAiB0lOPz3EvazcChvAi8HZE0dkp2PO4Wohbt3O4vcPLNUyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMIsUY7ovIhSzhiNe3KtwDT8y8TfE9KSq%2FR0C9gXJSiiQvMzKWhGdiJO4C31Nh%2FxyPZpyxv%2B5NVioIZ%2BSnrbr%2F4d1Guoid6EaUnFfsiRukMbHL9VInr%2BFNTWZJWmTEtjrtMpiPoYaGFNdGQwPktcq%2FxDWDCDqTQxr1zz7h2FxwMlJ7AQzcmURPx5igtFGq4CIiYkI5A8x7CfYtr3vZ2AAvatV4Xc8fRCUbqGCiyxM6xFYOJG4J3tZli2Ng675nBfmYO%2FANiDkea9qafEsR%2FOTElRg2T0hbI3gsftBN9Eq7cJHx79rwSdqKiurSNyJPUqFaw8%2B3KPpYam7YGUPurApR8w3z5AijSE7F6Zid8Ojl5hEbQsTnX9YrbAiuzUh7IrHsSo8B9lZyi3Gf1hsLOZeqSsx1rWFkqjCSgAH%2FeypqjuhOcI6JFnW1%2FNtCAvJu5RYJSAzQVeys0FiluFBh03qMMI7gh%2B32HCFjYBmdIXpihp%2FtsN8kdnlj0x4HGatjFSuuhF1vOIpWwd2iUPvVBs4JbHJvDU9V60zT9U310p4BFD6jJafk5cGIlT21iNv1JnJzBPmAsgrhh0YFqVidjsLOLQpLjlgewoXNqMVBi28YRtI31kqnK%2FG7%2BlZa6XdC0btpdXPF1SbD6EBAUikw0PPZzAY6pgHNPAG0nIrYrrZV2v4%2FOCv%2BG4NCqDtyDMhrKbApdAi4Ef1e3AVUW%2BqeoxuYQhGkqO%2Bv2H0Xetv9wRjQC2OI5BcEc55NZ4%2FBDSp6uyo8kNWvWUyQAg31UlQ9DClf1x2EukzbJiP6MBUJRRAjQywr0ICWn4CMU9pxRHizYyOneLzO7G9ryjozbyfgP2V%2BzVLG%2BvSmUuwRYHmZS6zbmtNaGBf28JSvk%2F1S&X-Amz-Signature=d1dc25f33803e6f90cd6a819aa4e4a94a501e945b8f8af4118860d63a47d8ddf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

***DAOCommitteeProxy:**** *[*0xDD9f0cCc044B0781289Ee318e5971b0139602C26*](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26)

***DAOCommittee:**** *[*0xd1a3fddccd09cebcfcc7845ddba666b7b8e6d1fb*](https://etherscan.io/address/0xd1a3fddccd09cebcfcc7845ddba666b7b8e6d1fb#code)

> ***실제로 V1이 배포된 주소는 ****[https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L13-L14](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L13-L14)****에서 확인할 수 있다.***

## V2

### upgradeTo

*V1에서 V2로 업그레이드하려면 *[*Proxy 컨트랙트의 upgradeTo 함수*](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/contracts/dao/DAOCommitteeProxy.sol#L62-L69)*를 호출해야 한다.*

![[*https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26?mtd=0x3659cfe6~Upgrade To*](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26?mtd=0x3659cfe6~Upgrade%20To)](images/6f0a69fa79fe.png)

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

![](images/4f85ddf3055b.png)

1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManager`******  — ***[https://etherscan.io/tx/0xaaa7e6494b270a4a1a5a9eee36d207013e894c418836e1990dc71d4ae77d4eac](https://etherscan.io/tx/0xaaa7e6494b270a4a1a5a9eee36d207013e894c418836e1990dc71d4ae77d4eac)
1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManagerV1_1`****** — ***[*https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3*](https://etherscan.io/tx/0x69b48b552e49a4e081754b72867e2abfb793484d9d0ab4de3b052918381e88a3)** **
1. ***target: ******`SeigManagerProxy`******, logic: ******`SeigManagerV1_2`****** — ***[https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46](https://etherscan.io/tx/0xb474ee85f9629c69ae3af4222901210975979e846d65d8629cd080d9cb8e1f46)

### Execute Agenda

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0aa629f7-413f-4556-a5bf-90932763dabd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XRRYN43%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfn2PocquEQdhltx9l50qL5V8LGwdFh1XNKiKDIeC6hAiB0lOPz3EvazcChvAi8HZE0dkp2PO4Wohbt3O4vcPLNUyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMIsUY7ovIhSzhiNe3KtwDT8y8TfE9KSq%2FR0C9gXJSiiQvMzKWhGdiJO4C31Nh%2FxyPZpyxv%2B5NVioIZ%2BSnrbr%2F4d1Guoid6EaUnFfsiRukMbHL9VInr%2BFNTWZJWmTEtjrtMpiPoYaGFNdGQwPktcq%2FxDWDCDqTQxr1zz7h2FxwMlJ7AQzcmURPx5igtFGq4CIiYkI5A8x7CfYtr3vZ2AAvatV4Xc8fRCUbqGCiyxM6xFYOJG4J3tZli2Ng675nBfmYO%2FANiDkea9qafEsR%2FOTElRg2T0hbI3gsftBN9Eq7cJHx79rwSdqKiurSNyJPUqFaw8%2B3KPpYam7YGUPurApR8w3z5AijSE7F6Zid8Ojl5hEbQsTnX9YrbAiuzUh7IrHsSo8B9lZyi3Gf1hsLOZeqSsx1rWFkqjCSgAH%2FeypqjuhOcI6JFnW1%2FNtCAvJu5RYJSAzQVeys0FiluFBh03qMMI7gh%2B32HCFjYBmdIXpihp%2FtsN8kdnlj0x4HGatjFSuuhF1vOIpWwd2iUPvVBs4JbHJvDU9V60zT9U310p4BFD6jJafk5cGIlT21iNv1JnJzBPmAsgrhh0YFqVidjsLOLQpLjlgewoXNqMVBi28YRtI31kqnK%2FG7%2BlZa6XdC0btpdXPF1SbD6EBAUikw0PPZzAY6pgHNPAG0nIrYrrZV2v4%2FOCv%2BG4NCqDtyDMhrKbApdAi4Ef1e3AVUW%2BqeoxuYQhGkqO%2Bv2H0Xetv9wRjQC2OI5BcEc55NZ4%2FBDSp6uyo8kNWvWUyQAg31UlQ9DClf1x2EukzbJiP6MBUJRRAjQywr0ICWn4CMU9pxRHizYyOneLzO7G9ryjozbyfgP2V%2BzVLG%2BvSmUuwRYHmZS6zbmtNaGBf28JSvk%2F1S&X-Amz-Signature=0fcdb23626291d5afe9a409d0aabe520f964c64fe8474654c2141bead64fd31b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[*이 트랜잭션*](https://etherscan.io/tx/0x4b51009dbba5e17e6f956618ce24d323a1864e12c7cd2d7b46a44ecf56723f31)*은 Agenda #14를 실행한다. 트랜잭션의 이벤트를 확인하면 Upgraded 로그(DAOCommitteeProxy —> DAOCommitteeProxy2)가 기록되어 있다. 어젠다의 상세 내용과 트랜잭션은 **에서 확인할 수 있다.*

![](images/65911581a984.png)

![](images/b1e54e3eb12a.png)