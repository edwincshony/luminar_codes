create database diet_db1;

use diet_db1;

-- id,name,email,phone

create table user(

id int auto_increment primary key,
name varchar(200) not null,
email varchar(100) not null unique,
phone varchar(10) not null unique);

desc user;

insert into user (name,email,phone)
values 
("dijo","dijo@gmail.com",8569878965),
("alan","alan@gmail.com",8569878975);

select * from user;

update user set name="akshay" where id = 1;

-- foodlog[id,title,meal_type,servingsize,calorie,date,user_id]

create table foodlog(

id int auto_increment primary key,
title varchar(200) not null,
meal_type enum("breakfast","lunch","dinner","snack") default "lunch",
serving_size varchar(200) null,
calorie int default 50,
date datetime default current_timestamp,
user_id int not null,
foreign key (user_id) references user(id) on delete cascade);

insert into foodlog (title,meal_type,serving_size,calorie,user_id) values
("pulav","breakfast","250gm",300,1);

insert into foodlog (title,meal_type,serving_size,calorie,user_id) values
("meals","lunch","450gm",450,1);

select * from foodlog;

-- inner join

-- SELECT column_name(s)
-- FROM table1
-- INNER JOIN table2
-- ON table1.column_name = table2.column_name;

select user.name, foodlog.title, foodlog.calorie from user inner join foodlog on user.id = foodlog.user_id;
