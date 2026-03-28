"""15. Write a program to count words in a sentence using dictionary.
"""

sentence = "my name is edwin c c shony"
count=0
freq = {}

for w in sentence.split():

    if w in freq:

        freq[w] += 1

    else:

        freq[w] = 1

print(freq)