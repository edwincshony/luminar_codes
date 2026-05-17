# bmi = weight / height ** 2

# weight = int(input("enter weight in kg: "))
# height = int(input("enter height in cm: "))

# bmi = weight / (height/100) ** 2

# w.a.p to calculate 25% of 75

# percentage = 25

# amount = 75

# result = percentage / 100 * amount

# print(result)

# head_count = 5

# bill_amount = 237

# # 8% gst on bill amount

# gst = 8

# bill_amount_split_indv = bill_amount / head_count

# result = gst/100 * bill_amount_split_indv + bill_amount_split_indv

# print(result)

"""
is price in range 150 to 500
"""
# price = 149

# if price >= 150 and price <= 500:

#     print("in range")
# else:
#     print("not")

"""
is_last_two_digit_in_range of 10 and 50
"""

# number = 151
# last_two_digit = number % 100

# print(last_two_digit)


# is_last_two_digit_in_range = last_two_digit >= 10 and last_two_digit <= 50

# print(is_last_two_digit_in_range)

# number = int(input("enter number: "))

# last_digit = number % 10
# even = last_digit % 2 == 0
# gt5 = last_digit > 5
# gt8 = last_digit > 8
# print(gt5)

"""

read a character eg: ch = "a"
display character is vowel if ch is a vowel
display character is not vowel

"""

# character = input("enter character: ")
# VOWELS = "aeiouAEIOU"
# if character in VOWELS:
#     print(character)
# else:
#     print("not bro")

# year = int(input("enter year: "))

# if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:

#     print("leap")

# else:

#     print("no")

# number = 10
# divby8 = number % 2 == 0 and number % 5 == 0

# print(divby8)


# num1 = 50
# num2 = 20
# num3 = 30

# if num1 > num2 and num1 > num3:

#     print(num1,"is larger")

# elif num2 > num1 and num2 > num3:

#     print(num2,"is larger")

# elif num3 > num1 and num3 > num2:

#     print(num3,"is larger")


"""
create a calculator application
read num1,num2 and operation

if operation == "+" => add num1+num2
if operation == "-" => sub num1-num2
if operation == "*" => multiply num1*num2
if operation == "/" => divide num1/num2
if operation == "%" => modulus num1%num2
if operation == "**" => exponentation num1**num2
if operation == "//" => floor division num1//num2
else invalid operation
"""

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))
# op = input("enter operation: ")

# match op:

#     case "+": print(num1+num2)
#     case "-": print(num1-num2)
#     case "*": print(num1*num2)
#     case "/":
          
#           if num2 == 0:
#                print("not possible")
#           else:
               
#             print(num1/num2)
#     case "%": print(num1%num2)
#     case "**": print(num1**num2)
#     case "//": 
#         if num2 == 0:
#                print("not possible")
#         else:
#             print(num1//num2)
#     case _: print("invalid")

# i = 1

# while(i<=10):

#     if i % 2 == 0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")

#     i += 1
"""
w.a.p to display all century years from 1800 to 2026
"""

# i = 1800
# while(i<=2026):

#     if i % 100 == 0:
#         print(i)

#     i += 1

# w.a.p to display all even numbers from 50 to 100

# i= 50
# while(i<=100):

#     if i%2==0:
#         print(i)
#     i += 1

"""
w.a.p to display all leap years from 1800 to 2026
"""

# i = 1800
# while(i<=2026):

#     if (i%100 == 0 and i%400==0) or (i%100 != 0 and i%4==0):
#         print(i,end=" ")
#     i += 1

"""
sum of even number upto limit
"""

# limit = 10
# esum = 0
# i=1
# while(i<=limit):
#     if i%2 == 0:
#         esum = esum + i
#     i += 1
# print(esum)

"""
w.a.p display sum of odd_numbers and sum of even_numbers upto limit 6
"""

# lmit = 6
# i=1
# esum = 0
# osum = 0
# while(i<=lmit):
#     if i%2 == 0:
#         esum = esum + i
#     else:
#         osum += i
#     i += 1
# print(esum)
# print(osum)

# reverse number 123 --> 321
# number = 123
# rev=0
# while(number!=0): 

#     ld = number % 10
#     rev = rev * 10 + ld
#     number = number // 10

# print(rev)

"""
number = 1234

sum of digits = 1 + 2 + 3 + 4 = 10
"""

# number = 1234
# sum=0
# while(number!=0):
#     ld = number % 10
#     sum = sum + ld
#     number //= 10
# print(sum)
  

#program prints all even digits of a number, starting from the rightmost digit (last digit) and moving left.
# number = 1234
# while(number!=0):
#     ld = number%10
#     if ld %2==0:
#         print(ld)
#     number //=10




#palindrome 121 ,

# number = 1112
# rev=0
# p_number = number
# while(number!=0):
#     ld = number%10
#     rev = rev*10+ld
#     print(rev)
#     number//=10
# if p_number == rev:
#     print("palin")
# else:
#     print("not p")



#armstrong number 153 = 

# number = 153
# cnumber = number
# anumber = number

# count=0
# res=0

# while(cnumber!=0):

#     ld = cnumber % 10
#     count += 1
#     cnumber//=10
# print(count)

# while(anumber!=0):
#     ld=anumber%10
#     res += ld ** count
#     anumber //= 10
# print(res)
# if res == number:

#     print("armstrong")
# else:
#     print("not bro")

"""
w.a.p to print from 75 to 100
"""

# for i in range(75,101):
#     print(i)
# print(len(True))

