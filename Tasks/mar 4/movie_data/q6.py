"""6. Accept a genre from the user (e.g., Action, Drama, Romance) and print all matching movies from move.csv.
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = list(DictReader(fr))

genre = input("enter genre: ")

match_movies = [m.get("Name") for m in data if m.get("Movie Categories") == genre]

print(match_movies)