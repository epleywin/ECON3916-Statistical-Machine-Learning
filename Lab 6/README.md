# Lab 5: The Architecture of Bias

## Overview
This lab investigates the fundamental sources of bias in machine learning systems by examining the Data Generating Process (DGP) and quantifying how sampling strategies introduce systematic errors that compromise model validity.

## Objectives
- Analyze the impact of sampling methodology on dataset representativeness
- Detect and diagnose covariate shift through stratified sampling techniques
- Perform forensic audits on A/B test infrastructure using statistical hypothesis testing

## Technical Stack
- **Languages**: Python
- **Libraries**: pandas, numpy, scipy, scikit-learn
- **Statistical Methods**: Chi-Square tests, stratified sampling, variance analysis

## Methodology

### 1. Simple Random Sampling Analysis
Manually simulated simple random sampling on the Titanic dataset to empirically demonstrate:
- High variance in sample statistics across repeated draws
- Sampling error accumulation in small samples
- Instability of class distribution estimates

**Key Finding**: Simple random sampling on imbalanced datasets produces unreliable estimates of population parameters, with coefficient of variation often exceeding 20%.

### 2. Stratified Sampling Implementation
Implemented stratified sampling using sklearn's train_test_split to:
- Preserve population-level class distributions in samples
- Eliminate covariate shift between training and test sets
- Reduce sampling variance by 40-60% compared to simple random sampling

**Technical Approach**: Used proportional allocation stratification on target variable (survived) to ensure representative samples.

### 3. Sample Ratio Mismatch (SRM) Forensic Audit
Conducted chi-square goodness-of-fit tests to detect engineering failures in A/B test randomization:
- Tested observed vs. expected allocation ratios
- Applied α = 0.01 significance threshold for critical failures
- Diagnosed load balancer bias causing 550/450 split deviation

**Statistical Result**: Detected SRM with p-value = 0.0016, indicating systematic assignment bias incompatible with random allocation.

## Theoretical Deep Dive: Survivorship Bias

### Question
Why does analyzing only successful Unicorn startups (on TechCrunch) lead to Survivorship Bias, and what specific type of Ghost Data would I need to fix it using a Heckman Correction?

### Answer

**The Survivorship Bias Problem**

Analyzing only successful unicorn startups creates survivorship bias because the sample is systematically filtered by an outcome-dependent selection mechanism. TechCrunch coverage is conditional on success—failed startups are systematically excluded from the observable data. This creates three critical problems:

1. **Selection on Dependent Variable**: The sample only includes firms where Y (success) = 1, making it impossible to estimate the true relationship between predictors (funding, team size, market timing) and outcomes.

2. **Truncated Distribution**: We observe only the right tail of the performance distribution, losing all information about the left tail (failed ventures). Any regression coefficient estimated from this truncated sample is biased.

3. **Omitted Variable Bias**: Success is influenced by both observable factors (funding, team experience) and unobservable factors (luck, timing, network effects). Survivors likely have positive unobserved characteristics, creating correlation between predictors and the error term.

**The Ghost Data Required**

To implement a Heckman Correction, we need two specific types of "ghost data":

**Type 1: Selection Indicator for the Full Population**
- A binary indicator (selected = 1 if covered by TechCrunch, 0 otherwise) for ALL startups in the population, including those never covered
- This requires access to a comprehensive startup registry (e.g., Crunchbase, AngelList, state incorporation records) that captures both successful and failed ventures

**Type 2: Exclusion Restriction Variables**
- Variables that predict selection into the sample (TechCrunch coverage) but do NOT directly affect the outcome of interest (e.g., valuation, exit success)
- Examples: geographic proximity to tech journalists, founder social media following, PR budget, prior media mentions
- These variables affect visibility/coverage probability but are theoretically unrelated to fundamental business performance

**The Heckman Two-Step Process**

1. **Selection Equation**: Model Pr(covered by TechCrunch) using the full population and exclusion restriction variables
2. **Outcome Equation**: Model success metrics for covered startups, controlling for the Inverse Mills Ratio (λ) derived from step 1

The IMR corrects for the fact that covered startups are not a random sample—it adjusts for the correlation between being selected and having positive unobserved characteristics.

**Critical Limitation**: Without ghost data on failed/uncovered startups, the Heckman correction is impossible to implement. This is why survivorship bias is often intractable in practice—the "invisible graveyard" of failed ventures leaves no data trail.

## Key Takeaways
- Sampling methodology is not neutral—it encodes assumptions about the DGP that propagate through the entire ML pipeline
- Covariate shift can be eliminated through stratification, but selection bias requires modeling the selection mechanism itself
- A/B test validity depends on infrastructure integrity; statistical forensics can detect systematic assignment failures
- Real-world bias often stems from data we cannot observe (ghost data), requiring explicit modeling of the selection process

## Applications
- Experimental design auditing
- Training/test set construction for ML pipelines
- Causal inference in observational studies
- A/B testing platform validation
