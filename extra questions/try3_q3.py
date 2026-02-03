"""
word1 = "ABC"

word2 = "PQR"

result = "APBQCR"
"""

word1 = "ABC"

word2 = "PQR"

result = ""

for i in range(0,len(word1)):

    result = result + word1[i] + word2[i]

print(result)