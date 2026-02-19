Claude will:

1. Work on the task
1. Try to exit
1. Stop hook blocks exit
1. Same prompt fed back
1. Repeat until DONE

### Install

`/plugin install ralph-loop@claud-plugins-official `

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/302ba72c-372a-4c22-9cd9-f60dc4793ea3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSIAKN5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T045158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5yi7n%2Fxo2tZawtkp40ZNP9JS7mAu%2BmNcZfyr2Nq3oMwIgSfq2llzvBKEPCHFn15rY8UyzPFcTAfp%2FJESjpu06F50q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFcNdtNRmrO9XYP45ircA6cXTbDQ9h%2B6Muip63p9RzPOT2%2FkvYF%2BkUfsHLg2KdgEWJvPfJBPjyK3suzNZ7igUN2ufSwIlaXJ1Kjv%2FFQlsYYaVvBfd9GlQEfZgy620DVQ5PGUPJ20vpt5iIc1xZzghezTK4NGiu0Pb3u4lza%2FTTqHdlbBR9ODRnU%2FvbV%2BDaxK8EA9Xw9VhewZO0eL8VN1LczvNvYnVGAgsUOX1WbE3NkzKdjxQL7ONHHKfKwiPTYEPQJSltaDitNU8T3tseYS7z%2BNXdnqml%2FtH9PDSswfczincI3TFp6vg0x9x58gY8TxL074k2uJS8l04gFkGxFQY%2FIpomaAuo%2BO86TPyLqBMByo9svClfV9MJJvLjd6JOzOTje1poSvTlNe9sOElgS8sDh8%2FQr8s9LXryXeodjBet21klxPvb32rR4u9YVccMpc96ttv%2FkVYYp%2FLGxVvYLjCmb8l9ohHcRCvNKcCalYTxsyK0RYwmxf9IZutEzYDd7ddonjNcrTCLO6qFlaTGZwjO01sKKvS%2BNthbg0EyKKBpRF5AtENTnMmBI%2B2U5asu%2F9baSKEjJdz7TjippsPhEiffr5BYaEVYS0e0%2B3hCui%2FtV4KXkvpli%2FnQwqHdf191WITcCfp5I4MP2XxfgVMMrz2cwGOqUBWviOYvigTdUn5tCoFpP6Z9cNdBrIUhiibJ2ieI79dXloJEXCVUOL7I9xbDIQhzCn%2BqAsuntGRM9%2B4oBRM1naIml1P3GPrIRAhJYPOJI26r%2BN%2F3EqL6H80fK4n2lhu%2BjpmGqE0HREkROnAa9kCuJGQkhQ5X9Zz0mn2xF8JN9qOKvbDqPRituGBkwVfheGW1c0N7JJScpRxdKEuIo1G1sg8A7j%2FxnY&X-Amz-Signature=12fb49fab6c307f44addd224de8ab6089b7889e6b2b6d43d9e4005fce3a6f58e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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