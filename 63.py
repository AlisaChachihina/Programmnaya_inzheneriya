a = '536352736384873885'
def get_dict(a):
    c = dict()
    b = []
    for i in range(len(a)):
        b.append(int(a[i]))
        if b[i] in c.keys():
            c[b[i]] += 1
        else:
            c[b[i]] = 1
    d = []
    for key in c.keys():
        d.append((key, c[key]))
    d.sort(key=lambda x: x[1], reverse=True)
    e = []
    for i in range(3):
        e.append(d[i])
    e.sort(key=lambda x: x[0])
    c.clear()
    for i in e:
        print(i[0])
        c[i[0]] = i[1]
    return c

print(get_dict(a))
