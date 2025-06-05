
import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("loan_comparison.xlsx", engine="openpyxl")

# Streamlit app
st.title("🎓 Student Loan Comparison Dashboard")

# Dropdown for tax bracket selection
tax_bracket = st.selectbox("Select Your Tax Bracket (%)", [12, 22, 32])

# Add tax-adjusted interest column
df["Tax-Adjusted Interest"] = df[f"Tax-Adjusted Interest ({tax_bracket}%)"]

# Display the filtered table
st.subheader("Loan Comparison Table")
st.dataframe(df[[
    "Loan Type", "Amount", "Rate (%)", "Term (years)",
    "Monthly Payment", "Total Repayment", "Total Interest", "Tax-Adjusted Interest"
]])

# Optional: Download button
st.download_button(
    label="📥 Download Full Comparison (Excel)",
    data=open("loan_comparison.xlsx", "rb").read(),
    file_name="loan_comparison.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
