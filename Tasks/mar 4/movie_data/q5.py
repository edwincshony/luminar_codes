"""5. Read move.csv and print the movie with the highest rating.
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = list(DictReader(fr))

ratings = [float(r.get("Rating")) for r in data]

max_rating = max(ratings)

high_rating = [r.get("Name") for r in data if float(r.get("Rating")) == max_rating]

print(high_rating)