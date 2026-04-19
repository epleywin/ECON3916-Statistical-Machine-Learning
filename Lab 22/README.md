
# Clustering World Economies with K-Means & PCA

---

## Objective

This project applies unsupervised machine learning to identify latent structural groupings among world economies and California census tracts, using K-Means clustering and Principal Component Analysis (PCA) to surface patterns across high-dimensional development and housing indicators.

---

## Methodology

**Data Acquisition**
- Retrieved 10 World Bank development indicators across ~160 countries via the `wbgapi` Python library, spanning dimensions such as GDP per capita, health expenditure, and educational attainment.
- Applied the same pipeline to the California Housing dataset, operating at the census tract level.

**Preprocessing**
- Standardized all features using `StandardScaler` prior to clustering to ensure equal contribution across indicators with disparate units and scales.

**Clustering**
- Fit a K-Means model with K=4 on the global development dataset; evaluated cluster stability across K=2 through K=10 using both the elbow method and silhouette analysis.
- Cross-tabulated algorithmically derived clusters against World Bank income classifications to assess structural alignment with established economic groupings.

**Dimensionality Reduction & Visualization**
- Projected high-dimensional cluster assignments into two dimensions via PCA for interpretable scatter plot visualization of cluster separation.

---

## Key Findings

**California Housing**
- Silhouette analysis identified K=2 as the optimal solution (score: 0.3308), indicating that California housing data separates most cleanly into two broad structural clusters rather than fragmenting into many granular subgroups.
- Cluster sizes are well-balanced, suggesting the model generalizes across the data rather than overfitting to outlier observations.
- The first two principal components account for approximately 48.9% of total variance — sufficient to characterize the dominant structure in the data and confirm a meaningful high-level division in housing characteristics across the state.

**World Economies**
- K-Means clustering on World Bank indicators produced groupings with substantial correspondence to official income classifications, validating the model's capacity to recover economically meaningful structure from raw development data without supervision.

---
