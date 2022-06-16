from utils import categories

cats = categories.transaction_categories

# Analyzing categories of spending
def analyze_spending(transactions):
    transactions = transactions[transactions['debit'].notna()]
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.at[index, 'category'] = key

# Analyzing categories of revenue
def analyze_revenue(transactions):
    transactions = transactions[transactions['credit'].notna()]
    for index, row in transactions.iterrows():
        for key, val in cats.items():
            if val in row['transaction']:
                transactions.at[index, 'category'] = key
    print(transactions)

# Banking Fees
def analyze_fees(transactions):
    pass

def analyze_merchants(transactions):
    pass