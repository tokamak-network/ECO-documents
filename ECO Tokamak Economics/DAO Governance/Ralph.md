Claude will:

1. Work on the task
1. Try to exit
1. Stop hook blocks exit
1. Same prompt fed back
1. Repeat until DONE

### Install

`/plugin install ralph-loop@claud-plugins-official `

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/302ba72c-372a-4c22-9cd9-f60dc4793ea3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662D2DBZFE%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T092622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBnBSQBIOOjhlSshC470OJs3HOnYy0gsDL%2FS6mEIpxiAAiBNg9TzHHX3TDqOXY%2BH3DDmo7x%2FC2%2FlPUo572f6YaT4tCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMXC%2BoRmsJ1uR0k5PuKtwD9H2NxEhDb3sOgjeSEz8UnnfrKzFzclaRSljZqPixY8VZ2Ro0MH%2F4EBsVNGQHv1wW2wrVUSCf6QsTdw4MV9HoU51SxVy7gb8FCGcWHJzUiwh5TKMRAlSFP7qb5xwSV5r%2FPuF8odpHJDd7PWRca7tc0%2Fc6qVd1EGKhi1PgF8XJlmYsgR5V3A51YKxzV3ASc2dW7Rl3%2Blat1rz28CddEkNihde0IOU0fsDRetoReuSJRw%2F61tYeLnvyeEum2PUx5kCVFpGf9ip57VLWDq7y%2F1OrhoTC4YtvVff1vu389xXoaOUpumagboOPD80u41l472ZE7XRTgkP3NMb5Ldafjwre5JBB53MvPrlbbu%2Fl%2FPrCRmQXpNBv9ybtWAJgX%2BsyZngObWw%2FNf8BVk40fVHFgOYc4HZtClFO7k%2FitksT2kf8S1lxNGX45BquJEdt75SMH%2B5e3yrYpQ7k2pAcJtusoisFANvy8iFKWNPoGJ9UxNEZ684QlPnvB8JLyYYcFq2HpSEOCdjo82XNXz6SmBC5lJKLXCeuAcxcmpWikR%2FTGwsI3TL2pvQl4vxdLCglBFxehWrxej%2BjKiyn0464EZs6LuZ%2BfrvurAAut3japdxSGVSHcXovkv3g5CktcM79ADww%2FJjbzAY6pgHr2eY9CWjlW06Je7Zcnpiz9jbswsRfUm%2Ft7LKIBFSTivayxADI9tEzkiiE%2BKWtmD5wyHzHEywhLTI49vojWq84DGp1YYO2qxcEyRZmpnuEH0oRjugklW0wZONQTJGE4%2BVbsNix1bnCEAzcLanHbU1mJHGup2N%2FEnG4TCMFGBaE%2FlBXCoMMpUCVotPOdD8ER2MjA%2BGlVYfpJbePJYEhMADfVejcXUMv&X-Amz-Signature=3b47452765d9ef3ca3562918f21dc74f809655c276205337995c8e60586cfdb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

`/ralph-loop:ralph-roop PROMPT [--max-iterations N] [--completion-promise TEXT]`

- PROMPT: 할일
- OPTIONS:
  - --max-iterations: 최대 반복 횟수
  - --completion-promise: 특정 문구 출력시 종료

ex

`/ralph-loop:ralph-roop "할 일 목록을 위한 REST API를 구축해주세요. 완료되면 DONE을 출력합니다." --max-iterations 50 --completion-promise "DONE"`

ralph-loop.local.md 파일이 생긴다.

Ralph가 내부적으로 각 부분을 실행할 수 있도록 프롬프트를 하나씩 실행해본다.

1. Anvil을 실행하여 현재 블록 번호를 기준으로 fork된 로컬 체인을 실행해주세요.
1. Contract Address —

Agent가 컨트랙트의 내용을 확인할 수 있도록 만든다.

1. 현재 문서의 내용과 컨트랙트의 내용이 같은지를 확인한다.
1. 현재 모든 storage 값을 확인한다. 현재 블록 기준으로 변경된 것이 있는지를 확인한다. 이때 block number를 기준으로 한다.
1. 


1. 요즘 내가 전혀 모르는 영역에 대한 작업도 에이전트와 해보게 되는데요, 이럴때 자연스럽게 제가 코칭모드가 되는데 이 접근이 꽤 효과적인거같아요. "네가 이 작업을 잘 하기위해 무슨 정보가 더 필요할까?", "네 계획을 시뮬레이션 해봤을 때 걱정되는게 있어?", "지금까지 알아낸걸로 계획을 수정해봐", "뭐가 불확실한거같아?", "그 가설을 네가 확인해보려면 어떻게 해야할까?" 등등..
2. 

각 컨트랙트의 모든 상태 변수도 확인해봐줄 수 있어요? 이를 윙해서는 anvil에 현재
mainnet 기준으로 로컬로 돌리거나 etherscan을 이용하거나 해야 할 것 같은데 직접
컨트랙트 코드를 분석하고 storage를 찍어서 확인해보면 좋을 것 같아요. 그것의
의미를 모두 파악해서 이것도 정리가 필요해요.

먼저 anvil을 사용해서 mainnet을 fork하는 방법이 가장 정확할 것 같습니다.

각 컨트랙트의 storage layout을 분석한 후 eth_getStorageAt를 호출해서 실제 값들을 읽어올 수 있습니다.

이렇게 수집한 데이터를 바탕으로 각 상태 변수의 현재 값과 그 의미를 문서화하면 전체 시스템의 상태를 명확하게 파악할 수 있을 거예요.