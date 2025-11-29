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
                letter = letter.lower()  # treat 'A' and 'a' as the same

                for entry in counts:
                    if entry["letter"] == letter:
                        entry["num"] += 1
                        break
                else:
                    # this runs only if we DIDN'T break: letter not found
                    counts.append({"letter": letter, "num": 1})

    return counts


def sort_on(items):
    return items["num"]
