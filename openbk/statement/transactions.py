import re
import pandas as pd

from utils import categories
from utils.exceptions import NoTransactionsException, MethodNotSupported


# Analyzing categories of spending
def analyze_spending(data):

    transactions = data[1]
    cats = categories.banks[data[2]]

    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['debit'].notna()].copy()
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.loc[index, 'category'] = key
    return transactions.reset_index(drop=True)

# Analyzing categories of revenue
def analyze_revenue(data):

    transactions = data[1]
    cats = categories.banks[data[2]]

    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['credit'].notna()].copy()
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.loc[index, 'category'] = key
    return transactions.reset_index(drop=True)

def get_merchants(data):

    transactions = data[1]
    cats = categories.banks[data[2]]

    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    transactions = transactions[transactions['debit'].notna()].copy()

    # Payment transactions
    ops = [cats['ecom_national'], cats['ecom_inter'], cats['card_pay']]

    try:
        for index, row in transactions.iterrows():
            if any(o in row['transaction'] for o in ops):
                splits = re.split(r"(CARTE[0-9]{4}|CARTE [0-9]{4})", row['transaction'])
                merchant = splits[2]
                transactions.loc[index, 'merchant'] = merchant
    except:
        raise MethodNotSupported("This method is not supported for your bank yet.")

    return transactions.reset_index(drop=True)
