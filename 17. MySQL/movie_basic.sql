create database movie_db;

use movie_db;

create table movie(

id int auto_increment primary key,
title varchar(100) unique,
language enum('malayalam','english','hindi'),
rating float not null,
run_time_in_mins int not null,
director varchar(100) not null,
genre enum("horror","comedy","thriller")
);

desc movie;

insert into movie (title,language,rating,run_time_in_mins,director,genre)
values 
('Drishyam','malayalam',8.6,160,'Jeethu Joseph','thriller'),
('Premam','malayalam',8.3,156,'Alphonse Puthren','comedy'),
('Bangalore Days','malayalam',8.3,171,'Anjali Menon','comedy'),
('Manichitrathazhu','malayalam',8.7,169,'Fazil','horror'),
('Inception','english',8.8,148,'Christopher Nolan','thriller'),
('The Dark Knight','english',9.0,152,'Christopher Nolan','thriller'),
('Interstellar','english',8.6,169,'Christopher Nolan','thriller'),
('3 Idiots','hindi',8.4,171,'Rajkumar Hirani','comedy'),
('Dangal','hindi',8.3,161,'Nitesh Tiwari','thriller'),
('Stree','hindi',7.5,128,'Amar Kaushik','horror');

select * from movie;



