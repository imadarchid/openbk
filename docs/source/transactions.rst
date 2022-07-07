Transactions
============

Get more insights from the bank transactions.

For now, transaction analysis is quite basic. The only added value here is the ability to get transaction types (i.e: whether it's a card payment, a wire transfer, etc.) or to get merchants.
We will be working on more cool things here, but feel free to contribute 😉.

.. warning::

   Please note that not all transactions can be categorized. The classification process is currently crowdsourced and will take some time to be more accurate. Do not hesitate to contribute by adding more categories.

.. _analyze_spending:

Analyze Spending
----------------

To get spending categories, you can use the ``analyze_spending(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.transactions import analyze_spending

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = analyze_spending(statement)

    print(result) # Show the output

.. _analyze_revenue:

Analyze Revenue
---------------

To get revenue categories, you can use the ``analyze_revenue(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.transactions import analyze_revenue

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = analyze_revenue(statement)

    print(result) # Show the output

.. _get_merchants:

Get Merchants
-------------

To get merchants (card payments), you can use the ``get_merchants(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.transactions import get_merchants

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = get_merchants(statement)

    print(result) # Show the output
