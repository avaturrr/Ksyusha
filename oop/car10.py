"""Создать файл car10.py. Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0),
отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные."""

class Car:
    def __init__(self, marka, model, year, speed=0):
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__speed = speed

    def up_speed(self, number=5):
        self.__speed += number

    def down_speed(self, number=5):
        self.__speed -= number

    def stop(self):
        self.__speed = 0
    @property
    def display_speed(self):
        print(self.__speed)

    def turn_speed(self):
        self.__speed *= (-1)

car_01 = Car("VW", "polo", 1999, speed=50)
car_01.up_speed()
car_01.display_speed
car_01.down_speed()
car_01.display_speed
car_01.turn_speed()
car_01.display_speed
car_01.stop()
car_01.display_speed
