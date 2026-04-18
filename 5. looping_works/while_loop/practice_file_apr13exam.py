#palindrome

#121 121
#158 != 851

number = int(input("enter number: "))

number_copy = number

rev = 0

while(number!=0):

    ld = number % 10

    rev = rev * 10 + ld

    number //= 10

print(rev)

if rev == number_copy:

    print("palindrome")

else:

    print("not palindrome")
