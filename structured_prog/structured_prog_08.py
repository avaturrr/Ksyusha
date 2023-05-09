"""Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
"""

from random import randint
arr = [randint(-9, 9) for i in range(1, 10)]
print(arr)
new_arr = []
for i in arr:
    new_arr.append(i * (-2))
print(new_arr)