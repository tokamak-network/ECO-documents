# 1. Transparent

## 개념

투명 프록시 패턴은 프록시를 통해 로직 컨트랙트에 접근하는 방식이나. 업그레이드 관리 로직이 프록시 컨트랙트에 포함되어 있다. (관리자만이 컨트랙트를 업그레이드할 수 있도록 함)

로직 컨트랙트 주소를 업그레이드하는 함수는 프록시, 로직 두 컨트랙트에 존재하나 사용자 어카운트와 어드민 어카운트의 함수 호출 대상 컨트랙트를 다르게 함으로써 함수 충돌 이슈를 해소한다.

어드민 계정은 프록시 컨트랙트로, 사용자 계정은 로직 컨트랙트를 호출하도록 되어있다.

## 장점

업그레이드 프로세스가 단순하고 이해하기 쉬움.

사용자와 개발자 모두 같은 주소를 사용하여 컨트랙트와 상호작용.

## 단점

더 많은 가스 비용이 발생할 수 있음.

프록시와 구현체 간의 명확한 구분이 필요.

## 부적합한 상황

가스 비용 최소화가 중요한 프로젝트.

업그레이드 프로세스에 더 많은 유연성이 필요한 경우.

## 예시 코드

```
// Transparent Proxy 패턴 예시 코드

pragma solidity ^0.8.0;

contract LogicContract {
    uint256 public data;

    function setData(uint256 _data) external {
        data = _data;
    }
}

contract TransparentProxy {
    address public logicContract;
    address public owner;

    constructor(address _logicContract) {
        logicContract = _logicContract;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    function _beforeFallback() internal virtual override {
        require(msg.sender != _getAdmin(), "TransparentUpgradeableProxy: admin cannot fallback to proxy target");
        super._beforeFallback();
    }

    // fallback 함수를 사용하여 로직 컨트랙트의 함수를 호출
    fallback() external payable {
        address target = logicContract;
        assembly {
            let ptr := mload(0x40)
            calldatacopy(ptr, 0, calldatasize())
            let result := delegatecall(gas(), target, ptr, calldatasize(), 0, 0)
            let size := returndatasize()
            returndatacopy(ptr, 0, size)

            switch result
            case 0 { revert(ptr, size) }
            default { return(ptr, size) }
        }
    }

    // 로직 컨트랙트를 업그레이드하는 함수
    function upgradeLogic(address _newLogicContract) external onlyOwner {
        logicContract = _newLogicContract;
    }

}
```

# 2. 비콘(Beacon)

## 개념

비콘 프록시 패턴은 여러 프록시 컨트랙트가 하나의 비콘 컨트랙트를 참조하여 로직 컨트랙트의 주소를 얻는 방식. 비콘은 로직 컨트랙트의 주소를 저장하고, 모든 프록시는 이 비콘을 통해 업그레이드된 로직에 접근.

## 장점

여러 프록시 컨트랙트의 업그레이드를 중앙에서 관리할 수 있음.

업그레이드 시 가스 비용이 절약됨.

## 단점

비콘 자체의 보안과 관리가 중요함.

모든 프록시가 동시에 업그레이드되어야 함.

## 적합한 상황

동일한 로직을 사용하는 다수의 프록시 컨트랙트가 있는 경우.

중앙에서 여러 컨트랙트의 업그레이드를 효율적으로 관리하고자 할 때.

## 부적합한 상황

각 프록시 컨트랙트가 서로 다른 로직을 요구하는 경우.

업그레이드 과정에서 개별 컨트랙트의 특수한 처리가 필요한 경우.

## 예시 코드

