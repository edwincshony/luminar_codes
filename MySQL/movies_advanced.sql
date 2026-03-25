-- Create Database
CREATE DATABASE mdb;

-- Use Database
USE mdb;

-- Create Table
CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    genre VARCHAR(100),
    language VARCHAR(100),
    runtime INT
);

-- Insert 50 Movies (Different Languages)

INSERT INTO movie (title, year, genre, language, runtime) VALUES
('Inception', 2010, 'Sci-Fi', 'English', 148),
('Parasite', 2019, 'Thriller', 'Korean', 132),
('Amélie', 2001, 'Romantic Comedy', 'French', 122),
('3 Idiots', 2009, 'Drama', 'Hindi', 170),
('Spirited Away', 2001, 'Animation', 'Japanese', 125),
('City of God', 2002, 'Crime', 'Portuguese', 130),
('The Intouchables', 2011, 'Drama', 'French', 112),
('Dangal', 2016, 'Sports Drama', 'Hindi', 161),
('Your Name', 2016, 'Animation', 'Japanese', 106),
('Roma', 2018, 'Drama', 'Spanish', 135),

('Crouching Tiger Hidden Dragon', 2000, 'Action', 'Mandarin', 120),
('Life Is Beautiful', 1997, 'Drama', 'Italian', 116),
('Baahubali: The Beginning', 2015, 'Epic', 'Telugu', 159),
('Baahubali: The Conclusion', 2017, 'Epic', 'Telugu', 167),
('Drishyam', 2013, 'Thriller', 'Malayalam', 160),
('Super Deluxe', 2019, 'Drama', 'Tamil', 176),
('Kumbalangi Nights', 2019, 'Drama', 'Malayalam', 135),
('Vikram Vedha', 2017, 'Action', 'Tamil', 147),
('Train to Busan', 2016, 'Horror', 'Korean', 118),
('Oldboy', 2003, 'Thriller', 'Korean', 120),

('Pan’s Labyrinth', 2006, 'Fantasy', 'Spanish', 118),
('The Lives of Others', 2006, 'Drama', 'German', 137),
('Run Lola Run', 1998, 'Thriller', 'German', 80),
('A Separation', 2011, 'Drama', 'Persian', 123),
('PK', 2014, 'Comedy', 'Hindi', 153),
('Lagaan', 2001, 'Drama', 'Hindi', 224),
('Joker', 2019, 'Drama', 'English', 122),
('Interstellar', 2014, 'Sci-Fi', 'English', 169),
('The Dark Knight', 2008, 'Action', 'English', 152),
('Gladiator', 2000, 'Action', 'English', 155),

('The Godfather', 1972, 'Crime', 'English', 175),
('Fight Club', 1999, 'Drama', 'English', 139),
('Pulp Fiction', 1994, 'Crime', 'English', 154),
('The Shawshank Redemption', 1994, 'Drama', 'English', 142),
('Forrest Gump', 1994, 'Drama', 'English', 142),
('Avengers: Endgame', 2019, 'Action', 'English', 181),
('Titanic', 1997, 'Romance', 'English', 195),
('The Matrix', 1999, 'Sci-Fi', 'English', 136),
('Slumdog Millionaire', 2008, 'Drama', 'Hindi/English', 120),
('RRR', 2022, 'Action', 'Telugu', 182),

('Minnal Murali', 2021, 'Superhero', 'Malayalam', 158),
('Master', 2021, 'Action', 'Tamil', 179),
('Kaithi', 2019, 'Action', 'Tamil', 145),
('Arjun Reddy', 2017, 'Drama', 'Telugu', 182),
('Sairat', 2016, 'Romance', 'Marathi', 174),
('Court', 2014, 'Drama', 'Marathi', 116),
('Fandry', 2013, 'Drama', 'Marathi', 105),
('Tumbbad', 2018, 'Horror', 'Hindi', 104),
('Gully Boy', 2019, 'Drama', 'Hindi', 154),
('Article 15', 2019, 'Crime', 'Hindi', 130);

select * from movie;

-- display all unique languages

select distinct language from movie;

-- display unique genres

select distinct genre from movie;

-- display names of Malayalam movies

select title from movie where language = "malayalam";

-- year wise summary
-- GROUP BY It groups all rows that have the same year.

select year,count(*) as movie_count from movie group by year order by movie_count desc;

-- language wise summary
-- GROUP BY It groups all rows that have the same language.

select language,count(*) as language_count from movie group by language order by language_count desc;

-- genre summary 

select genre,count(*) as movie_count from movie group by genre order by movie_count desc;

-- genre summary > 3

select genre,count(*) as movie_count from movie group by genre having movie_count > 3 order by movie_count desc;

-- highest run time

-- nested query
-- inner query works first then outer query works

-- return movie details with max runtime
select * from movie where runtime =  (select max(runtime) as max_runtime from movie);

-- return movie details with min runtime
select * from movie where runtime =  (select min(runtime) as max_runtime from movie);

-- retutn movie details greater than avg runtime
select * from movie where runtime > (select avg(runtime) as avg_runtime from movie);

-- find movies released in latest year from table data
select * from movie order by year desc LIMIT 1;
-- OR
select * from movie where year = (select max(year) from movie);

-- find movies in the same year as Kumbalangi Nights
select * from movie where year =  (select year from movie where title = 'Kumbalangi Nights');

-- find movies with runtime > the run time of Titanic
select * from movie where runtime > (select runtime from movie where title = "Titanic");
