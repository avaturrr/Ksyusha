"""Ввести строку с клавиатуры
Если длина строки больше 5 - вывести значение на экран
Если длина строки меньше 5 - вывести строку “Need more!”
Если длина строки равна 5 - вывести строку “len str == 5”
"""

line = input("Enter sentence: ")
if len(line) > 5:
    print(len(line))
elif len(line) < 5:
    print("Need more")
else: print("len str == 5")