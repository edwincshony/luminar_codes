create database book_db;

use book_db;

-- book[id,title,author,price,publisher,genre,year]

create table book(

id int auto_increment primary key,
title varchar(200) not null unique,
author varchar(200) not null,
price int not null,
publisher varchar(200) not null,
gnere enum("romance","fantacy","thriller","mystery","fiction") default "fiction",
year varchar(200) not null
);

alter table book rename column gnere to genre;
alter table book add check (price > 75);

desc book;

