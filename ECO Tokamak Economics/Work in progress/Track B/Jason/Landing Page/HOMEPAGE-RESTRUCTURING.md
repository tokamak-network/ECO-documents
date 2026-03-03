# Homepage Restructuring Proposal

## Problem Diagnosis

The current homepage **shows price data (Carousel) before explaining what Tokamak is.** For non-developer visitors, the first impression may feel like an exchange dashboard, and the Hero copy ("L2 ON-DEMAND TAILORED ETHEREUM") alone fails to communicate differentiation from competing L2s.

Additionally, core content (Protocols, Getting Started) is buried in the middle-to-lower portion of the page. Considering typical web scroll patterns (roughly 50% of visitors reach only the 60% mark of a page — NNGroup, "Scrolling and Attention", 2018), exposure opportunities are limited.

The current structure functions as a **technology catalog** — listing features without guiding visitors through a narrative. Most blockchain project landing pages follow the same pattern, making differentiation difficult.

---

## Three Approaches

| | A. Interactive Demo | B. Storytelling + Activity Proof | C. Live Dashboard |
|:--|:--|:--|:--|
| Core Idea | Hero IS an L2 deployment simulation | Narrative flow with live dev activity as evidence | Homepage as real-time ecosystem status board |
| Differentiation | Very high | High | Moderate |
| Effort | 2-3 weeks | 1.5-2 weeks | 1 week |
| Non-developer accessibility | Moderate | High | Low |
| Investor appeal | Moderate | High | High |
| Maintenance | High | Low | Medium |

---

## Approach A: Interactive Demo

The Hero itself becomes an **L2 deployment simulation**. Visitors experience "building an L2" visually on first load — no scrolling needed to understand the product.

### Page Structure

```
[1] Hero = Interactive L2 Builder Simulation
    "Pick your config → See your L2 launch"
    (visual simulation, not actual deployment)
[2] Ecosystem Live Dashboard (metrics + network visualization)
[3] Use Cases (3 scenario cards: Gaming / DeFi / Enterprise)
[4] Developer Hub (Docs, GitHub, Grant in one place)
[5] Blog + Reports (unified feed)
[6] Footer
```

### Section Details

**[1] Hero — Interactive Simulator**
- Visitor selects options: throughput level, privacy mode, VM type
- Animated visualization shows an L2 "deploying" on Ethereum
- Final state shows: "Your L2 is ready. [Deploy for Real →]"
- Background: network node graph instead of current 3D grid

**[2] Ecosystem Dashboard**
- Live metrics: Active L2s, Total Staked, Code Changes
- Animated network topology visualization
- Data sources: `/api/price` + latest biweekly report

**[3] Use Cases**
- 3 cards showing concrete scenarios where custom L2s solve real problems
- Each card links to relevant protocol or documentation

**[4] Developer Hub**
- Single section combining Docs, GitHub, Grant, Onboarding
- Replaces current Getting Started section with cleaner layout

**[5] Latest**
- Unified feed: Blog posts + Dev Reports in chronological order

### Trade-offs

- **Pro**: Memorable first impression, product differentiation is immediately felt
- **Con**: Highest development effort, simulation logic needs careful design to feel authentic without misleading, ongoing maintenance for simulator updates

### Effort Breakdown

| Phase | Work | Duration |
|:------|:-----|:---------|
| 1 | Simulator UI + interaction logic | 1 week |
| 2 | Network visualization + dashboard | 3-4 days |
| 3 | Use Cases + Developer Hub | 2 days |
| 4 | Latest feed + Footer | 1 day |
| 5 | Animation polish + responsive | 2-3 days |
| **Total** | | **~2-3 weeks** |

---

## Approach B: Storytelling + Activity Proof (Recommended)

A single-page **narrative** that guides visitors from problem → solution → proof → action. Development activity data (commits, code changes, active repos) is woven into the story as evidence — not just metrics, but **proof that Tokamak is actively building**.

### Page Structure

```
[1] Hero          "Every app deserves its own L2"     -- problem statement
         ↓ scroll
[2] Pain Points    3 limitations of existing L2s      -- build empathy
         ↓
[3] Solution       Tokamak's approach                 -- present the answer
         ↓
[4] Proof Wall     commits, code changes, projects    -- show activity ★
         ↓
[5] Protocols      3-4 key protocol highlights        -- concrete capabilities
         ↓
[6] Dev CTA        Start building (Docs/GitHub/Grant) -- call to action
         ↓
[7] Latest         Blog + Reports unified feed        -- recent news
         ↓
[8] Footer         Links + inline newsletter          -- wrap up
```

