"""Создать файл sqlalchemy_12.py. Получить всех студентов и создать для каждого дневник."""
from my_sqlalchemy.school.models import session, Student, Dairy

student_all = session.query(Student).all()
arr = []
for student in student_all:
    avg_score = float(input(f"Enter avg score for student {student.firstname} -"))
    diary = Dairy(avg_score, student)
    arr.append(diary)

session.add_all(arr)
session.commit()
