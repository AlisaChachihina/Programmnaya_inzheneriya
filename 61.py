a = input()
b = a.split(" ")
for i in range(len(b)):
    b[i] = int(b[i])
c = tuple(b)
print(b)
print(c)
