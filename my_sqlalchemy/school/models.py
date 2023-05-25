"""Создать пакет school. Создать файл models.py. Создать базу school в postgre.
Создать таблицу Учебной группы(Group) с помощью sqlalchemy в декларативном стиле.
Группа характеризуется названием(name).
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
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
        self.name

Base.metadata.create_all(engine)

