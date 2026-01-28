"""
4. Movie Ticket Booking
------------------------------------
Task:
- Ask for age

If age ≥ 18:
    - Ask for seat availability
    - If seats available:
        "Ticket booked"
    - Else:
        "House full"
Else:
    "Not eligible to watch the movie"
"""

age = int(input("enter age: "))

if age >= 18:
    availability = input("is seats availabile (Y/N): ")
    if availability == "Y":
        print("Ticket booked")
    elif availability == "N":
        print("House full")
    else:
        print("invalid")
else:
    print("Not eligible to watch the movie")