"""
w.a.p to print from 10 to 1
"""
# for i in range(500,399,-1):
#     print(i)
"""
w.a.p to display all odd numbers from 50 to 100

"""
# for i in range(50,101):
#     if i % 2 != 0:
#         print(i)

# number = int(input("enter number to print multiplication table: "))
# for i in range(1,11):
#     print(f"{i} * {number} = {i*number}")

# number = 28
# c_number = number
# sum=0
# for i in range(1,number):
#     if number%i==0:
#         print(i)
#         sum = sum + i

# if sum == c_number:
#     print("perfe")
# else:
#     print("bad")


"""
w.a.p to display first vowel character in a word
"""

# word = "qdwon"

# VOWELS = "aeiouAEIOU"

# for w in word:

#     if w in VOWELS:
#         print(w)
#         break


# common divisor of 2 numbers

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))
# gcd=1

# if num1 > num2:
#     small = num2
# else:
#     small = num1

# for i in range(1,small+1):
#     if num1%i==0 and num2%i==0:
#         gcd = i

# print(gcd)

# number1 = int(input("enter number1: "))
# number2 = int(input("enter number2: "))
# number3 = int(input("enter number3: "))
# gcd=1

# if number1<number2 and number1<number3:

#     smallest = number1

# elif number2<number1 and number2<number3:

#     smallest = number2

# else:

#     smallest = number3

# for i in range(1,smallest+1):

#     if number1 % i == 0 and number2 % i == 0 and number3 % i == 0:

#         gcd=i

# print(gcd)





# prime 2,3,5,7,11,13

# number = 4
# is_prime = False

# for i in range(2,number):

#     if number%i == 0:

#         is_prime=True
#         break

# if is_prime == False:
#     print("prime")
# else:
#     print("not")


    
# for i in range(6,-1,-1):
#     print(i)
# text = "p y t h o n   p r o g  r  a  m  m  i  n  g"
#        #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

# print(text[7:14])
# # print(text[:6])
# # print(text[7:])

# fact = 1

# number = 4

# for i in range(1,number+1):
    
#     fact *= i
# print(fact)

"""
string palindrome
"""

word = "amma"
res=""

word_len = len(word)-1

for i in range(word_len,-1,-1):
    
    res = res + word[i]
print(res)
if res == word:
    
    print("pal")
else:
    print("poda")

if word == word[::-1]:

    print("palindrome")

else:

    print("not palindrome")
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# limit = 10
# prev= 0
# current =1

# print(prev,end=" ")
# print(current,end=" ")

# for i in range(0,limit-2):
    
#     next = prev + current
#     print(next,end=" ")
    
#     prev = current
#     current = next




# def is_fibonacci_number(number):
    
#     is_fibo = False

#     if number<0:
#         return is_fibo
    
#     prev=0
#     current=1
    
#     while(current<=number):
        
#        if current == number:
#             is_fibo=True
#             break

#        next = prev+current
#        prev=current
#        current=next

#     return is_fibo

# print(is_fibonacci_number(4))
        

# def add(n1,n2):

#     result = n1+n2
#     return result

# print(add(10,20))

# add = lambda n1,n2:n1+n2
# print(add(10,20))

# even_odd = lambda num: 'Even' if num%2 == 0 else "odd"
# print(even_odd(2))

# address = """address line 1
# address line 2"""
# number = 732
# is_active = True
# avg = 4.6

# print(type(is_active))

# text = "hello"

# text = "hello"
# new = text.upper()

# print(text)
# print(new)

# word = "luminar technolab"

# print(word.find("tech"))
# print(word.find("python"))

# text = "hello world"

# count = 0

# for t in text:

#     if t == "l":

#         count += 1
# print(count)

# print("hello".isalpha())
# print("hello123".isalpha())
# print("12345".isdigit())

# text = "   python   "
# print(text.strip())

# print("python".count("on"))

# word = "aman##aplan**panamawith2car1bike"

# # w.a.p to display alphabet_count, digit_count, special_character_count

# acount = 0

# for w in word:

#     if w.isalpha():

#         acount += 1

#     if word.isdigit():

#         acount += 1

#     if word.isalpha():

#         acount += 1

# text = "ihave2penpencil3onecar"

# # w.a.p to display digits in the text

# for t in text:

#     if t.isdigit():

#         print(t)

# word1 = "silent"

# word2 = "listen"

# is_anagram = True

# for w in word1:

#     if word2.find(w) == -1:

#         is_anagram = False
#         break

# print(is_anagram)

# def pangram(word_name):

#     alphabets = "abcdefghijklmnopqrstuvwxyz"

#     for a in alphabets:

#         if a not in word_name:

#             return False
        
#     return True
# print(pangram("The quick brown fox jumps over the lazy dog"))

# def pangram(word_name):


#     alphabets = "abcdefghijklmnopqrstuvwxyz"

#     for a in alphabets:

#         if a not in word_name:

#             print("not pangram")

#             break

#     else:

#         print("pangram")

# pangram("The quick brown fox jumps over the lazy dog")

# expense_by_month = [1000,2000,1500,1500,1400,1477,1566,1489,1589,1478,1269,1478]

# sum = 0

# for e in expense_by_month:

#     print(e)

#     sum = sum + e

# print(sum)
# print(sum/len(expense_by_month))

"""
w.a.p to create 2 list even_list, odd_list
"""

# numbers = [10,1,5,89,15,5,9]

# even_list = []
# odd_list = []

# for n in numbers:

#     if n % 2 == 0:

#         even_list.append(n)

#     else:

#         odd_list.append(n)

