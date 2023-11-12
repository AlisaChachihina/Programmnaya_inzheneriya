a = ((1,2,3), 5)
b = list(a[0])
if a[1] in b:
    b.remove(a[1])
print(tuple(b))
