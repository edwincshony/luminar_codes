arr = ["apple","banana","apple","orange","banana","apple","grape","grape"]

freq = {}

for word in arr:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

most_word = max(freq, key=freq.get)


print(freq)
print(most_word)