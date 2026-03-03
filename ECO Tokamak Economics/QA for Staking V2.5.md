@Unknown 

# URL

[https://simple-staking-v2-one.vercel.app/staking](https://simple-staking-v2-one.vercel.app/staking)

- L1 sepolia testnet에서 수행

# Scope 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7d05fa1a-f5ad-4716-abd7-5bd467654284/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623I2ONSZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T084917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYbE%2FLAsG0fD46p5NMijLALvorelvKKSqMaU0V3VAPVwIgIvou%2B4sk%2FnVT7puXGS6x8dzpFgmBY4MqlfQCQgMtjrYq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCEP2ZLSL5JRnlg49yrcA68Vjpt7JQAjGNHc3xtDoswifWPxw3wsmrhz0wCcoIV8EsiQM%2Fha5iuN0YYH3JiXeymkDfLqMf2XzZY3fHcVP7CrR0R0zTOEi%2FyvhkQs49z5%2BR%2Fs%2F4XYziJ4qToUEipwZaUDm%2B7JKLl9gzlvfMnh%2BSYVR3kBcLiB%2F0q2jhHQ9Lovz%2BlhHVT5IfqcxMmbTqnszG6eZf37Gt19kGEYENmPa9TdgDyhcZTeXtjCY1548yMimaj9QGrGw8BHft%2BTm4Y%2Flqsi%2B3rGa32DqrY6VS6aKNLAG8Zd6A0%2BGKNtW4NZ%2By5vrywTFPyj9Bsd3hhdJZQtD4RQ4DP1nvF5StMmiOAaQ%2FxliUazFq%2BFjdxY71OfmQK9%2FbvYzp4rWkN%2FAvLLV0STQ2Xjpw0n4QbZGoVHww%2BuAy6XObZBk6L6bSr7lwtCLJ9m%2BcHbY%2FM5sXYLIZhdKbVj8qcc4yqdQkORGO3%2BjuEV8mJ07MSlSxCZohk%2BimyktoNS6jJdcf9kndSnSUhM5Rl6dYrM3nS5hAPgnXeMR0hYesOhlAT%2B7NQHQGvipp2J6O2WNtho7Aawi1C4pRxctiCHeD%2FuLLHSL%2BqpZTVfn59gQgy95zfPmlSaig3%2BNPhooOIwL0ETAe7GYGsFDUU9MNCa28wGOqUB4Miy8sp0vFtnWGBmJbvZdVz%2FSOowQHJBmkyco%2FEMhs3zhZu1yqG%2B6T2ntLt%2BCQHNCZH9NSJFyrc2AyMhuczr7rLZUfwNqSYk3OnQ0hlo%2Fp1ks5%2Bohj5bJN52pBChbWRi1l2B%2FBTFZSkKGIWPoKjU6rCifWMu%2Fqx1x0k5QDRuLfweM3QA7f6qoGqvLWc99KQI0vVq5%2FEJIIsrx0aR5%2BTk7DGHhnWK&X-Amz-Signature=4f20bbfd3096d4d841bde789208cafe40f986c613811714de44c275843b4da38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Titan_Test1 오퍼레이터의 Withdraw 버튼을 누른후 나오는 기능들에 대한 QA를 요청합니다.
1. 위의 L2 탭에 대한 QA는 추후 요청 예정

# 1. Result

withdraw 기능 테스트 → 테스트가 가능한 5개 operator 대상

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/829348ad-4284-47dd-804a-1d251814b323/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623I2ONSZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T084917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYbE%2FLAsG0fD46p5NMijLALvorelvKKSqMaU0V3VAPVwIgIvou%2B4sk%2FnVT7puXGS6x8dzpFgmBY4MqlfQCQgMtjrYq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCEP2ZLSL5JRnlg49yrcA68Vjpt7JQAjGNHc3xtDoswifWPxw3wsmrhz0wCcoIV8EsiQM%2Fha5iuN0YYH3JiXeymkDfLqMf2XzZY3fHcVP7CrR0R0zTOEi%2FyvhkQs49z5%2BR%2Fs%2F4XYziJ4qToUEipwZaUDm%2B7JKLl9gzlvfMnh%2BSYVR3kBcLiB%2F0q2jhHQ9Lovz%2BlhHVT5IfqcxMmbTqnszG6eZf37Gt19kGEYENmPa9TdgDyhcZTeXtjCY1548yMimaj9QGrGw8BHft%2BTm4Y%2Flqsi%2B3rGa32DqrY6VS6aKNLAG8Zd6A0%2BGKNtW4NZ%2By5vrywTFPyj9Bsd3hhdJZQtD4RQ4DP1nvF5StMmiOAaQ%2FxliUazFq%2BFjdxY71OfmQK9%2FbvYzp4rWkN%2FAvLLV0STQ2Xjpw0n4QbZGoVHww%2BuAy6XObZBk6L6bSr7lwtCLJ9m%2BcHbY%2FM5sXYLIZhdKbVj8qcc4yqdQkORGO3%2BjuEV8mJ07MSlSxCZohk%2BimyktoNS6jJdcf9kndSnSUhM5Rl6dYrM3nS5hAPgnXeMR0hYesOhlAT%2B7NQHQGvipp2J6O2WNtho7Aawi1C4pRxctiCHeD%2FuLLHSL%2BqpZTVfn59gQgy95zfPmlSaig3%2BNPhooOIwL0ETAe7GYGsFDUU9MNCa28wGOqUB4Miy8sp0vFtnWGBmJbvZdVz%2FSOowQHJBmkyco%2FEMhs3zhZu1yqG%2B6T2ntLt%2BCQHNCZH9NSJFyrc2AyMhuczr7rLZUfwNqSYk3OnQ0hlo%2Fp1ks5%2Bohj5bJN52pBChbWRi1l2B%2FBTFZSkKGIWPoKjU6rCifWMu%2Fqx1x0k5QDRuLfweM3QA7f6qoGqvLWc99KQI0vVq5%2FEJIIsrx0aR5%2BTk7DGHhnWK&X-Amz-Signature=9b4646b6251d2b4252d15b9ab06f496ac33d0e56c15d0acdb976cbe1a8e64951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Operator로 Candidate_jason 선택 시

1. Available in wallet → Available in your wallet으로 문구를 변경하고, 잔액표시 부분인 479.90 TON / 1010.00 WTON 쪽에 가깝도록 문구를 이동하는 것이 이해하기 편함
![](images/a38ecabffc7b.png)
1. withdraw 클릭 → 안내문구 팝업
  1. 문구내용은 중복인듯 (클릭시 나타나는 withdraw 팝업창에서 동일한 문구내용을 알려주고, 이해하였다는 check box까지 있으므로)
  1. 차라리 문구 교체 → To withdraw your staking, you need to go through two steps: first, unstake, and second, withdraw 93,046 blocks (~14 days) after the unstake. (스테이킹 물량을 인출하기 위해서는 두 단계를 거쳐야 합니다. 첫째, unstake를 먼저 실시하고, 둘째 unstake 이후 93,046 블록이(~14일) 지난 후에 withdraw를 실시합니다.)
![안내문구를 교체하면 좋을듯](images/6254c46ddb8a.png)
1. Withdraw 팝업창
  1. Max버튼 정상작동
![](images/0d2ecc7923b2.png)
  1. 일부 토큰에 대한 unstake 정상작동
![](images/3a6d0b02aa31.png)
  1. Unstake 클릭 후 지갑에서 confirm
![](images/87541c3482e5.png)
  1. 새로고침 후 처리결과 확인 (정상)
    1. You Staked : 111.41 → 61.41 
    1. Unstaking Staking Reward : 0 → 4.21 
    1. Pending withdrawal : 424 → 474
    1. Unclaimed staking reward
      1.  0 → 4.21  (정상. 단, 깜빡이는 점 표시라도 있으면 user가 add를 잊지 않을듯)
![](images/3de8d4466b88.png)
      1. add to your staking 실행 후, 4.21 → 2.73(비정상) → 0 (정상) 
        1. 왜 중간에 2.73을 한번 거친후에 0이 되는지 ?
![Add to your staking 실행 후, 새로 고침 → Unclaimed Staking Reward 잔액이 2.73 (비정상)](images/3c0cd2429787.png)
        1. Your staked : 61.41 → 65.39 (금액 이상함. 61.41+4.21 = 65.62가 아닌지? 만약 금액이 줄어든 정당한 이유가 있다면 tool tip으로 안내를 해주는 것이 좋을듯)
![다시 새로 고침 → Unclaimed Staking Reward 잔액이 0 (정상)](images/5a9cc40b5115.png)
1. Withdraw 
  1. unstake 해놓은 50 TON + reward를 포함한 총 65.39 TON 확인 (정상) 
    1. 다만, withdraw history에도 65.39로 표기되는게 일관성있을듯
  1. 모달창 안에서 리스트의 제목 변경 필요
    1.  withdraw history → unstake history 혹은 withdrawable list가 더 적합할듯
  1. 99.00 TON은 withdrawable인데,  “withdraw” 버튼이 계속 비활성화 
![](images/8677d27f6b35.png)
1. Restake 
  1. 가능금액 상이
    1. 화면 좌측 Pending withdrawal (375) ≠ 모달창 Total amount of Restake avaliable (50) 

![](images/0c0a0c3e1a3d.png)
  1. 모달창에서 Reward가 포함된 65.39가 아니라, 제외된 50 TON에 대해서만 restake 가능금액으로 표시됨
    1. Reward 포함된 65.39가 되어야 맞는 것인지 확인 필요
  1. 방금 unstake한 50 TON은 restake 선택이 안됨 
    1. user guide에 의하면, nstake한 것은 “언제든지” restake할 수 있어야 함
    1. 만약 14일 기다려야 restake 가능 한다면 user guide를 고쳐야 함

![](images/2f3d6a082f0c.png)
  1. 현재 Restake 가능금액인 99 TON을 restake 실시할 경우, 
    1. Your staked : 65.39 → 165.39 (정상)
    1. Unclaimed Staking Reward : 0 
    1. Total amount of Restake available : 50 (정상)

![Total amount of Restake avaiilable = 50 TON](images/cd4d6f475e99.png)
  1. Restake 토글 버튼을 해제 → Total amount of Restake available → 164.39  
(이 금액은 Your Staked 총액인데, 이것보다는 unstake를 완료하여 withdraw가 가능한 50 TON으로 고치는게 맞는듯?)
![Restake 토클을 해제하면 Total amount of Withdraw available = 164.39 TON 
(혹시 50 TON 아닌지?)](images/7e4f8bb65baa.png)

### Operator로 Eugene 선택시

1. 1044.48 TON 전액을 Unstake버튼을 눌러도 반응이 없음 
  1. withdraw 탭을 클릭해보면 history에도 해당 내역이 없음
  1. unstake가 되지 않았으므로 Your Stake에는 1,044.48이 그대로 있음 → 이금액과 동일하게 Total amount of withdraw available 문구에도 1044.48 TON으로 찍힘(withdraw할 것이 없으니 0이 맞는것 같은데)

![1044.48 TON에 대한 unstake 실행이 안됨](images/dc306e38455a.png)

![Total amount of withdraw available 문구에는 1044.48 TON으로 찍혀 나옴 (history에는 안찍힘)](images/02e5c11dbd64.png)

### Operator로 Titan_Test1 선택 시

1. withdraw 네트워크가 왜 2개 나오는지? (titan과 ethereum) → Operator로 Thanos 선택시에도 동일한 증상 발생
![](images/caa6d9028e7e.png)
1. 특히 Titan을 클릭하면 에러 화면 나옴 → Operator로 Thanos 선택시에도 동일한 증상 발생
![Withdraw to Titan 선택시 나타나는 에러화면](images/47f33fd10271.png)
1. Restake
  1. Restake 가능 금액이 틀림 
    1. Pending withdrawal (303) ≠ Total amount of Restake avaliable (0) 

![](images/60c0288f0a11.png)

### Operator로 Test_member 선택시

1. Unstake 정상
![](images/d2d112dee73c.png)
1. Withdrawal
  1. withdrawable로 표시된 50 TON에 대한 check 선택불가능 및 withdraw 버튼 비활성화
![Total amount of withdraw available 0 → pending withdrawal 금액인 122.34와 일치해야 할듯](images/b2e37f053ed6.png)
1. Restake 
  1. Pending withdrawal (122.34) = Total amount of Restake available (122.34)  → 정상
![](images/be0fc87bc3ec.png)

![122.34 TON이 restake 완료(정상)](images/b4a077cb631c.png)

### Operator로 Contract_team_DAOv2 선택시

1. Withdraw 가능 금액이 틀림
  1. Pending withdrawal (110.82) ≠ Total amount of Restake avaliable (0)
  1. Your staked가 0이므로 0으로 표기했지만, 맥락상 110.82로 해야 이해가 쉬울듯
![](images/548c01dc2c37.png)
1. Restake 가능 금액이 틀림 
  1. 화면좌측 Pending withdrawal (110.82) ≠ 모달창 Total amount ofwithdraw available (10.82) 
![](images/1aaf2d316963.png)

# 2. QA buget

1. 지급기준 ([QA policy](/00a62bf844134cc3b1489190f7fc9877#4662abf08c064e6e86c09eb9b434fadd)) 
  1. 개선사항 (에러, 개선건의 등) 건당 10 TON
1. 개선사항 : 19건
  1. 기능별 테스트(unstake, withdraw 등) : 12건 
  1. Operator별 테스트 : 7건
1. PI 요청 : 190 TON (19건 x 10 TON)