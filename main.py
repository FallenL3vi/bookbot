def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    words_dict = converter(chars_dict)
    words_dict.sort(reverse=True, key=sort_on)
    show_report(words_dict, num_words, book_path)

def show_report(words, whole_numb, path):
    print(f"--- Begin report of {path} ---")
    print(f"{whole_numb} words found in the document \n")
    for word in words:
        print(f"The '{word["letter"]}' character was found {word["value"]} times")
    print("--- End report ---")
    return None

def sort_on(dict):
    return dict["value"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def converter(dict):
    new_table = []
    for key, value in dict.items():
        if key.isalpha():
            new_table.append({"letter" : key, "value" : value})
    return new_table

main()
