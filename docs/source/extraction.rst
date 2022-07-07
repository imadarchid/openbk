Reading a Statement
===================

.. _chars:

PDF Statement characteristics
-----------------------------

**openbk** only supports PDF statements that can be downloaded from e-banking solutions. Please note that you will encounter errors with scanned statements.
Compatible PDF statements can be downloaded either through the banking web platforms or through the mobile apps.

.. _extracting:

Extraction
----------

To extract data from a PDF statement:

.. code-block:: python

    from openbk.extract import extract
    output = extract("path/to/your/file.pdf")

    print(output) # Show the output

The output of the ``extract()`` method is a list that comprises the following:

#. ``beg_balance``: Beginning balance of the month corresponding to that statement.
#. ``transactions``: Dataframe object with **transaction**, **debit**, **credit**, and **date** columns.
#. ``bank``: A string referring to the detected/mentioned bank.


You can find the explanation of each column below of the ``transactions`` object:

* **transaction**: refers the transaction text (Libellé). It describes the operation.
* **debit**: refers to the debited amount (expense) for transactions where applicable.
* **credit**: refers to the credited amount (revenue) for transactions where applicable.
* **date**: refers to the date of the transaction.

**The output of the ``extract()`` function is used in all subsequent methods**

You can now discover more about how you can analyze :doc:`transactions` or how to get fund :doc:`flows` for a given bank statement.
