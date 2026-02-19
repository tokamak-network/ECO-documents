**index**

Summary:

- 컨트랙트 업그레이드를 위해 Simple Delegate Proxy Pattern을 사용한다. 하지만 이 패턴은 **Storage collision**과 **Function selector collision** 문제를 일으킬 수 있다.
- Storage collision을 방지하기 위해 **ERC-1967**를 사용한다. Function selector collision을 하기 위해 **Transparent Proxy Pattern**을 사용한다.
- UUPS Proxy Pattern은 Transparent Proxy Pattern보다 가볍고 저렴하다. 또한 모든 외부 함수가 Implementation Contract에 존재하기 때문에 Function selector collision 모호성 문제가 발생하지 않는다. 따라서 **UUPS Proxy Pattern** 사용을 권장한다.

## Proxy

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/26c2a8b1-0f63-484c-ad11-a688f5842ccc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=7e477b56fb300adedc4f6442a0257498a1a067629178f7727dbbdbef03ed54bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Proxy Contract: 데이터 저장을 포함하는 컨트랙트이다.
- Implementation Contract: 비즈니스 로직을 포함하는 컨트랙트이다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dc5bb65c-bc2b-460f-8982-584f9d18b32a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=12059927afaeaa5f97a6d930f6426d8a01c09d442acbed43dd817159609c715b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

사용자는 Proxy 컨트랙트와 직접 상호작용한다. Proxy 컨트랙트는 Implementation 컨트랙트로 delegatecall을 통해 로직을 실행하며, 이 로직은 Proxy 컨트랙트의 storage를 사용한다.

버그를 발견하거나 로직을 업그레이드하려면 새로운 Implementation 컨트랙트를 배포한다. 그런 다음 upgradeTo(address newImplementation) 함수를 호출해 새로운 implementation 컨트랙트를 바라보도록 업데이트한다.

## **The problem with the Simple Delegate Proxy Pattern**

Simple Delegate Proxy Pattern에서는 두 가지 주요 문제가 존재한다:

- Storage collision
- Function selector collision

### **Storage collision**

Solidity 코드에서 변수 선언 순서는 컨트랙트의 storage layout을 결정한다.

```solidity
*//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;

contract ProxyStorage {
    bool public pauseProxy;
    mapping(uint256 => address) public proxyImplementation;
    mapping(address => bool) public aliveImplementation;
    mapping(bytes4 => address) public selectorImplementation;
}
*
```

![](images/a65dfaad743b.png)

아래 예시에서 Contract B를 새로운 Implementation 컨트랙트로 업그레이드하면, 변수 a에 접근하려 해도 실제로는 변수 b와 상호 작용하게 된다. 따라서 새로운 Implementation 컨트랙트는 저장 변수의 순서를 기존과 동일하게 유지해야 한다.

```solidity
*contract A {
	...
	uint256 a; 
	uint256 b;
}

contract B {
	...
	uint256 b;
	uint256 a;
	uint256 c;
}*
```

![](images/aec0264cbb25.png)

### Function selector collision

컨트랙트의 함수는 function selector에 의해 호출될 함수가 결정된다. 그런데 function selector는 함수명과 파라미터가 다르더라도 동일할 수 있다. 이 경우 Proxy Contract와 Implementation 컨트랙트가 동일한 function selector를 갖게 된다. 사용자가 함수를 호출할 때 Proxy 컨트랙트의 함수를 호출하려는 것인지, Implementation 컨트랙트의 함수를 호출하려는 것인지 모호성이 발생한다.

```solidity
contract AttackerProxy {
	// proxy code here...

**	// 0x42966c68
	function collate_propagate_storage(bytes16) external {
        implementation.delegatecall(abi.encodeWithSignature(
            "transfer(address,uint256)", proxyOwner, 1000
        ));
    }
**
	// ...
}

contract Implementation {
	// implementation code here...

**	// 0x42966c68
	function burn(uint256 value) public virtual {
        _burn(_msgSender(), value);
	}**

	function transfer(address to, uint256 value) public virtual returns (bool) {
        address owner = _msgSender();
        _transfer(owner, to, value);
        return true;
	}
	// ...
}
```

## Proxy Pattern

