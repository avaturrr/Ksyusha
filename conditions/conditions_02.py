"""Ввести предложение. Если в предложении есть слово code -
вывести на экран Yes, иначе вывести на экран No"""

line = input("Enter sentence: ")
if "code" in line:
    print("Yes")
else:
    print("No")