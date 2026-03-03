# Day 4 Analytics Report (2026-03-01)

---

## 1. 요약

| 지표 | Day 3 | Day 4 | 변화 |
|------|-------|-------|------|
| Landing page_view | ~8건 | 10건 | +25% |
| IH 유입 | 1건 | **8건** | **+700%** |
| PH 유입 | 1건 | 0건 | 소진 |
| Fresh generation | 1건 | **2건** | 2일 연속 0 후 복구 |
| famous_wallet_click | 0건 | **2건** | **첫 관측** |
| 배틀 | 0건 | 0건 | — |
| 공유 | 0건 | 0건 | — |

**한 줄 결론:** IH 포스트가 주력 유입 채널로 부상. wallet chips를 통한 첫 전환 확인 — 랜딩 리디자인 효과 검증.

---

## 2. 트래픽 소스별 분석

### Indie Hackers — **주력 채널으로 전환**
- Day 2: 4건 → Day 3: 1건 → **Day 4: 8건**
- 포스트 직접 referrer: 7건
- IH 메인 referrer: 1건
- **첫 IH→카드 생성 전환 발생** (오전 3:13 세션)
- 업데이트 포스트 + 댓글 대화(proofrelay, launch date 질문)의 효과

### Product Hunt — **소진 완료**
- Day 1: 15 → Day 2: 7 → Day 3: 1 → **Day 4: 0**
- 채널 종료.

### Direct
- 4건 (오후 12:44, 2:34, 2:56, 2:59, 5:30)
- 본인 또는 북마크 방문자

---

## 3. 핵심 세션: IH → famous_wallet_click → 전환

```
03:13:50  landing (IH 포스트 referrer로 유입)
03:14:02  famous_wallet_click: Vitalik Buterin
03:14:03  result 페이지 (vitalik.eth)
03:14:06  generate: hunter, cached=false (FRESH)
03:14:06  card_generated: Hunter Lv.33, Power 61,865
03:14:51  landing 복귀
03:14:54  famous_wallet_click: Griff Green
03:14:56  generate: merchant, cached=false (FRESH)
03:14:57  card_generated: Merchant Lv.38, Power 70,775
03:15:15  landing 재방문 후 이탈
```

**인사이트:**
- IH 포스트에서 유입 → 약 12초 후 첫 famous_wallet_click
- vitalik.eth 카드 확인 후 48초 만에 두 번째 카드 (griff.eth) 생성
- **wallet chips가 전환을 만들었다.** `famous_wallet_click` 이벤트 첫 관측
- 자기 지갑 입력은 하지 않음 — 구경 모드이나 제품은 체험함
- 배틀까지는 진행하지 않고 이탈

---

## 4. 생성된 캐릭터

| 시간 | 주소 | 클래스 | 레벨 | 파워 | cached | 소스 |
|------|------|--------|------|------|--------|------|
| 오전 3:14:06 | vitalik.eth | Hunter | 33 | 61,865 | false | IH → famous_wallet_click |
| 오전 3:14:57 | griff.eth | Merchant | 38 | 70,775 | false | IH → famous_wallet_click |

**griff.eth가 Merchant Lv.38, Power 70,775** — 현재까지 두 번째로 높은 파워 (pranksy.eth 70,140 추월).

---

## 5. 시간대별 패턴

```
오전 3시     ████  피크: IH 유입 → 카드 생성 2건 (미국 동부 오후 1시)
오전 5시     ██░░  IH 유입 2건 (전환 없음)
오전 7시     █░░░  IH 메인 유입 1건
오후 12-1시  ██░░  IH 포스트 유입 1건 + direct 1건
오후 2-3시   ██░░  direct 3건 (전환 없음)
오후 5시     █░░░  direct 1건
```

오전 3시 피크 = 미국 시간대 오후. IH 커뮤니티가 미국 중심임을 확인.

---

## 6. 4일 누적 핵심 수치

| 지표 | Day 1 | Day 2 | Day 3 | Day 4 | 누적 |
|------|-------|-------|-------|-------|------|
| 외부 방문자 | ~17 | 13-17 | 5-7 | 6-8 | **41-49** |
| 신규 카드 (fresh) | 2 | 0 | 1 | **2** | **5** |
| IH 유입 | 0 | 4 | 1 | **8** | **13** |
| PH 유입 | 15 | 7 | 1 | 0 | **23** (소진) |
| 풀 퍼널 완료 | 1 | 1 | 0 | 0 | **2** |
| famous_wallet_click | — | — | — | **2** | **2** |
| 리텐션 유저 | 1 | 2 | 1 | 0 | 2명 |
| 공유 | 0 | 1 | 0 | 0 | **1** |

---

## 7. 핵심 인사이트

### 긍정
1. **IH가 PH를 대체하는 주력 채널로 부상** — Day 4 유입의 80%가 IH. 포스트 업데이트 + 댓글 대화 효과.
2. **famous_wallet_click 첫 관측** — wallet chips(랜딩 리디자인)가 전환 퍼널에서 핵심 역할. "주소 입력" 허들 제거 효과 확인.
3. **2일 연속 0이던 카드 생성 복구** — IH 유입 → wallet chips → 카드 생성 파이프라인 작동.
4. **griff.eth Power 70,775** — 현재 최고 파워. 콘텐츠 소재로 활용 가능.

### 과제
5. **자기 지갑 입력 여전히 0건** — famous wallet 구경만 하고 이탈. 자기 주소 입력 유도 필요.
6. **배틀 진입 0건** — 카드 생성 후 배틀로 넘어가는 CTA가 약함.
7. **절대 트래픽 여전히 낮음** — 6-8명/일. IH 외 추가 채널 필요.

---

## 8. 다음 액션

### P0
| 액션 | 기대 효과 |
|------|-----------|
| IH 포스트 활동 유지 (새 댓글 응답, 다른 포스트 댓글) | IH 유입 유지/확대 |
| griff.eth Merchant 카드 Twitter 태그 포스트 | Power 70,775 최고 기록 소재 |

### P1
| 액션 | 기대 효과 |
|------|-----------|
| 카드→배틀 CTA 개선 (결과 페이지에서 배틀 유도 강화) | 배틀 전환율 개선 |
| "Try YOUR wallet" CTA를 wallet chips 바로 아래 배치 | famous wallet 구경 후 자기 지갑 입력 유도 |