Simple Delegate Proxy Pattern에는 Storage collision(기존 상태 변수가 보존되지 않을 수 있음)과 Function selector collision(어느 컨트랙트의 함수를 호출해야 하는지 모호해질 수 있음)이라는 두 가지 주요 문제가 있으며, 이러한 문제를 해결할 수 있는 패턴이 존재한다.

### [ERC-1967: Proxy Storage Slots](https://eips.ethereum.org/EIPS/eip-1967)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e18f6171-50dc-458e-b2f5-ca6b49acf0cb/CleanShot_2025-11-29_at_16.17.12.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=c939ede8a59331d71edcaffa96328fc6866f8997759384aed36d0c3239c9f250&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

delegatecall 구조에서 Storage는 Proxy 컨트랙트의 storage를 사용하고 Logic은 implementation 컨트랙트의 코드를 실행한다.

```solidity
contract Proxy {
    address public implementation; // slot 0
}
```

```solidity
contract Logic {
    uint256 public value; // slot 0
}
```

delegatecall을 실행하면 Logic 코드가 Proxy의 storage를 읽게 된다. 예를 들어 Logic.setValue(100)을 호출하면 Proxy의 slot 0 값이 100으로 변경되어, Proxy의 implementation 주소가 100으로 잘못 지정되는 문제가 발생한다.

이러한 storage collision 문제를 방지하기 위해 Proxy 컨트랙트는 logic, beacon, admin 주소를 특정 storage slot에 저장한다:

