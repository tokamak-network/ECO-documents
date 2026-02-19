2024. 1.22~23
## Tasks

List
## Frontend service page: 

    - [https://sepolia.dao.tokamak.network/#/](https://sepolia.dao.tokamak.network/#/)

## Test fund:

    - Sepolia ETH faucet: [https://sepolia-faucet.pk910.de/](https://sepolia-faucet.pk910.de/) 
    - Sepolia TON / TOS faucet (can earn 3,000 TON and 3,000 TOS per day by using requestTokens function): [https://sepolia.etherscan.io/address/0x3ef15696646e93f73c5455b9a3e66e490b064ee9#writeContract#F1](https://sepolia.etherscan.io/address/0x3ef15696646e93f73c5455b9a3e66e490b064ee9#writeContract#F1) 

## Storyboard (updated):

    - [figma](https://www.figma.com/file/eVKDcPi362P0RH4lSIYQf9/2024.1.25-DAO-page-minor-update?type=design&node-id=1-2&mode=design&t=XmGDPakuydNoRbFi-0)

## Design(updated): 

## Check points:

    - spelling
    - information duplicity, not understandable 
    - functional tests:
      - election tab → test following functions 
    - Analogy
      - Vote → Stake
      - Revote → Restake
      - Unvote → Unstake
      - Withdraw

## Work done

Eugene
“Election” section : Summary ([Slide](https://docs.google.com/presentation/d/1JXU_H0WRMpUczXWxqqgWzrj6S4wLnBcdLjjL7QbiJdQ/edit?usp=sharing))
To-do list
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dc6c1d8a-8028-40ef-a0f3-f4421c15357a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=0bbf1a0d0b012c1b2f5b8a692813ae8e4f906dab4c145b4b3cfc5100f263f574&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (Elected Candidates 영역) 선출된 3명의 후보를 표시하는 section인데, Elected Candidates라는 제목 옆에 상세한 설명이 필요 (혹은 Tooltip 활용) → 예를 들어, 투표이후에도 언제든지 수정할 수 있고, 그에 따라 계속 순위가 변동된다면 아래와 같은 안내문구 필요 (Tooltip 활용) **The elected candidates are the top three by number of votes. You can continue to change your vote via Revote, Unvote, Withdrawal at any time after you cast your vote. The ranking changes in real-time based on these results.**
- [x] (Candidates 영역) Candidates이라는 제목 옆에 상세한 설명이 필요 (혹은 Tooltip 활용). 예를 들어 **Select the candidates you want to vote on from the list of candidates, and click View Detail**
- [x] (Elected Candidates 리스트) **Status : Occupied → **의미를 잘 모르겠음. 불필요 하면 삭제하고, 꼭 필요하다면 tooltip으로 설명을 추가

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/efaf085a-36cf-4459-9b3a-8affdc1c01df/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=e3e458e85d1ae1ef524196ec041d2868046c869908e9d35850d1aac3eb91bba8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (각 Candidate 개별 페이지 > Detail) 생소한 용어는 설명 필요. 예를 들어 Winning probability가 무엇인지 설명해주는 tooltip 필요. 
- [x] (각 Candidate 개별 페이지 > Detail)  Winning probability 하단에 있는 you can check the amount of power 문구 옆에 here를 누르면 링크된 페이지가 안나옴

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2b713698-6152-46e2-ac7f-4f86d786bbbf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=8794e279646b380326b3877bf15f78102f8e858ce886b6b9aa3a5ba1a37b2cb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (각 Candidate 개별 페이지) 내가 투표한 10 TON이 Detail 탭에서는 합산되는데, Vote breakdown 탭, Supporters탭에서는  합산되지 않았다. → 시간이 좀 지난후, 페이지를 refresh 하니까 합산되어 나온다 . 
- [x] 아래 그림과 같이, 일정시간이 지났더라도 지갑을 연결하기 전에는 0 TON으로 반영되고, 지갑을 연결 후 refresh까지 해야만 금액이 제대로 반영됨

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/77f3c801-8b21-4485-a3d5-5264c40d41d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=be5c823afb010c3f1ed743ea3e8a0836c3e1dbf7d0207097d124c5c3b264ea1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1dd4d92b-7d0f-4819-aba3-cc95ae960ee6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=7dd15922e5f96a1cbb6099fee84dc0db76fc36a379133ef4e6e5f05b055d6c00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (Update Reward) update reward에 대한 안내 Tooltip 필요
- [x] (Update Reward) 0 TON에서 실제 Reward금액으로 반영되는데 시간이 소요되는데, spinner같은 것으로 계산이 진행중임을 표시하면 좋겠음

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/62da59b4-624d-416f-b3b9-0f6c5674a881/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=601da2948313814b283adfb8883fbc982a00596b3f0e67387ebcc3c73e8f72c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Update Reward) 버튼을 눌러서 Update를 할 때는 1.25 TON이 reward라고 소개되었지만, 실행후에 확인해보면 0.83 TON만 증가되어 있음 → 오류가 아니라면 그 이유를 설명해줘야 함(Tooltip 활용)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7dc1a304-b41f-4ed1-9d7d-f4ac62a44a0e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=b7932dc4093d24b90e90c1975b9c3d2a5b3a1ef65067730e40cf6dad4574fe3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/92f8edf4-6799-4a16-afdc-7d8f19573d37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=f1b9493d06503b0f36996e83de434aa8256fe5441a84a7080714062cb92552e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Revote, Unvote, Withdrawal) 실행이 활성화 되려면 일정기간을 기다려야 하는 Revote, unvote, Withdrawal 등의 기능에 대해서는 tooltip으로 그 이유를 설명하고, count down 시계를 넣어주면 좋겠음

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/bae7a4e2-7a32-4d9a-a8f8-8d193770665c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=6462e43421941682c9476feff8cf7b4a5a71213198f93b0f7075b78828191e0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] DAO discussion (Discrod) → 괄호안에 오탈자를 Discord로 수정
- [x] DAO discussion (Discrod) → link를 눌러보면 올바르지 않은 초대장으로 나옴

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/58b772be-cbb5-4772-bb50-e9bf06d5c5e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=c23f0f794105b1ee497c8b07f8523f894662cfd25ca5b8b9c654900f04f0012e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] 설령 9.9999…..로 표시되는 것이 맞다고 하더라도 10 TON으로 표시해주는 것이 사용자 입장에서는 혼란이 적을듯

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/db30addc-fd64-40d3-ba86-a3baf6b8e156/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=e7238c68f490bd775e56f7134bcbfabca56f5f941f1249af515e8d5f7bd4fbe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Your Vote 영역) 이 영역은 아마도 summary 영역인 것으로 보이는데, 내가 Vote한 Candidate에 대해서 withdrawal 금액도 표시되면 좋겠음 (현재로서는 해당 금액은 Withdrawal 탭으로 들어가야만 보임)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/37793f55-fea1-4b29-81f8-5635fce4a648/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=4aee9e6b56f9f387995341553474aa48bb419e44b004743f193d301ac93b6413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Your Vote 영역) Next Candidate 버튼을 눌러서 내가 vote하지 않은 다른 후보의 화면으로 이동을 했지만, 여전히 Your vote에는 “You Voted for this Candidate”로 나옴
- [ ] (오탈자)  “You Voted for this Candidate” → 불필요한 대문자를 소문자로 변경 → You voted for this candidate

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/51b6f7d9-25ae-4ee8-8fd6-b61ee272648a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJLK7D54%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYmUvDzH87WF1OvCGreBYkdtU7y0Zx9s0TvnZRGjyFsgIgNjqfXU8QJmh9REDVELMN%2BOFebBYA3oBcJ7qyV6jtRzUq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDJlS7os3R7cLE0UJMSrcA7052piNxp5jJALAE7Ul31UczT0ZnKsna7j7C41NIWYeXn2Ou42Uo3X1wK36wHKH%2B9rU5GoGGqxQvehMIEBnbvyZOcvUHSxEYeYF6s1pOTdz1Px9RIP6UO2mzOy8KOAgBdjETuz5r%2FYXJ9S1xT61J3jCgxVgu9RzHWwfo4irhuQ1l5f3CyYKqZByGN92v5RmCrrnvsR0zZFKmmTbWNc0w%2BMfzBJlrlvqccZX%2BVZnJ1sfI3EGeiOdWpxKb4H4zYkD94gx4HsFlI1OU7bdgUeQ4ndtOOVx3GAbc%2FhV1RGVsiyNVfOJMzKk9BM4ALeJ2X%2FqTT3pOLbR9tOnb2YKm1PShVBh0Rd71nM2VYuMzBLle%2FVWa53ddwB1FmEgWggzqVlAm5C3EVMDdaMUUUzQVDMeYL4CiCz7CLRVhCdh2rrW7ft%2BF30eDwEbq3C2GzbI3gnO2IJar5DUrhQCg7xat2as9etnZ15tWqyy9DEd3bftVCaVp9GXDWSJ0TSpyLa3ZshrjWm%2FNbhZZojhU2HvFHF8aSm1AckNUtzuGbWn7dTXSxy51PZ3Ls%2BzXQXY2tuBHGpqid4IRlwsaBGpQvkzuaDyrBQOJPEC%2BK%2F5ciY6iMdMr%2FEf22TK1avxFrppZhiLMInE2swGOqUBzK42rdBOU5SqHvElsCbPZHtnV7jeUJK0U1w6S6fI5yPVPnmMNyWwoY7yMfbC7qj06mrK7iq5HoMRPHz7w5jfH66YIgW8jfxFfIF723kwy6JiO96nYph4yThXP58CM01C7t4voDHu%2FECOMed7BI5WCWlweAYk6nMF3G0Tg%2BAFaN4clVZH3nyzL%2BoauNgrIfR07PvyjhnCBqxt%2FBtafbwYgtBx390U&X-Amz-Signature=1d96350b6610c77505686083a4b46883937fac1623ce8ea421765a311cd7f4e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (양식 통일) 버튼 비활성화 방식을 통일할 필요 (어떤 것은 버튼은 파란색으로 활성화 되어 있지만 실제로 눌러보면, 비활성화를 안내하는 modal windonw가 팝업되고 있음)
- [ ] 토큰 입력 form의 경우, 양식을 가급적 통일하면 좋을듯

