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

# number1 = int(input("enter number1: "))
# number2 = int(input("enter number2: "))

# if number1>number2:
#     smallest=number2
# else:
#     smallest=number1

# gcd=1

# for i in range(1,smallest):

#     if number1%i == 0 and number2%i == 0:

#         gcd=i

# print(gcd)

# number = int(input('enter number: '))
# is_prime = True
# if number<=1:
#     print("Not prime")
# else:
#     for i in range(2,number):
#         if number%i==0:
#             is_prime = False
#             break
#     if is_prime==True:
#         print("prime")
#     else:
#         print("nprime")

# word = input("enter word: ")

# result = ""

# for  i in range(len(word)-1,-1,-1):

#     result += word[i]

# if result == word:
#     print("palindrome")
# else:
#     print("npalindrome")

# find closest number to zero
# def closest_to_zero(nums):

#     closest = nums[0]

#     for num in nums:
#         if abs(num) < abs(closest):
#             closest=num
         
#         elif abs(num) == abs(closest) and num>closest:
#             closest=num

#     return closest

# print(closest_to_zero([-4, -2, -1,1, 4, 8]))

# word1 = "ieeau"
# word2 = "rnbb"

# result = ""

# max_len = max(len(word1), len(word2))

# for i in range(max_len):

#     # result += word1[i] + word2[i]

#     # If character exists in word1, take it.
#     if i < len(word1):
#         result += word1[i]

#     # If character exists in word2, take it.
#     if i < len(word2):
#         result += word2[i]

# print(result)

# def merge_alternately(word1, word2):

#     result = []

#     for i in range(max(len(word1),len(word2))): 
#         if i < len(word1):
#             result+=word1[i]
#         if i<len(word2):
#             result+=word2[i]

#     return "".join(result)

# print(merge_alternately('ieeau', 'rnbb'))

# def roman_to_int(s):

#     values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

#     total = 0

#     for i in range(len(s)):
#         value = values[s[i]]

#         if i+1 < len(s) and value < values[s[i+1]]:

#             total -= value

#         else:

#             total += value
#     return total
# print(roman_to_int('MCMXCIV'))

# def is_subsequence(s, t):

#     i=0
#     for ch in t:
#         if i<len(s) and s[i] == ch:
#             i+=1
#     return i==len(s)

# print(is_subsequence('ayc', 'ahbgdc'))

# strs = ["flower","flow","flight"]
# strs.sort()

# first,last = strs[0],strs[-1]
# i=0
# result=""

# while i<len(first):
#     if first[i] == last[i]:
#         result += first[i]
#         i += 1
#     else:
#         break

# print(result)

# def contains_duplicate(nums):

#     return len(set(nums)) < len(nums)

# print(contains_duplicate([1,3,2]))

# note = "aabb"
# magazine = "ab"

# magazine_freq = {}

# for l in magazine:
#     if l in magazine_freq:

#         magazine_freq[l] += 1
#     else:
#         magazine_freq[l] =1
# for l in note:
#     if l in magazine_freq and magazine_freq[l]>0:
#         magazine_freq[l]-=1
#     else:
#         print("not ransome")
#         break
# else:
#     print("ransome")

# arr = [2,3,4,5]

# target = 10

# arr.sort()
# found=False

# left=0
# right = len(arr)-1

# while(left<right):

#     current_sum = arr[left] + arr[right]

#     if current_sum == target:

#         print(arr[left],arr[right])

#         found=True
#         break
#     elif current_sum < target:
#         left += 1

#     else:
#         right-=1
# if found==False:
#     print("pair not found")

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# ana_grps = {}

# for word in words:

#     key = "".join(sorted(word))

#     if key in ana_grps:
#         ana_grps[key].append(word)
#     else:
#         ana_grps[key] = [word]

# result = list(ana_grps.values())
# print(result)

# arr = [2,3,4,5]

# target = 8

# arr.sort()

# found = False

# org = arr.copy()

# left = 0

# right = len(arr) - 1

# while(left<right):

#     current_sum = arr[left] + arr[right]

#     if current_sum == target:

#         print(org.index(arr[left]),org.index(arr[right]))

#         found = True

#         break

#     elif current_sum < target:

#         left += 1

#     else:

#         right -= 1

# if found == False:

#     print("no pair")

# lst = [1,2,4, 5]
# s = set(lst)

# i = 1
# while True:
#     if i not in s:
#         print(i)
#         break
#     i += 1

lst = [1,3, 4, 5]

s = set(lst)

i=1
while True:
    if i not in s:
        print(i)
        break
    i+=1