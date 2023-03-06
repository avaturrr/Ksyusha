"""Ввести почтовый адрес. Проверить доменное имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись “DOMAIN NAME is not supported’"""

line = input("Enter email: ")
if "gmail.com" in line:
    print(line)
else:
    print("DOMAIN NAME is not supported")