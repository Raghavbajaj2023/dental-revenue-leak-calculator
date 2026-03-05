import streamlit as st
import requests
import json

WEBHOOK_URL = "https://humanlesslab.app.n8n.cloud/webhook/dental-ai-audit"

st.title("Webhook Test Tool")

st.write("This tool sends a test request to your n8n webhook.")

if st.button("Send Test Webhook"):

    payload = {
        "name": "Test Dentist",
        "clinic": "Demo Dental",
        "email": "test@email.com",
        "phone": "1234567890",
        "website": "https://example.com",
        "weekly_calls": 100,
        "missed_percentage": 25,
        "patient_value": 1200,
        "monthly_leak": 30000
    }

    try:

        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        st.write("Status Code:", response.status_code)

        try:
            st.json(response.json())
        except:
            st.text(response.text)

    except Exception as e:
        st.error("Error occurred")
        st.write(str(e))
