"""
8. Reverse a string using a for loop.

"""

word = input("enter string: ")

reverse = ""

for i in word:

    reverse = i + reverse

print(reverse)


word = "edwin"

result = ""

word_length = len(word)-1 #4

for i in range(word_length,-1,-1): #4,-1,-1

    result = result + word[i] # ""+"n"="n", "n"+"i"="ni"

print(result)



