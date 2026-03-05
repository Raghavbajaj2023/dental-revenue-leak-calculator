import streamlit as st
import pandas as pd
import requests

WEBHOOK_URL = "https://humanlesslab.app.n8n.cloud/webhook/dental-leak-lead"

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

website = st.text_input(
"Clinic Website (optional)"
)

weekly_calls = st.number_input(
"How many patient calls does your clinic receive per week?",
min_value=0,
value=120
)

missed_percentage = st.slider(
"What percentage of calls go unanswered or to voicemail?",
0,50,25
)

patient_value = st.number_input(
"Average revenue from a new patient ($)",
min_value=0,
value=1200
)

implant_value = st.number_input(
"Average value of implant / cosmetic cases ($)",
min_value=0,
value=4000
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

    implant_loss = missed_calls * 0.08 * implant_value

    st.subheader("Estimated Patient Revenue Leakage")

    col1,col2 = st.columns(2)

    col1.metric("Missed Calls Per Week", round(missed_calls))
    col2.metric("Lost Patients Per Week", round(lost_patients))

    col1.metric("Monthly Lost Revenue", f"${round(monthly_leak):,}")
    col2.metric("Annual Lost Revenue", f"${round(annual_leak):,}")

    st.warning(
    f"Based on your inputs, your clinic may be losing **${round(monthly_leak):,} per month** due to missed calls."
    )

    st.info(
    f"Potential implant / cosmetic opportunity loss could add **${round(implant_loss):,} per month**."
    )

    chart_data = pd.DataFrame({
        "Period":["Weekly","Monthly","Annual"],
        "Revenue Loss":[weekly_leak,monthly_leak,annual_leak]
    })

    st.bar_chart(chart_data.set_index("Period"))

    if monthly_leak > 50000:
        score = "High Revenue Leakage"
        st.error("Your clinic likely has significant patient leakage.")
    elif monthly_leak > 20000:
        score = "Medium Revenue Leakage"
        st.warning("Your clinic may be losing substantial patient revenue.")
    else:
        score = "Low Revenue Leakage"
        st.success("Your clinic leakage appears relatively low.")

st.divider()

st.header("Why Clinics Lose This Revenue")

st.write(
"""
Most dental clinics miss **20–30% of inbound patient calls** during:

• Busy treatment hours  
• Lunch breaks  
• After closing  

When patients cannot reach a clinic immediately, they often call the **next clinic listed on Google**.
"""
)

st.divider()

st.header("How Clinics Eliminate This Revenue Leakage")

st.write(
"""
HumanlessLab installs **24/7 AI voice systems** that answer every patient call instantly, qualify treatment inquiries, and automatically book appointments into your calendar.
"""
)

st.markdown(
"""
• Never miss a patient inquiry  
• Automatically recover missed calls  
• Capture after-hours patients  
• Increase booked appointments without more marketing
"""
)

st.divider()

st.header("Get a Free Revenue Leak Audit")

with st.form("lead_form"):

    name = st.text_input("Name")
    clinic = st.text_input("Clinic Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    patient_volume = st.text_input("Monthly Patient Volume")

    submitted = st.form_submit_button("Request Free Audit")

    if submitted:

        data = {
            "name":name,
            "clinic":clinic,
            "email":email,
            "phone":phone,
            "website":website,
            "weekly_calls":weekly_calls,
            "missed_percentage":missed_percentage,
            "patient_value":patient_value,
            "monthly_leak":monthly_leak if 'monthly_leak' in locals() else None,
            "annual_leak":annual_leak if 'annual_leak' in locals() else None,
            "lead_score":score if 'score' in locals() else None
        }

        try:
            requests.post(WEBHOOK_URL,json=data)
        except:
            pass

        st.success(
        "Thank you. Our team will review your clinic's call flow and send you a detailed revenue leak analysis."
        )

st.divider()

st.markdown(
"""
### HumanlessLab  
AI Voice Systems for Dental Clinics  

Helping clinics capture every patient opportunity.
"""
)

st.link_button(
"Schedule Consultation",
"https://humanlesslab.com"
)
