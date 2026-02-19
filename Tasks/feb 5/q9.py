"""
9.Write a program using nested loops to display:

Outer loop 1
Inner loop 1
Inner loop 2
"""

for outer in range(1, 2):   # outer loop runs once
    print(f"Outer loop {outer}")
    
    for inner in range(1, 3):  # inner loop runs twice
        print(f"Inner loop {inner}")


