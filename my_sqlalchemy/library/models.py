from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///library.db")
connection = engine.connect()
Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    release_year = Column(Integer)
    price = Column(Integer)

    def __init__(self, title, author, release_year, price):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.price = price


Base.metadata.create_all(engine)