Lucas
Committee

- [ ] 'Not Decided Yet' font size needs to be modified to 30px -> 20px in Voters area.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/29f18351-37a0-47ed-8c84-2416d1d83538/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7EJ2AB2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLcnF6XRZ41%2BENFIRrfIVxUFNiI33ohB4r6PQtA8oNnwIgeK6BnfxrmeVG8LgJ5ZIZ3JwVlsQ%2FdwlPt2HGdQAf3Nkq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDP2xt9%2FE8B9bMrNMlyrcA4YWbiNudTocw%2FKxWvzlQAgGcXfM0PI9qYVVb%2B5uVKhl8TsXnL%2BCBSLdYs2e5worJtNFsT23UhzTzFYRmqvOnsEEV1RmzepKkNoaxu9lgh862%2FaDArp3vXZnm5mt645X463kbqJ19UZ3Ah8xR40QPJVjMhuTwZeCt58fxfP7AvaWNXOnnmMEOqurWe1GN1fiG1pqUjssoNiYixwirOGBhxFAGISBNm9RHWCctb0272%2FpHj4wKYX6bPW%2B%2F8Fy2yh8%2BZHUWB2jwW1ni6h0g%2FgCFySw550bO4NQZ%2Byum9%2BMZrucg%2BXqW%2FPWgMBP4XvAzoy34W0O%2BWsWWgGf6h8ORQ91SZfBLFhRegtPa9ywcBseKTykBUUANTJohDucZ9U5iVSt09Bv11HVwykhA5wTHkWY1FdZSvcD%2BaEyarAnUiZdLzlS%2F4dWHjH7Jtucp2iKL5XDI99EP1a8qZLGmRUcJMYMHJyEo5PoXaAz4j9K%2BdlP0PbpBI7%2FW9ludIQrX%2B0%2FeUFALFGbWNPb7zLiowxPi5hhZbpWw96ymIgM685CjNrqI3bFuF%2Fr4uRKeG5tEP0I3nI33G5rGEoXL81ynBLpXzCFmBqsH2V1gAIhpFsDXo8Jx6XR0u5XhXZ6xPULsKTNMIvE2swGOqUBdvEuwrtwxxOrHwMs0zNX%2FdjLR2NRnoHtzLaWl%2BXIHV6Qh1iUstwSTdJ8IlhSigdb9DJlqtOZewo12Dbz6kqE1wkvcsMz51bayHZCic4scvZ%2FDQ1wujPB9wf5YU9pvsSZXeOq7eSBWp8jnzCcHhzuW1zu4SNmmxDUJ%2BsX41jFUmeGwSVRpd09CQ%2FQNwnsgDler4CGDZan9OoVM1CjO2kMyFZtN7f7&X-Amz-Signature=41cac4e4edc470c04e9502f63bfeab28873f773bc58d7bd4ba3da167f8a9e78c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2024. 3.22~4.2
## Taks

