"""Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.

Примечание: данное задание подразумевает самостоятельное изучение
принципов работы со временем в Python(библиотека datetime)
"""
from random import randint
import datetime
arr = []
my_dict = {}
for i in range(5):
    my_dict["number_train"] = randint(1, 10)
    my_dict["point A"] = "A"
    my_dict["point B"] = "B"
    my_dict["Departure time"] = str(datetime.time(randint(0, 12), randint(0, 59)))
    my_dict["Arrival time"] = str(datetime.time(randint(12, 23), randint(0, 59)))
    arr.append(my_dict)
    my_dict = {}
print(arr)
filtred_arr = []
for j in arr:
    time_1 = datetime.datetime.strptime(j["Departure time"], "%H:%M:%S")
    time_2 = datetime.datetime.strptime(j["Arrival time"], "%H:%M:%S")
    dif = datetime.datetime.strptime(str(time_2 - time_1), "%H:%M:%S")
    if dif > datetime.datetime.strptime("07:20:00", "%H:%M:%S"):
        filtred_arr.append(j)
print(filtred_arr)
