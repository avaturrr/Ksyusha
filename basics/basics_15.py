"""Пользователь вводит время в минутах и расстояние в километрах.
Найдите скорость в м/c.
"""

first_number = input("Enter time: ")
second_number = input("Enter distance: ")
first_number = int(first_number)
second_number = int(second_number)
print(f"Speed {(second_number * 1000) / (first_number * 60)}")