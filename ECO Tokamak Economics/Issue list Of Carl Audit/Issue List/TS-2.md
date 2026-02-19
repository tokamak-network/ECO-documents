# TS-2 - Centralized execution of agenda

| ID | Type | Severity | Location |
| --- | --- | --- | --- |
| TS-2 | Centralization | Critical | contracts/dao/DAOCommittee_V1.sol#L509-L539 |

Description

executeAgenda 함수는 아젠다의 투표에 의해 실행 가능 여부가 결정되며, 해당 아젠다에 정의된 임의의 컨트

랙트를 실행합니다. 하지만 DEFAULT_ADMIN_ROLE을 가진 계정은 setAgendaStatus 함수를 실행해

서 투표 결과와 무관하게 특정 아젠다를 실행 가능한 상태로 변경할 수 있습니다.

특히 DEFAULT_ADMIN_ROLE을 가진

EOA 0xB4983DA083A5118C903910DB4f5a480B1D9f3687의 비밀키가 탈취당할 경우, 모든 자금

을 탈취당할 가능

Recommendation

아젠다의 투표를 통해서만 아젠다를 실행할 수 있도록 setAgendaStatus 함수를 제거합니다. 만약

setAgendaStatus 함수를 실행하는 아젠다가 필요하다면, setAgendaStatus 함수를 자기 자신

(DAOCommitteeProxy)만 실행할 수 있도록 변경합니다. (예: onlySelf)

상태 : 논의 필요 

Centralized Risk 안건 모아서 Kevin과 콜 잡기