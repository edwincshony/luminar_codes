"""
Festival Discount Checker
Problem Statement 
A shop offers a discount on items priced above ₹500. Write a program to accept prices of 10 items and print whether each item gets a discount immediately.
Input Format Ten integers representing item prices.
Output Format “Item X gets a discount” or “Item X no discount” for each item.
Sample Input:
200
800
450
550
999
120
700
350
50
600
Sample Output:
Item 1 (₹200) no discount.
Item 2 (₹800) gets a discount.
Item 3 (₹450) no discount.
Item 4 (₹550) gets a discount.
Item 5 (₹999) gets a discount.
Item 6 (₹120) no discount.
Item 7 (₹700) gets a discount.
Item 8 (₹350) no discount.
Item 9 (₹50) no discount.
Item 10 (₹600) gets a discount.
"""

for i in range(1,11):

    price = int(input())

    if price >= 500:

        print(f"Item {i} (₹{price}) gets a discount.")

    else:

        print(f"Item {i} (₹{price}) no discount.")
