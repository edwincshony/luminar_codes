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