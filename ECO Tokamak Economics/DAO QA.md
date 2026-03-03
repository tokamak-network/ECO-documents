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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dc6c1d8a-8028-40ef-a0f3-f4421c15357a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=0c28e835a65118690382580c06f6ff51feb1eeed8e93f6a79ecf49fc2a196711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (Elected Candidates 영역) 선출된 3명의 후보를 표시하는 section인데, Elected Candidates라는 제목 옆에 상세한 설명이 필요 (혹은 Tooltip 활용) → 예를 들어, 투표이후에도 언제든지 수정할 수 있고, 그에 따라 계속 순위가 변동된다면 아래와 같은 안내문구 필요 (Tooltip 활용) **The elected candidates are the top three by number of votes. You can continue to change your vote via Revote, Unvote, Withdrawal at any time after you cast your vote. The ranking changes in real-time based on these results.**
- [x] (Candidates 영역) Candidates이라는 제목 옆에 상세한 설명이 필요 (혹은 Tooltip 활용). 예를 들어 **Select the candidates you want to vote on from the list of candidates, and click View Detail**
- [x] (Elected Candidates 리스트) **Status : Occupied → **의미를 잘 모르겠음. 불필요 하면 삭제하고, 꼭 필요하다면 tooltip으로 설명을 추가

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/efaf085a-36cf-4459-9b3a-8affdc1c01df/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=a238741da18fcb850908efbbd016051be0f775bf427225fe7324f48fb9b5d197&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (각 Candidate 개별 페이지 > Detail) 생소한 용어는 설명 필요. 예를 들어 Winning probability가 무엇인지 설명해주는 tooltip 필요. 
- [x] (각 Candidate 개별 페이지 > Detail)  Winning probability 하단에 있는 you can check the amount of power 문구 옆에 here를 누르면 링크된 페이지가 안나옴

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2b713698-6152-46e2-ac7f-4f86d786bbbf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=f8b57b81cbd1bd3ea6da4c4bc53cc325d7a0ff0eb6e8d860559241eb56d505a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (각 Candidate 개별 페이지) 내가 투표한 10 TON이 Detail 탭에서는 합산되는데, Vote breakdown 탭, Supporters탭에서는  합산되지 않았다. → 시간이 좀 지난후, 페이지를 refresh 하니까 합산되어 나온다 . 
- [x] 아래 그림과 같이, 일정시간이 지났더라도 지갑을 연결하기 전에는 0 TON으로 반영되고, 지갑을 연결 후 refresh까지 해야만 금액이 제대로 반영됨

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/77f3c801-8b21-4485-a3d5-5264c40d41d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=a8a28c345e4a0b1bf56a4518fa0c2942a858c4d867e71601dcc5a09f296829d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1dd4d92b-7d0f-4819-aba3-cc95ae960ee6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=585758e487dd2236577d74eee5f504c85620f6803b8ea81a1b5038b8bb9c47c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] (Update Reward) update reward에 대한 안내 Tooltip 필요
- [x] (Update Reward) 0 TON에서 실제 Reward금액으로 반영되는데 시간이 소요되는데, spinner같은 것으로 계산이 진행중임을 표시하면 좋겠음

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/62da59b4-624d-416f-b3b9-0f6c5674a881/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=3636e321dad6a2d71470585c9cfb3d921aab05be955416e8348161248b4898e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Update Reward) 버튼을 눌러서 Update를 할 때는 1.25 TON이 reward라고 소개되었지만, 실행후에 확인해보면 0.83 TON만 증가되어 있음 → 오류가 아니라면 그 이유를 설명해줘야 함(Tooltip 활용)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7dc1a304-b41f-4ed1-9d7d-f4ac62a44a0e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=d1715708e6c7dd517c0a2c6186b49e446d2e71d6132e36f528a9813167d11b04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/92f8edf4-6799-4a16-afdc-7d8f19573d37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=872e81a5c21c4516f6b7dad57f2d742ad922e157bb509abe54b4603585ed9c09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Revote, Unvote, Withdrawal) 실행이 활성화 되려면 일정기간을 기다려야 하는 Revote, unvote, Withdrawal 등의 기능에 대해서는 tooltip으로 그 이유를 설명하고, count down 시계를 넣어주면 좋겠음

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/bae7a4e2-7a32-4d9a-a8f8-8d193770665c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=6eb50cbf8c4efc4f3d271ac8b6e9624fb7f06afe864b72f5008be8bdc4531ec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] DAO discussion (Discrod) → 괄호안에 오탈자를 Discord로 수정
- [x] DAO discussion (Discrod) → link를 눌러보면 올바르지 않은 초대장으로 나옴

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/58b772be-cbb5-4772-bb50-e9bf06d5c5e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=01d3019802fc924bd053db4760aa80fdacf4c2682cbc85d1a41475b5327cbb39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] 설령 9.9999…..로 표시되는 것이 맞다고 하더라도 10 TON으로 표시해주는 것이 사용자 입장에서는 혼란이 적을듯

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/db30addc-fd64-40d3-ba86-a3baf6b8e156/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=bd2b71c3468f0460209e0ef8c47d55809dbdcf3efd7a7b1b6cf54e9e4c3b682b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Your Vote 영역) 이 영역은 아마도 summary 영역인 것으로 보이는데, 내가 Vote한 Candidate에 대해서 withdrawal 금액도 표시되면 좋겠음 (현재로서는 해당 금액은 Withdrawal 탭으로 들어가야만 보임)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/37793f55-fea1-4b29-81f8-5635fce4a648/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=8a14802647cc1f2cda05ee61f56dfbb7043db648063dfb4b3c50441bc2ffc43b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (Your Vote 영역) Next Candidate 버튼을 눌러서 내가 vote하지 않은 다른 후보의 화면으로 이동을 했지만, 여전히 Your vote에는 “You Voted for this Candidate”로 나옴
- [ ] (오탈자)  “You Voted for this Candidate” → 불필요한 대문자를 소문자로 변경 → You voted for this candidate

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/51b6f7d9-25ae-4ee8-8fd6-b61ee272648a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX43ONLH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmZyzrev0dBlbaXvkHmdJ%2BWrYyh2cBa6EvREcvJhe9mwIhANtAo2J%2BQ%2BOfG0%2FhuOxnWLsLnjsgbH%2FGW%2BVEhL9BQxXoKv8DCHoQABoMNjM3NDIzMTgzODA1IgwPu710wzvP9Dlm3Mkq3APhgYjXcnZLKaepXxk7l%2FjJOrbSHD%2BJ%2FoKtm7ONec2KtQY%2FRVH467hbDyCR%2BWxxdEswle3dRnHKaRvNYuBkmTGGIxkDVtF5b083wn2hNmPEg82UYfY9f8qkUPTa5OzxWcG48vs16EWCYvy7Iuudw4K4sqZIwzjWiXxZOEEVik4fgiAjJQkxGfn%2BVGymnVsde3IKy4P%2Fg8TXH46pvp95z6UqVr%2FH%2Fcg0PGY6Po6ER4zA%2FQSCrY8x0kjOOoZ%2FO6EfnM%2Fa97ZCG%2FciG6i1mIwtIMeXe7EnTZII7slokLH5Qh2UAUdvlwIXtlg18TnCXYDTI%2FJsfEx1DXI8FB6p71I2jwslNy28cyI4vPRP9i0DeNP7H0Hvvw%2Bi%2Bs2%2F1yPxbw9oaIsTLiqNR7sbLL3pzwEUR0HlUbHKUsM4dK0s9fF5hX5LIOFBRVlJfM4aHA3eVC%2FzCznrBD7QovPwp1N72A5dCZ4YTybBZLhAJzP1f10G2A0hcDAC3Jsv0hy43%2FfN%2F6wpHignvP4vPMcHgERr8gSzmiRu1l4OUz5KAAXTH%2Bpa0MDcZYZuH5HNZe0XRK9V9vGmGx7bb%2Bo55B4dRie1JAYWjHNpDIDMlJ%2FqQdmo1vPl%2FDkK37wojau0BIxBjK7U5DD9mNvMBjqkAY7fEVBIxmtdfCqA5aLeAewbP9K0qgzuliRWmvtclzMgbzsFSMKaqhU17kzWQQHknYA99T0hXhTtgO8BN5%2FmZpIivVgCqcQ1oPgtUihtJaq3kTPrPXb77dxXmm%2Fx1UyvG2xylESxAAcRWCIiUQSAjlBHasC55mkuV2U1UER%2B%2Bdd7hTUuPWLd0oCj3bal5f3xciRgynes0OMxy5Rbj5k0qQ6eRe2A&X-Amz-Signature=261b6e4d4c2a3b3e7326ea7327fcee5345448b90913a65a633908b17f7b79e0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] (양식 통일) 버튼 비활성화 방식을 통일할 필요 (어떤 것은 버튼은 파란색으로 활성화 되어 있지만 실제로 눌러보면, 비활성화를 안내하는 modal windonw가 팝업되고 있음)
- [ ] 토큰 입력 form의 경우, 양식을 가급적 통일하면 좋을듯

