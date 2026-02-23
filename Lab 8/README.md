# Hypothesis Testing & Causal Evidence Architecture
### The Epistemology of Falsification: Hypothesis Testing on the Lalonde Dataset

---

## Objective

Most applied ML workflows optimize for estimation — minimizing loss, maximizing predictive accuracy. This project takes a deliberate step back and asks a harder question: *how do we know if a measured effect is real?*

Using the Lalonde (1986) experimental dataset, I operationalized the scientific method as a causal adjudication framework — shifting the analytical posture from "what is the effect?" to "can we falsify the claim that no effect exists?" The result is a rigorous, evidence-backed estimate of the Average Treatment Effect (ATE) of job training on real earnings.

---

## Technical Approach

- **Signal-to-Noise Quantification:** Computed the ATE as a difference-in-means between treatment and control groups, then stress-tested that signal using Welch's T-Test (`scipy.stats.ttest_ind`, `equal_var=False`) — selected specifically to account for unequal variance across earnings distributions, a common real-world violation of standard T-Test assumptions.

- **Non-Parametric Validation via Permutation Testing:** To guard against the normality assumptions baked into parametric tests, I ran a 10,000-resample Permutation Test (`scipy.stats.permutation_test`) — directly simulating the null world where treatment labels are meaningless. Convergence between the parametric and non-parametric p-values strengthens confidence in the result.

- **Type I Error Control:** All hypothesis tests were evaluated against a pre-specified significance threshold (α = 0.05), enforcing a disciplined decision boundary and protecting against false positives driven by multiple comparisons or data dredging.

---

## Key Findings

A statistically significant lift of **~$1,795 in real earnings (re78)** was detected in the treatment group, with the Null Hypothesis rejected under both the parametric and non-parametric frameworks — consistent with Lalonde's original findings.

---

## Business Insight

In production data environments, the ability to generate a compelling-looking metric is trivially easy. The ability to *defend* that metric under scrutiny is not.

Rigorous hypothesis testing functions as the **safety valve of the algorithmic economy** — the institutional check that separates genuine causal signal from spurious correlation dressed up as insight. Without it, organizations risk optimizing against noise: shipping features that don't move the needle, running campaigns that cannibalize organic lift, or allocating capital based on p-hacked dashboards.

The framework built here — parametric estimation validated by non-parametric falsification — is the same architecture that underpins A/B testing infrastructure at scale. The Lalonde dataset is the "Hello World." The discipline is transferable everywhere.

Netflix's Return-Aware Experimentation framework reframes A/B testing from a scientific truth-seeking exercise into a business returns optimization problem — explicitly treating experiments as tools for helping organizations make good decisions that lift business metrics over time, rather than for testing scientific theories. Medium The key departure from the academic p < 0.05 standard is that the threshold itself becomes a variable to be optimized: while scientists are rightly driven to prevent false discoveries from entering the scientific record, businesses may be more tolerant of false discoveries as long as more true discoveries are unearthed. Medium In practice, this means the "right" significance threshold is a function of implementation costs, expected effect sizes, and opportunity costs — not a universal constant. I understand that α = 0.05 is a useful scientific convention, but in production environments, decision thresholds are business parameters that should be calibrated to the specific cost-benefit structure of each decision.
