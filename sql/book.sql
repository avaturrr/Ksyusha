-- Создать файл book.sql. Создать таблицу Book.
-- Атрибуты: id(integer primary key autoincrement),
-- title(varchar), pages(int), author(varchar), price(float)
-- 07 Получить название, год и цену всех книг, год которых равен 2010

create table book (
    id integer primary key autoincrement,
    title varchar,
    pages integer,
    author varchar,
    price float
);

alter table book add column release_year integer;

insert into book (title, pages, author, price, release_year) VALUES ('qwe', 300, 'Fds', 20.2, 1993),
('asd', 340, 'Gfg', 34.4, 2002),
('hjkl', 350, 'Poi', 38.4, 2013), ('asfjh', 380, 'Pkdf', 3.4, 2007),
('kdld', 340, 'Gfg', 34.4, 2002);

select release_year, title, price from book;

select title, release_year, price from book where release_year = 2010;