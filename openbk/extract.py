import PyPDF2
import re

from utils.exceptions import NoBankDetected
from utils.extractors import awb, cih
from typing import List

# For now, we are using ICEs since they are truly unique identifiers
bank_ids = [
    {"name": "CIH", "id":"001542240000068"},
    {"name": "AWB", "id":"001648789000071"},
]

def extract(file, bank = None) -> List:
    if not bank:
        bank = detect_bank(file)

    match bank:
        case 'CIH':
            result = cih(file)
        case 'AWB':
            result = awb(file)

    result.append(bank)

    return result

def detect_bank(file):
    doc = open(file, 'rb')
    doc_data = PyPDF2.PdfFileReader(doc)
    first_page = doc_data.getPage(0)

    all_text = first_page.extract_text()
    for b in bank_ids:
        result = re.search(b["id"], all_text)
        if result:
            bank = b["name"]
            break

    if not bank:
        raise NoBankDetected("Could not detect a bank or your bank is not supported by openbk")
    return bank
