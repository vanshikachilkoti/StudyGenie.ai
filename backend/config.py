# import os
# from dotenv import load_dotenv

# # Load the .env file
# load_dotenv()

# # GEMINI API
# HF_API_KEY = os.getenv("HF_API_KEY")

# # EMAIL (Gmail SMTP)
# EMAIL_USER = os.getenv("EMAIL_USER")
# EMAIL_PASS = os.getenv("EMAIL_PASS")

# # GOOGLE CALENDAR (optional)
# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")


import os
import streamlit as st
from dotenv import load_dotenv

# Load .env only if running locally
load_dotenv()

# GEMINI API
HF_API_KEY = st.secrets.get("HF_API_KEY", os.getenv("HF_API_KEY"))

# EMAIL (Gmail SMTP)
EMAIL_USER = st.secrets.get("EMAIL_USER", os.getenv("EMAIL_USER"))
EMAIL_PASS = st.secrets.get("EMAIL_PASS", os.getenv("EMAIL_PASS"))

# GOOGLE CALENDAR (optional)
GOOGLE_CLIENT_ID = st.secrets.get("GOOGLE_CLIENT_ID", os.getenv("GOOGLE_CLIENT_ID"))
GOOGLE_CLIENT_SECRET = st.secrets.get("GOOGLE_CLIENT_SECRET", os.getenv("GOOGLE_CLIENT_SECRET"))
GOOGLE_REDIRECT_URI = st.secrets.get("GOOGLE_REDIRECT_URI", os.getenv("GOOGLE_REDIRECT_URI"))
