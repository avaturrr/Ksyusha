"""Создать класс Book и сессию в файле book.py. Создать файл sqlalchemy_06.
 Импортировать Book и сессию из модуля book. Создать 3 книги с помощью сессии."""
from sqlalchemy.orm import registry

from my_sqlalchemy.book import Book, user_table, session1

mapper_registry = registry()
mapper_registry.map_imperatively(Book, user_table)
book_1 = Book("qwe", 34, "Dkjl", 123, 1990)
book_2 = Book("lkj", 45, "Ulk", 12, 1999)
book_3 = Book("poj", 340, "Lkjlk", 56, 2005)
session1.add_all([book_1, book_2, book_3])
session1.commit()
