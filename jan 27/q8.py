"""
Create a program using match–case that accepts a grade (A, B, C, D, F) and prints the result message.
"""

grade = input("enter grade: ")

match grade:
    case "A" | "a": print("Excellent")
    case "B" | "b": print("good")
    case "C" | "c": print("average")
    case "D" | "d": print("need improvement")
    case "F" | "f": print("fail")
    case _: print("Invalid...")