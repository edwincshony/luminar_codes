"""
2. function with parameter and no return value

def function_name(p1,p2,p3): # function definition 

    function body

function_name(arg1,arg2,arg3) #function calling

"""

def addition(num1,num2):

    result = num1 + num2

    print(result)


# addition(100,200)
# addition(500,700)

# w.a function sub with 2 parameter num1,num2 display sub result

def subtraction(num1,num2):

    result = num1 - num2

    print(result)


# subtraction(200,100)

def cube(num):

    result = num**3

    print(result)

# cube(2)

# create a funtion max_two two parameter num1,num2

#display largest number

def max_two(num1,num2):

    if num1 > num2:

        print(f"{num1} is largest")

    else:

        print(f"{num2} is largest")

# max_two(10,20)


#create a function last_digit_max with two parameter num1,num2
#display num1 if last_digit of num1 > last_digit of num2
#display num2 if last_digit of num2 > last_digit of num1

def last_digit_max(num1,num2):

    ld_num1 = num1 % 10
    ld_num2 = num2 % 10

    if ld_num1 > ld_num2:

        print(f"Last digit of {num1} is greater")

    else:

        print(f"Last digit of {num2} is greater")

last_digit_max(127,98)