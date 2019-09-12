
import argparse
import string
from src.create_trie import Node, insert, search

"""
spell_checker.py - main interface
=================================

The spell checker will output a list of words that were not found in the dictionary.
"""


def check_document(document, dictionary):
    result = []

    # Insert dictionary words into a Trie
    root = Node("*")
    for dict_word in dictionary:
        insert(root, dict_word.lower().strip(string.punctuation))

    # Search Trie for the document words
    for doc_word in document:

        # First make it lower case and strip punctuation
        doc_word = doc_word.lower().strip(string.punctuation)
        if not search(root, doc_word):
            result.append(doc_word)

    # Return the list of misspelled words
    return result


if __name__ == '__main__':

    # Argument parsing
    parser = argparse.ArgumentParser(prog='spell_checker.py', description="Spell check a document\
     against provided dictionary")
    parser.add_argument('InputFile', help='The document to be checked')
    parser.add_argument('DictionaryFile', help='The dictionary')
    args = parser.parse_args()

    document_words = []
    # Parse document into a list
    try:
        with open(args.InputFile, "r") as file:
            for line in file:
                document_words.extend(line.split())
    except FileNotFoundError:
        pass

    dictionary_words = []
    # Parse dictionary file into a list
    try:
        with open(args.DictionaryFile, "r") as file:
            # Split on newline and put into a list
            for line in file:
                dictionary_words.extend(line.split())
    except FileNotFoundError:
        pass

    misspelled_words = check_document(document_words, dictionary_words)

    for word in misspelled_words:
        print(word)

