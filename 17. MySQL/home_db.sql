# home_db
# property [id,sqft,bhk,price,location,is_avilable,note]

create database home_db;

use home_db;

create table property(

	id int auto_increment primary key,
    sqft float not null,
    bhk int not null,
    price int not null,
    location varchar(200) not null,
    is_avilable boolean,
    note varchar(200)
);