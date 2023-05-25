"""Создать файл book.py.
Создать базу book.db. Создать таблицу Book с помощью механизма описания таблиц sqlalchemy.
Атрибуты: id(integer primary key), title(varchar), pages(int), author(varchar), price(float), release_year(int) """

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, Integer, VARCHAR, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///book.db", echo=True)
metadata = MetaData()
user_table = Table("Book", metadata,
                   Column("id", Integer, primary_key=True), Column("title", VARCHAR),
                   Column("pages", Integer), Column("author", VARCHAR), Column("price", Float),
                   Column("release_year", Integer))
metadata.create_all(engine)


class Book:
    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


Session = sessionmaker(bind=engine)
session1 = Session()
