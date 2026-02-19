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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a7223db8-84f4-4835-ac91-15afa4a7f90a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.47.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KFWLJON%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T040200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHrqShd3z8R5pgCQ0kWidT1ofyWw6XJFnaaPfRbukP%2FRAiEA7xvqPD2VxIyGumSXr86mMxK9EJ%2F6hAnZQ7D5YAE2uUAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKMx1Rw7zjNn1ATifyrcA7GhqBnJ618nU9YCzmP%2B3sB%2Fx8sbbYq5AUzdpfuoP21s2Pl2ybGrrR32fD0lhpYPxtmZKQSO4P29Jp3ops1DvskVGg1Y8U4thWMGX4a9CAbGXdr8D50S1ZG6U7B0O1Tvr5A8S4l9rkutkbEfnK8eMuDWn0Wpmqmbd4NB82OZoNkaEYq%2FtaWfqlrrdUUFdqaKYkS6ZqG6LxmRkzBczHA38VHiz68e0rlSBVTA9kKlwiYD2HSsVZeW25hVqa8EkaaKDNmcDPEZ7ILpgwFkb5rZkhE5UT7JWN3gV%2BDFRifi5mm17VIWgkKFaUn199CY4OZSY3RMeQl%2BpS2kTdfps9oh%2Fbtgpfb6Po1ExTpiAuSxNGNMHWJYQanEzYFg%2B1xoUjt9CuUXmmAcIK8Hy4UnyKl97UmYA12fVjm44er%2FKAkNaR06CrOnn7ag56LdQILbiMHPmN0lS72OXSC1Um%2FkT8ttjfz5GFLywUCompSWXWGkWfRMdmmHzIFGy34lzLonhlufszZelDWOltMFCrA34GbqEQ0zJrvyBmleUdKSh7G8Cuj2CpiSmBNJRSZBtK0oVtOlkIBCe5evAE%2B3gYI%2FT%2F0h3NUsvB%2Bjig746AjiR7E6YjbH2Y1SAVGasahs6y%2BkMLTx2cwGOqUBxwNwq%2BBDZAi2Sez4HRymz6T4lnYnbyrutl6pYpnfGoXspGBBsj8tvu7j3r0NQFVNxZLrius9eg6DBQOrBCVOn90ytOvVaqmaGQ%2BAcbss1oKwUDJFsOWatDnnJuAfhJ4r%2FsQ7GWOXbD%2BuBlIUULbfeSpAFIEaCdiyJ4tfhQTcaK6cI16d0%2BS4bVg7iHW%2FDGQA5kJTKJfAzMcG0bRWSpZpfzU7Iwe9&X-Amz-Signature=54a14dca09a8f14287419828a859bc759bfe087cf03540965e678a5d8a819685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)