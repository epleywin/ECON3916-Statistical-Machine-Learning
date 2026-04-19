FedSpeak Analysis — NLP on FOMC Minutes
Objective: To quantify shifts in Federal Reserve communication tone and thematic structure across two decades of FOMC meeting minutes using natural language processing and unsupervised machine learning techniques.

Methodology

Corpus Preprocessing: Ingested raw FOMC meeting minutes and applied a standard NLP pipeline — tokenization, lemmatization, and stop word removal — to produce a clean, analysis-ready corpus.
Feature Engineering: Constructed a TF-IDF document-term matrix incorporating both unigrams and bigrams to capture single-term frequency signals alongside common phrase patterns in Fed communications.
Sentiment Scoring: Applied the Loughran-McDonald financial sentiment lexicon to derive two core metrics per document: net sentiment (positive minus negative tone) and uncertainty (prevalence of hedging and ambiguous language).
Trend Visualization: Plotted sentiment time series across 20+ years of minutes to surface macro-level shifts in Fed communication strategy.
Document Clustering: Reduced TF-IDF vectors via PCA and applied K-Means clustering to identify latent thematic regimes across the FOMC document corpus.
Pre/Post-COVID Comparison: Conducted distributional analysis of sentiment scores segmented at March 2020 to isolate the communicative impact of the pandemic shock.


Key Findings
The analysis reveals a statistically meaningful shift in FOMC communication following the onset of COVID-19. Mean net sentiment declines noticeably in the post-March 2020 period, consistent with the Fed adopting more guarded and less optimistic policy language in response to acute macroeconomic disruption.
Notably, uncertainty scores do not rise commensurately — a counterintuitive result suggesting that while the valence of Fed communication turned more negative, the clarity and control of policy messaging was largely preserved. This pattern is consistent with forward guidance discipline: rather than signaling confusion, the Fed appeared to communicate deteriorating conditions in a measured and deliberate register.