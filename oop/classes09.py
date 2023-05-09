"""Создать файл classes09.py.
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""


class CommonClass:
    def __init__(self, height, weight, color, price):
        self.__height = height
        self.__weight = weight
        self.__color = color
        self.price = price

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    def get_color(self):
        return self.__color

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    def set_color(self, new_color):
        self.__color = new_color

    def discount(self, precent_discount):
        self.price = self.price * (100 - precent_discount) / 100

    def price_compare(self, number_for_compare):
        if self.price > number_for_compare:
            print("цена больше")
        elif self.price < number_for_compare:
            print("цена меньше")
        else:
            print("цены равны")


class Fridges(CommonClass):
    pass


class Tables(CommonClass):
    pass


class WashingMachine(CommonClass):
    pass


fridge_01 = Fridges(12, 13, "white", 100)
fridge_01.price_compare(50)

table_01 = Tables(2, 4, "orange", 30)
table_01.discount(10)
print(table_01.price)

w_machine_01 = WashingMachine(1, 12, "white", 400)
w_machine_01.set_color("black")
print(w_machine_01.get_color())
