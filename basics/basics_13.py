"""Пользователь вводит три числа. Увеличьте первое число в два раза,
второе числа уменьшите на 3,
третье число возведите в квадрат и затем найдите сумму новых трех чисел."""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
third_number = input("Enter third number: ")
first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)
print(first_number * 2 + (second_number - 3) + third_number ** 2)