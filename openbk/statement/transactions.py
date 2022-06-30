import re
import pandas as pd

from utils import categories
from utils.exceptions import NoTransactionsException

cats = categories.transaction_categories_cih

# Analyzing categories of spending
def analyze_spending(transactions):
    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['debit'].notna()].copy()
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.loc[index, 'category'] = key
    return transactions.reset_index(drop=True)

# Analyzing categories of revenue
def analyze_revenue(transactions):
    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['credit'].notna()].copy()
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.loc[index, 'category'] = key
    return transactions.reset_index(drop=True)

def get_merchants(transactions):
    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['debit'].notna()].copy()

    # Payment transactions
    ops = [cats['ecom_national'], cats['ecom_inter'], cats['card_pay']]

    for index, row in transactions.iterrows():
        if any(o in row['transaction'] for o in ops):
            splits = re.split(r"(CARTE[0-9]{4}|CARTE [0-9]{4})", row['transaction'])
            merchant = splits[2]
            transactions.loc[index, 'merchant'] = merchant

    return transactions.reset_index(drop=True)
