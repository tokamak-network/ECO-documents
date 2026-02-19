심플 스테이킹 V2는 Layer2를 운영하는 Layer2Candidate의 시퀀서에게 톤 시뇨리지를 발급하는 이코노미를 설계했다. 

그러나 Layer2를 실제로 운영하지 않는 또는 불합리하게 시뇨리지를 할당받는 행위 등을 발견할 즉시 톤 시뇨리지 발급을 중지할 수 있는 정책 및 프로세스를 정리해야 한다. 

Layer2Candidate 등록은 L2Registry에  Registrant 권한을 보유한 계정만 등록을 할 수 있다.  

그렇다면 이미 등록되어 시뇨리지를 발급받고 있는  Layer2Candidate 에 시뇨리지 발급 제한을 줄 수 있는 요건이 무엇이 되는지 알아보자. 

### Layer2Candidate 시퀀스에 시뇨리지 발급 제한 요건 

> [!tip]
> 💡 Layer2Candidate 시뇨리지 발급이 제한되는 경우를 모두 열거하자.

1. Layer2 가 일정기간동안 운영되지 않고 방치되고 있다고 판단될때 (ex. 롤업이 일주일이상 실행되지 않을때) 
1. Layer2 에 치명적인 exploit  되었을때 
1. 

### Layer2Candidate 시퀀서 대상 시뇨리지 발급 중지/실행  권한 : onlySeigniorageCommittee

> [!tip]
> 💡 Layer2Candidate 시뇨리지 발급 제한 함수의 실행권한을 누구에게 줄것인가?  이 권한을 가진 주소를 SeigniorageCommittee 로 정의한다. 

Layer2Candidate 시퀀서에게 시뇨리지 발급중지 함수를 실행하는 SeigniorageCommittee 권한은 누구에게 있는 것인가? 

 L2Registry 컨트랙에  SeigniorageCommittee 계정을 위한 스토리지를 추가하고, SeigniorageCommittee 계정 주소 변경은 L2Registry 컨트랙의 권한은 현재 오너 , 매니저, 등록으로 3개의 권한으로 구분되어 있는데,  SeigniorageCommittee 계정 (스토리지) 을 추가 해야 한다. 

** SeigniorageCommittee 계정 **→ 멀티시그 컨트랙 또는 다오 가 될수도 있다. 추후 결정  

[[L2Registry]] 

### Layer2Candidate 시퀀서 대상 시뇨리지 발급 중지 방법 

1. L2Regitry  의 systemConfigType 스토리지에 해당 SystemConfig 주소에 매핑된 정보를  **type(uint8).max ** (255) 로 수정한다. 
```javascript
/// systemConfig - type (0:empty, 1: optimism legacy, 2: optimism bedrock native TON)
    mapping (address => uint8) public systemConfigType;

```

  1. 이는 SystemConfig 컨트랙이 optimism legacy 나 optimism bedrock(nativeTON) 타입이 아니라는 것을 의미한다. 
  1. 현재 심플스테이킹 V2의 Layer2 지원 타입은 optimism legacy 와 optimism bedrock(nativeTON) 만 지원하고 있다. 
  1. 현재 changeType 은 Registrant 권한을 가진 계정이 가능하다. Registrant 권한은 등록을 할 수 있는 권한이다. reejct 된 것은 Registrant 권한으로도 수정할 수 없도록 해야 한다. 

```javascript
function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant {
        require(systemConfigType[_systemConfig] != 0, "unregistered");
       ** require(systemConfigType[_systemConfig] != 255, paused");**
        require(systemConfigType[_systemConfig] != _type, "same type");
        systemConfigType[_systemConfig] = _type;

        emit ChangedType(_systemConfig, _type);
    }

```
1. Layer2Manager에 
  1. issueStatusLayer2 에 reject 상태값 **type(uint8).max ** (255) 이 추가되고, 상태값을 reject로 수정해야 한다. 

```javascript
 /// systemConfig - stateIssue ( 0: none , 1: registered, 2: paused, 255: reject)
    mapping (address => uint8) public issueStatusLayer2;
```

b. 레이어2 컨트랙 주소 조회 : layer2CandidateOfOperator[operatorOfSystemConfig[systemConfig address]] 
1. SystemConfig 주소에 매핑된 정보를 0으로 수정할때,
  1. SeigManager 의 스토리지에서 Layer2와 관련이 있는 스토리지 값을 조정해야 한다. 
    1. totalLayer2TVL  : 전체 레이어2 TVL의 양을 나타내고 있으므로, 해당 레이어가 반영하고 있는 layer2 TON TVL 양을 빼야 한다. 
    1. layer2StartBlock :   이것은 전체 레이어2의 시뇨리지 발행과 관련된 것으로서, 변경사항 없다.  
    1. l2RewardPerUint :  레이어2 톤 한개당 리워드 할당량. 이것은 전체를 대상으로 이미 계산된 값이므로, 변경사항이 없다.  
    1. layer2RewardInfo : 해당 레이어에 대한 구조체 정보, 해당 레이어의 layer2Tvl은 0으로 설정되어야 한다. initialDebt 도 0으로 설정하는게 맞는듯.
```javascript
struct Layer2Reward {
        uint256 layer2Tvl;
        uint256 initialDebt;
    }
```
1. 시뇨리지 발급 제한 함수의 생성 
  1. L2Regitry 에 함수가 존재하고, L2Regitry에 실행하면  SeigManager 컨트랙의 레이어2의 tvl 초기화 함수를 실행하도록 하자.  
    1. 함수1:  L2Registry.rejectLayer2 (address systemConfig)  onlySeigniorageCommittee
    1. 함수2:  Layer2Manager.rejectLayer2 (address systemConfig)  onlyL2Registry 
    1. 함수3: SeigManager.rejectLayer2(address layer2)   onlyLayer2Manager
    1. reject 된 경우는 Registrant 권한에 의해서, 수정이 안되도록 해야 한다. 
1. 

### Layer2Candidate 시퀀서 대상 시뇨리지 발급 재실행(중지취소) 방법 

Layer2Candidate의 시퀀서에 시뇨리지 발급 중지 

# Dev 

Issue : 

[https://github.com/tokamak-network/ton-staking-v2/issues/3](https://github.com/tokamak-network/ton-staking-v2/issues/3)

# Deploy on sepolia 

- npx hardhat deploy —network sepolia 
- modify seigManagerV1_3  [link ](/166c00220d954ec89d7e90c392a64b0c#98da127968bb47a1baa4615b3e36ef34)