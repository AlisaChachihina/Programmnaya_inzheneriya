f_empty = open('2_empty.txt', 'r', encoding="utf-8") #открываем пустой файл на чтение
f_not_empty = open('2_not_empty.txt', 'r', encoding="utf-8") #открываем непустой файл на чтение


def read_file(file): #создаем функцию чтения из файла
    lines = file.readlines() #считываем все строки из файла
    if len(lines) == 0: #если количество строк равно 0:
        raise Exception("файл пустой") #генерируем исключение, что файл пустой
    else: #если количество строк больше 0
        for line in lines: # идем по каждой считанной строке
            print(line) #выводим каждую строчку на новой строке


read_file(f_not_empty) #выполняем функцию с непустым файлом
read_file(f_empty) #выполняем функцию с пустым файлом
