#!/usr/bin/env python3


def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        print(words_in_string(text))


def words_in_string(text) -> int:
    return len(text.split())


def number_chars(text):
    pass


if __name__ == "__main__":
    main()
