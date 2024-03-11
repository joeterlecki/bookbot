#! /usr/bin/env python3

"""This module performs various functions with text content as books"""


def count_words(text_content: str) -> int:
    """
    Take text content from a file and return the number of words

    Parameters:
    arg1 (str): Text Content as string

    Returns:
    int: length of words
    """
    words = text_content.split()
    return len(words)


def count_chars(text_content: str) -> list[str]:
    """
    Take text content and return count of alpha numeric chars in
    reverse sorted list

    Parameters:
    arg1 (str): Text Content as string

    Retruns:
    list[dict[str, int]: {"character: 'a', 'occurences': 3"},
    {"character: 'b', 'occurences': 2"}]]
    """
    chars = {}
    char_list = []
    for char in text_content:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1

    # convert dict to list of dict of alpha characters
    # this probly can be optimized by combining with first loop
    # but this is good enough for now
    for k, v in chars.items():
        if k.isalpha():
            char_list.append({"character": k, "occurences": v})
    char_list.sort(reverse=True, key=lambda d: d["occurences"])
    return char_list


def display_char_counts(total_words, char_list):
    """
    Takes the total words, and list character counts then
    displays appropriatel
    """
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} found in the document")

    for item in char_list:
        print(f"The '{item['character']}' character was found {item['occurences']} times")

    print("--- End report ---")


def main():
    """Main method"""
    with open("./books/frankenstein.txt") as f:
        book_content = f.read()
        words = count_words(book_content)
        chars = count_chars(book_content)
        display_char_counts(words, chars)
        f.read()


if __name__ == "__main__":
    main()
