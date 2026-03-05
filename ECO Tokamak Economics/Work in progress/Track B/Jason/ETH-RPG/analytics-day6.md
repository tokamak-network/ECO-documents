# ETH-RPG Analytics — Day 6 Report

**Date**: 2026-03-05 (Thu)
**Data source**: `/api/admin/metrics` production snapshot
**Period**: 2026-02-28 ~ 2026-03-05 (launch +6 days)

---

## 1. Core Counters (Cumulative)

| Metric | Count | Note |
|--------|------:|------|
| Landing page visits | 182 | `funnel_landing` counter |
| Input focus | 8 | 4.4% of landing |
| Generate start | 16 | 8.8% of landing |
| Generate success | 15 | 93.8% of starts |
| Share | 1 | 0.5% of landing, 4.2% of generates |
| OG image load | 9 | External previews (link unfurls) |
| Battles | 12 | 0 cached |
| Errors (empty wallet) | 1 | |

### Card Generation Breakdown
- **Total**: 24 (fresh 11, cached 13)
- Cache hit rate: 54% — 절반 이상이 이전에 생성된 지갑 재방문

---

## 2. Funnel Analysis

```
Landing (182) ──► Input Focus (8) ──► Generate Start (16) ──► Generate Success (15) ──► Share (1)
         4.4%                                8.8%                   93.8%                 6.7%
```

### Key Drop-offs
1. **Landing → Input Focus (4.4%)**: 대부분의 방문자가 주소 입력에 도달하지 않음
   - 하지만 `generate_start`(16)이 `input_focus`(8)보다 큼 → gallery card 클릭이 주요 전환 경로
2. **Generate → Share (6.7%)**: 카드를 만든 사람 중 1명만 공유 — 바이럴 루프 끊김

### 실제 전환 경로
- **갤러리 카드 클릭 → 결과 페이지**: 주요 전환 경로 (Vitalik, Stani, Griff 클릭 확인)
- **직접 주소 입력**: 거의 없음 (input_focus 8건 중 실제 생성은 일부)
- **퀴즈**: quiz_start 1건, 사실상 미사용

---

## 3. Class Distribution (Unique Wallets)

| Class | Count |
|-------|------:|
| Hunter | 2 |
| Priest | 2 |
| Elder Wizard | 1 |
| Merchant | 1 |
| Warrior | 1 |
| **Total unique** | **7** |

- 24 generates 중 7 unique address — 나머지 17은 캐시 히트(재방문) 또는 갤러리 지갑
- Hunter 우세 (MEMORY.md 예측과 일치: NFT ratio 25% 조건이 먼저 매칭)

---

## 4. Traffic Sources (Referrer)

| Source | Page Views | % |
|--------|----------:|---|
| Direct / Unknown | 40 | 75.5% |
| IndieHackers Post | 9 | 17.0% |
| IndieHackers Homepage | 3 | 5.7% |
| Internal (ranking → landing) | 1 | 1.9% |
| **Total (in ring buffer)** | **53** | 100% |

### IndieHackers Referrer URLs
- Post: `indiehackers.com/post/i-built-an-rpg-character-generator-for-ethereum-wallets-in-7-days-heres-what-happened-when-i-launched-cc4a698ab3`
- Product: `indiehackers.com/product/eth-rpg`
- Homepage: `indiehackers.com/`

### Note
- Ring buffer는 최근 100 events만 보유 → 초기 트래픽 로그는 이미 밀려남
- `funnel_landing` 카운터(182)와 ring buffer page_views(53)의 차이 = 초기 이벤트 유실
- "Direct / Unknown"에는 북마크, 주소창 직접 입력, referrer를 보내지 않는 앱(일부 Twitter 클라이언트 등) 포함

---

## 5. Daily Activity (Ring Buffer)

| Date | Page Views | Notable |
|------|----------:|---------|
| 2/28 (Sat) | 5 | Launch day — IH post live |
| 3/1 (Sun) | 13 | IH 트래픽 피크 |
| 3/2 (Mon) | 8 | 감소 시작 |
| 3/3 (Tue) | 13 | 소폭 반등 |
| 3/4 (Wed) | 12 | griff.eth 생성 1건, quiz_start 1건 |
| 3/5 (Thu) | 2 | 00:34 UTC가 마지막 (IH product 페이지 유입) |

