"""Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”
"""

my_str = (lambda name: f"hello, {name}")("Boris")
print(my_str)