import sys

from stats import count_characters, count_words, sort_on


def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
    return contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    book_text = get_book_text(path)
    dictionary = count_characters(book_text)
    dictionary.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    for set in dictionary:
        print(f"{set['letter']}: {set['num']}")
    print("============= END ===============")
    return


main()
