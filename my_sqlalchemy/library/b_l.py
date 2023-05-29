from sqlalchemy.orm import sessionmaker

from my_sqlalchemy.library.models import engine, Book
from my_sqlalchemy.library.ui import create_data

session = sessionmaker(bind=engine)()


def create():
    my_list = create_data()
    book = Book(my_list[0], my_list[1], my_list[2], my_list[3])
    session.add(book)
    session.commit()


def read():
    book = session.query(Book)
    for i in book:
        print(i.title, i.author, i.release_year, i.price)


def update():
    pass


def delete():
    pass


def filter_by_author():
    pass