### Hourly Activity (from hourlyActivity counter)
- 3/2 01:00 UTC — 2건 (마지막 hourly 활동)
- 3/4 16:00 UTC — 1건 (griff.eth generate)
- 나머지 72시간 전부 0 — **사실상 트래픽 고갈 상태**

---

## 6. User Journey Reconstruction

### Journey A: IH Post → Gallery Click → Card (가장 흔한 패턴)
```
IH post 클릭 → 랜딩 → gallery_view → famous_wallet_click (Vitalik) → result page → card_generated
```
- 3건 확인: Vitalik (2/28, 3/1), Stani (3/1), Griff (2/28, 3/4)

### Journey B: IH Post → 랜딩만 보고 이탈
```
IH post 클릭 → page_view (landing) → 이탈
```
- 대다수 패턴 — gallery까지는 보지만 클릭하지 않음

### Journey C: Direct → 반복 방문
```
Direct 방문 → page_view → 이탈 (or ranking 확인)
```
- referrer 없이 반복 방문하는 유저 존재 (본인 또는 북마크 사용자)

---

## 7. Key Insights

### 잘 되고 있는 것
1. **Generate 성공률 93.8%** — API 안정성 좋음 (15/16)
2. **Gallery card가 주 전환 경로** — famous wallet이 CTA 역할을 훌륭히 수행
3. **IH에서 유의미한 클릭스루** — 포스트가 실제 전환을 만들어냄

### 문제점
1. **공유율 4.2%** (1/24) — 바이럴 루프 완전히 끊김
2. **퀴즈 진입 1건** — 퀴즈 CTA가 사실상 보이지 않거나 매력 없음
3. **IH 트래픽 소진** — 3/2 이후 거의 0, 새 소스 필요
4. **Input focus vs generate gap** — 직접 입력은 거의 안 함, gallery 의존도 높음
5. **Hourly activity 거의 0** — ring buffer 이벤트와 hourly counter 간 불일치 (ring buffer에는 이벤트가 있지만 hourly counter는 generate만 카운트)

### 다음 액션
1. **공유 루프 개선** (최우선) — 24명이 카드 만들고 1명만 공유. 공유 UX 강화 필요
2. **새 트래픽 소스** — Dev.to 기술글 + Twitter 스레드 + Web3 Discord
3. **퀴즈 CTA 개선** — 현재 사실상 dead feature, 랜딩에서 더 눈에 띄게
4. **gallery 확장** — 전환 경로가 gallery 클릭이므로, 더 다양한 유명 지갑 추가

---

## 8. Raw Data Reference

### Counters (full)
```json
{
  "generate_total": 24, "generate_cached": 13, "generate_fresh": 11,
  "battle_total": 12, "battle_cached": 0,
  "share_twitter": 1, "share_farcaster": 0, "share_clipboard": 0,
  "error_api": 0, "error_rate_limit": 0, "error_invalid_address": 0,
  "error_no_transactions": 0, "error_empty_wallet": 1,
  "funnel_landing": 182, "funnel_input_focus": 8, "funnel_generate_start": 16,
  "funnel_generate_success": 15, "funnel_share": 1, "og_image_load": 9
}
```

### Class Distribution (full)
```json
{ "elder_wizard": 1, "hunter": 2, "merchant": 1, "priest": 2, "warrior": 1 }
```

### Generated Cards (from events)
| Wallet | Class | Level | Power | Date (UTC) |
|--------|-------|------:|------:|------------|
| vitalik.eth | Hunter | 33 | 61,865 | 2/28 18:14 |
| griff.eth | Merchant | 38 | 70,775 | 2/28 18:14 |
| stani.eth | Priest | 32 | 62,005 | 3/1 15:29 |
| griff.eth | Merchant | 38 | 70,775 | 3/4 16:48 |
