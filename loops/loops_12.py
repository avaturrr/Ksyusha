"""Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение элементов матрицы
и сумма индексов которых четна."""

#в задании список ДАН.я сначала создала
n = int(input("Enter number n: "))
m = int(input("Enter number m: "))
my_list = []
my_list_in = []
from random import randint
for i in range(1, m + 1):
    for j in range(1, n + 1):
        my_list_in.append(randint(1, 9))
    my_list.append(list(my_list_in))
    my_list_in = []
print(my_list)
#среднее арифметическое
sum = 0
count = 0
for a in my_list:
    for b in list(a):
        sum += b
        count += 1
average = sum / count
print(f"average {average}")
# количество элементов матрицы
# превосходящих среднее арифметическое значение элементов матрицы
# и сумма индексов которых четна.
count_fin = 0
for index_01, c in enumerate(my_list):
    for index_02, d in enumerate(list(c)):
        if d > average and (index_02 + index_01) % 2 == 0:
            count_fin += 1
print(f"task amount {count_fin}")