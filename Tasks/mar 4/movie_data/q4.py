"""4. Accept a year from the user and display all movie titles released in that year from move.csv.
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = list(DictReader(fr))

year = input("enter a year: ")

movie_title_of_year = [m.get("Name") for m in data if int(m.get("Year of Release")) == int(year)]

print(movie_title_of_year)