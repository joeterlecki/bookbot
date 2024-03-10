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


def count_letters(text_content: str) -> dict[str, int]:
    """
    Take text content and return count of unique chars

    Parameters:
    arg1 (str): Text Content as string

    Retruns:
    dict[str, int]: {"a": 1, "b": 2, "c": 3}
    """
    chars = {}
    # loop through text for each char
    for c in text_content:
        # set to lower
        lc = c.lower()
        # check if char is already in dict and if so append 1
        # if not just set as 1
        if lc in chars:
            chars[lc] += 1
        else:
            chars[lc] = 1
    return chars


def main():
    """Main method"""
    with open("./books/frankenstein.txt") as f:
        book_content = f.read()
        words = count_words(book_content)

        print(f"Ther are {words} in the document")
        letters = count_letters(book_content)


if __name__ == "__main__":
    main()
