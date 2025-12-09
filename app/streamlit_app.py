import streamlit as st

st.set_page_config(page_title="FraudShield AI", layout="wide")

st.title("FraudShield AI")
st.subheader("Real-Time Financial Fraud Detection System")

st.write(
    "This is the starting version of your project. "
    "Soon this app will show live transactions and fraud alerts in real-time."
)

amount = st.number_input("Transaction Amount (LKR)", min_value=0.0, step=100.0)
country = st.text_input("Country", value="Sri Lanka")
time_of_day = st.selectbox("Time of Transaction", ["Morning", "Afternoon", "Evening", "Night"])

if st.button("Simulate Prediction"):
    st.info("For now, the model is not trained yet. This button will later call the ML model.")
    st.json(
        {
            "amount": amount,
            "country": country,
            "time_of_day": time_of_day,
            "predicted_label": "NORMAL (placeholder)",
            "risk_score": 12,
        }
    )
