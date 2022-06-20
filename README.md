[![Documentation Status](https://readthedocs.org/projects/openbk/badge/?version=latest)](https://openbk.readthedocs.io/en/latest/?badge=latest)
# openbk

openbk is a small python library that can be used to read and extract transaction information from Moroccan bank statements (PDF).

[Installation](#dependencies-and-installation) | [Docs](https://openbk.readthedocs.io) | [Motivation](#motivation)

## Features

- Import an e-banking PDF statement and retrieve a clean DataFrame with transactions.
- Get basic metrics (total debit, total credit, net movements).
- Analyze bank transactions to extract their categories.
- Analyze card payments (online and offline) to detect merchants.
- Automatically detect which bank corresponds to the uploaded statement _(Coming Soon)_.

## Supported Banks
- ✅ CIH Bank (E-banking statements - Particuliers)
- 🔜 Attijariwafa Bank (Coming Soon)
- 🔜 Banque Centrale Populaire (Coming Soon)

_Other banks will be decided in the future_

ℹ️ **Transaction categories**: I do not have a comprehensive list of transaction types, so I hope that the classification gets better with your contribution!

## Dependencies and Installation
openbk relies on [`tabula-py`](https://pypi.org/project/tabula-py/) to read and extract tables from PDFs. Tabula requires the following to function properly:
- Python 3.7+
- Java 8+

To add openbk to your project:
```sh
pip install openbk
```

## Motivation
This project aims to simplify the task for developers who want to build apps that rely on the analysis of bank statements (Wallets, Lending, Consumer Behavior analysis, etc.). Ideally, openbk can help developers and data analysts in their financial scoring processes for applications in the Moroccan context.

### Data Privacy
Please be careful when handling sensitive financial information and make sure to comply with the latest Moroccan data privacy laws and guidelines.
