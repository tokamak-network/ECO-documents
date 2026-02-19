## [Tokamak.network](http://tokamak.network/) Landing page Q1 To do list

- Price Dashboard의 랜딩 페이지의 서브 페이지화
- Exploring INSIGHTS 섹션 업데이트 
- Newsletter Subscription 정책 변경 및 이메일 리스트와의 연동 확인

## Price Dashboard

tokamak network 랜딩 페이지 리뉴얼 후 별도의 도메인으로 분리 운영중인 Price Dashboard를 랜딩 페이지 내에 서브 페이지로 운영하기 위한 방법을 논의합니다.

- **도메인 **예시 - https://www.tokamak.network/price
- **Price 페이지 위치** ( About > Price dashboard )

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/764426db-0577-4be0-8c01-94213052721a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUIZ5OI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfSsVYSeHEyXDFsmam55GfIXx7g7elR4iSPhug%2FOvtGAiA30Rkl5s0nHijeT1OAW5419Mzb244YkTxgMGEE1NzEwir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM14F%2Bn5AFyvtuHq5FKtwD9ffv4lVm5AUlOEee5P3bLnV2%2BFdMUWtRkJpjufyl9BqVso8S8gM%2Bj0CXYVHDEVzjUdXs0iNv681wqxnS98F9oL6%2FVJrZtKBUw8oatQqys2tM1vfNflTXwdDwbdwkraLfAz8bTsxLaKL39UcddiOEzmZKTXfajdi5SjfYKvcmjmLoDeX4ZeRPQ10A54nyfnYiKQbuwvReWKQyAyNJPjeukI5a4GWC3JBHq5SbOuejDESzjWaDeVXjenBeF580AYaf2p7YuAjuw9Kr83mTH%2BR9whsUWl%2BKQNLlFQFkgvpJlPDaaOj41XVsjeNaT6d7tG%2F0G89dfYOGqiJiyQu53PiyolT5Y4o8pEjDoEf%2FONEyXVjLDOK%2FlruRKCUEmykzqC9pN6oaZ8EvNGBXf3ZPZULproDX7XAd84mj7pmr96Rme9JErLZhH%2FBjqBOaBPO3rkQU1JwcBSwUpxAnTa1bzTie346JsOaHge%2Bk94Jm%2FrKfD6xifC51VwDApexYfmY89PtXxYy1ZuG1ecfDp1Yoed58KGAqUOC7o%2B8eCE7rh4ykQC92UlZYqyVMeQsW2fgsF82X3w9cuGmO0tshLLcu%2FBTzai8SzItFFhIwpKxDpyN2S9OO8sMb4W46ejxoYwsww%2B7ZzAY6pgEbSssH1mfxWju%2FooGy%2B75m9Bbr%2FhO%2BURDBOsGyIMFxfXJkBGPd%2FnSKZL72%2Fiyn7GGbhFmBzy5f98f7WhC%2FfPSrg9p8V7r3GbwxHtBSx4U1y2bhSStLImEpquhbp5GM%2Ffx4AomIlZWFuneHN2EWh%2FoYQaKI%2Fiz9MbPUFjYJAN4QYQSjhauAujknK9xMxVvpR4nFG33PlZwRGv2lTQ5UL%2ByCOIio0LPC&X-Amz-Signature=b5081e224997cac972426181e489e2b7736fe4579e69c66d0807a4756a16d333&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Price Dashboard 화면**
![](images/85e059a648a1.png)

  - **변경 필요사항**
    - GNB 삭제
    - Footer 변경

**항목(지표)**
    - Price
      - TON Price($, ￦)
      - Market Cap
      - Fully Diluted Valuation
      - 24H opening price
      - 24H closing price
    - Supply
      - TON Supply
        - Total supply
        - Circulating supply
        - Circulating supply (Upbit standard)
        - Burned
        - TON Token history Raw data
      - TON Locked
        - DAO Vault
        - Staked
        - Vested
      - TON Liquidity measure
        - C1 (= Total Supply - DAO Vault - Staked - Vested)
        - C2 (= C1 + Staked TON)
        - C3 (= C2)
- **Dune 화면 (→ Praveen님께 확인)**
![](images/8716e472ad72.png)

  - TON Price
  - Market Cap
  - TON Supply
  - Circulating Supply (Upper Estimate)
  - Circulating Supply (Upbit standard)
  - Transfer
  - The Big Players of TON+WTON: Leading 10 Wallet
- **공통적으로 포함된 지표**
  - TON Price
  - Market Cap
  - TON Supply (Total Supply)
  - Circulating Supply
  - Circulating Supply (Upbit Standard)
- **새로운 Dashboard에서 업데이트된 내용**
  - Dashboard 상단
    - Title 수정: Price Dashboard → Tokamak Network Tokenomics Dashboard
      - 단, About 탭 하단의 2 depth 메뉴로서의 이름은 Price Dashboard로 적용(타이틀이 너무 길고, 수정해서 단순 Tokenomics Dashboard로의 적용은 혼란을 줄 우려있음)
    - Description: A more comprehensive dashboard showing TON(Tokamak) token details and other liquidity metrics with easy explanations.
  - Dashboard Overview
    - Sub Title: Real-Time TON(Tokamak) Market Insights
    - Sub Description: This dashboard integrates multiple data sources to provide reliable information. Price data is updated in real-time and is linked to market data from major exchanges to ensure accuracy. Use it as the best tool to comprehensively monitor Tokamak Network's ecosystem and performance
  - Live update 기능 추가
