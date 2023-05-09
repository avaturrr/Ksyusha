"""Создать файл matrix.py. Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b),
по-умолчанию(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод __str__ для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент матрицы,
минимальный, сумму всех элементов.
Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами
"""
from random import randint


class Matrix:
    def __init__(self, n=5, m=5, a=0, b=0, data=None):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self.data = [[randint(a, b) for _ in range(n)] for _ in range(m)]

    def __str__(self):
        return f"{self.data}"


def max_item(matrix):
    arr_max = []
    for i in matrix.data:
        arr_max.append(max(i))
    max_element = max(arr_max)
    return max_element


def min_item(matrix):
    arr_min = []
    for i in matrix.data:
        arr_min.append(min(i))
    min_element = min(arr_min)
    return min_element


def sum_item(matrix):
    arr_sum = []
    for i in matrix.data:
        arr_sum.append(sum(i))
    sum_element = sum(arr_sum)
    return sum_element


def main():
    matrix_01 = Matrix(3, 3, 1, 10)
    print(matrix_01)
    max_element = max_item(matrix_01)
    print(max_element)
    min_element = min_item(matrix_01)
    print(min_element)
    sum_element = sum_item(matrix_01)
    print(sum_element)


if __name__ == "__main__":
    main()
