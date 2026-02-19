**Critique 1**

Current optimistic rollups rely on a *first-valid-wins* model. While simultaneous challenges could create short-term unfairness, such boundary cases are rare. The paper’s focus here may be too narrow.

**Response**

In current contracts, ordering is not enforced → effectively U-P. Simply upgrading to U-B doesn’t guarantee incentive-compatibility; the paper’s aim is to design mechanisms that are incentive-compatible under any ordering.

---

**Critique 2**

The three scenarios (Fair-ordering, U-P, U-B) don’t fully cover all possible orderings. Auction theory could provide richer models and alternatives.

**Response**

The scenarios were chosen to represent meaningful baselines. Extending to auction-based prioritization is possible but outside the paper’s current scope as a short theoretical contribution.

---

**Critique 3**

When challenges enter the mempool, free-riding/front-running is possible. The paper only briefly mentions this as future work.

**Response**

Free-riding is less problematic: fraud proofs are resolved via multi-step dispute games. Commit–reveal schemes can further mitigate copycats, and realistically only validators already checking state can engage.

---

**Critique 4**

Confusion around proposer vs. sequencer: isn’t the proposer effectively the sequencer in rollups?

**Response**

Often they coincide, but strictly, the proposer is the entity submitting the state root. The paper uses this stricter terminology.

---

**Critique 5**

In the multi-winner case, equations suggest deterrence becomes independent of $N$. However, they still seem to imply both an *upper* and a *lower* bound on adversarial accounts $A$, which feels counterintuitive.

**Response**

Correct: $N$ disappears, but dependence on A remains. Security can be expressed as tolerating up to A \cdot s adversarial stake (Lemma 3). The apparent lower bound comes from requiring *non-trivial* deterrence ($\alpha < 1$), not from Lemma 3 itself.

---

**Critique 6**

There seems to be a *lower bound* on adversarial accounts A under non-trivial deterrence, which is not yet fully clarified.

- From deterrence condition:
$\alpha \le \frac{1-\eta}{\varphi}, \quad \varphi = \frac{A}{N}$
- Non-triviality requires $\alpha < 1$:
$\frac{1-\eta}{\varphi} < 1 \;\;\Longrightarrow\;\; \varphi > 1-\eta \;\;\Longrightarrow\;\; A > N(1-\eta).$
- This implies a **minimum number of adversarial accounts** must exist for non-trivial deterrence to hold, which feels paradoxical (fewer adversaries should not make deterrence harder).