class Worker: #создаем класс Работник
    def __init__(self, name, position, salary): #определяем конструктор и передаем в него параметры: имя, должность, зарплата
        self.name = name  #определяем атрибут имя
        self.salary = salary #определяем атрибут зарплата
        self.position = position #определяем атрибут должность

    def work(self): #создаем метод Работать
        print(f"Do work in a position {self.position}") #выводим результат


worker = Worker("Dmitriy", "Director", 100000) #создаем объект класса Работник
worker.work() #вызываем метод Работать у объекта класса
