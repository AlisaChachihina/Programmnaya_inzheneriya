class Tomato: #создаем класс Помидор
    states = ["none", "growing", "green", "red"] #стадии созревания помидора

    def __init__(self, index): #метод, вызывающийся при создании объекта класса, в который мы передаем параметр index
        self._index = index #определяем динамическое свойство
        self._state = Tomato.states[0] #определяем динамическое свойство

    def grow(self): #создаем метод Расти, который переводит Помидор на следующую стадию созревания
        index = Tomato.states.index(self._state) #получаем индекс текущего состояния созревания
        if index + 1 < len(Tomato.states): #проверяем наличие следующего состояния
            self._state = Tomato.states[index + 1] #если есть, то переводим в следующее состояние

    def is_ripe(self): #создаем метод Предоставлять информацию о своей зрелости
        return self._state == "red" #проверяем, что текущее состояние является состоянием "red"

class TomatoBush: #создаем класс Куст с помидорами
    def __init__(self, tomato_count): #метод, вызывающийся при создании объекта класса, в который мы передаем параметр количество помидоров
        self.tomatoes = [] #создаем динамическое свойство список помидоров
        for i in range(tomato_count): #создаем нужное количество помидоров и помещаем их в мвойство Помидоры
            self.tomatoes.append(Tomato(i))

    def grow_all(self): #моздаем метод Расти вместе с томатами
        for tomato in self.tomatoes: #идем по каждому помидору
            tomato.grow() #растим помидор

    def all_are_ripe(self): #создаем метод, проверяющий, что все помидоры выращены
        for tomato in self.tomatoes: #идем по кадому помидору
            if not tomato.is_ripe(): #проверяем, что помидор вырос
                return False #если хоть один не вырос, возвращаем false
        return True #если все выращены, то возвращаем true

    def give_away_all(self): #создаем метод предоставляющий урожай
        self.tomatoes.clear() #очищаем список помидоров

class Gardner: #создаем класс Садовник
    @staticmethod #помечаем метод статическим
    def knowledge_base(): #создаем метод, который выводит справку по садоводству
        print("Some knowledge about gardening") #выводим справку о садоводстве
    def __init__(self, name, plant): #метод, вызывающийся при создании объекта класса, в который мы передаем параметр Имя и Растение за которым он ухаживает
        self.name = name #создаем динамическое свойство Имя
        self._plant = plant #создаем динамическое свойство растение
    def work(self): #создаем метод Ухаживать за растением
        self._plant.grow_all() #выращиваем куст
    def harvest(self): #создаем метод Собрать урожай
        if self._plant.all_are_ripe(): #проверяем, что все помидоры на кусте выращены
            self._plant.give_away_all() #если все выращены - собираем
        else: #если нет
            print("Some tomato not grow") #выводим предупреждение


Gardner.knowledge_base()
tomato_bush = TomatoBush(3)
gardner = Gardner("Dmitriy", tomato_bush)
gardner.work()
gardner.work()
gardner.harvest()
gardner.work()
gardner.harvest()



