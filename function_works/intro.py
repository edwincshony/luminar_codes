"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
"""

"""

Function Types

1. function with no parameter and no return value
2. function with parameter and no return value
3. function with parameter and return value

"""

# function with no parameter and no return value

#function definition
def say_hello():

    print("hello")

#function calling
# say_hello()

def say_hai(): #can define parameters inside brackets

    print("hai")

# say_hai() #if parameters available include as arguments

# create a function say_morning that will display Good Morning


def say_morning():

    print("Good Morning")

say_morning()

from builtins import * # to see all functions in builtin hold ctrl and press on builtins
