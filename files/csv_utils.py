"""1. чтение
2. запись
3. добавление позиции в конец добавление строки в позицию
4. удаление ряда (по умолчанию последнего, или по запросу)

"""

import csv


def read(file):
    with open(file, "r") as my_csv:
        my_csv_read = csv.reader(my_csv)
        content_my_csv = []
        for row in my_csv_read:
            content_my_csv.append(row)
    return content_my_csv


def write(file, fields, rows):
    with open(file, "w") as my_csv:
        my_csv_write = csv.writer(my_csv)
        my_csv_write.writerow(fields)
        my_csv_write.writerows(rows)
    return my_csv_write


def write_row(file, row, index=-1):
    if index == -1:
        with open(file, "a") as my_csv:
            my_csv_write_end = csv.writer(my_csv)
            my_csv_write_end.writerow(row)
    else:
        my_csv = read(file)
        my_csv.insert(row, index)
        write(file, my_csv)


def delete_row(file, index=-1):
    my_list = read(file)
    if index == -1:
        my_list.pop(len(my_list))
    else:
        my_list.pop(index)
    write(file, my_list[0], my_list[1::])