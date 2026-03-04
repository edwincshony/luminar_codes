"""2. Write a program to count how many movie records are present in move.csv (excluding the header).
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

data = list(DictReader(fr))

print(len(data))