# app.py

import streamlit as st
import re
from utils.auth import conectar_planilha
from utils.sheets import preencher_planilha

st.set_page_config(page_title="PTO Populator", layout="centered")

st.title("🗓️ Fill in Vacation/Absence in the Spreadsheet")
st.markdown("Paste the data below (starting with the name on the first line):")

entrada = st.text_area("Data entry", height=300)

if st.button("✍️ Fill out worksheet"):
    if not entrada.strip():
        st.warning("Paste dates to continue.")
    else:
        try:
            sheet = conectar_planilha()
            resultado = preencher_planilha(entrada, sheet)
            st.success(resultado)
        except Exception as e:
            st.error(f"Erro: {e}")

st.markdown("---")
st.header("🧾 Dates converter dd/mm/yyyy")

texto_original = st.text_area("Paste dates to convert:", height=200, key="conversor")

if st.button("🔁 Convert to dd/mm/yyyy"):
    if texto_original.strip():
        texto_convertido = re.sub(
            r'(\b)(\d{1,2})/(\d{1,2})/(\d{4})',
            lambda m: f"{m.group(3).zfill(2)}/{m.group(2).zfill(2)}/{m.group(4)}",
            texto_original
        )
        st.text_area("Result:", value=texto_convertido, height=200, key="result")
    else:
        st.warning("Paste dates before convert.")
