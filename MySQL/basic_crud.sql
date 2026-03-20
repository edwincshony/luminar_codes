-- line comment
-- query for listing all databases

show databases;

-- query for creating database student_db

create database student_db;

-- query to switch to student_db

use student_db;

-- query for creating student table


/* CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
*/

-- student [id,name,course,place,age,email]


create table student (
    id int auto_increment primary key,
    name varchar(100) not null,
    course enum('django','testing','ds','mearn','asp') default 'django',
    place varchar(100) not null,
    age int,
    email varchar(100) not null unique
);

desc student; -- Describing Table Structure

/*INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);*/

 
INSERT INTO student (name,course,place,age,email)
VALUES 
('edwin','ds','adat',22,'edwin@gmail.com'),
('dijo','django','ksu',21,'dijo@gmail.com'),
('alan','django','thiroor',21,'alan@gmail.com');

select * from student;


