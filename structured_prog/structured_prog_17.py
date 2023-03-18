"""В массиве целых чисел с количеством элементов 19 определить максимальное число и
заменить им все четные по значению элементы.
"""
from random import randint
arr = [randint(1, 100) for a in range(0, 18)]
print(arr)
i = 0
j = 0
while i != len(arr):
    while (arr[j] >= arr[i]):
        i += 1
        if i == len(arr):
            my_max = arr[j]
            break
    j = i
print(my_max)
i = 0
while i < len(arr) - 1:
    if arr[i] % 2 == 0:
        arr[i] = my_max
    i += 1
print(arr)