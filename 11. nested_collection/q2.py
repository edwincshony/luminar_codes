# return result as dictionary with key-value pairs

lst = [10,11,12,11,10,13,13]

num_count = {n:lst.count(n) for n in lst}

print(num_count)

print("--------------------")

# display character count

word = "racecar"

char_count = {w:word.count(w) for w in word}

print(char_count)