- [implementation](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Utils.sol#L21): Storage slot `0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc` (obtained as `bytes32(uint256(keccak256('eip1967.proxy.implementation')) - 1)`).

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/69d700a2-c458-4095-949d-81535e249507/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=ddd20e5f378d0ed7b184725be5a4866a020fb7d315c8e4feb30b025cd0858a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [beacon](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Utils.sol#L121): Storage slot `0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50` (obtained as `bytes32(uint256(keccak256('eip1967.proxy.beacon')) - 1)`).
- [admin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Utils.sol#L83): Storage slot `0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50` (obtained as `bytes32(uint256(keccak256('eip1967.proxy.beacon')) - 1)`).

### Transparent Proxy Pattern

Transparent Proxy Pattern에서는 [TransparentUpgradeableProxy 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#L96)를 Proxy 컨트랙트로 사용한다.** **해당 Proxy 컨트랙트는 [msg.sender가 admin인지 non-admin인지 확인](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#L96)하고 이에 따라 다른 실행 경로를 제공한다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2e078e46-7fc5-4f7a-81c9-6fee5525f3d9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=58466eb70045d72a0cc4cb1e1adf7e8842f341763bf7b3f73aeb14cad71e0db1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

admin은 ([ProxyAdmin 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/ProxyAdmin.sol)를 경유하여) [Proxy 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/TransparentUpgradeableProxy.sol)의 함수만 호출할 수 있고, non-admin은 Implementation 컨트랙트의 함수만 호출할 수 있다. 이를 통해 [Function selector collision으로 인해 발생할 수 있는 모호성](/2bed96a400a380eba475cc6ccf86e218#2bed96a400a3810a8067efcef15ef520)을 제거했다.

**Transparent Proxy downsides:**

- Proxy 컨트랙트 모든 함수 호출마다 [admin 주소를 SLOAD](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#L96)하는 가스 비용이 발생한다.
- Proxy 컨트랙트에 [업그레이드 관련 로직](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#L114-L117)이 포함되어 있어 배포 시 가스 비용이 증가한다.

### UUPS(Universal Upgrade Proxy Standard) Proxy Pattern

Transparent Proxy Pattern은 업그레이드 로직을 Proxy 컨트랙트에 포함하지만, UUPS Proxy Pattern은 해당 로직을 Implementation 컨트랙트에 포함한다. 이를 통해 Transparent Proxy의 단점을 해결한다:

- [업그레이드 로직이 Implementation 컨트랙트에 포함](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/utils/UUPSUpgradeable.sol#L88-L91)되어 있어, Proxy 컨트랙트가 더욱 경량화되고, 배포 시 가스비가 절감된다.
- UUPS Proxy Pattern에서 사용하는 [ERC1967Proxy 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Proxy.sol)는 admin 주소를 매번 SLOAD하지 않아 가스 오버헤드가 제거된다.

> UUPS Proxy Pattern은 [ERC1967Proxy 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Proxy.sol)를 Proxy 컨트랙트로 사용한다. 해당 컨트랙트에는 external function이 존재하지 않기 때문에 [Function selector collision 문제](/2bed96a400a380eba475cc6ccf86e218#2bed96a400a381d9a205c5d9e5a826f0)가 발생하지 않는다. Implementation Contract 내에서 selector collision이 발생하면 컴파일러가 이를 감지한다.
> ![](images/107b2a2ec8a5.png)

> *OpenZeppelin은 UUPS Proxy Pattern 사용을 권장한다.*
> ![[*https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-vs-uups-proxies*](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-vs-uups-proxies)](images/2815ee9af4e0.png)

## UUPS Proxy Pattern

UUPS Proxy Pattern에서는 Proxy 컨트랙트로 [ERC1967Proxy 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Proxy.sol)를 사용하고, Implementation 컨트랙트는 [Initializable 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/utils/Initializable.sol)와 [UUPSUpgradeable 컨트랙트](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/utils/UUPSUpgradeable.sol)를 상속한다.

### [ERC1967Proxy](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/ERC1967/ERC1967Proxy.sol)

Proxy 기능(implementation 주소 관리, fallback forwarding)만 제공하며, external 함수는 존재하지 않는다.

### [UUPSUpgradeable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/8631702babdb0a3890c470e0c9aebf9bc28c3637/contracts/proxy/utils/UUPSUpgradeable.sol)

```solidity
function proxiableUUID() external view notDelegated returns (bytes32) {
    return ERC1967Utils.IMPLEMENTATION_SLOT;
}
```

UUPS Proxy Pattern에서 Implementation 컨트랙트는 UUPSUpgradeable 컨트랙트를 상속해야 한다. UUPSUpgradeable은 proxiableUUID 함수를 포함하며, 업그레이드 시 이 함수를 호출하여 새로운 Implementation 컨트랙트가 UUPS Proxy 패턴을 따르는지 확인한다.

```javascript
function upgradeToAndCall(address newImplementation, bytes memory data) public payable virtual onlyProxy {
    _authorizeUpgrade(newImplementation);
    _upgradeToAndCallUUPS(newImplementation, data);
}
```

컨트랙트 업그레이드 로직이 로직 컨트랙트에 있다. 그러므로 로직 컨트랙트는 _authorizeUpgrade 함수를 오버라이딩해서 auth 관리를 별도로 처리해야 한다.

```solidity
function _upgradeToAndCallUUPS(address newImplementation, bytes memory data) private {
    try IERC1822Proxiable(newImplementation).proxiableUUID() returns (bytes32 slot) {
        if (slot != ERC1967Utils.IMPLEMENTATION_SLOT) {
            revert UUPSUnsupportedProxiableUUID(slot);
        }
        ERC1967Utils.upgradeToAndCall(newImplementation, data);
    } catch {
        // The implementation is not UUPS
        revert ERC1967Utils.ERC1967InvalidImplementation(newImplementation);
    }
}
```

## Beacon Proxy Patter

Beacon Proxy Pattern은 여러 Proxy 컨트랙트가 동일한 Implementation 컨트랙트를 참조하도록 한다. 이를 통해 모든 Proxy 컨트랙트를 한 번에 업그레이드할 수 있다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fdbd0164-3122-4194-ab69-dadd2bb0c552/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=8032d74df15667ce15570ca9c91b0479d35365b99fc485877b7bbf6fc995dc98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> *Beacon Proxy 컨트랙트는 Beacon의 storage를 매번 읽는 구조라 *[*EIP-2930*](/2bed96a400a380eba475cc6ccf86e218)* access list를 활용하면 cold access 가스를 줄일 수 있다.*

> *여러 개의 Beacon Proxy를 수동으로 하나씩 배포하는 것은 번거롭다. 따라서 Factory 컨트랙트를 활용하여 새로운 Proxy 컨트랙트를 배포하고, 생성자에서 Beacon 주소를 설정하는 구조를 사용한다.*

## Diamond Proxy Pattern

> *EVM 환경에서는 컨트랙트 bytecode 크기가 24KB로 제한된다. Implementation 컨트랙트의 bytecode 크기가 이 제한을 초과할 때 해당 패턴을 사용한다.*

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/4784f6f1-b6a0-4660-9084-8ada7f937913/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=f2316983695cd2319820789e91e341d10587a56955af0a612f3e5d6fc82fd982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Diamond Proxy Pattern은 Transparent Proxy Pattern 및 UUPS Proxy Pattern과 달리 여러 Implementation 컨트랙트를 동시에 사용한다. Proxy 컨트랙트는 function selector를 기반으로 어떤 Implementation 컨트랙트에 delegatecall을 수행할지 결정한다.

![[*https://etherscan.io/address/0x312be6a98441f9f6e3f6246b13ca19701e0ac3b9#multipleProxyContract*](https://etherscan.io/address/0x312be6a98441f9f6e3f6246b13ca19701e0ac3b9#multipleProxyContract)](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7f561cb1-617a-4ab2-a82b-ea5bae7d4d65/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466236Z4N7L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbzMB3nvmY2iedHcVzpclI%2BXS6YRoE9%2B27Oy9Qgd9fjAiBTqo6K%2FDNL3yDueXaBD2Q7NG9cmEp%2FX%2Bk%2BglwInMNx%2BCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMh9i%2B4sHpNSYNpr4UKtwD50Xz0lAbTq6BOdQJSPd04bjo10KZywtoBX4ANVe1kJ%2FMvDpoEwDsIxrl%2BvU7xNErR5mLMu7%2Fte2TGJyNmEYcNHiNZcK6Em%2BEpEEtBXJOcykpz881T%2BV2Tb%2Fk9E%2B6%2BI5j0z4b1ma%2FmQ55WtSsghqP7HLLqnd7MuFUHSgeRjJoAEQkZbCdysbDGoyxhixEWyBZky217P89l2l5pwrro2lKAPiTiZ1yYE6IhC44zUiKWqkefW2O0SlOeyTmEA8mJDLAXx24C2jT5AFn17tV2xxbb6HPP2GvI4sAONfk%2B2uyLzBfT5i%2FCQX5X485BXWQXGbYNoJxIuEsS0rzvEhkOToDyEpERaHawy6vVc6cWB%2FKmb1EdFvtl7eo2jNc%2F4kPkMwofUY4Tao79n1ZAqDVxNSfXSU7s0AVAo5YI331jPwPhHdBm53ARqohklUgJf7gs19Pw5cUAWVLCQMiiJCozWJMzjXpFvkldJtnf8ble17BNd779uyIzxmzUQGLlrSXDx2gvzZ2bsc%2FnO8KPMQblVn8fqcxSxQC%2FXQGMPfIVkO1s1UEd5OB%2FhQDHCbJo22A5uUqblpkA5l51WOfIqXYdLyYdnf8X%2B1ZQsf6OWiMJuBcdoNjKDKTIMCST0kYJ94ww%2FDZzAY6pgGOa%2Bp3NKa0i6y6ANrfAEAoNYDYsIu%2BnutR2jhh%2FJmWOsnmvSuENmFNljhIQpTtc8ZCmGjrzNthQ6joIeJhOtYAGT7chGAEADZQrTHn7pCowq9WE6mTvgqxFBQPfTCFVu2TeRnqU%2BZeVAEmH%2BdZlCfEH0t%2FmmeJiI6v08Sd2qj29gfcbOmoO6Ne9lRfYJej8LNnq76v1fxHdF45fRiP3%2Bun6dP3jFvm&X-Amz-Signature=681389bdf7f7e2457e9ccbdd35e1765d2f8377e63e98caa00249589eadfe62e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

***Reference:***

- [*https://eips.ethereum.org/EIPS/eip-1967*](https://eips.ethereum.org/EIPS/eip-1967)
- [*https://www.cyfrin.io/blog/upgradeable-proxy-smart-contract-pattern*](https://www.cyfrin.io/blog/upgradeable-proxy-smart-contract-pattern)
- [*https://rareskills.io/post/beacon-proxy*](https://rareskills.io/post/beacon-proxy)
- [*https://rareskills.io/post/diamond-prox*](https://rareskills.io/post/diamond-proxy)[y](https://rareskills.io/post/diamond-proxy)