### Section Details

**[1] Hero — Problem Statement**

Replace the current technical jargon with a visitor-centric message:

> **"Every app deserves its own L2.**
> **But building one shouldn't take months."**
>
> [Start Building]  [See How It Works ↓]

- "See How It Works" scrolls to Pain Points, creating a guided journey
- Background: simplified network animation or clean gradient (lighter than current 3D grid)

**[2] Pain Points — Build Empathy**

Three cards that appear on scroll, each describing a real limitation:

| Problem | Description |
|:--------|:------------|
| Shared Congestion | "Your users compete with every other app on the same chain" |
| One-Size-Fits-All | "Generic L2s force you to compromise on throughput, cost, or privacy" |
| Months to Launch | "Setting up infrastructure takes engineering teams months" |

- Simple icons, short copy, no external data needed
- Scroll-triggered fade-in animation

**[3] Solution — Tokamak's Answer**

Transition animation where Pain Point cards "resolve" into Tokamak's approach:

> **"Tokamak lets you launch a tailored L2 in minutes."**

- Architecture diagram: Your App → Tokamak SDK → Custom L2 (on Ethereum)
- Three differentiators as icon + one-liner:
  - Dedicated Throughput
  - Custom Configuration
  - Ethereum-grade Security

**[4] Proof Wall — Activity Evidence ★**

The narrative pivot: "Don't take our word for it. Here's what we've been building."

Top row — 4 animated counters (reuse existing `AnimatedCounter` component):

| Metric | Data Source | Notes |
|:-------|:-----------|:------|
| Total Code Changes | Report `stats.linesChanged` | Latest biweekly report |
| Active Projects | Report `stats.activeRepos` | Latest biweekly report |
| Biweekly Commits | Report `stats.commits` | Latest biweekly report |
| TON Staked | `/api/price` → `stakedVolume` | Real-time from API |

Bottom row — Category activity chart:
- Horizontal bar chart showing code changes per category (L2 Infrastructure, Security, Governance, etc.)
- Data from `EcosystemLandscape.categories` in the latest report
- Each bar colored by category color, sorted by activity volume
- Links to full report: "See detailed report →"

**Future expansion**: As more biweekly reports accumulate, add a time-series sparkline showing commit/code-change trends over months.

**[5] Protocols — Key Capabilities**

Reduce from 12 protocols to **3-4 highlights** based on highest activity:

- L2 Infrastructure & Scalability
- Application-specific L2
- New class of zk-EVM
- (1 more based on current focus)

Each card: icon + title + 2-line description + [Learn More →]

Remaining protocols accessible via "See all protocols →" link to a dedicated page or expandable section.

**[6] Developer CTA — Call to Action**

Three equal cards in a row:

```
┌─────────────────┬─────────────────┬─────────────────┐
│  Docs           │  GitHub         │  Grant          │
│  Read the       │  Explore the    │  Get funded     │
│  documentation  │  codebase       │  to build       │
│  [Open Docs →]  │  [View Code →]  │  [Apply Now →]  │
└─────────────────┴─────────────────┴─────────────────┘
```

Replaces current Getting Started section. Cleaner, action-oriented.

**[7] Latest — Unified Feed**

Merge Medium blog posts and biweekly dev reports into a single chronological feed.

- Card format: thumbnail + title + date + type badge ("Blog" / "Dev Report")
- Show 3-4 most recent items
- "View all →" links to `/about/insight` or `/about/reports`

**[8] Footer**

Current footer structure + inline newsletter input (per Proposal 5 from incremental plan).

### Available Data Sources

| Data | Source | Status |
|:-----|:-------|:-------|
| Code changes, commits, active repos | Biweekly report HTML parsing | Ready (parser exists) |
| Category-level activity breakdown | `EcosystemLandscape` from reports | Ready (parser exists) |
| Per-repo activity levels (high/medium/low) | `LandscapeRepo.activity` | Ready |
| TON staked, supply, burned | `/api/price` endpoint | Ready (real-time) |
| Medium blog posts | `/api/medium` RSS feed | Ready |
| Newsletter subscriptions | Firebase RTDB | Ready |
| Historical trends across reports | Not yet available | Needs multiple reports + aggregation |
| Direct GitHub API (stars, PRs, issues) | Not integrated | Optional future enhancement |

### Trade-offs

