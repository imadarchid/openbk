import re
import json

import pandas as pd
import tabula
import PyPDF2

from utils.exceptions import FileReadException, DataExtractionException

def cih(file):

    df = tabula.read_pdf(file, stream=True, pages='all', pandas_options={'header': None}, area=(290, 10, 700, 577))

    print(f'Detected {len(df)} pages...')

    # All transactions
    transactions = []

    for pn, p in enumerate(df):
        try:
            print(f'Processing page {pn + 1} of {len(df)}....')
            statement = p
            if len(statement.columns) > 3:
                statement.drop(1, inplace=True, axis=1)
            statement.columns = ["transaction", "debit", "credit"]
            statement[["date", "transaction"]] = statement["transaction"].str.split(' ', expand=True, n=1)

            transactions.append(statement)
        except:
            raise FileReadException('It appears that you did not upload a valid PDF Statement')


    try:
        transactions = pd.concat(transactions, ignore_index=True)
        transactions = transactions[transactions.transaction.notnull()]
        transactions = transactions[transactions.date != 'PAGE']
        transactions = transactions[transactions.date != 'REPORT']
        transactions.date = transactions['date'].str[:5]
        transactions = transactions.replace(",", ".", regex=True)
        transactions['debit'] = transactions['debit'].replace(" ", "", regex=True)
        transactions['credit'] = transactions['credit'].replace(" ", "", regex=True)

        if pd.isna(transactions.iloc[0].credit):
            beg_balance = -float(transactions.iloc[0].debit)
        else:
            beg_balance = float(transactions.iloc[0].credit)

        if pd.isna(transactions.iloc[-1].credit):
            end_balance = -float(transactions.iloc[-1].debit)
        else:
            end_balance = float(transactions.iloc[-1].credit)

        transactions = transactions[transactions.date != 'TOTAL']
        transactions = transactions[transactions.date != 'SOLDE']
        transactions = transactions[:-1]

        transactions['debit'].astype(float)
        transactions['credit'].astype(float)

    except Exception:
        raise DataExtractionException('An issue occurred when analyzing your PDF statement')

    return [beg_balance, transactions]

def attijari(file):

    coordinates = []

    # Opening JSON file
    template = open('templates/awb.json')
    template_parsed = json.load(template)
    for c in template_parsed:
        coordinates.append([c['y1'], c['x1'], c['y2'], c['x2']])

    doc = open(file, 'rb')
    doc_data = PyPDF2.PdfFileReader(doc)
    totalpages = doc_data.numPages

    transactions = pd.DataFrame()

    for i in range(totalpages):
        # print(i)
        if i < 1:
            data = tabula.read_pdf(file, pages=[i+1], pandas_options={'header': None}, area=coordinates, stream=True)
            beg_box = data[0].values[0][1]
            temp_df = pd.concat([data[1], data[2], data[3], data[4]], axis=1, ignore_index=True)
            transactions = pd.concat([transactions, temp_df], axis=1)
        else:
            data = tabula.read_pdf(file, pages=[i+1], pandas_options={'header': None}, area=coordinates, stream=True)
            temp_df = pd.concat([data[0], data[1], data[2], data[3]], axis=1, ignore_index=True)
            transactions = pd.concat([transactions, temp_df], axis=0)

    transactions.columns = ['transaction', 'date', 'debit', 'credit']
    transactions = transactions.reset_index(drop=True)

    transactions = transactions[transactions.transaction.notna()]
    transactions = transactions[transactions.transaction != 'TOTAL MOUVEMENTS']

    transactions = transactions.replace(",", ".", regex=True)
    transactions['debit'] = transactions['debit'].replace(" ", "", regex=True)
    transactions['credit'] = transactions['credit'].replace(" ", "", regex=True)
    transactions['date'] = transactions['date'].replace(" ", "/", regex=True)

    transactions['debit'].astype(float)
    transactions['credit'].astype(float)

    # Add support for beg balance
    amount = re.findall(r"^(\d{1,3}(?: \d{3})*\,\d{2})", beg_box)
    amount = amount[0].replace(" ", "")
    amount = amount.replace(",", ".")

    if "CREDITEUR" in beg_box:
        beg_balance = float(amount)
    elif "DEBITEUR" in beg_box:
        beg_balance = float(-amount)
    else:
        raise ValueError()

    return [beg_balance, transactions]
