"""Создать файл sqlalchemy_07.py. Получить все книги и вывести их на экран в формате
год - название - автор"""
from sqlalchemy.orm import registry

from my_sqlalchemy.book import session1, Book, session2, user_table

mapper_registry = registry()
mapper_registry.map_imperatively(Book, user_table)
all_book = session2.query(Book)
for book in all_book:
    print(book.release_year, book.title, book.author)