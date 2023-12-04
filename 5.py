class MoreTenOrLessFiveSimbolsException(Exception): #создаем класс ошибки и наследуемся от класса Exception

    @staticmethod #добавляем декоратор статичной функции
    def message_more_ten(simbols): # создаем функцию, возвращающую сообщение ошибки, что символов больше 10
        return f"{simbols} simbols is more that 10 simbols" #возвращаем сообщение

    @staticmethod #добавляем декоратор статичной функции
    def message_less_five(simbols): ## создаем функцию, возвращающую сообщение ошибки, что символов меньше 5
        return f"{simbols} simbols is less that 5 simbols" #возвращаем сообщение


a = input() #считываем строку с консоли
try: #открываем блок try
    if len(a) > 10: #проверяем, что количество символов больше 10
        raise MoreTenOrLessFiveSimbolsException(MoreTenOrLessFiveSimbolsException.message_more_ten(len(a))) #генерируем ошибку с сообщением, что символов больше 10
    if len(a) < 5: #проверяем, что количество символов меньше 5
        raise MoreTenOrLessFiveSimbolsException(MoreTenOrLessFiveSimbolsException.message_less_five(len(a))) #генерируем ошибку с сообщением, что символов меньше 5
finally: #открываем блок finally
    print(len(a)) #выводим длину строки
