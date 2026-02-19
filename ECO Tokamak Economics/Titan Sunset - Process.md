14dd96a4-00a3-8038-bf5a-e9f314b560ef 

163d96a4-00a3-80ef-ad0f-f656373b7efe 

1. 컨트랙 업그레이드 [Harvey]
  1. repo: [https://github.com/tokamak-network/L2-Assets-Migration/tree/sepolia_sc](https://github.com/tokamak-network/L2-Assets-Migration/tree/sepolia_sc)
  1. **L1 Cross Domain Messenger**
  1. **L1 Bridge**
  1. L2에서 블록이 생성되지 않도록 노드가 변경될것이다.  L2 Cross Domain Messenger 과 L2 Bridge 는 업그레이드 안해도 됨. 
1. L2 데이타 집계 : 계정별 자산 분배 [Zena] 
  1. repo: [https://github.com/tokamak-network/L2-Assets-Migration/tree/get_owners_of_assets](https://github.com/tokamak-network/L2-Assets-Migration/tree/get_owners_of_assets)
  1. L2 데이타를 L1의 누구에게 보내야 할지를 파악하고, 얼마를 보내야 할지 집계한다. 
  1. 유니스왑 유동성도 각 소유자에게 분배 
  1. 일반 컨트랙의 자금은 owner, admin, deployer 순으로 게정이 있는 사람에게 보냄 
  1. OVM_SequencerFeeVault** **
    1. Titan: 0x6e1a64b7496DF60bF747085E89e1231A717fDd38 (Kevin 소유 주소)
Titan Sepolia: 0x091C8a37384ED31a469Ff23Fe4A183D11f56B22b (TOP에서 개인키 관리 중)
  1. 작업 
    1. Titan-sepolia : [[Titan-sepolia assets ]] 
    1. Titan : https://www.notion.so/tokamak/Titan-assets-161d96a400a38092afedf225bf5b4fdb

1. L1 Final Withdrawal 이 아직 안된 트랜잭션 및 정보 공개   [Victor] 
  1. Final Withdrawal 을 할 수 있는 파라미터 제공  
1. L1 에 L2 자산 분배정보 등록  [Harvey]
  1.   클래임을 통해 자산을 옮길 수 있다. 
1. 테스트 
  - Sepolia Bridge 
[L1ChugSplashProxy | Address 0x1F032B938125f9bE411801fb127785430E7b3971 | Etherscan](https://sepolia.etherscan.io/address/0x1F032B938125f9bE411801fb127785430E7b3971#readProxyContract)
  - Mainnet Bridge 
[etherscan.io](https://etherscan.io/address/0x59aa194798ba87d26ba6bef80b85ec465f4bbcfd#writeProxyContract)

[sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0x98627ec76ec3621332bfe9abec1f3d8b2f6f4fa7ac818b3b02a8d64523f242cc)

```json
[{position:'0x1a7dFF905E30d36578b6b2aC46089dEc51531067',hashed:'0x7d4ad43c4eb5152ab242a8eacacba53b20e06cff3a6533f6ce15cfcf03e2176d',token:'0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',amount:'996000000000000000'},{position:'0x1a7dFF905E30d36578b6b2aC46089dEc51531067',hashed:'0x946fda2cf90bda4739dce26cf41c16776e462618b3752e9645a05bb5512e2781',token:'0x0000000000000000000000000000000000000000',amount:'105899999967584534'}]    
```