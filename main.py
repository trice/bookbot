import sys
from stats import get_num_words
from stats import get_num_letters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def sort_on(thing):
    return thing[1]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    num_letters = get_num_letters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for tp in sorted(list(num_letters.items()), key=lambda x: x[1], reverse=True):
        print(f"{tp[0]}: {tp[1]}")

    print("============= END ===============")

    return 0

main()
