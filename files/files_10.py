"""Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей входящих в ту или
иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+. """

from csv_utils import *

arr = [["name", "last name", "age"],
       ["a", "a1", 23],
       ["b", "b1", 3],
       ["c", "c1", 43],
       ["d", "d1", 67],
       ["e", "e1", 20]]

write("my_csv_10.csv", arr)
matrix = read("my_csv_10.csv")
count1_12 = 0
count13_18 = 0
count19_25 = 0
count26_40 = 0
count40 = 0
for row in matrix[1::]:
    if 1<=int(row[2])<=12:
        count1_12+=1
    elif 13<=int(row[2])<=18:
        count13_18+=1
    elif 19<=int(row[2])<=25:
        count19_25+=1
    elif 26<=int(row[2])<=40:
        count26_40+=1
    else:
        count40+=1
print(f"группа 1 - 12: {count1_12}\n группа 13-18: {count13_18}\n группа 19-25: {count19_25}\n "
      f"группа 26-40: {count26_40}\n группа 40+ : {count40}")
