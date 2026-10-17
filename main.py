import sys

from stats import word_count
from stats import letter_count
from stats import chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: int, sorted_list_of_characters: list[tuple[str,int]]):
    print(
        "============ BOOKBOT ============\n" 
        f"Analyzing book found at {book_path}...\n" 
        "----------- Word Count ----------\n" 
        f"Found {word_count} total words\n"
        "--------- Character Count -------"
        )
    for character_set in sorted_list_of_characters:
        if character_set[0].isalpha():
            print(f"{character_set[0]}: {character_set[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print_report(book_path, word_count(get_book_text(book_path)), chars_dict_to_sorted_list(letter_count(get_book_text(book_path))))

main()