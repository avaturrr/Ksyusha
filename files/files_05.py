"""Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется."""

with open("test_05_01.txt") as my_first_file:
    my_list = my_first_file.readlines()
    count = 0
    for line in my_list:
        count += 1
        if count % 2:
            with open("test_05_03.txt", "a") as my_th_file:
                my_th_file.write(line)
        else:
            with open("test_05_02.txt", "a") as my_second_file:
                my_second_file.write(line)
