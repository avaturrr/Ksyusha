"""Создать файл book.py. Создать класс Book.
Атрибуты: количество страниц, год издания, автор, цена.
Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.
Ошибки вызываются при попытке создания неправильного объекта.
Обработка происходит в пользовательском коде(в main).
"""


class Book:
    def __init__(self, pages: int, year: int, author: str, price: int):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price
        if not (self.pages, int) or not isinstance(self.year, int) \
                or not isinstance(self.price, int):
            raise MyException_type_int
        elif not isinstance(self.author, str):
            raise MyException_type_str


class MyException_type_int(Exception):
    def __init__(self, text="Error. Enter int type in pages, year, price"):
        super().__init__(text)


class MyException_type_str(Exception):
    def __init__(self, text="Error. Enter str type in author"):
        super().__init__(text)


def main():
    book_01 = Book("1", 1990, "Jkjlas", 300)
    print(book_01)


if __name__ == "__main__":
    main()
