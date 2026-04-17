import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

model = joblib.load("model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("Financial Crisis Risk Predictor")
st.markdown(
    """
    This app uses a Random Forest model to estimate the risk that a country-year observation
    will be associated with a systemic financial crisis based on macroeconomic indicators.
    """
)

st.sidebar.header("Enter Economic Indicators")

year = st.sidebar.number_input("Year", min_value=1800, max_value=2025, value=2000, step=1)
exch_usd = st.sidebar.number_input("Exchange Rate (USD)", min_value=0.0, value=1.0, step=0.1)
inflation = st.sidebar.number_input("Inflation Rate", value=5.0, step=0.1)
gdp_weighted_default = st.sidebar.number_input("GDP-Weighted Default", min_value=0.0, value=0.0, step=0.1)
domestic_debt_default = st.sidebar.selectbox("Domestic Debt in Default", [0, 1])
external_debt_default = st.sidebar.selectbox("External Debt Default", [0, 1])
gold_standard = st.sidebar.selectbox("Gold Standard", [0, 1])
independence = st.sidebar.selectbox("Independent Country", [0, 1])
currency_crises = st.sidebar.selectbox("Currency Crises", [0, 1, 2])
inflation_crises = st.sidebar.selectbox("Inflation Crises", [0, 1])

input_data = pd.DataFrame([{
    'year': year,
    'exch_usd': exch_usd,
    'inflation_annual_percentages_of_average_consumer_prices': inflation,
    'gdp_weighted_default': gdp_weighted_default,
    'domestic_debt_in_default': domestic_debt_default,
    'sovereign_external_debt_2_default_and_restructurings_1800_2012_does_not_include_defaults_on_wwi_debt_to_united_states_and_united_kingdom_but_includes_post_1975_defaults_on_official_external_creditors': external_debt_default,
    'gold_standard': gold_standard,
    'independence': independence,
    'currency_crises': currency_crises,
    'inflation_crises': inflation_crises
}])

input_data = input_data[feature_names]

prediction = model.predict(input_data)[0]
prediction_proba = model.predict_proba(input_data)[0][1]

st.subheader("Prediction Result")

if prediction == 1:
    st.error(f"Predicted outcome: Crisis")
else:
    st.success(f"Predicted outcome: No Crisis")

st.metric("Predicted Crisis Probability", f"{prediction_proba:.2%}")

lower_bound = max(0, prediction_proba - 0.06)
upper_bound = min(1, prediction_proba + 0.06)
st.write(f"Approximate uncertainty range: {lower_bound:.2%} to {upper_bound:.2%}")

st.caption(
    "This range is a simple approximation based on cross-validation variability, not a formal confidence interval."
)

st.subheader("Input Profile")

plot_data = pd.Series({
    "Inflation": inflation,
    "Exchange Rate": exch_usd,
    "GDP Default": gdp_weighted_default,
    "Currency Crises": currency_crises,
    "Inflation Crises": inflation_crises
})

fig, ax = plt.subplots(figsize=(8, 4))
plot_data.plot(kind="bar", ax=ax)
ax.set_ylabel("Value")
ax.set_title("Selected Economic Inputs")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

st.subheader("Model Context")
st.write(
    "In the trained model, inflation and exchange rates were among the most important predictive variables."
)