def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
    return contents


def count_words(book_text):
    book_words = book_text.split()
    num_words = 0
    for word in book_words:
        num_words += 1
    print(f"Found {num_words} total words")


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_words(book_text)
    return


main()
