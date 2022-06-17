import re
from utils import categories

cats = categories.transaction_categories_cih

# Analyzing categories of spending
def analyze_spending(transactions):
    transactions = transactions[transactions['debit'].notna()]
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.at[index, 'category'] = key
    return transactions

# Analyzing categories of revenue
def analyze_revenue(transactions):
    transactions = transactions[transactions['credit'].notna()]
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.at[index, 'category'] = key
    return transactions

def get_merchants(transactions):
    transactions = transactions[transactions['debit'].notna()]

    # Payment transactions
    ops = [cats['ecom_national'], cats['ecom_inter'], cats['card_pay']]
    # print(ops)

    for index, row in transactions.iterrows():
        if any(o in row['transaction'] for o in ops):
            splits = re.split(r"(CARTE[0-9]{4}|CARTE [0-9]{4})", row['transaction'])
            merchant = splits[2]
            transactions.at[index, 'merchant'] = merchant

    print(transactions)