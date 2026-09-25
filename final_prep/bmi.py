"""
bmi in range of 19 to 25
"""

# height_in_cm = 173
# weight_in_kg = 63

# height_in_m = height_in_cm/100

# bmi = weight_in_kg/height_in_m**2

# is_bmi_in_range = bmi >= 19 and bmi <= 25

# print(is_bmi_in_range)

# print('Your BMI is',bmi)
# print(f"your bmi is {bmi}")

"""

read a character eg: ch = "a"
display character is vowel if ch is a vowel
display character is not vowel

"""

# character = input("Enter a character: ")

# VOWELS = "aeiouAEIOU"

# if character in VOWELS:

#     print(character,"is a vowel")

# else:

#     print(character,"is not a vowel")

# write a pgm to print 10 to 1

# for i in range(10,0,-1):

#     print(i)

"""
w.a.p to print from 75 to 100
"""

# for i in range(75,101):

#     print(i)

"""
w.a.p to display all odd numbers from 50 to 100

"""

# for i in range(50,101):

#     if i % 2 != 0:

#         print(i)

#w.a.p to print factorial of a number using for loop

# num = 5

# fact=1

# for i in range(1,num+1):

#     fact = fact * i

# print(fact)

"""
w.a.p to print from 10 to 1
"""

# for i in range(10,0,-1):
#     print(i)

"""
break,continue
"""

# for i in range(1,11):

#     if i == 5:

#         break

#     print(i)

# print("THE END\n")

# for i in range(1,11):

#     if i == 5:

#         continue

#     print(i)

# print("THE ENDDD\n")

"""
print common divisors of 2 numbers
"""

# number1 = int(input("Enter the number1: "))
# number2 = int(input("Enter the number2: "))
# number3 = int(input("Enter the number3: "))

# if number1 < number2 and number1 < number3:

#     smallest = number1

# elif number2 < number1 and number2 < number3:

#     smallest = number2

# else:

#     smallest = number3

# for i in range(1,smallest+1):

#     if number1 % i == 0 and number2 % i == 0:

#         print(i)
    

"""
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

# limit = int(input("Enter the limit: "))

# prev=0
# current=1
# print(prev,end=" ")
# print(current,end=" ")
# for i in range(0,limit-2):

#     next = prev + current
#     print(next,end=" ")

#     prev = current
#     current = next

# def is_fibonacci(number):

#     is_fibo = False

#     if number<0:
#         return is_fibo

#     prev=0
#     current=1

#     while current<=number:
#         if current == number:
#             is_fibo = True

#         next = prev + current
#         prev = current
#         current = next

#     return is_fibo

# print(is_fibonacci(4))
        
"""
w.a.p to display first vowel character in a word
"""

# word = "dwien"

# VOWELS = "AEIOUaeiou"

# for w in word:

#     if w in VOWELS:

#         print(w)
#         break

# number = int(input("enter number to print multiplication table: "))

# for i in range(1,number+1):

#     print(f"{i} * {number} = {i*number}")

"""

word1 = "ABCDEF"
word2 = "PQR"

balance = "DEF"
"""
# word1 = "ABCDEF"
# word2 = "PQR"

# result = ""

# min_len = min(len(word1),len(word2))

# result += word1[min_len:] + word2[min_len:]

# print(result)

# word1 = "ABC"
# word2 = "PQRDEF"
# word_length1 = len(word1)
# word_length2 = len(word2)

# if word_length1>word_length2:
#     print(word1[len(word2):])

# elif word_length2>word_length1:
#     print(word2[len(word1):])

# else:
#     print("No balance")

#perfect number
# tot=0
# number =20
# for i in range(1,number):
#     if number%i==0:
#         tot += i
# if tot==number:
#     print("perfect")
# else:
#     print("not perfect")

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

if number1>number2:
    smallest=number2
else:
    smallest=number1

gcd=1

for i in range(1,smallest):

    if number1%i == 0 and number2%i == 0:

        gcd=i

print(gcd)