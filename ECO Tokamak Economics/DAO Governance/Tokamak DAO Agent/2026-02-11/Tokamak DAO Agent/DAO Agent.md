1. 컨트랙트를 완전히 이해한다.
1. 새로운 안건이 올라온다. 안건은 + 컨트랙트 실행과 함께이다. 실제로 이를 실행하고 state diff를 비교하고 이에 대한 분석을 마친다.
1. 마크다운의 내용을 통해 calldata와 Proposal 생성을 도와준다.
1. 각각의 Agent는 특성을 갖고 있다. 각 Agent는 자신의 이해관계를 바탕으로 자신만으 의견을 내도록 한다.
1. 안건을 만든다. —> 이를 기반으로 어떤 target에 어떤 값을 가지고 transaction을 만들어야 하는지를 만든다.
1. 해당 안건에 대해 분석하는 것을 만든다.
1. 

DAO에 새로운 안건이 제출되면 컨트랙트 실행이 필요합니다. Agent는 해당 안건이 토카막 네트워크 생태계에 미칠 영향을 예측할 수 있습니다. 맞나요?

1. 예측하는 것이 아니라 실제로 검색하고 실행하도록 만들었다.
eg. Uniswap, SushiSwap, CowSwap, ABCD
1. 

### 개요

DAO 안건(agenda)은 컨트랙트 주소 배열(targets[])과 함수 호출 데이터(functionBytecodes)로 구성되며, atomicExecute 플래그에 따라 순차적으로 실행됩니다. 현재 에이전트는 개별 도구(query_on_chain, decode_calldata, simulate_transaction)를 수동으로 연결해야 하며, 다중 타겟의 연쇄 실행 시뮬레이션은 지원되지 않습니다.

**목표:** 안건 ID 하나만으로 전체 영향 분석을 자동으로 수행하는 `analyze_agenda` 도구를 개발하여, 에이전트가 DAO 제안이 생태계에 미치는 영향을 정확하게 예측할 수 있도록 합니다.

---

## 변경 파일 요약

| **파일** | **작업** |
| --- | --- |
| src/mcp/tools/agenda-analysis.ts | 신규 - 핵심 분석 로직 |
| contracts/test/AgendaSimulation.t.sol | 신규 - 멀티타겟 원자적 실행 포크 테스트 |
| src/mcp/tools/fork-test.ts | 수정 - env_vars 파라미터 추가 |
| src/mcp/tools/handlers.ts | 수정 - 도구 등록 (11번째 도구) |
| src/mcp/tools/index.ts | 수정 - MCP 서버 등록 |
| src/web/system-prompt.ts | 수정 - 안건 분석 워크플로우 추가 |

## Step 1: contracts/test/AgendaSimulation.t.sol 생성

Foundry 포크 테스트 파일입니다. AGENDA_ID 환경변수로 안건 ID를 받아 DAOCommitteeProxy로 prank하여 원자적 실행을 시뮬레이션합니다.

**핵심 구조:**

```solidity
contract AgendaSimulation is Test {
    address constant DAO_COMMITTEE_PROXY = 0xDD9f0cCc044B0781289Ee318e5971b0139602C26;
    address constant DAO_AGENDA_MANAGER = 0xcD4421d082752f363E1687544a09d5112cD4f484;
    address constant TON = 0x2be5e8c109e2197D077D13A82dAead6a9b3433C5;
    address constant WTON = 0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2;
    address constant DAO_VAULT = 0x2520CD65BAa2cEEe9E6Ad6EBD3F45490C42dd303;
    address constant SEIG_MANAGER = 0x0b55a0f463b6DEFb81c6063973763951712D0E5F;

    function setUp() public {
        agendaId = vm.envUint("AGENDA_ID");
    }

    function test_SimulateAgenda() public {
        // 1. getExecutionInfo(agendaId)로 targets, functionBytecodes, atomicExecute 읽기
        // 2. 주요 상태 스냅샷 (DAOVault 잔액, seigPerBlock 등)
        // 3. vm.prank(DAO_COMMITTEE_PROXY)로 각 target.call(calldata) 실행
        // 4. atomicExecute면 실패 시 전체 revert
        // 5. 실행 후 상태 스냅샷 → before/after diff 로깅
    }
}
```

**패턴:** 기존 Seigniorage.t.sol 스타일을 따릅니다 (minimal interfaces, console.log, vm.prank).