- **Dune - Tokamak Network Tokenomics Dashboard 변경사항 (논의)**
  - <현재 Dune 관리자 확인 필요> → Praveen님께 인수인계.
  - Token Addresses
    - 삭제: Titan Network 항목
  - Services
    - 삭제:  Titan L2, Titan Block Explorer
    - 추후 삭제: Tokamak Bridge, Simple Staking, DAO

## Exploring INSIGHTS 업데이트

섹션의 Goal: ‘Share updates on how Tokamak Network is evolving the solutions it offers’

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/308d637d-495b-4fe6-8676-fd2db07f79a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUIZ5OI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfSsVYSeHEyXDFsmam55GfIXx7g7elR4iSPhug%2FOvtGAiA30Rkl5s0nHijeT1OAW5419Mzb244YkTxgMGEE1NzEwir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM14F%2Bn5AFyvtuHq5FKtwD9ffv4lVm5AUlOEee5P3bLnV2%2BFdMUWtRkJpjufyl9BqVso8S8gM%2Bj0CXYVHDEVzjUdXs0iNv681wqxnS98F9oL6%2FVJrZtKBUw8oatQqys2tM1vfNflTXwdDwbdwkraLfAz8bTsxLaKL39UcddiOEzmZKTXfajdi5SjfYKvcmjmLoDeX4ZeRPQ10A54nyfnYiKQbuwvReWKQyAyNJPjeukI5a4GWC3JBHq5SbOuejDESzjWaDeVXjenBeF580AYaf2p7YuAjuw9Kr83mTH%2BR9whsUWl%2BKQNLlFQFkgvpJlPDaaOj41XVsjeNaT6d7tG%2F0G89dfYOGqiJiyQu53PiyolT5Y4o8pEjDoEf%2FONEyXVjLDOK%2FlruRKCUEmykzqC9pN6oaZ8EvNGBXf3ZPZULproDX7XAd84mj7pmr96Rme9JErLZhH%2FBjqBOaBPO3rkQU1JwcBSwUpxAnTa1bzTie346JsOaHge%2Bk94Jm%2FrKfD6xifC51VwDApexYfmY89PtXxYy1ZuG1ecfDp1Yoed58KGAqUOC7o%2B8eCE7rh4ykQC92UlZYqyVMeQsW2fgsF82X3w9cuGmO0tshLLcu%2FBTzai8SzItFFhIwpKxDpyN2S9OO8sMb4W46ejxoYwsww%2B7ZzAY6pgEbSssH1mfxWju%2FooGy%2B75m9Bbr%2FhO%2BURDBOsGyIMFxfXJkBGPd%2FnSKZL72%2Fiyn7GGbhFmBzy5f98f7WhC%2FfPSrg9p8V7r3GbwxHtBSx4U1y2bhSStLImEpquhbp5GM%2Ffx4AomIlZWFuneHN2EWh%2FoYQaKI%2Fiz9MbPUFjYJAN4QYQSjhauAujknK9xMxVvpR4nFG33PlZwRGv2lTQ5UL%2ByCOIio0LPC&X-Amz-Signature=5f0ef203b5680b1a71eeeaef8375223e75acbc487e825db894a8b3414c0da6d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. **Medium Category 정리**
  1. News - Tokamak Network Ecosystem 공지와 Project별 공지의 분리 여부 결정
  1. Devcon, Opinion - 통합 혹은 변경 여부 확인
  1. Tokamak Network - 리서치, 바이위클리 등이 혼재되지 않도록 분리
