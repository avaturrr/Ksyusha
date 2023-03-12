"""Создать список с фамилиями.
Вывести все фамилии, которые начинаются на П и заканчиваются на а"""
#создаем список фамилий
list_last_names = []
while True:
    last_name = input("Enter last_name or stop: ")
    if last_name == "stop":
        break
    else:
        list_last_names.append(last_name)
print(f"Список фамилий: {list_last_names}")
#фильтруем список
filtered_list_last_names = []
for i in list_last_names:
    if i[0] == "П" and i[len(i) - 1] == "а":
        filtered_list_last_names.append(i)
print(f"Фильтрованный список фамилий: {filtered_list_last_names}")