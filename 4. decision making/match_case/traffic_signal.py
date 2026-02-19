"""
read signals
red => STOP
green => GO
yellow => wait
_ => invalid
"""

signal = input("enter signal: ")

match signal:

    case "red" | "RED" | "Red" : print("Stop")

    case "green" | "GREEN" | "Green": print("Go")

    case "yellow" | "YELLOW" | "Yellow" : print("wait")

    case _: print("invalid")