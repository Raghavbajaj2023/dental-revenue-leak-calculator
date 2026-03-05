import streamlit as st
import requests
import pandas as pd

WEBHOOK_URL = "https://humanlesslab.app.n8n.cloud/webhook/dental-ai-audit"

st.set_page_config(
    page_title="Dental Revenue Leak Calculator",
    page_icon="🦷",
    layout="centered"
)

# ------------------------------------------------
# PREMIUM CSS
# ------------------------------------------------

st.markdown("""
<style>

body {
background: linear-gradient(135deg,#0f172a,#020617);
}

.block-container{
max-width:900px;
padding-top:2rem;
}

.glass{
background: rgba(30,41,59,0.6);
backdrop-filter: blur(20px);
padding:35px;
border-radius:16px;
margin-bottom:25px;
border:1px solid rgba(255,255,255,0.08);
}

.hero{
text-align:center;
margin-bottom:50px;
}

.big-number{
font-size:64px;
font-weight:800;
color:#ef4444;
text-align:center;
}

.metric-box{
background: rgba(30,41,59,0.7);
padding:20px;
border-radius:12px;
}

.stButton>button{
background:#2563eb;
color:white;
border-radius:10px;
height:52px;
font-size:18px;
font-weight:600;
width:100%;
border:none;
}

.stButton>button:hover{
background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HERO
# ------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🦷 Dental Revenue Leak Calculator</h1>

<p style="font-size:20px;color:#94a3b8">
Discover how much patient revenue your clinic may be losing from missed calls.
</p>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# CLINIC INFO
# ------------------------------------------------

st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("Clinic Information")

name = st.text_input("Your Name")
clinic = st.text_input("Clinic Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
website = st.text_input("Clinic Website")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# CALL DATA
# ------------------------------------------------

st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("Clinic Call Data")

weekly_calls = st.number_input(
"Weekly patient calls",
min_value=0,
value=120
)

missed_percentage = st.slider(
"Missed call percentage",
0,50,25
)

patient_value = st.number_input(
"Average revenue per new patient ($)",
min_value=0,
value=1200
)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# CALCULATE
# ------------------------------------------------

if st.button("Calculate Revenue Leakage"):

    missed_calls = weekly_calls * (missed_percentage / 100)

    lost_patients = missed_calls * 0.5

    weekly_leak = lost_patients * patient_value
    monthly_leak = weekly_leak * 4
    annual_leak = monthly_leak * 12

    # BIG RESULT
    st.markdown(f"""
    <div class="glass">

    <h2 style="text-align:center">Estimated Monthly Revenue Loss</h2>

    <div class="big-number">${round(monthly_leak):,}</div>

    <p style="text-align:center;color:#94a3b8">
    Your clinic may be losing significant patient revenue from missed calls.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        st.metric("Missed Calls / Week", round(missed_calls))
        st.metric("Lost Patients / Week", round(lost_patients))

    with col2:
        st.metric("Monthly Lost Revenue", f"${round(monthly_leak):,}")
        st.metric("Annual Lost Revenue", f"${round(annual_leak):,}")

    # ------------------------------------------------
    # CHART
    # ------------------------------------------------

    data = pd.DataFrame({
        "Period":["Weekly","Monthly","Annual"],
        "Revenue Loss":[weekly_leak,monthly_leak,annual_leak]
    })

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Revenue Loss Breakdown")

    st.bar_chart(data.set_index("Period"))

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------
    # AUDIT CTA
    # ------------------------------------------------

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("Get Your Free AI Revenue Leak Audit")

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
            requests.post(WEBHOOK_URL, json=data)

            st.success(
            "Your audit request has been submitted. We will send your detailed report shortly."
            )

        except:
            st.error("Audit request failed.")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# EDUCATION
# ------------------------------------------------

st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("Why Dental Clinics Lose Revenue")

st.write("""
Most dental clinics miss **20–30% of patient calls** during:

• Busy treatment hours  
• Lunch breaks  
• After closing  

Patients often call the **next clinic listed on Google** instead of leaving voicemail.
""")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# SOLUTION
# ------------------------------------------------

st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("How Clinics Eliminate This Revenue Leakage")

st.write("""
HumanlessLab installs **24/7 AI voice systems** that answer every patient call instantly, qualify treatment inquiries, and automatically book appointments.
""")

st.markdown("""
✔ Never miss patient inquiries  
✔ Recover missed calls automatically  
✔ Capture after-hours patients  
✔ Increase booked appointments without extra marketing
""")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("---")

st.markdown("""
### HumanlessLab  
AI Voice Systems for Dental Clinics  

Helping clinics capture every patient opportunity.
""")

st.link_button("Schedule Consultation","https://humanlesslab.com")
