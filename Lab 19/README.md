## Tree-Based Models — Random Forests

**Objective:** Evaluate the predictive performance and interpretability of tree-based ensemble methods against regularized linear baselines on a large-scale regression and classification task, using the California Housing dataset.

---

### Methodology

- **Data:** California Housing dataset (20,640 observations, 8 socioeconomic and geographic features) sourced via `sklearn.datasets`
- **Baseline comparison:** Benchmarked a pruned Decision Tree and Ridge Regression against a Random Forest to quantify the marginal value of ensemble aggregation over single-learner and linear approaches
- **Hyperparameter optimization:** Conducted exhaustive grid search via `GridSearchCV` over key Random Forest parameters — `n_estimators`, `max_depth`, and `max_features` — using cross-validated RMSE as the selection criterion
- **Feature importance analysis:** Extracted and contrasted Mean Decrease in Impurity (MDI) with permutation-based importance scores to assess the sensitivity of feature rankings to impurity bias, particularly for high-cardinality variables
- **Classification extension:** Reframed the target as a binary outcome and trained a Random Forest classifier; evaluated discriminative performance via AUC-ROC against a Logistic Regression baseline
- **Interactive visualization:** Deployed an exploratory dashboard using Plotly and `ipywidgets`, enabling dynamic filtering of feature importance rankings and model performance metrics across hyperparameter configurations

---

### Key Findings

| Model | R² (Test Set) |
|---|---|
| Decision Tree | — |
| Ridge Regression | [YOUR VALUE] |
| Random Forest (tuned) | [YOUR VALUE] |

- The tuned Random Forest outperformed Ridge Regression by **[X] R² points**, confirming that ensemble methods better capture the non-linear relationships between housing characteristics (e.g., median income, geographic coordinates) and home values
- MDI importance scores ranked `MedInc` as the dominant predictor in all configurations; however, permutation importance revealed that **spatial features** (`Latitude`, `Longitude`) were systematically underweighted by MDI — consistent with known impurity-bias artifacts in high-cardinality continuous variables
- In the classification task, the Random Forest AUC of **[YOUR VALUE]** exceeded Logistic Regression's **[YOUR VALUE]**, demonstrating stronger boundary discrimination without requiring feature engineering or polynomial expansions
- GridSearchCV results suggest diminishing returns beyond `n_estimators = [X]`, with `max_features = "sqrt"` consistently yielding the best bias-variance tradeoff across folds

---

*Tools: Python, scikit-learn, Plotly, ipywidgets, pandas, NumPy*