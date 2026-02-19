## Hammer’s work

- 6월 1주차 (25.05.30~25.06.05) 
  - TON Staking V2 테스트 케이스 작성
  - DRB 컨트랙트(Commit-Reveal2) 리뷰 진행
- 6월 2주차 (25.06.06~25.06.12) 
  - DAOCommittee_V2 Internal Audit 진행
    - There is no problem logically, so I left feedback on gas cost optimization.
  - L1 Verification 코드 리뷰 진행 중
- 6월 3주차 (25.06.13~25.06.19) & 6월 4주차 (25.06.20~25.06.26)
  - L1 Verification 코드 리뷰 완료 ([link](https://github.com/tokamak-network/tokamak-thanos/pull/359))
  - DRB 컨트랙트(Commit-Reveal2) 리뷰
    - 1차 리뷰 완료 후 진행사항 미팅 진행
      - 이슈 리포팅([link](https://github.com/tokamak-network/Commit-Reveal2/issues?q=is%3Aissue))
    - 어셈블리로 짜여진 코드를 Solidity로 옮겨서 리뷰 진행할 예정
      - 전체 코드의 80% 정도 포팅 및 리뷰 진행 중
  - TON Staking V2 테스트 케이스 작성
    - SeigManager까지 커버리지 작업 완료 후 메인 저장소에 반영하기 위한 작업 진행 중

## Initial Goals

- 초기 목표 (3개월 : 80~100% 목표)
  - 개발환경 현대화
  - TONStakingV2에 대한 100% 테스트 범위 달성
  - 코드 기반 취약성 진단 및 검사
  - 핵심 로직에 대한 불변 테스트 추가
  - mprocs와 같은 도구를 사용하여 원클릭 테스트 환경 구축
- 현재 진행한 상황 (60%)
  - 개발 환경 현대화
    - 패키지들은 가능한 최신 버전으로 업데이트했고, 메인 저장소에 반영하면 됩니다.
    - hardhat.config는 이번에 테스트 케이스 정리해주시면 해당 테스트 케이스들을 정리하면서 반영할 예정입니다.
  - 테스트 범위 100% 달성
    - L2 + SeigManager 컨트랙트까지 완료했고, 현재 메인 저장소에 반영하기 위해 준비하고 있습니다.
    - DepositManager 등은 아직 작업하지 못했습니다.
  - 핵심 로직에 대한 불변 테스트 추가
    - 유닛 테스트가 완료된 이후에 진행하려고 아직 진행하지 못하고 있습니다.
  - mprocs와 같은 도구를 사용하여 원클릭 테스트 환경 구축
    - 이 부분도 아직 진행하지 못하고 있습니다.
- 추가 진행한 작업들
  - Omniscia issue 리뷰진행 완료 (#75-#243, #256-#300)
  - L1 Verification Audit 진행 완료 (TRH)
  - DAOCommittee_V2 Internal Audit 진행 완료
  - DRB 컨트랙트 리뷰 진행 중 (DRB)

### My personal opinion(Harvey) on contract extension

- 초기 목표 진행내역(80~100%)보다 낮은 달성을 하였지만 저희 ECO프로젝트 뿐만 아니라 현재 다른 프로젝트(TRH, DRB)에도 기여하고 있어서 해당 달성률은 이해가 가능한 것 같습니다.
- 전체적으로 Toakmak Network 프로젝트들의 Internal Audit을 진행시켜서 external Audit전 더 좋은 코드를 만드는데 일조를 하고 있습니다. 
- 계속 연장하여서 초기 목표뿐 아니라 추가적으로 다른 프로젝트에도 참여하고 다른 작업(Audit 및 로직 개선등)들도 계속 같이 일하는게 좋아보입니다.