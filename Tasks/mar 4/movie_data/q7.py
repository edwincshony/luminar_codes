"""7. Create a new CSV file named top_rated.csv and write all movies from move.csv with a rating greater than 8.0.
"""

from csv import DictReader,DictWriter

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")
fw = open("Tasks\\mar 4\\movie_data\\top_rated.csv",'w')

Reader = DictReader(fr) # Reader has list of dictionaries

Writer = DictWriter(fw,Reader.fieldnames)

Writer.writeheader()

for di in Reader:

    if float(di.get("Rating")) > 8.0:

        Writer.writerow(di)


