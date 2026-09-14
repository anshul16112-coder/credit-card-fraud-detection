import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict whether the transaction is fraudulent.")

# Input fields
amt = st.number_input("Transaction Amount", min_value=0.0, value=100.0)

merchant = st.number_input("Merchant Code", min_value=0, value=0)
category = st.number_input("Category Code", min_value=0, value=0)
gender = st.number_input("Gender Code", min_value=0, value=0)
state = st.number_input("State Code", min_value=0, value=0)
job = st.number_input("Job Code", min_value=0, value=0)

lat = st.number_input("Customer Latitude", value=0.0)
long = st.number_input("Customer Longitude", value=0.0)
city_pop = st.number_input("City Population", min_value=0, value=1000)

merch_lat = st.number_input("Merchant Latitude", value=0.0)
merch_long = st.number_input("Merchant Longitude", value=0.0)

transaction_year = st.number_input(
    "Transaction Year", min_value=2000, max_value=2100, value=2026
)
transaction_month = st.number_input(
    "Transaction Month", min_value=1, max_value=12, value=1
)
transaction_day = st.number_input(
    "Transaction Day", min_value=1, max_value=31, value=1
)
transaction_hour = st.number_input(
    "Transaction Hour", min_value=0, max_value=23, value=12
)

birth_year = st.number_input(
    "Birth Year", min_value=1900, max_value=2026, value=1990
)
birth_month = st.number_input(
    "Birth Month", min_value=1, max_value=12, value=1
)
birth_day = st.number_input(
    "Birth Day", min_value=1, max_value=31, value=1
)

if st.button("🔍 Check Transaction"):

    # Create input in same feature order as training data
    input_data = pd.DataFrame([{
        "Unnamed: 0": 0,
        "cc_num": 0,
        "merchant": merchant,
        "category": category,
        "amt": amt,
        "gender": gender,
        "state": state,
        "zip": 0,
        "lat": lat,
        "long": long,
        "city_pop": city_pop,
        "job": job,
        "unix_time": 0,
        "merch_lat": merch_lat,
        "merch_long": merch_long,
        "transaction_year": transaction_year,
        "transaction_month": transaction_month,
        "transaction_day": transaction_day,
        "transaction_hour": transaction_hour,
        "birth_year": birth_year,
        "birth_month": birth_month,
        "birth_day": birth_day
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 FRAUDULENT TRANSACTION")
    else:
        st.success("✅ GENUINE TRANSACTION")