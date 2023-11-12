a1 = "Миша 16, Арсений 14, Рома 18, Слава 56"
a2 = "Слава 56"
a3 = "Арсений 17, Рома 12, Слава 19"


def get_contacts(a):
    b = a.split(", ")
    d = []
    for i in b:
        c = i.split(" ")
        d.append((c[0], int(c[1])))
    e = min(d, key=lambda x:x[1])
    print(e[0])
    return d


print(get_contacts(a1))
print(get_contacts(a2))
print(get_contacts(a3))