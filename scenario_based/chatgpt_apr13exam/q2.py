# (a) Count vowels
count=0
word = input("enter word: ").lower()

VOWELS = "aeiou"

for l in word:

    if l in VOWELS:

        count += 1

print(count)
