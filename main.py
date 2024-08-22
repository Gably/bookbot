def main():
    path = "books/frankenstein.txt"
    book = book_to_text(path)
    num_of_words = count_words(book)
    character_count_dict = count_char(book)
    sorted_character_count_list = char_count_dict_to_sorted_list_of_dict(character_count_dict)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    for character in sorted_character_count_list:
        if character["char"].isalpha():
            print(f"The '{character['char']}' character was found {character['count']} times")
    print("--- End report ---")

def book_to_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    char_count_dict = {}
    lowered_book = book.lower()
    for char in lowered_book:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict

def char_count_dict_to_sorted_list_of_dict(char_count_dict):
    list_of_dict = []
    for char in char_count_dict:
        list_of_dict.append(
            {
            "char": char, 
            "count": char_count_dict[char]
            }
            )
    list_of_dict.sort(reverse = True, key = sort_on)
    return list_of_dict

def sort_on(dict):
    return dict["count"]


main()