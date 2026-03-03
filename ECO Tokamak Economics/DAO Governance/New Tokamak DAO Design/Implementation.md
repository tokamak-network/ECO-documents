### **Contract**

**<현재 DAO 컨트랙트 구조에 새로운 DAO 모델을 적용하고자 한다.>**

**expected output:**

- 컨트랙트 중 재사용할 것과 새로 작성할 컨트랙트는 무엇인가?
- 다이어그램

**prompt:**

**<contract>**

skills:

- building-secure-contracts

**migration을 고려한 개발**

`feature/v2-migration`

- 컨트랙트 구조의 변경 사항을 다이어그램으로 확인하고 싶습니다. Excalidraw에서 바로 복사하여 붙여넣을 수 있는 JSON 형태로 작성해 주시면 즉시 확인할 수 있을 것 같습니다.
- 컨트랙트 상세 다이어그램과 설명이 포함된 md 파일을 만들어주세요. 누구나 이를 보고 컨트랙트가 어떻게 변화하는지 알 수 있도록 작성해 주세요. 가독성이 중요합니다. 컨트랙트 개발자라면 누구나 이 문서를 보고 쉽게 업그레이드를 진행할 수 있어야 합니다.
- 작업 내역을 feature/v2-migration 브랜치에 저장한 후, Foundry 기반으로 merge 시 사용될 컨트랙트만 작성해 주세요. 테스트 스크립트는 작성하지 말고 테스트 시나리오만 만들어 주세요. 모든 테스트 시나리오가 충족되면 그때 테스트 스크립트를 작성합니다.

**migration을 고려하지 않고 우선 개발**

`feature/v2-no-migration`

- 현재 브랜치에서 Foundry를 사용하는 앱으로 프로젝트를 완전히 새롭게 만들어주세요. 기존 파일들은 모두 삭제해도 됩니다. 곧바로 실행 가능한 컨트랙트가 필요합니다. 현재 프로젝트는 너무 오래되었습니다. building-secure-contracts 스킬이 컨트랙트 작성에 도움이 될 것입니다.

output:

1. migration이 필요한데 이에 관련한 상세 문서 요청
1. 새 브랜치를 만들고 Foundry 기반으로 실제로 merge 하게 됐을 때 사용하게 될 컨트랙트만 작성해 주세요. 테스트 스크립트는 작성하지 말고 테스트 시나리오만 만들어 주세요. 모든 테스트 시나리오가 충족되면 그때 테스트 스크립트를 작성할 것입니다.

**<webapp>**

- web3-frontend 스킬을 사용하여 가장 간단한 형태의 dApp을 만들어 주세요. 우선 지갑 연결 기능만 구현해 주시면 됩니다.

**skills:**

웹앱 개발: *—> 이 둘을 사용*

- **web3-frontend**
- **vercel-react-best-practices**

**<웹앱 디자인>**

- **web-design-guidelines**
- #3376f7 (main color)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/23500026-5951-475c-a8b3-65b15fd16d41/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGNE4INQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkLaU%2F5LZT5hzqIANRrr3nLwUIUPszJgMg3DaLtBY9iwIhAP8NA4avRs5L%2ByKlDGpCQ3lGNTP7n5mSE7wl8p5%2BYg1EKv8DCHoQABoMNjM3NDIzMTgzODA1IgxJdALJ1XbJE6lBGVAq3AOQ%2BRR73v%2BPnHtsRclAgePw0gZYHOfaYeE7wAZXWxXH60zlvLLDJ2HdXPbmkgJK3nh%2BTTCVJ2kgvbdUWxkLUTkuiBytcLLfKRXdi7wi0uSAMZ0ByjRvkc7k33hWnlhRyqLqIIHdiDu1mTgz6BdIKg9wOMaiUam8eC7qJ6U4mDzZL1rmaUkJjpHcC8uPB3dVKYwFp%2Fwx4egQH3r05WASAwg8hjNaCp9pC1xiZAgFU2G2PMQSNlATgXrqVX%2Bg3pTlRm6aY1h7GEy%2B9YuXLjitHIFEI5JjRE5r7yo6KK1yPy3AfMkzUd5bk4Re5V%2BwNH5%2B6KyknWBLjniDwQVr%2BcmNWiKW3gePyw8ubNAus4VOoncOr5ase%2Fpt7lHUushvwOOcChos8GC%2FC3XBTLYTR%2BFh9yveQj0otrnB677Pqv76%2BoDymG%2B%2F0xRp14BVdx%2FrOHUPwMC7eyLVr4b518ei7BUEwJ%2Fb08%2FYCZNfKjyQ5Rj0NcBW6%2BQzZxS0%2BVJdktKxeUj1TGbks%2B0YwR4J1yyY659nNFwFzklj0zYS1KsgS%2F92hR2qovTFcMGd0316zKhO263h7efbyN41hFhDsaHVxRoKbUF6FWsmjHQmf7pvROUnBNN14MsFXgMU4tlJpgKJzzD%2BmNvMBjqkAXnwE1Q3djdlLLTp0qTAAs%2BagQe0QRPDqMOqVOZlI5jQJ5xsPmaqje93ccDH%2FtGtEjBC7pBmFP0BlpTPCCmgByo1%2Fco5%2Fw%2FaL6eDJ8ZKZsPMZ1SIBlxv2qNttyKr1hLzbkhFFWCDNYWHSOkk7MKG9Cj6vH9eAuAzti2NJISKd0WnT9M0XLHe2kAJtk9oaeO5ob9ipN2AFuBAZx8%2Bg%2B%2FLs5ez6gXB&X-Amz-Signature=735cb4a5488e12f96309527079e31e7c6bb352d83ae0a34b5251d7fe74a58546&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**prompt**

이 디자인이 마음에 들지 않습니다. [https://www.tally.xyz/gov/web3atkaist-2023](https://www.tally.xyz/gov/web3atkaist-2023) 사이트의 스타일을 참고해서 업데이트해 주세요. 폰트나 법적인 문제가 발생할 가능성이 있다면 알려주세요.

output:

1. **우선 지갑 연결이 되는 웹사이트**
1. 디자인 시스템 생성 — #3376f7 (main color)
1. 

**<App>**