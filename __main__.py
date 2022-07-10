from email.policy import default
import PyPDF2
import re
import argparse

from openbk.utils.exceptions import NoBankDetected
from openbk.utils.extractors import cih, awb
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

def main():

  parser = argparse.ArgumentParser()
  
  parser.add_argument("--bank", "-b", type=str.upper, help="Bank to extract", choices=["CIH", "AWB", "AUTO"], default="AUTO")
  parser.add_argument("--file", "-f", type=str, help="File to extract")
  parser.add_argument("--beginning-balance", "-bb", action="store_true", default=False, help="Beginning balance")
  parser.add_argument("--transactions", "-t", action="store_true", default=False, help="List Transactions")
  parser.add_argument("--detected", "-d", action="store_true", default=False, help="Detected Bank")

  args = parser.parse_args()

  match args.bank:
    case 'CIH':
      result = cih(args.file)
    case 'AWB':
      result = awb(args.file)
    case 'AUTO':
      result = extract(args.file)
  
  if args.beginning_balance:
    print("Beginning Balance:", result[0])
  if args.transactions:
    print("Transactions:")
    print(result[1])
  if args.detected:
    print("Detected Bank:", result[2])

if __name__ == '__main__':
    main()