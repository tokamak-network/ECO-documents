# Audit Branches

1. Hammer:  
  1. [이슈 리스트 ](/19dd96a400a3800ebeb7cdb5e3bdbee7)
  1. [v2.5-audit-hammer 브랜치](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-hammer) 
1. Carl : 
  1. [이슈 ](/1a7d96a400a3804e9eaaff5c5504498d)
  1. 
  1. [v2.5-audit-carl 브랜치](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-carl)
1. Certik 
  1. [이슈 리스트](/1a1d96a400a380deaca3df7dd08dcb76)
  1. [v2.5-audit-certik 브랜치](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-certik)
1. Omniscia
  1. [이슈 리스트](/1a8d96a400a38078a819c9413f4677e5)
  1. [v2.5-audit-omniscia 브랜치](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-omniscia)

# 2025-03-04 

1. L2시퀀서 시뇨리지 발급 로직 오류 : 수정 
  - [[Agenda (2025-03-04)]] 
  1. 케빈과 미팅을, 내용 공유해야 함 
1. 오딧 진행사항 
  1. Hammer:  
    1. 위의 1번 오류 발견 → 수정함. → 해머님 검토중 
    1. v2.5-audit-hammer 브랜치에 이슈 클로징 된것 위주로 반영된 상태임. 
    1. 이슈 중에 닫히지 않은 것 확인 
      1. 62 : 변경 진행해야함
      1. 63, 69 : 확인 후 Close 요청드림
      1. 64, 73,74 → 위의 (1) 에러와 연관된 코드이므로, 위의 1번이 완전히 검토가 끝난 뒤, 클로징해야 함. 
  1. Carl : 
    1. v2.5-audit-carl 브랜치에 TS-2를 제외한 모든 코드 반영함. 
    1. 피드백 보고서 제출함. TS-2 답변 못함. 준비해서 다시 보내야함. 
      1. [The First feedback Report on Carl Audit ](/1a7d96a400a3800ca930e1b38da72d68)
    1. 위의 1번 오류사항 브랜치에 머지하고, 리포팅 함. → 검토 요청함   
    1. TS-2 관련 미팅해야 함
  1. Certik 
    1. v2.5-audit-carl 브랜치에 resolved 된것 머지함 
    1. 아직 해결되지 않은 항목
      1. SMV-01 , SMV-07, SMV-06, SMV-05 → 위의 1번 오류와 관련 사항으로 코드 적용후, 다시 리포팅하여 검토요청해야 함. 
      1. DAO-02 : Harvey, Zena 커뮤니케이션 필요 → 진행 완료
      1. DAC-01 : 답변이 The isVoter check in the DAOAgendaManager.sol can effectively prevent the issue. 로 왔는데.. → 문제 없음
      1. CON-02 : 수정은 했는데 링크가 안열려서 comment를 남기지 못함 → 진행 완료
      1. CON-01 : 정리할것 있으면 정리하고 케빈 확인 받아야 함. 
      1. L2 시퀀서 시뇨리지 오류 수정한것 리포팅해야함
  1. Omniscia
    1. v2.5-audit-omniscia 브랜치에 이슈관련 코드 적용함.
    1. 아직 해결되지 않은 항목 
      1. Manual Review :** **DAC-01M, DAP-01M, DAO-01M, 
      1. Code Style : AAN-01C, CTX-01C, DAA-01C, DAD-C, DAE-C, DAC-C, DAP-C, DAO-C, EST-01C
      1. 보고서 작업 해야함. 
[[Feedback Report ]] 
    1. 이슈 처리관련 질문 
      1. 이슈는 어떻게 닫는가? 커밋 올리면 바로 닫아도 되는건지. 따로 확인하시고 옴니시아에서 닫으시는 것인지.
    1. L2 시퀀서 시뇨리지 오류 수정한것 리포팅해야함 →  기존 이슈에 관련된거 찾아서, 커밋하자. 

# 2025-03-05 

1. L2시퀀서 시뇨리지 로직 수정 작업 (65 퍼센트 정도 진행됨 ) 
  1. 기본 구성 완료
  1. Pause/unpause 시 반영하여 수정해야 함
  1. 여러개의 레이어로 테스트 스크립트 작성  
  1. 칼님, 해머님께 로직 수정해야 하는것 말씀드림. 
