"""
8. Write a function that takes a string as a parameter and returns the number of vowels in it.

"""

def num_of_vowels(word):

    VOWELS = "aeiouAEIOU"

    count = 0

    for w in word:

        if w in VOWELS:

            count = count + 1

    return count

print(num_of_vowels("umbrella"))
        