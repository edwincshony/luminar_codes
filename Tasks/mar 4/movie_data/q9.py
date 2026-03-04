"""9. Read all movies from move.csv and write them into sorted_movies.csv sorted in descending order of rating.
"""
from csv import DictReader,DictWriter

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")
fw = open("Tasks\\mar 4\\movie_data\\sorted_movies.csv",'w')

Reader = DictReader(fr)

Writer = DictWriter(fw,Reader.fieldnames)

Writer.writeheader()

sorted_data = sorted(Reader,key=lambda r:float(r.get("Rating")),reverse=True)

for row in sorted_data:

    Writer.writerow(row)