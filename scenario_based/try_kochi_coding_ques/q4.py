"""
Restaurant Order Filter
Problem Statement 
A restaurant menu allows only vegetarian items with IDs 1–5. Write a program to read 7 customer orders (item IDs) and print only the vegetarian IDs as they are entered.
Input Format Seven integers representing item IDs.
Output Format Vegetarian item IDs (IDs ≤5) each on a new line.
Sample Input:
1
6
3
9
5
4
7
Sample Output:
Vegetarian item ID: 1
Vegetarian item ID: 3
Vegetarian item ID: 5
Vegetarian item ID: 4
"""

for i in range(1,8):

    item_id = int(input("enter item id: "))

    if 1 <= item_id <= 5:

        print(f"Vegetarian item ID: {item_id}")