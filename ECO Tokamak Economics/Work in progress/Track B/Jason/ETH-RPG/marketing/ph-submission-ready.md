# Product Hunt 제출 가이드 — 복사/붙여넣기 Ready

> 제출 시점: 2026-02-25 (수) 오전 — 즉시 등록
> 런칭 시점: 2026-02-25 (수) 17:00 KST
> 제출 URL: https://www.producthunt.com/posts/new

---

## Step 1: 기본 정보 입력

### Product URL
```
https://ethrpg.app
```

### Name
```
Eth·RPG
```

### Tagline (60자 이내)
```
Paste any ETH address, get your RPG hero card in 10 seconds
```
(57자 — OK)

### Topics / Categories
```
Web3, Gaming, Artificial Intelligence
```

---

## Step 2: Description (복사용)

```
Eth·RPG analyzes your on-chain Ethereum activity and generates a unique RPG character card.

What you get:
- Class assignment from 8 archetypes (Hunter, Rogue, Wizard, Guardian, Summoner, Merchant, Priest, Warrior)
- 7 stats calculated from real transaction data (Level, HP, MP, STR, INT, DEX, LUCK)
- AI-generated hero lore based on your wallet's history
- Combat Power score for bragging rights
- Beautiful dark fantasy card you can download and share
- PvP Battle mode — pit any two wallets against each other

No wallet connect. No signing. Completely read-only and safe.

Built with Next.js, Alchemy SDK, Claude AI, and Satori (next/og).
```

---

## Step 3: Screenshots (5장)

업로드 순서 (이 순서가 PH 갤러리에 표시됨):

| # | 파일 | 설명 | PH 라벨 |
|---|------|------|---------|
| 1 | `screenshots/1-landing.png` | 랜딩 페이지 (주소 입력) | Landing page |
| 2 | `screenshots/2-loading.png` | 로딩 화면 (픽셀아트 애니메이션) | Loading animation |
| 3 | `screenshots/3-card-front.png` | 캐릭터 카드 앞면 (스탯) | Character card — Stats |
| 4 | `screenshots/4-card-back.png` | 캐릭터 카드 뒷면 (AI 서사) | Character card — AI Lore |
| 5 | `screenshots/5-share-flow.png` | 공유 플로우 | Share & download |

**추가 옵션**: 카드 이미지 (`screenshots/cards/vitalik.png`)를 6번째로 추가하면 다양성이 높아짐.

---

## Step 4: Thumbnail / Logo

PH 썸네일은 240x240 정사각형. 옵션:
- `public/favicon.ico` 기반 — 검 아이콘
- 또는 ETH·RPG 로고 텍스트 + 다크 배경

---

## Step 5: Maker Comment (첫 댓글 — 런칭 직후 즉시 게시)

```
Hey everyone! I built Eth·RPG because I wanted to answer a fun question: if your Ethereum wallet were an RPG character, what would it be?

The app analyzes real on-chain data — your transaction history, DeFi swaps, NFT trades, bridge usage, gas spent — and maps it to RPG stats and one of 8 character classes.

The AI lore is my favorite part. It weaves actual crypto events (the Merge, NFT Summer, DeFi Summer) into your character's backstory. Every wallet gets a unique story.

Some fun results so far:
- vitalik.eth → Lv.33 Hunter, Power 62,045
- stani.eth (Aave founder) → Lv.32 Priest, Power 62,005
- pranksy.eth (NFT legend) → Lv.49 Hunter, Power 70,140

There's also a Battle Mode where you can pit any two wallets against each other in a turn-based RPG fight.

Tech stack: Next.js, TypeScript, Alchemy SDK for on-chain data, Claude API for lore generation, next/og (Satori) for server-rendered card images. Everything runs server-side — no wallet connection needed.

Would love to hear what class you get! Drop your result below.
```

---

## Step 6: 예약 설정

- **Schedule launch**: 2026-02-25 (Wed)
- **Launch time**: KST 17:00 (PT 00:01)
- 화~목 런칭이 가장 성과 좋음 (PH 가이드 기준)

---

## Step 7: 런칭일 체크리스트

### 런칭 전 (2/25 수 오전)
- [ ] PH 프로필 점검 — 사진, 바이오, 웹사이트 링크 설정
- [ ] PH에서 "New Product" → 위 정보 입력 → 2/25 런칭 등록
- [ ] 스크린샷 5장 업로드
- [ ] Description + Tagline 입력
- [ ] Maker comment 미리 작성 (런칭 즉시 게시)

### 런칭일 (2/25 수)
| KST | 작업 |
|-----|------|
| 17:00 | PH 런칭 시작 — Maker comment 즉시 게시 |
| 17:10 | PH 페이지 정상 동작 확인 |
| 17:30 | 지인/서포터에게 PH 링크 공유 (업보트 요청 X, "확인해봐" 톤) |
| 18:00 | Farcaster /ethereum 캐스트 (PH 링크 포함) |
| 22:00 | PH 댓글 모니터링 + 응답 |

### 런칭 다음날 (2/26 목)
- [ ] PH 순위 확인
- [ ] 댓글 전부 응답
- [ ] 추가 Farcaster 채널 포스팅

---

## 주의사항 (PH 규칙)

1. **업보트 직접 요청 금지** — "upvote please" 대신 "check it out, would love your feedback" 톤
2. **봇/가짜 투표 금지** — 감지 시 랭킹에서 제외됨
3. **제품이 작동해야 함** — 제출 전 ethrpg.app 정상 동작 최종 확인
4. PH Featured 기준 4가지: **Useful, Novel, High Craft, Creative** — Eth·RPG는 Novel + Creative에서 강점

---

## 빠른 링크

- PH 제출: https://www.producthunt.com/posts/new
- PH 런칭 가이드: https://www.producthunt.com/launch
- PH 프로필 설정: https://www.producthunt.com/my/settings
- ethrpg.app 프로덕션: https://ethrpg.app
