"""Имеется текстовый файл.
Переписать в другой файл все его строки с заменой
в них символа 0 на символ 1 и наоборот."""

with open("test_04_01.txt") as my_file:
    my_list = my_file.readlines()
for item in my_list:
    item = list(item)
    for letter in range(len(item)):
        if item[letter] == "0":
            item[letter] = "1"
        elif item[letter] == "1":
            item[letter] = "0"
    with open("test_04_02.txt", "a") as my_new_file:
        my_new_file.write("".join(item))
