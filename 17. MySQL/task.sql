create database task_db;

use task_db;

create table task(

id int auto_increment primary key,
title varchar(200) not null,
owner varchar(200) not null,
status boolean default False,
priority enum("low","medium","high") default "medium",
date datetime default current_timestamp
);

desc task;


