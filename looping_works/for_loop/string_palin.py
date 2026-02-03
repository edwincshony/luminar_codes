"""
string palindrome
"""

word = input("enter word: ")

result = ""

word_length = len(word)-1

for i in range(word_length,-1,-1):

    result = result + word[i]

if result == word:

    print("palindrome")

else:

    print("not palindrome")