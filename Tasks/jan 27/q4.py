"""
4.Write a program using match–case to print the type of triangle based on a given input:
* "e" → Equilateral
* "i" → Isosceles
* "s" → Scalene
"""

choice = input("enter value: ")

match choice:
    case "e" | "E": print("Equilateral")
    case "i" | "I": print("Isosceles")
    case "s" | "S": print("Scalene")
    case _: print("invalid ...")