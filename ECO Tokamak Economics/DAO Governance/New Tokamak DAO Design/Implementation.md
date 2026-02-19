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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/23500026-5951-475c-a8b3-65b15fd16d41/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6GQQSM6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUVkJE2Of9FKsnzLF7FJLmHd8DZ2dTHhqgESQR1BACdQIgIYMw%2BFtR2Zgtx%2Bg8GOI0ZBDNnAQmkpVpcGbeQqCTtdUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKCaoW3UDAhfTwUuCircA%2FHjltwxLy3hsIrF0DxiL7%2F3x6BQ3p%2FnfjGq5pt92OyRXLIHx8oTv1czVARD%2BsxRZ54pC84ducamy5kbVOLqS4KCXhfz%2B3b%2BR1rAh7VvOgwlnAfE3UqNZfYYhoxqWnGh1Khelc6ScU3XVbzMp2zpYVGFKbQVjR3xjdaLdJzvcSZc2%2BSssB0J6ALgGfRvqlmxuJYC%2FPwgDRlv%2BjWjnBkd54%2F%2FMQvTEgbt7Cej5fmf6NHlqwaNa9pUxooLAv0EpNzPl1uksS1d3KD5b3fS6wc2CtBm487L6a1ssV9UKtTfM4WwBV4gXkQkI08nSF4nREZUX6xCMjmZmb8SS5Bs2RHBd8e1qMR5AVXX8PDBiUrkOWjGWEb%2Bf8S1DaCKHn9zATAvSX1UlU%2BSqh3lQbh%2FXFuMbhaoaN7kdpngUUMixXj5b61ObMmOBJMlQE1BHwQJWCNhLD3LlsZknuiTP82wjmrmxve2uPqhUB51K43%2FooyQmpKbk%2FQ5oXwkEMCvOpim5w7riCbdQ9Je%2F8uL42aPwwGvT3EobviSYNGSXqNR1tdolK56g4K1Sbm4ZKvI4traqzS3cY9NPxyivHJhIbnMIW%2BhjH%2F6bExGR3ugtcGcD4nNbaXHZRXXpzzpiByyz0aBMMPv2cwGOqUBqH%2Bokr3FdXv4CI2XfZ7nvQJrfyKubim8ohvPVN0lEWA6ywbQQWxqNAWAPKPNU%2Fjail9V5Z%2B3py8MXfMek%2Br9Q8%2FRFs8aAJO8XaIBX1EH5jGslwvHjAgP6Kpu24E4swyW5dbB8k7J6etgHd0EnBS9c2CqCYcanbEZnRuTGjTXtAFK82RzXKcwFQbho%2Fu4rJyLjkDEqFGJBrL3VPYQPtoO%2BlPwtMYL&X-Amz-Signature=1c1eb4e7eaa711fb047fe05cb6dc88b1129e1a056a841af3fe7f5ac64cb3d016&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**prompt**

이 디자인이 마음에 들지 않습니다. [https://www.tally.xyz/gov/web3atkaist-2023](https://www.tally.xyz/gov/web3atkaist-2023) 사이트의 스타일을 참고해서 업데이트해 주세요. 폰트나 법적인 문제가 발생할 가능성이 있다면 알려주세요.

output:

1. **우선 지갑 연결이 되는 웹사이트**
1. 디자인 시스템 생성 — #3376f7 (main color)
1. 

**<App>**