import streamlit as st
import requests

WEBHOOK_URL = "https://humanlesslab.app.n8n.cloud/webhook/dental-ai-audit"

st.set_page_config(
    page_title="Dental Revenue Leak Calculator",
    page_icon="🦷",
    layout="centered"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

body {
background-color:#0f172a;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
max-width:900px;
}

.section{
background:#1e293b;
padding:35px;
border-radius:14px;
margin-bottom:25px;
box-shadow:0px 15px 40px rgba(0,0,0,0.3);
}

.result-box{
background:#1e293b;
padding:40px;
border-radius:16px;
text-align:center;
margin-bottom:30px;
}

.big-number{
font-size:48px;
font-weight:800;
color:#ef4444;
}

.stButton>button{
background:#2563eb;
color:white;
border-radius:10px;
height:50px;
font-size:18px;
font-weight:600;
border:none;
width:100%;
}

.stButton>button:hover{
background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO
# -------------------------

st.markdown("""
<div style='text-align:center;margin-bottom:50px'>

<h1>🦷 Dental Revenue Leak Calculator</h1>

<p style='font-size:20px;color:#94a3b8'>
Estimate how much monthly patient revenue your clinic may be losing due to missed calls.
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------
# CLINIC INFO
# -------------------------

st.markdown("<div class='section'>", unsafe_allow_html=True)

st.subheader("Clinic Information")

name = st.text_input("Your Name")
clinic = st.text_input("Clinic Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
website = st.text_input("Clinic Website (optional)")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# CALL DATA
# -------------------------

st.markdown("<div class='section'>", unsafe_allow_html=True)

st.subheader("Clinic Call Data")

weekly_calls = st.number_input(
"How many patient calls does your clinic receive per week?",
min_value=0,
value=120
)

missed_percentage = st.slider(
"What percentage of calls go unanswered or go to voicemail?",
0,50,25
)

patient_value = st.number_input(
"Average revenue from a new patient ($)",
min_value=0,
value=1200
)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# CALCULATE
# -------------------------

if st.button("Calculate Revenue Leakage"):

    missed_calls = weekly_calls * (missed_percentage / 100)

    lost_patients = missed_calls * 0.5

    weekly_leak = lost_patients * patient_value

    monthly_leak = weekly_leak * 4

    annual_leak = monthly_leak * 12

    st.markdown(f"""
    <div class='result-box'>

    <h2>Estimated Monthly Revenue Loss</h2>

    <div class='big-number'>${round(monthly_leak):,}</div>

    <p style='color:#94a3b8'>
    Your clinic may be losing significant patient revenue from missed calls.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Missed Calls / Week", round(missed_calls))
        st.metric("Lost Patients / Week", round(lost_patients))

    with col2:
        st.metric("Monthly Lost Revenue", f"${round(monthly_leak):,}")
        st.metric("Annual Lost Revenue", f"${round(annual_leak):,}")

    # -------------------------
    # FREE AUDIT CTA
    # -------------------------

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.subheader("Get Your Free AI Revenue Leak Audit")

    if st.button("Request Free Audit"):

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

            requests.post(WEBHOOK_URL, json=data)

            st.success(
            "Your audit request has been submitted. We will send your detailed report shortly."
            )

        except:

            st.error("There was an error submitting the audit request.")

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# EDUCATION
# -------------------------

st.markdown("<div class='section'>", unsafe_allow_html=True)

st.subheader("Why Dental Clinics Lose Revenue")

st.write("""
Most dental clinics miss **20–30% of inbound patient calls** during:

• Busy treatment hours  
• Lunch breaks  
• After closing  

Many patients simply call the **next clinic listed on Google** instead of leaving voicemail.
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# SOLUTION
# -------------------------

st.markdown("<div class='section'>", unsafe_allow_html=True)

st.subheader("How Clinics Eliminate This Revenue Leakage")

st.write("""
HumanlessLab installs **24/7 AI voice systems** that answer every patient call instantly, qualify treatment inquiries, and automatically book appointments.
""")

st.markdown("""
• Never miss a patient inquiry  
• Automatically recover missed calls  
• Capture after-hours patients  
• Increase booked appointments without more marketing
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.markdown("""
### HumanlessLab  
AI Voice Systems for Dental Clinics  

Helping clinics capture every patient opportunity.
""")

st.link_button("Schedule Consultation", "https://humanlesslab.com")
