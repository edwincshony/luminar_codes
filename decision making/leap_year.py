"""
Leap Year Explanation (Simple)

• A leap year usually occurs once every 4 years.
• Leap years have 29 days in February.
• Non-leap years have 28 days in February.

Types of years:
• Century years: years ending with 00 (e.g., 1800, 1900, 2000)
• Non-century years: all other years (e.g., 2024, 2026, 2028)

Rules to check a leap year:
• Non-century year → leap year if divisible by 4
• Century year → leap year only if divisible by 400

Examples:
• 2024 → leap year
• 2026 → not a leap year
• 2000 → leap year
• 1900 → not a leap year

This program checks whether a given year is a leap year.
"""


year = int(input("enter year:"))

            # century year check                     # non century year check

if ( year % 100 == 0 and year % 400 == 0 ) or ( year % 100 != 0 and year % 4 == 0 ): 

#(check if a year is century year and #check if a century year is a leap year) or

#(check if a year is non century year and #check if a non century year is a leap year )
    print("leap year")
else:
    print("non leap year")











# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0:
#     print("non leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("non leap year")
