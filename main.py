#!/usr/bin/env python3


def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        number_of_words = words_in_string(text)
        number_of_chars = number_chars(text)
        sorted_chars = sort_dict(number_of_chars)

        print("Words in text: ", number_of_words)
        print("Number chars: ", number_of_chars)
        print("Sorted chars: ", sorted_chars)


def words_in_string(text) -> int:
    return len(text.split())


def number_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def sort_dict(chars_dict):
    chars_list = []

    for k, v in chars_dict.items():
        if k.isalpha():
            char_dict = {"char": k, "count": v}
            chars_list.append(char_dict)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


if __name__ == "__main__":
    main()
