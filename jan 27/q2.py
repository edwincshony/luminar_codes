"""
Write a program that takes a character and checks whether it is a vowel or consonant using match–case.
"""

character = input("enter character: ")

match character:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("it is vowel")
    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
        print("it is consonant")

# match character:

#     case "a": print("It is a vowel")
#     case "e": print("It is a vowel")
#     case "i": print("It is a vowel")
#     case "o": print("It is a vowel")
#     case "u": print("It is a vowel")
#     case _: print("it is consonant")