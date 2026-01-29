number = int(input("enter number: ")) # 123

while(number!=0): # 123 != 0 T, 12 != 0 T, 1 != 0 T, 0!=0 F

    last_digit = number % 10 # 123 % 10 = 3, 12 % 10 = 2, 1 % 10 == 1

    print(last_digit) #3 2 1

    number = number // 10 #123 // 10 = 12, 12 // 10 = 1, 1 // 10 = 0

