f = open('text.txt', 'r', encoding="utf-8") #открываем файл на чтение
digits = [".", ",", ":", "-", "+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "—"] #символы, которые не нужно учитывать
def remove_digits(word): #функция для удаления ненужных символов
    result = ""
    for digit in digits: #идем по каждому ненужному символу
        result = word.replace(digit, "") #заменяем каждый ненужный символ на ""
    return result #возвращаем результат без ненужных символов
strs = f.readlines() #массив всех строк в тексте
d = dict() #создаем словарь
for str in strs: #идем по каждой строчке текста
    for word in str.split(" "): #идем по каждому слову в строчке
        w = word.rstrip() #удаляем символы переноса и лишние пробелы
        w = remove_digits(w) #удаляем ненужные символы
        if w == "": #проверяем, что слово не пустое
            continue #идем на следующую итерацию цикла
        if w in d.keys(): #проверяем наличие слова в словаре
            d[w] += 1 #если оно есть, то прибавляем единицу
        else: #если его нет
            d[w] = 1 #ставим единицу
t = [] #создаем пустой список
for key in d.keys(): #идем по каждому ключу в словаре
    t.append((key, d[key])) #добавляем в список кортеж вида (слово, количество этого слова в тексте)
t.sort(key=lambda x: x[1], reverse=True) #сортируем список по убыванию количества слова в тексте
f.close() #закрываем файл
sum = 0 #создаем переменную равную нулю
for key in d.keys(): #идем по каждому ключу в словаре
    sum += d[key] #добавляем в переменную количество всех слов
print(sum) #выводим общее количество слов в тексте
print(t[0]) #выводим самое часто встречающееся слово и количество вхождений



