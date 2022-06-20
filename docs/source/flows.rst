Account Flows
=============

Get basic metrics about a person's position given their bank statement.


.. _debits:

Account Debits
--------------

To get the sum of `debit` transactions, you can use the ``debits(statement)`` method.

- **statement**: a `statement` object is required. You can get this from running the extract function and selecting the third output.

.. code-block:: python

    from openbk.extract import extract
    from openbk.flows import debits

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output[2]
    result = debits(statement)

    print(result) # Show the output

.. _credits:

Account Credits
---------------

To get the sum of `credit` transactions, you can use the ``credits(statement)`` method.

- **statement**: a `statement` object is required. You can get this from running the extract function and selecting the third output.

.. code-block:: python

    from openbk.extract import extract
    from openbk.flows import debits

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output[2]
    result = credits(statement)

    print(result) # Show the output

.. _netmovements:

Net Movements
-------------

To get the sum of net movements, you can use the ``net_movements(statement)`` method.

- **statement**: a `statement` object is required. You can get this from running the extract function and selecting the third output.

.. code-block:: python

    from openbk.extract import extract
    from openbk.flows import net_movements

    output = extract("path/to/your/file.pdf")

    # Selecting the statement dataframe
    statement = output[2]
    result = net_movements(statement)

    print(result) # Show the output
