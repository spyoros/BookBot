def word_count(book_content: str) -> int:
    return len(book_content.split())

def letter_count(book_content: str) -> dict[str,int]:
    word_dict = {}
    for character in list(book_content):
        lower_case_character = character.lower()
        if lower_case_character not in word_dict:
            word_dict[lower_case_character] = 0
        word_dict[lower_case_character] = word_dict[lower_case_character] + 1
    return word_dict

def sort_on(content: tuple[str,int]) -> int:
    return content[1]

def chars_dict_to_sorted_list(content: dict[str,int]) -> list[tuple[str,int]]:
    ordered_list = []
    for k,v in content.items():
        ordered_list.append((k,v))
    ordered_list = sorted(ordered_list, reverse=True, key=sort_on)
    return ordered_list