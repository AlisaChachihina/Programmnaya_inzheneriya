class CopyrightDecorator: #создаем класс декоратора
    def __init__(self, func): #определяем конструктор с параметром функции
        self.func = func #определяем аттрибут func со значением параметра

    def __call__(self, *args, **kwargs): #определяем функцию вызова
        print(f"Function {self.func.__name__} made by Alisa") #выводим сообщение копирайта
        result = self.func(*args, **kwargs) #выполняем функцию
        return result #возвращаем значение функции


@CopyrightDecorator #добавляем декоратор к функции
def sum_elements(a1, a2): #создаем функцию сложения двух элементов
    return a1 + a2 #возвращаем сумму двух эелементов


@CopyrightDecorator #добавляем декоратор к функции
def print_message(message): #создаем функцию вывода сообщения
    print(message) # выводим сообщение


print(sum_elements(1, 2)) # выводим результат функции суммы эелементов
print_message("Message") #выводим сообщение



