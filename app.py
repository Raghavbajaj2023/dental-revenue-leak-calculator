import streamlit as st
import requests

# -----------------------------------
# CONFIG
# -----------------------------------

WEBHOOK_URL = "https://humanlesslab.app.n8n.cloud/webhook/dental-ai-audit"

st.set_page_config(
    page_title="Dental Revenue Leak Calculator",
    page_icon="🦷",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🦷 Dental Revenue Leak Calculator")

st.write(
"Estimate how much patient revenue your clinic may be losing due to missed calls."
)

# -----------------------------------
# CLINIC INFORMATION
# -----------------------------------

st.header("Clinic Information")

name = st.text_input("Your Name")
clinic = st.text_input("Clinic Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
website = st.text_input("Clinic Website")

# -----------------------------------
# CALL DATA
# -----------------------------------

st.header("Clinic Call Data")

weekly_calls = st.number_input(
"Weekly patient calls",
min_value=0,
value=120
)

missed_percentage = st.slider(
"Missed call percentage",
0,
50,
25
)

patient_value = st.number_input(
"Average revenue per new patient ($)",
min_value=0,
value=1200
)

# -----------------------------------
# CALCULATE
# -----------------------------------

if st.button("Calculate Revenue Leakage"):

    missed_calls = weekly_calls * (missed_percentage / 100)
    lost_patients = missed_calls * 0.5

    weekly_leak = lost_patients * patient_value
    monthly_leak = weekly_leak * 4
    annual_leak = monthly_leak * 12

    st.subheader("Estimated Revenue Loss")

    st.metric("Missed Calls / Week", round(missed_calls))
    st.metric("Lost Patients / Week", round(lost_patients))
    st.metric("Monthly Revenue Lost", f"${round(monthly_leak):,}")
    st.metric("Annual Revenue Lost", f"${round(annual_leak):,}")

    st.warning(
        f"Your clinic may be losing about **${round(monthly_leak):,} per month** due to missed calls."
    )

    # -----------------------------------
    # SEND TO N8N
    # -----------------------------------

    if st.button("Request Free AI Audit"):

        data = {
            "name": name,
            "clinic": clinic,
            "email": email,
            "phone": phone,
            "website": website,
            "weekly_calls": weekly_calls,
            "missed_percentage": missed_percentage,
            "patient_value": patient_value,
            "monthly_leak": monthly_leak
        }

        try:

            response = requests.post(
                WEBHOOK_URL,
                json=data,
                headers={"Content-Type": "application/json"}
            )

            st.write("Webhook Status:", response.status_code)
            st.write("Webhook Response:", response.text)

            if response.status_code == 200:

                st.success(
                "Your audit request has been submitted successfully."
                )

            else:

                st.error("Webhook request failed.")

        except Exception as e:

            st.error("Error sending request")
            st.write(e)

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.write(
"HumanlessLab — AI Voice Systems for Dental Clinics"
)
