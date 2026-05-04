# -----------------------------
# Basic data types
# -----------------------------

address = """address line 1
address line 2"""
number = 732
is_active = True
avg = 4.6

#string is immutable (can not be changed)

# Checking data types
print(type(address))     # <class 'str'> # 'address' is an object of class str
print(type(number))      # <class 'int'> # 'number' is an object of class int
print(type(is_active))   # <class 'bool'> # 'is_active' is an object of class bool
print(type(avg))         # <class 'float'> # 'avg' is an object of class float


# -----------------------------
# String object and methods
# -----------------------------

word = "           luminarch Technolab Technohub             "

# 'word' is an object of class str
# Methods like upper(), casefold(), find(), etc. belong to the str class


"""
Simplified view of the str class (not actual implementation):

class str:
    def casefold(self):
        pass

    def capitalize(self):
        # converts the first character of the string to uppercase and the rest to lowercase
        pass

    def index(self, substr):
        # Return index of substr; raise ValueError if not found
        pass
        
    s = "hello world"

    print(index(s, "world"))   # 6
    print(index(s, "lo"))      # 3
    print(index(s, "x"))       # raises ValueError

    def find(self, substr):
        # Return first index of substr; return -1 if not found
        pass

    def rfind(self, substr):
        # Return last index of substr; return -1 if not found
        pass

    def count(self, substr):
        # Return number of occurrences of substr
        pass
    
    def isalpha():
        # return true if str object is an alphabet otherwise false
        pass
        
    def isdigit():
        # return true if str object is an digit otherwise false
        pass
    
    def isalnum():
        # return true if str object is an alphanumeric otherwise false
        pass
        
    def startswith(self,prefix):
        # return true if str starts with prefix otherwise false
        pass

    def endswith(self,suffix):
        # return true if str ends with suffix otherwise false
        pass
        
    def strip(self):
        # remove space from left and right ends
        pass
        
    def lstrip(self)

    def rstrip(self)
"""



# -----------------------------
# String method usage
# -----------------------------

print(word.upper())          # Convert all characters to uppercase
print(word.casefold())       # Case-insensitive lowercase conversion

print(word.index("lu"))      # Index of "lu" from the left; raises ValueError if not found
print(word.find("lu"))       # Index of "lu" from the left; returns -1 if not found
print(word.rfind("ch"))      # Index of "ch" from the right; returns -1 if not found
print(word.count("Tech"))    # Number of times "Tech" appears
print(word.isalpha())    # Returns True if all characters are letters and string is not empty

print(word.isdigit())    # Returns True if all characters are digits and string is not empty

print(word.isalnum())    # Returns True if all characters are letters or digits and string is not empty

print(word.startswith("lu"))
print(word.endswith("hub"))
print(word.strip()) # word = "           luminarch Technolab Technohub             " output: luminarch Technolab Technohub 

text = "hello world"

# text[0] = "p" #can not update

new_string = text.capitalize() # text variable untouched 

print(new_string) 


word_name = "\tluminar technolab\n"


new_word = word_name.lstrip()
new_word = new_word.rstrip()

print(new_word)

print(dir(list))