Lucas
Committee

- [ ] 'Not Decided Yet' font size needs to be modified to 30px -> 20px in Voters area.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/29f18351-37a0-47ed-8c84-2416d1d83538/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN5LADJX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtOOYJqtfyQExO%2Bd7LnMQeKQ9Boc3F23klaK%2Fg2Tm3EgIhAJP4oJ3RJF5xQN5b9UI7ZrBSGmxbEbm3DB8QK2RtOfSWKv8DCHoQABoMNjM3NDIzMTgzODA1IgxIr%2BIbUZJGsEEmu6kq3ANYw5gFnq5WCbTxtWemZXUYplvx0mYTd2xBxqB3eiVnznAAFL9FXXnsp3CcGcqrAgs6KDMdHL0qlfDvxal191of3BmgNoMWfeZhdIP26FRc9CPNPGhErEvJmmYqjcPwhpTT0EvgnHTB35x6xWA%2BSAvhOYIJFNBLLsAuO81b0IIlS%2FLZuqkTeUElJwRDNRNhSRiZ%2BD6XLZ40hlgwAyBIfi1FZnSO6plsLv4TI04aZu49vtmV13djFdv%2F2cLUBeQxY7IQyxTrXwKMzac1luf0MN%2BCyoznk9i8agRDou3CAg3vt7ticp%2FpkK2%2FjysDkFf%2BbpmMDU7Ypr49%2BAufuruloBupAV9YgC%2FggXBdTM18iEYtylxkZKgO6LF4Sw6JP5vQ2bySNb809UV%2FbNg9lmAqnUdMJOZGyD%2FVkTdoo96nS%2B5EgKTUiulcRSwM9jiGpnqSH8rTOA3mjL1ZOqFY4SVW%2FMThzN4AtPSpl%2FKU7jJZrTLz21rOVWwMi6PQaSFYERiAJ5Cxx8LwqyKqTyxLG%2Fe0ucfvaa%2BQGG6r2HrPhLTBqeDqMFUpQRSEU3M5VxnM41fAVwQ9AJr2bC0OhwqQTiZ%2BMmUspG76jWJKKuV0z2c6zFlS580A45ai7tMKe1rYoTDdmdvMBjqkAazAeMAj1bNxZzBMRjg4ZodG4Xe1czjH6xjfrAChjYyCqZanE%2FeXlUoxMA%2BrCuI1XWmch1%2B85Wxd33q8dl8f9hiXzQ3k6i6RvR74qEac7sj9spTYnIQKIFRZngVIzsxUtxDLxeTYDQrmUo9p5NA3wnhtie9yjapXliu24QqhYG6dUG2DV0g7SQW50AcEUyGn4M3CxYUcEhtXMzFJQvbY8gCA%2FRjS&X-Amz-Signature=d5bc60d2ebd83ef0d08ffff081b2a52d9699b53cbe27ac22d3801a7831b18fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f9e58505-b68e-495e-aef5-6daf742b7ebb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2UMIQTV%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3UsJxujAvlw9J62ZLgACAlychDRHbgZIoQQndgCG9YgIgLQtXojpa2aXs3idbAJCAubras57e8mq1GLv6e8qEeSoq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFj5%2BurpvZX%2B0S%2FJ%2FSrcA2oIx56TZcK3McbhJ5m9f8O2xugVK9HA3FacZqohDE7xF309N1aoitsCtWmDqfs7f%2F8PgV%2BI67XMelc%2B%2BPivDOzVNZfaRK5otCDZe3438SpZ4UWDd1nQu0a4VosQsVsCE5zsZMFyiKKbJHqmE8DEJqnD5BEu6Kn9OHS0Uz5Im2wql6V70LJ4YqNLBDvXK%2FpkYvLMEs7NXUqQFOSQ%2FetkTmpLjfSZWtUcOmRGh8dglimHiO%2BOX2WrSuEEeYhWIktDxMsyJf8lGwkoxKpenOFKiy1MiQREPzrm5Z5Nd%2B3e%2BATqMEXtMbjlKB2xgTILOa9%2FjXuudv12U8rO%2FqZ1CXZDIBUMa7vzq15PnDtuKUPCZDegsGXmrrGjGuzgZ2xjM%2BVPC1d7YLj1GbKST7Bl1X%2FwnPpOt6OLl3xlQOco%2BgYamkxGH22xVxVb8XG82KB8iGaWiU6P0K%2B4vbLWOQD5O2AjxTBeS2p2uFCEXDZwnfNcR9radjGOJ61FufGyn6sBQduoqp6nxu9QuLQb9B9Gm7Nct8fHSr1W%2BgPmANgGvQc1ENBXicBqggmOFI%2B%2BaKBW90yDUjnwGNco5tnmcriW8m71%2BsM3hZcWaUqg7t54maVEB0AnBvYFhE5uSMQyAs5RMPOa28wGOqUB%2BCokVSwXBonqgFnPbMSl6A6qK37JUAhAxAwhBT5TYnJJVkRgEgcPNggayCWDonfU1G%2B7bd6gV07UtOnPQd6cagBpj3KbzGqZflwsAi%2FmVX84zeZuTj0jHDDz8mZD9lDRNStuRd5zI%2FtYip1rGIL%2FmpXY1XRThJene5HSL1ROwaX1K%2FzOFraBye%2F1ZZyfheQ%2BVYQHbhNGL7rp3noOJxcA0fgoPpHp&X-Amz-Signature=ecf111ed04b08a9dd3033ed008073fa678653110bbe76afb9aa97a6887fbc8f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [x] 파워톤 내용이 없어졌는데 맞는것인지? —> @Unknown 문의
- [x] 합산 금액이 이상함 (아래 그림의 4번항목) : 104.13 + 1.58 = 104.15 ????? —> @Unknown 문의
- [ ]  DAO 페이지에서 Trezor 지갑연동을 클릭하면 작동하지 않는 버그입니다. Trezor 버전이 낮아서 그런 것 같습니다. @Unknown 참고 부탁드립니다.