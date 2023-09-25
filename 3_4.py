s = str(input("Введите предложение на английском: "))
print("Длина предложения:", len(s))
s1 = s.lower()
print(s1)
print("Количество гласных в предложении: ", s1.count('a') + s1.count('e') + s1.count('i') + s1.count('o') + s1.count('u'))
s2 = s1.replace('ugly', 'beauty')
print(s2)
if s2.startswith('the') == True:
    print("Предложение начинается с The")
else:
    print("Предложение не начинается с The")
if s2.endswith('end') == True:
    print("Предложение заканчивается на end")
else:
    print("Предложение не заканчивается на end")