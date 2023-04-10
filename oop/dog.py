"""oop_01
Создать файл dog.py.
Создать пустой класс Dog
oop_02
Создать два объекта класса Dog. Вывести их на экран
oop_03
Добавить два метода в класс Dog: jump и run.
Методы выводят на экран Jump! и Run! соответственно. Создать объект и вызвать у него все методы
oop_04
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""


class Dog:
    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")

    def bark(self):
        print("Woof-woof")

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


dog_1 = Dog(50, 14, "Bobik", 3)
print(f"height {dog_1.height}, weight {dog_1.weight}, name {dog_1.name}, age {dog_1.age}")
dog_1.run()
dog_1.jump()
dog_1.bark()
dog_2 = Dog(100, 30, "Tuzik", 4)
print(f"height {dog_2.height}, weight {dog_2.weight}, name {dog_2.name}, age {dog_2.age}")
dog_2.jump()
dog_2.run()
dog_2.bark()
