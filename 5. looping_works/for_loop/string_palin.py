"""
string palindrome
"""

word = input("enter word: ")

result = ""

for i in range(len(word)-1,-1,-1):

    result = result + word[i]

if result == word:

    print("palindrome")

else:

    print("not palindrome")


"""
word = "python"

for i in range(len(word)-1,-1,-1):
    
    print(word[i],end="")"""






