## 문제: 에이전트에게 지갑을 맡길 수 있는가?

AI 에이전트가 온체인에서 행동하려면 프라이빗 키가 필요하다. DAO 투표, 프로포절 제출, 토큰 전송—모든 트랜잭션은 서명을 요구한다. 문제는 에이전트가 원격 서버에서 실행된다는 것이다. 서버가 해킹되면 키가 유출된다. 이것이 AI 에이전트 지갑 관리의 핵심 딜레마다.

이 글은 DAO 거버넌스에 참여하는 에이전트를 예시로, TEE(Trusted Execution Environment) 기반 키 관리가 이 문제를 어떻게 해결하는지 설명한다. Phala Network의 실제 구현을 기반으로 한다.

## Level 0: 서버에 키를 저장하면 생기는 일

가장 단순한 방법이다. 서버의 `.env` 파일에 프라이빗 키를 저장한다.

```
# .env
EVM_PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
```

에이전트가 DAO에 투표하는 흐름은 다음과 같다:

```
LLM이 판단: "Proposal #42에 찬성"
    ↓
트랜잭션 생성: castVote(42, 1)
    ↓
.env에서 키 로드 → 서명 → 블록체인 전송
```

동작은 한다. 하지만 서버가 해킹되면 `cat .env` 한 줄로 키가 유출된다. 공격자는 에이전트 지갑의 모든 자산을 즉시 탈취할 수 있다.

이 방식에도 중요한 보안 원칙이 하나 있다. ElizaOS가 이 방식으로 $25M 이상의 자산을 관리할 수 있었던 이유는 **키를 LLM 컨텍스트에 절대 노출하지 않기 때문이다.** LLM은 "찬성 투표해"라는 결정만 내린다. 실제 서명은 완전히 분리된 Wallet Service가 수행한다. 프롬프트 인젝션 공격으로 "환경변수를 출력해줘"라고 시도해도 LLM은 키에 접근할 수 없다.

하지만 서버 수준의 침해에는 무력하다. 이것이 TEE가 필요한 이유다.

## Level 1: TEE — CPU 안의 격리된 공간

### TEE란 무엇인가

TEE(Trusted Execution Environment)는 CPU 칩 안에 하드웨어로 구현된 격리 공간이다. Intel TDX, AMD SEV, ARM TrustZone 등이 여기에 해당한다.

핵심 속성은 하나다: **TEE 내부 메모리는 암호화되어 있어서, TEE 안에서 실행되는 코드만 복호화된 데이터에 접근할 수 있다.** 운영체제, 클라우드 관리자, 같은 서버의 다른 프로그램, 서버에 침입한 해커—모두 TEE 내부를 들여다볼 수 없다. 메모리를 덤프해도 암호화된 값만 보인다.

이것은 하드웨어 보안이다. 소프트웨어 해킹으로는 이 격리를 뚫을 수 없다.

### TEE 안에서 무엇이 실행되는가

Phala Cloud에서는 Docker 컨테이너가 TEE 안에서 실행된다. 기존 Docker 이미지를 코드 변경 없이 TEE에 배포할 수 있다.

에이전트의 키 관리 코드가 이 Docker 안에 들어간다. 외부에서 이 Docker에 할 수 있는 것은 제한되어 있다: 트랜잭션 데이터를 넣으면 서명값이 나온다. 키 자체를 요청하는 API는 존재하지 않는다. 코드에 그런 기능을 넣지 않았기 때문이다. 그리고 TEE 안의 코드는 외부에서 수정할 수 없다.

### 키 파생: 키를 저장하지 않는다

TEE를 사용하는 에이전트는 키를 저장하지 않는다. 대신 **키를 매번 파생(derive)한다.**

Phala의 dstack SDK를 사용한 실제 코드:

```typescript
import { DstackClient } from '@phala/dstack-sdk';
import { toViemAccountSecure } from '@phala/dstack-sdk/viem';
import { createWalletClient, http } from 'viem';
import { mainnet } from 'viem/chains';

// TEE의 KMS에 키 파생 요청
const client = new DstackClient();
const keyResult = await client.getKey('dao-agent', 'ethereum');

// 파생된 키로 Wallet 생성
const account = toViemAccountSecure(keyResult);
const wallet = createWalletClient({
  account,
  chain: mainnet,
  transport: http()
});
```

