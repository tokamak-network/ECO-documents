**index**

### Storage Layout

> [*기존 Layer2Regsitry 컨트랙트*](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L4)*(*[*0x0b3E174A2170083e770D5d4Cf56774D221b7063e*](https://etherscan.io/address/0x0b3E174A2170083e770D5d4Cf56774D221b7063e)*)를 대체하여 *[*업그레이드 가능한 Layer2Registry 컨트랙트*](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md#simple-staking-v2-contracts)*(*[*0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b*](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b)*)를 새롭게 배포했다.*

*Layer2RegistryProxy 컨트랙트와 Layer2Registry 컨트랙트는 동일한 storage layout을 사용한다. 두 컨트랙트 모두 동일한 state variable을 선언하고 있다.*

![*Layer2RegistryProxy.sol*](images/4d013b35f9a2.png)

![*Layer2Registry.sol*](images/d62937c2eee7.png)

***stoage slots:***

1. *pauseProxy*
1. *proxyImplementation*
1. *aliveImplementation*
1. *selectorImplementation*
1. *_supportedInterfaces*
1. *_roles*

1. *layer2s*
1. *_numLyater2s*
1. *_layer2ByIndex*

> ***일반적으로 implementation 주소는 logic contract의 storage slot과 겹치지 않도록 특정 storage slot에 지정한다.**** 하지만 여기서는 implementation 주소가 logic 컨트랙트의 storage slot과 겹치는 위치에 존재한다. 이 때문에 proxy와 implementation이 동일한 storage layout을 사용하는 방식을 선택한 것으로 보인다.*

### Auth

```solidity
constructor() {
    _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
    _setRoleAdmin(MINTER_ROLE, DEFAULT_ADMIN_ROLE);
    _setRoleAdmin(OPERATOR_ROLE, DEFAULT_ADMIN_ROLE);
}
```

*컨트랙트 배포자인 msg.sender(0x796c1f28c777b8a5851d356ebbc9dec2ee51137f)는 ADMIN_ROLE을 갖는다. ADMIN_ROLE의 어카운트는 MINTER_ROLE과 OPERATOR_ROLE을 관리(**`_setRoleAdmin`**)할 수 있게 된다.*

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1c07fb8e-6f42-4793-975a-a5703a7df444/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU6VKQFJ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6Q%2F5Igk1W%2ByxCXrEH1kaWfeB3Up5%2FH8XPknC8dFE6cAiEArNlUfFMmGOamc8dM0fRjMqVBd2ZUZXl11AQ8IDew7Gwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNu5DBnz9KSDsJgq6yrcAxyNSTPXogTuFIXPPtk%2FuXHHRrArK0VbWRx%2Bon8KHHqUpjSgXHG0vZWUI%2FWyO9qQp4OT5fMQO85qeccseoFSXonyhewVLTGXK4Th6bPF61XuRPasj1Zulhiq9SQQSMCDDhrfsCHaX2Y4z5UkCGN2Cwk60Dk8DplF7z%2BIaSGw7TgONKPnc%2Fqsjpe7YxOxCgIns26TB6rQMasptUdrvSnmg7qee7%2BTwDXtyEEpM7hCjTgQSh0a0C9cGDSssd%2F50v8JfLDk2tHgiwshtxaka%2BqVrTrPK0sdoMfUp4CJojsjfU5LaB9seL%2Fuq7AHZ2VguSSLfrpZ%2Fz41pqTfYM3WiJ492TvJcgsx4MNSUhxS7rtoHPWwf%2Bk0EAxifXPKm1SgQCTwesUqUbdKI2s7FSjfQ7hoHbmpqyjfHCz91ETxHO9OlPYD7JjVbeAdDc5EMjs5RxUSfVEW6qkGkyn7Y91u87MdoWGrer8ORl0gwL50dFLu7gdTG43kw0DkD1a5lammncBvwe0MCg92xegEMupoYuxqVmpI7Cl6PxQOyIQPdVe1rtMb0ZiuT4a3Fl6BeWk4YEY1L9CQ0P3NYQSvZTIvfmbKCN9nnu8jQIkCB9DmfWBh6eJbQvIBX6ycxITvTu3dMMKY28wGOqUBlwNDfvj4ACxUR757Y87ypfZ2wEcVkENGfn1jUfZtnfzzQ5CFpa6bsrFLFbFSsyFLw45bAhQmt8pcELEwDUs9OyMpEPr68HWaTeBX1Y93js72JE5I69f0INKBoOz5AQi9%2Ft8e1Zwi7ZlmzzF5VwG00XpmcNCNd9AVuJWW1%2BEujR%2Fj9MMy7COPVdGeN2N0U2%2FgvT35vkX7aefyiA42FDZq9unG59a3&X-Amz-Signature=36d27ba0ecb0887e37d8bc7bab3af34396934afea8a6b6bfad172f65260d05bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*이후 두 개의 트랜잭션을 호출하여 권한을 수정한다.*

![[*https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b*](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b)](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/202e78c8-fada-4e12-8c46-56db836211e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU6VKQFJ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6Q%2F5Igk1W%2ByxCXrEH1kaWfeB3Up5%2FH8XPknC8dFE6cAiEArNlUfFMmGOamc8dM0fRjMqVBd2ZUZXl11AQ8IDew7Gwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNu5DBnz9KSDsJgq6yrcAxyNSTPXogTuFIXPPtk%2FuXHHRrArK0VbWRx%2Bon8KHHqUpjSgXHG0vZWUI%2FWyO9qQp4OT5fMQO85qeccseoFSXonyhewVLTGXK4Th6bPF61XuRPasj1Zulhiq9SQQSMCDDhrfsCHaX2Y4z5UkCGN2Cwk60Dk8DplF7z%2BIaSGw7TgONKPnc%2Fqsjpe7YxOxCgIns26TB6rQMasptUdrvSnmg7qee7%2BTwDXtyEEpM7hCjTgQSh0a0C9cGDSssd%2F50v8JfLDk2tHgiwshtxaka%2BqVrTrPK0sdoMfUp4CJojsjfU5LaB9seL%2Fuq7AHZ2VguSSLfrpZ%2Fz41pqTfYM3WiJ492TvJcgsx4MNSUhxS7rtoHPWwf%2Bk0EAxifXPKm1SgQCTwesUqUbdKI2s7FSjfQ7hoHbmpqyjfHCz91ETxHO9OlPYD7JjVbeAdDc5EMjs5RxUSfVEW6qkGkyn7Y91u87MdoWGrer8ORl0gwL50dFLu7gdTG43kw0DkD1a5lammncBvwe0MCg92xegEMupoYuxqVmpI7Cl6PxQOyIQPdVe1rtMb0ZiuT4a3Fl6BeWk4YEY1L9CQ0P3NYQSvZTIvfmbKCN9nnu8jQIkCB9DmfWBh6eJbQvIBX6ycxITvTu3dMMKY28wGOqUBlwNDfvj4ACxUR757Y87ypfZ2wEcVkENGfn1jUfZtnfzzQ5CFpa6bsrFLFbFSsyFLw45bAhQmt8pcELEwDUs9OyMpEPr68HWaTeBX1Y93js72JE5I69f0INKBoOz5AQi9%2Ft8e1Zwi7ZlmzzF5VwG00XpmcNCNd9AVuJWW1%2BEujR%2Fj9MMy7COPVdGeN2N0U2%2FgvT35vkX7aefyiA42FDZq9unG59a3&X-Amz-Signature=fa14a24af5bc2cdfdcb30b4cdabf033f8db68a59db5b054a5cece7be5aa1e5fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. ***AddMinter: ******`msg.sender`****** —> ***[***`DAOCommitteeProxy`***](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#code)
1. ***TransferAdmin: ******`msg.sender`****** —> ***[***`DAOCommitteeProxy`***](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#code)

*DAOCommitteeProxy 컨트랙트는 ADMIN_ROLE과 MINTER_ROLE 2개를 갖게 된다. OPERATOR_ROLE을 갖고 있는 어카운트는 존재하지 않는다.*