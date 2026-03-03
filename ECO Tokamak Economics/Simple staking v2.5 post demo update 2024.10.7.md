### Frontend 

- L2 tab
- [ ] L2 Bridge url, block explorer url, L2 logo → 컨트랙트와 연결 해제, 일단 직접 받고 추후에 PR시스템으로 변경 
- [ ] L2 DAO candidate가 아니면 
- [ ] L2 DAO candidate 이면
- Withdraw modal
- [ ] Unstake + Withdraw에 History 내역이 안뜸 

---

추가 고려대상 (디자인팀과 논의후 공유 예정)

- *Withdraw modal*
- [ ] *L1 Withdraw history, subgraph 없이 내역 들고 오기 *
- *event + filtering을 통해서?*
  - *bridge address + deposit address 기준 가능? *
  - *로딩 UI 추가? *
- [ ] L2 tab 추가 정리
- [ ] DAO candidate 페이지 정리
- [ ] Staking status

### Design

- L2 tab
- [x] Sequencer seigniorage
- [x] L2 tab (L2 운영자가 아닌 기준) → Earned seigniorage 삭제 

L2 tab (L2 운영자 화면) 
- [x] L2 tab (L2 운영자 기준) → Earned seigniorage, 숫자 1개만 보여주기 (지금은 xxx TON / yyy TON 보여줌) 
- [x] TON locked in Bridge (Actual/Registered) 
- [ ] L2 운영자 화면 @Unknown 
  - Operator view → Claimable seigniorage modal
- [x] Claim
- [x] Stake → 합을 보여줘야됨 
- [x] Claim & Stake modal @Unknown 

