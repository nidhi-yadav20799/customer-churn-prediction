import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction"
)

st.title("Customer Churn Prediction App")

st.write("""
This machine learning application predicts customer churn using telecom customer data.
""")

tenure = st.slider("Tenure", 0, 72, 12)

monthly_charges = st.slider(
    "Monthly Charges",
    0,
    150,
    70
)

if st.button("Predict"):

    st.success(
        "Prediction model can be connected here."
    )
