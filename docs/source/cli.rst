CLI Usage
=========

About
-----

You can also use **openbk** through your CLI for basic data extraction (beginning balance, transactions, bank detection).

- ``--help``: Display commands and how to use them.
- ``--file FILE`` or ``-f FILE``: Bank statement filepath.
- ``--bank``: Pass a specific bank (bypasses the auto-detection of banks). Accepts the following values: CIH, AWB.
- ``--beginning-balance`` or ``-bb``: Flag to display the beginning balance of the statement.
- ``--transactions`` or ``-t``: Flag to display the extracted transactions.
- ``--detected``: Flag to only extract the detected bank.


Example commands
----------------

.. code-block:: console
    python openbk --file path/to/file -bb
    > Beginning Balance: 4312.9

.. code-block:: console
    python openbk --file path/to/file -bank CIH --transactions
    > [Transactions table]
