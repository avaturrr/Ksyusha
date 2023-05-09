"""Создать скрипт, который при запуске принимает неопределенное количество аргументов и считает сумму тех из них, что являются цифрами.
Пример:
python test.py 1 2 3 4 a b 5 6 -->  21
"""

import sys

args = sys.argv
print(args)
my_sum = 0
for i in args:
    if i.isdigit():
        my_sum += int(i)
print(my_sum)
