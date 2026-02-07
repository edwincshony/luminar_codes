#w.a.p to print factorial of a number using for loop

number = int(input("enter number: "))

fact = 1

for i in range(1,number+1):

    fact = fact * i

print(f"Factorial for number {number} is {fact}")