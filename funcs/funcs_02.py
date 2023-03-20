"""Написать программу для работы с матрицами:
Создание
Вывод
Сумма всех элементов
Нахождение максимального элемента
Нахождение минимального элемента.
"""

from random import randint
def my_func_create(n, m):
    arr = [[randint(1, 10) for _ in range(n)] for _ in range(m)]
    return arr
def my_func_output(arr: list):
    print(arr)
def my_func_sum(arr: list):
    sum = 0
    sum_01 = 0
    for arr_01 in arr:
        for i in arr_01:
            sum_01 += i
        sum += sum_01
    return sum
def my_func_max(arr: list):


def main():

if __name__ == '__main__':
   main()
