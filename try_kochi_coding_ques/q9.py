"""
First Failing Student Finder
Problem Statement 
You need to find the first student who scored below 40 marks. Ask marks one by one until you find such a student. Then print their number and marks.
Input Format Marks of students as integers.
Output Format The student number and marks when you find the first student who failed.
Constraints 0 ≤ marks ≤ 100
Sample Input:
76
89
55
39
Sample Output:
First failing student is Student 4 with marks 39
"""

count = 0

while True:

    marks = int(input())

    count += 1

    if marks < 40:

        print(f"First failing student is Student {count} with marks {marks}")

        break