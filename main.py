def count_words(text):
    words = text.split()

    return len(words)

def count_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
with open('books/frankenstein.txt', 'r') as fobj:
    file_contents = fobj.read()

num_words = count_words(file_contents)

char_count = count_chars(file_contents)
alpha_only = [item for item in char_count.items() if item[0].isalpha()]
alpha_only.sort(key=lambda x: x[1], reverse=True)

print("~~~~~ Starting report of books/frankenstein.txt ~~~~~")
print(f"{num_words} words total found in the text file.")
print()
print()
for char in alpha_only:
    print(f"The '{char[0]}' character was found {char[1]} times")
print("~~~~~ END ~~~~~")