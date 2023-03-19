"""Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
Найти сумму всех элементов матрицы, которые кратны 3."""

from random import randint
n = int(input("Enter n: "))
my_list = []
my_list_in = []
sum = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        item = randint(1, 9)
        my_list_in.append(item)
        if item % 3 == 0:
            sum += item
    my_list.append(list(my_list_in))
    my_list_in = []
print(my_list)
print(sum)