1. [**Tokamak.network**](http://tokamak.network/)** landing page 내 Insights 섹션 업데이트**
  1. 카테고리 탭 변경
  1. Medium Thumbnail API issue 해결
1. **Protocols와의 병합(Merge)**
  1. Tokamak Network 핵심 프로토콜과 해당 소식을 확인할 수 있는 Sub-landing page를 연결하는 섹션으로 업데이트

## Medium Category 정리

### AS-IS

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f2739a07-1b7d-4a2d-8344-ca232cdcb80d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUIZ5OI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfSsVYSeHEyXDFsmam55GfIXx7g7elR4iSPhug%2FOvtGAiA30Rkl5s0nHijeT1OAW5419Mzb244YkTxgMGEE1NzEwir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM14F%2Bn5AFyvtuHq5FKtwD9ffv4lVm5AUlOEee5P3bLnV2%2BFdMUWtRkJpjufyl9BqVso8S8gM%2Bj0CXYVHDEVzjUdXs0iNv681wqxnS98F9oL6%2FVJrZtKBUw8oatQqys2tM1vfNflTXwdDwbdwkraLfAz8bTsxLaKL39UcddiOEzmZKTXfajdi5SjfYKvcmjmLoDeX4ZeRPQ10A54nyfnYiKQbuwvReWKQyAyNJPjeukI5a4GWC3JBHq5SbOuejDESzjWaDeVXjenBeF580AYaf2p7YuAjuw9Kr83mTH%2BR9whsUWl%2BKQNLlFQFkgvpJlPDaaOj41XVsjeNaT6d7tG%2F0G89dfYOGqiJiyQu53PiyolT5Y4o8pEjDoEf%2FONEyXVjLDOK%2FlruRKCUEmykzqC9pN6oaZ8EvNGBXf3ZPZULproDX7XAd84mj7pmr96Rme9JErLZhH%2FBjqBOaBPO3rkQU1JwcBSwUpxAnTa1bzTie346JsOaHge%2Bk94Jm%2FrKfD6xifC51VwDApexYfmY89PtXxYy1ZuG1ecfDp1Yoed58KGAqUOC7o%2B8eCE7rh4ykQC92UlZYqyVMeQsW2fgsF82X3w9cuGmO0tshLLcu%2FBTzai8SzItFFhIwpKxDpyN2S9OO8sMb4W46ejxoYwsww%2B7ZzAY6pgEbSssH1mfxWju%2FooGy%2B75m9Bbr%2FhO%2BURDBOsGyIMFxfXJkBGPd%2FnSKZL72%2Fiyn7GGbhFmBzy5f98f7WhC%2FfPSrg9p8V7r3GbwxHtBSx4U1y2bhSStLImEpquhbp5GM%2Ffx4AomIlZWFuneHN2EWh%2FoYQaKI%2Fiz9MbPUFjYJAN4QYQSjhauAujknK9xMxVvpR4nFG33PlZwRGv2lTQ5UL%2ByCOIio0LPC&X-Amz-Signature=aa9b5db1ddd1ea77f4498dea15445ae815a0a35e76e121c44144d07e535f769c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Issue

Medium 게시물 관리상의 문제점 및 대응 방안

1. 기존 아티클의 카테고리 변경 관련 이슈
  - Editor 권한으로는 이미 발행된 아티클의 카테고리 변경이 제한되어 있음
  - Tokamak Network 계정으로 게시된 콘텐츠도 동일한 제약 사항 적용
1. 사용자 권한 관리의 한계
  - 퇴사자 및 이직자의 계정 권한 조정에 어려움 발생
  - 특히 이메일 주소 기반 권한 변경 시스템의 제약이 존재
1. 새로운 Tokamak Network Medium 계정 개설은 고려하지 않기로 결정
  - 기존에 축적된 콘텐츠의 가치를 보존하는 것을 우선시

### 논의

- Medium은 공지채널에 가깝고, 소통을 지원하기에는 어려움 점이 있음
  - 각 프로젝트별로 소통을 강화하기 위한 로드맵을 구성하고 있음 → 공지로서의 Medium 역할을 강조하는 것이 필요한가?
- *프로젝트별 카테고리 운영은 프로젝트의 운영이 유동적이기 때문에 어려울 수 있음*
  - *개발*
  - *아이디어/제안*
  - *Issue*
- *세미나 전에 Kevin 초대 후에 확인 필요 - Additional resource에 대한 확인*
- *브랜드 전체의 포럼을 만든 후에 카테고리 탭을 프로젝트별로 분류*
  - *담당자 할당에 대한 문제*
  - *생성되었다 사라지는 경우에 대한 관리 여부*
- *많은 프로젝트들이 외부 활동을 계획에 포함하고 있음 → Grant 평가 주요 요소*
- *어떤 플랫폼인가보다, 결국 커뮤니티 참여 인원의 문제*
  - *개발자가 많아서 떠들다보면 결국 원하는 것을 얻게됨 → 전담 개발자가 있거나, 디스코드 내에 개발 관련 내용이 활성화된 케이스가 많음.*
  - *해결법을 얻는 것이 중요, 어느 채널인지가 중요하지 않음*
- *별도로 ‘Forum’을 빼는 방안 - Developer 메뉴쪽에서 Forum으로. 가볍게 가져간 후에 추후에 반응을 보고 업그레이드하는 것은?*
- *Lucas님) 틀을 잡아놓고 데이터를 가져왔을 때, 상대적으로 정리가 덜 되어있는 것 같은 Medium을 간결하게 보여지도록 함.*
  - *랜딩페이지에서는 카테고리별로 정리된 내용을 보여주고, 링크를 통해 Medium에서 상세 Article을 볼 수 있도록*

[[Grant]]

## Newsletter Subscription 정리

**현황**

- Newsletter Subscription의 입력이 어디로 가는지, 정확하게 확인되지 않음 (인수인계 과정에서 유실된 것으로 추정)
⇒ **스티비 사용 유지 결정**

**수동 업데이트**

- Newsletter subscription에 입력된 메일 주소를 Spreadsheet에 Form 형태로 저장
- 특정 주기마다 수동으로 CSV 다운로드 이후 스티비 메일 목록에 추가
- 담당: Max