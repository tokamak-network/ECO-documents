# Farcaster + Hacker News 시딩 가이드 — 복사/붙여넣기 Ready

> 런칭일: 2026-02-25 (수)
> Farcaster: KST 17:30 (PH 런칭 30분 후)
> HN: 2/26 (목) KST 02:00 (HN 골든타임 PT 09:00)

---

## Part 1: Farcaster / Warpcast

### 채널별 포스팅 일정

| 날짜 | KST | 채널 | 포스트 |
|------|-----|------|--------|
| 2/25 (수) | 17:30 | /ethereum | 메인 캐스트 (아래 Cast A) |
| 2/26 (목) | 14:00 | /defi | DeFi 특화 캐스트 (Cast B) |
| 2/26 (목) | 15:00 | /nft | NFT 특화 캐스트 (Cast C) |
| 2/26 (목) | 16:00 | /base | Base 특화 캐스트 (Cast D) |
| 2/27 (금) | 10:00 | /korean | 한국어 캐스트 (Cast E) |

---

### Cast A — /ethereum (메인, 2/25)

```
Just built something fun — paste any ETH address and get your RPG hero card in 10 seconds

8 classes, 7 stats, AI-generated lore based on your on-chain history.

No wallet connect. No signing. Just vibes.

Some results so far:
- vitalik.eth → Lv.33 Hunter, Power 62,045
- stani.eth → Lv.32 Priest, Power 62,005
- pranksy.eth → Lv.49 Hunter, Power 70,140

What class is your wallet?

https://ethrpg.app?utm_source=farcaster&utm_medium=organic&utm_campaign=launch_seed
```

**첨부**: vitalik.eth 카드 이미지 (`screenshots/cards/vitalik.png`)

---

### Cast B — /defi (2/26)

```
Turns out heavy DEX users get classified as Rogues

Stablecoin movers? Merchants.
Gas-heavy contract deployers? Priests.

8 RPG classes based on your actual on-chain behavior. AI writes your hero lore.

stani.eth is a Priest with Power 62,005 — fitting for the Aave founder

What's your DeFi alter ego?

https://ethrpg.app?utm_source=farcaster&utm_medium=organic&utm_campaign=launch_defi
```

---

### Cast C — /nft (2/26)

```
NFT collectors = Hunters

pranksy.eth is a Lv.49 Hunter, Power 70,140 — the highest we've seen

Your wallet's NFT ratio, trade history, and contract interactions determine your class and stats. AI generates a unique hero backstory.

Are you a Hunter too?

https://ethrpg.app?utm_source=farcaster&utm_medium=organic&utm_campaign=launch_nft
```

---

### Cast D — /base (2/26)

```
Works with any ETH address — Base wallets included

Paste your address, get an RPG hero card with class, stats, and AI lore in 10 seconds.

wilsoncusack.eth (Base engineer) → Lv.14 Warrior, Power 23,680
jessepollak.eth (Base creator) → Lv.28 Hunter, Power 47,195

No connect. No sign. Read-only.

https://ethrpg.app?utm_source=farcaster&utm_medium=organic&utm_campaign=launch_base
```

---

### Cast E — /korean (2/27, 한국어)

```
이더리움 지갑 주소만 넣으면 RPG 캐릭터 카드가 나옴

8종 직업, 7종 스탯, AI가 만든 영웅 서사까지.

키 연결 없음. 서명 없음. 조회만.

vitalik.eth → Lv.33 사냥꾼, 전투력 62,045
stani.eth → Lv.32 사제, 전투력 62,005

내 지갑은 뭘까?

https://ethrpg.app?utm_source=farcaster&utm_medium=organic&utm_campaign=launch_korean
```

---

### Farcaster 포스팅 팁

1. **이미지 첨부 필수** — 카드 이미지가 있으면 타임라인에서 눈에 띔
2. **채널 선택** — Warpcast 앱에서 캐스트 작성 시 하단 채널 아이콘 탭 → 채널 검색
3. **답글 적극 응대** — 누가 자기 결과 공유하면 즉시 반응
4. **리캐스트** — 다른 사람이 Eth·RPG 결과 올리면 리캐스트

---

---

## Part 2: Hacker News (Show HN)

### 최적 타이밍

| KST | 비고 |
|-----|------|
| **2/26 (목) 02:00** (추천) | HN 골든타임 (PT 9AM-12PM)에 해당. PH 런칭 다음날 PT 아침 |

**추천: 2/26 (목) KST 02:00** — PT 09:00 피크타임과 정확히 겹침

---

### 제출 방법

1. https://news.ycombinator.com/submit 접속
2. Title 입력
3. URL 입력 (text와 URL 동시 입력 불가 — **URL 우선**)
4. 제출 후 자기 포스트에 첫 댓글로 상세 설명 작성

