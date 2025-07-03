import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import re
import os
import tempfile
import json

# --- Autenticação com Google Sheets ---
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_JSON_ENV = os.getenv("GOOGLE_CREDENTIALS_JSON") 
SPREADSHEET_NAME = "pto"

# --- Configurações da planilha ---
LINHA_NOMES = 5
LINHA_DATAS = 3
COLUNA_NOME = 1

# --- Mapeamento dos códigos ---
CODIGOS = {
    "B": "BH",
    "H": "H",
    "SSP": "SL",
    "SCERT": "SL",
    "SUCERT": "SL"
}

@st.cache_resource
def conectar_planilha():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SPREADSHEET_NAME).sheet1
    return sheet

def parse_data(val):
    try:
        return datetime.strptime(val.strip(), "%d-%b")
    except:
        return None

def preencher_planilha(dados_colados, sheet):
    linhas = dados_colados.strip().split("\n")
    if not linhas:
        return "⚠️ Empty data"

    nome = linhas[0].strip()
    dados = linhas[1:]

    # Localizar linha do nome
    nomes = sheet.col_values(COLUNA_NOME)[LINHA_NOMES - 1:]
    try:
        idx_nome = nomes.index(nome) + LINHA_NOMES
    except ValueError:
        return f"❌ '{nome}' was not found on sheet"

    # Mapear datas da linha 3 para colunas
    header = sheet.row_values(LINHA_DATAS)
    col_date_map = {}
    for col, val in enumerate(header, start=1):
        data = parse_data(val)
        if data:
            data = data.replace(year=2025)
            col_date_map[data.strftime("%d/%m/%Y")] = col

    updates = []

    for linha in dados:
        linha_limpa = re.sub(r'\s{2,}|\t+', '\t', linha.strip())
        partes = linha_limpa.split("\t")

        if len(partes) < 3:
            continue

        tipo = partes[0].split("~")[0].strip()
        if tipo not in CODIGOS:
            continue

        try:
            dt_ini = datetime.strptime(partes[1].strip().split()[0], "%d/%m/%Y")
            dt_fim = datetime.strptime(partes[2].strip().split()[0], "%d/%m/%Y")
        except:
            continue

        dias = (dt_fim - dt_ini).days
        if dias <= 0:
            datas_para_marcar = [dt_ini]
        else:
            datas_para_marcar = [(dt_ini + timedelta(days=i)) for i in range(dias)]

        for dia in datas_para_marcar:
            chave = dia.strftime("%d/%m/%Y")
            if chave in col_date_map:
                col = col_date_map[chave]
                updates.append({
                    "range": gspread.utils.rowcol_to_a1(idx_nome, col),
                    "values": [[CODIGOS[tipo]]]
                })

    if updates:
        sheet.batch_update([{
            "range": u["range"],
            "values": u["values"]
        } for u in updates])

    return f"✅ Atualização concluída! {len(updates)} células preenchidas para {nome}."

# --- Interface Streamlit ---
st.title("🗓️ Filling in Vacations/Licenses in the Spreadsheet")
st.markdown("Paste the data below (starting with the name on the first line):")

entrada = st.text_area("Data entry", height=300)

if st.button("✍️ Fill in the spreadsheet"):
    if not entrada.strip():
        st.warning("Paste data before to continue.")
    else:
        try:
            sheet = conectar_planilha()
            resultado = preencher_planilha(entrada, sheet)
            st.success(resultado)
        except Exception as e:
            st.error(f"Error to fill or connect to the sheet: {e}")


st.markdown("---")
st.header("🧾 Data conversor dd/mm/yyyy")

texto_original = st.text_area("Paste here all dates to be converted:", height=200, key="conversor")

if st.button("🔁 Converts date to dd/mm/yyyy"):
    if texto_original.strip():
        texto_convertido = re.sub(
            r'(\b)(\d{1,2})/(\d{1,2})/(\d{4})',
            lambda m: f"{m.group(3).zfill(2)}/{m.group(2).zfill(2)}/{m.group(4)}",
            texto_original
        )
        st.text_area("Converted Data:", value=texto_convertido, height=200, key="result", disabled=True)
    else:
        st.warning("Cole o conteúdo acima antes de converter.")
