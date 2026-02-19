##  Schedule for the integration of Thanos L2 and ton-staking-v2 

## Related to patch the bug 

- 코드 패치한 Repo : [https://github.com/tokamak-network/ton-staking-v2/tree/patch-candidate-add-on-proxy](https://github.com/tokamak-network/ton-staking-v2/tree/patch-candidate-add-on-proxy) → v2.5-audit-merge 로 머지한 후, → v2.5-audit-agenda에 머지함. 
- **Agenda Repo : **[**https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda**](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)

[Issue 304](https://github.com/tokamak-network/ton-staking-v2/issues/304#issuecomment-2826891830): **Optimizing storage variables in CandidateAddOn / OperatorManager contracts #304**

- Description of Bug 
CandidateAddOnProxy 와 CandidateAddOn (로직)의 메모리 구성이 달라 스토리지를 정상적으로 가져올 수 없는 현상
- Impact 
 등록한 CandodateAddOn (TRH-SDK로 등록한 Candidate)이 다오 멤버가 될 수 없으며, 아래 함수 호출 불가함. 
- 수정 방안 
- [x] CandidateAddOnProxy 의 메모리를 CandidateAddOn (로직)의 메모리와 같게 한다. 
- (Harvey)기본테스트: 위사항 확인되도록 테스트 파일 작성 및 테스트 
- [x] current. 현재 상태 테스트 → 문제 있음 확인해야 한다. 
- [x] patch. 패치 적용 → 문제없음 확인햐여 한다.  
- Sepolia 적용 방법 
- [x] (작업1) 기존에 배포된 Thanos Sepolia V2를 시뇨리지 중지 puase 시킨다.  
- [x] (작업2) CandidateAddOnFactory 코드 수정→ CandidateAddOnFactory 컨트랙 재배포  
- [x] (작업3) CandidateAddOnFactoryProxy 로직 업그레이드 아젠다 등록 
- [x] (Harvey) (작업4)  Trh-sdk로 L2 생성 
- [x] (Harvey) (작업5) L2 등록하는 다오 아젠다 통과 및 실행 
- [x] (Harvey) (작업6) L2를 CandidateAddOn 등록 
- [x] (Harvey) (작업7)  L2의 다오 멤버 관련 모든 기능 테스트 

 
- 메인넷 적용 방법
 - TRH 와 통합을 할 예정이기 때문에 아젠다에 TRH의 검증컨트랙을 검증자로 등록하는 안건도 추가해야함. → 이것은 일정이 늦어지므로, 이 안건에서는 포함하지 않습니다.

 - **Repo :  **[https://github.com/tokamak-network/ton-staking-v2/tree/deploy-candidateAndDAO](https://github.com/tokamak-network/ton-staking-v2/tree/deploy-candidateAndDAO)

- [x] (작업1) CandidateAddOnFactory 코드 수정→ CandidateAddOnFactory 컨트랙 재배포 
- [x] (작업2) 다오 아젠다 등록전 포크해서, 아젠다 등록 및 CandidateAddOn 등록 및 다오 멤버 기능 테스트 
- [ ] (작업3)  다오 아젠다 등록 
- [ ] (작업4) 다오 아젠다 통과 및 실행 
- [ ] (작업5) 포크해서,  CandidateAddOn 등록 및 다오 멤버 기능 테스트 

 