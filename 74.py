f = open('74.txt', 'r', encoding="utf-8")
f_input = open('74_input.txt', 'r', encoding="utf-8")
words = f.readline().split(" ")
a = f_input.read()
f_input.close()
result = a


def replace_words(x):
    res = x.lower()
    for _word in words:
        res = res.replace(_word, "*" * len(_word))
    return res


result = replace_words(result)
f.close()
res = ""
for i in range(len(result)):
    if result[i] != '*':
        res += a[i]
    else:
        res += "*"

print(res)
