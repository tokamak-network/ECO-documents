# Thanos standard (Optimism)

It may work on the Titan and Optimism series based on Thanos, but it may not work on the Arbitrum series.

Deposit Token : [https://sepolia.etherscan.io/address/0x757EC5b8F81eDdfC31F305F3325Ac6Abf4A63a5D#writeProxyContract](https://sepolia.etherscan.io/address/0x757EC5b8F81eDdfC31F305F3325Ac6Abf4A63a5D#writeProxyContract)

DAO Vote Test : [https://sepolia.dao.tokamak.network/#/agenda](https://sepolia.dao.tokamak.network/#/agenda)

# How to test (Sepolia - ThanosSepolia)

1. Deploy the L2 DAO Executor
  1. github : [GitHub - tokamak-network/ton-staking-v2 at L2-DAO-Test](https://github.com/tokamak-network/ton-staking-v2/tree/L2-DAO-Test) 
  1. need to Setting l2crossDomainMessenger Address & l1DAOContract Address
    1. l2crossDomainMessenger : `0x4200000000000000000000000000000000000007` (Thanos)
    1. l1DAOContract(L1DAOExecutor) : 0x109c37fdB56850A6dfd0e29290860B423c25f7e6 (Sepolia)
  1. Deploy & Setting 
    1. Deploy : npx hardhat run scripts/L2DAO/1.deploy_L2DAOExecutor.js --network thanossepolia
      1. DeployAddress : 0xDe6b80f4700C2148Ba2aF81640a23E153C007C7F
    1. Setting : npx hardhat run scripts/L2DAO/2.setting_L2DAOExecutor.js --network thanossepolia
1. Deploy the L1 DAO Executor (Sepolia)
  1. github : [GitHub - tokamak-network/ton-staking-v2 at L2-DAO-Test](https://github.com/tokamak-network/ton-staking-v2/tree/L2-DAO-Test) 
  1. need to Setting l1crossDomainMessenger & l1DAOContract & l2DAOContract Address
    1. l1crossDomainMessenger : `0xd054Bc768aAC07Dd0BaA2856a2fFb68F495E4CC2` (Thanos)
    1. l1DAOContract(L1DAO) : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386 (Sepolia) (no need)
    1. l2DAOContract(L2DAOExecutor) : 0xDe6b80f4700C2148Ba2aF81640a23E153C007C7F
  1. Deploy & Setting 
    1. Deploy : npx hardhat run scripts/L2DAO/1.deploy_L2DAOExecutor.js --network sepolia 
      1. DeployAddress : 0x109c37fdB56850A6dfd0e29290860B423c25f7e6
    1. Setting : npx hardhat run scripts/L2DAO/3.setting_L1DAOExecutor.js --network sepolia
1. Deploy the New Cross Trade in L2
  1. github : [https://github.com/tokamak-network/crossTrade](https://github.com/tokamak-network/crossTrade)
    1. Deploy
      1. Proxy : 0x0c448437EDCb2a093266dF30619924AE8131b9E3 (onlyOwner)
      1. Logic : 0xD6e99ec486Afc8ae26d36a6Ab6240D1e0ecf0271
      1. Proxy : 0x0e498afce58dE8651B983F136256fA3b8d9703bc (onlyOwner2)
      1. Logic : 0x70956c3E8492a0FB6986e9ceAA84CE27A0999fd9
  1. AddAdmin to L2 DAO Executor
    1. tx : [Thanos Sepolia transaction 0xe70ef665f5979e0537d62f5a8be2a7558a25aaeea6a2b6654432b7a9e986c639 | Blockscout](https://explorer.thanos-sepolia.tokamak.network/tx/0xe70ef665f5979e0537d62f5a8be2a7558a25aaeea6a2b6654432b7a9e986c639)
1. Execute the DAO Agenda in L1
  1. make the script : npx hardhat run scripts/L2DAO/DAOAgenda_L2initialize_sepolia.js --network sepolia
  1. AgendaCreate tx : [https://sepolia.etherscan.io/tx/0xba9dc3c12891d3c7f9b76912f9652cb7f7979013f6f39f3ca299a077ac8a71ee](https://sepolia.etherscan.io/tx/0xba9dc3c12891d3c7f9b76912f9652cb7f7979013f6f39f3ca299a077ac8a71ee)
  1. Execute tx : [https://sepolia.etherscan.io/tx/0x807dc79b113b20650d397b8388e01ecb22d5f180bc994c9a64558e8bd971ccfa](https://sepolia.etherscan.io/tx/0x807dc79b113b20650d397b8388e01ecb22d5f180bc994c9a64558e8bd971ccfa)
  1. 실행 전 
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/becec8ae-47a8-4997-a714-5f3c9e97f536/2FEDEDAA-F033-4FC0-9BAE-553367BCF828.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AJMMETH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfOjRav%2B7rWunzWQP8094EyHt9as5FXiY7L8imQxPeFAiAHA%2FJ4LWc8mqLJJtJJ7NqE%2BKvKG4CwTE3Glpd3j1hqJyr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMSdlgEFpgMDVxE%2FzpKtwD7Tz4N9x9%2FeOuhcd5bqnnbdFzIMrs2hWqX3gsG1FUL0aw1ysXQphKLK2J5tXiEuT7Ptv4mcO8PMGYsq7ARwqJNAwy%2BQlArtzfrUFtqdf%2BfFtHTiuIPq%2FjHUHmT5N8aMB3kG9m20wZvgrocvJ4bD%2Ft%2Fz6gXBkYDo%2BOb6QjYK1102ZxywFrkGlEeH8agnpFbpZtynq1Vl3kftI2%2FrTphPOcxHR%2F%2FjVhwTmsCPI%2FSxtXRjSd6JTZCs0zHQVP5Osl%2FIgdxTCrmJHApayUm1d35ewO9Y2SVd6axV6lVxMCuPeOh0EGvqF0W6MciV1bvUrlzJNduM%2BL4V0sHfGA5Q%2BA13Y9UuerQIbuYORMRC0N%2BOrBsL%2BP4tJHSVxP3cBz4a1hOvFMgf4fHUBFao1CGeHtLdKzffMlYRi%2BqhDnopFrYklFQnJ3e2MGfXVUm081Jow5Ks5McBr78V96H8jHXUYLecgDbYMV1Z4IxuCDhHbJQtQA%2FOzqRAEIQ2KN1nTjkDCHUUYXzpe9AZ12LHoXkpPPpFkqhCHryqUBnOcIt%2Bi1vMgrSUc61w8O550aHNLHFvfBCwzPXLYfHcFuDiD4h3bMrBveF3gZOBRq%2Bu2KsIgS6eHOMFZOICelyauX7Q%2F96gEwpsXazAY6pgEXyl3ucYePO9JY%2FJUPmLy%2B8WfSMXde8W9w5053e4PTCQibM9QGrPxM86HCqnfSVk1dgpkmfyBxWUmwWr76LlZVsY%2FG3uoEY8pLOofcH2YTNuF2t3FsLzhTDjyCt4xCYOhRNdhaHodGICeosHslNaWJhsXEY8sHGsNdMouePluA2bpTGBRGbfxG5aQIKF5nwEA%2B7zNb3CXsCgU%2BaGhoHhVACxoEHtJN&X-Amz-Signature=979dcb44acb8f4bf2f284647dae4d91735f13bb228a703a344d806c0e96e7611&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. 실행 후
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dba1f7cf-ac38-4dfa-974a-300582d93075/FE03EBAB-6F8B-4579-85FE-639D0927B8C0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNEPXJHW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAQV2Vachkzobs7qbJZLkpweGDzHNAnEC9%2BkBtVwhOzAiAgqgsBuaRXpUxU5mpSCr7iQBIHgGliyxkQDYn4TUV0Air%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMcUh0BOeEQmxcetFFKtwDbFqwTYos%2FD%2BKjCaDTgNlnqp9s7nv%2FMR4xXGbudUPcE5pDEjX8H2OmpSt0QOo4X4BoMPLRdUaIhhTkpC3NMvejPOogly%2Fa%2F0IY2htE8nB1L3vMbvOigljNMCT2NFshs8Kr%2FtE6aL%2FC3%2BDz8YLOcvKnfR9cOHdNr1g72SRqesoAPgEB4PFmi1J3A8Ov3m1%2FiUH9aHAI7lbHr60VRFEIeeEw65gCnZkZW%2FnyN%2BttX40Tgyy6hp2ISpaCQCFNrM99tx0Xc5Lnw8u3tI9vIyCURwI8UHkjsSPnVLl0BJ8gAocrkteywvfPIdZIBnTGyLWZdKZtew3jGGG%2Fqr5psLzsFtGqGoy3Lw0DSiMrBgy%2F1LqhwynYtz8gkmvbf8Cv%2BIT4pSej7hTwLWOTkntMBbfpxPmtYMKsxSnVgabdhfk0%2FNIA3xSGyoBQtllxDzda6uIo5zef3vjzBnTnsGAiiY2OgXOZxPk6iez0O9uFViVlEx8p1POOT1NOXvT%2FkUPZvHl3dI%2BMeX5zHwrnl3HBxEmmyprvOjMXctR5ByL%2FDaZtpXAtEQxL49RJzgSZwJfi%2BtgCk%2Bo%2FGjj%2F467KRsHpDMeAq1XHA9PVGz%2BvUyfLtJGxSvU64%2B%2BAVF9pjhHSN2x2oEww8TazAY6pgG%2FPklKcMVYIt5X9xBsjmjU0VGnmRyfkFrJ7SN16avjduOCBayC638D8YxEjD5wqzFct0Y3zYx%2FcJEKXwwyrLh2jInlM8yE2RGGfStWloqYp92XTfBQ6ES3kQ4uJv6cOtJZxCh7OhzfVqh3SHHmOFOZuWZuSxb1%2FpQgxHygFosWIWakFg0TDVQOFRXSqlhemKnfXne1UWs%2FbzJomrO6z7ob%2BfokJuA7&X-Amz-Signature=35a65e1df4a83086134d1797f2db7d537c5e03801f4467bfba141e1dbb4ef248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# How to test (Sepolia - ThanosSepolia)

delete the L1 DAO Executor

1. Deploy the L2 DAO Executor
  1. github : [GitHub - tokamak-network/ton-staking-v2 at L2-DAO-Test](https://github.com/tokamak-network/ton-staking-v2/tree/L2-DAO-Test) 
  1. need to Setting l2crossDomainMessenger Address & l1DAOContract Address
    1. l2crossDomainMessenger : `0x4200000000000000000000000000000000000007` (Thanos)
    1. l1DAOContract(L1DAOProxy) : 0xA2101482b28E3D99ff6ced517bA41EFf4971a386 (Sepolia)
  1. Deploy & Setting 
    1. Deploy : npx hardhat run scripts/L2DAO/1.deploy_L2DAOExecutor.js --network thanossepolia
      1. DeployAddress : 0x988A796F5ca1d4848d00daC1c17d0A2Bbca18a9b
    1. Setting : npx hardhat run scripts/L2DAO/2.setting_L2DAOExecutor.js --network thanossepolia
1. Deploy the New Cross Trade in L2
  1. github : [https://github.com/tokamak-network/crossTrade](https://github.com/tokamak-network/crossTrade)
    1. Deploy
      1. Proxy : 0x040D333A908322eba974A8d40996f1367F2a2593
      1. Logic : 0xA2C90A682DC0849e9Ed8B781E06a73441b5CA1e6
  1. AddAdmin to L2 DAO Executor
    1. tx : [Thanos Sepolia transaction 0x923731c05a144da591be87b7da98179a0291f72fdca6a8d769595da992261cd2 | Blockscout](https://explorer.thanos-sepolia.tokamak.network/tx/0x923731c05a144da591be87b7da98179a0291f72fdca6a8d769595da992261cd2)
1. Execute the DAO Agenda in L1
  1. make the script : npx hardhat run scripts/L2DAO/L1DAOAgenda_L2initialize_sepolia.js --network sepolia
  1. AgendaCreate tx : [https://sepolia.etherscan.io/tx/0x6077f5ac7071dc3e0a9739484a743987d59174b4de87ed39ab32db401ca3661f](https://sepolia.etherscan.io/tx/0x6077f5ac7071dc3e0a9739484a743987d59174b4de87ed39ab32db401ca3661f)
  1. Execute tx : [https://sepolia.etherscan.io/tx/0x8b00d423cbe53bcbf76c25e86acd5bf9f46bf1664617746778e574739f2793b6](https://sepolia.etherscan.io/tx/0x8b00d423cbe53bcbf76c25e86acd5bf9f46bf1664617746778e574739f2793b6)
  1. 아젠다 실행 전 
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/03d6f7b2-ed9a-4d55-a85b-b954049c2ac4/5002B166-0A4B-4AFE-8695-6B350002CEDA.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAJQKVGY%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsgtSafhj3BZ3lZx0fNSxv%2BvhdvNbiDcaqNgtyDwXuMgIgFckFbRahW040%2BY9rMCnNfRM9%2BQhz5dUJH1SjQWRv3Nsq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDKbA6uLf%2FCb2KpfBrCrcA8iIOK%2B8xaMCK8RYzvaeZPDYUcsqKX4UTYZB9wBIon1VMsN%2B3%2FXEDSoPPN1Mv%2B9dbgOrLP%2Fn%2BfL2W%2BdvFcy10aDCPEdhBYKm8zHkTyoVsum%2BUtPzpKIyVkdP%2Fj86%2FZtv%2FLSQo54i33zdiami2AuHkGY9sV7u7%2Bh%2F9%2BX5vD6ncKfcqUxkfmGKS%2BDuRGCLiXuHMP5zRf2WBAUEOPnVHdt0mVtcA0bWgxXv6c16B5SgHTjfF8A9RrTQfS5rpQhfcaBMzjPXzv0J5%2FbNR%2B6cy9r6NcnSCsm3k3JU%2BCsQhpjWaG95YlEgmrGK9QHCyWBrOj0gqtFfRinlnYLUp1gqWPIncRDgfwl5uzf2O81IKPTg4HoBwtYZrKAIc%2BSGuO2aE6VqgcNSdU2O4CteXsGc7woPg2cmRoCeRMAwaw7Rj2oR0dhHd6u7ktVK1VDuhBdpl8Z1aolF2TNUU%2BhAbSkxg9AtD9DpBy1pw6TSCUFFemMfTWStYSanf%2F9pY3KynlSwns4Kzpy3uklYkC1VA53KMabnE%2BBtSL0MpY04hJLcABqLTqCCelxXTnoHly7N98lbMWf3UFtn3sa8iH3jwczfrWYJVq59iiBTdPx8S1dbJkwO8cy0imQQpVt4fZl2L5YHMM%2FD2swGOqUBPaYQMtZNAplHQSKZiBa2a8mMxZNc02Na5R4x9HBIu2N9GIThAhholgBtx8qGisLNiW76Z0He1It33337thNf6DI7cQbmYZjwzzb%2BZNvoARTSkV0dfdq1FwJAN7MnV4AyeaiXWV%2BqZPvUv0hceZ2kX9Ft2cXzEOVW4UrkAT96cIHhgPpqu6Qf1BkGz9rsilS%2FH%2BteK0piDoXP88dKUzYDWL%2FLhkKa&X-Amz-Signature=a78b9fc26d72be621998301d797886e99a539246709613f1c94d63c6c8c90774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. 아젠다 실행 후 
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/bec11283-9ade-47b7-9683-e771894e3f96/FD027BE0-AFB7-4217-99F9-3DDE6E5A100F.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URBSQANH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDc3PkdmLOk6YoliLcxaqZexYmqPZZmz6MHaHccpwusXAIhAKXqHb412CSfdJoI%2FEyIHtTaS3ChBNRfffmKVzoDdM2yKv8DCHcQABoMNjM3NDIzMTgzODA1Igy0e23G%2B4h60DtvWlYq3AOl4uyauiodEiAy%2BSjyjwtzAojFZBxBOg7PiY1jGso3FBB%2FJARO4FPiRM5u%2Fe4YaVPa2856Avs0P7c0Ylat7MMxYzMKVBu9bGYW%2BX6iWhEnqhLv9TW733q4CO9K%2BV7zVnDSpTm3HWoZyvSDiMRgcUClSBilCpwihPEt5RECtBvaZsMm4mKdtRRZ7U9KJQ1%2BfTnNj%2BSUhkQw5UButNUWNrtUQ7oBOKSxJhT39TSVKFBONZ6w%2BpriORb4eseYzLwMLZfp0pg8S%2BHyo2wboV2Q5stTcBj6W9DYBoCqRo%2FaiwKmI6ACJAJCbmB5aRGk8TYhk1H2SngJ3LvjHtvJIVP3g%2BIALw4Zi0g%2B7wOtm6tT1XPNA1uvl5ZsuJNimblsBdzR2H%2FQEkVY3P08LtMD7S5AIgPX4f94WxnOJSn8COHuH0inQ%2FvPRbW%2FdSZMbzi8BTZExQIYv2lxo9%2FDLciYI7%2FdWBr31cWS0MHBUuNV3%2FKXpUepISXE5HbxdRT5A7F3q98WUOrLpY7w8FDvpt2FG1En6sWFupVKtZHkoQiWRza0lT7Eu2Jt6RD6mpEfcg04pe8lGz6FHTV6ap7qhMmEUrMNSLBmsp%2BHtrTr16VXrSO2B9a4lVL8AfAYks7oXeYuATCJxNrMBjqkAQXESj2VqeT9DSLvwJdGqCy2haLIkq5s2XvBKAmszZ8lsNYxk2npxU7iR7cIymkFch5dY9CuAhfj8k36f%2FeP5zEWLgoHuDVhRBjrT2Tua5KUaC6%2FQajyysSzCwe%2BpmrfdIJ0HvHslSKJ3ROO5YMzf8CXB9bdGFLHzicEUCd%2B9f4d%2FA%2ByMm4NoPRbHIqd%2FRzzwLiv2DLVap4HjbZQi81aYRIWYi91&X-Amz-Signature=7f43488506dbd1d86eab9d774beeac58cf664ee0a6d509298cb984a3e9833922&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)