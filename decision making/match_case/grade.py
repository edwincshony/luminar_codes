"""
read grade 
A => excellent
B => good
C => average
_ => Fail
"""

grade = input("enter grade: ")

match grade:
    case "A" | "a": print("Excellent")
    case "B" | "b": print("good")
    case "C" | "c": print("average")
    case _: print("Fail")
