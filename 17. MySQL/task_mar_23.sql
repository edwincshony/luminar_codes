/* Road Issues Database Assessment

Database Setup

– Create Database create database road_db;

– Use Database use road_db;

– Create Table create table road_issues( id int auto_increment primary
key, title varchar(150) not null, issue_type
enum(“pothole”,“signal”,“drainage”,“lighting”,“road_damage”) default
“pothole”, location varchar(100) not null, severity
enum(“low”,“medium”,“high”) default “low”, reported_by varchar(100),
reported_date date, status enum(“open”,“in_progress”,“resolved”) default
“open” );

------------------------------------------------------------------------

Assessment Questions

Basic Queries 1. Display all road issues 2. Display only title and
location 3. Show all issues reported in Thrissur 4. Show all pothole
issues 5. Show issues with high severity

Conditions 6. Display issues where status is open 7. Display issues
where severity is medium AND location is Kochi 8. Display issues where
severity is high OR status is open 9. Display issues reported after
2026-03-10 10. Display issues where status is not resolved

LIKE Operator 11. Find issues where title starts with “S” 12. Find
issues where title ends with “ing” 13. Find issues where location
contains “chi” 14. Find reported_by names starting with “a” 15. Find
titles with exactly 5 characters

Sorting & Limiting 16. Display all issues ordered by reported_date
(latest first) 17. Display top 3 latest issues 18. Display 2 records
after skipping first 3

Aggregate Functions 19. Find total number of issues 20. Find number of
issues in Thrissur 21. Find latest reported date 22. Find earliest
reported date

Update & Delete 23. Update status to resolved where id = 2 24. Change
severity to high for all pothole issues 25. Delete a record where id = 4

Advanced Conditions 26. Display issues where severity is high and status
is not resolved 27. Display issues where location is either Kochi or
Thrissur 28. Display issues where issue_type is not pothole 29. Display
issues reported between two dates 30. Display issues where reported_by
is NULL
*/

create database road_db;

use road_db;

CREATE TABLE road_issues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    issue_type ENUM('pothole','signal','drainage','lighting','road_damage') DEFAULT 'pothole',
    location VARCHAR(100) NOT NULL,
    severity ENUM('low','medium','high') DEFAULT 'low',
    reported_by VARCHAR(100),
    reported_date DATE,
    status ENUM('open','in_progress','resolved') DEFAULT 'open'
);

desc road_issues;

INSERT INTO road_issues(title,issue_type,location,severity,reported_by,reported_date,status)
VALUES
('Pothole near Swaraj Round', 'pothole', 'Swaraj Round', 'high', 'Arun Nair', '2026-03-01', 'open'),
('Traffic signal malfunction at East Fort', 'signal', 'East Fort Junction', 'high', 'Meera Pillai', '2026-03-02', 'in_progress'),
('Drainage blockage near KSRTC Stand', 'drainage', 'KSRTC Bus Stand Road', 'medium', 'Ravi Kumar', '2026-03-03', 'open'),
('Street light not working at Punkunnam', 'lighting', 'Punkunnam Road', 'low', 'Anjali Menon', '2026-03-04', 'resolved'),
('Damaged road near Amala Hospital', 'road_damage', 'Amala Nagar', 'medium', 'Suresh Babu', '2026-03-05', 'open'),
('Large pothole at Ollur Junction', 'pothole', 'Ollur Junction', 'high', 'Deepak Varma', '2026-03-06', 'in_progress'),
('Signal timing issue at Shornur Road', 'signal', 'Shornur Road Junction', 'medium', 'Nisha George', '2026-03-07', 'open'),
('Water logging due to drainage issue', 'drainage', 'Ayyanthole', 'high', 'Vineeth Raj', '2026-03-08', 'open'),
('Dim street lighting near Viyyur', 'lighting', 'Viyyur Road', 'low', 'Lakshmi Das', '2026-03-09', 'resolved'),
('Cracked road near Thrissur Zoo', 'road_damage', 'Zoo Road', 'medium', 'Rahul Krishnan', '2026-03-10', 'in_progress');

-- 1. Display all road issues
select * from road_issues;
-- 2. Display only title and location
select title,location from road_issues;
-- 3. Show all issues reported in Thrissur
select * from road_issues where location = "Amala nagar";
-- 4. Show all pothole issues
select title from road_issues where issue_type = "pothole";
-- 5. Show issues with high severity
select title from road_issues where severity = "high";
-- 6. Display issues where status is open
select title from road_issues where status = "open";
-- 7. Display issues where severity is medium AND location is Kochi
select title from road_issues where severity = "medium" and location = "Amala Nagar";
-- 8. Display issues where severity is high OR status is open
select title from road_issues where severity = "high" or status = "open";
-- 9. Display issues reported after 2026-03-10
select title from road_issues WHERE reported_date >= '2026-03-10';
-- 10. Display issues where status is not resolved
select title from road_issues WHERE status != "resolved";
-- 11. Find issues where title starts with “S”
select title from road_issues WHERE title like "S%";
-- 12. Find issues where title ends with “ing”
select title from road_issues WHERE title like "%ing";
-- 13. Find issues where location contains “chi”
select title from road_issues WHERE location like "%chi%";
-- 14. Find reported_by names starting with “a”
select reported_by from road_issues WHERE reported_by like "a%";
-- 15. Find titles with exactly 5 characters
select title from road_issues WHERE title like "_____";
select title from road_issues WHERE char_length(title) = 5;
-- 16. Display all issues ordered by reported_date (latest first)
select title,reported_date from road_issues order by reported_date DESC;
-- 17. Display top 3 latest issues 
select title from road_issues order by reported_date DESC LIMIT 3;
-- 18. Display 2 records after skipping first 3
select * from road_issues LIMIT 2 OFFSET 3;
-- 19. Find total number of issues
select count(*) as total_issues from road_issues;
-- 20. Find number of issues in Thrissur
select count(*) as Ayyanthole_issues from road_issues where location="Ayyanthole";
-- 21. Find latest reported date 
select reported_date from road_issues order by reported_date DESC LIMIT 1;
-- 22. Find earliest eported date
select reported_date from road_issues order by reported_date ASC LIMIT 1;
-- 23. Update status to resolved where id = 2
UPDATE road_issues set status = "resolved" where id = 2;
select * from road_issues;
-- 24. Change severity to high for all pothole issues
SET SQL_SAFE_UPDATES = 0;
UPDATE road_issues set severity = "medium" where issue_type="pothole";
select * from road_issues;
-- 25. Delete a record where id = 4
delete from road_issues where id=4; 
-- 26. Display issues where severity is high and status is not resolved
select title from road_issues where severity = "high" and status != "resolved";
-- 27. Display issues where location is either Kochi or Thrissur
select title from road_issues where location = "Swaraj Round" or location = 'Ollur Junction';
-- 28. Display issues where issue_type is not pothole
select title from road_issues where issue_type != "pothole";
-- 29. Display issues reported between two dates
select title from road_issues where reported_date between '2026-03-01' and '2026-03-07';
-- 30. Display issues where reported_by is NULL
select title from road_issues where reported_by = NULL;










