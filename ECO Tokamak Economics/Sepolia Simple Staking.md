# Test web page :

 [https://sepolia.staking.tokamak.network](https://sepolia.staking.tokamak.network/)

Candidates
```javascript
layer2Info_num1 = {
      operatorAdmin: "0x43700f09B582eE2BFcCe4b5Db40ee41B4649D977", 
      name: "TokamakOperator_v2" 
			layer: "0xCBeF7Cc221c04AD2E68e623613cc5d33b0fE1599",
			coinage : "0x02c91aF739a4414F0a6b4F820Be9E7dc46CD62f2"
  }

  layer2Info_num2 = {
      operatorAdmin: "0xc1eba383D94c6021160042491A5dfaF1d82694E6", 
      name: "ContractTeam_DAO_v2",
			layer: "0x277201BF0B20C672b023408Bf7778cFf3779b476",
			coinage : "0xFB44a113F5BFe58DE5365E7B00b5404925635fdB"
  }

  layer2Info_num3 = {
      operatorAdmin: "0xf3D37602D501DC27e1bDbc841f174aDf337909D2", 
      name: "ContractTeam_DAO2_v2",
			layer: "0x81581558791d423F2BBea52923BfD245DBB9C4F5",
			coinage: "0xE9d1565cd4827fBC3dB670733D2c630f6f951E93"
  }

add Candidate (for test)
operatorAdmin: "0x757DE9c340c556b56f62eFaE859Da5e08BAAE7A2"
name: member_DAO
layer: "0xAbD15C021942Ca54aBd944C91705Fe70FEA13f0d"
coinage: "0xD52d06f68dFEB59A647557836612549bc07dFd21"

```

# Test 

Zena ( 1차 테스트. 피드백 확인 완료함 ) 
- [x] 톤이 있는데, staking 버튼이 활성화가 되지 않습니다. 
- [x] 총 유통량이 0 개로 표시되었습니다. 
- [x] 시뮬레이터에서 버튼을 눌러도 동작이 없습니다. 

Zena ( 2차 테스트. 2023.12.12) 
- [x] 오퍼레이터가 1000톤을 스테이킹하지 않아 업데이트 시뇨리지를 못하게 한 메세지 같은데, 메세지 내용이 안맞는것 같습니다. 리워드가 표시되는데, “No staking reward for this layer2” 이렇게 메세지가 표시되어서 좀 혼동이 있을것 같습니다.  ⇒ 일부러 이렇게 하였음. 문구 이대로 함. 
- [ ] **ContractTeam_DAO_v2 레이어에서는 **1000 톤을 스테이킹하고, 업데이트 시뇨리지를 통해 1.82 의 시뇨리지를 받았는데, **ContractTeam_DAO2_v2 레이어에서 1000톤을 스테이킹하고, ** 25.46을 받는다고 나옴. 맞는지 확인이 필요한데, 오퍼레이터가 1000 톤을 스테이킹하지 않아, 확인이 어려움. 오퍼레이터 1000톤 스테이킹하고, 실제 받는지 확인이 필요함. 
- [ ] 언스테이킹 버튼을 눌렀는데, 동작을 안함. 아마도 오퍼레이터라서, 1000 톤 이하의 톤이 잔액으로 남아야 하는데, 이조건을 맞추지 않아서 인듯함. 언스테이킹 버튼을 눌렀을때 해당 안내 메세지가 표시되어야 할 것 같음. ⇒ max 보다 크게 적으면 비활성화 하자. 다른 곳에서도 공통 인터페이스임. 
- [ ]  500 톤을 언스테이킹 하였는데, 팬딩 금액에 표시되지 않습니다. 

Harvey (1차 테스트)
- [ ] 6.1TON을 unclaim했는데 2.8개가 늘어났습니다.
여기서 6.1TON이 전체 Reward를 의미하는 건가요?
  1. operator가 1000TON을 staking하지 않았을때 (정상작동 확인)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2e77ee50-1fbd-4b2f-8e7f-9b1e67baae9f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YZKAFTN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1A1P%2Bs95wH3wVKDv4HVcgXIqL9Cu%2FA8eRngEC4YPOAAiEA2kxw4Ravqp1Z2V3S6JQfkxMRBssCsRWwgcCNUaJb9vcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDPwPZQEFqwImrG57USrcA2aD7v3%2F4Ova8SDyPhk7v3T3JT%2FMJbuCJUcZGfqbeV4fCNo4FArZqv98J1f314v9UybnnB%2BYky4f%2F%2FgwS2xo9QHDF9wdHXCPq%2BAqiGv4alUkCSlkwTsyWKbqsoK8zKkQL%2BC%2FSe4uHvB44TA0N4ohUQ5nxBP%2BUiNO0IKbx6igwBHe2ROPG6BoYvjxjgaDr%2FhsIn6llxVUATIzyDAFTI0%2BtB3YA0%2BLXebuc5uX57FBp5zUrnoQr%2FkVyhoiJJXhCe75t0He5YJQg6He5C%2FZhCtCDdRkk3QfOb7w0PQITUjincuBZps6v%2FnDF8wTF8ZCkdIKRnI1CxQPUssJO%2BUsA%2F%2BQX6lyIWPSE43lrDxUUhaJZYvKzFRoRmrg%2F%2BudJKy74%2BlWlTEzJChW3UtinOjEKO0JXDZkmJVOH%2Fw1y4LNP0LoweyMLFD3%2FbsuRkYZhilON0GK3unJ2Yytcj4%2FRjzFbBUNK6Xkpc6fpGxb9NqOrPwNZbO0xsaijbLG3hqErcWNASTBoVkTnXSqY3JM6WUbFh84PJTX4pRmfiXyTtQFgMtTkBRTHjUDyBQViz1dp8W2E3gp9GzONYkjHGjnJIUr%2BAEZf5Frd5PmdZ8KiwSnfMIMnK3gpWF0IsZGYYrGdUBKMLLx2cwGOqUBd6KDblPlKe4p5HAiwCG%2FdlYYnBBZHIdI%2FIOUnTx%2BWa9hDXRkwspwFW2USvW0apT6hvsgjl01eUcDN0na5zAz1TzNWGxy8rarSzygylLVy6quPoC8rNfpvkQxynxO733ctROoQ8u8aSxcXshv%2FkrbT2alakni%2BnGt6RGxE2CbANm%2FpaHRnFrni0Rdian1B%2Fls4bc0gq%2B%2FfUyEby9guL26ARybUx5x&X-Amz-Signature=774243e56b6e2e799403446b631a8d22a0aa4f0e6527a01760d9c6eece34654d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/197a92cc-1cee-4231-91ad-eee396238c48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YZKAFTN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1A1P%2Bs95wH3wVKDv4HVcgXIqL9Cu%2FA8eRngEC4YPOAAiEA2kxw4Ravqp1Z2V3S6JQfkxMRBssCsRWwgcCNUaJb9vcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDPwPZQEFqwImrG57USrcA2aD7v3%2F4Ova8SDyPhk7v3T3JT%2FMJbuCJUcZGfqbeV4fCNo4FArZqv98J1f314v9UybnnB%2BYky4f%2F%2FgwS2xo9QHDF9wdHXCPq%2BAqiGv4alUkCSlkwTsyWKbqsoK8zKkQL%2BC%2FSe4uHvB44TA0N4ohUQ5nxBP%2BUiNO0IKbx6igwBHe2ROPG6BoYvjxjgaDr%2FhsIn6llxVUATIzyDAFTI0%2BtB3YA0%2BLXebuc5uX57FBp5zUrnoQr%2FkVyhoiJJXhCe75t0He5YJQg6He5C%2FZhCtCDdRkk3QfOb7w0PQITUjincuBZps6v%2FnDF8wTF8ZCkdIKRnI1CxQPUssJO%2BUsA%2F%2BQX6lyIWPSE43lrDxUUhaJZYvKzFRoRmrg%2F%2BudJKy74%2BlWlTEzJChW3UtinOjEKO0JXDZkmJVOH%2Fw1y4LNP0LoweyMLFD3%2FbsuRkYZhilON0GK3unJ2Yytcj4%2FRjzFbBUNK6Xkpc6fpGxb9NqOrPwNZbO0xsaijbLG3hqErcWNASTBoVkTnXSqY3JM6WUbFh84PJTX4pRmfiXyTtQFgMtTkBRTHjUDyBQViz1dp8W2E3gp9GzONYkjHGjnJIUr%2BAEZf5Frd5PmdZ8KiwSnfMIMnK3gpWF0IsZGYYrGdUBKMLLx2cwGOqUBd6KDblPlKe4p5HAiwCG%2FdlYYnBBZHIdI%2FIOUnTx%2BWa9hDXRkwspwFW2USvW0apT6hvsgjl01eUcDN0na5zAz1TzNWGxy8rarSzygylLVy6quPoC8rNfpvkQxynxO733ctROoQ8u8aSxcXshv%2FkrbT2alakni%2BnGt6RGxE2CbANm%2FpaHRnFrni0Rdian1B%2Fls4bc0gq%2B%2FfUyEby9guL26ARybUx5x&X-Amz-Signature=122e65557bbd78b5e68b7acd915fa734c3660a42b376fdb1bd19d7b8ce10cc27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. operator가 1000TON을 staking 후 (정상작동 확인)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0c914276-e248-445e-bd2a-fe40606faa6f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMBH3UD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqKylQT8QW5cq5JLaxh7n2eR1duA5gQ3poy%2BFytjulsgIhAJ6erj0EWHEyApqGOitYZqNVB3ccMaNGkkMem2V0BtlqKv8DCHQQABoMNjM3NDIzMTgzODA1Igx4aIhUY%2FtV%2F9u3aw0q3AO1uXmNJcZyGFhEQI0SF16NdU0C6mP53%2Fl9yr5J4kslUBPdkG01dBBLO%2BvBzWw6XUbg8qHR2WNLZm5UeRVl5LjFjlPOGv4myE5Z8iDFZ6h5kNdEvVvW4724xrDlC4vR2yTl4FKjd%2Bx%2FKyFUAZBIZROVUIqD%2FJPcHGkHZwvBuYpbxIRG%2FnGMkgkdquiSRXM%2F4Eeh61LU6JKCKywxfX0s19RsUpIc0J4Y3tT7wG4FjoBnDVX4it0mYO%2FygxdwTWFWenXiIk8CtAUvncFclOh7%2BhQsv1bAosOTfrljepTDcy5s%2FHvHEE4%2FMd0c7liKiYDNTrAAc6DO4nfn6fmdboni1tFqYUuKdQ7Udp6Octs1HfNhmkF3dRWzeU7vQP9zpR4iPgKjMq%2Bso50mRfPXKDPZ%2BlQGIdgR6DlCpIUblYgoHzIfO6lul7qREd%2Bm2wiDuw7OHJyGLM2jnEM0TEnBNURCOf84z0WIxGdmqMDYVQQW2Uzr1XBt8IvyBJppblNpjJmC8rl5mUvh89%2FQtWaiRFJ7e8kOwRZ4J4%2F4mkA1%2FHBKQQgXSChBKp395OgmvQUVXVkdosiY075z6va2I9r5hqTWPgs6rHZZrnomUXUX5tziMmN3YyX3Hv1HGuV2X1Nw1jDP8NnMBjqkAe38WMOZV2Ptt65NI5%2Fku%2FQOCnKG9dWfAnezwha9R2t%2BaTjp2KYWsdIQ%2FgdNbbGy5ShvlcasyKJqZKgV0JHljj%2Fjw2XNgauyztnCLZmZKQoTXfgyZ4b36VUX7xYfqv%2FrWJEqaBUyy69YDno0zcctL761MyA3%2FvnKAuzKTGUsgwlh1uKed523a%2F%2Ff5HnEYUvxcHnFZeBSJNV2rhUPWVJOC1V9prvz&X-Amz-Signature=eae5e88c5da425fbbc1e3e54a1f0acec1d69ae7c6c5ec7f5958ed7646ac1da64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c34351d-f22b-43fd-95da-df40a71d2f49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMBH3UD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqKylQT8QW5cq5JLaxh7n2eR1duA5gQ3poy%2BFytjulsgIhAJ6erj0EWHEyApqGOitYZqNVB3ccMaNGkkMem2V0BtlqKv8DCHQQABoMNjM3NDIzMTgzODA1Igx4aIhUY%2FtV%2F9u3aw0q3AO1uXmNJcZyGFhEQI0SF16NdU0C6mP53%2Fl9yr5J4kslUBPdkG01dBBLO%2BvBzWw6XUbg8qHR2WNLZm5UeRVl5LjFjlPOGv4myE5Z8iDFZ6h5kNdEvVvW4724xrDlC4vR2yTl4FKjd%2Bx%2FKyFUAZBIZROVUIqD%2FJPcHGkHZwvBuYpbxIRG%2FnGMkgkdquiSRXM%2F4Eeh61LU6JKCKywxfX0s19RsUpIc0J4Y3tT7wG4FjoBnDVX4it0mYO%2FygxdwTWFWenXiIk8CtAUvncFclOh7%2BhQsv1bAosOTfrljepTDcy5s%2FHvHEE4%2FMd0c7liKiYDNTrAAc6DO4nfn6fmdboni1tFqYUuKdQ7Udp6Octs1HfNhmkF3dRWzeU7vQP9zpR4iPgKjMq%2Bso50mRfPXKDPZ%2BlQGIdgR6DlCpIUblYgoHzIfO6lul7qREd%2Bm2wiDuw7OHJyGLM2jnEM0TEnBNURCOf84z0WIxGdmqMDYVQQW2Uzr1XBt8IvyBJppblNpjJmC8rl5mUvh89%2FQtWaiRFJ7e8kOwRZ4J4%2F4mkA1%2FHBKQQgXSChBKp395OgmvQUVXVkdosiY075z6va2I9r5hqTWPgs6rHZZrnomUXUX5tziMmN3YyX3Hv1HGuV2X1Nw1jDP8NnMBjqkAe38WMOZV2Ptt65NI5%2Fku%2FQOCnKG9dWfAnezwha9R2t%2BaTjp2KYWsdIQ%2FgdNbbGy5ShvlcasyKJqZKgV0JHljj%2Fjw2XNgauyztnCLZmZKQoTXfgyZ4b36VUX7xYfqv%2FrWJEqaBUyy69YDno0zcctL761MyA3%2FvnKAuzKTGUsgwlh1uKed523a%2F%2Ff5HnEYUvxcHnFZeBSJNV2rhUPWVJOC1V9prvz&X-Amz-Signature=3fbb99dc21e5129f496b97105c1c385665d4135176df983fcdd65f73b580a141&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- [ ] no staking reward라고 뜨지만 unclaimed Staking Reward가 쌓입니다.

Suah 
