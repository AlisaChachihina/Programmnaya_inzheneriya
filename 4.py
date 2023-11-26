class Worker: #создаем класс Работник
    def __init__(self, name, position, salary): #определяем конструктор и передаем в него параметры: имя, должность, зарплата
        self.name = name  #определяем атрибут имя
        self.__salary = salary #определяем приватный атрибут зарплата
        self._position = position #определяем защищенный атрибут должность

    def work(self): #создаем метод Работать, использующий защищенный атрибут должность
        print(f"Do work in a position {self._position}") #выводим результат

    def say_salary(self): #создаем метод Сказать зарплату, использующий приватный атрибут зарплата
        print(f"{self.name} has salary of {self.__salary}") #выводим результат


worker = Worker("Dmitriy", "Programmer", 70000) #создаем объект класса Работник
worker.work() #вызываем метод Работать, использующий защищенный атрибут должность (Никаких ошибок)
worker.say_salary() #вызываем метод Сказать зарплату, использующий приватный атрибут должность (Никаких ошибок)
print(worker._position) #пытаемся обратиться к защищенному атрибуту позиция напрямую (Предупреждение)
worker.__salary #пытаемся обратиться к приватному атрибуту зарплата напрямую (Ошибка)



