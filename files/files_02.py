"""Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры."""

my_file = open("test2.txt", "w+")
for line in range(6):
    my_file.writelines([input("Enter line:")])
    my_file.write("\n")
my_file.close()
with open("test2.txt") as my_file:
    line = my_file.readlines()
    print(line)
