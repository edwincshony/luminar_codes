"""1. Write a Python program to read the file move.csv and print the first 5 rows.
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = list(DictReader(fr))

# print(data[:5])

for row in data[:5]:

    print(row)