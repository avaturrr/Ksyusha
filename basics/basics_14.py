"""Пользователь вводит цены 1 кг конфет и 1 кг печенья. Найдите стоимость:
а) одной покупки из 300 г конфет и 400 г печенья;
б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет."""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
first_number = int(first_number)
second_number = int(second_number)
print("a)  {}".format(first_number / 1000 * 300 + second_number / 1000 * 400))
print("б) {}".format((first_number / 1000 * 1800 + second_number /1000 * 2000) * 3))
