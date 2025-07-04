# utils/auth.py

import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.constants import SCOPE, SPREADSHEET_NAME
import streamlit as st

@st.cache_resource
def conectar_planilha():
    cred_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not cred_json:
        raise ValueError("⚠️ GOOGLE_CREDENTIALS_JSON not defined.")
    
    creds_dict = json.loads(cred_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
    client = gspread.authorize(creds)
    return client.open(SPREADSHEET_NAME).sheet1
