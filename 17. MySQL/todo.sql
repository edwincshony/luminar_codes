-- table relations
create database todo_db;

use todo_db;

create table user(

id int auto_increment primary key,
name varchar(200) not null,
email varchar(200) not null unique,
phone varchar(14) not null unique);

create table task(

id int auto_increment primary key,
title varchar(200) not null,
user_id int not null,
status enum("pending","completed") default "pending",
date datetime default current_timestamp,
foreign key (user_id) references user(id) on delete cascade
);

desc task;

select * from todo_db.task;

insert into user (name,email,phone) values ("vipin","v@gmail.com",9658745896);

insert into task(title,user_id) values ("emi",1);
insert into task(title,user_id) values ("bill payment",1);
select * from task;