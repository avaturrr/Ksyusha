"""Дан список чисел. Найти произведение всех чисел, которые кратны 3.
"""

from functools import reduce

my_list = [1, 2, 3, 4, 6]
new_list = reduce(lambda x, y: x * y, list(filter(lambda number: number % 3 == 0, my_list)))
print(new_list)
