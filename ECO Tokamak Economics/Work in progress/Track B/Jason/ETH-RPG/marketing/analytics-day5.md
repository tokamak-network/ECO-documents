# Day 5 Analytics Report (2026-03-02)

---

## 1. 요약

| 지표 | Day 4 | Day 5 | 변화 |
|------|-------|-------|------|
| Landing page_view | ~10건 | ~12건 | +20% |
| IH 유입 | 10건 | 5건 | 안정 (포스트 4 + 메인 1) |
| Fresh generation | 2건 | 1건 | stani.eth (Priest) |
| famous_wallet_click | 3건 | 1건 (Stani Kulechov) | 패턴 지속 |
| 배틀 | 0건 | **2건** | **Day 3 이후 첫 배틀** |
| 공유 | 0건 | 0건 | — |
| PH 유입 | 0건 | 0건 | 소진 |

**한 줄 결론:** IH가 안정 유입 채널로 정착 (5일 누적 18건). 며칠 만에 배틀 재개(2건). famous_wallet_click → 카드 생성 패턴이 매일 반복 중.

---

## 2. 트래픽 소스별 분석

### Indie Hackers — 안정 채널
- Day 2: 4건 → Day 3: 1건 → Day 4: 10건 → **Day 5: 5건**
- 포스트 직접 referrer: 4건 (오전 12:21, 6:02 ×2, 오후 — 이전 분석 포함)
- IH 메인 referrer: 1건 (오전 1:18)
- **전환 발생**: stani.eth famous_wallet_click → Priest 카드 생성 (fresh)

### Direct
- 7건 (오전 2:14, 8:13, 11:04, 11:42, 11:43, 오후 12:25, 2:55)
- 일부 본인, 일부 북마크/직접 입력

### Product Hunt / 기타
- 0건. PH 완전 소진 (Day 4부터 0).

---

## 3. 핵심 세션

### 세션 1: IH → vitalik.eth → 재방문 (오전 12:21~1:53)

```
00:21:03  landing (IH 포스트 referrer)
00:21:41  famous_wallet_click: Vitalik Buterin
00:21:43  card_generated: Hunter Lv.33, 61,865P (cached)
01:18:05  landing (IH 메인 referrer) — 57분 후 재방문
01:53:14  generate: hunter cached=true — 35분 후 또 재방문
```

**인사이트:** IH에서 유입 후 약 90분간 3번 재방문. 리텐션 신호.

### 세션 2: IH → stani.eth → 카드 생성 (오전 6:02)

```
06:02:43  landing (IH 포스트 referrer)
06:02:56  famous_wallet_click: Stani Kulechov
06:02:59  card_generated: Priest Lv.32, 62,005P (fresh!)
```

**인사이트:** Day 4와 동일한 패턴 반복 — IH 유입 → famous wallet chip 클릭 → 카드 생성. 13초 만에 전환.

### 세션 3: 배틀 2건 (오전 10:08~10:09)

```
10:08:03  battle (cached=false)
10:09:05  battle (cached=false)
```

**인사이트:**
- Day 3-4 동안 배틀 0건이었는데 재개
- 약 1분 간격으로 2건 — 같은 유저가 연속 배틀한 것으로 추정
- referrer/주소 정보 없어 출처 불명
- 가능성 1: 오전 6시 stani.eth 유저가 4시간 후 재방문하여 배틀
- 가능성 2: direct 방문자 중 배틀 진행

---

## 4. 생성된 캐릭터

| 시간 | 주소 | 클래스 | 레벨 | 파워 | cached | 소스 |
|------|------|--------|------|------|--------|------|
| 오전 12:21 | vitalik.eth | Hunter | 33 | 61,865 | true | IH → famous_wallet_click |
| 오전 1:53 | (vitalik.eth) | Hunter | — | — | true | 재방문 재조회 |
| 오전 6:02 | stani.eth | Priest | 32 | 62,005 | **false** | IH → famous_wallet_click |

**Fresh generation: 1건** (stani.eth Priest).

---

## 5. 시간대별 패턴

