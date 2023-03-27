"""Дан список чисел. Вернуть список, где каждое число переведено в строку
[5, 3] -> [‘5’, ‘3’]
"""
my_list = [1, 2, 3]
new_list = list(map(lambda i: str(i), my_list))
print(new_list)