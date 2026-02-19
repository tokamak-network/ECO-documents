[[Untitled]]

# Tokamak DAO Agent - 발표 & 데모 가이드 (개발자 대상)

## 1. 한 줄 소개

**"Tokamak Network의 스마트 컨트랙트를 개발자보다 깊이 이해하는 AI 에이전트"**

## 2. 발표 구조 (권장 순서)

### Part 1: 문제 정의 — "왜 이것을 만들었는가?"

Tokamak Network에는 **42개의 검증된 스마트 컨트랙트, 746개의 Solidity 파일**이 존재한다.

DAO 거버넌스 제안이 올라오면 다음을 모두 수행해야 한다:

- 컨트랙트 코드 읽기
- 스토리지 슬롯 확인
- view 함수 호출
- 트랜잭션 시뮬레이션
- 영향 범위 분석

이 과정이 복잡하고 시간이 오래 걸린다. 그래서 AI에게 물어보고 싶지만, **AI의 답변을 신뢰할 수 없다**.

**핵심 문제 — AI 할루시네이션이 블록체인에서는 치명적이다**

예시:

```
질문: "TON 토큰이 Uniswap에서 거래 가능한가요?"

일반 AI 답변: "TON은 ERC20 토큰이므로 Uniswap에서 거래할 수 있습니다."
→ 틀림. TON의 transferFrom은 `msg.sender == sender || recipient`을 요구함.
→ DEX 라우터(제3자)가 transferFrom을 호출하면 revert됨.
→ 이 답변을 믿고 스왑을 시도하면 트랜잭션이 실패하고 가스비만 날림.
```

TON의 `SeigToken.transferFrom` 구현:

```solidity
function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
    require(msg.sender == sender || msg.sender == recipient,
        "SeigToken: only sender or recipient can transfer");
    // ...
}
```

이 제한은 소스 코드를 읽어야만 알 수 있고, 일반 AI는 이를 확인하지 않고 "ERC20이니까 가능합니다"라고 답한다.

### Part 2: 해결 방법 — "AI에게 도구를 주자"

**핵심 아이디어**: AI가 추측하지 못하게 하고, 대신 **온체인 데이터를 직접 조회하는 11개 도구**를 제공한다.

```
CLAUDE.md 규칙 (프로젝트의 #1 규칙):
"컨트랙트 동작에 대해 절대 추측하지 않는다.
 1. 멈춘다 — 답변을 작성하지 않는다
 2. 검증한다 — MCP 도구를 먼저 호출한다
 3. 답변한다 — 검증 결과만을 근거로 답변한다"
```

11개 도구는 5개 카테고리로 나뉜다:

| 카테고리 | 도구 | 하는 일 |
| --- | --- | --- |
| 코드 탐색 | `get_contract_info` | 이름/주소로 컨트랙트 메타데이터 조회 |
|  | `read_contract_source` | Solidity 소스 파일 읽기 |
|  | `search_contract_code` | 전체 746개 .sol 파일에서 패턴 검색 |
| 온체인 조회 | `read_storage_slot` | raw 스토리지 슬롯 직접 읽기 |
|  | `read_contract_state` | 스토리지 레이아웃 기반 전체 상태 디코딩 |
|  | `query_on_chain` | view/pure 함수 호출 |
| 거버넌스 | `fetch_agenda` | DAO 안건 조회 (투표, 타겟, calldata) |
|  | `decode_calldata` | 트랜잭션 데이터 → 함수 호출로 디코딩 |
| 시뮬레이션 | `simulate_transaction` | `eth_call`로 트랜잭션 dry-run |
| 검증 | `verify_token_compatibility` | DEX 스왑 시뮬레이션 (approve→transferFrom→swap) |
|  | `run_fork_test` | Foundry `forge test --fork-url`로 메인넷 포크 테스트 |

### Part 3: 라이브 데모

아래 데모 시나리오 참조.

### Part 4: 아키텍처 & 코드 워크스루

아래 기술 아키텍처 참조.

---

## 3. 데모 시나리오

### 데모 1: "TON은 Uniswap에서 거래 가능한가?" (핵심 데모)

**이 데모가 프로젝트의 핵심 가치를 보여준다.**

Web UI(`localhost:5173`)에서 실행:

```
"TON 토큰이 Uniswap V2에서 거래 가능한가요?"
```

AI의 동작 순서:

1. 바로 답변하지 않고 `verify_token_compatibility` 도구를 호출
1. 도구가 실제 TON 홀더(DAOVault)를 찾아 시뮬레이션 수행
1. 세 가지 시나리오를 테스트:
  - `approve` → 성공 (가스: ~46,000)
  - `transferFrom` (라우터가 호출) → **revert**: `"SeigToken: only sender or recipient can transfer"`
  - `swap` → **revert** (transferFrom 실패로 인해)
1. AI가 증거를 인용하며 "불가능합니다" 답변
1. "WTON으로 wrap하면 거래 가능합니다" 대안 제시

**포인트**: SSE 스트리밍으로 도구 실행 과정이 실시간으로 보인다. 사용자는 AI가 무엇을 하고 있는지 투명하게 볼 수 있다.

### 데모 2: "DAO 제안 분석" (거버넌스 데모)

```
"가장 최근 실행된 DAO 안건을 분석해줘"
```

AI의 동작:

1. `fetch_agenda` → 안건 조회 (투표 현황, 타겟 컨트랙트, 실행 상태)
1. `decode_calldata` → calldata를 함수 호출로 디코딩
1. `read_contract_source` → 타겟 함수의 Solidity 코드 확인
1. 종합 분석: 이 안건이 무엇을 바꾸려 하는지, 어떤 영향이 있는지

**포인트**: AI가 여러 도구를 연쇄적으로 호출하며 분석을 깊어가는 과정을 보여준다.

### 데모 3: "컨트랙트 상태 디코딩" (기술 데모)

```
"SeigManager의 현재 상태를 보여줘"
```

AI의 동작:

1. `read_contract_state` 호출
1. 프록시 패턴 자동 감지 (SeigManagerProxy → SeigManagerV1_3 구현체)
1. 스토리지 레이아웃 JSON으로 각 슬롯을 변수명+값으로 디코딩
1. `_ton`, `_wton`, `_registry`, `seigPerBlock` 등 핵심 상태 변수 표시

**포인트**: raw hex → 사람이 읽을 수 있는 상태로 변환하는 과정.

---

## 4. 기술 아키텍처 (코드 수준 설명)

### 전체 구조

```
┌──────────────────────┐       ┌──────────────────────────┐
│  Claude Code (CLI)   │       │  Web Chat UI (Browser)   │
│  MCP Protocol        │       │  Anthropic API           │
│  stdio 전송           │       │  SSE 스트리밍             │
│                      │       │                          │
│  src/mcp/server.ts   │       │  src/web/server.ts       │
│  (21줄)              │       │  (226줄)                 │
└──────────┬───────────┘       └──────────┬───────────────┘
           │                              │
           └──────────┬───────────────────┘
                      ▼
           ┌────────────────────────────┐
           │  공유 도구 핸들러            │
           │  src/mcp/tools/handlers.ts │
           │  (11개 도구 정의 + 디스패처) │
           └──────────┬─────────────────┘
                      ▼
     ┌────────────────────────────────────┐
     │         8개 도구 모듈               │
     ├────────────────────────────────────┤
     │ contract-info.ts     (메타데이터)   │
     │ contract-source.ts   (소스 읽기)    │
     │ storage.ts           (스토리지)     │
     │ on-chain.ts          (view 호출)   │
     │ governance.ts        (거버넌스)     │
     │ simulation.ts        (시뮬레이션)   │
     │ verification.ts      (DEX 검증)    │
     │ fork-test.ts         (포크 테스트)  │
     └────────────────┬───────────────────┘
                      ▼
     ┌────────────────────────────────────┐
     │         데이터 소스                  │
     ├────────────────────────────────────┤
     │ contracts/src/        746 .sol     │
     │ contracts/out/        컴파일된 ABI  │
     │ scripts/mainnet/      레지스트리    │
     │ scripts/storage/      레이아웃      │
     │ Ethereum Mainnet      RPC (viem)   │
     │ Foundry               포크 테스트    │
     └────────────────────────────────────┘
```

### 핵심 코드 경로 3가지

### 경로 1: MCP 인터페이스 (Claude Code용)