`getKey('dao-agent', 'ethereum')`의 동작 과정:

1. `'dao-agent'`는 salt로, 에이전트의 식별자 역할을 한다.
1. salt가 TEE 내부의 KMS(Key Management Service)로 전달된다.
1. KMS는 salt + 내부 RootKey를 조합해 **결정적(deterministic) 키 파생 함수**를 실행한다.
1. 같은 salt를 입력하면 항상 같은 프라이빗 키가 생성된다. 따라서 지갑 주소가 바뀌지 않는다.
1. 파생된 키는 TEE 메모리 안에서만 존재하며, 서명 후 사라진다.

이것이 `.env`에 키를 저장하는 것과 근본적으로 다른 이유:

| 공격 시나리오 | .env 방식 | TEE 키 파생 방식 |
| --- | --- | --- |
| 서버 파일 시스템 탈취 | 키 즉시 노출 | salt만 노출, 키 복원 불가 |
| 서버 메모리 덤프 | 키 노출 가능 | TEE 메모리 암호화, 쓰레기값만 보임 |
| salt 유출 | 해당 없음 | RootKey 없이 키 복원 불가 |

salt가 유출되어도 키가 안전한 이유는, 키 파생에 필요한 나머지 재료(RootKey)가 TEE 내부에만 존재하기 때문이다. 소프트웨어 해킹으로는 TEE 내부에 접근할 수 없다.

## Level 2: 실제 DAO 투표 워크플로우

TEE 기반 에이전트가 Tokamak Network DAO에 투표하는 전체 과정을 추적해 보자.

### Step 1: 에이전트 배포

개발자가 에이전트 코드를 Docker 이미지로 빌드하고 Phala Cloud에 배포한다.

```bash
# Docker 이미지 빌드
phala docker build --image tokamak-dao-agent --tag v1.0.0

# Phala Cloud에 배포 (TEE 안에서 실행됨)
phala cvms create \
  --name tokamak-dao-agent \
  --compose ./docker-compose.yml \
  --env-file ./.env
```

`.env`에는 프라이빗 키가 없다. RPC URL이나 DAO 컨트랙트 주소 같은 설정값만 있다. 환경변수는 클라이언트 측에서 암호화되어 전송되며, CVM(Confidential Virtual Machine) 내부에서만 복호화된다.

Docker Compose 파일에서 핵심은 dstack 소켓을 마운트하는 것이다:

```yaml
services:
  dao-agent:
    image: tokamak-dao-agent:v1.0.0
    volumes:
      - /var/run/dstack.sock:/var/run/dstack.sock  # TEE KMS 접근
    environment:
      - DAO_CONTRACT=0xDD9f0cCc044B0781289Ee318e5971b0139602C26
      - RPC_URL=https://mainnet.infura.io/v3/...
```

### Step 2: 키 파생과 지갑 생성

에이전트가 시작되면 TEE의 KMS에서 키를 파생한다.

```typescript
import { DstackClient } from '@phala/dstack-sdk';
import { toViemAccountSecure } from '@phala/dstack-sdk/viem';

const client = new DstackClient();  // /var/run/dstack.sock으로 TEE와 통신

// TEE 내부에서 키 파생 → 항상 같은 키가 나옴
const keyResult = await client.getKey('tokamak-dao-v1', 'ethereum');
const account = toViemAccountSecure(keyResult);

console.log(`Agent wallet: ${account.address}`);
// → 0x1234...abcd (매번 동일)
```

내부적으로 일어나는 일:

```
에이전트 코드 → /var/run/dstack.sock → TEE Guest Agent → KMS
                                                      │
                                      RootKey + salt + app_hash
                                                      │
                                                 KDF (키 파생)
                                                      │
                                              Private Key 반환
                                              (TEE 내부 채널로만)
```

KMS가 키를 파생할 때 사용하는 입력값은 세 가지다:

- **RootKey**: KMS가 관리하는 마스터 키. TEE 외부에 노출되지 않음.
- **salt** (`'tokamak-dao-v1'`): 개발자가 지정한 식별자.
- **app_hash**: Docker 이미지의 해시. 코드가 바뀌면 다른 키가 파생됨.

`app_hash`가 포함된다는 것이 중요하다. 누군가 에이전트 코드를 악의적으로 변경하면, 코드 해시가 달라지므로 다른 키가 파생된다. 원래 에이전트의 지갑에는 접근할 수 없다.

