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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/9837aa8d-6138-4b46-8e6a-eeed6ded3e4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMTEXG5A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBKGnQURjtSEoKrs03vOj4%2FDFfLAv3BBes1dHouQY8HiAiEApzM0F%2F%2FlhjN8vaaF27CTxTwsqPHiGixTp4u3AXMhnM4q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDC00BYdPxhlPfBTFeyrcA7C7tzRECLQAvHAYi1ACDqBXOaaYTGVqKqK0CllFZF1FWlajZvXgDKS%2BF0r2fOZprSHoypmam647DCuJissMCVvj4zSuunmVVsb%2FPX5t%2B%2BOYpXj7%2BnDNvWH3jeCBXD%2F3A%2BW9r6yvjLDns6NVC6F1vvHYggm5np8T74kpN9IGb2DcK6792quIGC3kfpEh9w816bXxGj5oQJpgN7SlrZSRsVEp6jabi0ZL%2FmAASSFASzgKmDf18iLqm2FY27Bt9PHJ9lQSkIC70YDGuTjwWhyNLi9vQsKaCJTtCwVn1WRuWCRv5mBPHGp8i3pj01GwzaUzNDOm9q1Si0CzCmbucRXomEf0oyD4NLmOdDkjOTeSuGsJPW%2Fxdg%2FhLXuEv9SODX%2Bcw20m8gTJS%2FAj2hmV7BCSjoLJ5f9LENWbXL%2BfZwvVjuM%2BD6F0G8GB7DS05itI%2BKz8gd4FF6ujX8x1Ak5XmvVjHIRWfd2R2vT2R1kmQonK0Z4Ce6wZptgbE2Z6NGF6vUyfhnr6CJ8atd59ynqecAZSiXGuJP8rxv53ACmEIVloVk%2BKoa51CcZs4koT2D0pMideSM3lXpftQpTw%2FdD0G%2FYDdGx3eKBOX3gtU%2Fv0dutH71owYKKbgw5gLNGFsRDVMOnu2cwGOqUBQGvO7b4R%2Fo2Dz2ZhyNi788nxysFqrOCinZAY%2Bksq1y%2FWzrxa%2Bj1UzBWtoT%2FrWOfUQBKjQ%2FA4dHKihgEf02EWyf%2Bx24mOF1DV43alhlEJa0pBXd%2FXG5dPP7SVGOMNXbiB1gNOU9pwJsU8D%2BpKjOfJF9x4O08gRFDqsAqq4S%2FmkhIHnTzCxoe3clp3iCHFPIBC%2B04XqDqvktaDDq%2BeJ%2FBTJj9cK99B&X-Amz-Signature=f308edd0c5428dea86c95bc97d4b96a80b93949230117efffda632ee0873b516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Zena

### Justin