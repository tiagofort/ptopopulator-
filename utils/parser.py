# utils/parser.py

from datetime import datetime

def parse_data(val):
    try:
        return datetime.strptime(val.strip(), "%d-%b")
    except:
        return None
