"""
Bus Ticket Booking Counter
Problem Statement 
A bus has 30 seats. Write a program to take booking requests until the bus is full. After each booking, display the remaining seats.
Input Format Integer requests for seats by each customer.
Output Format Seats booked and remaining seats. When no seats are left, print “Bus Full. No more bookings.”
Sample Input:
5
10
15
5
Sample Output:
5 seats booked. Seats left: 25
10 seats booked. Seats left: 15
15 seats booked. Seats left: 0
Bus Full. No more bookings.
"""

tot_seats = 30

while True:

    seats = int(input("Enter seats to book: "))

    tot_seats -= seats

    print(f"{seats} seats booked. Seats left: {tot_seats}")

    if tot_seats == 0:

        print("Bus Full. No more bookings.")

        break