"""Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""
from random import randint
from time import sleep


def my_generator():
    while True:
        yield randint(-100, 100)
        sleep(1)


def main():
    random_number = my_generator()
    for i in random_number:
        print(i)


if __name__ == "__main__":
    main()
