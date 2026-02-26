movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]

# display all movie title

all_movie_title = [lst[1] for lst in movies]
print("all movie titles: ",all_movie_title)


# movie with top rating

max_rating = max([lst[4] for lst in movies])
top_movies = [lst[1] for lst in movies if lst[4] == max_rating]
print(top_movies)

print("movie with top rating: ",max_rating)

# display kannada movies

kannada_movies = [lst[1] for lst in movies if lst[3] == "Kannada"]

print("kannada movies: ",kannada_movies)

# display movies whre actor is yash

yash_movies = [lst[1] for lst in movies if lst[2] == "Yash"]

# print(yash_movies)


# which language most number of movies

language_list = [lst[3] for lst in movies]
print(language_list)

language_counts  = {lst[3]:language_list.count(lst[3]) for lst in movies}

print("language counts (try): ",language_counts )

language_count_list = [[v,k] for k,v in language_counts.items()]

# print(sorted(language_count_list,reverse=True)[0][1]) #Kannada
print(sorted(language_count_list,reverse=True))

# most_common_language  = max(language_counts , key=language_counts .get) # chatgpt approach limitation only gives highest

# print("Language with most movies: ",most_common_language )
print("----------")
# movie with max budget

max_budget = max([lst[5] for lst in movies])
movie_with_max_budget = [lst[1] for lst in movies if lst[5] == max_budget]
print("Movie with maximum budget: ",movie_with_max_budget)

# languages

languages = [lst[3] for lst in movies]

print("Languages: ",languages)
