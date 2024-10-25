import streamlit as st

# Title of the page
st.title("Loan Approval Prediction")

# Encodings for categorical variables
gender_mapping = {"Male": 1, "Female": 0}
marital_status_mapping = {"Married": 0, "Single": 1}
education_mapping = {"High School": 0, "Bachelor's": 1, "Master's": 2}
credit_history_mapping = {"Good": 0, "Poor": 1}
property_area_mapping = {"Urban": 1, "Rural": 0}

# 4x4 grid layout with columns
col1, col2, col3, col4 = st.columns(4)

# Categorical columns with dropdowns and encoding
with col1:
    gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
    gender_encoded = gender_mapping[gender]

    marital_status = st.selectbox("Marital Status", options=["Married", "Single"], index=0)
    marital_status_encoded = marital_status_mapping[marital_status]

with col2:
    dependents = st.number_input("Dependents", min_value=0, step=1)

    education = st.selectbox("Education", options=["High School", "Bachelor's", "Master's"], index=0)
    education_encoded = education_mapping[education]

with col3:
    self_employed = st.selectbox("Self-Employed", options=["Yes", "No"], index=1)
    self_employed_encoded = 1 if self_employed == "Yes" else 0

    applicant_income = st.number_input("Applicant Income (Dollars)", min_value=0, step=1000)

with col4:
    co_applicant_income = st.number_input("Co-Applicant Income (Dollars)", min_value=0, step=1000)
    loan_amount = st.number_input("Loan Amount (Dollars)", min_value=0, step=1000)

# Another row for Loan Term, Credit History, Property Area
col5, col6, col7, col8 = st.columns(4)

with col5:
    loan_term = st.number_input("Loan Term (Months)", min_value=0, step=1)

with col6:
    credit_history = st.selectbox("Credit History", options=["Good", "Poor"], index=0)
    credit_history_encoded = credit_history_mapping[credit_history]

with col7:
    property_area = st.selectbox("Property Area", options=["Urban", "Rural"], index=0)
    property_area_encoded = property_area_mapping[property_area]

# Calculating Income-to-Loan Ratio and Income per Term
with col8:
    total_income = applicant_income + co_applicant_income
    income_to_loan_ratio = total_income / loan_amount if loan_amount > 0 else 0
    income_per_term = total_income / loan_term if loan_term > 0 else 0

    st.write(f"Income-to-Loan Ratio: {income_to_loan_ratio:.2f}")
    st.write(f"Total Income: {total_income:.2f}")
    st.write(f"Income per Term: {income_per_term:.2f}")

# Submit button to predict loan approval
if st.button("Predict"):
    # You can now use these encoded values for machine learning prediction
    data = {
        "Gender": gender_encoded,
        "Marital Status": marital_status_encoded,
        "Dependents": dependents,
        "Education": education_encoded,
        "Self-Employed": self_employed_encoded,
        "Applicant Income": applicant_income,
        "Co-Applicant Income": co_applicant_income,
        "Loan Amount": loan_amount,
        "Loan Term": loan_term,
        "Credit History": credit_history_encoded,
        "Property Area": property_area_encoded,
        "Income-to-Loan Ratio": income_to_loan_ratio,
        "Total Income": total_income,
        "Income per Term": income_per_term
    }
    
    # Show the encoded data
    st.write("Encoded data for model prediction:", data)

    # Placeholder for prediction logic
    st.success("Prediction submitted for processing.")