```
오전 12시    ██░░  IH 유입 → vitalik.eth 카드 조회
오전 1시     █░░░  재방문 (IH 메인 + vitalik 재조회)
오전 2시     █░░░  direct 1건
오전 6시     ██░░  IH 유입 → stani.eth 카드 생성 (fresh)
오전 8시     █░░░  direct 1건
오전 10시    ██░░  배틀 2건!
오전 11시    ██░░  direct 2건
오후 12시    █░░░  direct 1건
오후 2시     █░░░  direct 1건
```

오전 12시, 6시 = 미국 시간대 오전~오후. IH 유입은 일관되게 미국 시간대.

---

## 6. 5일 누적 핵심 수치

| 지표 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | 누적 |
|------|-------|-------|-------|-------|-------|------|
| 외부 방문자 | ~17 | 13-17 | 5-7 | 6-8 | 5-7 | **46-56** |
| 신규 카드 (fresh) | 2 | 0 | 1 | 2 | 1 | **6** |
| IH 유입 | 0 | 4 | 1 | 10 | 5 | **20** |
| PH 유입 | 15 | 7 | 1 | 0 | 0 | **23** (소진) |
| famous_wallet_click | — | — | — | 3 | 1 | **4** |
| 배틀 | 2 | 2 | 0 | 0 | **2** | **6** |
| 풀 퍼널 완료 | 1 | 1 | 0 | 0 | ? | **2+** |
| 리텐션 (재방문) | 1 | 2 | 1 | 0 | 1 | 유저 2-3명 |
| 공유 | 0 | 1 | 0 | 0 | 0 | **1** |

---

## 7. 핵심 인사이트

### 긍정
1. **IH가 안정 유입 채널로 정착** — 5일간 20건 유입. Day 4-5에서 일관된 트래픽.
2. **famous_wallet_click → 카드 생성 패턴 확립** — Day 4: Vitalik+Griff, Day 5: Stani. wallet chips가 전환 퍼널의 핵심 진입점.
3. **배틀 재개** — Day 3-4 연속 0건 후 Day 5에서 2건. 배틀 기능이 여전히 작동.
4. **리텐션 신호** — 오전 12:21 유저가 90분간 3번 재방문. 제품에 재방문 동기 존재.

### 과제
5. **자기 지갑 입력 여전히 0건** — famous wallet 구경만. "구경 → 자기 것 만들기" 브릿지 필요.
6. **배틀과 카드 생성의 연결 약함** — 카드 생성 유저와 배틀 유저가 동일인인지 불명. 결과 페이지에서 배틀로의 CTA 개선 필요.
7. **절대 트래픽 정체** — 5-8명/일 수준에서 성장 없음. IH 외 추가 채널 필요.

---

## 8. 다음 액션

### P0
| 액션 | 기대 효과 | 상태 |
|------|-----------|------|
| Battle CTA `opponent` 전환 (A안) | 유명 지갑 카드에서 배틀 유도. "Battle vitalik.eth with YOUR wallet" | 검토 완료, 구현 대기 |
| IH 포스트 활동 유지 | IH 유입 유지 | 진행 중 (댓글 4건 답변 완료) |

### P1
| 액션 | 기대 효과 | 상태 |
|------|-----------|------|
| 랜딩 카피 "personality test" 실험 (spec 문서 A안) | Landing → Input 전환 개선 | spec 작성 완료 |
| HN karma 확보 계속 | 재런칭 준비 | 진행 중 |
| griff.eth Power 70,775 Twitter 태그 | 콘텐츠 + 도달 | 미실행 |

### 채널 상태 요약
| 채널 | 상태 | 5일 누적 |
|------|------|---------|
| IH | **주력 채널** | 20건 유입, 전환 3건+ |
| PH | 소진 | 23건 (Day 4부터 0) |
| HN | karma 확보 중 | shadow ban 해제 대기 |
| Twitter | 태그 포스트 간헐적 | 유입 미미 |
| Dev.to | SEO 잠복 | 댓글 대화 1건 |
| Farcaster | 차단 | Power Badge 없음 |
| Reddit | 차단 | karma 부족 |
