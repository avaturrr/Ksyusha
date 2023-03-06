"""Запросить у пользователя возраст. Если возраст меньше 0 - вывести Wrong input,
если меньше 18 - вывести Cola, иначе - вывести Beer"""

user_age = int(input("Введите возраст: "))
if user_age < 0:
    print("Wrong age")
elif user_age < 18:
    print("Cola")
else: print("Beer")