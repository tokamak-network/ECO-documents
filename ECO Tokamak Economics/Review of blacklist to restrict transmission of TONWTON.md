Channel request : [https://tokamak-network.slack.com/archives/C04E0TV3893/p1719661450342969](https://tokamak-network.slack.com/archives/C04E0TV3893/p1719661450342969)

# 컨트랙 검토 결과 

- TON 
  - _transfer 함수에서 callbackEnable 을 true로 하고, seigManager를 설정하면, seigManager의 onTransfer 함수를 호출하기 때문에 seigManager.onTransfer 함수를 수정하여 블랙리스트를 관리할 수 있다고 생각하였으나, 
  - TON은 setManager함수에서 설정을 못하도록 막았기 때문에, seigManager를 설정할 수 없어서, 블랙리스트를 관리할 수 없습니다. 

[Link](https://github.com/tokamak-network/plasma-evm-contracts/blob/858b2040b67d7de1f7cfa3b477e62dc938ca4499/contracts/stake/tokens/TON.sol#L18-L20)

[Link](https://github.com/tokamak-network/plasma-evm-contracts/blob/858b2040b67d7de1f7cfa3b477e62dc938ca4499/contracts/stake/tokens/SeigToken.sol#L33-L38)
- WTON 
  - _transfer 함수에서 callbackEnable 을 true로 하고, seigManager를 설정하면, seigManager의 onTransfer 함수를 호출하기 때문에 seigManager.onTransfer 함수를 수정하여 블랙리스트를 관리할 수 있습니다. 
  - 기존 전송 가스  53898 에서 250801 로 많이 증가됩니다. 

[Link](https://github.com/tokamak-network/plasma-evm-contracts/blob/858b2040b67d7de1f7cfa3b477e62dc938ca4499/contracts/stake/tokens/SeigToken.sol#L33-L38)

 

⇒ 결론 : 블록리스트에 대한 TON  전송을 컨트랙에서 제어할 수 있는 방법이 없습니다. 따라서 WTON 만 제한하는 것도 의미가 없다고 생각됩니다. 

블록리스트에 대한 TON/WTON 전송을 제한할 수 있는 다른 방법을 고민해봐야 할 것 같습니다. 

# Test 

- Repo Reviewed: [GitHub - tokamak-network/ton-staking-v2 at put-blacklist](https://github.com/tokamak-network/ton-staking-v2/tree/put-blacklist)test
- test : [code](https://github.com/tokamak-network/ton-staking-v2/blob/put-blacklist/test/blacklist/0.test-blacklist.ts) 
`npx hardhat test test/blacklist/0.test-blacklist.ts`

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a7223db8-84f4-4835-ac91-15afa4a7f90a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.47.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4PGMB2C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChFsLwzv8eRoQYen0SRPCdFQqz9aA49rysNjDR08o3QwIhALcpHHjA1PTX5IWPUKvHu0rD4N%2FfL41IwQ8wT8KK7mSQKv8DCHgQABoMNjM3NDIzMTgzODA1IgyPQ9Fi5Sk4POw9YKQq3AMion2iG2NMdpkm2MsO%2F9f%2FaV4%2FwMt9qSaIS8PIR2u8NAOovl7P2vskBATkV7MCz%2FY72yEHXnnJ5gxC12ExTMfzRXiupVUi%2BIj7y6xZbs1qMXrfmBYOJr2UyOjoIyJ0rJQB1lGxomI3k3HkRiu4yVFbQnHTEKIJeamTku5E5dxClJKvZY2H5HCz48Y4d0SrHg%2FsVJiyt8S%2F%2FY7mQzA2P4TZJzCpwrK4dw0pckNC%2BNF50Di0vgNmhF1FNCaRXVv477FXyuzn8vVV2%2BN8qyDkRBJMJcBOox1GLmnqDcmLGvexw9dytpuKp5CO1X5shQJCts99Hyp%2Fq8RNaKAumYYT107wJblP1xeEdIzxnmPy3KjVhaN%2FyPfyvrznieX8v0KbftZOL1%2FxBh8PNMnViKaXt4AEBqHaPQCCFfvPzf%2B7%2Bdy6Awll7na7eeTrwxpgZi5ZdH3VrESmJJ10xzVPzjN5K9ITp7Hgvy8o9R4lQPwrQYv58Ih0G9%2FtrDdLLGQj2iM4ipmArL6RtNbv32m0Yz0tVB4m8vTcyML%2Bhbs%2Bt02x3SA2Z9e1FxmSLQDJM3YKJZr%2FAoSH3ONBF9BE26dHOh5J9dZARDvtF3uN244SlfBMpCn36cIMAiyZbxFeQNkC3jDb8NrMBjqkAbNxS%2FT4YSExy%2FplSL6LWrDdoDdEbvA6FSVummX6vCFCR4s%2FLW4z8SE2%2Ferjxo38YcfAmYZ7Hf%2Byidt73OAAddazkH9jGu2Dy%2B%2B5MPWYS3UVf9LesfX%2B%2FGuMqyv0iyIl1rSU4uMgYw%2FOZ2xE7N52XSjqCW7qPQqpuOHe9gb%2FN%2BYgZU1MoF3g6Ef%2FtkosOR2v4r4PUO%2FwS7sFw2KP5TcwfWLqsCvG&X-Amz-Signature=ae391123a6db92cdb3661c6db43d255a8c618d65c3b925c8feae08a09978c32e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)