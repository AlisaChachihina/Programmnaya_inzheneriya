class Worker: #создаем класс Работник
    def __init__(self, name, position, salary): #определяем конструктор и передаем в него параметры: имя, должность, зарплата
        self.name = name  #определяем атрибут имя
        self.__salary = salary #определяем приватный атрибут зарплата
        self._position = position #определяем защищенный атрибут должность

    def work(self): #создаем метод Работать, использующий защищенный атрибут должность
        print(f"Do work in a position {self._position}") #выводим результат

    def say_salary(self): #создаем метод Сказать зарплату, использующий приватный атрибут зарплата
        print(f"{self.name} has salary of {self.__salary}") #выводим результат


class Homeworker(Worker): #создаем класс Работник из дома
    def __init__(self, name, position, salary): #определяем конструктор и передаем в него параметры: имя, должность, зарплата
        super().__init__(name, position, salary) #вызываем конструктор родительского класса

    def work(self): #переопределяем метод родительского класса Работать
        print(f"Do work at home in a position {self._position}") #выводим результат


worker = Worker("Dmitriy", "Programmer", 70000) #Создаем объект класса Работник
home_worker = Homeworker("Anton", "Programmer", 70000) #Создаем объект класса Работник из дома
worker.work() #вызываем метод Работать из объекта класса Работник
home_worker.work() #вызываем метод Работать из объекта класса Работник из дома
