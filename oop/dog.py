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
oop_05
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя
и меняет атрибут имени у объекта. Создать один объект класса.
Вывести имя. Вызвать метод change_name. Вывести имя.
oop_06
Добавить в метод инициализации новый приватный атрибут - master.
Создать метод get_master() который возвращает значение атрибута master.
oop_08
Сделать все атрибуты класса Dog приватными. Сделать для каждого атрибута
getter и setter используя декораторы. Все change методы удалить
"""


class Dog:
    def __init__(self, height, weight, name, age, master, city="Minsk"):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__city = city

    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")

    def bark(self):
        print("Woof-woof")

    def get_master(self):
        return self.__master

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        self.__city = new_city
        return self.__city
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, new_weight):
        self.__height = new_weight
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def master(self):
        return self.__master
    @master.setter
    def master(self, new_master):
        self.__master = new_master

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city




dog_1 = Dog(50, 14, "Bobik", 3, "b")
print(f"height {dog_1.height}, weight {dog_1.weight}, name {dog_1.name}, age {dog_1.age}")
dog_1.run()
dog_1.jump()
dog_1.bark()
print(dog_1.get_city())
print(dog_1.set_city("Brest"))
dog_2 = Dog(100, 30, "Tuzik", 4, "t")
print(f"height {dog_2.height}, weight {dog_2.weight}, name {dog_2.name}, age {dog_2.age}")
dog_2.jump()
dog_2.run()
dog_2.bark()
print(dog_2.get_city())
print(dog_2.set_city("Pinsk"))

dog_3 = Dog(13, 2, "Woof", 1, "w")
print(f"Dog_3 name {dog_3.name}")

print(f"dog_3 master {dog_3.get_master()}")
