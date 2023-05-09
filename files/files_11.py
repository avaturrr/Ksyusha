"""Создать csv файл с данными о ежедневной погоде.
Структура:  Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней."""

from csv_utils import *
import datetime

arr = [["date", "place", "degrees", "wind_speed"],
       ["2023-04-01", "Minsk", 12, 20],
       ["2023-04-02", "Brest", 13, 21],
       ["2023-04-03", "Minsk", 15, 32],
       ["2023-04-03", "Brest", 16, 4],
       ["2023-04-05", "Minsk", 18, 2],
       ["2023-03-31", "Minsk", 18, 2], ["2023-03-30", "Brest", 18, 2], ["2023-03-29", "Minsk", 18, 2],
       ["2023-03-28", "Brest", 18, 2], ["2023-03-27", "Minsk", 18, 2], ["2023-03-26", "Brest", 18, 2]]

write("my_csv_11.csv", arr)
matrix = read("my_csv_11.csv")
total_degrees = 0
total_speed = 0
count = 0

for row in matrix[1::]:
    row[0] = datetime.datetime.strptime(row[0], "%Y-%m-%d")
    row[2] = int(row[2])
    row[3] = int(row[3])
    delta = datetime.datetime.now() - row[0]
    if row[1] == "Minsk" and int(delta.days) <= 7:
        total_degrees += row[2]
        total_speed += row[3]
        count += 1

avd_degrees = total_degrees/count
avd_speed = total_speed/count

print(f"средняя скорость {avd_speed}, средняя температура {avd_degrees}")
