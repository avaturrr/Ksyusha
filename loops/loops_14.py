"""Создать список учеников подобной структуры.
Определить средний балл каждого студента по всем предметам,
и вывести сведения о студентах, средний балл которых больше 4"""

#создаем список
from random import randint
pupils = []
my_dict = {}
amount_student = int(input("Enter amount students: "))
for i in range(1, amount_student + 1):
    my_dict["first_name"] = input("Enter first name: ")
    my_dict["Group"] = 42
    my_dict["physics"] = randint(1, 10)
    my_dict["informatics"] = randint(1, 10)
    my_dict["history"] = randint(1, 10)
    pupils.append(my_dict)
    my_dict = {}
print(pupils)
#Определить средний балл каждого студента по всем предметам,
#и вывести сведения о студентах, средний балл которых больше 4
for a in pupils:
    average = (a["physics"] + a["informatics"] + a["history"]) / 3
    if average > 4:
        print(a)