# print(even_list)
# print(odd_list)

"""
w.a.p create two list squares_list and cube_list
"""

# colors = ["red","blue","black"]
# new_colors = ["cyan","yellow"]

# colors.extend(new_colors)
# print(colors)

# colors = ["red","green","blue","green"]
# removed = colors.pop(2)
# print(removed)
# print(colors)

# colors = ["red","green","blue","green"]
# colors.remove("green")
# print(colors)

# a = ["red","white","blue","black"]
# b = a.copy()

# print(a == b)
# print(a is b)

# colors = ["red","green","blue","green"]
# freq = colors.count("ui")
# print(freq)

# a = ["red", "white"]
# b = a.copy()
# b[0] = "yellow"
# print(b)

# nums = [10, 5, 1]
# nums.sort()
# nums.sort(reverse=False)
# print(nums)

# laptop = {"brand":"moto", "ram": 8, "rom": 128,"sim": "bsnl"}

# print(laptop)

# laptop["brand"] = "lenovo"

# print(laptop)


# employee = {"id":101,"name":"edwin","salary":45000,"dept":"qa"}

# print(employee.get("id3","sorry bro"))

"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists

"""

# student_details = {"id":101,"name":"edwin","course":"data science","marks":40}

# print(student_details["name"])

# student_details["marks"] += 5

# print(student_details)

# student_details["grade"]  = "a"

# print(student_details)

# print(student_details.get("attendance","elada"))

# print(student_details)

# manali = {

#     "dijo": 300,
#     "akshay": 1000,
#     "edwin": 800,
#     "alan": 15000,
#     "manoj": 0,
#     "supin": 0,
#     "sreeyesh": 500

#     }

# total_expense = 0

# for val in manali.values():

#     total_expense = total_expense + val

# print(total_expense)

# print(total_expense/len(manali))

# remain_amt_to_give = {}

# for key,val in manali.items():

#     payment = total_expense/len(manali) - val

#     remain_amt_to_give[key] = payment

# print(remain_amt_to_give)

# sales_report = {

#     "sunday" : 18000,
#     "monday" : 18000,
#     "tue": 1500,
#     "wed": 2900,
#     "thurs": 15000,
#     "fri": 19000,
#     "sat": 2148
# }

# #display day wise sales
# # total_sale
# # display avg_sales
# # display day where sales < avg_sales

# # day with highest sale
# # day with lowest sale

# print(sales_report)
# sal=0
# for val in sales_report.values():
#     sal = sal + val
# print(sal)
# print(sal/len(sales_report))

# for key,val in sales_report.items():

#     if val < sal/len(sales_report):

#         print(key)


# largest = float('-inf')
# highest_day  = None

# for key in sales_report:

#     if sales_report[key] > largest:

#         largest = sales_report[key]

#         highest_day = key

# print(largest)

# arr = [10,12,13,14,15]
 
# sqaures = [i for i in range(1,11)]
# print(sqaures)

#create a new list that contain word length > 3

# words = ["apple","bat","carrot","elephant","ball","red"]

# word_lengt3 = [word for word in words if len(word)>3]

# print(word_lengt3)

# display character count

# word = "racecar"

# count_char = {w:word.count(w) for w in word }

# print(count_char)

# word = "racecarfast"

# # print non recursive character
# # print recursive character whose count > 2

# non_rec = [w for w in word if word.count(w)==1]
# print(non_rec)
# rec = {w:word.count(w) for w in word if word.count(w)>2}
# print(rec)

# word count

# text = "python programming programming is simple"

# words = text.split()

# print(words)

# word_count = {w:words.count(w) for w in words}
# print(word_count)

# ----------------------------
# MOST CALORIE FOOD VLOGGER
# ----------------------------
# food_logs = [
#     [1, "adithya", "dosa", "meals", "chapathy", 1800],
#     [2, "sreya", "dosa", "biriyani", "mandi", 2000],
#     [3, "amritha", "dosa", "mandhi", "porotta", 2000],
#     [4, "dijo", "dosa", "mandhi", "meals", 300],
# ] #see most like food and most liked lunch extraction in files

# # People who ate dosa
# ate_dosa =  [row[1] for row in food_logs if row[2] == "dosa"]
# print(ate_dosa)

# calories = max([row[5] for row in food_logs])
# max_calories_person = [row[1] for row in food_logs if row[5] == calories]
# print(max_calories_person)

# calories =[row for row in food_logs]
# print(calories)

# social_media_posts = [
#     [1, "good morning", 500, 600, "arun"],
#     [2, "elon vs trump", 7000, 9000, "vipin"],
#     [3, "epstien files", 14000, 1500, "dijo"],
#     [4, "nigal njettum", 15000, 80000, "edwin"],
# ]


# insta_owners  = [for ]

# most_liked_meal find from all food

# food_logs = [
#     [1, "adithya", "dosa", "meals", "chapathy", 1800],
#     [2, "sreya", "dosa", "biriyani", "mandhi", 2000],
#     [3, "amritha", "dosa", "mandhi", "porotta", 2000],
#     [4, "dijo", "dosa", "mandhi", "meals", 300],
# ]

# all_foods = []

# for row in food_logs:

#     all_foods.extend(row[2:5])

# food_count = {f:all_foods.count(f) for f in all_foods}

# most_liked = [[v,k] for k,v in food_count.items()]
# print(sorted(most_liked,reverse=True)[0][1])

# movies = [
#     [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
#     [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
#     [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
#     [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
#     [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
#     [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
# ]

# movies_titles = [row[1] for row in movies]
# print(movies_titles)

# # movie with top rating

# ratings = max([row[4] for row in movies])
# top_movies = [row[1] for row in movies if row[4] == ratings]
# print(top_movies)

# # which language most number of movies
# language_list = [mov[3] for mov in movies]

# print(language_list)

# language_count = {mov:language_list.count(mov) for mov in language_list}
# print(language_count)

# # movies_fav = max(language_count,key=language_count.get)
# # print(movies_fav)

# movies_fav = [[v,k] for k,v in language_count.items()]
# print(sorted(movies_fav,reverse=True))

# # movie with max budget

# budget = max([row[5] for row in movies])
# budget_movie = [row[1] for row in movies if row[5] == budget]
# print(budget_movie)

# titanic_data = [
#     {"id": 1, "survived": 0, "pclass": 3, "class": "Third", "name": "Braund, Mr. Owen Harris", "sex": "male", "age": 22, "fare": 7.25},
#     {"id": 2, "survived": 1, "pclass": 1, "class": "First", "name": "Cumings, Mrs. John Bradley (Florence)", "sex": "female", "age": 38, "fare": 71.28},
#     {"id": 3, "survived": 1, "pclass": 3, "class": "Third", "name": "Heikkinen, Miss. Laina", "sex": "female", "age": 26, "fare": 7.92},
#     {"id": 4, "survived": 1, "pclass": 1, "class": "First", "name": "Futrelle, Mrs. Jacques Heath (Lily)", "sex": "female", "age": 35, "fare": 53.10},
#     {"id": 5, "survived": 0, "pclass": 3, "class": "Third", "name": "Allen, Mr. William Henry", "sex": "male", "age": 35, "fare": 8.05},
#     {"id": 6, "survived": 0, "pclass": 3, "class": "Third", "name": "Moran, Mr. James", "sex": "male", "age": None, "fare": 8.45},
#     {"id": 7, "survived": 0, "pclass": 1, "class": "First", "name": "McCarthy, Mr. Timothy J", "sex": "male", "age": 54, "fare": 51.86},
#     {"id": 8, "survived": 0, "pclass": 3, "class": "Third", "name": "Palsson, Master. Gosta Leonard", "sex": "male", "age": 2, "fare": 21.07},
#     {"id": 9, "survived": 1, "pclass": 3, "class": "Third", "name": "Johnson, Mrs. Oscar W (Elisabeth)", "sex": "female", "age": 27, "fare": 11.13},
#     {"id": 10, "survived": 1, "pclass": 2, "class": "Second", "name": "Nasser, Mrs. Nicholas (Adele)", "sex": "female", "age": 14, "fare": 30.07},
#     {"id": 11, "survived": 1, "pclass": 3, "class": "Third", "name": "Sandstrom, Miss. Marguerite Rut", "sex": "female", "age": 4, "fare": 16.70},
#     {"id": 12, "survived": 1, "pclass": 1, "class": "First", "name": "Bonnell, Miss. Elizabeth", "sex": "female", "age": 58, "fare": 26.55},
#     {"id": 13, "survived": 0, "pclass": 3, "class": "Third", "name": "Saundercock, Mr. William Henry", "sex": "male", "age": 20, "fare": 8.05},
#     {"id": 14, "survived": 0, "pclass": 3, "class": "Third", "name": "Andersson, Mr. Anders Johan", "sex": "male", "age": 39, "fare": 31.27},
#     {"id": 15, "survived": 0, "pclass": 3, "class": "Third", "name": "Vestrom, Miss. Hulda Amanda Adolfina", "sex": "female", "age": 14, "fare": 7.85},
#     {"id": 16, "survived": 1, "pclass": 2, "class": "Second", "name": "Hewlett, Mrs. (Mary D Kingcome)", "sex": "female", "age": 55, "fare": 16.00},
#     {"id": 17, "survived": 0, "pclass": 2, "class": "Second", "name": "Williams, Mr. Charles Eugene", "sex": "male", "age": None, "fare": 13.00}
# ]

# # q1 : number of survived passengers


# sur = [di for di in titanic_data if di.get("survived") == 1]
# print(len(sur))
# # q2 : display unique passenger class 
# unique_pass_class = {di.get("pclass") for di in titanic_data}
# print(unique_pass_class)
# # q3 number of female passengers
# females = [di for di in titanic_data if di.get("sex") == "female"]
# print(len(females))
# # q10:female survival rate
# # q3 number of female passengers
# females_survived = [di for di in titanic_data if di.get("sex") == "female" and di.get("survived") == 1]
# print(len(females_survived))

# rate = (len(females_survived)/len(females))*100
# print(round(rate,2))

# countries_data = [
#     {"country_name": "Afghanistan", "capital": "Kabul", "population": 43844000, "is_independent": True, "region": "Asia", "currency": "AFN"},
#     {"country_name": "Albania", "capital": "Tirana", "population": 2830000, "is_independent": True, "region": "Europe", "currency": "ALL"},
#     {"country_name": "Algeria", "capital": "Algiers", "population": 46800000, "is_independent": True, "region": "Africa", "currency": "DZD"},
#     {"country_name": "Argentina", "capital": "Buenos Aires", "population": 46300000, "is_independent": True, "region": "South America", "currency": "ARS"},
#     {"country_name": "Australia", "capital": "Canberra", "population": 26800000, "is_independent": True, "region": "Oceania", "currency": "AUD"},
#     {"country_name": "Austria", "capital": "Vienna", "population": 9000000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Bangladesh", "capital": "Dhaka", "population": 177100000, "is_independent": True, "region": "Asia", "currency": "BDT"},
#     {"country_name": "Belgium", "capital": "Brussels", "population": 11700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Brazil", "capital": "Brasília", "population": 213300000, "is_independent": True, "region": "South America", "currency": "BRL"},
#     {"country_name": "Canada", "capital": "Ottawa", "population": 41500000, "is_independent": True, "region": "North America", "currency": "CAD"},
#     {"country_name": "Chile", "capital": "Santiago", "population": 19700000, "is_independent": True, "region": "South America", "currency": "CLP"},
#     {"country_name": "China", "capital": "Beijing", "population": 1413000000, "is_independent": True, "region": "Asia", "currency": "CNY"},
#     {"country_name": "Colombia", "capital": "Bogotá", "population": 52300000, "is_independent": True, "region": "South America", "currency": "COP"},
#     {"country_name": "Denmark", "capital": "Copenhagen", "population": 5900000, "is_independent": True, "region": "Europe", "currency": "DKK"},
#     {"country_name": "Egypt", "capital": "Cairo", "population": 119600000, "is_independent": True, "region": "Africa", "currency": "EGP"},
#     {"country_name": "Ethiopia", "capital": "Addis Ababa", "population": 137800000, "is_independent": True, "region": "Africa", "currency": "ETB"},
#     {"country_name": "Finland", "capital": "Helsinki", "population": 5600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "France", "capital": "Paris", "population": 66600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Germany", "capital": "Berlin", "population": 83700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Greece", "capital": "Athens", "population": 10300000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "India", "capital": "New Delhi", "population": 1472400000, "is_independent": True, "region": "Asia", "currency": "INR"},
#     {"country_name": "Indonesia", "capital": "Jakarta", "population": 287200000, "is_independent": True, "region": "Asia", "currency": "IDR"},
#     {"country_name": "Iran", "capital": "Tehran", "population": 90100000, "is_independent": True, "region": "Asia", "currency": "IRR"},
#     {"country_name": "Iraq", "capital": "Baghdad", "population": 46100000, "is_independent": True, "region": "Asia", "currency": "IQD"},
#     {"country_name": "Ireland", "capital": "Dublin", "population": 5100000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Israel", "capital": "Jerusalem", "population": 9400000, "is_independent": True, "region": "Asia", "currency": "ILS"},
#     {"country_name": "Italy", "capital": "Rome", "population": 58700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Japan", "capital": "Tokyo", "population": 122700000, "is_independent": True, "region": "Asia", "currency": "JPY"},
#     {"country_name": "Kenya", "capital": "Nairobi", "population": 57200000, "is_independent": True, "region": "Africa", "currency": "KES"},
#     {"country_name": "Malaysia", "capital": "Kuala Lumpur", "population": 34800000, "is_independent": True, "region": "Asia", "currency": "MYR"},
#     {"country_name": "Mexico", "capital": "Mexico City", "population": 132700000, "is_independent": True, "region": "North America", "currency": "MXN"},
#     {"country_name": "Morocco", "capital": "Rabat", "population": 38200000, "is_independent": True, "region": "Africa", "currency": "MAD"},
#     {"country_name": "Netherlands", "capital": "Amsterdam", "population": 17700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "New Zealand", "capital": "Wellington", "population": 5300000, "is_independent": True, "region": "Oceania", "currency": "NZD"},
#     {"country_name": "Nigeria", "capital": "Abuja", "population": 240800000, "is_independent": True, "region": "Africa", "currency": "NGN"},
#     {"country_name": "Norway", "capital": "Oslo", "population": 5500000, "is_independent": True, "region": "Europe", "currency": "NOK"},
#     {"country_name": "Pakistan", "capital": "Islamabad", "population": 257800000, "is_independent": True, "region": "Asia", "currency": "PKR"},
#     {"country_name": "Peru", "capital": "Lima", "population": 34800000, "is_independent": True, "region": "South America", "currency": "PEN"},
#     {"country_name": "Philippines", "capital": "Manila", "population": 117400000, "is_independent": True, "region": "Asia", "currency": "PHP"},
#     {"country_name": "Poland", "capital": "Warsaw", "population": 40500000, "is_independent": True, "region": "Europe", "currency": "PLN"},
#     {"country_name": "Portugal", "capital": "Lisbon", "population": 10200000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Russia", "capital": "Moscow", "population": 143500000, "is_independent": True, "region": "Europe/Asia", "currency": "RUB"},
#     {"country_name": "Saudi Arabia", "capital": "Riyadh", "population": 37500000, "is_independent": True, "region": "Asia", "currency": "SAR"},
#     {"country_name": "South Africa", "capital": "Pretoria", "population": 61200000, "is_independent": True, "region": "Africa", "currency": "ZAR"},
#     {"country_name": "South Korea", "capital": "Seoul", "population": 51700000, "is_independent": True, "region": "Asia", "currency": "KRW"},
#     {"country_name": "Spain", "capital": "Madrid", "population": 47500000, "is_independent": True, "region": "Europe", "currency": "EUR"},
#     {"country_name": "Sweden", "capital": "Stockholm", "population": 10600000, "is_independent": True, "region": "Europe", "currency": "SEK"},
#     {"country_name": "Switzerland", "capital": "Bern", "population": 8900000, "is_independent": True, "region": "Europe", "currency": "CHF"},
#     {"country_name": "Thailand", "capital": "Bangkok", "population": 71800000, "is_independent": True, "region": "Asia", "currency": "THB"},
#     {"country_name": "Turkey", "capital": "Ankara", "population": 87800000, "is_independent": True, "region": "Europe/Asia", "currency": "TRY"},
#     {"country_name": "United Kingdom", "capital": "London", "population": 68100000, "is_independent": True, "region": "Europe", "currency": "GBP"},
#     {"country_name": "United States", "capital": "Washington, D.C.", "population": 348500000, "is_independent": True, "region": "North America", "currency": "USD"},
#     {"country_name": "Vietnam", "capital": "Hanoi", "population": 100300000, "is_independent": True, "region": "Asia", "currency": "VND"}
# ]

# high_population = [di.get("population") for di in countries_data]

# max_pop = max(high_population)

# country_with_high_pop = [di.get("country_name") for di in countries_data if  di.get("population") == max_pop]

# print(country_with_high_pop)

# high_population1 = max(countries_data,key=lambda x:x.get("population"))
# print(high_population1.get("country_name"))

# # Sort all countries by population and produce a structure that maps country → population in sorted order.

# country_sorted = sorted(countries_data,key=lambda x:x.get("population"),reverse=True)
# country_pop = {di.get("country_name"):di.get("population") for di in country_sorted}
# print(country_pop)

# leads = [
#     {"source": "LinkedIn", "status": "New", "title": "Data Analyst", "course": "Advanced SQL & Python", "created_date": "15-02-26"},
#     {"source": "Organic Search", "status": "Contacted", "title": "Software Engineer", "course": "Full-Stack Development", "created_date": "16-02-26"},
#     {"source": "Referral", "status": "Qualified", "title": "Project Manager", "course": "Agile Methodologies", "created_date": "16-02-26"},
#     {"source": "Facebook Ads", "status": "New", "title": "Marketing Specialist", "course": "Digital Growth Hacking", "created_date": "17-02-26"},
#     {"source": "Webinar", "status": "Nurturing", "title": "Student", "course": "Introduction to Machine Learning", "created_date": "17-02-26"},
#     {"source": "LinkedIn", "status": "Unqualified", "title": "HR Manager", "course": "Data Visualization", "created_date": "18-02-26"},
#     {"source": "Direct Traffic", "status": "Converted", "title": "Freelance Designer", "course": "UI/UX Design Masterclass", "created_date": "18-02-26"},
#     {"source": "Google Ads", "status": "New", "title": "Business Analyst", "course": "Tableau for Beginners", "created_date": "19-02-26"},
#     {"source": "Organic Search", "status": "Nurturing", "title": "Systems Admin", "course": "Cloud Architecture (AWS)", "created_date": "19-02-26"},
#     {"source": "Referral", "status": "Contacted", "title": "Product Owner", "course": "Scrum Certification", "created_date": "20-02-26"},
#     {"source": "LinkedIn", "status": "Qualified", "title": "Junior Developer", "course": "React & Next.js", "created_date": "20-02-26"},
#     {"source": "Twitter", "status": "New", "title": "Content Creator", "course": "Video Editing Pro", "created_date": "21-02-26"},
#     {"source": "Webinar", "status": "New", "title": "Operations Lead", "course": "Lean Six Sigma", "created_date": "21-02-26"},
#     {"source": "Facebook Ads", "status": "Unqualified", "title": "Retail Associate", "course": "Cybersecurity Fundamentals", "created_date": "22-02-26"},
#     {"source": "Direct Traffic", "status": "Converted", "title": "Backend Dev", "course": "Go Programming", "created_date": "22-02-26"},
#     {"source": "LinkedIn", "status": "Nurturing", "title": "Data Scientist", "course": "Deep Learning Specialization", "created_date": "23-02-26"},
#     {"source": "Google Ads", "status": "Contacted", "title": "Sales Manager", "course": "CRM Automation", "created_date": "23-02-26"},
#     {"source": "Organic Search", "status": "New", "title": "IT Consultant", "course": "Ethical Hacking", "created_date": "24-02-26"},
#     {"source": "Referral", "status": "Converted", "title": "CTO", "course": "Executive Leadership", "created_date": "24-02-26"},
#     {"source": "Webinar", "status": "Qualified", "title": "QA Engineer", "course": "Automated Testing", "created_date": "25-02-26"},
#     {"source": "LinkedIn", "status": "New", "title": "UX Researcher", "course": "Design Thinking", "created_date": "25-02-26"},
#     {"source": "Organic Search", "status": "Nurturing", "title": "Financial Analyst", "course": "Excel Macros & VBA", "created_date": "25-02-26"},
#     {"source": "Facebook Ads", "status": "New", "title": "Small Business Owner", "course": "Social Media Marketing", "created_date": "26-02-26"},
#     {"source": "Twitter", "status": "Unqualified", "title": "Accountant", "course": "Python for Finance", "created_date": "26-02-26"},
#     {"source": "Google Ads", "status": "Contacted", "title": "Network Engineer", "course": "Cisco CCNA Prep", "created_date": "26-02-26"},
#     {"source": "LinkedIn", "status": "New", "title": "Full Stack Dev", "course": "Node.js Microservices", "created_date": "27-02-26"},
#     {"source": "Direct Traffic", "status": "Qualified", "title": "Graphic Designer", "course": "Motion Graphics", "created_date": "27-02-26"},
#     {"source": "Referral", "status": "New", "title": "Graduate Student", "course": "Data Science Boot Camp", "created_date": "27-02-26"},
#     {"source": "Webinar", "status": "Nurturing", "title": "SEO Specialist", "course": "Advanced SEO 2024", "created_date": "01-02-26"},
#     {"source": "LinkedIn", "status": "Converted", "title": "Technical Writer", "course": "API Documentation", "created_date": "02-02-26"},
#     {"source": "Organic Search", "status": "Contacted", "title": "Security Analyst", "course": "CompTIA Security+", "created_date": "03-02-26"},
#     {"source": "Facebook Ads", "status": "New", "title": "E-commerce Manager", "course": "Shopify Mastery", "created_date": "04-02-26"},
#     {"source": "Google Ads", "status": "Qualified", "title": "Database Admin", "course": "NoSQL Databases", "created_date": "05-02-26"},
#     {"source": "Twitter", "status": "New", "title": "Copywriter", "course": "AI for Writing", "created_date": "06-02-26"},
#     {"source": "LinkedIn", "status": "Nurturing", "title": "App Developer", "course": "SwiftUI & iOS", "created_date": "07-02-26"},
#     {"source": "Webinar", "status": "Unqualified", "title": "Teacher", "course": "EdTech Integration", "created_date": "08-02-26"},
#     {"source": "Referral", "status": "Contacted", "title": "VP of Engineering", "course": "Scaling Tech Teams", "created_date": "09-02-26"},
#     {"source": "Direct Traffic", "status": "New", "title": "Web Designer", "course": "Webflow Mastery", "created_date": "10-02-26"},
#     {"source": "Organic Search", "status": "Qualified", "title": "Risk Analyst", "course": "Quantitative Finance", "created_date": "11-02-26"},
#     {"source": "Facebook Ads", "status": "New", "title": "Artist", "course": "NFT & Crypto Art", "created_date": "12-02-26"},
#     {"source": "LinkedIn", "status": "Converted", "title": "Cloud Architect", "course": "Google Cloud Professional", "created_date": "13-02-26"},
#     {"source": "Google Ads", "status": "Nurturing", "title": "Marketing Director", "course": "Omnichannel Strategy", "created_date": "14-02-26"},
#     {"source": "Webinar", "status": "New", "title": "Logistics Coordinator", "course": "Supply Chain Mgmt", "created_date": "15-02-26"},
#     {"source": "Twitter", "status": "Contacted", "title": "Blogger", "course": "Affiliate Marketing", "created_date": "16-02-26"},
#     {"source": "Referral", "status": "New", "title": "HR Specialist", "course": "Conflict Resolution", "created_date": "17-02-26"},
#     {"source": "Direct Traffic", "status": "Qualified", "title": "Frontend Dev", "course": "Vue.js Framework", "created_date": "18-02-26"},
#     {"source": "LinkedIn", "status": "Nurturing", "title": "DevOps Engineer", "course": "Kubernetes in Practice", "created_date": "19-02-26"},
#     {"source": "Organic Search", "status": "Converted", "title": "Product Manager", "course": "Product Analytics", "created_date": "20-02-26"},
#     {"source": "Facebook Ads", "status": "Unqualified", "title": "Chef", "course": "Culinary Management", "created_date": "21-02-26"},
#     {"source": "Google Ads", "status": "New", "title": "Legal Assistant", "course": "Legal Tech & AI", "created_date": "22-02-26"}
# ]

# google_ads_conv = [di for di in leads if di.get("status") == "Converted" and di.get("source") == "Google Ads"]
# google_ads_all = [di for di in leads if di.get("source") == "Google Ads"]
# rate = len(google_ads_conv)/len(google_ads_all)
# print(rate)

"""
1

