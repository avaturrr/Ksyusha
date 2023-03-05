"""Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
Примечание: после ввода переменных преобразовать переменные к типу int
 >> first_number = int(first_number)
"""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
first_number = int(first_number)
second_number = int(second_number)
print("{} плюс {} равно  {}".format(first_number, second_number, (first_number + second_number)))