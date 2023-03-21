"""Ввести строку с клавиатуры. Вернуть результат логического выражения:
длина строки не меньше 8 или в строке есть “python”."""

my_line = input("Enter line: ")
print(len(my_line) >= 8 or "python" in my_line)