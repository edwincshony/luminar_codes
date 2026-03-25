"""6. Write a program to check whether a string is palindrome.
"""

word = "amma"
result = ""
for i in range(len(word)-1,-1,-1):

    result += word[i]

if word == result:

    print("palindrome")

else:

    print("Npalindrome")