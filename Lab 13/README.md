# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Estimate a multivariate hedonic pricing model on 2026 California real estate data and furnish a manual proof of the Frisch-Waugh-Lovell (FWL) theorem, demonstrating that algorithmic *ceteris paribus* is not merely a theoretical convenience but a mathematically exact operation recoverable through sequential residual extraction.

---

## Methodology

- **Data:** Synthetic 2026 California residential transaction records sourced from Zillow, comprising `Sale_Price`, `Property_Age`, and `Distance_to_Tech_Hub` — a feature set designed to surface multicollinearity and omitted variable bias in a controlled, interpretable setting.

- **Baseline OLS (Bivariate):** Estimated a simple regression of `Sale_Price` on `Property_Age` alone, establishing a contaminated benchmark coefficient that conflates the age effect with the unmodeled influence of tech hub proximity.

- **Multivariate OLS:** Extended the specification to include `Distance_to_Tech_Hub`, producing a full hedonic model via `statsmodels.formula.api`. The shift in the `Property_Age` coefficient between the bivariate and multivariate models provides direct, quantifiable evidence of omitted variable bias (OVB).

- **Manual FWL Proof — Stage 1 (Partialling Out the Regressor):** Regressed `Property_Age` on `Distance_to_Tech_Hub` and extracted the residuals — the component of `Property_Age` that is orthogonal to, and therefore linearly independent of, tech hub proximity.

- **Manual FWL Proof — Stage 2 (Partialling Out the Outcome):** Regressed `Sale_Price` on `Distance_to_Tech_Hub` and extracted the residuals — the component of sale price unexplained by location alone.

- **FWL Verification:** Regressed the Stage 2 residuals on the Stage 1 residuals via simple OLS. By the FWL theorem, this coefficient must be algebraically identical to the `Property_Age` coefficient recovered in the full multivariate model, confirming that shared covariance has been fully purged.

- **Visualization:** Plotted both the contaminated bivariate fit and the FWL-corrected partial regression to provide an intuitive, geometric illustration of how controlling for covariates reshapes the estimated relationship.

---

## Key Findings

The bivariate model produced a severely biased estimate of `Property_Age`'s effect on sale price. Because older properties in California's 2026 market tend to be located farther from major tech hubs — and distance from tech hubs is a primary value depressant — the simple regression falsely attributed a disproportionate share of location-driven price suppression to the age of the structure itself.

Introducing `Distance_to_Tech_Hub` into the multivariate specification corrected this attribution, yielding a materially different `Property_Age` coefficient that reflects its true, isolated contribution to price variation.

The manual FWL implementation confirmed this result with exact numerical precision: after sequentially regressing out the influence of `Distance_to_Tech_Hub` from both `Property_Age` and `Sale_Price`, the coefficient from the resulting univariate residual regression matched the multivariate OLS estimate to full floating-point accuracy. This constitutes a direct, empirical proof that the FWL theorem is not an approximation — it is an algebraic identity. The multivariate estimator achieves *ceteris paribus* by implicitly executing this partialling operation across all included regressors simultaneously.

---

## Tech Stack
- **Language:** Python 3.10+
- **Libraries:** `pandas`, `statsmodels.formula.api`, `matplotlib`
- **Data:** Zillow Synthetic California Real Estate Dataset (2026)
