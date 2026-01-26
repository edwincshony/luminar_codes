"""
Write a program that takes a traffic light color as input and prints the corresponding action using match–case.
"""

color = input("enter the color: ")

match color:
    case "red" | "RED" | "Red" : print("Stop")

    case "green" | "GREEN" | "Green": print("Go")

    case "yellow" | "YELLOW" | "Yellow" : print("wait")

    case _: print("invalid")