- 공통 (Overview + L2 tab) 
- [x] L1 contract address 개편 (컨트랙트팀) → sectioning, tooltip, 이더스켄 링크 바로가기 
- [ ] 모달 워닝 간결화  (Suah)
- [ ] DAO candidate 페이지 정리 (Suah) [https://sepolia.dao.tokamak.network/#/election/0xa6b4da13c80d4d3644e990f2f872d72e617f9dd0](https://sepolia.dao.tokamak.network/#/election/0xa6b4da13c80d4d3644e990f2f872d72e617f9dd0)
- [x] Staking Status and information ([https://app.aave.com/staking/](https://app.aave.com/staking/))
- 문구 업데이트  (Suah): 
  - (L2 내용 추가) Choose a DAO candidate to stake, restake, unstake, or withdraw TON (or WTON).
- UI 추가
  - Average APY (?)
    - ~30.40%
  - Total staked (?)
    - 10,594,766 TON 
  - Seigniorage emission (?)
    - ~28,224 TON per day
      - Staker 30% → S/T + 0.5*(T-S)
      - DAO 20%→ 0.1*(T-S)
      - sTOS holder 50% → 0.4*(T-S)
- [x] Staking Status Information & UI 추가 @Unknown 
  - tool tip 추가

![](images/afeed0eb6439.png)

![](images/84cdc98a6eb2.png)

- [x] Tool tip 추가 @Unknown 
- [x] Add Step 1: Unstake Step 2: Withdraw

![](images/7e5865dbd38a.png)

- [x] design: [Link](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Simple-staking?node-id=14-2740&node-type=frame&t=dMrNnhj7Xr66Y7kM-11) @Unknown 

![](images/5e21d3cbd85f.png)

- [x] 명칭 변경, tooltip 추가, 
- [x] Stake modal
- [x] Withdraw modal

### Contract 

- [ ] ~~RollupConfig 등록 → DAO로 permission으로 등록~~  
- [x] **registerRollupConfigByManager → _name 삭제 **
- [x] 중복체크 제거 
- [ ] ~~RollupConfig 등록 → ~~아직 오픈이 될수 없다라고 외부에 공유가 되어야한다. upgradable 권한에 대해서 완료해야함 (테스크 추가) 
- [x] Claim할때 TON 또는 WTON 선택 가능 → 점검 하고 문제가 있으면 공유 
- [x] L2 Bridge url, block explorer url, L2 logo contract data storage 삭제 

### Model

- [x] L2 tab 정보 정리 
- [x] L1 contract address 개편 (컨트랙트팀)
- [ ] Add Step 1: Unstake Step 2: Withdraw

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6988f9d1-121c-474f-a4c3-eb4cfb71fac0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665BXT7QV%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T084946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyR%2B5iq4SBWxUy%2FH1s9mXEGctdXzIaXoLtzDQvJr3ICQIgWuFeOjmIx%2BX41HTckSKeSV%2B882uPjFUg5C%2BBPCAkDL8q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAfjyvqOwAmDx5b0tCrcAx1ys%2BUi6bI5qxg0vgBtz5ZYuguBW5eSvXQ1XkQwev8JkLUqHHD8O9vbnOJK%2FqYHJ9mJV8KzGr9pLoixxLVSGPqUnNIjry7OUOd%2FvzryvquWlR59oo38xjUYY5coCs3PSibOB7t%2BSbM%2BIHuIFI1IS%2Fjun08whJMe%2BrDRz6V%2B%2FZ0cIJ9lEZh2L8xuD8qo6NRPxLGQtLF1TZ2iN1Pw4KMlLLXJJWe6ASGeaYSRNg1tHPJUeyRQSPgVAB5r42KKE2F3bYJW1A2l7qTWzNoFPG3BnqO8%2BKwBzlgjoJ7hBz74biudtbv9QHY1SpqF0Zhi%2BG3b4db3SZ8eVpEOHeImjU6Fcu5n14EmBvgO5MXnp5zhSTeytLztEJ9wkrEFbgW5qO0JeBkvnq6aFjouTMNTuP6xx6eJqm5elMOIPXHQ%2FDHlcmOaiUU7EQxEVKzo0iPEHkudYIKBF8ybEKlrUrnHp%2BH0WAwxuExcdmD3GlYTeR9tD5KvZLmnoSGmbvbfSY6EwG5jTI0rXOTRAwAWskYVd93iJs%2FCzCPHJMmInYSSwRCphVX8i7XDdeFWRorGKsNx6D6zq0rJxr2UHF1xlZksahUSB5Cp93zbO1qvPsAEz%2F2hSty1nQ6YALR7vxvg4sHSMNOZ28wGOqUBAfns6ZZ1H2k5RJ57WfeNStcXqSJ76wKgDMb%2BJKbKLnorJOR7uSCGmmO%2B8G%2B24W3npJQsOhfyyNQ0S958H9RwmE0ggmTJBx9Y8B%2F1axBm4W4vYtCfjYE22QZpnPEgG%2FubgZOMYqrrxN9OxXCQE5LaAfgBheG7IYzLihns3nh86QCQYP2Fq7lAy86ULp73CEtbjx5NhG6unwiJdGkouro1ixG9504J&X-Amz-Signature=131dcc9fa5735b94b738abfc7a15959693c42769cff587980ae78f8674cb38ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] withdraw to L2 interface ⇒ default 화면 만들기.

**Github UX/UI feedback**
#45 by mandoopapa - Restake 과정이 길고 어렵습니다.
![](images/46cc52a671ec.png)

    - Candidate에 Operator 표시 되지 않음
      - Time unstake → 시간 표시 작동 여부 확인 필요
    - Unstake에서 바로 Restake 할 수 있는 UX 제공 고려
      - Unstake 항목 Time영역을 정리해 Restake 버튼 구성 고려
      - Operator 상세화면 Staking 리스트 Time영역도 Restake 바로가기 버튼 구성 고려

![](images/f7b69db32d23.png)

#40 by monica - UX/UI feedback
    1. Commission Rate and Your Staked interval is close, making it less readable.
      - Commission Rate과 Your Staked 사이 여백 일정하게 유지 & 결과값(수치) 강조

![](images/86e9ebd6c5a4.png)

    1. Staking (where users perform staking-related transactions) and L2 (information verification) have different properties, so why did you combine them into a tab?
(L2 menu name should be renamed to L2 info)

![](images/bdec794d64a7.png)

    1. It's awkward to see “Available in wallet” before connecting wallet and after connecting wallet, even if you don't have TON balance.
      - 해당 영역은 추후 Simulator 기반으로한 UX/UI 업데이트 고려 중

![](images/4e63794082df.png)

4, 5, 6 항목은 [#42 항목 Closed](https://github.com/tokamak-network/simple-staking-v2/issues/42) 처리 확인

    1. My transactions are disabled, so when I turned on the toggle, it changed to All transactions. UI that is not clear from the user's point of view.
      - 처음 기본 상태는 ‘All transactions’이고 토글 활성 시 ‘My transactions’
      - 토글 활성 ‘My transactions’ 거래 내역 없을 시 ‘No transactions’

![](images/1165b475e29e.png)
    1. ~~There are too many explanations. But it doesn't seem to be a necessary explanation.~~
      - 업데이트된 디자인 설명 문구 이미 삭제 반영, 서비스팀 이슈 공유

![](images/e372c4b52c0c.png)
    1. The number of decimal places is too short. / It need to show you the total number of digits (tooltip?)
      - 내부 정책 소수점 2자리 표시, 자리수 추가 확장할지 논의 필요

![](images/dd1fd902c69b.png)
    1. Withdraw modal - 논의 필요
      - The placement of the Restake function within the Withdraw tab lacks logical coherence.
Users typically expect to find related functions grouped together, so this arrangement doesn't align with the user's mental model.
      - The Restake option, represented only by a toggle switch, is not visually prominent.
      - It's not intuitive for users wanting to restake to have to check the Withdraw section.
      - Having the Restake option on the same line as "Withdraw history" can be confusing for users and fails to clearly communicate the purpose of the feature.

![](images/46ea1cf58325.png)
    1. The "Withdraw history" label doesn't effectively communicate its purpose or content. When there's no history to display, Clearly state "No withdrawal history" or "You haven't made any withdrawals yet”
      - 인출 내역 없을 경우 "No history" 디자인 추가되어 있음 (개발 미반영!?)

![](images/8c995abb2c31.png)
    1. 버튼 상태 불일치: 현재 잔액(1.01 TON)이 입력한 금액(5 TON)보다 적은 경우에도 Unstake 버튼이 활성화됩니다. 이는 사용자에게 혼란을 줄 수 있습니다. 입력 필드 주변의 빨간색 테두리 또는 경고 아이콘과 같은 시각적 표시기를 추가하여 사용자에게 즉각적인 피드백을 제공해야 합니다.
      - Balance값 보다 높은 금액 입력 시 버튼 비활성 & 색상 또는 안내 문구 추가 필요

![](images/fc43c8b6e2ae.png)
    1. Unstake 작업을 수행했음에도 불구하고 기록은 기록에 반영되지 않습니다. 그러나 어떤 경우에는 기록이 표시됩니다.
      - 히스토리 없을 경우 문구 추가 및 Loading UI 추가 구성함, 개발 미반영!?

![](images/8f1403c0c2fe.png)
    1. Unstake가 Withdraw에 앞서야 하는 중요한 정보가 사용자에게 즉시 제공되지 않아 사용자가 이 프로세스를 직관적으로 이해하기 어렵습니다. Withdraw 탭에 진입한 사용자는 Unstake의 필요성을 명확하게 인식하지 못한 채 프로세스를 시작하고 실제 Unstake 프로세스 중에 경고 메시지를 통해 이 정보를 늦게 접하게 됩니다.
      - Step 1: Unstake / Step 2: Withdraw 형태로 디자인 반영함

![](images/b6227e619a52.png)