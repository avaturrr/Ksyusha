"""Создать бесконечный генератор случайных чисел. Генератор должен принимать диапазон случайных чисел и смещение
Пример: a = 1, b = 10, diff = 10
1- 10
11-20
…
N +10 - M + 10
"""
from random import randint
from time import sleep


def my_generator(a, b, diff):
    while True:
        random_number = randint(a, b)
        a += diff
        b += diff
        yield random_number
        sleep(1)


def main():
    for i in my_generator(1, 3, 5):
        print(i)


if __name__ == "__main__":
    main()
