"""Создать квадратную матрицу размерностью n
и заполнить ее случайными значениями от 1 до 9."""

n = int(input("Enter number: "))
my_list = []
my_list_in = []
from random import randint
for i in range(1, n + 1):
    for j in range(1, n + 1):
        my_list_in.append(randint(1, 9))
    my_list.append(list(my_list_in))
    my_list_in = []
print(my_list)