```
// Beacon contract - 프록시와 원본 컨트랙트 간의 상호작용을 관리
contract Beacon {
    address public implementation;

    // 프록시의 로직 컨트랙트를 설정하는 함수
    function setImplementation(address _implementation) external {
        implementation = _implementation;
    }
}

// Logic contract - 실제 로직을 포함하는 스마트 컨트랙트
contract LogicContract {
    uint256 public data;

    // 상태를 변경하는 함수
    function setData(uint256 _data) external {
        data = _data;
    }

    // 상태를 조회하는 함수
    function getData() external view returns (uint256) {
        return data;
    }
}

// BeaconProxy contract - 사용자와 프록시 사이의 인터페이스 역할
contract BeaconProxy {
    address public beacon;

    constructor(address _beacon) {
        beacon = _beacon;
    }

    fallback() external {
        address _impl = Beacon(beacon).implementation();
        assembly {
            let ptr := mload(0x40)
            calldatacopy(ptr, 0, calldatasize())
            let success := delegatecall(gas(), _impl, ptr, calldatasize(), 0, 0)
            let retSz := returndatasize()
            returndatacopy(ptr, 0, retSz)
            switch success
            case 0 {
                revert(ptr, retSz)
            }
            default {
                return(ptr, retSz)
            }
        }
    }
}

```

# 3. UUPS(Universal Upgradeable Proxy Standard) (EIP-1822)

## 개념

UUPS 패턴은 업그레이드 로직을 구현 컨트랙트 자체에 포함시키는 방식으로 현재 프록시 패턴에서 가장 흔히 쓰이는 패턴이다. (구현 컨트랙트가 자신을 업그레이드할 수 있는 기능을 내장하고 있음) 이는 프록시 컨트랙트가 업그레이드 로직을 가지지 않게 하여, 구현 컨트랙트에서만 업그레이드를 관리. 프록시 컨트랙트는 단순히 구현 컨트랙트로의 요청을 전달하는 역할만 수행한다. 오픈제플린에서도 Transparent가 아닌 UUPS 패턴 사용을 권장하고 있다.

## 장점

구현 컨트랙트에서 업그레이드를 관리하기 때문에, 가스 비용이 절약됨.

업그레이드 로직과 구현 로직의 분리가 불필요.

## 단점

구현 컨트랙트에 추가적인 복잡성이 생김.

잘못된 업그레이드가 시스템 전체에 영향을 줄 수 있음.

## 예시코드

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// 필요한 OpenZeppelin 컨트랙트를 가져옵니다.
import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

// 구현 컨트랙트
contract MyContractV1 is Initializable, OwnableUpgradeable, UUPSUpgradeable {
    uint256 private value;

    // 초기화 함수
    function initialize(uint256 _value) public initializer {
        __Ownable_init();
        __UUPSUpgradeable_init();
        value = _value;
    }

    // 업그레이드 권한 체크
    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}

    // 비즈니스 로직 예시: 값 설정
    function setValue(uint256 _value) public {
        value = _value;
    }

    // 비즈니스 로직 예시: 값 조회
    function getValue() public view returns (uint256) {
        return value;
    }
}


