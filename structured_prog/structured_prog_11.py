"""Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1
предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.
"""

from random import randint
arr = [randint(1, 15) for a in range(5)]
print(arr)
#c циклом фор
first_item = arr[0]
for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]
arr[len(arr) - 1] = first_item
print(arr)
#с циклом вайл (предыдущий список сдвинула)
first_item = arr[0]
i = 0
while i < len(arr) - 1:
    arr[i] = arr[i + 1]
    i += 1
arr[len(arr) - 1] = first_item
print(arr)