```
사용자 질문 (Claude Code 터미널)
    ↓
Claude가 MCP 프로토콜로 도구 호출 결정
    ↓
src/mcp/server.ts
  - McpServer (stdio transport)
  - registerAllTools()가 Zod 스키마로 11개 도구 등록
    ↓
각 도구 모듈의 register 함수
  예: registerVerifyTokenCompatibility(server)
  - server.tool("verify_token_compatibility", zodSchema, handler)
    ↓
handleVerifyTokenCompatibility(args)
  - viem publicClient로 eth_call 시뮬레이션
    ↓
결과를 MCP 프로토콜로 Claude에게 반환
```

핵심 파일: `src/mcp/server.ts` (21줄)

```typescript
const server = new McpServer({ name: "tokamak-dao", version: "1.0.0" });
registerAllTools(server);
const transport = new StdioServerTransport();
await server.connect(transport);
```

### 경로 2: Web 인터페이스 (브라우저용)

```
사용자 메시지 (React Chat UI)
    ↓
POST /api/chat → src/web/server.ts
    ↓
Anthropic API 호출 (시스템 프롬프트 + 도구 정의 포함)
    ↓
Phase 1: 스트리밍 응답 수신
  - SSE로 text_delta 이벤트를 브라우저에 전송
  - tool_use 블록 수집
    ↓
Phase 2: 도구 병렬 실행
  - stopReason === "tool_use"이면
  - Promise.all()로 모든 도구 동시 실행
  - executeTool(name, args) → 핸들러 디스패치
    ↓
Phase 3: 루프
  - 도구 결과를 메시지 히스토리에 추가
  - Anthropic API 재호출 (최대 50 라운드)
  - stopReason === "end_turn"이면 종료
    ↓
SSE로 최종 응답 스트리밍
```

핵심 코드 (`src/web/server.ts`):

```typescript
// 도구 호출 루프
for (let round = 0; round < MAX_TOOL_ROUNDS; round++) {
  // Phase 1: Anthropic API 스트리밍
  const response = await anthropic.messages.create({
    model: MODEL, max_tokens: CHAT_MAX_TOKENS,
    system: SYSTEM_PROMPT, tools, messages, stream: true,
  });
  // ... SSE 이벤트 전송 ...

  if (stopReason !== "tool_use") break;

  // Phase 2: 도구 병렬 실행
  const toolResults = await Promise.all(
    pendingTools.map(async (tool) => {
      const result = await executeTool(tool.name, tool.input);
      await sendEvent({ type: "tool_result", name: tool.name, result });
      return { type: "tool_result", tool_use_id: tool.id, content: result };
    })
  );

  // 메시지 히스토리에 추가하고 다음 라운드
  messages.push({ role: "assistant", content: assistantContent });
  messages.push({ role: "user", content: toolResults });
}
```

### 경로 3: 검증 도구 (verify_token_compatibility)

```
AI가 "TON이 Uniswap에서 거래 가능?" 질문 수신
    ↓
verify_token_compatibility 도구 호출
  args: { token_address: "0x2be5...", dex: "uniswap_v2" }
    ↓
src/mcp/tools/verification.ts
  1. findTokenHolder() — 알려진 주소(DAOVault, DepositManager 등)에서 잔액 조회
     publicClient.readContract({ functionName: "balanceOf", args: [knownAddress] })
     → 잔액 > 0인 주소 = holder

  2. 시나리오별 시뮬레이션:
     approve:
       simulateCall(holder, tokenAddress, approveCalldata)

     transferFrom:
       simulateCall(router, tokenAddress, transferFromCalldata)
       → TON에서 revert: "SeigToken: only sender or recipient can transfer"

     swap:
       simulateCall(holder, routerAddress, swapCalldata)
       → revert (transferFrom 실패로 인해)
    ↓
마크다운 리포트 생성 (성공/실패, 가스, 리버트 이유)
```

### 핵심 설계 결정

**1. "추측 금지" 프로토콜을 여러 레이어에서 강제**

이 프로젝트의 가장 중요한 설계 결정. 단순히 프롬프트에 "추측하지 마"라고 쓰는 것으로는 불충분하므로, 여러 계층에서 강제한다:

| 계층 | 파일 | 방법 |
| --- | --- | --- |
| 프로젝트 규칙 | `CLAUDE.md` | 질문 패턴별 필수 도구 매핑 테이블 |
| 시스템 프롬프트 | `src/web/system-prompt.ts` | "Verification-First Rule" 명시 |
| 도구 결과 | `contract-info.ts` | 토큰 반환 시 "DEX 호환성은 verify로 검증하세요" 경고 삽입 |
| 설정 | `.claude/settings.json` | 프롬프트 제출 전후 검증 여부 체크 (hooks) |

**2. 듀얼 인터페이스, 단일 도구 핸들러**

MCP 서버(Claude Code)와 Web 서버(브라우저)가 동일한 `handlers.ts`를 공유:

```
handlers.ts의 두 가지 export:
  getToolDefinitions()  → Anthropic API 형식의 도구 정의 (Web 서버용)
  executeTool(name, args) → 이름으로 핸들러 디스패치 (Web 서버용)

각 도구 모듈의 export:
  register[ToolName](server) → MCP 서버에 Zod 스키마로 등록
  handle[ToolName](args) → 실제 로직 (양쪽 공유)
```

이 구조 덕분에 도구 로직이 한 곳에만 존재하고, 인터페이스를 추가해도 도구를 다시 구현할 필요가 없다.

**3. 스토리지 레이아웃 프리컴퓨팅**

Solidity는 상태 변수를 256비트 스토리지 슬롯에 패킹한다. 이를 디코딩하려면 컴파일러의 storage layout이 필요한데, 매번 Etherscan을 호출하는 대신 미리 추출해서 JSON으로 저장:

```
scripts/storage/extract-layouts.ts → scripts/storage/layouts/*.json (40개)

레이아웃 JSON 구조:
{
  "contractName": "SeigManagerV1_3",
  "layout": {
    "storage": [
      { "label": "_ton",      "slot": "0", "type": "t_address" },
      { "label": "_wton",     "slot": "1", "type": "t_address" },
      { "label": "seigPerBlock", "slot": "5", "type": "t_uint256" }
    ]
  }
}
```

런타임 디코딩 (`read_contract_state`):

```
eth_getStorageAt(address, slot=0) → 0x000...2be5e8c49...
→ 레이아웃 참조 → slot 0 = _ton (address)
→ 디코딩: 0x2be5e8c4936...
```

**4. 프록시 패턴 자동 처리**

Tokamak 컨트랙트 대부분이 프록시 패턴을 사용한다. 도구가 이를 자동 처리:

```
컨트랙트 레지스트리 (contracts.json):
  "SeigManagerProxy": { address: "0x710...", implementation: "SeigManagerV1_3" }

read_contract_state("SeigManagerProxy") →
  - 주소: SeigManagerProxy (0x710...) ← 여기서 스토리지를 읽음
  - 레이아웃: SeigManagerV1_3 ← 이 구현체의 레이아웃으로 디코딩
```

**5. Web 서버의 도구 호출 루프**

Anthropic API의 tool_use를 직접 구현한 에이전틱 루프:

```
구조:
  for (round = 0; round < 50; round++) {
    API 호출 (스트리밍)
    if (도구 호출 없음) break
    도구 병렬 실행 (Promise.all)
    결과를 히스토리에 추가
    다음 라운드
  }

설정값 (src/config.ts):
  MAX_TOOL_ROUNDS = 50            // 최대 도구 호출 라운드
  MAX_TOOL_RESULT_CHARS = 12,000  // API에 보내는 최대 크기
  CHAT_MAX_TOKENS = 16,384        // 응답 최대 토큰
  DEFAULT_CHAT_MODEL = "claude-sonnet-4-5-20250929"
```

---

## 5. 빌드 과정 (어떻게 만들어졌는지)

### Step 1: 데이터 수집 — 컨트랙트 소스와 메타데이터

```bash
# 1. Etherscan에서 검증된 컨트랙트 소스 다운로드
bun run scripts/storage/fetch-sources.ts
# → contracts/src/ 에 746개 .sol 파일 생성 (42개 디렉토리)

# 2. Foundry로 컴파일 → ABI 생성
cd contracts && forge build
# → contracts/out/ 에 컴파일된 ABI JSON 생성

# 3. 스토리지 레이아웃 추출
bun run scripts/storage/extract-layouts.ts
# → scripts/storage/layouts/ 에 40개 레이아웃 JSON 생성

# 4. DAO 안건 데이터 수집
bun run scripts/fetch-agendas.ts
# → scripts/mainnet/agendas.json (80+ 안건)

# 5. 컨트랙트 레지스트리 수동 구축
# → scripts/mainnet/contracts.json (주소, 타입, 프록시 관계)
```

