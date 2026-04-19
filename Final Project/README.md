# Financial Crisis Risk Predictor

This project builds a machine learning model to predict the likelihood of a systemic financial crisis using historical macroeconomic data. The goal is not to explain *why* crises happen, but to identify patterns that signal elevated risk and support better decision-making.

---

## 📊 Project Overview

Financial crises are rare but extremely costly events. This project uses a Random Forest classification model to estimate the probability that a country-year observation will experience a systemic crisis.

The model is deployed through an interactive Streamlit dashboard, where users can adjust economic indicators and see how predicted crisis risk changes in real time.

---

## ❓ Prediction Question

**Can we predict whether a country will experience a systemic financial crisis based on macroeconomic indicators?**

This is a **prediction problem**, not a causal one. The model is designed to forecast outcomes based on patterns in the data, not to determine cause-and-effect relationships.

---

## 🧠 Model

- **Baseline Model:** Logistic Regression  
- **Final Model:** Random Forest Classifier  

The Random Forest model was chosen because it performed better at identifying crisis events, especially given the class imbalance in the dataset.

---

## 📁 Dataset

- **Source:** Global Financial Crisis Dataset (historical country-year data)  
- **Observations:** 15,190  
- **Target Variable:** `systemic_crisis` (binary: 0 = no crisis, 1 = crisis)  

The dataset includes variables such as:
- inflation rates  
- exchange rates  
- debt default indicators  
- currency crises  
- independence status  

---

## ⚠️ Key Challenges

- **Class imbalance:** Crisis events are rare, making them harder to predict  
- **Missing data:** Some macroeconomic indicators were incomplete and required imputation  
- **Outliers:** Variables like inflation had extreme values that skewed distributions  

---

## 📈 Results

The Random Forest model achieved significantly better performance than the baseline, particularly in identifying crisis events.

However, even the best model struggles with recall, meaning some crises are still missed. This reflects the inherent difficulty of predicting rare economic shocks.

---

## 💡 Interpretation

This model should be viewed as a **risk assessment tool**, not a definitive predictor.

- A higher predicted probability = higher risk signal  
- A lower probability = lower observed risk based on historical patterns  

**Important:** Feature importance reflects predictive relationships, not causal effects.

---

## 🌐 Streamlit App

The project is deployed as an interactive dashboard:

👉 https://financial-crisis-predictor-nwpvtxybhfcrlpecfbaqra.streamlit.app

Users can:
- adjust economic indicators  
- view predicted crisis probability  
- see how risk changes dynamically  

---

## 🛠️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/epleywin/financial-crisis-predictor.git
cd financial-crisis-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Repository Structure

```
app.py
model.pkl
feature_names.pkl
requirements.txt
3916-final-project-starter.ipynb
```

---

## ⚠️ Limitations

- The model is purely predictive and does not establish causality  
- Performance is constrained by class imbalance and data quality  
- Predictions should be interpreted with caution, especially in high-stakes decisions  

---

## 🚀 Final Takeaway

Even with modern machine learning, predicting financial crises remains difficult. However, this model provides a structured way to quantify risk and identify patterns that may not be obvious at first glance.

It is best used as a **decision support tool**, not a standalone answer.