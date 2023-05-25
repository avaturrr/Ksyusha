"""Создать файл sqlalchemy_08.py.
Написать программу: пользователь вводит границы фильтрации по году.
Отобразить на экране те книги, год которых находится в заданных границах.
Если таких книг нет - вывести сообщение: Not found.
"""
from sqlalchemy import and_
from sqlalchemy.orm import registry

from my_sqlalchemy.book import session3, Book, user_table

mapper_registry = registry()
mapper_registry.map_imperatively(Book, user_table)
start_year = int(input("Enter start year: "))
finish_year = int(input("Enter finish year: "))
selected_book = session3.query(Book).filter(and_(Book.release_year >= start_year,
                                                Book.release_year <= finish_year))
if selected_book:
    for book in selected_book:
        print(book.release_year, book.title, book.author)
else:
    print("Not found")
