# Indie Hackers Post — Updated (2026-02-27)

> **URL**: https://www.indiehackers.com (게시: Products > New Post 또는 Community 포스트)
> **카테고리**: Show IH / Building in Public
> **상태**: Day 1 포스트 대비 2일 누적 데이터 + 제품 개선사항 반영

---

## Title

I launched an RPG character generator for Ethereum wallets to crickets — here's what 48 hours of real data taught me

---

## Body

I had a simple idea: what if your Ethereum wallet was an RPG character?

Paste any ETH address, and in 10 seconds you get a full character card — class, stats, AI-generated lore, and a Combat Power score. You can even battle other wallets in turn-based PvP and compete on a global leaderboard. No wallet connect, no signing, completely read-only.

**Try it:** https://ethrpg.app

### What it does

The app reads your on-chain transaction history and maps it to RPG mechanics:

- **8 classes** based on behavior patterns (NFT collectors become Hunters, DEX traders become Rogues, diamond hands become Guardians, etc.)
- **7 stats** calculated from real data using log-scale normalization (so both 10-tx wallets and 50,000-tx whales get meaningful scores)
- **PvP battles** — pit any two wallets against each other in deterministic turn-based combat
- **Global ranking** — leaderboards by Combat Power, battle record, and explorer score
- **AI lore** that references actual crypto events (The Merge becomes "The Great Convergence," DeFi Summer becomes "The Alchemy Renaissance")
- **Shareable card image** rendered server-side — optimized for social feeds

### The 7-day build

- **Day 1-2:** Blockchain data pipeline + transaction classifier + stat formulas
- **Day 3:** AI lore generation (with 4-step fallback) + card image renderer
- **Day 4:** Frontend (landing, result page, share flow)
- **Day 5:** PvP battle system + global ranking
- **Day 6:** Polish, error handling, deploy to Vercel
- **Day 7:** Launch day

Solo dev. Tech stack: Next.js, TypeScript, Alchemy SDK (on-chain data), Claude API (lore), @vercel/og (image rendering), Vercel hosting.

### 48-hour launch results (honest numbers)

After 2 days:

- **30-34 external visitors** (not counting my own testing)
- **2 card generations** from real users (both on Day 1 — Day 2 had zero new ones)
- **2 users completed the full funnel** (card -> battle -> ranking)
- **2 return visitors** came back 24 hours later
- **1 organic Twitter share** by a user (first viral loop trigger)
- **$0 revenue** (it's free)

Not exactly a rocketship. But the details tell a more nuanced story.

### What I learned about launching with zero audience

I prepared a "multi-channel simultaneous launch" across 6 platforms. Here's what actually happened:

- **Product Hunt** — 6 upvotes, traffic halved by Day 2. New maker account = low algorithmic visibility.
- **Hacker News** — Shadow banned. New account + low karma = auto-filtered.
- **Farcaster** — 0 engagement. No Power Badge = can't post in channels.
- **Reddit** — Couldn't post. Subreddit karma requirement not met.
- **Twitter** — 3 clicks total, but 1 organic user share. 0 followers = shouting into void.
- **Dev.to** — 14 views. Only channel with zero barrier.
- **Indie Hackers** — 4 visitors, 0 conversions. Product page live, community post up.

**4 out of 7 channels were effectively blocked.** Every major platform has invisible gatekeeping for new accounts. I didn't know this going in.

### The good news buried in the data

**The product works. Distribution doesn't.**

Here's what the small sample actually showed:

1. **Users who find it go deep.** The one HN user who saw my post before it got killed? They hit an error (empty wallet), tried a different address, generated a card, fought a battle, and checked the ranking. Full funnel in 2 minutes.

2. **Retention is real.** Two Day 1 users came back 24 hours later — same time of day, same behavior. The ranking system creates a reason to return.

3. **First organic share on Day 2.** An IH visitor ran 3 battles in a row, then shared the result on Twitter. The viral loop triggered for the first time — even if it didn't cascade yet.

4. **Card-to-battle conversion is high (~60%).** Once someone has a card, they want to fight. The RPG hook works.

**The bottleneck is the top of funnel.** 30+ people visited the landing page. Only 2-3 actually typed in a wallet address. That's a ~15% conversion rate on the first step. The rest of the funnel is fine — the problem is getting people to try it.

### What I changed after Day 1

Based on the data, I redesigned the landing page:

- Added **clickable wallet chips** (vitalik.eth, stani.eth, etc.) so visitors can try instantly without typing
- Improved the empty wallet error to suggest famous addresses instead of a dead end
- Stripped redundant CTAs — one clear action, not three

The original landing page asked users to paste an Ethereum address. That's a huge ask for a cold visitor. The chips reduced friction to a single click.

### If I did it again

1. **Build platform presence 4+ weeks before launch** — karma, followers, badges. Every major platform gates new accounts.
2. **Personal network first, platforms second** — DMs convert 10x better than cold posts. I should have started here.
3. **Zero-barrier channels only on Day 1** — Dev.to and Indie Hackers are the only places where a new account can post immediately.
4. **Ship the "try it instantly" UX before launch** — asking cold visitors to paste a wallet address is too much friction. Should have had the clickable demo wallets from Day 0.

### The fun part

I tested ~60 known wallets. Some results:

- **vitalik.eth** — Hunter, 62,065 Power. Ethereum founder — hunts relics across chains.
- **stani.eth** — Priest, 62,005 Power. Aave founder — channels sacred protocol mana.
- **pranksy.eth** — Hunter, 70,140 Power. NFT legend — highest power score yet.
- **sassal.eth** — Summoner, 57,995 Power. ETH educator — bridges between realms.

All 8 classes appeared in the wild. The rarest? Summoner — heavy bridge users are a tiny minority.

### What's next

- Building karma on HN and Reddit for a relaunch attempt
- Daily Twitter posts tagging crypto figures with their character cards
- Direct outreach to crypto/dev friends (should have started here on Day 0)
- Considering open-sourcing the classification engine as a standalone library
- Watching if the landing page redesign moves the 15% conversion needle

---

**Would love to hear:**
- Has anyone else launched to crickets and turned it around? What was the inflection point?
- What's your experience with platform gatekeeping as a new account?

https://ethrpg.app — paste any ETH address (or click a famous wallet), see what hero you are.

---

## 게시 가이드

### 게시 위치
- **Option A**: Products > 기존 프로덕트 페이지에 마일스톤/업데이트 포스트
- **Option B**: Community > 새 텍스트 포스트 (기존 포스트와 별개)
- **추천: Option B** — 새 포스트로 올리되, 기존 Day 1 포스트가 있으면 "Update" 느낌으로

### 태그 (해당되는 것 선택)
- `show-ih`
- `building-in-public`
- `launch`
- `web3`

### 포스트 시간
- **미국 시간 기준 오전 9-11시 (PT)** = **한국시간 02:00-04:00**
- 또는 **한국시간 낮에 게시**해도 괜찮음 (IH는 HN처럼 시간 민감하지 않음)

### 게시 후 행동
1. 포스트에 본인 댓글 1개 추가: "Happy to answer any technical questions! The stat formulas and battle system are probably the most interesting parts from an engineering perspective."
2. 다른 Show IH / 최근 런칭 포스트에 진심 어린 댓글 2-3개 남기기 (커뮤니티 참여 시그널)
3. 답글에 신속 응답 (IH는 대화형 커뮤니티)
