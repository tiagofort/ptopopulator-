## utils/auth.py

Responsible for securely connecting to the Google Spreadsheet using a **Service Account** and credentials provided via environment variable GOOGLE_CREDENTIALS_JSON. It uses Streamlit’s @st.cache_resource to cache the connection.

```
@st.cache_resource
def conectar_planilha():
    ...
```

## utils/sheets.py

This is the core logic of the system. It processes each pasted PTO line by:

1. Extracting the employee name

2. Validating PTO types (H, B, SSP, etc.)

3. Using a regular expression to extract start and end dates (regardless of spacing)

4. Mapping dates to spreadsheet columns

5. Preparing batch updates for the Google Sheet

Handles edge cases like:

- Unknown names

- Missing or malformed dates

- Invalid leave codes

## utils/parser.py

A helper used to parse header values in the spreadsheet into Python datetime objects. Required to match pasted data dates with the spreadsheet's structure.


