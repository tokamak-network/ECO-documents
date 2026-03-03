---
title: I Built a Tool That Turns Any Ethereum Wallet Into an RPG Character — Here's How
published: true
tags: ethereum, webdev, ai, opensource
cover_image: https://ethrpg.app/og-default.png
---

*Paste an address, get a hero card with stats, class, and AI-generated lore in 10 seconds.*

---

What if your Ethereum wallet had a character class? What if every swap, mint, and bridge you've ever done contributed to your RPG stats?

I built [Eth·RPG](https://ethrpg.app) to answer that question. It reads your on-chain history and generates a full RPG character card — class, stats, combat power, and an AI-written fantasy backstory.

No wallet connection. No signing. Completely read-only.

![Eth·RPG character card example](https://ethrpg.app/og-default.png)

## The Engineering Challenge

Take a dataset with wild variance — one user has 3 transactions, another has 50,000 — and turn it into a balanced, visually shareable result in under 10 seconds. It's like taking everyone's Spotify listening history and generating a D&D character sheet that feels *fair* for both casual listeners and power users.

The core challenges:
1. **Normalization** — how do you score data that spans 5+ orders of magnitude?
2. **Classification** — how do you categorize users without machine learning?
3. **Generation** — how do you make AI output feel personal, not generic?
4. **Rendering** — how do you produce shareable images with zero client-side processing?

## How It Works

### 1. Fetch On-Chain Data

I use the [Alchemy SDK](https://www.alchemy.com/sdk) to pull everything about a wallet:

- ETH balance
- Transaction count
- All asset transfers (ETH, ERC-20, ERC-721, ERC-1155)
- First/last transaction timestamps

Two transfer queries (sent + received) are combined to get the full picture. Max 1000 transfers per direction with pagination support.

### 2. Classify Transactions

Each transfer is classified against a protocol whitelist — ~40 contract addresses mapped to four categories:

- **DEX**: Uniswap V2/V3, SushiSwap, Curve, 1inch, CoW Protocol...
- **NFT**: Seaport, OpenSea, LooksRare, Blur
- **Bridge**: Optimism, Arbitrum, zkSync, Stargate, Hop, Base...
- **Stablecoin**: USDC, USDT, DAI, FRAX, GHO...

I chose hardcoded whitelisting over ABI decoding. It's faster, simpler, and covers 95%+ of real-world activity. One important edge case: utility NFTs (ENS domains, POAPs, Uniswap V3 LP positions) are excluded from the "collectible NFT" count to avoid misclassification.

The output is a set of ratios:

```
nftRatio = nftTransfers / totalTransfers
dexRatio = dexSwaps / totalTransfers
bridgeRatio = bridgeTransfers / totalTransfers
stableRatio = stableTransfers / totalTransfers
```

### 3. Determine Class (Priority Matching)

Eight classes, evaluated in order. First match wins:

| Priority | Class | Condition |
|----------|-------|-----------|
| 1 | Hunter | NFT ratio >= 25% AND nftRatio dominates |
| 2 | Rogue | DEX swap ratio >= 20% |
| 3 | Summoner | Bridge tx >= 8 or ratio >= 12% |
| 4 | Merchant | Stablecoin ratio >= 25% |
| 5 | Priest | Gas > 1.0 ETH AND contracts > 150 |
| 6 | Elder Wizard | 4+ year wallet, < 30 tx/year, < 10 ETH |
| 7 | Guardian | < 200 txs AND balance > 5 ETH |
| 8 | Warrior | Default fallback |

The implementation is an array of matcher functions. Adding a 9th class means inserting one function at the right priority position — no nested `if/else` chains.

```typescript
const CLASS_MATCHERS: ClassMatcher[] = [
  { classId: 'hunter',       match: (d) => d.nftRatio >= 0.25 && d.nftRatio > d.dexRatio },
  { classId: 'rogue',        match: (d) => d.dexRatio >= 0.20 },
  { classId: 'summoner',     match: (d) => d.bridgeCount >= 8 || d.bridgeRatio >= 0.12 },
  // ... first match wins
];

function determineClass(data: WalletMetrics): CharacterClassId {
  for (const { classId, match } of CLASS_MATCHERS) {
    if (match(data)) return classId;
  }
  return 'warrior'; // default
}
```

### 4. Calculate Stats (Log-Scale Normalization)

This is where it gets mathematically interesting.

On-chain data has an enormous range. Vitalik has mass transactions; a fresh wallet has 3. Linear scaling breaks immediately — whales would max out every stat while most wallets cluster near zero.

The solution: **logarithmic normalization**. Think of it like the Richter scale for earthquakes — a magnitude 6 is 10x stronger than a 5, not just "1 more." Same idea here: each order of magnitude in activity adds a fixed increment to the stat.

```typescript
function calcLevel(txCount: number): number {
  return clamp(1 + Math.floor(10 * Math.log10(1 + txCount)), 1, 60);
}

function calcHP(balanceEth: number): number {
  return Math.round(100 + 250 * Math.log10(1 + balanceEth));
}

function calcMP(gasSpentEth: number): number {
  return Math.round(80 + 220 * Math.log10(1 + gasSpentEth));
}

function calcSTR(dexSwaps: number, bridgeCount: number): number {
  return Math.round(50 + 180 * Math.log10(1 + dexSwaps + bridgeCount));
}
```

Why this works: `log₁₀(10) = 1`, `log₁₀(100) = 2`, `log₁₀(10000) = 4`. The function compresses large ranges into tight, meaningful intervals. A wallet with 10 transactions and one with 10,000 both get *differentiable, non-extreme* stats.

The stat mappings are intuitive:
- **ETH balance → HP** (wealth = health)
- **Gas spent → MP** (gas is your magical resource)
- **DEX/bridge activity → STR** (active trading = strength)
- **Unique contracts → INT** (diversity of interaction = intelligence)
- **Transaction frequency → DEX** (pace of activity = dexterity)

Combat Power combines everything with weighted coefficients plus a class bonus that compensates for classes with naturally lower raw stats.

### 5. Generate AI Lore

Each wallet gets a unique fantasy backstory. This was the trickiest part — how do you make AI output feel *personal* to a specific wallet, not just generic fantasy text?

The answer: **a structured prompt with a translation dictionary.** Real crypto events get mapped to RPG equivalents:

```typescript
const CRYPTO_EVENT_DICTIONARY = {
  'Luna/Terra Collapse':  'The Fall of the Lunar Kingdom',
  'The Merge':            'The Great Convergence',
  'NFT Summer 2021':      'The Season of Relic Fever',
  'DeFi Summer 2020':     'The Alchemy Renaissance',
  'FTX Collapse':         'The Merchant Guild Betrayal',
};

// The prompt includes the wallet's class, stats, active period,
// and which events overlap with their transaction history
const prompt = `
  You are writing lore for a ${className} (Level ${level}, Power ${power}).
  This hero was active during: ${matchedEvents.join(', ')}.
  Their primary activity: ${dominantBehavior}.
  Write a 3-5 sentence dark fantasy backstory in second person.
`;
```

The system has a **4-step fallback cascade** — because an AI-dependent feature can't be a single point of failure:

1. Primary LLM call (10s timeout with AbortController)
2. Fallback LLM model
3. Direct Anthropic API call
4. **Deterministic template fallback**

Step 4 is the interesting one. When all LLM calls fail, a hash function maps `classId-level-power-txCount` to a pre-written template:

```typescript
function deterministicHash(seed: string): number {
  let hash = 0;
  for (const char of seed) {
    hash = ((hash << 5) - hash) + char.charCodeAt(0);
  }
  return Math.abs(hash);
}

// Same wallet always gets the same fallback — no flickering on retry
const templateIndex = deterministicHash(`${classId}-${level}-${power}`) % templates.length;
```

All generated text passes through a sanitization layer: a forbidden word list catches financial terms or inappropriate language that might leak through the LLM.

### 6. Render the Card Image (Server-Side)

Card images are rendered with `@vercel/og` (Satori) — JSX components compiled to PNG on the server. No canvas, no ImageMagick, no Puppeteer.

```typescript
// This React component becomes a 1080x1350 PNG
return new ImageResponse(
  <div style={{ display: 'flex', flexDirection: 'column', ... }}>
    <ClassHeader class={character.class} level={character.level} />
    <StatBars stats={character.stats} />
    <PowerDisplay power={character.power} />
    <LoreText lore={character.lore} />
  </div>,
  { width: 1080, height: 1350 }
);
```

Two image formats:
- **Card**: 1080x1350 (mobile feed optimized, shareable)
- **OG**: 1200x630 (link preview on Twitter/Farcaster)

Both are CDN-cached for 24 hours. Error states render a visual error card rather than returning an HTTP error — better UX when images are embedded in feeds.

## Some Fun Results

I tested ~60 wallets. Some highlights:

| Wallet | Class | Level | Power |
|--------|-------|-------|-------|
| vitalik.eth | Hunter | 33 | 62,045 |
| stani.eth (Aave) | Priest | 32 | 62,005 |
| pranksy.eth | Hunter | 49 | 70,140 |
| jessepollak.eth (Base) | Hunter | 28 | 47,195 |
| ricmoo.eth (ethers.js) | Guardian | 19 | 45,150 |

All 8 classes are represented in the wild. Summoner is the rarest — heavy bridge users are a small subset.

## Tech Stack

- **Next.js 16** (App Router)
- **TypeScript** (strict mode)
- **Alchemy SDK** — on-chain data
- **Claude API** — lore generation
- **@vercel/og (Satori)** — server-side image rendering
- **Tailwind CSS 4**
- **Vercel** — deployment + edge caching
- **Sentry** — error monitoring

## What I'd Do Differently

1. **Protocol whitelisting doesn't scale.** It works for ~40 known contracts, but any new DEX or NFT marketplace is invisible until manually added. A production system would need transaction decoding via ABI or a classification API like Transpose. I chose the whitelist because it ships in a day; the alternative is a week of parser work.

2. **In-memory cache resets on cold starts.** I launched with a simple `Map<string, CachedResult>` and a 24h TTL. First cold start after deploy wiped everyone's cached results. I added Vercel KV (Redis) as a persistence layer on day 3 — should have started there. The lesson: if your cache holds user-visible data, it needs to survive restarts.

3. **Log-scale tuning is more art than science.** I tested ~60 known wallets (Vitalik, DeFi founders, NFT collectors, fresh wallets) and manually adjusted multipliers until the stat distribution "felt right." A better approach: collect 1000+ wallet samples, plot the actual distribution, and derive multipliers statistically. I might do this for v2.

## Try It

[https://ethrpg.app](https://ethrpg.app)

Paste any ETH address or ENS name. Takes about 10 seconds.

Have you ever gamified raw data into something shareable? I'd love to hear what scoring or classification approaches worked for you — or what pitfalls you ran into.

---

*Built by a solo developer over a 7-day sprint. The entire codebase is Next.js + TypeScript.*
