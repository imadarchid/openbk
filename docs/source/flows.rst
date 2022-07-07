Account Flows
=============

Get basic metrics about a person's position given their bank statement.

.. _debits:

Account Debits
--------------

To get the sum of `debit` transactions, you can use the ``debits(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.flows import debits

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = debits(statement)

    print(result) # Show the output

.. _credits:

Account Credits
---------------

To get the sum of `credit` transactions, you can use the ``credits(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.flows import debits

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = credits(statement)

    print(result) # Show the output

.. _netmovements:

Net Movements
-------------

To get the sum of net movements, you can use the ``net_movements(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.flows import net_movements

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = net_movements(statement)

    print(result) # Show the output

Ending Balance
-------------

To get the ending balance of a statement, you can use the ``ending_balance(statement)`` method.

- **statement**: a `statement` parameter is required. You can get this from running the extract function.

.. code-block:: python

    from openbk.extract import extract
    from openbk.statement.flows import ending_balance

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output
    result = ending_balance(statement)

    print(result) # Show the output
