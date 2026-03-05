import streamlit as st

st.set_page_config(
    page_title="Dental Revenue Leak Calculator",
    layout="centered"
)

st.title("Dental Revenue Leak Calculator")

st.subheader(
    "Estimate how much monthly patient revenue your clinic may be losing due to missed calls."
)

st.divider()

st.header("Clinic Call Data")

weekly_calls = st.number_input(
    "How many patient calls does your clinic receive per week?",
    min_value=0,
    placeholder=120
)

missed_percentage = st.slider(
    "What percentage of calls go unanswered or to voicemail?",
    0,50,25
)

patient_value = st.number_input(
    "Average revenue from a new patient",
    min_value=0,
    placeholder=1200
)

implant_value = st.number_input(
    "Average value of implant / cosmetic cases (optional)",
    min_value=0,
    placeholder=4000
)

after_hours = st.selectbox(
    "Does your clinic answer calls after hours?",
    ["Yes","No"]
)

st.divider()

if st.button("Calculate Revenue Leakage"):

    missed_calls = weekly_calls * (missed_percentage / 100)

    lost_patients = missed_calls * 0.5

    weekly_leak = lost_patients * patient_value

    monthly_leak = weekly_leak * 4

    annual_leak = monthly_leak * 12

    st.success("Estimated Patient Revenue Leakage")

    st.metric("Missed Calls Per Week", round(missed_calls))
    st.metric("Lost Patients Per Week", round(lost_patients))
    st.metric("Estimated Monthly Lost Revenue", f"${round(monthly_leak):,}")
    st.metric("Estimated Annual Lost Revenue", f"${round(annual_leak):,}")

    st.write(
        f"Based on your inputs, your clinic may be losing approximately **${round(monthly_leak):,} per month** in potential patient revenue due to missed calls and delayed responses."
    )

st.divider()

st.header("Why This Happens")

st.write(
"""
Most dental clinics miss **20–30% of inbound patient calls** during busy hours,
lunch breaks, or after closing.

Many of these patients contact the **next clinic listed on Google**
instead of leaving voicemail.
"""
)

st.divider()

st.header("How Clinics Eliminate This Revenue Leakage")

st.write(
"""
HumanlessLab installs **24/7 AI voice systems** that answer every patient call instantly,
qualify treatment inquiries, and automatically book appointments into your calendar.
"""
)

st.markdown("""
• Never miss a patient inquiry again  
• Automatically recover missed calls  
• Capture after-hours patients  
• Increase booked appointments without more marketing
""")

st.divider()

st.header("Get a Free Revenue Leak Audit")

with st.form("audit_form"):

    name = st.text_input("Name")
    clinic = st.text_input("Clinic Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    website = st.text_input("Website")
    volume = st.text_input("Monthly Patient Volume")

    submit = st.form_submit_button("Submit")

    if submit:
        st.success(
            "Thank you. Our team will review your clinic's patient call flow and send you a detailed revenue leak analysis."
        )

st.divider()

st.markdown(
"""
### HumanlessLab  
AI Voice Systems for Dental Clinics  

Helping clinics capture every patient opportunity.
"""
)

st.link_button("Schedule Consultation", "https://humanlesslab.com")
