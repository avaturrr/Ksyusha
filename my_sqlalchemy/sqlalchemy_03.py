"""Создать файл sqlalchemy_03.py.
Написать программу: пользователь вводит год. Отобразить на экране те книги,
год которых меньше введенного пользователем года. Если таких книг нет - вывести сообщение: Not found.
Для проверки количества записей - привести результат запроса к списку и использовать функцию len()
"""
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sa_test.db")
with engine.connect() as connection:
    year = int(input("Enter year: "))
    select_year = f"""select title, pages, author, price, release_year 
    from Book where release_year < {year}"""
    query = text(select_year)
    selected_data = connection.execute(query)
for i in selected_data:
    print(i)
