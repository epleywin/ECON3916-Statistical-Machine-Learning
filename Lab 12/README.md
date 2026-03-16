# Architecting the Prediction Engine: Multivariate OLS Real Estate Valuation Forecasting

## Objective
Engineer a multivariate Ordinary Least Squares (OLS) prediction engine capable of forecasting residential real estate valuations from cross-sectional market data, with rigorous out-of-sample evaluation grounded in financially interpretable loss metrics.

---

## Methodology

- **Dataset Acquisition & Scoping:** Sourced the Zillow Home Value Index (ZHVI) 2026 Micro Dataset — a rich, cross-sectional snapshot of contemporary U.S. real estate market conditions — as the empirical foundation for model training and evaluation.

- **Feature Engineering & Model Specification:** Constructed a multivariate feature matrix using `pandas` and `numpy`, then specified the regression model declaratively via `statsmodels`' Patsy Formula API, enabling clean, reproducible model architecture.

- **OLS Estimation:** Fit the prediction engine using Ordinary Least Squares regression, estimating coefficients across all selected predictors to minimize in-sample residual variance.

- **Train/Test Split & Out-of-Sample Evaluation:** Partitioned the dataset into training and holdout sets to simulate real-world deployment conditions and assess genuine predictive generalizability.

- **Loss Quantification (RMSE in USD):** Calculated Root Mean Squared Error (RMSE) denominated directly in U.S. Dollars — translating abstract statistical loss into a concrete, decision-relevant financial error margin.

---

## Key Findings

This project marked a deliberate architectural shift from classical inferential econometrics — where models explain relationships — to **predictive engineering**, where models are optimized to generalize to unseen data.

The engine's performance was evaluated not by p-values or R², but by its **real-world financial cost of being wrong**. By expressing RMSE in actual USD, the model's error tolerance was made directly legible to business stakeholders, enabling concrete assessment of algorithmic risk in a production pricing or investment context.

The results demonstrate that a well-specified OLS engine, even without nonlinear complexity, can serve as a credible baseline prediction system for real estate valuation — and that rigorous out-of-sample loss measurement is the correct benchmark for any model deployed in a financial decision-making pipeline.

---

## Tech Stack
`Python` · `pandas` · `numpy` · `statsmodels` · Patsy Formula API
