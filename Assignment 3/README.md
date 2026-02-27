## Theoretical Visual Evidence for Conclusive Selection Bias Mitigation

This is fundamentally an epistemological question in causal inference — the Love Plot is necessary but not sufficient on its own. Here is the full evidentiary hierarchy, ordered from weakest to strongest proof:

---

### Tier 1 — The Love Plot (What You Just Built)
**What it shows:** Whether covariate means converged between treated and control groups after matching.

**What constitutes conclusive visual evidence:**
- Every blue circle (post-match) must land inside the green band (`|SMD| ≤ 0.10`). A single covariate outside this zone is sufficient to claim residual confounding survives.
- All connecting segments must point **leftward** (toward zero). Any rightward shift — an orange segment — means matching actively worsened balance on that variable, which is a red flag regardless of where it lands in absolute terms.
- The reduction must be **substantial, not cosmetic.** A covariate moving from `|SMD| = 0.08` to `0.06` is noise. Moving from `0.45` to `0.04` is evidence the algorithm corrected a real structural imbalance. The ratio of mean |SMD| before vs. after should be ≥ 75–80% reduction to be credible.

**What it cannot prove:** Equal means do not guarantee equal distributions. Two groups can have identical means but radically different spreads, skewness, or tail behaviour — all of which constitute remaining imbalance that the Love Plot is blind to.

---

### Tier 2 — Variance Ratio Plot (The Gap the Love Plot Leaves)
**What it shows:** Whether the *spread* of each covariate is comparable between groups post-matching, not just the means.

**Formula:** `VR = σ²_treated / σ²_control`

**What constitutes conclusive visual evidence:**
- All post-match variance ratios must fall within **[0.5, 2.0]** — Rubin's (2001) rule of thumb. Ratios outside this range indicate distributional imbalance that |SMD| cannot detect.
- A perfectly balanced match produces VR = 1.0 for all covariates. Visual proximity to the 1.0 line is the signal you're looking for.

**Why this matters for SwiftCart specifically:** If high-spending subscribers have more variance in `pre_spend` than controls (plausible in loyalty data), matching on PS alone can align means while leaving the variance ratio at 3.0 or 4.0 — meaning the distributions are still structurally different.

---

### Tier 3 — Propensity Score Overlap Plot (Common Support)
**What it shows:** Whether treated and control units actually inhabit the same region of PS space — the **common support** assumption.

**What constitutes conclusive visual evidence:**
- Pre-match: the PS distributions of treated and control should be visually separated (this is expected — it confirms selection bias existed).
- Post-match: the two PS distributions must **substantially overlap**, ideally appearing nearly identical. Remaining separation after matching means you are extrapolating treatment effects into regions with no comparable controls, which invalidates the ATT estimate entirely.
- There should be **no mass at the extremes** (PS ≈ 0 or PS ≈ 1) in the matched sample. Units with extreme scores are structurally unmatchable and should have been trimmed before matching.

---

### Tier 4 — Empirical CDF Plot (The Strongest Single Visual Test)
**What it shows:** Full distributional equivalence across the entire covariate range, not just means or variances.

**What constitutes conclusive visual evidence:**
- Post-match empirical CDFs for treated and control must be **visually indistinguishable** for every covariate — the two lines should essentially overlap.
- Pre-match CDFs should show clear horizontal separation (the visual signature of selection bias).
- The maximum vertical distance between the post-match CDFs is the **Kolmogorov-Smirnov statistic**. A near-zero KS statistic after matching is the closest thing to distributional proof of balance available without a randomized experiment.

---

### Tier 5 — Effective Sample Size (Not Visual, But Required Context)
This is not a plot but is mandatory interpretive context for all of the above. Balance achieved by discarding 80% of your control pool is not the same as balance achieved with high retention. The footnote in your Love Plot already reports this — but the ESS must be explicitly defended. For SwiftCart with 8,941 rows, losing more than ~40% of matched pairs to the caliper should trigger a sensitivity analysis with a looser caliper.

---

### The Unified Evidentiary Standard

| Evidence | What It Rules Out | Tier |
|---|---|---|
| Love Plot (all |SMD| ≤ 0.10) | Mean imbalance | Necessary |
| Variance Ratio (all VR ∈ [0.5, 2.0]) | Spread imbalance | Necessary |
| PS Overlap Plot | Extrapolation beyond common support | Necessary |
| Empirical CDF overlap | Full distributional imbalance | Sufficient |
| Adequate ESS | Precision-bias tradeoff | Required context |

Only when **all four visual tests pass simultaneously** with adequate ESS can you claim with theoretical rigour that selection bias was successfully mitigated. In practice, peer reviewers and journal editors in economics and epidemiology expect at minimum Tiers 1–3. Tier 4 is the gold standard. No single plot, including the Love Plot, is sufficient on its own.
