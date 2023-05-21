"""Создать файл sqlalchemy_02.py. Создать соединение к базе sa_test.db.
Создать 5 книг с помощью sqlalchemy.
"""
from sqlalchemy import create_engine, text

engin = create_engine("""sqlite:///sa_test.db""")
with engin.connect() as connection:
    insert_data = ("""insert into Book (title, pages, author, price, release_year) 
    values ("Kldksfj", 3, "Kjlkj", 300, 2009), ("Jksfj", 33, "Ojlkj", 30, 2022),
    ("Gksfj", 53, "Flkj", 30, 2001), ("Wdksfj", 603, "Wjlkj", 60, 1994),
    ("Rdksfj", 98, "Djlkj", 23, 2010)""")
    query = text(insert_data)
    connection.execute(query)
    connection.commit()