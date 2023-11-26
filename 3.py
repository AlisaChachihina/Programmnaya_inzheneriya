class Worker: #создаем класс Работник
    def __init__(self, name, position, salary): #определяем конструктор и передаем в него параметры: имя, должность, зарплата
        self.name = name  #определяем атрибут имя
        self.salary = salary #определяем атрибут зарплата
        self.position = position #определяем атрибут должность

    def work(self): #создаем метод Работать
        print(f"Do work in a position {self.position}") #выводим результат


class SelfWorker(Worker): #создаем класс Самозанятый и наследуемся от класса Работник
    def __init__(self, name, position, salary, taxes): #определяем конструктор и передаем в него параметры: имя, должность, зарплата, налоги
        super().__init__(name, position, salary) #вызываем конструктор родительского класса
        self.taxes = taxes #определяем атрибут налоги

    def pay_taxes(self): #создаем метод Заплатить налоги
        print(f"Pay the taxes in the amount of {self.taxes}") #выводим результат


worker = SelfWorker("Dmitriy", "Programmer", 70000, 70000 * 0.13) #создаем объект класса Самозанятый
worker.work() #вызываем метод Работать родительского класса
worker.pay_taxes() #вызываем метод Заплатить налоги
