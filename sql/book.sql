-- Создать файл book.sql. Создать таблицу Book.
-- Атрибуты: id(integer primary key autoincrement),
-- title(varchar), pages(int), author(varchar), price(float)

create table book (
    id integer primary key autoincrement,
    title varchar,
    pages integer,
    author varchar,
    price float
);

