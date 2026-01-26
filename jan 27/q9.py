"""
9. Write a program using match–case to check whether an entered shape is:
* "c" → Circle
* "r" → Rectangle
* "s" → Square
"""

shape = input("enter the shape: ")

match shape:
    case "c": print("Circle")
    case "r": print("Rectangle")
    case "s": print("Square")
    case _: print("invalid ...")