# utils/sheets.py

from datetime import datetime, timedelta
import re
import gspread
from config.constants import LINHA_NOMES, LINHA_DATAS, COLUNA_NOME, CODIGOS
from .parser import parse_data

def preencher_planilha(dados_colados, sheet):
    linhas = dados_colados.strip().split("\n")
    if not linhas:
        return "⚠️ Empty Data."

    nome = linhas[0].strip()
    dados = linhas[1:]

    nomes = sheet.col_values(COLUNA_NOME)[LINHA_NOMES - 1:]
    try:
        idx_nome = nomes.index(nome) + LINHA_NOMES
    except ValueError:
        return f"❌ '{nome}' not found on spreadsheet"

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
        datas_para_marcar = [(dt_ini + timedelta(days=i)) for i in range(max(1, dias))]

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

    return f"✅ {len(updates)} filled cells for {nome}."
