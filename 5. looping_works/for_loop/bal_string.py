"""

word1 = "ABCDEF"
word2 = "PQR"

balance = "DEF"
"""

# efficient approach

word1 = "ABCDEF"
word2 = "PQR"
result = ""

min_len = min(len(word1),len(word2))

result += word1[min_len:] + word2[min_len:]

print(result)

# merge 
#word1="ABCD"
#word2="PQRS"
# merge_string = APBQCRDS

# efficient version

w1 = "abcdef"
w2 = "pqrs"

result = ""

min_len = min(len(w1), len(w2))

for i in range(min_len):
    result += w1[i] + w2[i]

result += w1[min_len:] + w2[min_len:]

print(result)

# my approach
word1 = "ABCDEF"
word2 = "PQR"
word_length1 = len(word1)
word_length2 = len(word2)

if word_length1 > word_length2:

    print(word1[len(word2):])

elif word_length1 < word_length2:
    print(word2[len(word1):])

else:
    print("Not possible to take balance")


