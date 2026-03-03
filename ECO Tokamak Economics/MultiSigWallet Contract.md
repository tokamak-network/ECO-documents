repo: [https://github.com/tokamak-network/tokamak-multisig-wallet/tree/simpleVersion](https://github.com/tokamak-network/tokamak-multisig-wallet/tree/simpleVersion)

## 정책 특징

1. numConfirmationsRequired = 2로 고정값입니다.
1. Owner의 수는 3명으로 배포 시 Owner주소들을 입력합니다. (Owner수도 3명으로 현재는 고정하였는데 수정하시고 싶으시면 말씀부탁드립니다.)
1. Owner의 역할은 submitTransaction, confirmTransaction, executeTransaction, revokeConfirmation 함수들을 실행하여서 MultiSigWallet에서 실행되는 Transaction을 관리합니다.
1. Owner가 변경될려면 submitTransaction을 이용해서 MultiSigContract를 통해서 changeOwner를 실행해야합니다.
1. submitTransaction을 한 Owner는 해당 Transaction에 대해서 confirmTransaction이 바로 됩니다. (추후 1명의 Owner만 추가로 confirmTransaction을 실행하면 executeTransaction을 실행할 수 있습니다.)
1. submitTransaction은 한개의 행동밖에 못합니다. (변경 가능)
  1. ex) transferFrom을 실행한 후 transfer 실행할려면 각각 submitTransaction을 따로 생성해야함
1. Contract는 ETH와 ERC20을 받을 수 있고 submitTransaction을 통해서 전송도 가능합니다.

## 테스트 방법

```json
//git repo 설치
git clone https://github.com/tokamak-network/tokamak-multisig-wallet.git

cd tokamak-multisig-wallet

//branch 변경
git checkout simpleVersion

// .env.sample을 .env로 복사
cp .env.sample .env

// 복사 후 .env의 ETH_NODE_URI_MAINNET 값 입력

//npm 설치
npm install

//테스트 실행
npx hardhat test test/MultiSigWallet.js
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/1b654185-f2a7-4312-b4e5-3068f4b8aa0b/7CE44755-4345-4201-9B1D-2E3D4E457AE0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROFICQBV%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T084311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA1z81uSbYY2hijxBfcnTz3QnwfDV%2BxQqRojb0MEQMoLAiAwXrz9GfplAZpGCFgnSotrSmogWBFIgL5khLU09PoTXCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMXTpOyKA2GmJ6fHZzKtwDg2Hzd0voCo%2Fi8i0DhO7Gjo%2FDpgW0r1OK287E50iVFdWBVdiBhct9V33fSjwaoyUu65DTsGm2UPlUj70k8Rou69CKti5xQR3xt1grGYCloyVgSXlGTWSg%2Bg0uZGIevU03NOfNDR6Mr5eMZUYlIvaysD%2FDidzvhhwfasRAQAXH%2FF9hFqhEurHqsTJHRjfFm%2B7%2Fr8mkSgopT0qv5jg94HiPAnh4pwPlnnk0XLG8IdvuAnM6JC7G1So51P168NKQl88cVC0LUvdAND7Y5wq2gbJVAESa33FCRzg%2BxEcmunVmjxF2FfBhywJDB1B9um6L5Jy0sWGNsdc5aLYx9L7GReQGdbAxloi8T0KJZ3%2BOZb%2FBxEqdQMO%2B8Ch6jkZ9JXQC1M1Qtb%2BIWhPE%2Bnm%2B9Qm8SCSUMbHyJdWJTtDQCUV%2ByNkFXzrYFFU4QgNsrp5%2BiDuILASJWQSGKbmuwdWBL5e%2BvoQly2pUDJESfowaGRj%2BG3RPgviH3JA5K6qM5LD4HOZBEmcxyqafWtuBZyeLN698wTGFTzZZCWdKkEkA2cytQy6U91pYux3QYWMMxrguHD3I0L%2FNTMuu1OZzga2zML8mpfh%2BLDQ4%2B5ZG8HCGdqNkDJtjFq%2FcLKpDGj66erQUHMUw9u%2FazAY6pgH50E9C%2BgMtKHxvvvAphxocGDRdjj2ASzIAlbqfrOmojM5gqKHdq%2Brth0nYXGaRzRv7pTx9QC4u5GzESFP5jQfjoppFfSUPmmtrvDaIj2e%2BpLRTAenw%2BAIQ3EwlrrKtB5ug7S8f7NZPjiFde7ra7eo9kL5x7mDN3piXaA%2BEptRGV07Vnm4QITqK9dtzR4Z0EA4NPzPD3uIBzMhHqqsCovNeFj8XuwIX&X-Amz-Signature=c36cafc9992b69b316b42c3ddb384513c2e871bc1bd3177a27ff9062d5df57cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 질문

1. confirmTransaction된 Transaction에 대해 executeTransaction이 실패하더라도 나중에 성공 조건이 되어서 다시 실행할 수 있게 되어있습니다. (executeTransaction이 실패한 index에 대해 계속해서 executeTransaction이 가능)
물론, Owner들만 사용하는 것이라 큰 문제는 되지 않을 것이지만 추후 Owner가 변경될 수 있는 가능성이 있어서 이렇게 되어도 괜찮은지 질문드립니다.
  1. 다른 방법
    1. confirmTransaction이 2이상되면 executeTransaction에 대한 timeLimit이 설정 (1주일이내 실행 등?) (해당 timeLimit은 Owner가 변경가능 or MultiSig Contract를 통해서 변경가능 or 고정값으로 설정 등이 있습니다.)
    1. 실행했을때 실패했을 경우 다시 실행 불가 (이것이 더 간단하지만 위에 방법이 더 좋아보입니다.)
    1. 지금 그대로 진행하여도 Owner관리만 잘되면 문제없습니다.

## 추가 변경 코드

1. executeTransaction 실행 후 해당 index로 다시 실행 불가
1. changeOwner 후 이벤트가 oldOwner, index, newOwner로 변경됨
1. 이더를 보내는 transaction을 생성할때 Contract에 ETH가 있는지 확인함