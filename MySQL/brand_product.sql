create database shopwise_db;
use shopwise_db;
show databases;
create table brand(
id int auto_increment primary key,
name varchar(200) not null unique
);
create table product(
id int auto_increment primary key,
title varchar(100)not null,
price int not null,
brand_id int not null ,
foreign key (brand_id) references brand(id) on delete cascade
);
desc product;
desc brand;
insert into brand(name) values
("peterengland"),
("alensolly"),
("vanhuesen");
insert into product(title,price,brand_id)values
("shirt",1200,2),
("pant",1000,2),
("tshirt",800,1);
select*from product;
select brand.name,product.title,product.price from brand inner join product on brand.id=product.brand_id;
select brand.name,product.title,product.price from brand left join product on brand.id=product.brand_id;

use py_db;
show tables;
desc vehicle;
use gosell_db;

select * from vehicle;

