# KR

## Safe wallet에 DAOContract와 foundation이 owner로 들어가야 하는 이유가 무엇일까?

- Safe wallet의 Owner가 L1에 배포되는 핵심 컨트랙트 (브릿지 등)의 수정 권한을 가지기 때문에 DAO Contract와 foundation이 Owner로 들어가지 않는다면 Owner가 마음대로 브릿지 로직을 수정하여서 **L2에 예치된 자산을 다른 주소로 옮기거나 브릿지 로직을 변경하여 부당하게 시뇨리지를 취득하는 등의 악위적인 행위를 할 수 있습니다. (백서 상 시뇨리지에 영향을 주는 요소에 L2 예치 수량도 포함되어있기 때문에) **([https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#222-톤-스테이킹-v2ton-staking-v2](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#222-%ED%86%A4-%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%82%B9-v2ton-staking-v2))**
**위의 경우를 예방하기 위해서 DAO Contract와 foundation을 Safe wallet의 Owner로 두고자 하고 SafeWallet의 propose가 통과하기 위해서는 모두의 승인이 필요합니다.
- 우리 TokamakDAO Candidate로 등록되어서 시뇨리지를 받는 대상으로 들어온 경우, 자신의 체인의 Bridge Contract의 로직을 변경할 경우 시뇨리지를 받는 Tokamak 생태계 유저들에게 피해를 주기 때문에 SafeWallet 중 한명을 DAO로 하여서 SafeWallet의 Owner가 로직을 마음대로 변경하지 못하게 하기 위함 
- 현재** SeigManager에서 시뇨리지를 계산할때 브릿지의 TON수량도 시뇨리지 계산에 들어가기 때문에 브릿지를 로직을 변경하면 TON을 딜레이없이 Deposit, Withdraw할 수 있게 된다면 악용가능함** (이것 아니고 더 많은 경우도 생길 수있음)
- L2체인이 TokamakDAO의 Candidate로 들어오더라도 해당 L2가 안정적이라는 것은 저희가 보장해주지 않음 (L2체인이 TokamakDAO의 Candidate로 들어온다고 해도 Deposit할려고 하는 유저들을 보호해준다는 의미는 아님) (이것은 시뇨리지와 다른 문제임)
- 기존 Tokamak 생태계 참여자들이 시뇨리지에 대해 피해를 보지않게하기 위한 작업

## Safe wallet에 DAOContract가 Owner로 들어가는 경우는 저희 DAO의 Candidate로 등록된 체인만 적용되는 것인지 아니면 그냥 L2체인만 만들고자하는 체인들도 적용되는 것인지?

- TRH 플랫폼을 이용하여서 L2체인만 만들 경우에는 해당하지 않습니다. 
  - 그럼 TRH 플랫폼을 이용하여서 L2체인만 만들 경우에는 SafeWallet과정이 없는것인지? SafeWallet이 있다면 어떤식으로 구성되는지? 
  - SafeWallet 배포는 있는데 Owner가 Admin이 한명이 등록된 상태 
- TRH 플랫폼을 이용하여서 L2체인이 tokamakDAO 후보자로 등록하였을 때만 시뇨리지 보상을 원한다고 판단하고, TokamakDAO 생태계로의 온보딩을 의미하는 것이기 때문에 악의적인 상황을 막기 위해서 SafeWallet의 Owner로 DAO Contract와 foundation이 들어가며 탈중앙화의 가치를 줄일 수 밖에 없습니다.
- TRH 플랫폼을 이용해서 L2체인을 만들때 TokamakDAO 후보자로 등록했을때랑 안했을때의 차이점은 무엇무엇이 있는지? 그리고 TokamakDAO후보자로 처음에는 등록안하였다가 추후 등록할 수 있는 방법은 없는지?
  - 추후 등록가능함
  - 등록 과정
    1. SafeWallet의 owners와 threshold를 변경
      1. owners: Admin → Admin, DAOContract, Foundation
      1. threshold: 1 → 3
    1. Admin이 배포한 L1 컨트랙트의 로직 계약 주소와 프록시 계약 주소를 온체인 검증하여 L1 컨트랙트가 임의로 수정되었는지 확인
    1. 검증 완료 시 TokamakDAO Candidate로 등록

# EN

## Why should DAOContract and foundation be included as owners in Safe Wallet?

- Since the Owner of the Safe Wallet has the authority to modify the core contracts (bridge, etc.) deployed in L1, if the DAO Contract and foundation are not included as the Owner,** the Owner can arbitrarily modify the bridge logic to move assets deposited in L2 to another address or change the bridge logic to unfairly acquire seigniorage, etc. (Because the L2 deposit amount is also included in the factors affecting seigniorage in the white paper)
**([https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2))
To prevent the above cases, we want to make the DAO contract and foundation the owners of Safe Wallet, and for SafeWallet's proposal to pass, everyone's approval is required.
- If you are registered as a TokamakDAO Candidate and receive seigniorage, changing the logic of your own chain's Bridge Contract will cause damage to Tokamak ecosystem users who receive seigniorage. To prevent this, we have designated one of the SafeWallets as a DAO to prevent the Owner of SafeWallet from changing the logic at will.
- Currently, **when calculating seigniorage in SeigManager, the TON amount of the bridge is also included in the calculation, so if the logic of the bridge is changed to allow TON to be deposited and withdrawn without delay, it can be exploited** (there may be more cases than this one).
- Even if the L2 chain enters the TokamakDAO Candidate, we do not guarantee that the L2 is stable. (Even if the L2 chain enters the TokamakDAO Candidate, it does not mean that we will protect users who want to deposit.) (This is a different issue from seigniorage.)
- Work to ensure that existing Tokamak ecosystem participants are not harmed by seigniorage.

## When DAOContract is entered as the Owner in the Safe Wallet, does it only apply to chains registered as Candidates for our DAO, or does it also apply to chains that only want to create L2 chains?

- This does not apply if you only create an L2 chain using the TRH platform.
  - So, if I only build an L2 chain using the TRH platform, does that mean there's no SafeWallet process? If there is a SafeWallet, how is it structured?
  - SafeWallet is distributed, but only one owner is registered as Admin.
- Since the L2 chain is registered as a tokamakDAO candidate using the TRH platform, and it is determined that the seigniorage reward is desired only when it is onboarded to the TokamakDAO ecosystem, the DAO Contract and foundation are included as the Owner of SafeWallet to prevent malicious situations, which inevitably reduces the value of decentralization.
- When building an L2 chain using the TRH platform, what are the differences between registering as a TokamakDAO candidate and not registering? Also, is there a way to register as a TokamakDAO candidate later if you initially opted not to?
  - You can register later
  - Registration process
    1. Change the owners and threshold of SafeWallet.
      1. Owners: Admin → Admin, DAOContract, Foundation
      1. Threshold: 1 → 3
    1. Verify the logical contract address and proxy contract address of the L1 contract deployed by the Admin on-chain to confirm whether the L1 contract has been arbitrarily modified.
    1. Upon verification, register as a TokamakDAO Candidate.