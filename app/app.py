import streamlit as st
import joblib
import numpy as  np

st.title("Customer Churn Predictor")
st.write("Model Used : Decision Tree")
model = joblib.load("models/model.pkl")
accuracy = joblib.load("models/accuracy.pkl")
st.write("Model Accuracy:", round(accuracy*100,2), "%")

st.divider()

st.subheader("Enter Customer Details")

senior = st.selectbox("Senior Citizen", [0,1])
partner = st.selectbox("Partner", [0,1])
dependents = st.selectbox("Dependents", [0,1])
tenure = st.number_input("Tenure")
internet = st.selectbox("Internet Service", [0,1,2])
security = st.selectbox("Online Security", [0,1])
contract = st.selectbox("Contract Type", [0,1,2])
payment = st.selectbox("Payment Method", [0,1,2,3])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

st.divider()

if st.button("Predict"):
    features = np.array([[
        senior,
        partner,
        dependents,
        tenure,
        internet,
        security,
        contract,
        payment,
        monthly,
        total
    ]])

    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")