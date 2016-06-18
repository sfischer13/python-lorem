====================
Python Lorem Package
====================

.. image:: https://img.shields.io/pypi/v/lorem.svg
        :target: https://pypi.python.org/pypi/lorem

.. image:: https://img.shields.io/travis/sfischer13/python-lorem.svg
        :target: https://travis-ci.org/sfischer13/python-lorem


Summary
-------

Generator for random text that looks like Latin.

Simple Example
--------------

.. code:: python

    import lorem
    
    s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
    p = lorem.paragraph()
    t = lorem.text()

Complex Example
---------------

.. code:: python

    from lorem.text import TextLorem
    
    # separate words by '-'
    # sentence length should be between 2 and 3
    # choose words from A, B, C and D
    lorem = TextLorem(wsep='-', srange=(2,3), words="A B C D".split())
    
    s1 = lorem.sentence()  # 'C-B.'
    s2 = lorem.sentence()  # 'C-A-C.'
