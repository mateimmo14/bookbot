from stats import count_characters, count_words


def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
    return contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_words(book_text)
    char_counte = count_characters(book_text)
    print(char_counte)

    return


main()
