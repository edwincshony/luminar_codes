"""8. Read move.csv, calculate how many movies are in each genre (Movie Categories), and write the output into genre_count.txt.
"""

from csv import DictReader

fr = open("Tasks\\mar 4\\movie_data\\movie.csv")
fw = open("Tasks\\mar 4\\movie_data\\genre_count.txt",'w')

Reader = DictReader(fr)

genre_summary = {}

for g in Reader:

    genre = g.get("Movie Categories")
    movie = g.get("Name")

    if genre in genre_summary:

        genre_summary[genre] += 1

    else:

        genre_summary[genre] = 1

for genre,count in genre_summary.items():

    fw.write(f"{genre}:{count}\n")


