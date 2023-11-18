f = open('73.txt', 'r', encoding="utf-8")
digits = [".", ",", ":"]

strs = f.readlines()
words_count = 0
lines_count = len(strs)
letters_count = 0
for str in strs:
    words = str.split(" ")
    for word in words:
        _word = word.replace("\n", "")
        words_count += 1
        for letter in _word:
            if letter not in digits:
                letters_count += 1
f.close()
print("Input file contains:")
print(f"{letters_count} letters")
print(f"{words_count} words")
print(f"{lines_count} lines")
