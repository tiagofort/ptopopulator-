# app.py

import streamlit as st
import re
from utils.auth import conectar_planilha
from utils.sheets import preencher_planilha

st.set_page_config(page_title="Preenchimento de Férias", layout="centered")

st.title("🗓️ Preencher Férias/Licenças na Planilha")
st.markdown("Cole os dados abaixo (começando com o nome na primeira linha):")

entrada = st.text_area("Entrada de dados", height=300)

if st.button("✍️ Preencher planilha"):
    if not entrada.strip():
        st.warning("Cole os dados antes de continuar.")
    else:
        try:
            sheet = conectar_planilha()
            resultado = preencher_planilha(entrada, sheet)
            st.success(resultado)
        except Exception as e:
            st.error(f"Erro: {e}")

st.markdown("---")
st.header("🧾 Conversor de Datas dd/mm/yyyy")

texto_original = st.text_area("Cole as datas a converter:", height=200, key="conversor")

if st.button("🔁 Converter para dd/mm/yyyy"):
    if texto_original.strip():
        texto_convertido = re.sub(
            r'(\b)(\d{1,2})/(\d{1,2})/(\d{4})',
            lambda m: f"{m.group(3).zfill(2)}/{m.group(2).zfill(2)}/{m.group(4)}",
            texto_original
        )
        st.text_area("Resultado:", value=texto_convertido, height=200, key="result", disabled=True)
    else:
        st.warning("Cole os dados antes de converter.")
