**index**

### Storage Layout

> [*기존 Layer2Regsitry 컨트랙트*](https://github.com/tokamak-network/tokamak-dao-contracts/blob/main/deployed.mainnet.json#L4)*(*[*0x0b3E174A2170083e770D5d4Cf56774D221b7063e*](https://etherscan.io/address/0x0b3E174A2170083e770D5d4Cf56774D221b7063e)*)를 대체하여 *[*업그레이드 가능한 Layer2Registry 컨트랙트*](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md#simple-staking-v2-contracts)*(*[*0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b*](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b)*)를 새롭게 배포했다.*

*Layer2RegistryProxy 컨트랙트와 Layer2Registry 컨트랙트는 동일한 storage layout을 사용한다. 두 컨트랙트 모두 동일한 state variable을 선언하고 있다.*

![*Layer2RegistryProxy.sol*](images/b9d1a01863a3.png)

![*Layer2Registry.sol*](images/7513ccb6676d.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1c07fb8e-6f42-4793-975a-a5703a7df444/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTTRMI2T%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDK7ReAKZQw%2BgmNPRAN9iLRW%2Bw5EjuB24YmEvGqwxdKMAiB1YGOZObnZYcKYThyDlFH9ZtCf8HqEvQ9w%2BWM4hLBUyyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMsDM3YiNSieer1nDjKtwD9S8AgrgEZkBvY2W7PPkJdEFxjpxPXzcQtrZUGGaWJ9%2FJh1GkSmzFcebb22MKO79g55RucqKzk8H0NdhTgfk%2BhfhjH9RzeGwkOLle8GQJwU8EdBgC38UltctKie7iMMVna9Ukg7Go7R1l1PaByK0EjUYp%2BakKCyFRsBkOv9RxsZkiopBU6YHc68QyxHUgIHmHDhxnoyUxSaBZ3F4ltUmiQB7GflFSbNdPJIJHh%2F5EN8%2BTSIjXszsUeNtI%2BLjYMNSLUUBK%2B3YdoBy%2F1czgwo3auV2xBYxDDpT%2BHTMiAxl%2F2U4AEs4siQJ9pIRmokfF%2F%2BkKjDfZo1xdRKqD61wY%2B3bYfitYb6amZmCROAEEsfrCKdJ23o%2FsJbm3TAe2hM4b7FAurJCBD1%2FX9wGNwsp2lr%2FP7lr8ePcKGnlJGoGsfHwKs9RzFUHaOxSzqhmrTelrAAUEK9j79HBhQhTDNkCLsPq4TRiM5sewPFBpgWoiXdmk5STNEabaUzwWkaJGm5nsj%2FzysZHLFX8wYxXqR1eiswn8%2B%2BIxAmGMF%2BHvhYrL0zy5k7ziRd1vDMT%2BLBuBynomVv3KJrSit37DwboriKM7Rp2mDJv3Rw%2FE%2F3PaaUIXVPliJkOdjGDQGpd%2Bsisa6YcwsvHZzAY6pgHTliPbi7UgmUfDrMoYDXYi1F2WROE%2F2ljJcTpLB2%2FuyzlxP%2Fn1t0SErCWEJESphoHBQeGHCvL6XMTc4SLrMjfdYexuQb4eRJeNQYs3tNncjOnKzM8Q6WjeSCfVSap8kEVx6vjJWtP4KfIwqAnkWEkBtIEoqR9YciNRSBAlDcGujOa%2BA3NLJkXZfdNmsOylmesnKTT7btd%2Bd5B0gJXVGHrHKNpKg1%2FD&X-Amz-Signature=106799619fbf3fe9eae4e41216a4db4abfcebcd40c74be3c43564412a287adc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*이후 두 개의 트랜잭션을 호출하여 권한을 수정한다.*

![[*https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b*](https://etherscan.io/address/0x7846c2248a7b4de77e9c2bae7fbb93bfc286837b)](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/202e78c8-fada-4e12-8c46-56db836211e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTTRMI2T%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDK7ReAKZQw%2BgmNPRAN9iLRW%2Bw5EjuB24YmEvGqwxdKMAiB1YGOZObnZYcKYThyDlFH9ZtCf8HqEvQ9w%2BWM4hLBUyyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMsDM3YiNSieer1nDjKtwD9S8AgrgEZkBvY2W7PPkJdEFxjpxPXzcQtrZUGGaWJ9%2FJh1GkSmzFcebb22MKO79g55RucqKzk8H0NdhTgfk%2BhfhjH9RzeGwkOLle8GQJwU8EdBgC38UltctKie7iMMVna9Ukg7Go7R1l1PaByK0EjUYp%2BakKCyFRsBkOv9RxsZkiopBU6YHc68QyxHUgIHmHDhxnoyUxSaBZ3F4ltUmiQB7GflFSbNdPJIJHh%2F5EN8%2BTSIjXszsUeNtI%2BLjYMNSLUUBK%2B3YdoBy%2F1czgwo3auV2xBYxDDpT%2BHTMiAxl%2F2U4AEs4siQJ9pIRmokfF%2F%2BkKjDfZo1xdRKqD61wY%2B3bYfitYb6amZmCROAEEsfrCKdJ23o%2FsJbm3TAe2hM4b7FAurJCBD1%2FX9wGNwsp2lr%2FP7lr8ePcKGnlJGoGsfHwKs9RzFUHaOxSzqhmrTelrAAUEK9j79HBhQhTDNkCLsPq4TRiM5sewPFBpgWoiXdmk5STNEabaUzwWkaJGm5nsj%2FzysZHLFX8wYxXqR1eiswn8%2B%2BIxAmGMF%2BHvhYrL0zy5k7ziRd1vDMT%2BLBuBynomVv3KJrSit37DwboriKM7Rp2mDJv3Rw%2FE%2F3PaaUIXVPliJkOdjGDQGpd%2Bsisa6YcwsvHZzAY6pgHTliPbi7UgmUfDrMoYDXYi1F2WROE%2F2ljJcTpLB2%2FuyzlxP%2Fn1t0SErCWEJESphoHBQeGHCvL6XMTc4SLrMjfdYexuQb4eRJeNQYs3tNncjOnKzM8Q6WjeSCfVSap8kEVx6vjJWtP4KfIwqAnkWEkBtIEoqR9YciNRSBAlDcGujOa%2BA3NLJkXZfdNmsOylmesnKTT7btd%2Bd5B0gJXVGHrHKNpKg1%2FD&X-Amz-Signature=df2b5a9d311980005589fc5bc5fbe36f974759113b6741dc3a9decac38f2ff9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. ***AddMinter: ******`msg.sender`****** —> ***[***`DAOCommitteeProxy`***](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#code)
1. ***TransferAdmin: ******`msg.sender`****** —> ***[***`DAOCommitteeProxy`***](https://etherscan.io/address/0xDD9f0cCc044B0781289Ee318e5971b0139602C26#code)

*DAOCommitteeProxy 컨트랙트는 ADMIN_ROLE과 MINTER_ROLE 2개를 갖게 된다. OPERATOR_ROLE을 갖고 있는 어카운트는 존재하지 않는다.*