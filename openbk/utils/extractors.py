from typing import List
import pandas as pd
import tabula

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

    return [beg_balance, end_balance, transactions]

def attijari(file):
    data = tabula.read_pdf_with_template(file, template_path="templates/awb.json", pages='all', pandas_options={'header': None})

    transactions = pd.concat([data[1], data[2], data[3], data[4]], axis=1, ignore_index=True)
    transactions.columns = ['transaction', 'date', 'debit', 'credit']

    transactions = transactions[transactions.transaction.notna()]
    transactions = transactions[transactions.transaction != 'TOTAL MOUVEMENTS']

    transactions = transactions.replace(",", ".", regex=True)
    transactions['debit'] = transactions['debit'].replace(" ", "", regex=True)
    transactions['credit'] = transactions['credit'].replace(" ", "", regex=True)
    transactions['date'] = transactions['date'].replace(" ", "/", regex=True)

    transactions['debit'].astype(float)
    transactions['credit'].astype(float)

    # Add support for beg balance and end balance

    return transactions
