import streamlit as st
import requests
import pandas as pd
import time

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
max-width:850px;
padding-top:2rem;
}

.glass-card{
background: rgba(30,41,59,0.65);
backdrop-filter: blur(18px);
border-radius:14px;
padding:28px;
margin-bottom:22px;
border:1px solid rgba(255,255,255,0.05);
}

.hero{
text-align:center;
margin-bottom:40px;
}

.big-number{
font-size:60px;
font-weight:800;
color:#ef4444;
text-align:center;
margin-bottom:10px;
}

.stButton>button{
background:#2563eb;
color:white;
border-radius:10px;
height:50px;
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

<p style="font-size:18px;color:#94a3b8">
Discover how much patient revenue your clinic may be losing from missed calls.
</p>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# CLINIC INFO
# ------------------------------------------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader("Clinic Information")

name = st.text_input("Your Name")
clinic = st.text_input("Clinic Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
website = st.text_input("Clinic Website")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# CALL DATA
# ------------------------------------------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# CALCULATE BUTTON
# ------------------------------------------------

if st.button("Analyze Revenue Leakage"):

    # AI analysis animation

    progress = st.progress(0)

    status = st.empty()

    steps = [
        "Scanning clinic call patterns...",
        "Analyzing missed call probability...",
        "Estimating patient revenue impact...",
        "Generating audit report..."
    ]

    for i in range(4):
        status.info(steps[i])
        progress.progress((i+1)*25)
        time.sleep(1)

    status.success("Analysis Complete")

    # ------------------------------------------------
    # CALCULATIONS
    # ------------------------------------------------

    missed_calls = weekly_calls * (missed_percentage / 100)
    lost_patients = missed_calls * 0.5

    weekly_leak = lost_patients * patient_value
    monthly_leak = weekly_leak * 4
    annual_leak = monthly_leak * 12

    # ------------------------------------------------
    # ANIMATED COUNTER
    # ------------------------------------------------

    placeholder = st.empty()

    for x in range(0, int(monthly_leak)+1, max(1,int(monthly_leak/30))):

        placeholder.markdown(f"""
        <div class="glass-card">

        <h2 style="text-align:center">Estimated Monthly Revenue Loss</h2>

        <div class="big-number">${x:,}</div>

        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.03)

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Missed Calls / Week", round(missed_calls))
        st.metric("Lost Patients / Week", round(lost_patients))

    with col2:
        st.metric("Monthly Revenue Lost", f"${round(monthly_leak):,}")
        st.metric("Annual Revenue Lost", f"${round(annual_leak):,}")

    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------
    # CHART
    # ------------------------------------------------

    data = pd.DataFrame({
        "Period":["Weekly","Monthly","Annual"],
        "Revenue":[weekly_leak,monthly_leak,annual_leak]
    })

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("Revenue Loss Breakdown")

    st.bar_chart(data.set_index("Period"))

    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------
    # AI SUMMARY
    # ------------------------------------------------

    st.markdown("""
    <div class="glass-card">

    <h3>AI Revenue Leak Summary</h3>

    • Missed patient calls are likely causing revenue leakage.  
    • Many patients will contact competing clinics instead.  
    • High-value treatments like implants or cosmetic dentistry may also be lost.

    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # RISK LEVEL
    # ------------------------------------------------

    risk = "LOW"

    if monthly_leak > 50000:
        risk = "HIGH"
    elif monthly_leak > 20000:
        risk = "MEDIUM"

    st.markdown(f"""
    <div class="glass-card">

    <h3>Patient Leakage Risk</h3>

    <h1 style="color:#ef4444;text-align:center">{risk}</h1>

    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # CTA
    # ------------------------------------------------

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

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
            "Your audit request was submitted. Our team will send your detailed report shortly."
            )

        except:

            st.error("Failed to submit audit request.")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# EDUCATION
# ------------------------------------------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader("Why Dental Clinics Lose Revenue")

st.write("""
Most dental clinics miss **20–30% of inbound patient calls** during:

• Busy treatment hours  
• Lunch breaks  
• After closing  

Many patients simply call the **next clinic listed on Google** instead of leaving voicemail.
""")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# SOLUTION
# ------------------------------------------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)

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
