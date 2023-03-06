"""Пользователь вводит значение температуры в градусах Цельсия.
Вывести температуру  в градусах Фаренгейта.
"""

temperature = input("Enter temperature: ")
temperature = int(temperature)
print(f"Температура в градусах Фаренгейта: {(temperature * 9 / 5) + 32}")
