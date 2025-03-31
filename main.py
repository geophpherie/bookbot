import sys
from stats import count_words


def count_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

with open(sys.argv[1], "r") as fobj:
    file_contents = fobj.read()

num_words = count_words(file_contents)

char_count = count_chars(file_contents)
alpha_only = [item for item in char_count.items() if item[0].isalpha()]
alpha_only.sort(key=lambda x: x[1], reverse=True)

print("~~~~~ Starting report of books/frankenstein.txt ~~~~~")
print(f"{num_words} words found in the document.")
print()
print()
for char in alpha_only:
    print(f"{char[0]}: {char[1]}")
print("~~~~~ END ~~~~~")

