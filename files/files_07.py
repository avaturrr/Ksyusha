"""Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл
"""
import json
from random import randint

matrix = [[randint(1, 9) for _ in range(5)] for _ in range(5)]

with open("test_07.json", "w") as my_file:
    data = json.dumps(matrix)
    print(type(data), data)
    my_file.write(data)

with open("test_07.json", "w") as file:
    data = json.load(file)
    for i in data:
        for j in range(len(i)):
            if j % 2 == 0:
                i[j] = 0
    print(data)
