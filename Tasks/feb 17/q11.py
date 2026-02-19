"""11. Write a program to count how many times a given number appears in a
    list.
"""

my_list = [10,20,10,40,50,700]

count = 0

number = int(input("enter number to track frequency: "))

for num in my_list:
      
    if num == number:
            
            count = count + 1

if count == 0:
      
      print(f"The number {number} doesn't exist in list")
    
else:
      
      print(f"The number {number} appears {count} time(s) in the list")