1. 오딧 진행 사항  
  1. Hammer 
    1. 이슈 중에 닫히지 않은 것 확인 
      1. L2 시퀀서 시뇨리지 로직 변경하고 알려드려야함 
      1. 62 : 변경 진행해야함
      1. 63, 69 : 확인 후 Close 요청드림
  1. Carl 
    1. 수정 필요한 항목
      1. L2 시퀀서 시뇨리지 로직 변경하고 알려드려야함 
      1. TS-2 : 멀티 시그로 변경
      1. TS-6 : 수정 진행해야함 ( 기존 로직의 사용하지 않는 함수에 revert 를 해주기) 
      1. TS-14 : 수정 진행해야함
  1. Certik
    1. 아직 해결되지 않은 항목
      1. CON-01 : 멀티시그로 변경 (멀티 시그 조사 필요) → 케빈과 미팅해서 방향성 결정 
  1. Omniscia
    1. 아직 해결되지 않은 항목
      1. Manual Review : DAP-01M, DAO-08M, DAO-10M 
        1. [https://github.com/tokamak-network/ton-staking-v2/issues/262](https://github.com/tokamak-network/ton-staking-v2/issues/262) - 문제점 인식..?
        1. [https://github.com/tokamak-network/ton-staking-v2/issues/271](https://github.com/tokamak-network/ton-staking-v2/issues/271) - 문제 없음
        1. [https://github.com/tokamak-network/ton-staking-v2/issues/273](https://github.com/tokamak-network/ton-staking-v2/issues/273) - 문제 없음
      1. Code Style: DAC-C, DAP-C, DAO-C, EST-01C

# 2025-03-06 

1. L2시퀀서 시뇨리지 로직 수정 작업 
  1. 수정하고 테스트 중 
  1. 테스트 완료하고, 하비님 내부 점검 후, 
  1. 오늘 안에 칼에게 보고서 제출하기 
1. 오딧 진행 사항  
  1. Hammer 
    1. 이슈 중에 닫히지 않은 것 확인 
      1. L2 시퀀서 시뇨리지 로직 변경하고 알려드려야함 
      1. 62 : 변경 진행해야함 (Member가 자의로 retireMember 실행 시 blackList로 추가)
  1. Carl 
    1. 수정 필요한 항목
      1. L2 시퀀서 시뇨리지 로직 변경하고 알려드려야함 
      1. TS-2 : 멀티 시그로 변경
      1. TS-6 : 수정 진행해야함 ( 기존 로직의 사용하지 않는 함수에 revert 를 해주기) 
  1. Certik
    1. 아직 해결되지 않은 항목
      1. CON-01 : 멀티시그로 변경 (멀티 시그 조사 필요) → 케빈과 미팅해서 방향성 결정 
        1. [[MultiSig Wallet]] 
  1. Omniscia
    1. 아직 해결되지 않은 항목
      1. 전체적으로 확인 진행해야함

# 2025-03-07

1. L2시퀀서 시뇨리지 로직 수정 작업 
  1. 수정완료하고, 칼님과 해머님께 보고함
  1. 하비님 수정코드 점검함 
1. 멀티시그 관련 케빈과 미팅 오후 4시 
1. 오딧 진행 사항  
  1. Hammer 
    1. 이슈 중에 닫히지 않은 것 확인 
      1. 62 : 로직 완료, 테스트 코드 추가 필요
    1. 오늘부터 코드 수정사항을 이슈로 열지않고 채널에 쓰레드로 커뮤니케이션을 하기로 함. 
  1. Carl 
    1. 피드백 보고서 제출함. 
[Feedback_Report-2025.03.06.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/cd548453-024e-437e-9ad0-be6f8b5721f8/Feedback_Report-2025.03.06.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYTBKT74%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFz5xM2aK7aiUPLtTNtFLrkXse1JVs78naA%2B0PLfyTnZAiEAg%2BMpLRgFHi1NgEoMuNCYctsAqmb0jL2xinv%2BUGTNThQq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFGi4hCKu2grO3CcUircA67TfLgb28IP5CDwtyQGtHr8xbBX28Mi8WvHFp8k2Wi91kctOzjAM5bv4BIk1OUJoS5zY7lJkysI9aBJE62Z0SGlHa3spo%2F35gHo61qCbcnVw9ME4A7SVxl38krcagsZRXEK7NODwgc89mvD5infN8A3t3ANqyKudeyDAbV5Ezq2aYCvQsWO%2BqyhQCY%2Fc%2F%2BbhY5%2Bpe%2BHEm8PpaSJZKAlKX7aeVultjjn7NqGfmtjw%2Fg5R7QyBWD2KRw3CRLToq0c528UaxLih1ZcqhyHYQcyT6mnUhGMX7UEIS67MgAPH%2FdWnbW%2BQl55mtrp21NBZq6WJEu60JjaZ8RsDN%2Bu3%2F6qyY2kYsX5qjxBvWRs%2B0cIyM0blsr93XYf9K5mc7WdwgLoHY%2BXMzNUeeAI%2FkJNQ63v27miA3J%2F2FMckq8H%2BJiT11vmOYDCR4Jzerdzslgcw4xATdrvgGVbo32wpt9Z5p4e%2B8kGBo3bSLUmWvdFznaZ0fS9z4x4CTfmD3KPhrm5kdeJFGfPqCIN9aa5phFPwt8IwA5YdDzUa3J5jW70RmwDDuamftpTnzv78qt5cboLUf35xqJsVQU7X5OxAcZKzT%2FIWC4PIriVFztAX4zy9u%2FUt67A8fQ5H%2F4YBEzP0i52MImZ28wGOqUBARofk4%2B1gNksPULT7ZqDXmKr2pFrqPu4m8dgSqvhlOkp8FLhfSAPzvTpNjHLxPvixeHS9zGW%2BRo3MJ1%2FtK9elqWPKheXLTL%2FeW7n%2BS1Vh1bc%2FwhmGdSuovKf%2BFM1U2JiJo%2B8zXnKl%2BERWei1NHItVdjoCkMmNZV7DnABtx7t4%2BiecmL0ui7tKBuTzHgwUAluvhMF8JB3ZWb7YDG9tFf5jm2M7ZxU&X-Amz-Signature=637e1581e289fd9fe09b982316ab43eb7c6d293515872c911849475fb5562b80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      1. 제출이후, 6영업일 이내로 칼님이 보고서를 다시 주시기로 하였음. 
    1. 수정 필요한 항목 
      1. TS-2 : 멀티 시그로 변경
  1. Certik
    1. 아직 해결되지 않은 항목
      1. L2시퀀서 시뇨리지 로직 수정으로 인해, 이전에 해결되었다고 한 항목을 다시 수정하여 제출하기 
      1. CON-01 : 멀티시그로 변경 (멀티 시그 조사 필요) → 케빈과 미팅해서 방향성 결정 
        1. [[MultiSig Wallet]] 
  1. Omniscia
    1. 아직 해결되지 않은 항목
      1. 전체적으로 확인 진행해야함

# 2025-03-10

1. L2시퀀서 시뇨리지 로직 다시 수정 
  1. 수정완료하고, 칼님과 해머님께 보고함
  1. 최초 오딧 커밋에서 1개 커밋 추가함. 
branch: [https://github.com/tokamak-network/ton-staking-v2/tree/fix-l2-seigs-](https://github.com/tokamak-network/ton-staking-v2/tree/fix-l2-seigs-)
v2
Commit: a7760e19801970c63005eecd05ab78c583e15476
1. 멀티시그 관련 개발  
  1. 1차 개발 후 케빈에게 리포팅 , 케빈 오늘까지 리뷰해주기로 함 → 케빈이 OK 하셨습니다. 
  1. repo: [https://github.com/tokamak-network/tokamak-multisig-wallet/tree/simpleVersion](https://github.com/tokamak-network/tokamak-multisig-wallet/tree/simpleVersion)
  1. [[MultiSigWallet Contract]] 
  1. 메인넷 환경 추가 테스트 필요
1. 오딧 진행 사항  
  1. Hammer 
    1. 해머와 같이 로직 점검 및 수정 중 , 커뮤니케이션은 채널 쓰레드 이용하는 중 
      1. 취약점 제출  [https://github.com/tokamak-network/ton-staking-v2/issues/303](https://github.com/tokamak-network/ton-staking-v2/issues/303) → 코드 수정후 커밋 제출함 → 해머가 확인후, 클로즈해야함. 
      1. 개인 Layer2를 배포하고, 오퍼레이터를 현재 커미티 위원으로 조정한다면, 어떻게 될지 확인해야합니다. ⇒ 아래 코드에서 해당 layer2컨트랙 주소가 sender가 맞는지 확인. 문제없음
```javascript
 address candidate = ICandidate(msg.sender).candidate();
        CandidateInfo storage candidateInfo = _candidateInfos[candidate];
        require(
            candidateInfo.candidateContract == msg.sender,
            "DAOCommittee: invalid candidate contract"
        );
```

[Link](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741525045357279?thread_ts=1741494712.069019&cid=C08FB51CJG4)
    1. 이슈 62 : Close됨
    1. Hammer님 질문
      1. 최종보고서를 별도로 작성해야 할까요? 문서 작업에 시간을 들이는 것보다 이슈로 만들고 코드를 좀더 보는게 나을 것 같습니다.
      1. 아래 사항들을 추가로 더 했으면 좋겠습니다.
        1. 테스트 커버리지 측정 및 100% 달성
        1. 전체 코드베이스에 대한 취약점 진단 및 오딧
        1. 기존 개발 환경을 최신 개발 환경으로 마이그레이션(필요한 경우 monorepo 도입)
        1. 주요 로직에 대한 퍼징 테스트 코드 개발
        1. mprocs를 활용한 원클릭 테스트 환경 구축
          1. 실무자 단계에서 이것이 중요한지 확인하기 (금액이 합리적인가)
  1. Carl 
    1. 피드백 보고서 다시 제출함. 
[Feedback_Report-2025.03.08.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/cd2a7cbd-2852-428e-bf3d-b33f1033d4f0/Feedback_Report-2025.03.08.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNQLI3CR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAf75TM%2FTiXYumMCawJ1Is%2BLxkttobl0o9VGLObp86cnAiEAzV8CPCGdrlI8PjuRY8s6IJF3gAy5q3%2Fz8IO8360d13Aq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNKO7A9Qo6D21WHDgyrcA16p94OEXklMClHepR9eiRMGn2alOfRk0VAUuQCGh7%2ByAG%2FZbM8LGQ1RKSEs06EqF0Zd1wYvkW4tKa4Uq1D5U%2FKrA%2B3rHKsliFdh5d2df8pzUPiTSXBo90GdL%2BDsbe%2BJe1FvZmm%2Bo2R6zpGIBaroym5Hl0dRYdHKnYXLcI%2F3Ofyyq7viNlOM3pXUrFK2VrgaNGIlz4wbUhurcLvsopdx6qt8Dlndt%2F17u6%2BjMqiieajiwOhujPRSVNzcZVpWmCpbfEwBMjXOO3YS%2B%2FBQT7npQGxWDZ7kFFVosZQU5JBKHNMKesYDnIULHq%2BuwzJiTSM%2F9u0ceF1ITn2tPcTyqME%2FN3otHt2hnly2Qn0OLZmcgMqwcazm5YWcksQSLo895o90j7yQ13g6wPQ7cKetMb0jtRpC7RTeF53wdDGw6neCtmYnDzjIBl7UXTpGbIc6BfNKzypkbjIljfmYIw1bMvqKoNk%2B3cqF%2FdmGqCyl2vdGh2lwgoHPJaVgxPupn%2FXU1dFEyzPcMQCLDT%2B1ti3lua8pHlb2zwH8TSUS3SXX%2FbeXJa00wrJNsjfv6cmqqNAWgo8BqgArlH7Ic6yaG%2Ff%2BsvD1TGBNA6DAOYhWPVgVZht9fdMUgQUTMwSsPrr5gzF6MKqY28wGOqUBCNmwq2K7PLzqiH7Gcwq67nGLJYH34bkjegWww2NP51sttDy6vpo6GGGl4qZ%2F%2B0yUnDxuzXzGhc%2BNPPgIxhGjP%2Fr0ZoY9nIkNgAfHO1inQvjDW3PSyKC0oRjEgzSbMWQik%2B2ts%2FYpArgIvIrFZH3JpA2cefOFtkrXLDY95gHpNpWyn0BEYFT%2F6dxglDGbeinS9MPzqr6JfADHeB5YUN5rHWlZcpsG&X-Amz-Signature=b69ce7f35d597023b8da8af8888b2b3c1088a3f009fa1f89a2fa9df0ace05527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    1. 칼님이 점검하고 있는 중 → 이번주안에 보고서가 나올것 같음  
  1. Certik
    1. 2차 보고서 확인 및 답변 중 
      1. L2시퀀서 시뇨리지 로직 다시 답변함 
      1. CON-01 | Centralization Risks 작업중 
        1. DAOCommitteeOwner 함수들 대다수 삭제
  1. Omniscia
    1. 전체적으로 확인 진행해야함
      1. 확인 진행 중

# 2025-03-11

1. 멀티시그 관련 개발  
  1. 메인넷 환경 추가 테스트 필요
1. 오딧 진행 사항  
  1. Hammer 
    1. Hammer님과 대화
      1. Tokamak - 보고서가 꼭 필요하진 않으나 업무가 상호간 종료되었다는 기준에 대한 합의가 필요합니다.
      1. Hammer - 보고서가 있는게 깔끔하다면 오딧을 13일까지 진행하고, 추가로 1-2일정도 시간을 더 들여서 보고서를 작성하도록 하겠습니다 
      1. **보고서를 받고 최종 잔금나가는 것이 맞아서 13일날이 아닌 보고서받고 드려도 괜찮을까요? **
        1. 13일날 간단하게 그냥 issue만 정리해서 보고서를 주시면 13일날 잔금 드릴 수 있을 것 같습니다. (보고서 업데이트는 필수사항이 아님)
  1. Carl 
    1. 칼님이 점검하고 있는 중 → 이번주안에 보고서가 나올것 같음  
  1. Certik
    1. 2차 보고서 확인 및 답변 중 
      1. [CON-01 | Centralization Risks 작업중 ](/1a1d96a400a380958368c1f92acf09af)
        1. DAOCommitteeOwner 함수들 대다수 삭제
        1. [[23]] 
      1. 수정완료 한것을 v2.5-audit-certik 브랜치로 모두 머지했는지 확인하기 
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
    1. 수정요청사항 중 수정하지 않은 것 다시 점검 중 

# 2025-03-12

1. 멀티시그 관련 개발  
  1. 추가 변경코드 적용 
    1. [[MultiSigWallet Contract]] 
    1. 서틱 답변에 반영하여야 함. 
1. 오딧 진행 사항  
  1. Hammer 
    1. 최종보고서 확인
      1. [Table of Contents - HackMD](https://hackmd.io/@JWIJNWSZQYe4YscQzAySwQ/rksDtCpskl)
      1. 최종 커밋 명시하고, 
      1. 하비: 깃에서 내려받아서, 테스트 
        1. npx hardhat test test/layer2/units/3.all.test.sepolia.test.ts
        1. **3-1.layer2Manager.zero.sepolia.ts, 3-2.l2StartBlock.one.sepolia.ts**
  1. Carl 
    1. 칼님이 점검하고 있는 중 → 이번주안에 보고서가 나올것 같음  
  1. Certik
    1. 2차 보고서 확인 및 답변 중 
      1. [CON-01 | Centralization Risks 작업중 ](/1a1d96a400a380958368c1f92acf09af)
        1. DAOCommitteeOwner 함수들 대다수 삭제
        1. [[23]] 
      1. 수정완료 한것을 v2.5-audit-certik 브랜치로 모두 머지했는지 확인하기 
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
    1. 수정요청사항 중 수정하지 않은 것 다시 점검 중 

# 2025-03-13

1. 멀티시그 관련 개발  
  1. 추가 DAO executeTransaction 테스트 진행
  1. 서틱 답변에 반영하여야 함. 
1. 오딧 진행 사항  
  1. Hammer 
    1. 최종보고서 받음
      1. [Table of Contents - HackMD](https://hackmd.io/@JWIJNWSZQYe4YscQzAySwQ/rksDtCpskl)
      1. 코드 확인 및 테스트 → 확인함.
      1. 케빈,제이든과 확인후, 해머 오딧 종료해야 함. 
  1. Carl 
    1. 최종 Branch : [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-carl-merge](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-carl-merge)
    1. Carl님 보고서
      1. EN 
[Tokamak Network - Staking v2.5 Security Assesment-draft-031311-EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/bb36ffb9-81af-4a81-aaf2-ed3ae35c6fb5/Tokamak_Network_-_Staking_v2.5_Security_Assesment-draft-031311-EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QHMM2AF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeyVF9gzMs52Uy98sMVEnqGGGKAF3%2FhygpvfNZWlFGkwIgXgJDPwBa86sjTJWkwkOM51dJFipBI4Aw%2FP%2BZDiN6wy8q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDGiiII7joVaTJBX6GSrcAxOqMZBH0X5YXTnJm35WTEroFuer915XISbX%2F867SFAw6ndRYD6a%2BAF8j46Pxep6%2BesawAd%2FXEepaNxuiiZBZpExQEhZ71jFSXDZu7S7aL8BiV1oGIy9JvxxyGPPG2gYCjm8%2Bp79Dxtt9yu1ZNtO8WI92Q%2BChVq4offDesUoJrDAmG3pwjdfSv2k%2BbHA7IdFBHK2y5WIVVPgMPS1iLw2Ksr0EvpcipoG6bWYb6ZHV4216TwksTNqaUNAi%2FSfEusz4BsoAtEV77TboiB9JBLrjYv%2F7cW3FaMsRv%2BfMi2FmnoHImsVnHZNettNmNEresshxMpFDN8qS0QXZMpZRIka2FVvVjxQKqh%2BUvC%2FHOty88zqDyJAXMKz8RBIeZV0IA7wPf4h8F5YuOkrWzdeFpgfGKmIOSt8pmRekcsuI9qQqiScCLIk9%2FofvQvvpxZwtK9K0fW0DocgEosfVmuXQ3mcXfiIkmumTRdLR42X1gqhUdtKwZJhO%2B5vsG2oxI5empJ2AFWyqaHxyampYxhwfpuLGZojYVGjvYDexm9Xj6J2eLTQemh07gV0sACDrdyq0ytpRb8NlTcheqBFEcFmgurMazdhBzPj92YexrMs3q2SoSorNZaqtJ6ERDG9Fe4CMI6a28wGOqUB1CVMZSJnoVh%2B2Hj0bJhG%2Fwgm%2FoCzr2bwaCAJuEhDxQL3%2BzkyD5E4FKWqu190barqHjEB6Hwpy8ta6VPHtoxV0tSSGNdgsU1%2BAJruF462sbHlP1GuBLFgseNfJPqqLa4k3X%2BFn7mWf86dhw677TWxqwOemnUPCgbtKlnSA8U5pz0ENPk8EG3BxLVZ0F9uYwFABVmKbQvwhRyHFswCnn98qN9DKXH%2F&X-Amz-Signature=7082e8486cab7f788c582047e6bef83967622c461b6238cb310c621c4bbd5161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
      1. KOR :
[Tokamak Network - Staking v2.5 Security Assesment-draft-031311.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/602c5e48-4889-4c40-8648-d255aa3531ee/Tokamak_Network_-_Staking_v2.5_Security_Assesment-draft-031311.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJGSVUCQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBEiwJG8fc%2Bg%2BaV2V7vtmy7QKzaXem%2FPzBWxl2yvZhNSAiEAmm8%2Fekb8kMZLVBMNjxIPUyZMPfb6ME%2BOe8QD4AVRtsIq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDE5nzlT3Fx8bXyqhWSrcAzfF3RYh7%2BdvZpNGcaYklnpPAlBQVBa4lgOswPXphtnz79xelh%2FL6hpKGA5J%2BJwW1I28EErLpW4B7SNiCyjQLX5b8SaIhbrsN2WV3MMuDWuesyCrPt%2Bxdi1HBQoYKVpyzJCDvapUr4H6%2BQ4c443eFOVsFrYC99BNMX%2Boh9FI8QzXWijHEVOxh1mkmYcAbkBCYDuqODSptaMoSDAIG8IhAAF%2B0FPZIuiMdqTyG7%2F4mgPn9sg1OzC3bi3x8oKMbaVK4bPLW15YI5duqJPp9%2B5ChzIhORqpKui0gSf3LAUrqBVJyQPSLBrfb82RoB08K15cJMtJPCKF7XBsuI%2B3OLN8nQjNoPxDaGTMGNAexZvEjh5j0D4TZac39DaqFDAFn%2FDu3RdqVs%2BwonrTXrpXig6RjwVMy4w2WakbD27yYeJcL%2BsVi3zk0Bx6Nmnu5Xpz3gZWM8G2Uv4H%2FnBxCOgEiRWayAByfegtGBeZWCeaGjLJOIexruatkrq5x8FZndIvMYDUxcnGrqeGFW6zt9xiBkLMnO3VNNeVG%2FZJhL9IDDMtBIhCk%2BKVMnqx7ppj1znbCjIyrN%2F%2FmvUCf1pvGck2TJkQ7DnT5DV59mznVxlLIxpmOahm8ZPiqQCQlf%2Bza9JNMMiY28wGOqUBMOLNseRF0l2q7PWyxJdqDmTqB9cm%2FJfZ7sd78bD3LS2ez4BCEGztO8q7eVyxNE6REEA%2F9uiAUeupx9cQvNjaJ9FTdNSkdBa9h7ZuuNMT3XoB067oFNGu3nj5OVq90GtXlLB4%2FYyiExyvPUYDxYt4KFL8MmRl2zIBZowLJkQvORv9NtNGqn91%2B3pSYBQXxJsSg0zaeGoX1Pnh%2B7JKDR8gm38MJdzY&X-Amz-Signature=1d335c272a3a8981f3676d73761b7a052dc48c97088c9bb9dcc33a59a420bc0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    1. Feedback 보고서
[Feedback_Report-2025.03.11.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6559e2ef-9d93-49d6-a193-d57c3230dff7/Feedback_Report-2025.03.11.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625Q7BC6A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq9Q8Oi00zQYu7zDV%2FfsL51LDj4VmJwZvcZjmzXAFvJgIhANxbLWZEsFwSold3ZJPSYxfUQYPCtQoVBxkSCfVGvoRqKv8DCHoQABoMNjM3NDIzMTgzODA1Igyd0aZEbp8DQLBBuZIq3ANPMF5%2FCTRy%2BBd1TuuU42sQP7Cib0Zx%2BcCP8BpKZe3D4Eg40QAC4b4HgZtkUz4VB5Rd5X2DU4PjAFUtB3AvKEFwmhRPiHM3%2F25SEctzn2KVP71XhPB8Czr9PNVoz8Oh%2BEJ3IMDXpL9vBO3eTCxRRYscCCdWFpntAvA6EWsNXmV6%2Ba09tLPqWWb197RwTayCttYtf%2Bhdnz%2FMiBaEJ6lxV0fGIsQ6MGPaJRj5ph8JaOfrGRH3cnXmV9BpVES5UC2hJfDQiu1L0T03cqAxJdgCPcsWIr78dbhtoOs2qLxLysfOz97aK%2FS2JQjIuL6eW%2Bix%2F9ZtdRPEWdP3ekVcCQwp0umq78qJroxPpnI5gJMapJfKP1CVKCh%2BqhSwyYynwTmn4HtJLQyYM5sD1lHlWQ9gImkfmCvQP3JmZgMKlj5Ol9Wpw6L6rcTtG%2BjiCL%2BsPmXssAHvB7zjdlvzv%2FiKRCZY78ctq2VcIEwwFQ4F86TF80nnqQ4khpVjgzn8f90e5DMwkZEqy2O%2BoOia6iUyaCH6FMSMUoYlxHAhQIXoA8rov3IsR7h3i6fa5CQkDS%2BCB%2B01MzEOsf5i4ClBJK54QOZvOFQw%2BDNvzXwcXUsDUbG3fTEJEHwf2ZiaxfFPyWMmtDCnmdvMBjqkASWPbl1hgwsJCCKDPyNwoEF8x8rLrrEi1txyslL6UyqkS8mGsujjCl2eoIEK91vPymVl%2BBSNFXYALBacdP4HDkUaWSblSkSw8%2FUNSEaIgy6unMCtLctp%2Bb59sBjM92hJ1sJG3sL%2FHQbZXQr7rO8aCFD1yxPe0ZIQ9%2BGSBoUtTvbnv1J7RO9F4okTHvIy23bj6MksailYE2ZSVaf2gGKmDQKCz1It&X-Amz-Signature=75d533ae10d5193ead43d3f0cbe9cc25bb17498e902b0c5550098ab4e0d0930c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    1. 코드 확인 및 테스트 → 확인함. 
    1. 케빈,제이든과 확인후, 칼 오딧 종료해야 함. 
  1. Certik
    1. 2차 보고서 확인 및 답변 중 
      1. [CON-01 | Centralization Risks 작업중 ](/1a1d96a400a380958368c1f92acf09af)
        1. [[23]] 
          1. DAOCommitteeOwner 함수들 중 target으로 실행하는 함수 삭제 완료
          1. DAOCommitteeOwner에 executeTransaction 함수 추가 (멀티 시그 repo에 예시 함수들 추가하기[현재 없어지는 함수들 추가])
      1. 수정완료 한것을 v2.5-audit-certik 브랜치로 모두 머지했는지 확인하기 
        1. 확인 완료 - CON-02 추가 머지 필요 (머지 진행함)
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
    1. major와 medium 을 서로(제나, 하비) 각각 재 검토해보기   
    1. 이슈143, 153에서 다른 라이브러리를 사용하라고 해서, 채널에 라이브러리를 추천해달라고 요청함. 

# 2025-03-14

1. 오딧 진행 사항  
  1. Hammer 
    1. 최종보고서 국문/영문 받음
      1. 국문
[STAKING_V2_AUDIT_REPORT_KO.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6f6c4924-1d19-4a92-a8fc-4ac16fe7e39b/STAKING_V2_AUDIT_REPORT_KO.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CANBJNM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHLQB%2FVyeXGTbEWfTL2NUhH9oDzPBSdc2RpXn7YoGtOEAiB4EM9AlFhggkwXGCqL0MaHFBLQ5oUol1KSOK0nWRJzHir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMoDCQt6LoGrQBQ2tbKtwDq0htjwnESlkfVHM%2FR4lhOOPDpqPcaA%2BaB7A2KUIzEu0BaF4prwapMxVo9BWeo%2Bo274oQ%2FxHgEB4cq7M7W5U1HXyqTo1LoOdtiMsRjkdpCsNSMni1TIaQm1WJuc0hAlmy9xVNZ41ot8ZVEub0h8qT6ABCbADLfAnoqbmXglpUrcDQ4wIUDXlfK8oWFQQ5zXzauA3LZyQPApeq8JMBuWzjJa2uiGuRHKMiCLaY%2B50OXTOgLEyyoABHpDD1IchKf9zslsYYRbS69cSvPJlQqWvgUHGY4kYc9Z%2BT%2F92mCoog9Dn%2BEFR%2FFT6VVFs6lOuxa4EmP6qaZjE5%2FGVI2DYu%2B37lvbmV1b9GBWaQBEpD1w41rSh990kOhmzsMkQt%2FsbU4UpTiEVSRNAEBjpO814axpfvQ6Wrk832yXJz0pAOIdg0Pct1pg3L0FfsaGV7mu9UhTR4EuzfoE5AN0GVfGk6qkg%2FuxcepHWpXcNmKsgraNsKm%2FaxXZowEqJngsmex27nn2V6RjD%2Fqh%2Fd9ZlvU5SiWTN9h%2BH%2FWf92aLKDvCzzT5ePcviF%2FaHqtQHf9mlxJvVBv1UKvYhKqsngTuWqTdxqP7s6%2FrH%2FSYawlg1Gf%2Bfi2Ux5Xg%2B0wwcY1TvcBxr78Rsw9JrbzAY6pgFTA97l4mQyjJlhDvGpI0Ca5Kbwn0yRgd5ceNhD03sxcYgUu6JcmYyi%2FSkcX2LlEe0lkld5x9nG9c%2Bkml8Y%2B6%2BciXsXHSnkHFqYJ7Cp%2FyTpY6YUVIRO4H0wmXFp2KwR9PRk90tC9PgRbN7ifEEaII6neh5Lu%2FZsP8lFXCzIDgNSKHlbtzNSjmLYKEEN%2FLrc6QGi9KK3RvA%2FpgkimMJLGWrJgeQek%2FLy&X-Amz-Signature=16827677ca55039c0e9dbf270a0d406012b5caee6c7e8c2bac3f2fe48d3473d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
      1. 영문
[STAKING_V2_AUDIT_REPORT_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d7ece422-5369-41c5-be89-857c453eba23/STAKING_V2_AUDIT_REPORT_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653H4VM5I%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTO257P8%2Fnea4mXz5mYt7yTwFMzjdCpvAODfSA41bUsAIhAJ7o%2FSJT6uxAYJuBqXzoK%2Fn9aUL9sKslTa0E74x%2Bph%2BqKv8DCHoQABoMNjM3NDIzMTgzODA1IgwMMi4cdR988n8dnxUq3APWjRxGJLd1TMz01%2Bnpy4uMDz2RZGIzswqMnkz50m24C7MN%2BX8y2orvlsxz%2FK8h2W%2B6nrjS4hcXtuqZFfKXO3duY62sH%2BTyqGwSQKK55hss%2BaGPkeIC3jNyDsj489jov2wWcUelbLF52p5bE2omuE7nGhM8WxvgO0zO4QSgXDHPaO9co8HzOJCx1ZIaopaRsaCighLFiGCw7APr9X%2Fj1sm8OYpYjY2FncclGaO%2BJdRIoYSnFRb5krHknffC3AtaUoRXlJiJPwHaQx8%2Fmm5w%2BEftdjKL%2FYaz2UlTmdm0XJdc4PzdmjvhszdZl51r6BnTHtxzeW3M3Bbl0I5yUZKG1S0aAOKwskDx365v94gdcBK2xP%2FuBIzrHX9rT35SnpriB3cLVBX0YPFpSOkefJOD5yymvIWaBIaSbldLUFK4NttuNvkON2CDP7IPvPPOf5CKl8aXkl4kx3mzDjOGRZbw43Dm%2FtRGHI2kR9eI0AawUSbtqkneLcZKgaY9bCashBublfnfLPOo%2F8OMFQCUyoqT6NI%2BmZ3zUeDa5i6A1HilLC%2FBCVSTuR7coOO%2BKZb7u%2B6TonCLwsFWM8KdfPPhcJCo46fWZyus%2BysiwsdoVpI0dopjDpsAIWMSubadyAoQgjDBmNvMBjqkAW0PdGtodPqGf93IlwMwexIqwVSgXbCnLXYQVvb97tZBrJsWtERpFCSOqPStwEKrLjVoDKdAkeWqC23QpCSv%2BWF8aA3GmrmxNR%2B3QSmaNPpxSRS%2FMPxIOlyVm6j2LNDgneVj1T6RrqeO6yFvaGqsDtg83ooxrGpk%2F3Z6kJdv1trjFATmGrHgS7OHkMYBxekuuZHw5YZI8IhkkGkTvatxefclSzQs&X-Amz-Signature=a88acf28843bf289744b8ca69ece89b822f27705076bb365330da5661d45bf3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
      1. 마지막 Branch
        1. [bd80049e95d573f2fb6e7463d68e61438c9ff157](https://github.com/tokamak-network/ton-staking-v2/commit/bd80049e95d573f2fb6e7463d68e61438c9ff157)
    1. Jaden님께 정산요청함 
      1. 정산 주소 : [0x4D145A5e90736ad71cBF0081366625BD9eb170Cc](https://etherscan.io/address/0x4D145A5e90736ad71cBF0081366625BD9eb170Cc)
  1. Carl 
    1. 제이든님께 정산요청함 → 3월 14일 까지 정산하신다고 함. 
  1. Certik
    1. 2차 보고서에 CON-02, CON-1 Pending 에 코멘트 남기고 Certik에 알림.
    1. CON-02 답신
      1. [Project Findings](https://skyharbor.certik.com/report/ba5c44fc-4e5a-40cd-a1f7-519149448df4?findingIndex=CON-02)
      1. CON-02 is resolved. However, many fixes are reverted in the commit including DAC-05,DAC-02,DAC-04 and COT-01
        1. 적용하고 코멘트 남겼습니다.
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
    1. major와 medium 을 서로(제나, 하비) 각각 재 검토해보기   
    1. 이슈143, 153에서 다른 라이브러리를 사용하라고 해서, 채널에 라이브러리를 추천해달라고 요청한 상태 
→ 답변해줌:  a well-audited example implementation being that of Uniswap V4: [https://github.com/Uniswap/v4-core/blob/main/src/libraries/FullMath.sol](https://github.com/Uniswap/v4-core/blob/main/src/libraries/FullMath.sol)  

# 2025-03-17

1. 오딧 진행 사항  
  1. Hammer 
    1. 정산완료
    1. L2에서 출금 대기 중인 것도 L2 Total TVL에 포함되는 것에 대한 체크요청 
      1. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099)
      1. 해머의 체크포인트는 일리가 있음 → 언제든지 바로 뺄수있는 금액이기 때문에 어뷰징의 가능성이 너무 높음. → L2에서 출금예정인 금액은 L2 Total TVL에서 빼는 것이 합리적임. 
      1. TRH팀에 출금예정 금액을 온체인에서 확인할 수 있는지 문의함. → NAM :  현재 없는데, 더 생각해보고 피드백을 주겠다고 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929)
    1. 저는 Tokamak Network의 개발 환경을 현대화하고 더 쉽게 접근할 수 있도록 만들고 싶습니다. 이를 통해 더 많은 사람들이 프로젝트를 테스트하고 더 안전하고 더 나은 제품을 만드는 데 기여할 수 있습니다. 이를 위해 다음을 수행하고 싶습니다.
      1. 개발 환경 현대화
        1. hardhat 환경을 foundry로 변경하고, 패키지들도 가능한 최신 버전으로 관리했으면 좋을 것 같아서요. 일전에 테스트 진행해본 바로는 테스트 코드 수행 속도가 10배 이상 차이 나는 것 같더라구요. 그리고, L1 / L2를 docker로 deploy해서 언제든지 테스트할 수 있는 환경을 만들려고 합니다. 현재 사용되는 툴들이 비교적 너무 오래된 것들이 많아서 비효율적인 부분들이 많은 것 같아요.
      1. 100% 테스트 범위 달성
      1. 코드 기반에 대한 취약성 진단 및 감사
      1. 주요 논리에 대한 불변 테스트 추가
      1. mprocs와 같은 도구를 사용하여 원클릭 테스트 환경 구축
    1. TON-StakingV2쪽 컨트랙트 개발도 참여하고 싶습니다.
      1. 해당 부분에 대해서는 정확한 내용 논의 중 ("비개발자 관점에서 코드를 면밀하게 분석하고, 개선하는 과정이 필요할 것 같다."라는 생각이 들어서입니다)
      1. 릴리즈 일정이 잡혀있어서 TON-StakingV2에 대해서는 아래의 작업만 진행하면 좋을 것 같습니다.
        1. 코드 오딧 및 코드 개선 작업 참여
        1. 테스트 코드 개선(커버리지 측정 및 100% 커버리지 달성)
    1. 제안드린 5가지는 모든 repo에 대해서 진행하고 싶습니다.
      1. 진행할 repo를 추려야할 것 같습니다.
      1. 기간과 금액은 작은 단위의 일감을 여러개로 만들어서 정하는 것이 좋을 것 같습니다.
  1. Carl 
    1. 정산완료
  1. Certik
    1. 2차 보고서에 CON-02, CON-1 Pending 에 코멘트 남기고 Certik에 알림.
      1. CON-01은 아직 답변없습니다.
      1. CON-02 is resolved
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
    1. major와 medium 을 서로(제나, 하비) 각각 재 검토해보기   
    1. 이슈143, 153에서 다른 라이브러리를 사용하라고 해서, 채널에 라이브러리를 추천해달라고 요청한 상태 
→ 답변해줌:  a well-audited example implementation being that of Uniswap V4: [https://github.com/Uniswap/v4-core/blob/main/src/libraries/FullMath.sol](https://github.com/Uniswap/v4-core/blob/main/src/libraries/FullMath.sol)  

# 2025-03-18

1. 오딧 진행 사항  
  1. Hammer 
    1. L2에서 출금 대기 중인 것도 L2 Total TVL에 포함되는 것에 대한 체크요청 
      1. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099)
      1. 해머의 체크포인트는 일리가 있음 → 언제든지 바로 뺄수있는 금액이기 때문에 어뷰징의 가능성이 너무 높음. → L2에서 출금예정인 금액은 L2 Total TVL에서 빼는 것이 합리적임. 
      1. TRH팀에 출금예정 금액을 온체인에서 확인할 수 있는지 문의함. → NAM :  현재 없는데, 더 생각해보고 피드백을 주겠다고 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929)
      1. Nam 이 목요일까지 답변주기로 함 [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE)
    1. TON-StakingV2쪽 컨트랙트 개발도 참여하고 싶습니다.
      1. 릴리즈 일정이 잡혀있어서 TON-StakingV2에 대해서는 아래의 작업만 진행하면 좋을 것 같습니다.
        1. 코드 오딧 및 코드 개선 작업 참여 → 다음주에 아젠다 올려야해서 추가적으로 진행하기 힘듬 (취약점이 있으면 하는데 코드 개선은 힘들다..) (이 부분에 대한 기간을 정확히 물어보기, 재단에는 해당 기간을 Agree하시는 지에 대한 내용 확인) (기간때문에 긍정적이지 않음)
        1. 테스트 코드 개선(커버리지 측정 및 100% 커버리지 달성)
          1. 테스트 커버리지는 아직 진행해보지 않아서 정확하게 측정은 불가능하지만, 30-50%를 목표로 하려도 합니다. 그 외에도 오딧을 위한 툴링들도 함께 진행하려고 합니다. 예를들어 이번 오딧에서 나온 프록시 이슈 같은 것들을 자동으로 점검할 수 있는 도구들도 개발하려고 계획하고 있습니다. (b만 진행한다고 하면 총 몇% 목표로 진행 하실 수 있는지 여쭈어보기)
  1. Certik
    1. 2차 보고서: CON-01은 아직 답변없습니다.
  1. Omniscia
    1. 보고서 작업 중   [[Feedback Report ]] 
1. 아젠다 준비 시작하기 
  1. 서틱과 옴니시아에서 최종보고서가 나오면 바로 아젠다 올릴수 있도록 준비하기 
  1. 해머: 코드 오딧 및 개선 참여 일정이 어떻게 되는지.. 
  1. 옴니시아브랜치에서 새브랜치 따서 공유하기 
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
    1. 테스트 날짜: 목요일 2시 콜 
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
    1. 테스트 날짜:  
1. TRH 에서 개발 및 테스트를 하기 위한 별도의 테스트배드를 구축해야 할 필요가 없는지. 
  1. 심플스테이킹 컨트랙 전체 재배포, TRH 개발용 , sepolia 

# 2025-03-19

1. 오딧 진행 사항  
  1. Hammer 
    1. L2에서 출금 대기 중인 것도 L2 Total TVL에 포함되는 것에 대한 체크요청 
      1. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099)
      1. 해머의 체크포인트는 일리가 있음 → 언제든지 바로 뺄수있는 금액이기 때문에 어뷰징의 가능성이 너무 높음. → L2에서 출금예정인 금액은 L2 Total TVL에서 빼는 것이 합리적임. 
      1. TRH팀에 출금예정 금액을 온체인에서 확인할 수 있는지 문의함. → NAM :  현재 없는데, 더 생각해보고 피드백을 주겠다고 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929)
      1. Nam 이 목요일까지 답변주기로 함 [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE)
    1. 테스트 코드 개선 (1달 : 목표 달성률 30~50%) 
      1. 커버리지 측정
      1. 100% 커버리지 달성
      1. 코드 오딧 (테스트 코드 작성하면서 조금씩 진행)
        1. 코드 오딧은 심각한 취약점이 아니면 반영안하고 다음 버전이 나오면 반영하기로 함 
  1. Certik
    1. 2차 보고서: CON-01은 아직 답변없습니다.
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백 → 케빈과 제이든에게 공유함 
      1. 해당 내용 아직 답변없음
1. 아젠다 준비 시작하기 
  1. 서틱과 옴니시아에서 최종보고서가 나오면 바로 아젠다 올릴수 있도록 준비하기 
  1. 옴니시아브랜치에서 새브랜치 따서 공유하기 
    1. [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
    1. 테스트 날짜: 목요일 2시 콜 
    1. **배포 :  심플스테이킹 전체를 다시 배포하자. 주말까지 새로 배포하자. ( 커뮤니티버전 개발 및 TRH 개발용으로 사용) **
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
    1. 테스트 날짜:  
1. TRH 에서 개발 및 테스트를 하기 위한 별도의 테스트배드를 구축해야 할 필요가 없는지. 
  1. 심플스테이킹 컨트랙 전체 재배포, TRH 개발용 , sepolia 
1. 블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-20

1. 오딧 진행 사항  
  1. Hammer 
    1. L2에서 출금 대기 중인 것도 L2 Total TVL에 포함되는 것에 대한 체크요청 
      1. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099)
      1. 해머의 체크포인트는 일리가 있음 → 언제든지 바로 뺄수있는 금액이기 때문에 어뷰징의 가능성이 너무 높음. → L2에서 출금예정인 금액은 L2 Total TVL에서 빼는 것이 합리적임. 
      1. TRH팀에 출금예정 금액을 온체인에서 확인할 수 있는지 문의함. → NAM :  현재 없는데, 더 생각해보고 피드백을 주겠다고 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929)
      1. Nam 이 목요일까지 답변주기로 함 [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE)
    1. 테스트 코드 개선 (1달 : 목표 달성률 30~50%) 
      1. 커버리지 측정
      1. 100% 커버리지 달성
      1. 코드 오딧 (테스트 코드 작성하면서 조금씩 진행)
        1. 코드 오딧은 심각한 취약점이 아니면 반영안하고 다음 버전이 나오면 반영하기로 함 
  1. Certik
    1. 2차 보고서: CON-01은 아직 답변없습니다.
    1. 하비님이 확인해달라고 쓰레드에 문의하기로 함. 
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백  
      1. 해당 내용 아직 답변없음
1. 코드 통합 
  1. 하비님 코드 머지 완료함  [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda) 브랜지에 머지함
  1. 제나 통합 브랜치 : 옴니시아+칼 통합함, 해머 통합 중.
    1. [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge)
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
    1. 테스트 날짜: 목요일 2시 콜 
      1. 제나 배포 및 테스트 스크립트 완료: npx hardhat test test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts 
        1. code: [https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1165](https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1165)
        1. 아젠다 생성하는 스크립트 중에서 다오 변경된 함수 반영 요청 : @Harvey  
          1. 아래 sepolia와 mainnet 스크립트 모두 반영요청함. 
          1. 8.dao-staking-v2.5.deployments.sepolia.test.ts
          1. 7.dao-staking-v2.5.deployments.mainnet.test.ts
          1. 아젠다 생성중에 SeigManagerV1_2 업그레이드 추가됨 
            1. [https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1249-L1256](https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1249-L1256)
          1. 아젠다 생성중 SeigManagerV1_3 추가 함수 변경됨 
            1. [https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1275-L1292](https://github.com/tokamak-network/ton-staking-v2/blob/e02e64bdd25dd37416f8f3214f08ee02c91f44ab/test/layer2/units/8.dao-staking-v2.5.deployments.sepolia.test.ts#L1275-L1292)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
    1. 테스트 날짜: 
      1. 제나 배포 및 테스트 스크립트 완료: npx hardhat test test/layer2/units/7.dao-staking-v2.5.deployments.mainnet.test.ts 
    1. 아젠다 배포 문서 [[Deploy TON-Staking-v2  on Mainnet ]] 
      1. 예상 가스비 적기 
      1. 컨트랙 배포 스크립트 만들기 
      1. 아젠다 제출 스크립트 만들기
      1. 배포 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 아젠다 할때, 13번 아젠다 No 투표해달라고 요청하기  
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. ECO 커뮤니티 버전 개발용, TRH 개발용으로 사용함.  
  1. [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 이번주 주말까지 작업하기 
1. 블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-21

1. 오딧 진행 사항  
  1. Hammer 
    1. L2에서 출금 대기 중인 것도 L2 Total TVL에 포함되는 것에 대한 체크요청 
      1. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1741932606024099)
      1. 해머의 체크포인트는 일리가 있음 → 언제든지 바로 뺄수있는 금액이기 때문에 어뷰징의 가능성이 너무 높음. → L2에서 출금예정인 금액은 L2 Total TVL에서 빼는 것이 합리적임. 
      1. TRH팀에 출금예정 금액을 온체인에서 확인할 수 있는지 문의함. → NAM :  현재 없는데, 더 생각해보고 피드백을 주겠다고 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741933670884929)
      1. Nam 이 목요일까지 답변주기로 함 [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742259535922969?thread_ts=1741933670.884929&cid=C06UKCF86TE)
      1. 지금 반영이 힘들고, 나중에 대책이 마련되면 알려주시기로 함. [https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742524395904819?thread_ts=1741933670.884929&cid=C06UKCF86TE](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742524395904819?thread_ts=1741933670.884929&cid=C06UKCF86TE)
      1. 해머님에게 답장함. [https://tokamak-network.slack.com/archives/C08FB51CJG4/p1742524747882649?thread_ts=1741932606.024099&cid=C08FB51CJG4](https://tokamak-network.slack.com/archives/C08FB51CJG4/p1742524747882649?thread_ts=1741932606.024099&cid=C08FB51CJG4)
    1. 문의할 내용
      1. 계약날짜 (언제부터 작업하실 수 있는지) - 다음주 수요일부터 가능
      1. Omniscia 관련 작업 - 해당 내용에 대해서는 동의하셨고 261개의 피드백 모두하는것은 아닌 것 같아서 Minor이상 내용만 정리하여서 다음주 월요일날 내부 회의 후 Hammer님께 전달드리면 될 것 같습니다.
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1.  컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
      1. 컨트랙 배포를 위해서 해머님에게 옴니시아에서 수정한 사항에 대한 검토작업을 드렸으면 함.  검토기간을 해머님과 확인필요 
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백  
      1. [[Omniscia 최종보고서 비용추가]] 
1. 코드 통합 
  1. 제나 통합 브랜치 : 옴니시아+칼 + 해머 통합, 서틱 통합중. 
    1. [https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-merge)
  1. 하비 테스트 : [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
    1. DAO & MultiSigWallet
      1. npx hardhat test test/agenda/12.UpgradeDAOProxy-test-mainnet.js 
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
    1. 아젠다 배포 문서 [[Deploy TON-Staking-v2  on Mainnet ]] 
      1. 예상 가스비 적기 
      1. 컨트랙 배포 스크립트 만들기 
      1. 아젠다 제출 스크립트 만들기
      1. 배포 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 아젠다 할때, 13번 아젠다 No 투표해달라고 요청하기  
  1. 컨트랙트 배포일, 아젠다 생성일 각각 다 확인
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. ECO 커뮤니티 버전 개발용, TRH 개발용으로 사용함.  
  1. [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 이번주 주말까지 작업하기 
1. 블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-24

1. 오딧 진행 사항  
  1. Hammer
    1. 문의할 내용
      1. Omniscia Audit 확인 범위 결정
        1. [[Omniscia Audit result]] 
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1. 컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
      1. 컨트랙 배포를 위해서 해머님에게 옴니시아에서 수정한 사항에 대한 검토작업을 드렸으면 함.  검토기간을 해머님과 확인필요 
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백  
      1. [[Omniscia 최종보고서 비용추가]] 
    1. 추가 계약 연장이 아닌 대안으로 진행하기로 결정
  1. Zena님 피드백 사항
    1. MultiSigWallet Contract 콘솔로그 지우기,  함수나 스토리지에 주석 추가
      1. [https://github.com/tokamak-network/tokamak-multisig-wallet/commit/d53f72fa8ca6152da113448290e871be1d573859](https://github.com/tokamak-network/tokamak-multisig-wallet/commit/d53f72fa8ca6152da113448290e871be1d573859)
    1. DAOCommitteeOwner에서 추가 삭제해도 되는 함수 확인 및 적용
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/1de4e2e25789069b8a4e5dbcc7c2831f0202135e](https://github.com/tokamak-network/ton-staking-v2/commit/1de4e2e25789069b8a4e5dbcc7c2831f0202135e)
    1. DAOCommitteeOwner에서 daoExecuteTransaction함수 onlyOwner 및 to주소 확인
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/4dfd81a0818dc09c93011e780635c1645eeb5817](https://github.com/tokamak-network/ton-staking-v2/commit/4dfd81a0818dc09c93011e780635c1645eeb5817)
    1. Candidate 에러 발생
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/8d1ec0d4a1520dde4606bbd4cc21ddb4461e1fb3](https://github.com/tokamak-network/ton-staking-v2/commit/8d1ec0d4a1520dde4606bbd4cc21ddb4461e1fb3)
    1. 다오 설정함수 입력값과 스토리지 같으면 revert 추가
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/bc7f291d8b4092aa5fd71c19f709ac3cd3852b4c](https://github.com/tokamak-network/ton-staking-v2/commit/bc7f291d8b4092aa5fd71c19f709ac3cd3852b4c)
    1. 다오 setCooldown 이름 변경
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/91629964492a29cf8c1870d151203d0792d0c1a9](https://github.com/tokamak-network/ton-staking-v2/commit/91629964492a29cf8c1870d151203d0792d0c1a9)
    1. 다오에서 eth를 보낼 수 없어서 daoExecuteTransaction 함수 확인 및 onlyOwner 테스트 추가
      1. [https://github.com/tokamak-network/ton-staking-v2/commit/3b86b360cfa4e34c0d29eada2e35366030f46f4d](https://github.com/tokamak-network/ton-staking-v2/commit/3b86b360cfa4e34c0d29eada2e35366030f46f4d)
    1. 새로 배포한 코드로 테스트하기
    1. 배포시 필요한 가스 엑셀 문서에 추가 (멀티시그 월렛 컨트랙 배포 및 실행 함수 관련)
  1. Kevin 피드백 
    1. MultiSigWallet에서 사용하는 Interface 예제 필요
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서 [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 예상 가스비 적기 
    1. 컨트랙 배포 스크립트 만들기  
    1. 아젠다 제출 스크립트 만들기
    1. 배포 이후, 테스트 스크립트 만들기  
  1. 컨트랙 배포하기 
    1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 
    1. 메인넷에 컨트랙 배포 예정일 :  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
  1. 컨트랙트 배포일, 아젠다 생성일 각각 다 확인
    1. 해머님 코드 리뷰 완료일
    1. 컨트랙 배포일 : 3월 31일 
    1. 서틱에 요청 : 3월 31일  
    1. 아젠다 생성 및 제출일  :  4월 4일 아젠다 생성 
    1. 아젠다 투표일 : 4월 28일 
    1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. ECO 커뮤니티 버전 개발용, TRH 개발용으로 사용함.  
  1. 배포문서 : [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 배포 후, 개발환경 주소 공지하기 
  1. 톤스테이킹 기능 테스트 스크립트 실행 및 확인하기  
  1. 다오 기능 테스트 스크립트 실행 및 확인하기 
1.   블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-25

1. 오딧 진행 사항  
  1. Hammer
    1. Omniscia Audit 확인 범위 결정
      1. [[Omniscia Audit result]] 
      1. v2.5-audit-merge 브랜치 기준으로 해당 코드 링크 커맨트로 추가함. 
    1. 계약 업무 범위 확인
      - 테스트 코드 개선 (목표 달성률 30~50%)
        1. 커버리지 측정
        1. 100% 커버리지 달성
        1. 코드 오딧
      - Audit 피드백 확인 
    1. **Scope of Work**
      1. Improve and refactor test code to achieve a test coverage rate of 30–50%.
        1. Measure and report test coverage using appropriate tools.
        1. Increase test coverage to 100% where feasible.
        1. Conduct code audits to identify and address potential issues.
      1. Review and respond to the feedback from the Audit 
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1. 컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
      1. 컨트랙 배포를 위해서 해머님에게 옴니시아에서 수정한 사항에 대한 검토작업을 드렸으면 함.  검토기간을 해머님과 확인필요 
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백  
      1. [[Omniscia 최종보고서 비용추가]] 
    1. 추가 계약 연장이 아닌 대안으로 진행하기로 결정
  1. Kevin 피드백 
    1. MultiSigWallet에서 사용하는 Interface 예제 필요
1. 일정 
  1. 컨트랙 배포일 : 3월 31일 
  1. 서틱에 요청 : 3월 31일  
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 메인넷에 컨트랙 배포 및 서틱에 중앙화 취약점 재검토 요청(3월 31일)  
  1. [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 예상 가스비 적기 
    1. 컨트랙 배포 스크립트 만들기 : 배포된 컨트랙들의 오너가 DAO 여야 한다. 
    1. 멀티시그월렛 오너 3개 알아두기 
    1. 다오 오너가 멀티시그월렛을 오너로 주는 것도 월요일 작업 
  1. 다오 오너 EOA 를 오너에서 삭제 ?   
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서 [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. 배포문서 : [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 다오 기능 테스트 스크립트 실행 및 확인하기 
  1. oldDAO 배포 verify 
    1. [https://github.com/tokamak-network/verify-oldDAO](https://github.com/tokamak-network/verify-oldDAO)
1.   블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 
1. TRH 협업 
  1. Verification contract audit [문서](/1bbd96a400a3806e986aca30875c2933), [PR](https://github.com/tokamak-network/tokamak-thanos/pull/324) 

# 2025-03-26

1. 오딧 진행 사항  
  1. Hammer
    1. Hammer님 업무 진행속도를 높이기 위해서 [https://github.com/tokamak-network/ton-staking-v2/issues/75#issuecomment-2750695241](https://github.com/tokamak-network/ton-staking-v2/issues/75#issuecomment-2750695241) 이슈들 다음과 같이 변경 → 코드 머지 된 부분 이슈에 명시함 
    1. Hammer님 25.03.26일부터 업무 진행 중
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1. 컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
      1. 컨트랙 배포를 위해서 해머님에게 옴니시아에서 수정한 사항에 대한 검토작업을 드렸으면 함.  검토기간을 해머님과 확인필요 
  1. Omniscia
    1. 보고서 제출 : [https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view](https://drive.google.com/file/d/1JzPxI-ZdJPwZBHidTKxCdkDgcq1sIEe8/view)
    1. 늦은 보고서 제출로 인한 추가금 발생 피드백  
      1. [[Omniscia 최종보고서 비용추가]] 
    1. 추가 계약 연장이 아닌 대안으로 진행하기로 결정
    1. Omniscia와 커뮤니케이션 관련자료 남기기
      1. [omniscia.io](https://omniscia.io/reports/tokamak-network-ton-staking-v2-67bc7fe2ee4dd600185cd150/) (Omniscia 보고서)
      1. [Omniscia on Twitter / X](https://x.com/Omniscia_sec/status/1889721009311195529) (Omniscia 홍보)
      1. 각 페이지 스크린샷을 통해서 남기는 작업 진행 완료
      1. 계약서에 명시된 범위에 해당하는 컨트랙들에서 나온 이슈 개수 확인하기 
  1. Kevin 피드백 
    1. MultiSigWallet에서 사용하는 Interface 예제 필요
1. 일정 
  1. 컨트랙 배포일 : 3월 31일 
  1. 서틱에 요청 : 3월 31일  
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 메인넷에 컨트랙 배포 및 서틱에 중앙화 취약점 재검토 요청(3월 31일)  
  1. [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 예상 가스비 적기 
    1. 컨트랙 배포 스크립트 만들기 : 배포된 컨트랙들의 오너가 DAO 여야 한다. 
    1. 멀티시그월렛 오너 3개 알아두기 
    1. 다오 오너가 멀티시그월렛을 오너로 주는 것도 월요일 작업 
  1. 다오 오너 EOA 를 오너에서 삭제 ?   
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서 [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. 배포문서 : [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 다오 기능 테스트 스크립트 실행 및 확인하기 (작업 중)
1.   블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 
1. TRH 협업 
  1. Verification contract audit [문서](/1bbd96a400a3806e986aca30875c2933), [PR](https://github.com/tokamak-network/tokamak-thanos/pull/324) 

# 2025-03-27

1. 오딧 진행 사항  
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1. 컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
  1. Omniscia
    1. 오딧 산출물 폴더 생성 함  : [https://drive.google.com/drive/folders/1DKAoItbfTDiCKNBck1N6zVHt3i9HoQ4J](https://drive.google.com/drive/folders/1DKAoItbfTDiCKNBck1N6zVHt3i9HoQ4J)
      1. Omniscia와 커뮤니케이션 관련자료 남기기 
    1. 계약서에 명시된 범위에 해당하는 컨트랙들에서 나온 이슈 개수 확인하기  → 가격 산정할때는 오딧 범위가  [정확하게](/175d96a400a380779395cba6edc3bf0d) 들어갔는데, 계약시 git 전체로 계약되었음. 
  1. Kevin 피드백 
    1. MultiSigWallet에서 사용하는 Interface 예제 필요 : [https://github.com/tokamak-network/tokamak-multisig-wallet](https://github.com/tokamak-network/tokamak-multisig-wallet) readme에 설명 및 script 또는 test  파일 제공하고, 알려주기 (아젠다 작업 이후)
1. 오딧 관련 이슈 생성 
  1. 멀티시그 월렛 배포하고 다오 오너를 수정하는 것과 관련하여, 이슈를 만들어야 할것 같음. 그래서 git 이슈에 오딧 관련 이슈를 추가하고, 멀티시그 월렛으로 다오 오너 변경하는 것도 같이 추가해야 할것 같음. 
  1. 다오 오너 변경사항 X 에 공지해야 하는지 확인. → 월요일 변경하고 케빈에게 여쭤보기 , 거래소 정보제공과 관련 하여 중요한 사항일 수 있음.  
1. 일정 
  1. 컨트랙 배포일 : 3월 31일 
  1. 서틱에 요청 : 3월 31일  
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 메인넷에 컨트랙 배포 및 서틱에 중앙화 취약점 재검토 요청(3월 31일)  
  1. [[Deploy TON-Staking-v2  on Mainnet ]] 
    1. 예상 가스비   
      - 다오 오너 계정 : 0xB4983DA083A5118C903910DB4f5a480B1D9f3687 ( 78,381 gas, 0.0002506 ETH 필요 , gasPrice: 5gwei 기준) )
      - 멀티시그월렛의 오너 계정 3개 ( 계정당 .. 가스비 필요)
      - **컨트랙 배포 가스비 : 38,868,869 gas , 0.194344345 ETH ( gasPrice: 5gwei 기준)**
    1. 컨트랙 배포 스크립트 만들기 : 배포된 컨트랙들의 오너가 DAO 여야 한다. 
    1. 멀티시그월렛 오너 3개 알아두기 
    1. 다오 오너가 멀티시그월렛을 오너로 주는 것도 월요일 작업 
  1. 다오 오너 EOA 를 오너에서 삭제 ?   
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 
  1. 케빈에게 공유 가스비 및 계정, 작업 일자 공유하기 
    - 일시: 2005년 3월 31일 월요일 오후 2시
    - 작업 내용 :
      - 멀티시그 월렛 컨트랙 배포
      - 다오의 오너EOA를 멀티시그월렛 컨트랙으로 변경
      - 톤스테이크 V2 오딧한 컨트랙 배포 및 각 컨트랙 오너를 다오로 변경
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. 배포문서 : [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 다오 기능 테스트 스크립트 실행 및 확인하기 (작업 중)
1.   블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-28

1. 오딧 진행 사항  
  1. Certik
    1. CON-01  메인넷 배포된 주소로 확인을 해야한다고함.
      1. 컨트랙을 먼저 배포해서, 오너를 수정하고, 다시 검토요청을 해야 할것 같음. 
  1. Kevin 피드백 
    1. MultiSigWallet에서 사용하는 Interface 예제 필요 : [https://github.com/tokamak-network/tokamak-multisig-wallet](https://github.com/tokamak-network/tokamak-multisig-wallet) readme에 설명 및 script 또는 test  파일 제공하고, 알려주기 (아젠다 작업 이후)
1. 오딧 관련 이슈 생성 
  1. 멀티시그 월렛 배포하고 다오 오너를 수정하는 것과 관련하여, 이슈를 만들어야 할것 같음. 그래서 git 이슈에 오딧 관련 이슈를 추가하고, 멀티시그 월렛으로 다오 오너 변경하는 것도 같이 추가해야 할것 같음. 
  1. 다오 오너 변경사항 X 에 공지해야 하는지 확인. → 월요일 변경하고 케빈에게 여쭤보기 , 거래소 정보제공과 관련 하여 중요한 사항일 수 있음.  
1. 일정 
  1. 컨트랙 배포일 : 3월 31일 
  1. 서틱에 요청 : 3월 31일  
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 메인넷에 컨트랙 배포 및 서틱에 중앙화 취약점 재검토 요청(3월 31일)  
  1. 배포문서에 케빈이 실행할 내용 적었는지 확인, 컨트랙 배포 및 배포된 컨트랙들의 오너가 DAO 인지 확인하는것 추가하기  
    1. [[Deploy TON-Staking-v2  on Mainnet ]] 
  1. 케빈에게 공유함
    - 일시: 2005년 3월 31일 월요일 오후 2시
    - 작업 내용 :
      - 멀티시그 월렛 컨트랙 배포
      - 다오의 오너EOA를 멀티시그월렛 컨트랙으로 변경
      - 톤스테이크 V2 오딧한 컨트랙 배포 및 각 컨트랙 오너를 다오로 변경
    - [@Kevin](https://tokamak-network.slack.com/team/U04E2KL62RZ) 준비할 계정과 필요한 가스비
      - **다오 오너 EOA 계정 **:
        - **0xB4983DA083A5118C903910DB4f5a480B1D9f3687**
        - 필요한 가스 : 78,381 gas, 0.000548667 ETH 필요 , gasPrice: 7gwei 기준
      - **멀티시그월렛에서 사용할 오너 계정 3개**
        - 제안서 제출하는 계정이 필요한 가스
          - 필요한 가스 : 216,665 가스 , 0.001516655 ETH 필요, gasPrice: 7gwei 기준
        - 제안서 컨펌하고 실행하는 계정에서 필요한 가스
          - 필요한 가스 : 140,670 가스, 0.00098469 ETH 필요, gasPrice: 7gwei 기준
      - 컨트랙 배포 및 권한 변경에 필요한 가스비
        - 38,868,869 gas , 0.272082083 ETH , gasPrice: 7gwei 기준
        - 사용하고 남은 것은 환불할 것임.
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 ⇒ 검토가 되는지 바로 확인하기, 안되면 아젠다까지 제출하고 검토요청해야 할 수 도 있음. 
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
1. 톤 스테이킹 개발 테스트 환경 구축  (sepolia환경) 
  1. 배포문서 : [[Building TON Staking Development  Environment on Sepolia ]] 
  1. 다오 기능 테스트 스크립트 실행 및 확인하기 - 완료
1. 해머님 이슈 리포팅 피드백  
  1. [https://github.com/tokamak-network/ton-staking-v2/issues/304](https://github.com/tokamak-network/ton-staking-v2/issues/304)
1.   블로그 준비하기 
  1. 오딧 수행시, 체크리스트 추가하기 

# 2025-03-31

1. 일정 
  1. 컨트랙 배포일 : 3월 31일 
  1. 서틱에 요청 : 3월 31일  
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 메인넷에 컨트랙 배포 및 서틱에 중앙화 취약점 재검토 요청(3월 31일)    
  1. [[Deploy TON-Staking-v2  on Mainnet ]] 
  1. 컨트랙 메인넷에 배포 후, 서틱에 주소 제출하고 검토요청하기 ⇒ 검토가 되는지 바로 확인하기, 안되면 아젠다까지 제출하고 검토요청해야 할 수 도 있음. 
1. 오딧 관련 이슈 생성 
  1. 멀티시그 월렛 배포하고 다오 오너를 수정하는 것과 관련하여, 이슈를 만들어야 할것 같음. 그래서 git 이슈에 오딧 관련 이슈를 추가하고, 멀티시그 월렛으로 다오 오너 변경하는 것도 같이 추가해야 할것 같음. 
  1. **다오 오너 변경사항 X 에 공지해야 하는지 확인. → 월요일 변경하고 케빈에게 여쭤보기 , 거래소 정보제공과 관련 하여 중요한 사항일 수 있음.  **
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 13번 아젠다 No 투표해달라고 요청하기 
    1. 아젠다 제출후, 이슈 만들기. 
1. 해머 작업
  1. 옴니시아 [이슈 모두 검토 및 클로징](https://github.com/tokamak-network/ton-staking-v2/issues) 완료  
  1. 관련 피드백 커밋 완료 후, [v2.5-audit-merge](https://github.com/tokamak-network/ton-staking-v2/commits/v2.5-audit-merge/) 브랜치를 [v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/commits/v2.5-audit-agenda) 브랜치에 머지함.  
  1. TRH 의 검증컨트랙 내부오딧에 관심있음. 
1.   블로그 준비하기 
  1. 오딧 수행시, [체크리스트](/1bbd96a400a38043a479c3a64e5b5c49) 추가하기 
1. Sepolia 퍼블릭 버전 컨트랙 업그레이드 하기 → 아젠다 올리고 나서, 

# 2025-04-01

1. 일정 
  1. 3월 31일 : Certik에 중앙화 취약점 이슈 피드백 전달 [[Certik Centralization Risks]]
  1. 아젠다 생성 및 제출일 : 4월 4일 아젠다 생성 
  1. 아젠다 투표일 : 4월 28일 
  1. 아젠다 실행일 : 4월 28일 / 서비스 반영일 
1. 오딧 관련 이슈 생성 
  1. [https://github.com/tokamak-network/ton-staking-v2/issues/308](https://github.com/tokamak-network/ton-staking-v2/issues/308)
  1. 칼님과 해머님께 직접 최종 보고서 댓글로 올려달라고 요청함. 
1. Certik 의 중앙화 취약점 해결 관련 이슈를 만듬 
  1. [https://github.com/tokamak-network/ton-staking-v2/issues/309](https://github.com/tokamak-network/ton-staking-v2/issues/309)
  1. 댓글에, 이 취약점 해결을 위해 멀티시그 월렛 배포 한 내용 적어어야 함. 
  1. 다오의 오너를 멀티시그 월렛 으로 변경한 내용 기재해야 함.  
  1. 이 이슈를 근거로, 다오 오너를 멀티시그 월렛으로 변경한 내용 공지하기, tokamak dev 채널에 공지하기
    1. [https://tokamak-network.slack.com/archives/C07JU4P56MR/p1743488468349029](https://tokamak-network.slack.com/archives/C07JU4P56MR/p1743488468349029)
  1.  X에도 공지하기, 공지하기 전에 검토자를 제이슨님과 하비님 지정해서 검토하기   
    1. [https://tokamak-network.slack.com/archives/C07JU42NK9R/p1743491642472869?thread_ts=1743491102.854039&cid=C07JU42NK9R](https://tokamak-network.slack.com/archives/C07JU42NK9R/p1743491642472869?thread_ts=1743491102.854039&cid=C07JU42NK9R)
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. sepolia:  아젠다를 이용한 배포 / 테스트 준비 (멀티시그월렛 포함)
  1. mainnet: 아젠다를 이용한 배포 / 테스트  준비 (멀티시그월렛 포함)
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
  1. 아젠다 제출 이슈 생성하기 
    1. 아젠다 제출후, 이슈 만들기. 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
1. 채널에 케빈에게 [https://dao.tokamak.network/#/agenda/13](https://dao.tokamak.network/#/agenda/13) 를 투표를 거절로 해달라고 요청하기 
  1. 다오 Candidate 페이지 정상동작 확인함. 
  1. 케빈에게 투표해달라고 요청함 .[https://tokamak-network.slack.com/archives/C08B3V360R1/p1743491847339909](https://tokamak-network.slack.com/archives/C08B3V360R1/p1743491847339909) 
  1. 투표 완료후에 해당 트랜잭션 댓글에 명시하고,  [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59) 닫기. (안건종료되었으므로, 닫는다는 문구 추가하기 )
1. 해머 작업
  1. 매주 화요일 오후 9시 정기 미팅 
1.   블로그 준비하기 
  1. 오딧 [체크리스트](/1bbd96a400a38043a479c3a64e5b5c49) 만들기  
1. Sepolia 퍼블릭 버전 컨트랙 업그레이드 하기 → 아젠다 올리고 나서, 
1. 톤 유통량 문서 업데이트 함  [https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004](https://docs.google.com/spreadsheets/d/1-4dT3nS4q7RwLgGI6rQ7M1hPx9XHI-Ryw1rkBCvTdcs/edit?gid=681869004#gid=681869004)

# 2025-04-02

1. 일정 : 캘린더에 일정 등록하기 
  - 4월 4일 금요일 4시 예정 
    - [[Propose an agenda on Mainnet after auditing]] 
    - TON Staking V2 및 다오 업그레이드 아젠다 등록 
    - 다오 웹페이지에서 아젠다(내용) 확인 ,  
  - 아젠다 투표가능한 날짜 : 4월 20일 → 4월 21 일 오전 10시 채널에 케빈에게 투표요청 
  - 아젠다 실행일 : 아젠다 투표시작한 날짜 + 3일 : 4월 24일 (4월 21일날 투표진행되었을 경우)
  - TON Staking V2 서비스 오픈일 : 4월 29일
1. Certik 최종 보고서 받음  
  1. Certik  최종 보고서 검토 후, 승인 서명 해야 함 → 승인함 
> Hi @Zena Park (Tokamak Network Admin), @JaeSeung Hwang (Tokamak Network Admin), @Harvey Jo (Tokamak Network Admin)
> 
> The newer version of the final report is ready. Please review, confirm and sign off the report for publishing.
> 
> It would take 1-2 business days to publish and you would be notified via email when it is done.
> 
> Findings summary: 12/15 resolved, 0/15 pending.

[REP-final-20250401T084012Z.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/267a677b-2f6d-471a-ab24-cda2b26273a6/REP-final-20250401T084012Z.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VFKNDS6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfALDuFe9BZzMztWzUrBVj12CZifB%2FNRKSzEpDCZdBsAIgGpk%2BYSHjUYCXQEUbeEbuuMXX9VlwAxbVh9MBbUsBfv0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMNwB0R7jmgw7FYMNCrcA3iVdwFJhLZcqUq6zOv9sRf8aUvttpOcktDp09lm0AHHPyvPHjONAI6HjNkziT9IQveYKlFPEeRpfAf%2Fw2i0ePBg2POJOtMI871JSDVLrZQ75VMMjssDvTEBC6AZxl2R4dafUhcGL%2BgQle9D8%2FqyaKd2AUfF3m9rHy%2BrPmva4XY168n7W9l3tOKoSPs%2B972c9itCh0ICLbsy1F4547nDTvGWeiQrFBx61%2B1TBZ31CRoJyNU%2BDYwvFEQ4RaawIHX6Vs8TSJaO5iKtyMcHY9jI2F3Ak%2BPBNR6wNs98aj05ujgXiXZ2WsxX2Aw1un%2FgnMMFCHKq2cXgTFA7JZFOs%2BNtfcLSHYjBhYuhzNQHEXOYlKOIOkLX4%2BnEPP5i0ev0kLRikBxqaWfKLMET5rRPvEk%2Bes1mqUFor1eLiYIEGlZaiGYKm9bqJqSljJiABDgev4Sln0Mibhw4OKaHY8%2FukiwVotvMtw51Ot5ZTVF3ljTgbBuxlvCQwFtAi7MnMx8ngRFL4to1IBxfmH9WsAB53FbR7SQGYNCkLUKT9ghnrflMI9uYLkWXUM2YkhKX88yc8gdBjUqmRr6RFJ3ntBuevA0l3FCvcrs6GfiyKLx8J7MWaRHQAtR%2BopBTXf0qxxtmMNWa28wGOqUBsNFMnCnKx9yJaX6bgm737%2FhSxlbBXZvYXdUNs2Aqy1I%2Bn9%2BlfhM9Cyv2673GWgxS46RaqQ5pRL%2FYr3lupyvpxh9yRzfMWkBmhFMEFe36hrlTdfiO%2BtvX7MDOUwLWZozXB3i5b2VtMrqYvd4vx2lNSgpdBMqYkjyXP4TrfycKnYat2JnoF%2BTXyNRWUjY%2FHiVz%2FRVPrxQYCdQByBB137DS2ApQuL1g&X-Amz-Signature=ff10126b13a30bcc013a6e6056bcb0cfef321921dc58c9af1ad15de0f84f2964&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. CertiK 리더보드에 최종 보고서를 게시하고 웹 또는 소셜 채널에서 공유하도록 설정선택함.
  1. **Request Emblem for Your Website (?)**
    1. [https://skyharbor.certik.com/audits/projects?projectId=e56e3bff-25d9-4be5-9a56-dc12a27994a8&edit=0](https://skyharbor.certik.com/audits/projects?projectId=e56e3bff-25d9-4be5-9a56-dc12a27994a8&edit=0)
  1. **무료 버그바운티 설정할 수 있음. **
  1. 계정 프로필 검토 및 작성. 계정 프로필은 최종 보고서에 포함됩니다. 항상 ACCOUNTS 탭에서 수행할 수 있습니다.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/692e2869-d208-49ab-8733-0629d2f55908/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-02_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.16.15.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPFYIWVJ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHaVIVO2SFq5rCRgyNevdCeKzcvE4GK1Ka9qB9tnMNgzAiEAzpqmeJ%2Fj8c%2BDyfOi7pTJ5%2FCf2ITsl65P%2FkpJ%2Fw2FQ0Aq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDGb5kqEewVEfgnRpkSrcA8qV0%2FEvVipMj%2BxKQaV2zhMrMeVvYpXKa2b%2BvYxyb%2BZzIXwT%2BnG985b%2BW227StjKTavxhbAF7Y4ETHDNZu0t46O01Srvvjl7%2F6dcc6dg9r49aLZBaYkONrKCXi%2FPM%2FRlk%2Bb70h%2FaxxZZboGhqrCWuGLlk2HMbqXxk9Bp3m%2FPds1TlJaecipkV%2F1uI%2BoM%2BbHGt9ZNWab1GGn1cBxcZp0x9eZFZhkd3sqrK2ToHMzhf8me%2Bsu2HpJG4Cp8zcq9zxBULmb8mr8NM3p9EFmo7AmrP0sVyVl4TVyczbtmtqva4BONZS%2B2cXE4pP3oX4mLfHAOmPeKaGg4ByBaYY43lpu7sZppvK5JMyczQoZ%2Fx0Ks3kmjT7eksP6tUF4ZFLNj39NsavkuBAeMoLv6Qqlnj7S91RbPaO%2Bru3r9tdEOgKWx0OErJo%2BzTUuxjTX8EOOZxmlbplDTXGskTydIn5HU2GG0vWUpwtYb%2Bvmlplc0ap1yaOScoYiv%2BSTWy0xp372SyUL7N0ZJIuON5u15pMkuS0UyF02%2BHZSxI%2F%2ByjvxALGNiY1hArHLUBWTCPT1gpGFoJgim9PzcsZTrC1HLWWJdAQKGC9q35MNRo%2FLOrHxfi6xDPeS6ZKdK55sKVj5BDF98MP2Y28wGOqUBnX9oJp09Utc3ZPk4D8uuB%2FI9ai0JUGc3b26eXFkhGXVLS9wb5UIY8ocjBEXyzIO0FoaNc5PQmuaXonpeOVEnXfQ3UuaQAd2gXPlN4dHkCYCaqZ3Mg3fz2m7BrogqC4UP8aemAm5m5rSPTubI8xV26DxuoudFFSWiCaKEKDwQ4Xxvicabads%2FodZuesfgkoQU2AoRGZQVIPy%2FIlhE2KVpW6dzXa4b&X-Amz-Signature=0670ecb1b5fe4ef2e8d76df36e6f64c5dd5c9f5c98250715396a0eeda0cbd4c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1.  X에도 공지하기, 케빈에게 요청함    
  1. [https://tokamak-network.slack.com/archives/C07JU42NK9R/p1743491642472869?thread_ts=1743491102.854039&cid=C07JU42NK9R](https://tokamak-network.slack.com/archives/C07JU42NK9R/p1743491642472869?thread_ts=1743491102.854039&cid=C07JU42NK9R)
  1. 오딧 블로그 글이 나오므로 X공지는 따로 안하기로 함.
1. 아젠다 제출 준비하기   
  1.  브랜치 [GitHub - tokamak-network/ton-staking-v2 at v2.5-audit-agenda](https://github.com/tokamak-network/ton-staking-v2/tree/v2.5-audit-agenda)
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
    1. 아젠다 제출 스크립트 만들기
    1. 배포 주소를 활용해 아젠다 승인 이후, 테스트 스크립트 만들기  
      1. [https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/agenda/23.AgendaPassTest(25.03.31)-mainnet.js](https://github.com/tokamak-network/ton-staking-v2/blob/v2.5-audit-agenda/test/agenda/23.AgendaPassTest(25.03.31)-mainnet.js)
      1. npx hardhat test test/agenda/23.AgendaPassTest\(25.03.31\)-mainnet.js 
      1. Staking V2 Test : 
`npx hardhat test test/layer2/units/9.dao-staking-v2.5.after.deploy.mainnet.test.ts`
  1. 아젠다 제출 이슈 생성하기 
    1. 아젠다 제출후, 이슈 등록하고, 아젠다 설명 수정  → 다음주 월요일 전까지 
    1. 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
1.  케빈에게 [https://dao.tokamak.network/#/agenda/13](https://dao.tokamak.network/#/agenda/13) 를 투표를 거절로 해달라고 요청하기 
  1. 케빈 투표 완료후에 해당 트랜잭션 댓글에 명시하고,  [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59) 닫기. (안건 종료되었으므로, 닫는다는 문구 추가하기 ) 
  1. [https://tokamak-network.slack.com/archives/C08B3V360R1/p1743491847339909](https://tokamak-network.slack.com/archives/C08B3V360R1/p1743491847339909)
1.   블로그 준비하기 : 서비스  오픈 (아젠다 실행일) 전까지 작성 
  1. 오딧 [체크리스트](/1bbd96a400a38043a479c3a64e5b5c49) 만들기  :  
1. 다오 제안페이지에서 추가되는 함수 정리
  1. [[Add Functions on DAO Proposal page ]] 
1. 프론트 컨트랙 가이드 수정사항 있는지 확인하기 
  1. [[[For Service] Interface for giving seigniorage to CandidateAddOn’s OperatorManager ]] 
  1. sdk에 사용하고 있는 문서도 보강하기 [[TON-Staking-SDK]] 
1. Sepolia 퍼블릭 버전 컨트랙 업그레이드 하기 
[[5-Redeploy TON-Staking-v2 on sepolia  (using agenda)  ]] 

  1. Sepolia에 컨트랙 배포함.
  1. 아젠다 제출 → 4월 3일 4시 ,
    1. 프론트 다오 웹페이지에서 안건 확인
  1. 프론트 다오 웹페이지의 설명 화면은 → 4월 4일  

# 2025-04-03

1. 일정 : 캘린더에 일정 등록하기 
  - 4월 4일 금요일 4시 예정 
    - [[Propose an agenda on Mainnet after auditing]] 
    - TON Staking V2 및 다오 업그레이드 아젠다 등록 
    - 다오 웹페이지에서 아젠다(내용) 확인 
  - 아젠다 투표가능한 날짜 : 4월 20일 → 4월 21 일 오전 10시 채널에 케빈에게 투표요청 
  - 아젠다 실행일 : 아젠다 투표시작한 날짜 + 3일 : 4월 24일 (4월 21일날 투표진행되었을 경우)
  - TON Staking V2 서비스 오픈일 : 4월 29일
1. Certik 최종 보고서 받음  
  1. Request Emblem for Your Website (?)
    1. [https://skyharbor.certik.com/audits/projects?projectId=e56e3bff-25d9-4be5-9a56-dc12a27994a8&edit=0](https://skyharbor.certik.com/audits/projects?projectId=e56e3bff-25d9-4be5-9a56-dc12a27994a8&edit=0)
  1. 무료 버그바운티 설정할 수 있음.** **
1. 아젠다 제출 준비하기   
  1. 아젠다 배포 문서[[Propose an agenda on Mainnet after auditing]] 
  1. 아젠다 제출 이슈 생성하기 → 다음주 월요일 전까지 
    1. 아젠다 제출후, 이슈 등록 : 참고, [https://github.com/tokamak-network/ton-staking-v2/issues/59](https://github.com/tokamak-network/ton-staking-v2/issues/59)
    1. 이슈 생성후, 다오 아젠다의 설명 수정하기  
1. Sepolia 퍼블릭 버전 컨트랙 업그레이드 하기  4월 3일 
  - [[5-Redeploy TON-Staking-v2 on sepolia  (using agenda)  ]] 
    - Sepolia에 컨트랙 배포함. 
    - L2초기화함. 웹페이지에서 L2 태그 사라지는지 확인함.
  - sepolia 아젠다 제출 후, 웹페이지 확인함 
  - 프론트 다오 웹페이지에서 안건함
  - 프론트 다오 웹페이지의 안건 설명 화면 편집 확인함
1.   블로그 준비하기 : 서비스  오픈 (아젠다 실행일) 전까지 작성 
  1. 오딧 [체크리스트](/1bbd96a400a38043a479c3a64e5b5c49) 만들기  :  4월 11일 까지 
  1. 1차 초안  :  4월 16일 까지 
  1. 리뷰 마감 : 4월 18일 까지 
  1. 블로그 공지 :   4월 24일 
1. 프론트 컨트랙 가이드 수정사항 있는지 확인하기 
  1. [[[For Service] Interface for giving seigniorage to CandidateAddOn’s OperatorManager ]] 
  1. sdk에 사용하고 있는 문서도 보강하기 [[TON-Staking-SDK]] 

# 2025-04-04

1. 일정 
  - 4월 4일 금요일 아젠다 제출
    - [[Propose an agenda on Mainnet after auditing]] 
    - 아젠다 생성 X에 포스트 
  - 4월 21일 
    - 아젠다 투표 가능 시작일
    - 아젠다 투표 X에 포스트
    - 오딧 내용 블로그 공지  
    - 스테이킹 V2의 업데이트 주요 내역 블로그 공지 
  - 4월 24일 
    - 아젠다 실행 가능일  
    - 아젠다 실행 X에 포스트
  - 4월 29일
    - TON Staking V2 서비스 오픈
    - TON Staking V2 서비스 오픈 X에 포스트
    - DAO proposal 웹에 추가된 기능 업데이트  
1. Certik 최종 보고서 받음  
  1. Request Emblem for Your Website  클릭함. 
  1. 무료 버그바운티 설정할 수 있음.** → 아직 요청 안함. **
  1. 보안 점수를 올릴수있는 방법을 문의함. 텔레그램 채널 
1. 옴니시아 
  1. 텔레그램 채널(견적받은 사람) 과 슬랙채널(오딧해준 사람)에 컨플레인함 
    1. 문의 : 우리가 요청한 견적보다 많은 범위의 견적을 해서, 예상보다 많은 취약점이 발생했고, 이로인해, 추가 예산없이 보고서를 못받는 상황이 되었다. 이렇게 상황이 되도록 왜 제안 범위 이외의 컨트랙을 오딧에 포함했는지 이해할 수 있게 설명해달라.
    1. 추후 방향성 : 옴니시아를 신뢰하고 있기에 거금을 들여 오딧을 했다. 계약부터 신뢰할수없다면 누가 오딧결과를 신뢰할수 있겠는가. 앞으로 이런일이 발생할수도 있을텐데, 안좋은 사례로 남지 않게 하는게 좋지 않겠는가? 우리가 제안한 범위만으로 보고서를 받을 수 있게 해달라.
1. 아젠다 제출 , 이슈 등록 
1.   블로그 준비하기 : 서비스  오픈 (아젠다 실행일) 전까지 작성 
  1. 오딧 내용 블로그 
    1. 오딧 [체크리스트](/1bbd96a400a38043a479c3a64e5b5c49) 만들기  :  4월 11일 까지 
    1. 1차 초안:  4월 16일 까지 
    1. 리뷰 : 4월 18일 까지 
    1. 공지 : 4월 21일 까지 
  1. 스테이킹 V2의 업데이트 주요 내역 블로그
    1. 1차 초안  :  4월 14일 까지 
    1. 리뷰 : 4월 18일 까지 
    1. 공지:  4월 21일  까지 
1. 다오 웹 proposal [[Add Functions on DAO Proposal page ]] 
  1. 추가 함수 문서 작성 :   4월 11 일 
1. 프론트 컨트랙 가이드 수정사항 있는지 확인하기 
  1. [[[For Service] Interface for giving seigniorage to CandidateAddOn’s OperatorManager ]] 
  1. sdk에 사용하고 있는 문서도 보강하기 [[TON-Staking-SDK]] 

## Certik

보안점수올릴수있는 방법
**Missing Items from our System:**

**Code Security Factors:**

1. Please resolve any outstanding findings by responding through our SkyHarbor platform. Our auditors will assist with reviewing your comments and make the necessary updates to your audit report.

2. Please provide the link to any past audit reports.

**Fundamental:**

1. Please provide us with a link to past Fundraising rounds that were completed by your company. (i.e. News article that shows investors and amount invested).

**Operational:**

1. Please ensure major website settings such as: proper FTP port configurations, HTTP to HTTPs traffic redirection, proper certificate configurations (common certificate issues: Self-signed certificate, Wrong host certificate, Expired certificate), as well as DNS Health records such as DMARC, DKIM, SPF are configured properly.

**Additional ways to improve your score:**

- Team Verification: Enhance your community trust and transparency while keeping your team completely anonymous with our CertiK’s fast and simple third-party team verification.

- Bug Bounty Program: Please provide bug bounty program information. (If you do not have one,  bug bounty services are offered by major providers such as CertiK or Immunefi)

  - Bug Bounty Price; 3k USD

[Bug Bounty One Pager  (1) .pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c06f4301-a3a0-4f9b-9e41-83c9baf0ba5b/Bug_Bounty_One_Pager__%281%29_.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6MYV6HW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8%2BKpyYMi6UvuGOjsEAPEBkNCZRpGaWYilc5FOoFVQ4AiA5v8YeD8Hr0tBVVZSKSWPBUbNz54SoNuXw%2F%2F8zKzzhYCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM81v0shpBOTYCHRkNKtwDQ4MHWo2btaKBMy4KXL%2BTkrWV1Q8eprXBBYmFN43KtUNZxUNVpFIVLD61nrOUBRWLYtDxP8ZmGKPVhxIrla4gmnQWZVgZ0B5r3mlhbvvGTyio1kbO%2B60vZ8LniAhtA9IpWCXU4Ii1fDwUa3OhtWazy8CGWGcvcqJV4LxWUzc33iYYgQyXLZKWEdruDDbYpuX0WF4L1VkGoaoJGCJ4mizLdZYZg2vOGSYzDelLN7XvFERVOE9yYcfQEX9KBIuTteTwFEvRnyFiFHtHcMU8ksLVlYbcirSb1LjYlNBZ%2F4EaSRvXs01qgIHoTSqvaWhBo1ezNlRSLu%2B3ak1pfYjiulM8Jn7MTiVMe9xuGHDUTsVmRxgplvA2vNOiFIiQ3AC%2BJwHz5fEO98ey9H964XCa9wk%2BqXLIIxwZpp7hMxHrdYtNwsljyLBw8LNiY8mLJEeqx66dj9L%2BTyQ1t9WX3H%2BHZO4b6O7kIknOSx2a6TZ4fuYdwMJdtbtmI6bCxEhl%2FsDRmJ5d5nTwGRQGEiouOgXG6b2rK6Vr%2FpF9GPtuK30ZlJC8x%2FO6hJIJL%2FgKg4BW8a%2FzBfPzTk3QZ2RTE1Tp1U0BMJkfIz6guXOE4cyd9DZ5gLQR62EWsSDyIviX0Pyd%2FNswtpjbzAY6pgGrdC27sDhfSG8YLYFPhZ3oQ%2FlrJ7t2KIrusjPNMC9jfxyvLKkuJpeBMUHV7Fg6WwvnkgCmGXKZllLaF9CVPtsRKbIefBNgHrm%2BVC%2BgUNuO3ukvNMwCBmid8uEsc0NIxNtXHVYp5RXqTuOTd1%2FqFTh%2BPrAKC9vsipNr2kMrblMUDJsl5438%2FOsam3fxGBp2PT2L7Dmt8l6jDaL5vMGtD2GqPnMFjGsb&X-Amz-Signature=94967543eb42662ff35732402783729dfb4280271109fcae31d5039c4d97ac35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Contract Verification: CertiK conducts a contract verification on your deployed contract(s), and we'll grant you a CV Badge if the deployed code 100% matches with what we audited. (Operational Resilience)

### 블로그 준비하기  

Audit결과에 대한 Report(기사)가 있었으면 좋겠다.

- 발견, 개선, 수치적으로 어떤 것들이 개선되었는지 포함 
- 개선된 내용들 주요 사항들
- 정책적인 사항들
- 마이너한 사항들은 보고서로 대체
- 추후에 결과물이 생태계에 미칠 영향 

ex) 시뇨리지 로직이 어떻게 변경되었기 때문에 앞으로 이렇게 하는게 유리하다 (최종적으로 Audit을 진행해준 모든 기관들 감사하다)