## 변경 내용

1. DAOVault의 claimTON agenda 실행불가
1. DAOVault의 claimERC20 function실행일때 address가 ton일 경우 실행불가
1. DAOVault의 claimWTON function일때 amount값이 DAOVault가 가진 WTON보다 높을 경우 실행불가
1. approveAndCall은 TON주소만 가능하게 require문 추가
1. claimActivityReward시 claimTON에서 claimWTON으로 변경
1. DAOCommitteeOwner의 setTargetSetTON 추가 후 DAOVault의 TON주소 변경
1. DAOVault주소, Layer2Registry주소, agendaManager주소, candidateFactroy주소, TON주소 설정 DAOCommitteeOwner에서 가능하게 변경.

## Audit 요청 Contract

DAOCommitteeDAOVault.sol

DAOCommitteOwner.sol

## Git

[https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit](https://github.com/tokamak-network/ton-staking-v2/tree/Agenda_Audit)

## Test

npx hardhat test test/agenda/1.test.js

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/9837aa8d-6138-4b46-8e6a-eeed6ded3e4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7TZ45U3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz2k6U7PukXaWQbhP0AytCV171PytMBnSQnUYUBnZZaAIhAJuKfV14kgf0lkzrFE1ZdsPrpzeBwErQ%2B%2FUO1BK1ibj0Kv8DCHoQABoMNjM3NDIzMTgzODA1IgxkjE56p4nfBsY20Moq3APGiU%2BosOZKd1hqNZ%2F7eCQpxvTjHh%2FCHTL7eCz91ooakNLLFK00ccXxAX5xEUSjdjPkbNIh%2BOnrrWi%2BHMzN2x%2Bl3TswAe%2BXbjG37RWYeuekvgVwLIJXYPdxDD%2FhIgpRX98pGqIcxjN6vtX6WPXLsCn83hZX8XEz%2FS3DGexzkjQEpm%2FSGlcHSuHIccyNW5RS7tV2k8%2BUS3hnYDciby4FhThnHlXyn4zdAZ%2FYKUl66JiVfbqTeguBW6OJ1uuMS%2FAxu9%2FtfI2hY58hVwLq0yDVU0bib0IApOBeMAwXFPcYNtXLSrTdQt%2Fl0sSRGv%2BNJz5ps7ar0IMGCx%2Fac79FZhVbyPZHZgRlvhByL5TqfkooVbIPfYCQg1jFaxkqsAt3k1oUo7Htt20wqokqbI8ifjOxMv9f2NDetD14hL7fSizOSh5Bfs55ZHA9jt5M75HDLNRrIje27uM8tsY6C0t%2FMkk%2BH4GjV8EpytRyIjy%2FxfXiVwe0BkuciWeeQ3YTGAKxWsVCvqziNSMMZg%2Bpj8Dhda2cJOWzkYXvMPTmldCp1IQzwkRmvblQOa27XlarCXlTsCyQ8GLRuYTrKuG8R05%2FVVpvtklOzDS4URH2L8Y8k1o4aBStZxVvmrp%2BiI4nd1QzSzCLmtvMBjqkAR5PISzvBdZxYCSNvCWtr5NyDor%2BNvfcf0gG16mjAZBclQqZ%2FINI2XJELTC3CdtgWkh2kcD6k4QOcnP6pouGyXxj3ms0X5p0yR%2FEjqWOuYRrl7KhR%2FHX%2Bl5tQdk8XU6gTThsq61%2FRVfjrnlm4JHoRJoZQmFUz1FP6IMON3YXFixANriNzwLXLiMbD8RGz0rrUHkz%2B7J%2FYXSI5hnZvenrGAWuFVyo&X-Amz-Signature=9e27d3b690471a9168dedb6def25a0f04225d9b20a2a58f0793afe45fa01db15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Zena

- [x] Z_1. console 로그 코든는 삭제해야 합니다.
- [x] Z_2. DAOCommitteeOwner 쪽으로 옮기는 편이 좋을것 같습니다.  
- [x] Z_3. function createCandidate(string calldata _memo) 함수를 지울 수 없습니다. 일반 유저가 candidate 만드는 함수가 없습니다. 
- [x] Z_4. wton 주소를 하드코딩 하지 않고 스토리지에 관리해야 합니다. 다른 네트웤에서는 wton 주소가 다릅니다. 
- [x] Z_5. 함수시그니처가 변하지 않는 값입니다. 함수안에서 메모리로 사용하지 않고, 전역으로 선언해서 사용하는 것이 좋을 것 같습니다. 
- [x] Z_6. ton 를 하드코딩 할 수 없습니다. 네트웤마다 톤 주소가 다릅니다. 
- [x] Z_7. require(!check1, "claimTON dont use"); 체크는 check1 = selector1.equal(claimTONBytes) 확인후 바로 해야 합니다.   for문 밖에서 체크하고 있습니다 .
- [x] Z_8. parseRevertReason 함수 이름이 적절하지 않은 것 같습니다. 
- [x] Z_9. 불필요한 로그는 모두 삭제해야 합니다. 
- [x] Z_10. approveAndCall에서 bool 선언을 안해도되는 부분이 있습니다.
- [x] Z_11. claimActivityReward에서 claimWTON이 아닌 claimERC20으로 변경되어야합니다.

### Justin

- [x] J_1. onApprove 최적화
- [x] J_2. [질문] onApprove에서 다음 require가 createAgenda를 할 때인데, execute할 때의 daoWTONamount와 다를 수 있는데, 이게 유의미한 require 문일지 생각이 들긴 들었습니다. 근데 없는 것 보다는 나은 것 같습니다.
- [x] J_3. [질문] DAOCommitteeOwner