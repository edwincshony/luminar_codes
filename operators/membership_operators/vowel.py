"""

read a character eg: ch = "a"
display character is vowel if ch is a vowel
display character is not vowel

"""

character = input("enter character: ")

VOWELS = "aeiouAEIOU"

if character in VOWELS:
    print(character,"is a vowel")
else:
    print(character,"is not a vowel")
