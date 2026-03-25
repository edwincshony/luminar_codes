Got it — alphabetical is clean, but not how you *learn*. Here’s your file reordered from **basic → advanced**, keeping everything else exactly as required.

---

# MySQL Operations Syntax Reference

## Line Comment

/*
-- line comment
*/

## List All Databases

/*
show databases;
*/

## Create Database

/*
create database database_name;
*/

## Switch to Database

/*
use database_name;
*/

## Create Table

/*
create table table_name (
column1 datatype constraints,
column2 datatype constraints,
...
);
*/

## Table Structure Description

/*
desc table_name;
*/

## Insert Data

/*
INSERT INTO table_name (column1, column2, column3, ...)
VALUES
(value1, value2, value3, ...),
(value1, value2, value3, ...);
*/

## Select All Records

/*
select * from table_name;
*/

## Select Specific Columns

/*
select column1, column2 from table_name;
*/

## Where Clause

/*
select * from table_name where condition;
*/

## AND / OR Conditions

/*
select * from table_name where condition1 and condition2;
select * from table_name where condition1 or condition2;
*/

## Not Equal

/*
select * from table_name where column_name != value;
*/

## Between

/*
select * from table_name where column_name between value1 and value2;
*/

## Like

/*
select * from table_name where column_name like 'pattern';
*/

## Order By

/*
select * from table_name order by column_name asc;
select * from table_name order by column_name desc;
*/

## Limit

/*
select * from table_name limit number;
*/

## Limit with Offset

/*
select * from table_name limit number offset offset_value;
*/

## Distinct

/*
select distinct column_name from table_name;
*/

## Aggregate Functions

/*
select max(column_name) from table_name;
select min(column_name) from table_name;
select count(*) from table_name;
select avg(column_name) from table_name;
select sum(column_name) from table_name;
*/

## Group By

/*
select column_name, aggregate_function(column_name)
from table_name
group by column_name;
*/

## Having

/*
select column_name, aggregate_function(column_name)
from table_name
group by column_name
having condition;
*/

## Subquery

/*
select * from table_name where column_name = (select column_name from table_name);
*/

## Update

/*
update table_name
set column1 = value1, column2 = value2
where condition;
*/

## Delete

/*
delete from table_name where condition;
*/


Update my MySQL syntax reference MD file using this new class content:

[PASTE YOUR NEW CLASS CONTENT HERE]

Rules:
1. Extract only syntax examples and operations
2. Use the exact same structure as my current file (headers + /* */ blocks)
3. Add new sections alphabetically under existing ones
4. Don't add explanations, just clean syntax
5. Keep format: # Main header, ## Section headers, /* syntax */
6. No ```sql``` code blocks - use /* */ only
7. Output complete updated MD file

Current file:
[PASTE YOUR CURRENT MD FILE HERE]