"""Дан список целых чисел.
Подсчитать сколько четных чисел в списке
"""

from random import randint
arr = [randint(-9, 9) for i in range(1, 5)]
print(arr)
i = 0
count = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        count += 1
    i += 1
print(f"количество четных чисел {count}")