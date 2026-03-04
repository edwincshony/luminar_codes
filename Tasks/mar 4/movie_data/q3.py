"""3. Write a program to read the header row from move.csv and print all column names.
"""
from csv import DictReader
fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = DictReader(fr)

print(data.fieldnames)