a = ((1, 2, 8, 5, 1, 2, 9), 8)
b = []
c = False
for i in a[0]:
    if c:
        b.append(i)
        if i == a[1]:
            break
    else:
        if i == a[1]:
            b.append(i)
            c = True
b = tuple(b)
print(b)