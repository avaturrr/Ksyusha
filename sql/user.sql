--Создать скрипт user.sql.
-- Создать таблицу
-- Добавить 5 записей
-- Получить всех пользователей с вашим именем
-- Получить всех пользователей младше 25
-- Получить всех пользователей в возрасте от 15 до 18
--

create table user (
   id integer primary key autoincrement,
   firstname varchar(255),
   lastname varchar(255),
   age integer
);

insert into user (firstname, lastname, age) VALUES ('Ksjusha', 'Lkjdfl', 29),
                                                   ('Andrew', 'slkd', 30),
                                                   ('Sofia', 'slkdfj', 31),
                                                   ('Anna', 'slokefjd', 13),
                                                   ('Stefania', 'lsk', 16);
select firstname, lastname, age from user where firstname='Ksjusha';
select firstname, lastname, age from user where age < 25;
select firstname, lastname, age from user where age >= 15 and age <= 18;