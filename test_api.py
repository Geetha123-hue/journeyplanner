import google.generativeai as genai
import streamlit as st

# Get API Key from Streamlit Secrets
API_KEY = st.secrets["AIzaSyBqESoUYeXNYbS2BEMBtuArVZplvGyCy1A"]


if not API_KEY:
    print("⚠️ API Key is missing! Please check your .env file.")
    exit()

# Configure API
genai.configure(api_key=AIzaSyBqESoUYeXNYbS2BEMBtuArVZplvGyCy1A)

# Test API connectivity
try:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content("Give me a short travel recommendation for a trip from New York to Los Angeles.")
    
    if hasattr(response, "text"):
        print("✅ API is working! Response from Gemini API:")
        print(response.text)
    else:
        print("⚠️ No response generated by API.")

except Exception as e:
    print(f"❌ API connection failed: {e}")
