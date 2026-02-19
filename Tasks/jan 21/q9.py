"""
9. Read two values attendance and mark and print the result of
	attendance >= 75 and mark >= 40.
"""

attendance = int(input("Enter attendence: "))

mark = int(input("Enter mark: "))

result = attendance >= 75 and mark >= 40

print(result)