# Recovering Experimental Truths via Propensity Score Matching

---

## Objective

Applied Propensity Score Matching to a selection-biased observational dataset to neutralize confounding and recover a causal treatment effect consistent with the randomized experimental benchmark.

---

## Methodology

- **Diagnosed Observational Failure:** Established the baseline problem using a naive difference-in-means on the observational Lalonde subset, surfacing a heavily distorted estimate driven by systematic selection bias — not treatment effect.

- **Modeled the Selection Process:** Fit a Logistic Regression model (via Scikit-Learn) on pre-treatment covariates — age, education, race, marital status, and prior earnings — to estimate each unit's propensity score: the conditional probability of receiving treatment given observable characteristics.

- **Applied Nearest-Neighbor Matching:** Used a 1-to-1 Nearest Neighbor algorithm to pair each treated unit with its closest control counterpart in propensity score space, constructing a matched sample where the treated and control groups are statistically comparable on all observed confounders.

- **Validated Against Experimental Ground Truth:** Compared the matched estimate against the known experimental ATE from the randomized Lalonde subset to assess how closely the PSM procedure recovered the true causal effect.

---

## Key Findings

| Estimate | Value |
|---|---|
| Naive Observational Difference | -$15,204 |
| PSM-Adjusted Treatment Effect | ~+$1,800 |
| Experimental Benchmark (Ground Truth) | ~+$1,795 |

The naive estimate was not merely attenuated — it was directionally wrong, suggesting job training *harmed* earnings. After matching on propensity scores, the adjusted estimate recovered the true treatment effect within close proximity of the randomized experimental benchmark, demonstrating that the original bias was entirely attributable to selection into treatment, not the training program itself.

This result illustrates both the danger of unexamined observational inference and the power of design-based causal methods to correct it.
