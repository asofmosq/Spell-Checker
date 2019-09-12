Spell Checker
===============

A spelling checker that outputs a list of words that were not found in the dictionary.
This library parses a dictionary file into a Trie and then searches the Trie with the words from the input file.

Typical Workflow
----------------

.. code:: bash

    $ python spell_checker.py test/Document.txt test/Dictionary.txt


Dependencies
------------

Spell checker was written and tested using Python 3.6.4 and depends on package argparse.