### Step 2: MCP 도구 개발

파일 구조:

```
src/mcp/tools/
├── index.ts          # registerAllTools() — 전체 도구 등록
├── handlers.ts       # getToolDefinitions() + executeTool() — 웹 서버용
├── validation.ts     # 입력 검증 유틸리티
├── contract-info.ts  # get_contract_info
├── contract-source.ts# read_contract_source, search_contract_code
├── storage.ts        # read_storage_slot, read_contract_state
├── on-chain.ts       # query_on_chain
├── governance.ts     # fetch_agenda, decode_calldata
├── simulation.ts     # simulate_transaction
├── verification.ts   # verify_token_compatibility
└── fork-test.ts      # run_fork_test
```

개발 순서:

1. 코드 탐색 도구 먼저 (contract-info, contract-source) — 기본적인 컨트랙트 정보 접근
1. 온체인 조회 도구 (storage, on-chain) — 실제 블록체인 데이터 읽기
1. 거버넌스 도구 (governance) — DAO 안건 분석
1. 시뮬레이션 도구 (simulation) — 트랜잭션 테스트
1. 검증 도구 (verification, fork-test) — 프로젝트의 핵심 차별점

### Step 3: 검증 시스템 구축 — 프로젝트의 차별점

`verify_token_compatibility`의 핵심 로직 (`src/mcp/tools/verification.ts`):

```
1. findTokenHolder() — 알려진 Tokamak 컨트랙트에서 토큰 잔액 조회
   - DAOVault (0x2520CD65...), SwapProxy (0x30e65B3A...) 등
   - DepositManagerProxy (0x0b58ca72...) (WTON용)
   - balanceOf > 0인 주소를 holder로 사용

2. 시나리오 시뮬레이션 — viem의 simulateCall()로 eth_call
   - approve: holder가 router에게 approve
   - transferFrom: router가 holder 대신 전송 (여기서 TON은 revert)
   - swap: 실제 DEX 스왑 calldata로 시뮬레이션

3. 결과 리포트 — 각 시나리오의 성공/실패, 가스, revert 이유
```

Foundry 포크 테스트 (`contracts/test/TONCompatibility.t.sol`, 197줄):

```solidity
// TON의 transferFrom 제한을 증명하는 테스트
function test_TON_TransferFrom_ThirdParty_Reverts() public {
    uint256 amount = 100 ether;

    vm.prank(user);
    ton.approve(UNISWAP_V2_ROUTER, amount);

    vm.prank(UNISWAP_V2_ROUTER);
    vm.expectRevert("SeigToken: only sender or recipient can transfer");
    ton.transferFrom(user, recipient, amount);
}

// WTON은 표준 ERC20이므로 성공
function test_WTON_TransferFrom_ThirdParty_Succeeds() public {
    uint256 amount = 100 ether;

    vm.prank(user);
    wton.approve(UNISWAP_V2_ROUTER, amount);

    vm.prank(UNISWAP_V2_ROUTER);
    wton.transferFrom(user, recipient, amount); // 성공
}

// 실제 Uniswap V2 스왑도 실패
function test_TON_UniswapV2_Swap_Reverts() public {
    vm.prank(user);
    ton.approve(UNISWAP_V2_ROUTER, amountIn);

    address[] memory path = new address[](2);
    path[0] = TON;
    path[1] = WETH;

    vm.prank(user);
    vm.expectRevert();
    IUniswapV2Router(UNISWAP_V2_ROUTER).swapExactTokensForTokens(
        amountIn, 0, path, user, block.timestamp + 3600
    );
}
```

### Step 4: Web Chat UI

