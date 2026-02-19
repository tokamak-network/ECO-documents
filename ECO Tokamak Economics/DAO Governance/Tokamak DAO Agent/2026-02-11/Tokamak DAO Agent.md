[[DAO Agent]]

**Motivation**

DAOs play a crucial role in decentralization. However, understanding new proposals and predicting their impact on the Tokamak Network ecosystem requires deep knowledge of blockchain and Tokamak Network. Community participation is low due to insufficient incentives relative to these high barriers to entry.

**Solution**

The DAO Agent provides objective opinions on new proposals based on its understanding of Tokamak Network and on-chain data. This allows the community to understand proposals more easily and enables voters to make better decisions.

**Roadmap**

The roadmap is to build agents that represent the perspectives and incentives of key stakeholders—L2 Operators, Verifiers, the Foundation, and token holders—so they can generate and comment on proposals, with a Security Council veto as the final safeguard.

**What did you learn?**

**1/**

TON 토큰은 Uniswap에서 거래되지 않습니다. ERC20 토큰이므로 Uniswap에서 거래가 가능할 것으로 예상되지만, 실제로는 revert됩니다. TON은 SeigToken 컨트랙트를 상속하는데, 이 컨트랙트는 호출자가 송신자 또는 수신자여야 한다는 조건을 가지고 있기 때문입니다.

하지만 AI는 ERC20 토큰이라는 이유로 Uniswap에서 거래가 가능하다고 답했습니다. 이 문제를 해결하기 위해 AI가 추측하지 않고 온체인 데이터를 직접 조회하고 실행할 수 있는 도구를 추가했습니다.

**2/**

MCP는 AI에게 도구를 제공하는 표준 규격이다.

```bnf
┌─────────────┐         ┌─────────────────┐         ┌──────────────┐
│   Claude    │  stdio  │    MCP Server   │  HTTP   │    블록체인    │
│  (클라이언트)  │ ◄─────► │  (우리가 만든 것)  │ ──────► │   (이더리움)   │
└─────────────┘         └─────────────────┘         └──────────────┘
"이 도구를 호출해줘"     "도구 목록은 이거고, 결과는 이거야"    "실제 데이터가 있는 곳"
```

*eg.*

일반 Claude의 경우

- 사용자: “TON 토큰 잔액이 얼마야?”
- Claude: “제가 블록체인에 접근할 수 없어서 모릅니다.”

MCP가 연결된 Claude의 경우

- 사용자: “TON 토큰 잔액이 얼마야?”
- Claude: (query_on_chain 도구 호출) —> “현재 잔액은 1,234 TON입니다.”

“TON이 Uniswap에서 거래 가능해?”라고 물으면:

1. Claude가 판단: “이건 verify_token_compatibility 도구를 써야겠다.”
1. Claude → MCP 서버로 JSON 전송을 한다.
```bnf
{
	"tool": "verify_token_compatibility",
	"arguments": { "token": "TON", "dex": "uniswap" }
}
```
1. MCP 서버가 실행:
- Foundry fork 테스트 실행

- 실제 메인넷 상태를 복제해서 거래 시뮬레이션

- transferFrom이 revert 되는 것을 확인
1. MCP 서버 → Claude로 결과 반환
```bnf
{ "result": "FAIL", "reason": "transferFrom restriction" }
```
1. Claude가 사용자에게 답변 → “TON은 Uniswap에서 거래할 수 없습니다. (검증 완료)”

현재 이 구조에 대해서 자세히 설명을 한다.

이후에는 포럼 사이트를 구축하고 포럼에 새로운 안건이 올라오면 에이전트들이 이를 읽고 서로 댓글을 남기고 계속해서 의견들을 종합하도록 만들려고 한다.

mcp를 이용할 수 있을지는 모르겠다.

RPG 캐릭터처럼 만들고자 한다.

[https://x.com/Voxyz_ai/status/2021370776926990530](https://x.com/Voxyz_ai/status/2021370776926990530)

토카막 네트워크 생태계에 대한 이해

—> 토카막 네트워크 컨트랙트에 대한 이해

이를 위해서 Tokamak Network 생태계를 가장 잘 이해할 수 있는 mcp 서버를 만드는 것을 목표로 했습니다.

제가 만들고 싶었던 것은 우선은 **"Tokamak Network의 스마트 컨트랙트를 개발자보다 깊이 이해하는 AI 에이전트"**