Find the country with the highest population using a functional approach (e.g., max() with a key function).

2

Sort all countries by population and produce a structure that maps country → population in sorted order.

3

Calculate the conversion rate of Google Ads leads
(Converted Google Ads leads ÷ Total Google Ads leads × 100).

4

Compute the distribution of lead statuses (count of each status) and then calculate the Qualified lead rate based on the total leads.

5

Determine the song with the highest downloads and also provide an alternative approach using dictionary swap + sorting.
"""
countries_data = [
    {"country_name": "Afghanistan", "capital": "Kabul", "population": 43844000, "is_independent": True, "region": "Asia", "currency": "AFN"},
    {"country_name": "Albania", "capital": "Tirana", "population": 2830000, "is_independent": True, "region": "Europe", "currency": "ALL"},
    {"country_name": "Algeria", "capital": "Algiers", "population": 46800000, "is_independent": True, "region": "Africa", "currency": "DZD"},
    {"country_name": "Argentina", "capital": "Buenos Aires", "population": 46300000, "is_independent": True, "region": "South America", "currency": "ARS"},
    {"country_name": "Australia", "capital": "Canberra", "population": 26800000, "is_independent": True, "region": "Oceania", "currency": "AUD"},
    {"country_name": "Austria", "capital": "Vienna", "population": 9000000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Bangladesh", "capital": "Dhaka", "population": 177100000, "is_independent": True, "region": "Asia", "currency": "BDT"},
    {"country_name": "Belgium", "capital": "Brussels", "population": 11700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Brazil", "capital": "Brasília", "population": 213300000, "is_independent": True, "region": "South America", "currency": "BRL"},
    {"country_name": "Canada", "capital": "Ottawa", "population": 41500000, "is_independent": True, "region": "North America", "currency": "CAD"},
    {"country_name": "Chile", "capital": "Santiago", "population": 19700000, "is_independent": True, "region": "South America", "currency": "CLP"},
    {"country_name": "China", "capital": "Beijing", "population": 1413000000, "is_independent": True, "region": "Asia", "currency": "CNY"},
    {"country_name": "Colombia", "capital": "Bogotá", "population": 52300000, "is_independent": True, "region": "South America", "currency": "COP"},
    {"country_name": "Denmark", "capital": "Copenhagen", "population": 5900000, "is_independent": True, "region": "Europe", "currency": "DKK"},
    {"country_name": "Egypt", "capital": "Cairo", "population": 119600000, "is_independent": True, "region": "Africa", "currency": "EGP"},
    {"country_name": "Ethiopia", "capital": "Addis Ababa", "population": 137800000, "is_independent": True, "region": "Africa", "currency": "ETB"},
    {"country_name": "Finland", "capital": "Helsinki", "population": 5600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "France", "capital": "Paris", "population": 66600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Germany", "capital": "Berlin", "population": 83700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Greece", "capital": "Athens", "population": 10300000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "India", "capital": "New Delhi", "population": 1472400000, "is_independent": True, "region": "Asia", "currency": "INR"},
    {"country_name": "Indonesia", "capital": "Jakarta", "population": 287200000, "is_independent": True, "region": "Asia", "currency": "IDR"},
    {"country_name": "Iran", "capital": "Tehran", "population": 90100000, "is_independent": True, "region": "Asia", "currency": "IRR"},
    {"country_name": "Iraq", "capital": "Baghdad", "population": 46100000, "is_independent": True, "region": "Asia", "currency": "IQD"},
    {"country_name": "Ireland", "capital": "Dublin", "population": 5100000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Israel", "capital": "Jerusalem", "population": 9400000, "is_independent": True, "region": "Asia", "currency": "ILS"},
    {"country_name": "Italy", "capital": "Rome", "population": 58700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Japan", "capital": "Tokyo", "population": 122700000, "is_independent": True, "region": "Asia", "currency": "JPY"},
    {"country_name": "Kenya", "capital": "Nairobi", "population": 57200000, "is_independent": True, "region": "Africa", "currency": "KES"},
    {"country_name": "Malaysia", "capital": "Kuala Lumpur", "population": 34800000, "is_independent": True, "region": "Asia", "currency": "MYR"},
    {"country_name": "Mexico", "capital": "Mexico City", "population": 132700000, "is_independent": True, "region": "North America", "currency": "MXN"},
    {"country_name": "Morocco", "capital": "Rabat", "population": 38200000, "is_independent": True, "region": "Africa", "currency": "MAD"},
    {"country_name": "Netherlands", "capital": "Amsterdam", "population": 17700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "New Zealand", "capital": "Wellington", "population": 5300000, "is_independent": True, "region": "Oceania", "currency": "NZD"},
    {"country_name": "Nigeria", "capital": "Abuja", "population": 240800000, "is_independent": True, "region": "Africa", "currency": "NGN"},
    {"country_name": "Norway", "capital": "Oslo", "population": 5500000, "is_independent": True, "region": "Europe", "currency": "NOK"},
    {"country_name": "Pakistan", "capital": "Islamabad", "population": 257800000, "is_independent": True, "region": "Asia", "currency": "PKR"},
    {"country_name": "Peru", "capital": "Lima", "population": 34800000, "is_independent": True, "region": "South America", "currency": "PEN"},
    {"country_name": "Philippines", "capital": "Manila", "population": 117400000, "is_independent": True, "region": "Asia", "currency": "PHP"},
    {"country_name": "Poland", "capital": "Warsaw", "population": 40500000, "is_independent": True, "region": "Europe", "currency": "PLN"},
    {"country_name": "Portugal", "capital": "Lisbon", "population": 10200000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Russia", "capital": "Moscow", "population": 143500000, "is_independent": True, "region": "Europe/Asia", "currency": "RUB"},
    {"country_name": "Saudi Arabia", "capital": "Riyadh", "population": 37500000, "is_independent": True, "region": "Asia", "currency": "SAR"},
    {"country_name": "South Africa", "capital": "Pretoria", "population": 61200000, "is_independent": True, "region": "Africa", "currency": "ZAR"},
    {"country_name": "South Korea", "capital": "Seoul", "population": 51700000, "is_independent": True, "region": "Asia", "currency": "KRW"},
    {"country_name": "Spain", "capital": "Madrid", "population": 47500000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Sweden", "capital": "Stockholm", "population": 10600000, "is_independent": True, "region": "Europe", "currency": "SEK"},
    {"country_name": "Switzerland", "capital": "Bern", "population": 8900000, "is_independent": True, "region": "Europe", "currency": "CHF"},
    {"country_name": "Thailand", "capital": "Bangkok", "population": 71800000, "is_independent": True, "region": "Asia", "currency": "THB"},
    {"country_name": "Turkey", "capital": "Ankara", "population": 87800000, "is_independent": True, "region": "Europe/Asia", "currency": "TRY"},
    {"country_name": "United Kingdom", "capital": "London", "population": 68100000, "is_independent": True, "region": "Europe", "currency": "GBP"},
    {"country_name": "United States", "capital": "Washington, D.C.", "population": 348500000, "is_independent": True, "region": "North America", "currency": "USD"},
    {"country_name": "Vietnam", "capital": "Hanoi", "population": 100300000, "is_independent": True, "region": "Asia", "currency": "VND"}
]
# country with highest population

pop = max(countries_data,key=lambda x:x.get("population"))
print(pop.get("country_name"))

# sort countries wrt  population

population = sorted(countries_data,key=lambda x:x.get("population"),reverse=True)
pop_max = {p.get("country_name"):p.get("population") for p in population}
print(pop_max)