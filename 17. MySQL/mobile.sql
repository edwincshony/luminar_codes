create database mobile_db;

use mobile_db;
-- mobile[id,title,brand,specs,price]
create table mobile(
	id int auto_increment primary key,
    title varchar(200) not null unique,
    brand varchar(200) not null,
    specs varchar(200) not null,
    price int not null
);

desc mobile;