word = "racecarfast"

# print non recursive character
# print recursive character whose count > 2

non_recursive = [w for w in word if word.count(w) == 1]

print(non_recursive)

recursive = {w:word.count(w) for w in word if word.count(w) > 2}

print(recursive)