"""Дана целочисленная квадратная матрица.
Найти в каждой строке наибольший элемент и
поменять его местами с элементом главной диагонали."""

from random import randint
arr = []
for a in range(5):
    arr.append([randint(1, 10) for b in range(5)])
print(arr)
diagonal = 0
for arr_01 in arr:
    i = 0
    j = 0
    while i != len(arr_01): #этот цикл находит максимальное число
        while arr_01[j] >= arr_01[i]:
            i += 1
            if i == len(arr_01):
                my_max = j
                break
        j = i
    arr_01[diagonal], arr_01[my_max] = arr_01[my_max], arr_01[diagonal]
    diagonal += 1
print(arr)

from random import randint
arr = []
for a in range(5):
    arr.append([randint(1, 10) for b in range(5)])
print(arr)
for index, item in enumerate(arr):
    max_01 = max(item)
    index_max_01 = item.index(max_01)
    item[index_max_01], item[index] = item[index], item[index_max_01]
print(arr)