```
프론트엔드 (React 19 + Vite):
  src/client/
  ├── App.tsx              # 앱 진입점
  ├── main.tsx             # Vite 진입점
  ├── index.css            # 전역 스타일
  └── components/
      ├── Chat.tsx         # 메인 채팅 컴포넌트
      └── chat/
          ├── useChat.ts       # SSE 스트리밍 & 상태 관리 훅
          ├── ChatInput.tsx    # 입력 영역
          ├── ChatBubble.tsx   # 메시지 버블
          ├── ToolCallBlock.tsx# 도구 호출 결과 (접기/펼치기)
          ├── ChatLoader.tsx   # 로딩 인디케이터
          ├── AsciiSpinner.tsx # ASCII 스피너
          ├── TerminalHeader.tsx # 터미널 스타일 헤더
          └── types.ts        # 공유 타입 정의

백엔드 (Hono + Bun):
  src/web/
  ├── server.ts           # API 서버 + SSE 스트리밍 + 도구 루프
  └── system-prompt.ts    # AI 시스템 프롬프트 (검증-우선 규칙 포함)
```

SSE 이벤트 타입:

```
text_delta   → AI의 텍스트 응답 (스트리밍)
tool_use     → AI가 도구를 호출함 (이름, 인자)
tool_result  → 도구 실행 결과 (성공/실패, 결과 텍스트)
thinking     → AI가 다음 응답을 생각 중 (도구 결과 처리)
done         → 대화 종료
error        → 에러 발생
```

### Step 5: 규칙과 프로토콜

`CLAUDE.md`에 프로젝트 규칙 명시:

- 검증-우선 프로토콜 (질문 패턴별 필수 도구 매핑)
- 아키텍처 설명 (새 세션에서도 맥락 이해)
- 워크플로우 규칙 (계획→실행→검증)

`src/web/system-prompt.ts`에 동일 규칙을 자연어로 삽입:

- Web UI에서도 동일한 검증-우선 행동을 보장
- "Verification-First Rule" 섹션에서 `verify_token_compatibility`를 **반드시** 먼저 호출하도록 명시

`.claude/settings.json`의 hooks:

- UserPromptSubmit hook: 프롬프트 제출 전 체크
- Stop hook: 응답 완료 후 검증 누락 체크

---

## 6. 기술 스택

| 영역 | 기술 | 선택 이유 |
| --- | --- | --- |
| 런타임 | Bun | TypeScript 네이티브 실행, 빠른 시작 시간 |
| AI 프로토콜 | MCP SDK (`@modelcontextprotocol/sdk`) | Claude Code와 stdio로 직접 연결 |
| AI API | Anthropic SDK (`@anthropic-ai/sdk`) | Web UI용 도구 호출 루프 |
| 블록체인 | viem | 타입 안전한 Ethereum RPC 클라이언트 |
| 포크 테스트 | Foundry (forge) | 메인넷 상태에서 Solidity 테스트 실행 |
| 웹 서버 | Hono | 경량, Bun 네이티브, SSE 지원 |
| 프론트엔드 | React 19 + Vite | 빠른 개발, SSE 이벤트 처리 |
| 데이터 | JSON 파일 | 외부 DB 불필요, 버전 관리 가능 |

---

## 7. 데모 준비 체크리스트

### 환경

- [ ] `.env`에 `ALCHEMY_RPC_URL`, `ANTHROPIC_API_KEY` 설정
- [ ] `bun install` 완료
- [ ] Web 서버: `bun run dev:web` (포트 3333)
- [ ] 클라이언트: `bun run dev:client` (포트 5173)

### 사전 테스트

- [ ] Web UI에서 간단한 질문 ("TON 컨트랙트 정보")
- [ ] 검증 도구 테스트 ("TON이 Uniswap에서 거래 가능한가?")
- [ ] 거버넌스 도구 테스트 ("안건 0번을 분석해줘")

### 백업

- 네트워크 문제 시: `agendas.json` 캐시로 거버넌스 데모 가능
- Web UI 문제 시: Claude Code 터미널에서 직접 MCP 도구 사용

---

## 8. 청중이 기억해야 할 것

1. **AI가 추측하면 블록체인에서는 치명적이다** → 온체인 검증이 유일한 답
1. **도구를 가진 AI는 다르다** → 11개 전문 도구로 실제 블록체인 접근
1. **증거 기반** → 모든 답변이 `eth_call` 시뮬레이션이나 Foundry 포크 테스트로 뒷받침됨
1. **아키텍처가 깔끔하다** → 듀얼 인터페이스 + 단일 도구 핸들러, 코드 중복 없음