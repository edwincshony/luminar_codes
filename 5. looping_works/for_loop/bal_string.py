"""

word1 = "ABCDEF"
word2 = "PQR"

balance = "DEF"
"""


word1 = input("enter word1: ")
word2 = input("enter word2: ")
word_length1 = len(word1)
word_length2 = len(word2)

if word_length1 > word_length2:

    print(word1[len(word2):])

elif word_length1 < word_length2:
    print(word2[len(word1):])

else:
    print("Not possible to take balance")

#word1="ABCD"
#word2="PQRS"
# merge_string = APBQCRDS
