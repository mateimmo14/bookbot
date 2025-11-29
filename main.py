from stats import count_characters, count_words, sort_on


def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
    return contents


def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    dictionary = count_characters(book_text)
    dictionary.sort(key=sort_on, reverse=True)
    print(dictionary)

    return


main()
