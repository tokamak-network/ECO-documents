## Hammer’s work

- 5주차 (25.04.25~25.05.01) 
  - [https://github.com/tokamak-network/update-dev-env/wiki/Week-4](https://github.com/tokamak-network/update-dev-env/wiki/Week-4)
  - L1Verification Contract Audit 작업 진행
  - **`OperatorManagerV1_1`**** 와 ****`CandidateAddOnFactory`****  **Contract 쪽 작업 진행
- 6주차 (25.05.02~25.05.08) & 7주차 (25.05.09~25.05.15)
  - [https://github.com/tokamak-network/update-dev-env/wiki/Week-5-&-6](https://github.com/tokamak-network/update-dev-env/wiki/Week-5-&-6)
  - L1Verification Contract Audit 작업 진행
  - CandidateAddOn Contracts 테스트 진행
- 8주차 (25.05.16~25.05.22)
  - [https://github.com/tokamak-network/update-dev-env/wiki/Week-7](https://github.com/tokamak-network/update-dev-env/wiki/Week-7)
  - SeigManager 테스트 케이스를 작성, 현재 모의 계약을 개발하고 단위 테스트 시나리오를 설계하여 최대한 유연하게 세뇨리지 분배 로직을 테스트 중
  - SeigManager 로직 중 일부는 테스트되었으며, updateSeigniorage 메서드에 대한 단위 테스트도 진행 중
- 9주차 (25.05.23~25.05.29)
  - [https://github.com/tokamak-network/update-dev-env/wiki/Week-8](https://github.com/tokamak-network/update-dev-env/wiki/Week-8)
  - SeigManager의 세뇨리지 분배 로직 테스트가 거의 완료 (현재 Layer2와 커미션에 대한 세뇨리지 분배 로직만 남았습니다.)
  - 타입체인을 활용한 테스트 케이스 개발 개선
  - 테스트 케이스 개발 전략 변경

### My personal opinion(Harvey) on contract extension

- L1Verification Contract Audit을 진행해주시고 Hammer님이 컴퓨터 보안학과 출신이라 Audit했을때 공격 가능한 케이스를 잘봐주십니다.
- 초기 목적이였던 테스트코드 개선 작업도 많이 진행해주셨습니다. 테이트 케이스 개발 개선 및 전략 변경을 통해서 더 좋은 테스트 케이스를 만들려고 노력하십니다.
- 연장을 해야하나? 
  - 연장을 해야한다고 생각합니다. 저희 토카막 네트워크의 다른 프로젝트에서 진행하는 Audit도 진행해주시기 때문에 따로 외부 Audit을 신청하여서 진행하는 것 보다 internal Audit에서 부터 같이 참여하는 것도 좋고 비용적으로도 외부 Audit보다 저렴하게 진행할 수 있는 것 같습니다. 그리고 개인적으로 얘기했을때 토카막의 다른 프로젝트에도 관심이 많았습니다. 다른 프로젝트에도 기여를 할 수 있을거라 생각됩니다. (DRB 프로젝트가 6월말이나 7월초에 internal Audit을 진행할려고 준비중이라고 하는데 이때도 많은 도움을 주실 것 같습니다.)