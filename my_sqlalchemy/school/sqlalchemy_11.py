"""Создать таблицу Студент(Student) с помощью sqlalchemy в файле models.py.
Студент характеризуется именем(firstname) и фамилией(lastname) и группой к которой он приурочен.

Создать файл sqlalchemy_11.py. Создать две группы. Добавить в каждую по три студента.
"""
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column