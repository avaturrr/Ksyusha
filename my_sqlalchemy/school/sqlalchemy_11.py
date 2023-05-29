"""Создать таблицу Студент(Student) с помощью sqlalchemy в файле models.py.
Студент характеризуется именем(firstname) и фамилией(lastname) и группой к которой он приурочен.

Создать файл sqlalchemy_11.py. Создать две группы. Добавить в каждую по три студента.
"""
from my_sqlalchemy.school.models import Student, session
from my_sqlalchemy.school.sqlalchemy_10 import group_1, group_2

student_1 = Student('max', 'ivanov', group=group_1)
student_2 = Student('igar', 'ivanovich', group=group_1)
student_3 = Student('Valera', 'ivanko', group=group_1)
student_4 = Student('far', 'petrov', group=group_2)
student_5 = Student('har', 'petrovich', group=group_2)
student_6 = Student('baks', 'gari', group=group_2)

session.add_all([student_1, student_2, student_3, student_4, student_5, student_6])
session.commit()
