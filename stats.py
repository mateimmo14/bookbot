from curses import nl
from traceback import print_exc


def count_words(book_text):
    book_words = book_text.split()
    num_words = 0
    for word in book_words:
        num_words += 1
    print(f"Found {num_words} total words")


def count_characters(book_text):
    counts = []
    for word in book_text:
        for letter in word:
            if letter.isalpha():
                for entry in counts:
                    if entry["letter"] == letter:
                        entry["num"] += 1
                        break
                else:
                    counts.append({"letter": letter, "num": 1})
    return counts


def sort_on(items):
    return items["num"]
