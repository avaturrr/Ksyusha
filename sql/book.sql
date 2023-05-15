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

alter table book add column release_year integer;

insert into book (title, pages, author, price, release_year) VALUES ('qwe', 300, 'Fds', 20.2, 1993)
('asd', 340, 'Gfg', 34.4, 2002)
('hjkl', 350, 'Poi', 38.4, 2013) ('asfjh', 380, 'Pkdf', 3.4, 2007) ('kdld', 340, 'Gfg', 34.4, 2002);