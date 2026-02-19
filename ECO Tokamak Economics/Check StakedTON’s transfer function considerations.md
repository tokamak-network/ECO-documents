같은 레이어안에서 소유권 이전하는 기능에 대한 고찰

- seigManager 에서 같은 레이어 내에서 transfer 구현가능 ( 코인에이지의 민터가 seigManager이기 때문에) 
  - transfer 함수 안에서 mint와 burnFrom 기능 가능 
- 레이어의 operator는 다른 계정에게 transfer 할 수 없음. 
  - EOA가 다른 EOA 에게 transfer 가능함. ( 주소0 과 주소1로는 불가능함. )
  - 등록되어 인증된 컨트랙계정이 EOA 계정으로 transfer 가능함. 
  - EOA 계정은 등록되어 인증된 컨트랙 계정에게만 transfer 가능함. ? 
    - 사전에 정의된 콜백 인터페이스 호출 가능 하도록 해야 하나.. 
    - transfer 가능한 컨트랙 관리 : 등록 인터페이스를 만들어야 함.
- DAOCandidate 또는 Layer2Candidate 모두 사용가능한 기능인가? 특정 레이어만 사용가능한 기능인가? 
  - 특정 레이어만 사용가능해야 한다면, 가능한 레이어 관리해야함. 

 