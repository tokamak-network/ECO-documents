## Hammer’s work

- 9월 1주차 (~25.09.04)
  - Tokamak Network Terminal
    - unify the wallet connection/signing interface across browsers
  - DRB-node
    - add unit test code for DRB-node
    - study best practices for writing Golang test case
- 9월 2주차 (~25.09.10)
- 9월 3주차 (~25.09.18)
  - Changing Tokamak Network Terminal repository management method to monorepo(NX)
  - Reviewing Commit-Reveal2 audit report
  - Analyzing signature generation logic of SafeWallet
- 9월 4주차 (~25.09.25)
  - Development Audit Platform
  - Auditing DRB-node
  - Research Safe Wallet

## Check the development schedule

- TON-Staking-V2 Test
  - 현재 진행된 사항 : 테스트 코드 작성 중 토카막 네트워크 터미널 개발로 인해 중요도 낮음으로 연기
  - 남은 개발사항 : 새로운 컨트랙트 배포 계획이 있을 때, 현재까지 개발된 테스트 코드와 문제점들을 개선할 예정
- Tokamak Network Terminal
  - 현재 진행된 사항 : MCP 서버를 통해 로컬에 서명을 위한 웹 서버를 구동하고, 지갑 플러그인을 통해서 서명하는 부분까지 PoC 완료.
  - 남은 개발사항 : 기존 QRCODE를 사용하던 코드를 마이그레이션하고, 토카막 네트워크 커뮤니티 dApp들을 로컬에 구축하는 도구(Tool)를 추가할 예정.
- Audit Platform
  - 현재 진행된 사항 : Supabase로 serverless로 동작하는 플랫폼 구축.
    - Github 인증 기반으로 각 미션에 대한 ACL 적용 가능
    - 미션의 설명과 이슈 제보에 Markdown 및 Github 링크를 통해 코드 첨부 가능
    - 미션 작성자와 제보자의 수정 권한을 최소화하여 등록된 내용이 임의로 변경되지 않도록 보호
    - 리더보드를 통해 각 미션의 참여 현황과 기여도를 한눈에 확인 가능
    - 대시보드를 통해 참여한 미션과 제보한 이슈, 회득한 바운티에 대한 통계 정보 제공
  - 남은 개발사항 :
    - 잘 운용되고 있는 audit 프로그램을 참고해서 UI/UX를 사용자 친화적인 형태로 개선
    - 커뮤니티에 오픈할 첫번째 미션 설정 및 PoC 프로그램 진행
- Safe Wallet Multisig 서명 프론트엔드 개발 기획
  - Safe Wallet의 서명 프론트엔드를 참고해서 TRH에 Multisig 컨트랙트 및 프론트엔드를 모듈 형태로 추가할 수 있는 검토