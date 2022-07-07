import pandas as pd
from utils.exceptions import NoTransactionsException


def debits(data):
    transactions = data[1]

    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    total_debit = transactions['debit'].astype(float)
    total_debit = total_debit.sum()

    return total_debit

def credits(data):
    transactions = data[1]

    if not isinstance(transactions, pd.DataFrame) or transactions.empty:
        raise NoTransactionsException('Wrong format or empty statement')

    total_credit = transactions['credit'].astype(float)
    total_credit = total_credit.sum()

    return total_credit

def net_movements(data):
    transactions = data[1]

    net_mov = credits(transactions) - debits(transactions)

    return net_mov

def ending_balance(beg_balance, data):
    transactions = data[1]

    delta = net_movements(transactions)

    return beg_balance + delta
