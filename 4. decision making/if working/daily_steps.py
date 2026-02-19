"""
7)Daily Steps Activity Level
    Input: steps
    Conditions:
    If steps < 5000 → Sedentary
    If steps between 5000 and 9999 → Moderately Active
    If steps >= 10000 → Active
"""

steps = int(input("enter steps: "))

if steps < 5000:
    print("Sedentary")
elif steps >= 5000 and steps <= 9999:
    print("Moderately Active")
elif steps >= 10000:
    print("Active")
