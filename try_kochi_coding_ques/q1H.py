"""
Parking Lot Fee Calculator
Problem Statement 
A parking lot charges ₹20 for the first hour and ₹10 for each additional hour. Write a program to repeatedly accept parking hours for each vehicle until the user enters 0. For each entry, display the parking charge immediately.
Input Format An integer representing parking hours for each vehicle. Input ends when 0 is entered.
Output Format For each entry, output the parking charge. Print “Exiting…” when 0 is entered.
Sample Input:
1
3
0
Sample Output:
Parking charge: ₹20
Parking charge: ₹40
Exiting...
"""


while True:

    hour = int(input("enter the hour: "))

    if hour == 0:

        print("Exiting...")

        break

    if hour == 1:

        charge = 20 

    else:

        charge = 20 + (hour-1) * 10

    print("Amount is:",charge)



        

    