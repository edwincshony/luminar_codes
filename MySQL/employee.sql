/* MySQL Practice Task – Employee Database

Database Setup Create a database named: empdb

Table Structure Create a table named employee with the following
fields: - id (Integer, Primary Key, Auto Increment) - name (Varchar) -
department (Varchar) - salary (Integer) - email (Varchar)

Task Instructions 1. Create the database. 2. Create the table with the
given structure. 3. Insert at least 10 employee records into the table.

Practice Questions (Write SQL Queries)

1.  Display all records from the employee table.
2.  Display only the name and salary of all employees.
3.  Display all employees who work in the IT department.
4.  Display employees whose salary is greater than 40000.
5.  Display employees whose name starts with the letter ‘A’.
6.  Display employees whose email ends with ‘gmail.com’.
7.  Display employees who belong to either HR or Finance department.
8.  Display employees whose salary is between 30000 and 45000.
9.  Display employees whose name contains exactly 5 characters.
10. Display all employees sorted by salary in ascending order.

Additional Practice (Optional)

11. Display employees sorted by salary in descending order.
12. Display employees who are not in the IT department.
13. Display employees whose email contains the letter ‘a’.
14. Display the first 5 records from the employee table. */

create database empdb;

use empdb;

create table employee(

id int auto_increment primary key,
name varchar(100),
department varchar(100),
salary int,
email varchar(100));

desc employee;

insert into employee(name,department,salary,email)
values 
("edwin","IT",50000,"edwin@gmail.com"),
("Alan","HR",55000,"alan@gmail.com"),
("dijo","Finance",30000,"dijo@gmail.com"),
("akshay","Finance",25000,"akshay@gmail.com"),
("akash","Manager",75000,"akash@gmail.com");

select * from employee;
select name,salary from employee;
select name from employee where department = "IT";
select name from employee where salary > 40000;
select name from employee where name like "A%";
select name from employee where email like "%gmail.com";
select name from employee where department = "IT" or department = "Finance";
select name from employee where salary between 30000 and 45000;
-- q9 below 2 methods
select name from employee where char_length(name) = 5;
select name from employee where name like "_____"; -- sir method
-- q10
select name from employee order by salary ASC;

-- optional questions
select name from employee order by salary desc;
select name from employee where department != "IT";
select name from employee where email like "%a%";

-- limit and offset

-- Example: Fetch first 5 records from employee table

select * from employee limit 5;

-- Example: Get 3 employees with lowest salary
select * from employee order by salary asc limit 3;

-- Example: Get the 3rd highest salary record
-- (Skip first 2 highest salaries, then return 1 record)
select * from employee order by salary desc limit 1 offset 2;

-- aggregrate functions

select max(salary) as max_salary from employee;

select min(salary) as min_salary from employee;

select count(*) as row_count from employee; -- returns row count

select avg(salary) as average_salary from employee;

select sum(salary) as total_salary from employee;

/* UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
*/

update employee set salary = 51000,email = "edwin1@gmail.com" where id = 1;

select * from employee;

delete from employee where id=4;
