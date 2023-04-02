"""Написать программу для работы с матрицами:
Создание
Вывод
Сумма всех элементов
Нахождение максимального элемента
Нахождение минимального элемента.
"""

from random import randint
def my_func_create(n: int, m: int):
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
    arr_01_max = []
    for arr_01 in arr:
        arr_max = max(arr_01)
        arr_01_max.append(arr_max)
    my_max = max(arr_01_max)
    return my_max
def my_func_min(arr: list):
    arr_01_min = []
    for arr_01 in arr:
        arr_01_min.append(min(arr_01))
    my_min = min(arr_01_min)
    return my_min

def main():
    matrix = my_func_create(3, 4)
    my_func_output(matrix)
    sum = my_func_sum(matrix)
    my_max = my_func_max(matrix)
    my_min = my_func_min(matrix)
    print(f"sum = {sum}, max = {my_max}, min = {my_min}")
if __name__ == '__main__':
   main()
