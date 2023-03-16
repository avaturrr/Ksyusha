"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)."""
from random import randint
arr = [1, 2, 3, 1, 2, 1, 3, 4, 5, 1, 2,1,2]
print(arr)
i = 0
j = -1
count = 0
while i < len(arr) - 1:
    i += 1
    j += 1
    while arr[i] > arr[j] and i < len(arr) - 1:
        i += 1
        j += 1
    count += 1
print(count)