# Causal ML — Double Machine Learning for 401(k) Policy Evaluation

## Objective
Leverage the Double Machine Learning (DML) framework to produce credible, debiased estimates of the Average Treatment Effect (ATE) of 401(k) plan eligibility on household net financial assets, isolating the causal channel from high-dimensional confounders via orthogonalized nuisance estimation.

---

## Methodology

- **Regularization Bias Demonstration:** Simulated a data-generating process (DGP) with a known true ATE of 5.0 to illustrate that naïve LASSO application shrinks the treatment coefficient toward zero — a canonical form of regularization-induced confounding bias that motivates the DML correction.

- **Double ML / Partially Linear Regression (PLR):** Implemented a DoubleML PLR model using Random Forest nuisance learners with 5-fold cross-fitting, separating the estimation of the outcome residual and treatment residual to achieve Neyman orthogonality and root-*n* consistent inference.

- **ATE Estimation on 401(k) Data:** Applied the PLR model to the 401(k) pension plan dataset, estimating the average causal effect of eligibility (`e401`) on net financial assets while flexibly controlling for income, age, family size, and other covariates.

- **Heterogeneous Treatment Effects (CATE):** Decomposed the estimated treatment effect across income quartiles to detect and quantify treatment effect heterogeneity, producing Conditional ATE (CATE) estimates with bootstrapped confidence intervals.

- **Visualization:** Plotted CATE point estimates and 95% confidence intervals across income subgroups to communicate effect heterogeneity to both technical and policy audiences.

---

## Key Findings

The DML PLR model yields a statistically significant positive ATE of 401(k) eligibility on net financial assets, consistent with prior reduced-form literature. CATE analysis reveals meaningful variation across the income distribution, suggesting that eligibility incentives are not uniformly effective — a finding with direct policy relevance for retirement savings design.

A formal **sensitivity analysis** (Cinelli-Hazlett-style bounds) was conducted to assess robustness to potential unobserved confounding:

| Parameter | Value |
|---|---|
| Significance level | 0.95 |
| Partial R² of confounder w/ outcome (`cf_y`) | 0.03 |
| Partial R² of confounder w/ treatment (`cf_d`) | 0.03 |
| Correlation parameter ρ | 1.0 |

Under this scenario, the **theta bounds** span approximately **−2,643 to +909**, with the full confidence interval ranging from roughly **−3,457 to +1,693**. The **Robustness Value (RV)** of ~1.5% indicates that an unobserved confounder explaining as little as 1.5% of residual variance in both the outcome and treatment would be sufficient to reduce the point estimate to zero at conventional significance levels. The **RVₐ** of ~0.13% sets an even more stringent threshold for sign reversal.

These results underscore the importance of rigorous sensitivity reporting alongside DML point estimates: while the structural estimate is economically meaningful, its statistical robustness to even modest omitted-variable bias is limited, warranting cautious interpretation in a policy context.