```

# 4. Diamond (EIP-2535)

[Link](https://github.com/mudgen/diamond-3-hardhat/blob/main/contracts/Diamond.sol)

## 개념

다이아몬드 패턴은 여러 기능을 갖는 스마트 컨트랙트를 하나의 주소(다이아몬드)에 결합할 수 있도록 설계된 패턴. 이를 통해 스마트 컨트랙트의 기능을 개별적으로 추가, 제거, 업데이트할 수 있다.

### 다이아몬드 패턴의 주요 구성 요소

- 다이아몬드(Diamond): 사용자와 상호 작용하는 컨트랙트. 다이아몬드는 여러 facet의 기능을 사용할 수 있도록 프록시 역할을 한다.
- Facet: 특정 기능 또는 로직을 구현한 스마트 컨트랙트를 의미, 각 facet은 다이아몬드의 특정 기능을 담당.
- 다이아몬드 컷(DiamondCut): 다이아몬드에 facet을 추가, 제거, 또는 교체하는 과정을 관리하는 로직을 포함한 컨트랙트나 함수. 이를 통해 다이아몬드의 기능을 업그레이드하거나 수정할 수 있음.
- DiamondLoupe: 다이아몬드의 Facet과 함수에 대한 정보를 제공.
- Ownership: 다이아몬드의 소유권 관리를 담당.

### 기능을 등록하고 사용자가 사용할 수 있게 되는 과정

- Facet 등록: diamondCut 함수를 호출하여 새로운 facet(기능 구현 컨트랙트)을 다이아몬드에 추가하거나, 기존 facet의 기능을 수정하거나 제거. 이 함수 호출은 주로 다이아몬드의 소유자나 관리자에 의해 수행된다. 어떤 facet 주소에서 어떤 함수 선택자(function selectors)를 추가, 교체, 또는 제거할지는 FacetCut 구조체를 통해 이뤄진다.
- 함수 선택자 매핑: 다이아몬드 패턴에서는 함수 선택자(함수의 시그니처를 나타내는 4바이트 해시)를 기반으로 요청을 적절한 facet으로 라우팅합니다. diamondCut을 통해 facet이 추가되면, 다이아몬드는 내부적으로 함수 선택자와 해당 facet 주소 간의 매핑을 저장합니다. 이 매핑 정보는 함수 호출이 어떤 facet으로 전달되어야 하는지 결정하는 데 사용됩니다.
- 사용자 호출 처리: 사용자가 다이아몬드 컨트랙트의 함수를 호출하면, 다이아몬드 컨트랙트의 fallback 함수 또는 receive 함수가 실행. 호출된 함수 선택자를 확인하고, 내부적으로 저장된 매핑 정보를 사용하여 해당 함수 선택자에 매핑된 facet으로(컨트랙트 주소) 요청을 전달. delegatecall을 통해 facet의 코드가 다이아몬드 컨트랙트의 컨텍스트(상태 변수 등)에서 실행된다.
- 함수 실행: 요청이 적절한 facet으로 라우팅되면, facet 내의 해당 함수가 실행된다. 이때, 함수 실행 결과는 다이아몬드 컨트랙트의 상태에 영향을 미침. 함수 실행이 완료되면, 결과(반환 값 또는 이벤트)는 사용자에게 전달된다.

## 장점

- 스마트 컨트랙트의 확장성과 유연성 향상.
- 스마트 컨트랙트의 크기 제한 문제 해결.

## 단점

- 구현과 관리의 복잡성 증가.
- 보안 리스크 관리가 더 중요해짐.

## 예시 코드

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDiamondCut {

    enum FacetAction { Add, Replace, Remove }
    struct FacetCut {
        address facetAddress;
        FacetAction action;
        bytes4[] functionSelectors;
    }

    function diamondCut(FacetCut[] calldata _facetCuts) external;
}

contract DiamondStorage {

    struct FacetAddressAndSelector {
        mapping(bytes4 => address) selectorToFacet;
    }

    function diamondStorage() internal pure returns (FacetAddressAndSelector storage ds) {
        bytes32 position = keccak256("diamond.standard.diamond.storage");
        assembly {
            ds.slot := position
        }
    }
}

contract Diamond is IDiamondCut, DiamondStorage {

    function diamondCut(FacetCut[] calldata _facetCuts) external override {
        FacetAddressAndSelector storage ds = diamondStorage();
        for (uint256 i = 0; i < _facetCuts.length; i++) {
            FacetCut memory _facetCut = _facetCuts[i];
            address _facetAddress = _facetCut.facetAddress;
            for (uint256 j = 0; j < _facetCut.functionSelectors.length; j++) {
                bytes4 selector = _facetCut.functionSelectors[j];
                if (_facetCut.action == FacetAction.Add || _facetCut.action == FacetAction.Replace) {
                    ds.selectorToFacet[selector] = _facetAddress;
                } else if (_facetCut.action == FacetAction.Remove) {
                    ds.selectorToFacet[selector] = address(0);
                }
            }
        }
    }

    fallback() external payable {
        FacetAddressAndSelector storage ds = diamondStorage();
        address facet = ds.selectorToFacet[msg.sig];
        require(facet != address(0), "Function does not exist.");
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), facet, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}

```