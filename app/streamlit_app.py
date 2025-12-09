import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import uuid
from datetime import datetime

import streamlit as st

from db.mongo import get_transactions_collection

st.set_page_config(page_title="FraudShield AI", layout="wide")

st.title("🚨 FraudShield AI")
st.subheader("Real-Time Financial Fraud Detection System")

st.write(
    "This is the starting version of your project. "
    "Soon this app will show live transactions and fraud alerts in real-time."
)

st.markdown("### 🔹 Simulate a Transaction")

amount = st.number_input("Transaction Amount (LKR)", min_value=0.0, step=100.0)
country = st.text_input("Country", value="Sri Lanka")
time_of_day = st.selectbox("Time of Transaction", ["Morning", "Afternoon", "Evening", "Night"])

if st.button("Save Transaction to Database"):
    transactions_col = get_transactions_collection()

    transaction_doc = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": "demo_user_001",  # later we can make this dynamic
        "amount_lkr": float(amount),
        "country": country,
        "time_of_day": time_of_day,
        "channel": "ONLINE",  # for now fixed
        "created_at": datetime.utcnow(),
        "model_prediction": None,   # later we will fill this
        "risk_score": None,         # later we will fill this
        "is_fraud_label": None,     # for manual feedback later
    }

    try:
        result = transactions_col.insert_one(transaction_doc)
        st.success(f"Transaction saved! MongoDB _id: {result.inserted_id}")
        st.json(transaction_doc)
    except Exception as e:
        st.error(f"Error saving transaction: {e}")
