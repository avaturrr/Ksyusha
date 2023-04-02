"""Имеются два текстовых файла с одинаковым числом строк.
Выяснить, совпадают ли их строки.
Если нет, то получить номер первой строки,
в которой эти файлы отличаются друг от друга."""

with open("test_06_01.txt") as first_file:
    my_first_list = first_file.readlines()
with open("test_06_02.txt") as second_file:
    my_second_list = second_file.readlines()
for i in range(len(my_first_list)):
    if my_first_list[i] != my_second_list[i]:
        print(i + 1)