---

### Title (복사용)

```
Show HN: Eth·RPG – Your Ethereum wallet's on-chain history as RPG stats
```

### URL

```
https://ethrpg.app
```

---

### 첫 댓글 (제출 직후 자기 포스트에 게시)

```
vitalik.eth is a Lv.33 Hunter with Power 62,045. This analyzes any Ethereum wallet's on-chain history and generates RPG stats, a class, and AI-written fantasy lore.

It reads on-chain data via Alchemy SDK — transaction count, gas spent, DeFi swaps, NFT trades, bridge usage, unique contracts — and maps them to RPG stats using log-scale formulas.

Classification works by ratio analysis: if your NFT trade ratio is >= 25%, you're a Hunter. DEX swap ratio >= 20% makes you a Rogue. 8 classes total, evaluated in priority order (first match wins).

The AI lore part uses Claude to generate a fantasy backstory that references real crypto events (the Merge, DeFi Summer, NFT boom) matched to the wallet's active period.

Card images are server-rendered with next/og (Satori). No client-side canvas — the OG route returns a PNG that works as a link preview image.

Example stat formula:

  Level = clamp(1 + floor(10 * log10(1 + tx_count)), 1, 60)

Stack: Next.js, TypeScript, Alchemy SDK, Claude API, next/og, Tailwind. Deployed on Vercel.

No wallet connection or signing needed — completely read-only. Curious: if you could add a 9th class, what on-chain behavior would define it?
```

---

### HN 필수 규칙

1. **Show HN 접두어 필수** — 제목이 "Show HN:" 으로 시작해야 함
2. **제품이 실제로 작동해야 함** — 바로 써볼 수 있어야 함
3. **광고 톤 금지** — "amazing", "revolutionary" 같은 표현 X. 팩트 기반
4. **1인칭 톤** — "I built", "My side project" 식으로 자연스럽게
5. **기술 디테일 강조** — HN 유저는 어떻게 만들었는지에 관심이 큼
6. **댓글 즉시 응답** — HN에서 댓글은 업보트보다 강력한 랭킹 시그널
7. **URL과 text 동시 입력 불가** — URL을 넣으면 text 필드 무시됨. 상세 설명은 첫 댓글로

---

### HN 댓글 대응 템플릿

**"How is this different from DegenScore?"**
```
DegenScore focuses on a single reputation score. Eth·RPG classifies wallets into 8 RPG archetypes with full stat breakdowns and AI-generated lore. It's more about fun/identity than a credit score.
```

**"What about privacy?"**
```
Everything is read-only — we query the same public blockchain data you can see on Etherscan. No wallet connection, no signing, no personal data stored beyond the wallet address for caching (24h TTL).
```

**"Why log-scale for stats?"**
```
Linear scaling doesn't work for on-chain metrics — whale wallets would max out every stat. Log scale compresses the range so a 10-tx wallet and a 10,000-tx wallet both get meaningful, differentiable stats.
```

**"Is the AI lore just GPT wrapper?"**
```
It uses Claude with a structured prompt that includes the wallet's class, stats, active period, and matched crypto events. The prompt instructs it to write in a specific dark fantasy tone. There's also a fallback template system if the API call fails.
```

---

## 통합 타임라인

| 날짜 | KST | 플랫폼 | 작업 |
|------|-----|--------|------|
| 2/25 (수) | 17:00 | PH | 런칭 시작 + Maker comment |
| 2/25 (수) | 17:30 | Farcaster | /ethereum 메인 캐스트 |
| 2/25 (수) | 18:00 | Twitter | @EthRPGapp 고정 트윗 + 카드 이미지 |
| 2/25 (수) | 18:00 | Reddit | r/ethereum 포스트 (카르마 10+ 필요 — 미달 시 스킵) |
| 2/25 (수) | 20:00 | Twitter | 태그 포스트 #1 — vitalik.eth |
| 2/26 (목) | 02:00 | HN | Show HN 제출 + 첫 댓글 |
| 2/26 (목) | 10:00 | 전체 | 퍼널 데이터 첫 체크 |
| 2/26 (목) | 12:00 | Twitter | 태그 포스트 #2 — stani.eth |
| 2/26 (목) | 14:00 | Farcaster | /defi 캐스트 |
| 2/26 (목) | 15:00 | Farcaster | /nft 캐스트 |
| 2/26 (목) | 16:00 | Farcaster | /base 캐스트 |
| 2/26 (목) | 18:00 | Twitter | 태그 포스트 #3 — pranksy.eth |
| 2/27 (금) | 02:00~06:00 | HN | 댓글 모니터링 |
| 2/27 (금) | 10:00 | Farcaster | /korean 캐스트 |