**상태 추적 대상:**

- DAOVault: TON/WTON/ETH 잔액
- SeigManager: seigPerBlock
- 대상 컨트랙트별 주요 파라미터 (console.log로 출력)

---

## Step 2: src/mcp/tools/fork-test.ts 수정 — env_vars 지원

`run_fork_test`에 `env_vars` 옵션 파라미터를 추가합니다.

**변경 내용:**

1. `handleRunForkTest` 함수 시그니처에 `env_vars?: Record&lt;string, string&gt;` 추가
1. `Bun.spawn`의 env에 `...(args.env_vars || {})` 머지
1. `handlers.ts`의 ToolArgsMap과 tool definition에 `env_vars` 추가
1. MCP 서버 등록에도 Zod 스키마 추가

**기존 코드** (fork-test.ts:63-71):

```typescript
const proc = Bun.spawn(["forge", ...forgeArgs], {
    cwd: CONTRACTS_DIR,
    env: {
        ...process.env,
        FOUNDRY_PROFILE: "fork",
    },
```

**변경 후:**

```typescript
const proc = Bun.spawn(["forge", ...forgeArgs], {
    cwd: CONTRACTS_DIR,
    env: {
        ...process.env,
        FOUNDRY_PROFILE: "fork",
        ...(args.env_vars || {}),
    },
```

*참고:* env_vars 키/값은 영숫자와 언더스코어만 허용합니다 (커맨드 인젝션 방지).

---

## Step 3: src/mcp/tools/agenda-analysis.ts 생성 — 핵심 분석 로직

기존 도구의 핸들러를 호출하지 않고, 공유 인프라(publicClient, loadAllAbis, contracts.ts)를 직접 사용하여 구조화된 데이터로 처리합니다. 이를 통해 마크다운 파싱 없이 깔끔하게 동작합니다.

**재사용할 기존 모듈:**

- `src/mcp/client.ts` → publicClient (viem RPC 클라이언트)
- `src/mcp/data/abis.ts` → loadAllAbis(), loadAbi() (ABI 로딩)
- `src/mcp/data/contracts.ts` → getContractByName(), getContractName(), getAllContracts() (컨트랙트 조회)
- `src/mcp/tools/validation.ts` → validateAddress(), formatError() (검증 유틸)
- `src/mcp/tools/fork-test.ts` → handleRunForkTest() (포크 테스트 실행)

**handleAnalyzeAgenda(args) 워크플로우:**

```
Input: { agenda_id: string, include_fork_test?: boolean }
│
▼
┌─── 1. 안건 메타데이터 조회 ───┐
│  numAgendas() → 존재 확인      │
│  getExecutionInfo(id)          │
│  getAgendaStatus(id)           │
│  getVotingCount(id)            │
└───────────────────────────────┘
│
▼
┌─── 2. 콜데이터 디코딩 ────────┐
│  각 functionBytecodes[i]를     │
│  viem.decodeFunctionData()로   │
│  함수명 + 인자 추출            │
│  (loadAllAbis() 재사용)        │
└───────────────────────────────┘
│
▼
┌─── 3. 개별 시뮬레이션 ────────┐
│  각 (target, calldata)를       │
│  publicClient.call()로 시뮬    │
│  from: DAOCommitteeProxy       │
│  성공/실패 + revert reason     │
└───────────────────────────────┘
│
▼
┌─── 4. 포크 테스트 (선택) ─────┐
│  handleRunForkTest({           │
│    test_pattern: "test_Sim*",  │
│    contract_pattern: "Agenda*",│
│    env_vars: {AGENDA_ID: id}   │
│  })                            │
│  → 원자적 실행 + 상태 diff     │
└───────────────────────────────┘
│
▼
┌─── 5. 리스크 평가 ────────────┐
│  타겟 분석:                     │
│  - DAOVault → 재무 위험        │
│  - upgradeTo → 프록시 업그레이드│
│  - set*/update* → 파라미터 변경│
│  - transfer → 토큰 이동        │
└───────────────────────────────┘
│
▼
마크다운 보고서 출력
```

**출력 형식 (마크다운):**

### Agenda #N 분석 보고서

### 개요

- 상태: VOTING / WAITING_EXEC / ...
- 투표: 찬성 N / 반대 N / 기권 N
- 원자적 실행: true/false
- 대상 컨트랙트: N개

### 실행 호출 상세

