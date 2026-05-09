"""
Employee Overtime Payment
Problem Statement 
An office stores overtime hours of 8 employees. Write a program to input overtime hours one by one and calculate the total overtime payment at ₹200 per hour.
Input Format Eight integers representing overtime hours for each employee.
Output Format Total overtime payment to all employees.
Sample Input:
3
5
0
2
4
1
6
3
Sample Output:
Total overtime payment to all employees: ₹4800
"""

charge = 0

for i in range(8):

    hour = int(input())

    charge += hour * 200

print(f"Total overtime payment to all employees: ₹{charge}")