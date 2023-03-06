"""Ввести почтовый адрес. Проверить доменное имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись “DOMAIN NAME is not supported’"""

line = input("Enter email: ")
line_01 = line[::-1]
line_01 = line_01[:9]
if line_01 == "moc.liamg":
    print(line)
else:
    print("DOMAIN NAME is not supported")