List
    - Updating the Gitbook user guide
    - Consolidating distributed documentation into a Gitbook user guide

## Work done

Eugene
<<1차 수정>>

- [x] gitbook 수정 (Edit number #66) 
- [x] Google slide 수정

<<Staking & DAO 파트>>

- [x] 1. 개요파트 추가 : 구체적인 서비스 설명을 추가. 예를 들어, 전체적인 Simple staking과 DAO와의 연계구조를 설명
- [x] 2. 각각의 공식 서비스 페이지 링크 : 설명공간 맨앞에 섹션을 만들어서 넣어주는 것이 좋을듯 (모든 서비스에 공통 적용)

<<Create DAO candidate 파트>>

- [x] 1. 하비님 자료외에는 모두 없앨 것
- [x] 2. User 입장에서의 용어와 설명방식으로 문장을 매끄럽게 다듬을 것
- [x] 3. 1,000.1 ton 스테이킹 후 매타마스크에서 approve로 뜨는지 확인 필요
- [x] 4. 상기 스테이킹은 후보 contract를 생성시킨 계정으로 해야 정상적으로 작동함을 설명
- [x] 5. Sepolia네트워크에서 화면캡처를 하여 설명에 추가 (03. DAO 후보로 등록 및 04. 결과확인…부분)

<<DAO 페이지서브매뉴>>

- [x] 명칭을 DAO candidates, Agenda로 각각 변경 (화면 캡처 다시 해야 함, user guide slide에도 변경해야 함)
- [x] 용어 통일 : 예를 들어 L2 Operator : Create 까지만 한 사람. Register까지 해야만 Candidate가 되어 DAO Candidates 페이지에 나타난다.
- [x] DAO candidate에서 4번 게임화는 삭제 : 그외 1~3번 내용은 DAO 섹션의 소개글로 이동

<< User guide slide >>

- [x] stake, unstake, restake, withdraw 등 → gitbook simple staking 쪽으로 옮기고 google slide에서는 삭제
- [x] 단, stake는 restake와 unstake는 withdraw와 각각 합칠 예정 (따라서 이들을 묶어서 동일한 섹션으로 설명할 것. 특히 unstake + withdraw는 개발상에서도 두 버튼을 하나로 합칠 예정)
- [x] 서브매뉴로 Staking reward

<<agenda 파트>>

- [x] voting 부분이 slide에서는 **07.   Decision-Making 항**목으로 별도로 분리되었는데 합치면 좋을듯

<<Github Rep, Contract URL 리스트>>

- [x] [@harvey (10-19 KST)](https://tokamak-network.slack.com/team/U05P2EZM3FV)님과 상의하여 정리 (위치 : DAO, Simple Staking 각각 맨 앞의 소개 페이지에 정리)

<<기타>>

- [x] 대문자/소문자 통일 : 앞에 것만 대문자로 통일
- [x] Slide를 gitbook으로 모두 옮기는 것도 방법

<<오탈자>>

- [x] voting이라고 설명된 부분이 아직도 있으니 수정바람
- [x] 단 Propose, Agenda 서브매뉴에서는 voting이 있는게 맞음


<<버그 발견>>

- [x] DAO > candidate > name, description > edit을 해도 반영이 안됨(지갑으로 컨펌까지는 됨) 
—> 컨트랙트에서는 반영됨, 프론트에서 반영안됨 (대소문자 모두 가능) —> @Unknown 문의

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f9e58505-b68e-495e-aef5-6daf742b7ebb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJARNSMT%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjDFkCnbxFWjQx%2B2TXIsZG1liGH4i0NefsDaDnM0VPkAIhAP7HIHcfL77EckHSBSEm9jPo0a2uyyN%2F3q7oMDPsITJaKv8DCHcQABoMNjM3NDIzMTgzODA1IgxQ2dT7xPFZrNU8ElMq3AMRqcOuf1aY3YYmvwa4Fi5VW29PJlts0%2BTrAOhXzMg%2FMYOUQZYfLRztHS1%2FDRTQXfrI0dC8rlRjG59DhZPcI1uUT%2FOp%2B37IO%2BW2ZpyCPbiu9p9oBoUaAn%2FSbGF1nBQsIyVuUmxYLANOH6EQUgZQvIKt1LWXj5d3KwR%2FZ85f6RtHYwI369FsOfYf84%2Bw3hRI3%2F6bxAGNRkShGSPlTjAIbFIlwJw8SkIjlRwF3Uy9ltXGxR5VsqrXl2bEBM3tjBq5vaLHq1cKRKggF2g9XFiAY14WUd5rKxddaqOQRL2Z1VHVS%2F3oaT4LlGx%2Fc4J5WaAiMj1WJ22N9NkDXEo1LYIGF4c0jniFsCo%2Fu46tFyKXNgM7C%2BTuViBKXiz4ZQ4U27zXKmrfF6oLJQ3SooqwxvxnyCssQKQuyRd58vyKunlTD%2FEVffRBC7s5AA%2FlrQzHPpLg7ituaWigTu3tZlBH5Aa2nj3Q37L5kKns4wb%2BnhwH9Y93bUAeKJc4nRdFXlKs3VbTOF6rFMFg3icYQ4yZTquBTlcZKyX5HZ13OgE8Viz3e%2Bq6Dh6mRF%2B0I23m3Y%2BxONEcyHykN%2Bblpim2jIEy8dwGgunJbMWKqW1QX7Dq4SWXRiWmckGxEWclxOQQpo8MmDDDxNrMBjqkAR5dFI5t6ex%2F%2Bdlqup%2BnpqG88liN2cnWRnUwVLAOQo7kaoqp%2FXcecgPsh77euDps4XjySZRafb1E7ky6F4a4M7CXw8d9IIH77wQ6hE0IAdoBeg9%2BkDyWzGvuCbEmJ2Ap8XX6MoE%2F6SRVA3pB7%2FbUehtPfI5gI2A2XocmPxSX6H9keo1BYOjoWI4HOZv%2BIhmTQeFy5SGABj1fUauvyLImt4Fe3WQT&X-Amz-Signature=fb2e6aad17fd2f7759549fb0f559902a7309ffa913690fb00d01dbe416c39718&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] 파워톤 내용이 없어졌는데 맞는것인지? —> @Unknown 문의
- [x] 합산 금액이 이상함 (아래 그림의 4번항목) : 104.13 + 1.58 = 104.15 ????? —> @Unknown 문의
- [ ]  DAO 페이지에서 Trezor 지갑연동을 클릭하면 작동하지 않는 버그입니다. Trezor 버전이 낮아서 그런 것 같습니다. @Unknown 참고 부탁드립니다.