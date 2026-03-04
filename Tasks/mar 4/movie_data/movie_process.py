
fr = open("Tasks\\mar 4\\movie_data\\movie.csv")

"""Write a Python program to read the file move.csv and print the first 5 rows."""

from csv import DictReader, DictWriter



data = DictReader(fr)

# for row in data[:5]:

#     print(row)

"""Write a program to count how many movie records are present in move.csv (excluding the header)."""

# print(len(data))

"""3. Write a program to read the header row from move.csv and print all column names.
"""

# print(data.fieldnames)

"""4. Accept a year from the user and display all movie titles released in that year from move.csv.
"""

# n = int(input("enter a year to fetch movie names: "))

# movie_titles = filter(lambda x:int(x.get("Year of Release")) == n,data)

# for movie in movie_titles:

#     print(movie.get("Name"))

"""5. Read move.csv and print the movie with the highest rating.
"""

ratings = [float(r["Rating"]) for r in data]
max_rating = max(ratings)

high_rating = [m.get("Name") for m in data if float(m.get("Rating")) == max_rating]

print(high_rating)


"""
6. Accept a genre from the user (e.g., Action, Drama, Romance) and print all matching movies from move.csv.

"""

# genre = input("enter genre: ")

# match_genre = [m.get("Name") for m in data if m.get("Movie Categories") == genre]

# print(match_genre)

"""7. Create a new CSV file named top_rated.csv and write all movies from move.csv with a rating greater than 8.0.
"""

fw = open("Tasks\\mar 4\\movie_data\\top_rated.csv","w")

writer = DictWriter(fw,fieldnames=data.fieldnames)

for row in data:

    if float(row.get("Rating")) > 8.0:

        fw.write(row)

"""8. Read move.csv, calculate how many movies are in each genre (Movie Categories), and write the output into genre_count.txt.
"""

