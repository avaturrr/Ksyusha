"""Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
В файле files_08 импортировать функции. С помощью функций создать файл
с информацией о товарах(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""

from csv_utils import *
#create file
write("my_csv.csv", ["name", "price", "amount", "comment"], [["a", 1, 2, "a1"], ["b", 3, 4, "b1"], ["c", 5, 6, "c1"]])
#read file
content = read("my_csv.csv")
print(content)
#add new position
write_row("my_csv.csv", ["d", 7, 8, "d1"])
#delete position 3
delete_row("my_csv.csv", 3)

