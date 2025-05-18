def get_num_words(book_text):
    split_words = book_text.split()
    return len(split_words)

def get_num_letters(book_text):
    num_letters = {}
    for letter in book_text.lower():
        if not letter.isalpha():
            continue
        if letter not in num_letters:
            num_letters[letter] = 0

        num_letters[str(letter)] += 1

    return num_letters

