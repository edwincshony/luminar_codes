"""
Library Fine Tracker
Problem Statement
A library charges fines as follows:
•
0–5 days late → ₹2 per day
•
6–10 days late → ₹3 per day
•
10 days late → ₹5 per day
Write a program that reads the late days for 5 members one by one and prints the fine for each member immediately.
Input Format Five integers, each indicating days late for one member.
Output Format Fine for each member on a new line.
Sample Input:
2
7
0
12
5
Sample Output:
Member 1 fine: ₹4
Member 2 fine: ₹21
Member 3 fine: ₹0
Member 4 fine: ₹60
Member 5 fine: ₹10
"""


fine = 1

for i in range(1,6):

    days_late = int(input("enter the late days: "))

    if days_late <= 5:

        fine = days_late * 2

    elif days_late >= 6 and days_late <= 10:

        fine = days_late * 3

    else:

        fine = days_late * 5

    print(f"Member {i} fine:{fine}")