"""Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке,
то создать и вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
Для создания результирующий строки используйте срез)
"""

my_line = input("Enter line: ")
middle_letter = my_line[len(my_line) // 2]
print(middle_letter)
if middle_letter == my_line[0]:
    print(my_line[1:(len(my_line) - 1)])