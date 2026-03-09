# Spurious Correlation & Multicollinearity in Macroeconomic Time-Series Data

## Overview
This project investigates two of the most common—and consequential—pitfalls in econometric modeling: spurious correlation and multicollinearity. Using macroeconomic data sourced from the **FRED API**, I demonstrate how naive analysis of raw time-series data can produce misleading statistical relationships, and walk through a rigorous diagnostic and remediation workflow.

## Methodology

**1. Correlation Trap Visualization**
Using Python, pandas, and seaborn, I visualized pairwise correlations across multiple macroeconomic indicators in their raw level form. These plots expose "correlation traps"—cases where two unrelated variables appear strongly associated simply because both trend upward over time.

**2. Multicollinearity Diagnostics via VIF**
To quantify redundancy among predictors, I applied Variance Inflation Factor (VIF) analysis using statsmodels. High VIF scores confirmed the presence of severe multicollinearity in the raw data, highlighting the instability this would introduce into any regression model built on these features.

**3. Stationarity Transformation**
To address non-stationarity, I transformed all variables into Year-over-Year (YoY) growth rates—a standard technique for removing shared trends and anchoring each series to economically meaningful change signals rather than arbitrary level trajectories.

**4. Causal Structure Mapping with DAGs**
Finally, I employed Directed Acyclic Graphs (DAGs) to move beyond correlation and map the true structural relationships between variables. This causal framework clarifies which associations are genuine, which are confounded, and which disappear entirely once shared trends are removed.

## Key Takeaways
- Raw macroeconomic levels are nearly always non-stationary and will produce spurious correlations if used uncritically.
- VIF diagnostics are an effective first-pass tool for identifying redundant features before model fitting.
- YoY transformations and DAG-based causal reasoning together form a principled framework for building more honest, interpretable macroeconomic models.

## Tools & Libraries
`Python` · `pandas` · `seaborn` · `statsmodels` · `FRED API`
