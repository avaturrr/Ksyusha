"""Ввести число, проверить на то, что было введено именно число.
Возвести его в куб и вывести результат на экран."""

number = input("Enter number: ")
if number.isalpha():
    print("It's not number")
else: print(int(number) ** 3)