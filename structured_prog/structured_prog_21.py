"""Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
"""
m = int(input("Enter m: "))
n = int(input("Enter n: "))
my_dict = {}
for i in range(m, n + 1):
    key = i
    arr = []
    for k in range(2, i):
        if i % k == 0:
            arr.append(k)
    my_dict[key] = arr
for key, value in my_dict.items():
    print(f"{key}: {value}")
