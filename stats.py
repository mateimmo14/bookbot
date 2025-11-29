from curses import nl
from traceback import print_exc


def count_words(book_text):
    book_words = book_text.split()
    num_words = 0
    for word in book_words:
        num_words += 1
    print(f"Found {num_words} total words")


def count_characters(book_text):
    counts = {}
    book_text = book_text.lower()
    for word in book_text:
        for letter in word:
            if letter.isalpha() == True:
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1
    return counts