### Call 1: SeigManager.setSeigPerBlock(uint256)

- 타겟: 0x0b55... (SeigManagerProxy)
- 인자: seigPerBlock = 5000000000000000000000000000
- 시뮬레이션: SUCCESS (gas: 45,000)

### Call 2: ...

### 포크 테스트 결과

- 전체 실행: SUCCESS / FAILED
- 상태 변경:
  - seigPerBlock: 3.92e27 → 5.0e27
  - DAOVault TON: 변동 없음

### 리스크 평가

- 레벨: MEDIUM
- 요인:
  - 시뇨리지 파라미터 변경 (seigPerBlock 28% 증가)
  - 스테이커 보상에 직접 영향

---

## Step 4: src/mcp/tools/handlers.ts 수정 — 도구 등록

1. import 추가: `handleAnalyzeAgenda from ./agenda-analysis.ts`
1. `getToolDefinitions()`에 11번째 도구 추가:
```typescript
{
    name: "analyze_agenda",
    description: "DAO 안건을 종합 분석합니다. 실행 호출 디코딩, 시뮬레이션, 포크 테스트, 리스크 평가를 수행합니다.",
    input_schema: {
        properties: {
            agenda_id: { type: "string", description: "Agenda ID (e.g. '15')" },
            include_fork_test: { type: "boolean", description: "Run atomic execution fork test (default: true)" }
        },
        required: ["agenda_id"]
    }
}
```
1. ToolArgsMap에 타입 추가
1. `executeTool()` switch에 case 추가

---

## Step 5: src/mcp/tools/index.ts 수정 — MCP 등록

`registerAgendaAnalysisTool`을 import하고 `registerAllTools()`에 추가:

```typescript
// Phase 6: Agenda Analysis
registerAgendaAnalysisTool(server);
```

---

## Step 6: src/web/system-prompt.ts 수정 — 시스템 프롬프트 업데이트

**Capabilities** 섹션에 추가:

### Governance Analysis

- **analyze_agenda**: DAO 안건 종합 분석 (호출 디코딩 + 시뮬레이션 + 포크 테스트 + 리스크 평가)

**Behavior Guidelines**에 추가:

> **6. Agenda Analysis** - DAO 안건 분석 요청 시:
> - `analyze_agenda` 도구를 사용하여 종합 보고서 생성
> - 디코딩된 호출의 의미를 사용자가 이해할 수 있게 설명
> - 리스크가 있으면 명확히 경고

---

## Step 7: run_fork_test env_vars를 handlers.ts에도 반영

`handlers.ts`의 ToolArgsMap과 tool definition에 `env_vars` 추가:

```typescript
run_fork_test: { 
    test_pattern: string; 
    contract_pattern?: string; 
    verbosity?: number; 
    env_vars?: Record<string, string> 
};
```

tool definition의 `input_schema.properties`에:

```typescript
env_vars: { 
    type: "object", 
    description: "Environment variables for forge test" 
}
```

---

## Verification

### 1. 포크 테스트 단독 실행

실제 안건 ID로 테스트 (예: 과거 실행된 안건):

```bash
AGENDA_ID=1 FOUNDRY_PROFILE=fork forge test --match-contract AgendaSimulation --fork-url $ALCHEMY_RPC_URL -vvv
```

### 2. MCP 도구로 테스트

Claude Code에서:

```typescript
analyze_agenda(agenda_id: "1")
analyze_agenda(agenda_id: "1", include_fork_test: false)  // 빠른 분석만
```

### 3. 기존 도구 회귀 확인

기존 포크 테스트가 여전히 동작하는지 확인:

```bash
FOUNDRY_PROFILE=fork forge test --match-contract TONCompatibility --fork-url $ALCHEMY_RPC_URL -vvv
FOUNDRY_PROFILE=fork forge test --match-contract StakingDeposit --fork-url $ALCHEMY_RPC_URL -vvv
```

### 4. Web UI에서 테스트

- Web 서버 시작 후 "안건 1번을 분석해줘" 요청
- `analyze_agenda` 도구가 호출되고 보고서가 생성되는지 확인

### 5. 에지 케이스

- 존재하지 않는 안건 ID → 에러 메시지
- 이미 실행된 안건 → 정상 분석 (실행 완료 표시)
- 레지스트리에 없는 타겟 주소 → "알 수 없는 컨트랙트" 표시 + 콜데이터 디코딩 시도