"""Создать пакет school. Создать файл models.py. Создать базу school в postgre.
Создать таблицу Учебной группы(Group) с помощью sqlalchemy в декларативном стиле.
Группа характеризуется названием(name).
"""
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy_utils import database_exists, create_database

DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_NAME = "school"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}", echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer,
                      ForeignKey('group.id'),
                      nullable=False)
    group = relationship('Group',
                         foreign_keys='Student.group_id',
                         backref='students')

    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group

#
class Dairy(Base):
    __tablename__ = "dairy"
    id = Column(Integer, primary_key=True)
    avg_score = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    students = relationship("Student", foreign_keys="Dairy.student_id",
                            backref=backref("students", uselist=False))

    def __init__(self, avg_score, student):
        self.avg_score = avg_score
        self.student = student


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()