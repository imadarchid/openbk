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

The output of the ``extract()`` method is a Dataframe object with **transactions**, **debit**, **credit**, and **date** columns.
