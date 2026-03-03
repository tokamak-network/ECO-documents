# Indie Hackers Post — Week 1 Follow-up (2026-03-03)

> **URL**: https://www.indiehackers.com (Community > New Post)
> **카테고리**: Building in Public
> **상태**: Day 5 데이터 기반 후속 포스트. 첫 포스트의 building-in-public 톤 유지.

---

## Title

Week 1 data from my ETH wallet RPG: 56 visitors, 6 card generations, and the one UX change that actually worked

---

## Body

Last week I posted about launching my Ethereum wallet RPG generator to crickets. A few of you left great comments (the "on-chain personality test" suggestion was especially sharp — more on that later). Here's what happened since.

**Quick recap:** Paste any ETH address, get an RPG character card with class, stats, AI lore, and Combat Power. Battle other wallets in PvP. No wallet connect needed. https://ethrpg.app

### The numbers after 5 days (still small, still honest)

- **~56 external visitors** total
- **6 fresh card generations** (real users generating new cards, not cached)
- **6 battles** fought
- **2-3 returning users** who came back multiple times
- **1 organic share** (Twitter)
- **$0 revenue** (still free)

Not viral. But the conversion funnel told a clear story.

### Indie Hackers became my only working channel

Here's the traffic source breakdown after 5 days:

- **Indie Hackers: 20 referrals** — started at 0 on Day 1, grew to 5-10/day by Day 4-5
- **Product Hunt: 23 referrals** — all in the first 2 days, then completely dead
- **Everything else: ~13** — direct visits, Dev.to (SEO), a few Twitter clicks

Product Hunt gave me a spike and died. HN shadow-banned me. Reddit and Farcaster blocked me. **IH was the only channel that grew over time instead of decaying.** And it grew because of conversation — every comment reply, every engagement kept the post visible.

The lesson: on platforms where algorithms decide visibility, new accounts are invisible. On platforms where conversation decides visibility, you can earn your way in.

### The one UX change that moved the needle

My original landing page had a text input: "Paste your wallet address." That's asking a cold visitor to go find a 42-character hex string. Conversion was ~10%.

After Day 1, I added **clickable wallet chips** — vitalik.eth, stani.eth, griff.eth, etc. One tap to see a real character card instantly.

The results were immediate. Starting Day 4, I saw a new event type for the first time: `famous_wallet_click`. Every single IH visitor who generated a card did it by clicking a chip, not by typing an address.

The typical session looked like this:

1. Land from IH post (0 sec)
2. Click "Vitalik Buterin" chip (12 sec)
3. See Hunter card, Power 61,865 (15 sec)
4. Click back, try "Griff Green" chip (48 sec)
5. See Merchant card, Power 70,775 (50 sec)
6. Leave

**Total time to first value: 12 seconds.** Before the chips, it was infinite for most visitors — they just bounced.

The bad news? Zero users typed their own address. They browsed famous wallets like a gallery and left. The chips removed friction for trying the product, but didn't bridge to personal investment.

### What the funnel actually looks like

```
Landing page visitors:  56
  |
  v
Famous wallet click:     4  (7% of visitors clicked a chip)
  |
  v
Card generated:          6  (all from chips or direct links)
  |
  v
Battle started:          6  (surprisingly high conversion from card to battle)
  |
  v
Shared result:           1  (the viral loop barely fires)
  |
  v
Typed own address:       0  (the missing step)
```

The funnel has two holes:
1. **Landing → first click** (93% bounce). Most visitors read and leave without trying.
2. **Browse famous wallets → type own address** (0% conversion). Nobody makes the jump from spectating to participating.

The card-to-battle conversion is actually strong (~100% for engaged users). The problem is entirely top-of-funnel.

### What I'm trying next

Based on the data and a comment from @Rachealbuildgrowth here on IH (who suggested framing this as an "on-chain personality test"), I'm exploring:

1. **Reframing the headline** — "What Kind of Hero Is Your Wallet?" feels like a tool. "What's Your On-Chain Class?" feels like a personality quiz. Personality quizzes have natural share motivation ("I got Hunter, what did you get?")

2. **Flipping the battle CTA** — When you view a famous wallet's card, the battle button now says "Battle vitalik.eth with YOUR wallet" instead of a generic "Start Battle." This forces you to think about your own address in context.

3. **Reducing input friction** — The 42-character address is the biggest barrier. Exploring ways to make the "try your own" step feel as easy as clicking a chip.

### The micro-retention signal

One thing that surprised me: I have 2-3 users who keep coming back. One person visited 3 times in 90 minutes. Another returned the next day at the same time. With 56 total visitors, having repeat users at all feels meaningful.

The ranking system seems to create the return trigger — your position changes as other people battle, so there's a reason to check back.

### Fun discoveries from the data

- **griff.eth** (Giveth founder) has the highest Combat Power I've seen: **Merchant Lv.38, 70,775 Power**. He edges out pranksy.eth (70,140) by 635 points.
- **stani.eth** (Aave founder) is a **Priest** — makes sense, the class triggers on high gas spend + heavy contract interactions.
- The rarest class in the wild is **Summoner** — you need heavy bridge usage, which most wallets don't have.

### Honest takeaway after week 1

The product works. People who try it engage deeply. But "try it" requires too much commitment from a cold visitor, and I haven't solved that yet.

If you have ideas on bridging the gap between "browse someone else's card" and "make your own," I'd love to hear them. That's the conversion problem I'm stuck on.

---

**Try it:** https://ethrpg.app — click any famous wallet chip to see a card instantly, or paste your own address if you're feeling brave.

---

## 게시 가이드

### 핵심 전략
- 첫 포스트 대비 **데이터 중심**으로 차별화
- 퍼널 분석 + UX 개선 스토리 = IH 빌딩인퍼블릭 핵심 콘텐츠
- Rachealbuildgrowth 태그로 커뮤니티 연결감 유지
- 마지막에 질문으로 끝나서 댓글 유도

### 태그
- `building-in-public`
- `growth`

### 게시 시간
- **한국시간 02:00-04:00** (미국 PT 오전 9-11시)
- 또는 한국시간 낮에 게시해도 OK

### 게시 후 행동
1. 첫 번째 포스트에 "Week 1 update posted" 댓글 추가 + 링크
2. 다른 빌딩인퍼블릭 포스트에 진심 댓글 2-3개
3. 댓글에 빠른 응답