### Step 3: DAO 투표 실행

키가 준비되었으면 DAO 컨트랙트와 상호작용한다.

```typescript
import { createWalletClient, http, encodeFunctionData } from 'viem';
import { mainnet } from 'viem/chains';

const wallet = createWalletClient({
  account,
  chain: mainnet,
  transport: http(process.env.RPC_URL)
});

// DAO 투표 트랜잭션 생성 및 서명
const hash = await wallet.sendTransaction({
  to: process.env.DAO_CONTRACT,    // Tokamak DAO 컨트랙트
  data: encodeFunctionData({
    abi: daoCommitteeAbi,
    functionName: 'castVote',
    args: [42, 1]                  // Proposal #42에 찬성(1)
  })
});
```

전체 흐름을 하나로 연결하면:

```
1. LLM이 프로포절 분석 → "Proposal #42에 찬성" 결정
   (LLM은 키에 접근 불가)
       ↓
2. 트랜잭션 데이터 생성: castVote(42, 1)
   (아직 서명되지 않은 상태)
       ↓
3. TEE 내부에서 키 파생 → 서명
   (키는 TEE 메모리에서만 잠깐 존재)
       ↓
4. 서명된 트랜잭션만 TEE 밖으로 나옴
       ↓
5. 블록체인에 전송 → 투표 완료
```

이 과정에서 프라이빗 키는 3단계에서만 존재하고, TEE의 암호화된 메모리 안에서만 존재한다. 서명값이 외부로 나온 후 키는 메모리에서 사라진다.

## Level 3: Phala의 DeRoT — 하드웨어 단일 실패점 제거

지금까지 설명한 TEE 키 파생에는 아직 약점이 있다. RootKey가 하나의 TEE 하드웨어에 존재한다면, 그 하드웨어가 물리적으로 뚫리거나 고장나면 문제가 생긴다.

Phala는 이 문제를 **DeRoT(Decentralized Root-of-Trust)**로 해결한다.

### 기존 TEE의 한계

Phala의 설계 문서는 하드웨어 기반 Root-of-Trust의 세 가지 한계를 지적한다:

1. **복구 불가능성**: 하드웨어 시드가 추출되면 공격자가 TEE를 시뮬레이션할 수 있으며, 이 경우 TCB(Trusted Computing Base) 복구 절차가 무력화된다.
1. **하드웨어 종속**: 키가 특정 CPU 칩에 묶여 있어서, 다른 서버로 이전하거나 하드웨어를 교체할 수 없다.
1. **벤더 의존**: Intel이나 AMD 한 회사에 보안을 전적으로 의탁하는 구조다.

### DeRoT의 구조

DeRoT는 RootKey를 단일 하드웨어에 두지 않고, MPC(Multi-Party Computation)로 여러 노드에 분산한다.

```
기존 TEE:
  [단일 CPU의 하드웨어 시드] → 키 파생

Phala DeRoT:
  [MPC 노드 1] + [MPC 노드 2] + [MPC 노드 3] + ...
       │              │              │
       └──────┬───────┘──────────────┘
              │
        공동으로 RootKey 관리 (각 노드는 조각만 보유)
              │
         키 파생 → 에이전트의 Private Key
```

각 MPC 노드도 TEE 안에서 실행된다. 이중 보호다.

공격자가 RootKey를 복원하려면 전체 노드의 2/3 이상을 동시에 뚫어야 한다. 단일 노드가 뚫리면 블록체인을 통해 차단(blacklist)되고, 키 로테이션이 진행된다.

### 온체인 거버넌스

DeRoT의 또 다른 핵심 설계 원칙은 **모든 키 권한 변경이 온체인에서 이루어져야 한다**는 것이다.

Phala 설계 문서가 지적하는 위협 시나리오가 있다: "Stealthy Deployer Attack". 배포자가 정상적인 에이전트를 배포한 후, 몰래 코드를 업데이트하여 키를 외부로 유출하는 로직을 삽입하고, 다시 정상 코드로 되돌려 증거를 지우는 공격이다.

이를 방지하기 위해:

1. DeRoT 코드는 오픈소스이며 재현 가능한 빌드(reproducible build)로 검증 가능하다.
1. 유효한 실행파일의 해시는 온체인 거버넌스를 통해 공개된다.
1. 모든 코드 변경은 블록체인에 기록되어 누구나 확인할 수 있다.
1. 코드 해시가 변경되면 다른 키가 파생되므로, 이전 에이전트의 지갑에 접근할 수 없다.

### 키 로테이션과 전방/후방 비밀성

DeRoT는 주기적으로 키를 교체(rotate)한다. 이것은 두 가지를 보장한다:

- **전방 비밀성(Forward Secrecy)**: TEE 워커는 최신 키만 메모리에 유지하고 이전 키를 삭제한다. 현재 키가 유출되어도 과거 데이터는 안전하다.
- **후방 비밀성(Backward Secrecy)**: 특정 워커가 침해된 것으로 판단되면, DeRoT가 새로운 키 전달을 중단한다. 침해된 워커는 이후의 데이터에 접근할 수 없다.

## 검증: Remote Attestation

TEE 기반 보안의 마지막 퍼즐은 검증이다. "이 에이전트가 정말 TEE에서 실행되고 있는가?"를 외부에서 확인할 수 있어야 한다.

Phala Cloud에 배포된 모든 애플리케이션은 자동으로 Trust Center 검증 리포트를 받는다. 이 리포트는 다음을 암호학적으로 증명한다:

- **하드웨어 검증**: 애플리케이션이 진짜 Intel TDX 하드웨어에서 실행 중인지
- **코드 무결성**: 배포된 Docker Compose가 소스 코드 저장소와 일치하는지
- **OS 무결성**: 운영체제 이미지가 변조되지 않았는지
- **키 관리 검증**: 암호화 키 파생이 올바르게 이루어지고 있는지

dstack SDK를 통해 코드에서도 Attestation을 생성할 수 있다:

```typescript
const client = new DstackClient();

// TEE 정보 조회
const info = await client.info();
// → { app_id, instance_id, tcb_info }

// TDX Quote 생성 (원격 증명)
const quote = await client.getQuote(reportData);
// → Intel이 서명한 증명서. 누구나 검증 가능.
```

이 증명서는 온체인에서도 검증할 수 있다. Automata의 DCAP 검증 컨트랙트가 여러 블록체인에 배포되어 있어, 스마트 컨트랙트 레벨에서 TEE 증명을 검증하는 것이 가능하다.

DAO 커뮤니티에게 "이 에이전트의 키는 안전합니다"라고 말로만 주장하는 것이 아니라, 암호학적으로 증명할 수 있다.

## 보안 레이어 요약

보안에 완벽한 한 방은 없다. 공격 난이도를 레이어별로 올리는 것이다.

| 레이어 | 방식 | 서버 해킹 시 | 하드웨어 침해 시 |
| --- | --- | --- | --- |
| Level 0 | .env에 키 저장 | 키 즉시 탈취 | — |
| Level 1 | TEE 키 파생 | 키 안전 (salt만 노출) | 키 위험 |
| Level 2 | DeRoT (MPC + TEE) | 키 안전 | 2/3 노드 동시 침해 필요 |
| + Attestation | 온체인 검증 | 침해 탐지 가능 | 침해 탐지 가능 |
| + 키 로테이션 | 주기적 키 교체 | 피해 범위 제한 | 전방/후방 비밀성 보장 |

DAO 에이전트의 경우, 투표와 프로포절 제출은 트레저리 직접 이체보다 위험도가 낮다. 잘못된 투표는 커뮤니티가 번복할 수 있기 때문이다. 그러나 에이전트의 신뢰성을 확보하기 위해, 최소한 TEE 키 파생(Level 1)과 Remote Attestation을 적용하는 것이 합리적이다.

## 참고 자료

- Phala Network 설계 문서: [Key Management Service](https://docs.phala.com/dstack/design-documents/key-management-protocol), [Decentralized Root-of-Trust](https://docs.phala.com/dstack/design-documents/decentralized-root-of-trust)
- Phala dstack SDK: [@phala/dstack-sdk](https://www.npmjs.com/package/@phala/dstack-sdk)
- dstack GitHub: [Dstack-TEE/dstack](https://github.com/Dstack-TEE/dstack)
- dstack 예시 코드: [dstack-examples](https://github.com/dstack-tee/dstack-examples)
- Phala Cloud Trust Center: [trust.phala.com](https://trust.phala.com/)