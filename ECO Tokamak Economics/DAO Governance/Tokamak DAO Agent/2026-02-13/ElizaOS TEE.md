## ElizaOS TEE 통합 방식

ElizaOS는 **@elizaos/plugin-tee** 플러그인을 통해 TEE를 통합하며, 키 파생과 원격 증명 두 가지 핵심 기능을 제공합니다.

### 🔐 TEE 벤더

- **Phala Network (dstack)**를 유일한 벤더로 지원
- **TappdClient**로 Phala의 dstack TEE와 통신
- **Intel TDX** 기반 하드웨어 사용
- **3가지 동작 모드**:
  - LOCAL: localhost:8090 시뮬레이터
  - DOCKER: host.docker.internal:8090
  - PRODUCTION: 실제 TEE 환경

### 🔑 키 파생 (DeriveKeyProvider)

```javascript
TappdClient.deriveKey(path, subject)
    ↓
rawDeriveKey → SHA-256 또는 Keccak-256 해싱
    ↓
Ed25519 (Solana) 또는 ECDSA (EVM) 키페어 생성
```

- **Solana**: rawDeriveKey() → SHA-256 → Ed25519 Keypair (첫 32바이트를 시드로 사용)
- **EVM**: rawDeriveKey() → Keccak-256 → viem의 PrivateKeyAccount 생성
- WALLET_SECRET_SALT를 salt로 사용
- 프라이빗 키는 TEE 엔클레이브 메모리 내에서만 존재

### 🛡️ 원격 증명 (RemoteAttestationProvider)

- **TappdClient.tdxQuote()**로 TDX Quote 생성
- RTMR 값(0~3)을 포함한 증명 보고서 반환
- 제3자가 에이전트가 실제 TEE 환경에서 실행 중임을 검증 가능

### 🔌 플러그인 구조

```typescript
const teePlugin: Plugin = {
  name: "tee",
  actions: [remoteAttestationAction],
  providers: [
    remoteAttestationProvider,
    deriveKeyProvider,
  ],
};
```

런타임의 getSetting() 등을 통해 다른 플러그인에서도 키 파생 및 증명 서비스 요청 가능

### ⚖️ 우리 프로젝트와의 비교

| **구분** | **ElizaOS plugin-tee** | **우리 agent-key-management** |
| --- | --- | --- |
| TEE 벤더 | Phala (dstack) + Intel TDX | 시뮬레이터 (dstack 확장 가능) |
| 키 파생 | TappdClient.deriveKey() → 해싱 | HKDF-SHA256 계층적 파생 |
| 키 관리 | 파생만 (lifecycle 없음) | 생성/회전/폐기 전체 lifecycle |
| 정책 엔진 | 없음 | caller/spending-limit/rate-limit |
| 증명 | TDX Quote (RTMR) | 시뮬레이션된 attestation |
| 서명 | viem PrivateKeyAccount | viem toAccount() 커스텀 서명 |

**핵심 차이점**: ElizaOS는 키 파생과 서명에 집중하는 반면, 우리 프로젝트는 키 lifecycle 관리와 정책 기반 서명 제어까지 포괄합니다.

### 📚 참고 자료

- [elizaos-plugins/plugin-tee](https://github.com/elizaos-plugins/plugin-tee)
- [elizaos-plugins/plugin-tee-log](https://github.com/elizaos-plugins/plugin-tee-log)
- [elizaos-plugins/plugin-sgx](https://github.com/elizaos-plugins/plugin-sgx)
- [elizaos-plugins/plugin-tee-marlin](https://github.com/elizaos-plugins/plugin-tee-marlin)
- [Phala-Network/ai16zTEE](https://github.com/Phala-Network/ai16zTEE)