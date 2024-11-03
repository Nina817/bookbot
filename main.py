from pprint import pprint

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count_dict = get_num_characters(text)
    format_report(path = book_path, word_count=num_words, character_dict=character_count_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    result = {}
    for character in text:
        character =  character.lower()
        if character:
            if character in result.keys():
                result[character] += 1
            else:
                result[character] = 1
    return result

def format_report(path, word_count, character_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    for key, value in character_dict.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")

main()