- **Pro**: Accessible to non-developers, strong investor narrative, activity data adds credibility, moderate effort, low maintenance
- **Con**: Depends on good copywriting (EN required, KR optional), biweekly report data is only as fresh as the latest report, category chart needs design attention

### Effort Breakdown

| Phase | Work | Duration |
|:------|:-----|:---------|
| 1 | Hero + Pain Points + Solution (copy + layout) | 2-3 days |
| 2 | Proof Wall (report data integration + category chart) | 2-3 days |
| 3 | Protocols highlight + Dev CTA | 1 day |
| 4 | Latest feed (Blog + Reports merge) + Footer | 1 day |
| 5 | Scroll animations + responsive polish | 1-2 days |
| **Total** | | **~1.5-2 weeks** |

### Comparison: Current vs Proposed

| Aspect | Current | Proposed |
|:-------|:--------|:---------|
| Hero | Technical jargon listing | Visitor problem statement |
| Price data | 2nd section (too early) | Staking only, inside Proof Wall |
| Protocols | All 12 listed | 3-4 highlights + "see all" link |
| Activity proof | None | Commits, code changes, projects front and center |
| Getting Started | Buried in middle | Post-climax CTA position |
| Newsletter | Standalone section | Footer inline |

---

## Approach C: Live Dashboard

The homepage becomes a **real-time ecosystem status board**. Every section shows live data — the page itself is proof that Tokamak is active and transparent.

### Page Structure

```
[1] Hero = 3 key metrics + one-line tagline
[2] Network Status Dashboard (TVL, Active L2s, Staking, Transactions)
[3] Recent Activity Feed (GitHub commits, blog posts, reports as unified timeline)
[4] Protocols Grid (current design, improved visually)
[5] Developer CTA
[6] Footer
```

### Section Details

**[1] Hero — Metrics First**
- Large animated numbers: Total Staked, Active Projects, Code Changes
- One-line tagline: "Building the infrastructure for on-demand L2s"
- Minimal copy, data speaks

**[2] Network Status**
- Dashboard-style layout: cards with real-time metrics
- Staking volume, supply breakdown, burn rate from `/api/price`
- Report stats (commits, contributors) from latest biweekly report
- Auto-refresh or polling for live feel

**[3] Activity Feed**
- Chronological timeline mixing:
  - Blog posts (from Medium RSS)
  - Dev reports (from parsed reports)
  - Optionally: GitHub commits (requires new API integration)
- Each item: timestamp + type icon + title + link

**[4] Protocols Grid**
- Keep current 12-protocol grid
- Visual refresh: better cards, activity indicators per protocol
- Add code-change badges from report data

**[5] Developer CTA**
- Same as Approach B: Docs / GitHub / Grant cards

### Trade-offs

- **Pro**: Leverages existing API infrastructure, strong transparency signal, data-driven credibility for investors, moderate effort
- **Con**: If metrics are modest, page feels underwhelming. Non-developers may not understand what the numbers mean. Dashboard aesthetic may feel cold/impersonal. Requires continuous data to stay fresh.

### Effort Breakdown

| Phase | Work | Duration |
|:------|:-----|:---------|
| 1 | Hero metrics + Network Status dashboard | 2-3 days |
| 2 | Activity feed (timeline component) | 2 days |
| 3 | Protocols visual refresh | 1 day |
| 4 | Dev CTA + Footer | 1 day |
| **Total** | | **~1 week** |

---

## Recommendation

**Approach B (Storytelling + Activity Proof)** offers the best balance:

1. **Narrative flow** makes the page accessible to all audiences — developers, investors, and curious visitors
2. **Activity data** (commits, code changes, active projects) woven into the story adds credibility without overwhelming
3. **Existing data sources** (biweekly reports, price API) are sufficient — no new external integrations required at launch
4. **Moderate effort** (1.5-2 weeks) with low ongoing maintenance
5. **Scalable**: as more reports accumulate, historical trend charts can be added incrementally

### Suggested Implementation Order

Ordered by impact-to-effort ratio:

| Priority | Phase | Effort |
|:---------|:------|:-------|
| 1 | Hero + Pain Points + Solution (new narrative sections) | 2-3 days |
| 2 | Proof Wall (report data + category chart) | 2-3 days |
| 3 | Protocols highlight reduction (12 → 3-4) | 1 day |
| 4 | Latest feed + Footer inline newsletter | 1 day |
| 5 | Scroll animations + responsive polish | 1-2 days |
