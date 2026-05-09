"""
Movie Ticket Discount
Problem Statement 
A cinema gives discounts:
•
Age <12: 50% discount
•
Age 12–18: 30% discount
•
Age >60: 40% discount Else: No discount
Write a program to read ages of 5 customers and display their discount.
Input Format Five integers representing ages.
Output Format Discount percentage for each customer.
Constraints age ≥0
Sample Input:
10
15
25
61
35
Sample Output:
Customer 1 discount: 50%
Customer 2 discount: 30%
Customer 3 discount: 0%
Customer 4 discount: 40%
Customer 5 discount: 0%
"""

for i in range(1,6):

    age = int(input())

    if age < 12:

        discount = 50

    elif age >= 12 and age <= 18:

        discount = 30

    elif age>60:

        discount = 40

    else:

        discount = 0

    print(f"Customer {i} discount: {discount}%")