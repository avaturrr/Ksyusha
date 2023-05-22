"""Создать файл sqlalchemy_04.py.
Написать программу: пользователь вводит данные о книге.
Пользователю отображается введенная им информация.
Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
Если ответ да - выполнить метод .commit(), иначе - .rollback()"""
from time import sleep

from sqlalchemy import create_engine, text

title_user = input("Enter title: ")
pages_user = int(input("Enter pages: "))
author_user = input("Enter author: ")
price_user = int(input("Enter price: "))
release_year_user = int(input("Enter release year: "))
sleep(2)
user_choice = input("Хотите сохранить эту книгу? y / n")

engine = create_engine("sqlite:///sa_test.db")
connection = engine.connect()
trans = connection.begin()
insert_book = ("insert into Book (title, pages, author, price, release_year) "
               "values (:title_user, :pages_user, :author_user, :price_user, :release_year_user);")
query = text(insert_book).bindparams(title_user=title_user, pages_user=pages_user, author_user=author_user,
                                     price_user=price_user, release_year_user=release_year_user)
connection.execute(query)
if user_choice == "y":
    trans.commit()
else:
    trans.rollback()
