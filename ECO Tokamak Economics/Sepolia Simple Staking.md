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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/2e77ee50-1fbd-4b2f-8e7f-9b1e67baae9f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWGQ5NP%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDN8aJY%2Bna60U9Nfa3fxwgce4GW49nfYXSBH%2FnIyjZm%2FAIhAKTX2HVdCYgequUWVcUQO5ybcdMMIv0T8R6hGUqrFHJlKv8DCHoQABoMNjM3NDIzMTgzODA1Igx%2FmxMzbAHl7edDz4sq3APIIhZzdpnQQykezu9KgctDY4oz6RLHHckRC4aPDy3Q7NgogNi4I%2FkuKXAnvvkSQJeLCssdMR8EVdO2A%2BT0CN5whL6PjS1wbd8PV6zAdXyFBTQACviYLETz4DfUkD3jCdN7wtXsqk1MDeqV%2BQksQSXGAxF94jgstGrlpVnQ4WVggVFSwXf6%2F6misXVogOzWIDSniQoOVax%2Bw9nbfkGSDTyT3DAtnfzwcKUonT%2FKFXYChpcIpoXVYqIe4kO89vIUq9LwXlt%2FQv7eGP%2BHXS%2Fyr%2BPltYzPdNHIJxvpNAoyZassYF01vb3nT45r%2Ft9%2FIFPtFfItBXLRbEb5s0IIhNvFc85ea5OPGTwHtfV8fqFFdEbCHXfDoEJtDqeY7Me5xbROuRoK7OtFt%2F62Mz9rQaBDmR5Awn889GSacR33zKVQmw3VCD9jF9wfiSsYuXfYYUWYiUQFPYe5dPglWB7yaAUgsfT9spYX%2F3f90xw9VNdiMTqrj7c7V6mYKGgyjU4p5oHmlGgT2wvjVFpk%2F0KAHRCIVpgGcxiq5HQmkJX8zd3JMk7H4Ry5Xhj3wWZIGNch0Rdovw%2BAZL5yvAx1FEk6IMHPKdIKbDmWrBvijwz6ef8RkeC6hKe2WgvJD%2FpSz8IlOzCvmtvMBjqkAVQyaUrtVq2qTO4NR84uUl9KS3oDnzIWiIms9AcVQc%2BJmpLxXsBwQ1lv%2FCtjabeKCgbkmXUwMgyuh1Z0BrOweljGx%2BnTxWoFOCVuMmGgIIoesuIzcR%2BYVGDhve12WFpbKde3G%2B%2BulY5rrK9YVhi6%2B8jvIy2LFnxPZwu4yguLB2ErzAeHKIjsS0CvRwaUQC4r9kVflVptik%2B9P3I9m%2Bsn8O2nhrzF&X-Amz-Signature=737ee9161a3edcab0a81fec59da21bd90e5f8fb4f71ecf72348d300a1401d598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/197a92cc-1cee-4231-91ad-eee396238c48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWGQ5NP%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDN8aJY%2Bna60U9Nfa3fxwgce4GW49nfYXSBH%2FnIyjZm%2FAIhAKTX2HVdCYgequUWVcUQO5ybcdMMIv0T8R6hGUqrFHJlKv8DCHoQABoMNjM3NDIzMTgzODA1Igx%2FmxMzbAHl7edDz4sq3APIIhZzdpnQQykezu9KgctDY4oz6RLHHckRC4aPDy3Q7NgogNi4I%2FkuKXAnvvkSQJeLCssdMR8EVdO2A%2BT0CN5whL6PjS1wbd8PV6zAdXyFBTQACviYLETz4DfUkD3jCdN7wtXsqk1MDeqV%2BQksQSXGAxF94jgstGrlpVnQ4WVggVFSwXf6%2F6misXVogOzWIDSniQoOVax%2Bw9nbfkGSDTyT3DAtnfzwcKUonT%2FKFXYChpcIpoXVYqIe4kO89vIUq9LwXlt%2FQv7eGP%2BHXS%2Fyr%2BPltYzPdNHIJxvpNAoyZassYF01vb3nT45r%2Ft9%2FIFPtFfItBXLRbEb5s0IIhNvFc85ea5OPGTwHtfV8fqFFdEbCHXfDoEJtDqeY7Me5xbROuRoK7OtFt%2F62Mz9rQaBDmR5Awn889GSacR33zKVQmw3VCD9jF9wfiSsYuXfYYUWYiUQFPYe5dPglWB7yaAUgsfT9spYX%2F3f90xw9VNdiMTqrj7c7V6mYKGgyjU4p5oHmlGgT2wvjVFpk%2F0KAHRCIVpgGcxiq5HQmkJX8zd3JMk7H4Ry5Xhj3wWZIGNch0Rdovw%2BAZL5yvAx1FEk6IMHPKdIKbDmWrBvijwz6ef8RkeC6hKe2WgvJD%2FpSz8IlOzCvmtvMBjqkAVQyaUrtVq2qTO4NR84uUl9KS3oDnzIWiIms9AcVQc%2BJmpLxXsBwQ1lv%2FCtjabeKCgbkmXUwMgyuh1Z0BrOweljGx%2BnTxWoFOCVuMmGgIIoesuIzcR%2BYVGDhve12WFpbKde3G%2B%2BulY5rrK9YVhi6%2B8jvIy2LFnxPZwu4yguLB2ErzAeHKIjsS0CvRwaUQC4r9kVflVptik%2B9P3I9m%2Bsn8O2nhrzF&X-Amz-Signature=920361d240c456e5ab8fe6ea8890961f94f834ad15b53e532183efd2d41be781&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. operator가 1000TON을 staking 후 (정상작동 확인)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0c914276-e248-445e-bd2a-fe40606faa6f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZZOPSYI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr2dkJcBrXL4t5RHgFB7N0A5p774bDh%2FkyiGhdJXIHrwIhAM%2Bbah5NhvgT%2FyGndjkOvwKuhVlVTVFYUgkhD%2F%2Bvyn9pKv8DCHoQABoMNjM3NDIzMTgzODA1IgzmNJrRjff1mfEKdJ8q3AP0D%2BHHyQQC56f9fpD94LcvKCSSr7clLIVwBWLlxo6xo3qXddXhjgkTnsvfMrqSJxLeagWFxsCGovNK4vaSqXnRbS8%2Bz%2BBBPZI%2B8HGOLouS5%2Ftlgo7%2FPCbr4qgL8XsuVEHY%2Bzs1bQNA7TFF9FqL%2FozxzL8Z7ftlJVye2D4NrTV1S810Hu9ut7imH4%2B7BkWF8OGz08No03ZcpizFuINMnz4sB5SdP%2F8Dlmyv501%2BIn%2Fr4c764avlVFYyf03lyVwqonVEFD5Z1HNRCL%2BiZ1ulsqe6crYnzeSVWJsFhL%2Bzr0cVmi0%2FTmsXaVLuwhd0Tpp5w0NpnChyk3uY3kQMvaW0pBj9GaQJPP2P4R4WdvGMn19Aa2oFycXz0OYkWEqoAhavfbaP%2B6T8CAO%2FWODBGPhpRDiDXV68JiV%2FaF53H1UPgdmEreztaBG4k%2Fp6ZAA%2BrOEszjUfPAl2gbHiHS5FIxvWxBrBG%2BVD6ORt6igy2%2FhJxmCp5skVfULrEamjBpya8vYF4m3vF0x%2FZXgKvB550Dgj8UGZ0FBxfiFulTrU8ZiXw0sb%2FcEkX%2BeVsmrQzJSHPnDgPQ38CvH56jA1epA8FhVAUu8A5uV5yOsgE68B4T9gJnRfi6lJNqxgPSJwCDdEyzDKmNvMBjqkAbhBASuioSLxUOxvev0%2FvdkDF4SzghJk9euatOCwG610fc52AV0GEgA4ihossC6t6iqTBaHrL6Y29Znbs6UKn6NANqe1%2FOhk%2BrGXrqWfQnTNdVPP1RzNOf%2BgIkQPND0khtzv0xVF9BNXuYOZtmvlG823h0Ci2y4l4pgWBx9IvdEUQ3QqvFCDW7NKMM0BwEZZpOIssoZ8ImAqDMjHtj5IZ%2FoSR5%2BH&X-Amz-Signature=2255c8ae8c77b3fbb9473fcbcfc08a2b63a4d2decb96239bf7c2d23f999f8075&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7c34351d-f22b-43fd-95da-df40a71d2f49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZZOPSYI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr2dkJcBrXL4t5RHgFB7N0A5p774bDh%2FkyiGhdJXIHrwIhAM%2Bbah5NhvgT%2FyGndjkOvwKuhVlVTVFYUgkhD%2F%2Bvyn9pKv8DCHoQABoMNjM3NDIzMTgzODA1IgzmNJrRjff1mfEKdJ8q3AP0D%2BHHyQQC56f9fpD94LcvKCSSr7clLIVwBWLlxo6xo3qXddXhjgkTnsvfMrqSJxLeagWFxsCGovNK4vaSqXnRbS8%2Bz%2BBBPZI%2B8HGOLouS5%2Ftlgo7%2FPCbr4qgL8XsuVEHY%2Bzs1bQNA7TFF9FqL%2FozxzL8Z7ftlJVye2D4NrTV1S810Hu9ut7imH4%2B7BkWF8OGz08No03ZcpizFuINMnz4sB5SdP%2F8Dlmyv501%2BIn%2Fr4c764avlVFYyf03lyVwqonVEFD5Z1HNRCL%2BiZ1ulsqe6crYnzeSVWJsFhL%2Bzr0cVmi0%2FTmsXaVLuwhd0Tpp5w0NpnChyk3uY3kQMvaW0pBj9GaQJPP2P4R4WdvGMn19Aa2oFycXz0OYkWEqoAhavfbaP%2B6T8CAO%2FWODBGPhpRDiDXV68JiV%2FaF53H1UPgdmEreztaBG4k%2Fp6ZAA%2BrOEszjUfPAl2gbHiHS5FIxvWxBrBG%2BVD6ORt6igy2%2FhJxmCp5skVfULrEamjBpya8vYF4m3vF0x%2FZXgKvB550Dgj8UGZ0FBxfiFulTrU8ZiXw0sb%2FcEkX%2BeVsmrQzJSHPnDgPQ38CvH56jA1epA8FhVAUu8A5uV5yOsgE68B4T9gJnRfi6lJNqxgPSJwCDdEyzDKmNvMBjqkAbhBASuioSLxUOxvev0%2FvdkDF4SzghJk9euatOCwG610fc52AV0GEgA4ihossC6t6iqTBaHrL6Y29Znbs6UKn6NANqe1%2FOhk%2BrGXrqWfQnTNdVPP1RzNOf%2BgIkQPND0khtzv0xVF9BNXuYOZtmvlG823h0Ci2y4l4pgWBx9IvdEUQ3QqvFCDW7NKMM0BwEZZpOIssoZ8ImAqDMjHtj5IZ%2FoSR5%2BH&X-Amz-Signature=414d2a96830d51dd8fffbedb87f24782bdc56fbed02242eb25eec32bbcd84110&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- [ ] no staking reward라고 뜨지만 unclaimed Staking Reward가 쌓입니다.

Suah 
